def mail(to,from,title,message,filepath,)
    # PRG1: ライブラリ設定
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from pathlib import Path

    # PRG2: メール情報の設定
        #宛先のメールアドレス
    to_email = to
        #送信するメールアドレス
    from_email = from
    cc_mail = ''
        #件名
    mail_title = title
        #本文
    message = message

    # PRG3: MIMEマルチパートでメールを作成
    msg = MIMEMultipart()
    msg['Subject'] = mail_title
    msg['To'] = to_email
    msg['From'] = from_email
    msg['cc'] = cc_mail
    msg.attach(MIMEText(message))

    # PRG4: 添付ファイルの読み込み
    filepath =Path(filepath)
    filename = filepath.stem
    with open(filepath, 'rb') as f:
        attach = MIMEApplication(f.read())
    attach.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attach)

    # PRG5: サーバを指定してメールを送信する
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    # -----------------ここから-----------------
    smtp_password = 'Gmailで取得したアプリパスワード'
    # -----------------ここまで-----------------

    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(from_email, smtp_password)
    server.send_message(msg)
    server.quit()
