def send_message(prompt, llm='claude'):
    try:
        if llm=='claude':
            from sys import exit as sys_exit
            import time
            from claude_api.client import (
                ClaudeAPIClient,
                SendMessageResponse,
            )
            from claude_api.session import SessionData, get_session_data
            from claude_api.errors import ClaudeAPIError, MessageRateLimitError, OverloadError
            from setup import get_credential
            user_agent = get_credential("claude_user_agent")
            cookie_header = get_credential("claude_cookie_header")
            cookie_header = cookie_header.replace('…', '...')

            for i in range(5):
                try:
                    session = SessionData(cookie_header, user_agent)

                    client = ClaudeAPIClient(session, timeout=240)

                    chat_id = client.create_chat()
                    if not chat_id:
                        print("\nMessage limit hit, cannot create chat...")
                        sys_exit(1)
                    try:
                        res: SendMessageResponse = client.send_message(
                            chat_id, f"{txt}"
                        )

                    except ClaudeAPIError as e:
                        if isinstance(e, MessageRateLimitError):
                            print(f"\nMessage limit hit, resets at {e.reset_date}")
                            print(f"\n{e.sleep_sec} seconds left until -> {e.reset_timestamp}")
                        elif isinstance(e, OverloadError):
                            print(f"\nOverloaded error: {e}")
                        else:
                            print(f"\nGot unknown Claude error: {e}")
                    finally:
                        client.delete_chat(chat_id)
                    return res.answer
                except RuntimeError as r:
                    print(r+'Were going to try again')
                    time.sleep(60)
    except:
        llm='hugchat'
    if llm=='hugchat':
        from hugchat import hugchat
        from hugchat.login import Login
        email= get_credential('hugchat_email')
        passwd = get_credential('hugchat_password')
        sign = Login(email, passwd)
        cookies = sign.login()
        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        query_result = chatbot.chat(prompt)
        return str(query_result) # or query_result.text or query_result["text"]
if __name__ == '__main__':
    story = """Me and my fiancee have been together for  6 years in next march we never been in a major fight or even had any disagreements i always thought she's going to be the one we've been engaged for 1 year recently she's been offered post graduation studies for one year in USA by her college while paying half of the cost only due to her high GPA you can name it scholarship we both come from above middle class families not extremely rich but some where between i wasn't agreeing or comfortable with her being gone for a full year in foreign country i wanted to go with her but 
due to my work i can't leave for extended period of time (i have my own company) so all rely on me being there, she kept pushing and say how this will be awsome for her career and how i can visit her and how she won't be able to do this after our marriage (we were planning for marrying in a year give or take) 
i finally agreed so she can't regret or think i hold her back in our future 
She left to USA in about 2 month and half ago but there something wasn't right i knew two weeks before her leaving that her bestie 25F is going with her i found out that she applied for the studies after her knowing my fiancee are going and she even paid full cost due to her poor GPA (both went to the same college) but she wasn't going to miss the chance to go to USA and have fun as she described
I became very uncomfortable and told my fiancee that i don't want her to travel with her cause she is bad influence and always partying and can't keep her self out of trouble this led to our first huge fight and how she already paid the cost of the trip and such things i offered to pay her back what she paid but she refused and said that i shouldn't be worried about her hanging out with her friend cause she will only focus on her studies i agreed and kept my mind busy from thinking about any dark thoughts
Keep in mind her friend was engaged and cheated on her fiance that one of many reasons i don't like her and when we are out in a group she act 
like pick me girl around me and sometime flirt and my naive fiancee say that how her bestie is and it's joking around and it's normal i just don't get comfortable around her she's always expose things my fiancee did in the past even before our relationship so she can make my fiancee looks like a bad person and then say that she didn't knew that i didn't know about what she said
First month of my fiancee being in the USA went smooth and we talked everyday despite the time zone differences then she started to get cold or don't answer immediately and blame it on the studies i understood that she must be under stress but at the same time she wasn't answering her 
friend was posting ig stories of her going out and partying and stuff and when I asked my fiancee did she go out with her she denied i told her i don't mind her having fun but she should be careful around her friend she assured me that she doesn't hangout with her that much except in the morning cause they share same place i told her that I trust her and that i belive her and that  I just miss her we returned to talk everyday and things returned to be normal again but three weeks ago i received a message from her bestie saying we should talk i asked her what is it she said that she doesn't like how my fiancee behaving recently i told her how so she said that she is going out alot mostly with her but my fiancee told her not to tell me so i won't be worried and she told me that she is talking and flirt with guys when they hit on her and she keep on a conversation my heart dropped i told her is she cheating on me she said no i just thought you guys were fighting or something i told her we 
are just fine and I'll talk to her about this she told me don't mention that i told you anything i agreed
Next day i FaceTime my fiancee and asked her what is wrong and if there anything she wish to tell me she told me no i just love you and miss you and this kind of talk i told her i love her so much but if she was keeping things behind my back i won't ever forgive her and she knows that 
i hate lying she got mad and told me she's tired and going to sleep and that she only busy studying i apologized and told her that her not answering my calls make me worry about her and we talked for a bit before hangup
Her friend for the past three weeks keep me updated without even me asking but there was nothing major and most of the time i didn't even reply to her friend'"""
    txt = f"""generate me an interesting title for this story so i can put it as a caption for my tiktok video, make it SEO optimized and add 10 hashtags to boost views, here's story: {story}"""

    response = send_message(txt, llm='claude')
    title = response.split('"')[1]
    hashtags = []
    for i in range(len(response)):
        hashtag = ''
        if response[i] == '#':
            for c in range(i, len(response)):
                if response[c] == ' ' or response[c] == '\n':
                    break
                hashtag += response[c]
            hashtags.append(hashtag)
                
    print(title)
    print(hashtags)