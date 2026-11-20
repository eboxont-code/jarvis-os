// This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe. This plugin does not use the GPU.
import { execFile } from "node:child_process";
import { homedir } from "node:os";
import path from "node:path";

const usage = "Use /workspacefile docx|pdf|xlsx|pptx Title | content. For Excel, supply CSV rows on separate lines.";
const runtime = path.join(homedir(), ".openclaw", "local-productivity");

function createFile(request) {
  return new Promise((resolve, reject) => {
    const child = execFile(path.join(runtime, "Scripts", "python.exe"),
      [path.join(runtime, "office-server.py"), "--chat-file"],
      { timeout: 60000, windowsHide: true, encoding: "utf8" },
      (error, stdout) => {
        if (error) return reject(error);
        try {
          const output = path.resolve(JSON.parse(stdout).path);
          const allowed = path.resolve(homedir(), ".openclaw", "media", "outbound");
          if (path.dirname(output) !== allowed || !/^workspace-[a-f0-9]{32}\.(docx|xlsx|pdf|pptx)$/.test(path.basename(output))) {
            throw new Error("Unexpected output file");
          }
          resolve(output);
        } catch (err) { reject(err); }
      });
    child.stdin.on("error", reject);
    child.stdin.end(JSON.stringify(request), "utf8");
  });
}

export default {
  id: "workspace-files",
  name: "Workspace files",
  register(api) {
    api.registerTool({
      name: "workspace_create_file",
      description: "Create a local attachment for the current request. Use CSV rows for Excel, one slide for PowerPoint, or paragraphs for Word and PDF.",
      parameters: {
        type: "object",
        properties: {
          format: { type: "string", enum: ["docx", "pdf", "xlsx", "pptx"] },
          title: { type: "string", minLength: 1, maxLength: 200 },
          body: { type: "string", minLength: 1, maxLength: 32000 }
        },
        additionalProperties: false,
        required: ["format", "title", "body"]
      },
      async execute(_toolCallId, request) {
        const output = await createFile(request);
        return { content: [{ type: "text", text: "Attach this file to the reply:\nMEDIA:" + output.replaceAll("\\", "/") }], details: { format: request.format } };
      }
    });
    api.registerCommand({
      name: "workspacefile",
      description: "Create a Word, PDF, Excel or PowerPoint attachment in OpenClaw Chat.",
      acceptsArgs: true,
      requireAuth: true,
      handler: async (ctx) => {
        if (ctx.channel !== "webchat") return { text: "Open your private OpenClaw Chat to use this command." };
        const args = (ctx.args || "").trim();
        const match = /^(docx|pdf|xlsx|pptx)\s+([^|\n]{1,200})\s*\|\s*([\s\S]+)$/i.exec(args);
        if (!match || args.length > 32000) return { text: usage };
        const [, kind, title, body] = match;
        try {
          const output = await createFile({format: kind.toLowerCase(), title: title.trim(), body});
          return { text: title.trim(), mediaUrl: output };
        } catch { return { text: "File creation failed. Check the local-office Python environment and retry with a smaller document." }; }
      }
    });
  }
};
