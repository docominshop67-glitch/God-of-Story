@echo off
chcp 65001 > nul
title Docomin - GitHub Push
echo ========================================================
echo   🚀 ระบบอัปโหลด Docomin ขึ้น GitHub อัตโนมัติ
echo ========================================================
echo.
echo กำลังตรวจสอบ Git Remote:
git remote -v
echo.
echo --------------------------------------------------------
echo กำลัง Push ข้อมูลขึ้น https://github.com/antiny817-crypto/docomin ...
echo --------------------------------------------------------
git push -u origin master
if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo  🎉 อัปโหลดขึ้น GitHub สำเร็จเรียบร้อยแล้ว!
    echo  URL: https://github.com/antiny817-crypto/docomin
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo  ⚠️ การส่งข้อมูลขึ้น GitHub ต้องการการยืนยันตัวตน (Authentication)
    echo  หากระบบขอ Username / Password ให้กรอก:
    echo  - Username: antiny817-crypto
    echo  - Password: ให้ใส่ Personal Access Token (PAT) ของ GitHub
    echo ========================================================
)
echo.
pause
