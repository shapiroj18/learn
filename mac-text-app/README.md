## mac-text-app
Bash script that can be used to send scheduled text messages on a mac.  
   * In the script set `MESSAGE` to whatever message you want to send
   * In the script set `RECIPIENT` to whoever you want to send (by name)
   * In your terminal open cron with `crontab -e` and add an entry such as `* * * * * cd ~/path_to_enclosing_folder && ./mac_texts.sh` to schedule running your bash script on a schedule with [crontab syntax](https://crontab.guru/)