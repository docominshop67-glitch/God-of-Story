const localtunnel = require('localtunnel');
const fs = require('fs');

(async () => {
    try {
        console.log("Opening public localtunnel...");
        const tunnel = await localtunnel({ port: 5000 });
        console.log("=========================================");
        console.log("PUBLIC ONLINE URL:", tunnel.url);
        console.log("=========================================");
        
        fs.writeFileSync("PUBLIC_URL.txt", tunnel.url, "utf-8");
        fs.writeFileSync("C:/Users/ACER/Desktop/คลิกเปิดเว็บ_Docomin_ออนไลน์.url", `[InternetShortcut]\nURL=${tunnel.url}\n`, "utf-8");
        
        tunnel.on('close', () => {
            console.log("Tunnel closed");
        });
        
        tunnel.on('error', (err) => {
            console.error("Tunnel error:", err);
        });
    } catch (err) {
        console.error("Failed to start tunnel:", err);
    }
})();
