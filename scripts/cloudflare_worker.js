/*
 * P-Reinforce Cloud Bridge (Always-On Ingestion) - KST VERSION
 * Supports: Text (UTF-8 safe), Photos, Documents
 */

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('P-Reinforce Cloud Bridge is Running (KST Mode)', { status: 200 });
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response('Invalid JSON', { status: 400 });
    }

    if (!body.message) return new Response('OK');

    const msg = body.message;
    const chatId = String(msg.chat.id);

    if (!env.ALLOWED_CHAT_ID || !env.BOT_TOKEN || !env.GITHUB_REPO || !env.GITHUB_PAT) {
      return new Response('Worker environment variables are missing', { status: 500 });
    }

    if (chatId !== String(env.ALLOWED_CHAT_ID)) {
      return new Response('Unauthorized Access', { status: 403 });
    }

    // --- 한국 시간(KST) 계산 로직 ---
    const now = new Date();
    const kstOffset = 9 * 60 * 60 * 1000; // 9 hours in ms
    const kstDate = new Date(now.getTime() + kstOffset);
    
    const dateStr = kstDate.toISOString().split('T')[0];
    const timeStr = kstDate.toISOString().split('T')[1].replace(/:/g, '').split('.')[0];
    // ----------------------------

    let fileName = "";
    let base64Content = "";

    if (msg.text) {
      fileName = `00_Raw/${dateStr}/${timeStr}_Telegram_Note.md`;
      const rawText = `---\ntype: telegram\ncreated: ${kstDate.toISOString()}\n---\n\n${msg.text}`;
      base64Content = utob(rawText);
    } 
    else if (msg.photo) {
      const fileId = msg.photo[msg.photo.length - 1].file_id;
      fileName = `00_Raw/${dateStr}/${timeStr}_Image.jpg`;
      base64Content = await getTelegramFileBase64(fileId, env.BOT_TOKEN);
    }
    else if (msg.document) {
      const fileId = msg.document.file_id;
      const origName = msg.document.file_name || "document.bin";
      fileName = `00_Raw/${dateStr}/${timeStr}_${origName}`;
      base64Content = await getTelegramFileBase64(fileId, env.BOT_TOKEN);
    }

    if (fileName && base64Content) {
      const success = await commitToGithub(fileName, base64Content, env);
      if (success) {
        await sendTelegramMessage(`✅ 지식 수집 완료 (KST): ${fileName.split('/').pop()}`, env.BOT_TOKEN, env.ALLOWED_CHAT_ID);
        return new Response('Success', { status: 200 });
      } else {
        await sendTelegramMessage(`❌ GitHub 업로드 실패`, env.BOT_TOKEN, env.ALLOWED_CHAT_ID);
        return new Response('GitHub API Error', { status: 500 });
      }
    }

    return new Response('OK', { status: 200 });
  }
};

function utob(str) {
  return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function(match, p1) {
    return String.fromCharCode('0x' + p1);
  }));
}

async function getTelegramFileBase64(fileId, botToken) {
  const fileResp = await fetch(`https://api.telegram.org/bot${botToken}/getFile?file_id=${fileId}`);
  const fileJson = await fileResp.json();
  if (!fileJson.ok) return null;

  const filePath = fileJson.result.file_path;
  const rawFile = await fetch(`https://api.telegram.org/file/bot${botToken}/${filePath}`);
  const arrayBuffer = await rawFile.arrayBuffer();

  let binary = '';
  const bytes = new Uint8Array(arrayBuffer);
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

async function commitToGithub(path, base64Content, env) {
  const ghUrl = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/${path}`;

  const response = await fetch(ghUrl, {
    method: 'PUT',
    headers: {
      'Authorization': `token ${env.GITHUB_PAT}`,
      'User-Agent': 'P-Reinforce-Cloud-Bridge',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: `reinforce: remote upload (${path})`,
      content: base64Content
    })
  });

  return response.ok;
}

async function sendTelegramMessage(text, botToken, chatId) {
  const url = `https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(text)}`;
  await fetch(url);
}
