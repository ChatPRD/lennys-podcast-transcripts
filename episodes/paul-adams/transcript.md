---
guest: Paul Adams
title: What AI means for your product strategy | Paul Adams (CPO of Intercom)
youtube_url: https://www.youtube.com/watch?v=R-Geamq9xc0
video_id: R-Geamq9xc0
description: 'Paul Adams is the longtime chief product officer at Intercom, where
  he leads the product management, product design, data science, and research teams.
  Before Intercom, Paul was the global head...

  '
duration_seconds: 4981.0
duration: '1:23:01'
view_count: 25212
channel: Lenny's Podcast
keywords:
- growth
- onboarding
- roadmap
- user research
- iteration
- a/b testing
- experimentation
- analytics
- pricing
- monetization
- revenue
- hiring
- culture
- leadership
- management
---

# What AI means for your product strategy | Paul Adams (CPO of Intercom)

## Transcript

Paul Adams (00:00:00):
This is a meteor coming towards you. This is going to radically transform society. And I think if people don't explore AI properly, it will leave them behind. I'd start with the thing your product does. "What's the core premise behind it? Why do people use it? What problem does it solve for them?" That kind of thing. So, go back to basics. And then ask, "Can AI do that?" And for a lot, the answer is going to be, "Yes, it can." For some it might be, "It can partially do it." And then, maybe for others, "It can't do that, at least not yet." And then, for some of it'll be replacement, AI would replace, it'll just do it. And, in other places, it'll be augmentation. It'll augment. It'll help people. But yeah, I think that you've got to match your product, and what AI can do, and what it will be able to do, and then ask yourself, "Okay, what are we going to do?"

Lenny (00:00:52):
Today my guest is Paul Adams. Paul is chief product officer at Intercom, a role that he's held for over 10 years. Prior to this role, he was global head of brand design at Facebook, a user researcher at Google, a product designer at Dyson, and his first job was an automotive interior designer. In our conversation, Paul shares some amazing stories of failure, including the story of him giving a huge presentation where he froze on stage and had to walk off. And what he learned from these experiences of failure. We then get deep into how to think about AI as a part of your product strategy, including a ton of great examples from Intercom's experience going all in on AI. Paul also shares some of his favorite frameworks, and product lessons, and so much more.

(00:01:34):
This is the first recording I've ever done not from my home studio, instead from a hotel room. So, this is a fun experiment for us all. With that, I bring you Paul Adams after a short word from our sponsors. This episode is brought to you by Eppo. Eppo is a next generation A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features. And Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does. When I was at Airbnb, one of the things that I loved most was our experimentation platform, where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more with advanced statistical methods that can help you shave weeks off experiment time and accessible UI for diving deeper into performance and out-of-the box reporting that helps you avoid annoying prolonged analytic cycles.

(00:02:40):
Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny and 10X your experiment velocity. That's getE-P-P-O.com/lenny. This episode is brought to you by Hex. If you're a data person, you probably have to jump between different tools to run queries, build visualizations, write Python, and send around a lot of screenshots and CSV files. Hex brings everything together. Its powerful notebook UI lets you analyze data in SQL, Python, or no-code in any combination and work together with live multiplayer and version control.

(00:03:29):
And now, Hex's AI tools can generate queries and code, create visualizations, and even kickstart a whole analysis for you all from natural language prompts. It's like having an analytics copilot built right into where you're already doing your work. Then, when you're ready to share, you can use Hex's drag and drop app builder to configure beautiful reports or dashboards that anyone can use. Join the hundreds of data teams like Notion, AllTrails, Loom, Mixpanel, and Algolia using Hex every day to make their work more impactful. Sign up today at hex.tech/lenny to get a 60-day free trial of the Hex team plan. That's hex.tech/lenny. Paul, thank you so much for being here and welcome to the podcast.

Paul Adams (00:04:14):
Thanks, Lenny. Nice to be here.

Lenny (00:04:15):
It's nice to have you here. I've heard so many good things about you from so many different people, so I'm really happy that we're finally doing this. Also, you have an Irish accent, which is always a boost for ratings in my experience, so thank you for bringing that with you here.

Paul Adams (00:04:26):
Yeah, that's nice to hear.

Lenny (00:04:28):
I wanted to start with a couple stories. So the first is your story of giving a keynote at Cannes. Can you share what happened there?

Paul Adams (00:04:38):
Yeah, some things that happened in work are very memorable at the time and they don't really scar you. This goes in the book that have scarred for life. Yeah, it's good. Long story short, I was at Facebook just over a decade ago. Loved it at the time. I think it was a great place to be at the time. And, basically San Francisco, I did a lot of talks for Facebook internally and externally. Facebook had a keynote slot, always had a keynote slot at Cannes, the world's biggest advertising festival. And, the year prior, Zuck had been interviewed. He was the speaker, he'd been interviewed. He'd gotten a hard time on privacy. It didn't go well as well as they'd hoped.

(00:05:14):
So, the next year they asked me to do it. Maybe it was the Irish accent that made the offer come my way. And, yeah, I got out and spun a stage, the world's biggest advertising stage. And, I'd say, I was three, four minutes into the talk, a very similar talk when I'd given lots of times. And, I just froze. I couldn't remember what I was supposed to say. It was the first ever time in my life I'd rehearsed the talk word for word. Usually, I have talking points, and things get mixed around, and it's informal. This was media trained, "Do not say the wrong thing." Kind of talk. And I just could not remember what to say. I had some version of a panic attack, walked off-stage, I was still mic'd up, cursed. Everyone started laughing. I was like, "Geez, are they laughing at me? Oh my God, this is..."

(00:06:06):
But, I managed to turn it around, I walked back out. I'd been disarmed internally in my head. And, the most of it went well. And I was famous that night. Out in Cannes afterwards on whatever the sea front, it's just like rose everywhere. And yeah, I was famous and infamous for my performance.

Lenny (00:06:26):
I feel like you lived the worst nightmare that everybody has when they're thinking about giving a talk. And, I think what's interesting is you survived. And, I think that's a really interesting lesson is you could freeze in front of thousands of people, walk off-stage, and then it works out okay.

Paul Adams (00:06:43):
Yeah. And it all happened organically, I guess, or very naturally. But yeah, ever since then, every time I walk out onto a conference talk stage, still today, I have this tiny doubt in the back of my head. It's never happened since. But yeah, I think you have to go with it with these things, when life throws you these, whatever, curveballs you have got to adapt and it's not that big a deal. None of these things are that big a deal, at the end of the day. You move on and live and learn. So yeah, but I still hope it doesn't happen again.

Lenny (00:07:15):
I also hate public speaking and I always fear this is exactly what's going to happen to me. And so, I think this is nice to hear, that even when the worst possible thing basically happens, things can survive.

Paul Adams (00:07:27):
You can turn it around. Yeah.

Lenny (00:07:29):
A second area I wanted to hear from is your time at Google. And, there's a couple products you worked on at Google. Both of them were not what you'd call big successes. And then, there's a transition to Facebook, which was also messy. Can you just share a couple stories from that time?

Paul Adams (00:07:45):
Yeah. Similar to the walking on stage thing, you live and learn. And, I was at Google for four years now and I was at Facebook for two and a half years or so. And, in both of those companies, this is at the height of... The social tech wave was at its peak. Google were very afraid of the existential threat posed by Facebook. Facebook were very confident they could pull off some new social advertising unit that would be an AdWords or something like that, that would destroy Google's revenue, eat them from the inside out. And so, being there at the time was fascinating and moving to the new companies. At Google, I worked on a lot of failed social projects, like you mentioned. Google Buzz, Google Ventilator, Google Plus. I think, a lot of the motivation for those projects came from a place of fear. It didn't come from a place of, "Let's make a great product for people. Let's really understand the things people struggle with when communicating with family and friends. Let's really, really try and create something wonderful." It came from a place of fear.

(00:08:47):
And so, during those times, I learned I think how not to lead in places. And by the way, I should say, at the time in Google, there was other things happening that were amazing, like Google were building Google Maps, an incredible product. One of my favorite products. I think one of the best products ever made. They were building Android. I was in the mobile team and the mobile apps team at the time, the Android came out. So, they can make an incredibly good product. So, I just happened to be in the social side, which wasn't as good. And, yeah, Google Buzz is a privacy disaster, and Google Plus is similar.

(00:09:24):
And so, halfway through I'd published research about groups and I'd done a ton of research. An interesting side note there is, at the time, I was working in the UX team as a researcher, I was been asked to do a lot of tactical research, like usability study type stuff, like can people use these products? And, I ended up doing a lot of formative research as well in the same session. So, I'd say to the team, "Hey, I'll do the research. I'll answer your questions. But also, I'm going to do this other thing, and I'm going to take 20 minutes doing that." And so, what we used to do is, what I used to do with people was map out their social network, all the people in it, their family, their friends, how they communicate. We'd map on all the channels, we'd talk about what worked well, what didn't. And, we did this with dozens and dozens of people over the course of maybe 18 months. And the same pattern emerged every single time, which was, people need way better ways to communicate with small groups of family and friends.

(00:10:17):
And I look back now and go like, "WhatsApp." Or it may be iMessage if everyone's on Apple. But, really obvious in hindsight. But at the time, not obvious. And so, we tried to build a product around that called Google Plus. But, again, it came from the wrong place. And so, halfway through, the research that I've done, all this research had been made public through a conference talk. And, Facebook noticed, got in touch, one thing led to another, and I left and joined Facebook, which was an amazing thing for me, personally.

(00:10:51):
Facebook was an amazing place at the time and exciting. And they were trying to do things for the other reasons, the good reasons. "Okay, let's build an amazing product for people."

Lenny (00:11:01):
And this was during Google Plus being built, you basically shifted.

Paul Adams (00:11:04):
Yeah, midway, I'm stressed to even tell you about it. The project hadn't been launched, it was still under wraps. It was highly confidential. Google had done a lot of things at the time that were the first for them. I don't know if they've done them since. But things like, everyone worked in Google Plus was sent to a different building. That building had a different key card. If you didn't work in Google Plus you could not get in. All sorts of counter-cultural things at the time. And, as a result, there was a lot of antagonism internally for Google Plus. And so, when I left in the middle of the project, leaving with all of the plans in my head to the enemy, some people saw me as a traitor, understandably. Other people thought I was enlightened, too fancy you talked to. But it was the right thing for me to do. But at the time, it was a hard thing to do.

Lenny (00:11:56):
I know there's also a lot of scrutiny in what you took with you and the process.

Paul Adams (00:12:01):
Yeah, when I left, Google assumed that I was one of the spies. I was quarantined. I told them I was leaving. They forensically analyzed my laptop, all sorts of stuff like that. So, it was pretty intense. Looking back, I can understand why that happened. But the root cause for me is that the project has been run from a place of competitive fear, which I don't think leads to good things.

Lenny (00:12:32):
So one of the themes through the stories you just shared is, let's say, failure is... I don't want to make it that harsh, but just things not working out. And, I'm curious as a product leader, how important you think that is for people to go through, if you think that's something that is almost a good thing? And, I guess just is there anything there that you find helpful as a coach, as a mentor, as two people that are trying to become basically you?

Paul Adams (00:12:58):
Very, very. It still is. It still is. I've personally failed so many times. There are two stories and the Google one is long deep tentacles. They're two stories. I failed a ton of times. I remember, when I was at Facebook I was very happy. And, I knew Eoghan and Des, the co-founders of Intercom. And, they were trying to persuade me to join Intercom. We were like, it was a 10-person company at the time. But, Eoghan said something to me at that time which has stuck with me ever since. He said, "At Facebook, you can design the product. But at Intercom, you can design the company." And, that was extremely appealing to me, a great pitch. He's like, "Just design the company with us that you want to work in."

(00:13:41):
And so, part of that was a company that embraces failure, that says it's okay to try things. I'm a big believer in big bets, high risk, high reward. I don't get as excited about incremental things. No, I haven't said that. There's of course a place for that too, especially as companies get bigger. But, I get excited about big bets. And if you make big bets, you're going to get a lot of it wrong. So a lot of the principles that we built here at Intercom are in building software.

(00:14:09):
We have a principle called Ship to Learn. And, we've actually changed it since. It's over on the wall here. Ship fast, ship early, ship often is what it says now. You say Ship to Learn. Ship fast, ship early, ship often. So, in that idea is the idea of failure. It's not going to go right. And, it's going to go wrong more often than not. But if you ship early, and fast, and learn fast, you can change fast, and you can improve fast. And, that's the culture that we, as much as possible, try to embrace and teach people. But it's much easier said than done.

Lenny (00:14:43):
Yeah. Especially when you're in the moment like, "God dammit. Everything's going to fall apart. I really messed this one up."

Paul Adams (00:14:48):
Yeah. And there's a trade-off with quality that people really struggle with. We've high standards of ourselves. A lot of Intercom comes from a design founder background. We value the craft a lot. We never want to be embarrassed by what we ship. So there's a real tension there, a real trade-off, where people have these high standards, which we encourage. We encourage them to ship fast, and learn, and make mistakes. It's a constant tension that we're navigating.

Lenny (00:15:17):
Speaking of taking big bets and going all in, I know there's been a huge shift at Intercom to move towards AI and embrace AI. And so, maybe just to start broadly, I'm curious just what are some of your broader insights or surprises so far in how you've thought about AI and how you think AI will integrate into product and product strategy?

Paul Adams (00:15:39):
What day that ChatGPT launch? November 29th, I think, last year. Ever since that day, I literally wake up every day thinking about AI pretty much. And, I read as much as possible and still feel like I'm way behind in it. I think, for me, when I talk to you about AI, people typically fall into one of two camps. You're either all in, really truly all in. This is a meteor coming towards you. This is bigger than mobile as a technology shift, as big as the internet. Maybe it's bigger than the internet itself as a technology shift, the way it'll shape society. So I'm all in. I've gone over the hill or whatever. I'm over the other side. And so, there's people in that camp.

(00:16:23):
And then, I think there's people in another camp, which is, "I've heard this before. It's hype. Last year was crypto. It was Web3. None of those things worked out. There was the metaverse." So, there's definitely I think a lot of skepticism or maybe cynicism around it. And I don't understand why. The other things didn't really pan out. The metaverse is coming back. And, I'm trying to remember, there's the law where you have the hype, and then the trough of disillusionment, and then you come out the other side.

Lenny (00:16:54):
Yeah, that little curve.

Paul Adams (00:16:55):
Yeah. And I think that's where a lot of people might be, where there was so much hype, it was so noisy, and still is a little bit so noisy that you tune it out a little bit. And, I think, some people have fallen into that camp. I'm all in in the other camp. This is going to radically transform society and it blows my mind even seeing new types of things that come out, like ChatGPT Vision just came out recently, and just seeing the things that people can do with it. And we're just scratching the surface still. So, we're all in, for sure.

Lenny (00:17:31):
Awesome. I want to unpack that. But, I think there's also this camp of people that like, "Yes, something big is happening. I just don't have the time to understand, to build, to play around." What have you found and/or what advice would you share to people that are just like, "I want to go deeper down this rabbit hole. I just don't know where to start, because I have so much work to do already and this isn't a side thing."

Paul Adams (00:17:53):
The advice I have for people, and the advice I have for myself, I'm in that too, I wake up every day to too many emails, and Slack chats, and people knocking on my door, and my desk, and all things. So, this is a challenge for me too. You just have to take the time. There's just no other way for me. And that to me doesn't mean... It's about priorities. It doesn't mean that you need to work crazy hours. I don't believe in working crazy hours. I don't know what hours I work. I don't know, 50 hours a week maybe. I think, beyond that, you start to make bad decisions and things like that. You get tired. And you need to live the rest of your life. You got to put it into your day. Whether that's setting aside dedicated time to read.

(00:18:33):
Reading is the thing. You got to read. You got to stay up to date, and you got to play with things, and try things. If you don't have ChatGPT... If you don't have a... I can't remember if it's a pro licenser, whatever, but if you haven't upgraded to get access to things like GPT for Vision, where you can take photos and you have the mobile app. And I was going out for dinner last Friday night with my wife. I try not to take work to dinner with my wife. But, I wanted to try it. And, I took some photos of her food. And, you can do all sorts of crazy stuff, like tell you how healthy the meal is or whatever.

Lenny (00:19:07):
Oh, wow.

Paul Adams (00:19:07):
Anyway. You got to try it. You just got to try it. So, my advice people is, you've got to try it. You've got to set aside the time, or it'll pass you by. It does remind me the mobile wave about a decade ago. Again, I was at Google at the time, I was working on the mobile team. So I guess, it was my job to stay on top of things. But, at that time, some companies like Facebook went all in on it, maybe a bit late, but they eventually made the brave decision. I think if people don't explore AI properly, it will leave them behind.

Lenny (00:19:38):
It reminds me, I think, at Facebook, Zuck, and also Airbnb, Brian did this, is he said, "Any mocks you show me for new product designs have to be in a mobile app or on a mobile web. They can no longer be desktop for now."

Paul Adams (00:19:50):
Right. Yeah. Same with Facebook. Yeah, that's right.

Lenny (00:19:54):
I guess, do you think that that's the way to approach this is as a leader, just, "Everything you bring me needs to have some AI component." That sounds probably not like a good idea, but is there something that you're thinking about, or have done of just convincing people this is where you want to spend your time?

Paul Adams (00:20:05):
Yeah, it's harder, for sure. It's harder, because-

Lenny (00:20:08):
You don't want to force it.

Paul Adams (00:20:09):
... Yeah, a lot of the tech is invisible. We have a machine learning team we've had on here for a long time, so we've been working in this space for quite some time. But, it's funny, even if you go back 18 months, I think if I was on your podcast 18 months ago and you said to me like, "Hey, what do you think about AI?" I would've said something like, "It's not real. Machine learning's real, let's talk about that." So, things change, and my perception of it's changed. But a lot of the improvements are behind the scenes. They're with large language models or different types of things people are building in the background of infrastructure.

(00:20:43):
So I don't know what it looks like to design mobile mock-ups that are AI mock-ups. But I do think that people need to start really thinking strategically. Maybe it's just not a mock-up stage, but start to think really strategically about their product and whether it's in the line of the media, or it's coming or not. It's not everything is. And if so, for some I think they require a foundational strategic change. Others, it might be less so. But, I think that's actually the head space that I think people need to be in.

Lenny (00:21:17):
Can you impact that further? What does that look like to really think deeply about whether your product is in the way of the meteor?

Paul Adams (00:21:25):
You can get sidetracked by the technology, for sure. And I do. I just mentioned, hey, going out for dinner and taking a photo of my food. You can get sidetracked by the tech and some of it's really cool. I wouldn't start there. I'd start with the thing your product does. What's the core premise behind it? Why do people use it? What problem does it solve for them? That kind of thing. And then, ask the question. So go back to basics. "Okay, what is my product for? And why do people love it?' And then ask, "Can AI do that?" And for a lot the answer's going to be, "Yes, it can." For some, it might be, "It can partially do it." And then, maybe for others, "It can't do that, at least not yet."

(00:22:07):
So you're going to need to map what your product does against what AI can do. And AI can do a lot. It can write. I'll give you a list. It can write, it can summarize, it can summarize text, it can write text, it can answer queries, it can find facts, it can scan text, it can scan images. It can listen to your voice and repeat it. It can take actions. That's the next big thing coming. It can take actions, actually do things. It could like, I mean, "Hey AI. Whatever the AI is called. "Change my flight to Tuesday." Right? It can do things like that.

(00:22:46):
And so, it can do a lot of things. It can build rules. So, I think any product that has any workflow in it, which is almost all B2B SaaS products, any product that has multimedia in it, they're in the media line or whatever. I don't don't know if this metaphor is working. But, the media is coming and they're in its path. And so, for a lot of these products that you just need to look at what AI can do. And then, for some of it'll be replacement. AI would replace, it'll just do it. And, in other places it'll be augmentation. It'll augment. It'll help people as the copilot ideas that are going around. But yeah, I think that you've got to map your product, and what AI can do, and what it will be able to do, and then ask yourself, "Okay, what are we going to do?"

Lenny (00:23:33):
Is there an example of that at Intercom or a different company of, "Here's a problem we're trying to solve? Oh, AI can actually do this fully for us."

Paul Adams (00:23:40):
Oh, yeah. I'll give you Intercom first. Again, this date, I think it was November 29th, etched in our head. We have Fergal who was our head of machine learning. And, Fergal just turns around that day and he's like... Okay, I think he tweeted something actually. He had a tweet that day that was like, "This is it. This is the time. This is the moment. This is the before after." I actually often talk about people... because this is a framework I have, before, after moments. This is a before after moment. That was before. And that is after. And everything has changed. So, we literally ripped up our strategy almost entirely, and started again, from first principles and said, "Okay, why do people use Intercom?" Intercom is a customer support product. And then, very soon after that, Sam Altman, who's the founder and head of OpenAI, said, "Hey, one of the first industries that's going to be disrupted is customer service." We're like, "Yep."

(00:24:35):
So we did. We totally changed how we think, how we work, and we just went heads down and built a product called Fin. We built other things first actually. Fin came later, now that I think about it. But we went all in on it. It was a little bit of a bet the farm mindset. So we've done it. I think other companies like Google and Bard have to do it, and maybe they're a little bit slow, but it's so early in this tech cycle that, I think, they're fine. So yeah, we did. It was hard, but we had to do it.

Lenny (00:25:13):
Can you share briefly what Finn is just for folks that aren't familiar?

Paul Adams (00:25:16):
Fin, first and foremost, is an AI chatbot. So, if you think about customer service, people have questions for a business, and historically, that was mostly email, and phone, and mostly ticketing based. You'd file a ticket, a lot of do not reply email, and so on. And then, came along conversational customer support, which is just basic messaging, like WhatsApp or iMessage, like I mentioned earlier. Now, there's bot first experiences and Fin is an AI chatbot, AI first, chatbot first. So the first line of defense for a customer support team is Finn, not a person. And so, it fundamentally changes. The results we've seen with Fin are mind blowing. Our biggest challenge is actually trying to help customer support teams think about organizational change.

(00:26:05):
The tech is way ahead. It's actually people wrapping their heads around what this means for the role, the teams, loads of cool stuff, like new types of jobs for people, like conversation designers, a job we have where you design the conversations that Fin does or managers. So anyway, that's what Fin is. Fin has expanded. So, Fin is now also in our Intercom inbox. They've placed a people answer queries, customers support queries, and now Fin's in there too, helping the support reps. Suggesting answers for them to use, or helping them rephrase things. So, it's now augmenting people as well as answering questions by itself.

Lenny (00:26:46):
I think you're one of the few companies that has pivoted fully into AI. And, I think there's a lot of lessons here about how team structures might change, product strategy, priorities, things like that. So I'm curious just to unpack a couple more things here. First of all, what impact have you seen after going all in and going in this direction?

Paul Adams (00:27:05):
It's very early, honestly, to be able to answer that properly. And it depends what you measure as success. So, again, there's a lot of hype and buzz with AI. So, if you're measuring it by interest, it's a huge success. Our target customer is customer support. Our customer support manager leader. And so, they're very curious. They're like, "Does it actually work?" Again, back to the earlier thing of there's so much hype, there's a bit of skepticism around it. "Does it actually work? Is it as good as a person?" And in customer support, people who tend to work in that role are typically very high empathy, care a lot about people. And so, they're like, "But is it as good as a person? Is it nice, friendly? Does it understand humanity?" And so, a lot of curiosity, and a lot of interests, and a lot of people trying it.

(00:27:57):
We have some customers who are hugely successful with it. They can answer up to 50, 60, 70% of their inbound questions with Fin. So we've some customers who see huge success. But it's early. And so, has it transformed our business financially? Not yet. I think, all fast-growing startups... If you think of AI Intercom as, I guess, a new startup, even though we're 900 people, the growth curve, you're looking for this exponential curve, as opposed to big public company linear growth curve. With the exponential one, it takes a while. The first year or two years is the bottom of that. And so, I think we're still in the trying to figure out exactly what's going on, trying to talk to educate people. But, we have enough evidence to believe it's the future for sure.

Lenny (00:28:53):
Are there any examples of either this product or other instances of AI just blowing your mind where you're just like, "Wow, I never imagined it would be this good"?

Paul Adams (00:29:02):
I go back to that before after thing. So, the first version of ChatGPT was a before, after, where we we've been working, like I said, in this space, we've had a machine learning team for a long time. The way our machine learning thing worked before ChatGPT was that there was not a manual setup. A customer support manager would have to orchestrate the bot, and teach it what to say, and just a lot of orchestration, a lot of teaching it. And then, ChatGPT showed up and it's like, "Oh, it can do it by itself." It gets it wrong sometimes. So, do people get the question wrong too? It's as good as a person nearly for a lot of these basic things. So that blew my mind. And then, that was, "Oh, it can answer questions." But then, you're like, it can reason.

(00:29:45):
There's actually a debate about whether is this reasoning or deduction. But, it can work things out. And, I'm not one for going down into these really philosophical things. I'm like, "We just need to build. Let's go back, build the product." Or whatever. But it can work things out. And that blew my mind. And, we fed ChatGPT and other companies too, we played with other LLMs, like Entropik and so on, it can work things out. And that was mind-blowing. Then you can see it doing things, like writing code. And I was like, "Wow, it's really good at writing code. What does that mean?" And then, you start thinking, here at Intercom we have a one to five ratio. So a PM has about five engineers on a team. And you're looking at this thing writing code and you're like, "What happens next? Do we need as many engineers or will their role change? And they'll start doing different types of things like reviewing code instead of writing code?"

(00:30:41):
So that blew my mind. And then, the visual stuff, like I mentioned earlier, I think the visual thing was bigger than the original one. It can parse imagery, and it can help you see the world. You take a photo of your bike and say, "Hey, what's wrong?" And It'll tell you what's wrong, how to fix it. You can be traveling, take photos of stuff. It's in a different language. It's etched in stone on a 12th century cathedral. You're like, "What does that say?" And it'll tell you what it says. It's just like how to do that. This is what I'm actually repeating most to people these days, here in Ireland, if you want to be a radiologist, so study X-rays and tell people what's wrong, and so on, and forth, it's seven years training to learn that skill. So, seven years to be a radiologist, and then you're just into the job. AI, it seems it's already better at it. So, it's already better at it, and it can ingest every X-ray ever made. No human can ever read, and think about, and synthesize every X-ray ever made.

(00:31:45):
So, of course it's better. And then, you're like, "Okay, what happens now?" I guess, the whole job changes. Radiologists will not take x-ray. Well, I guess they might take them. But, they won't analyze them, for sure. They'll look at what AI says, check that it's right, and then it's bedside manner time. Tell the patient, maybe tell them what course. So the job just fundamentally changes. And by the way, that could be amazing. Here in Ireland, we have long queues for hospitals, epic waiting lists for people getting X-rays. So, this is a really good thing possibly for people. Here's the craziest one I have. AI can listen to your voice and copy it, so it can say things and it sounds exactly like you and it's really, really good. Almost in distinguishable. You're like, "That sounds like Paul." And so, I mentioned the Metaverse earlier. I don't know if you saw Zuck talks to Lex [inaudible 00:32:35]. See that?

Lenny (00:32:35):
Yep.

Paul Adams (00:32:35):
So that was my first, "Oh." For people who haven't seen it, they met in the Metaverse, I think, or some virtual world.

Lenny (00:32:42):
It was a black room.

Paul Adams (00:32:44):
In a black room. Yeah. And, the tech has come on so they can analyze your face and build a 3D model. It's really good, really, really close. So, you can imagine, that's going to get better. Based on the trajectory of that technology, it's going to get better. And so, the voice thing and the face thing means both of those things are almost indistinguishable from a real person. And, AI will be able to ingest all the things people say and do. And, when people die, it'll be able to replicate that person. And so, there's an afterlife, hey, your parent dies and you can still talk to them. And, that could be the weirdest thing. Maybe it's not good for people. I don't know. But, that tech is just around the corner. And the AI can answer your questions, mind-blowing. It's mind-blowing.

Lenny (00:33:35):
There's actually a Black Mirror episode with that same premise, where-

Paul Adams (00:33:38):
That's right.

Lenny (00:33:39):
... Yeah. And I don't think it ended well.

Paul Adams (00:33:41):
No.

Lenny (00:33:43):
Be careful.

Paul Adams (00:33:44):
For sure. For sure. Yeah, I think, the [inaudible 00:33:48] and the voice translation thing is another one. I can't remember. Maybe it's in Mission Impossible, where it can take a voice, translate it, and translate it in real-time. And this tech is, again, just here, where if I was a native Spanish speaker and couldn't speak English, you and I could still have this podcast. Your voice would be translated in Spanish in real-time for me. It's, again, mind-blowing.

Lenny (00:34:10):
We're actually working on dubbing/translating podcast episodes, which is all done through AI, where it figures out what you're saying, makes it Spanish, and then also changes your lips to match. And, we're trying to launch a couple of those. And that's actually very AI-based. Yeah.

Paul Adams (00:34:25):
That's cool. That's really cool.

Lenny (00:34:27):
You mentioned that your ENG team might change your thinking, because AI can make them much more efficient and work differently. I'm curious what you've seen actually change on your team, either using AI-ish tools, or just building AI products. What do you think is most different? And I'm curious from the perspective of a team that's trying to think about integrating AI and starting to lean into AI, what have you seen most change and should change?

Paul Adams (00:34:52):
Ultimately, you need really great machine learning engineers. That's where it starts. And if you don't have that, then you're going to find it hard to build truly, really, truly great things. So, what OpenAI provide, and what Entropik provide, and Claude, they provide an amazing technology, but you got to build on top of it. If you really want something brilliant, you got to build on top of it. So, we adapted what they build for customer support. Maybe someday we need to go build our own LLM that's just for customer support. Maybe. I don't know where that will all go. And maybe everyone will have their own LLM for every single business. I don't really know, to be honest. Maybe these companies will provide specialized LLMs. But anyway, that's the first thing. And, of course, these people are in high demand. So, you need to invest in building out that function, I think. Really invest in building out the function.

(00:35:46):
So that's what we've been doing. Our ML team's way bigger than it was and way bigger than it ever has been at Intercom. And then, it forks. So, some projects are very heavy on that ML team and it needs them. But other projects are more front end, like the inbox stuff I mentioned earlier, where we have Fin and Fin is working, we've built the underlying technology. Now it's a question of if you have a human support person answering questions in the inbox, that's a natural chat conversational interface, pretty straightforward. What happens when there's now an AI assistant in there? How do they talk? And what do they do? And when do they interject? And how do you represent that in the user experience that feels natural? So that's a really hard design problem.

(00:36:32):
So, saying back into like, okay, we've a product team that's a product manager, a product designer, maybe three, four, maybe five engineers, and they're getting help from the machine learning team. So, we now have both setups. And increasingly, we can do more with the latter, more teams who can build on the foundational technology that we've been building over the last 12 months or so. So that's one thing. I think a second thing that comes to mind is not to think about it as bolted on. I think some people are still in that camp.

(00:37:08):
Again, I'll go back to the mobile thing. There's just so many direct parallels with it. Like I said earlier, at Google, I worked in the mobile apps team. I worked on mobile Gmail, mobile docs, and it was the mobile team. And we were in London. We're like, "Hey, we're the mobile team in London." And meanwhile, over in Mountainview in California, no one cared. It's was like, "You're 20 people. We're 200. No one uses this stuff on a phone." And again, a lot of skepticism. "No one's going to write docs on the phone. Seriously? They're going to write a full document on a phone, are you crazy?" So, don't do that. We're trying not to do that. Don't bolt it on. Don't be like, "Oh, we'll have a bunch of AI people..." And we do have some specialists. But generally speaking, we're trying to have everyone learn about it.

Lenny (00:37:57):
Interesting. So, I'm curious just specifically what that looks like, don't bolt it on. The idea there is don't just have a site team that's like, "They're the AI team. They're going to add AI to all this stuff." You're finding and lesson is integrated into every product team.

Paul Adams (00:38:10):
And we're still early there. We're still early. So, what we're trying not to do is have the AI inbox team, and they're the only people who work on AI features in the inbox. I think it's much better to have everyone learn about it. By the way, I'm a big believer in generalists, a big, big believer in... I guess, my background is jack of all trades master of none. That's probably how I describe myself. I've worked as a researcher, designer, PM. And so, I believe in generalists, and so I believe in setting teams up that way. And, yes, specialists matters at times. Machine learning for sure is a deep specialism. And in Intercom, we generally, in engineering too, much prefer people who learn new things, whether it's a new coding language, or framework, or how to design AI interfaces, or whatever, get more people being able to do it.

Lenny (00:39:05):
I feel like, again, your company is a little bit of living in the future, where a lot of companies are going to get to once they realize, "Oh shit. We really need to get big here." Or they're already working on it. I'm curious if there's other maybe pitfalls you ran into that you think people should try to avoid and something you could share there, or just any other lessons about making this transition that you think might be useful to other people.

Paul Adams (00:39:27):
Yeah, what I've mentioned so far, don't bolt it on. Stay up-to-date. I mentioned earlier, read, read. I feel like I'm behind all the time. It's moving so fast.

Lenny (00:39:36):
What are you reading? What do you find is most interesting and informative for reading about what's happening in AI?

Paul Adams (00:39:42):
I'd love to tell you that it's incredibly structured. I have a great reading list that I got to read every Sunday morning. It's pretty random. I'm on Twitter, which is now called X, of course, a lot. I follow some people on Twitter. I actually use the recommended feed in Twitter a lot. I think, because I interact and look at a lot of AI, I get to see a lot more. So I do that and I do it deliberately to try and generate more stuff. I'll search Twitter as well. There's loads of cool stuff there. There's some newsletters as well and some people I follow.

Lenny (00:40:12):
Any newsletters you could call out that you think are most interesting?

Paul Adams (00:40:16):
Yeah, Matt Rickard is one guy who talks a lot about AI. The blogs of companies too. OpenAI have a pretty good blog, and they write papers, and summarize them.

Lenny (00:40:27):
Cool. If there's any other ones you think of, either people on Twitter to follow or newsletters, email me after, and then we'll add them to the show notes.

Paul Adams (00:40:34):
Yeah, perfect. Yeah, yeah, there definitely is. I'll dig them out. Your question earlier, how do you do it? You just try. Try book out half an hour and just go deep for half an hour, and then bookmark a few things, come back to them. Like everyone, you could be so busy, so many distractions, you just got to have to set aside time.

Lenny (00:40:50):
Are there any other tools or apps that you find really helpful? Sounds like ChatGPT is at the center of how you play around with it. Is there anything else that you find really interesting?

Paul Adams (00:40:59):
I'll try other things like Bard. For example, Bard is Google's AI search engine. Rewind is another fascinating company. I think it's rewind.ai. Rewind is basically augmented AI for your memory. So, install it on your local machine, and it captures everything, and remembers everything. It's all local, so there's no privacy issues. And, you got to try these things to understand whether it's any good, or useful, or where's the boundaries, and how does it work, and so on. So, I'm a believer in that type of thing.

Lenny (00:41:35):
This episode is brought to you by HelpBar by Chameleon, the free in-app universal search solution built for SaaS. Your help content lives outside your app and is scattered in many places forcing users to waste time hunting for answers. HelpBar solves this, it delivers answers directly inside your app and eliminates context switching. Users can search or ask questions to get AI generated answers and lists of the most relevant documentation from all of your help sources, including your knowledge base, docs, blog, and video libraries. You can also use HelpBar to navigate your app and launch actions, such as scheduling a meeting or viewing an interactive demo.

(00:42:13):
The best products today use Command K for in-app search and navigation. HelpBar makes that readily available within your app without engineering or new code. Give users a faster and more delightful self-serve experience that reduces friction and increases in-app engagement. Upgrade your user experience with this modern component and supercharge your product-LED motion. Sign up for HelpBar today. It's free and easy to set up in minutes. Check it out at helpbar.ai/lenny, that's helpbar.ai/lenny. When you started rolling out AI and leaning into this direction, did you run into any big challenges or hurdles organizationally, or personal interests, or opinions? I don't know. Is there anything you ran into that was a big stumbling block and something you had to get over?

Paul Adams (00:43:00):
Yeah, Intercom is full of diverse opinions about things. And, I think with AI, I'm all in. I'm leaning forward. The media is coming. I'm sold. I'm way past that point. Also, no one knows. No one knows. And so, a lot of the time, when we talk internally, the strong buy-in from Eoghan, our co-founder and CEO, Des co-founder, like me, like a lot of the senior leadership team we're in all in camp. And so, that helps a lot. Of course, if you're senior leadership team in the company are all in, of course, then it trickles down. But equally, some of the hurdles have been like, "Why are you all in?" And I'm like, "An educated guess. A hunch."

(00:43:51):
The part of business strategy and product strategy that, it's just hard. It's like taste. People talk about product taste, "Who has product taste?" And a lot of it is, it's judgment based on experience. That's all I can say. I don't know. For me, personally, I don't know, I lived through the mobile thing pretty closely, having worked at Google on mobile. I lived through that phase. So, I can see the same type of thing happening now with bigger. So I'm using that experience to go all in.

(00:44:23):
But it's a challenge for some people, because they don't have that context, or they disagree with it. We have a lot of debate here about the future. Fergal, I mentioned earlier, gave myself and a few other product leaders and Des he gave us a... I don't know, is it a pitch or what? A play? I don't know, about how maybe all of our roadmap with AI is wrong. I don't know if you are familiar with the Horizons framework of Horizon 1, 2, and 3.

Lenny (00:44:54):
Mm-hmm. Yeah. Amazon.

Paul Adams (00:44:56):
Yeah. So, Horizon 1 is the medium short to medium term, next 12 months, 12 to 18 months. Horizon 2 being like, "Hey, what's happening?" Whatever, 18 to 36 months out. Or, I think, people use different timeframes, different Horizons. Anyway. We're in Horizon 1 land. We're like, "Yeah, and the next year we're going to do this." And he's like, "Yeah, but two years from now, if this path plays out, everything we're doing now is going to be irrelevant and useless." And you're like, "Oh, okay." And so, those discussions happen. And, the level of ambiguity is off the charts. So, a lot of the challenges have been navigating that ambiguity and helping people get the conviction I have without drying out voices of alternative voices and opinions, which are often valid too.

Lenny (00:45:53):
What does help people get that conviction? Is it just showing them examples of, "Here's something." "Wow, look at this thing. This is unreal." And, I think, partly what helps, I imagine, is the market you're in seems like such a clear opportunity for AI, feels like an easier pitch than maybe a lot of other markets.

Paul Adams (00:46:09):
Yeah, that's true. For sure. That's true. Yeah, showing people is definitely the easiest way. I think customer support is definitely... Like I said, [inaudible 00:46:20], number one, customer support. So you're like, "Okay, I guess we should adapt." Adapt or die is our mantra. Adapt or die. I think that there are other industries where they're on the same journey, it's just not as obvious. So for example, reporting software, Tableau or any reporting product, how do they work? Well, they're the typical read, write app, build dashboards, filtering, querying, hardcore querying, query database, get some numbers, show it in a UI. A lot of thought and care goes into how you present that data to people. The different types of charts that are appropriate help people make good decisions ultimately.

(00:47:04):
I think, again, this is hand wave, who knows. Maybe that's all done dead now. And, the reporting product of the future is just a box, and the box just goes to the database, and the box is just, "Who was our best salesman last year January? Okay. Who was our top performing representative in January? Lenny." The report product to the future might look like that. And so, project management tools is another one. There's a bunch of products that I think are just outside the most obvious customer support one. And yet, equally ripe for a newcomer to come with a completely different paradigm and potentially take over.

Lenny (00:47:45):
I like that this connects back to your very first point about trying to think about where AI integrates is. Think about what problem are you solving as a company. For example, Tableau, helping people visualize data. And then, the question is, can AI just do this for you? And in that case, oh, and maybe you can. And that gives you basically a whole strategy of like, "Okay, how do we actually do that with AI?"

Paul Adams (00:48:06):
Yeah. And, I don't know if the reporting thing will play out that way. But, if you're a Tableau type company, you've tons of designers who design dashboards, and filters, and querying type workflow. What do they do? The UI is the box. So, it's really hard to get into your head like, "We must..." If you have conviction that we must change really hard.

Lenny (00:48:33):
Maybe one last question here. For team members learning and starting to work within this realm, is there anything you find helpful to get them ramped up, other than the advice you've already shared, which is just read a lot of stuff, watch Twitter/X, subscribe to these newsletters, and then just try it?

Paul Adams (00:48:49):
I also try and read things that say it's all a load of crap. So, it's very easy... I've been guilty of this many times. Back to the mistakes you've made. I've been guilty of this many times, where I've jumped on a bandwagon and it was all wrong. And the older I get... The Web3 thing, I'm like, "I don't even know what Web3 is." Crypto, I never bought crypto. Maybe I'm wrong about that. But, I'm not a bandwagon jumper. But, maybe might've been when I was earlier. And I try these days to read the alternative opinion. People who are skeptical or think it's bad. A lot of people think this is terrible for humanity. This technology is going to eat us alive. So, I try and balance my optimism. I'm a delusively optimistic thinker, so I try and balance that with a negativity, I guess.

Lenny (00:49:50):
That's really good advice.

Paul Adams (00:49:51):
Yeah.

Lenny (00:49:52):
Is there anything else in this realm that you think might be useful to share before we shift to a different topic?

Paul Adams (00:49:58):
Oh, yeah. The other thing is, don't be afraid. I think people are a bit afraid of it. And, for example, if I started walking around our office here saying, "Hey, I think we need two engineers per team going forward." That's probably not really a good idea to do that. And I think in reality that's not going to be how it plays out. I just feel like there's loads of great studies over the years about how people don't end up losing jobs, the jobs get moved around. And also, for customer support, for example, it's a high attrition job. So, people saying, "Hey, everyone's going to lose their job. A bot's going to take over." It's like, maybe some of that will happen. But probably to attrition, as in someone quit and just didn't get back-filled. So, the doomsday scenarios that I don't think would play out as much. But, for sure, it's easy to be afraid of it. And, I think you have to lean into it.

Lenny (00:50:54):
I love that. Okay, I want to chat about frameworks. You have a lot of interesting frameworks you've put out there. So, maybe we do a rapid fire through a number of frameworks that you've worked with and find useful. And, you actually mentioned this before and after, which I hadn't heard about. What's the general idea to that concept?

Paul Adams (00:51:14):
Before, after is literally that simple, I think. We've a rebrand at the moment happening, and that'll be a before, after moment. We're redesigning our pricing. And then, the day that pricing goes live, that would be a before, after, because nothing's the same. And so, we need to go back out and talk to people again. I'm a big believer in talking. You got to talk to customers, it's the only way. You've got to talk, talk, talk, learn, learn, learn. Don't take with the safe face value, go deeper. And so, a lot of these before, after moments, once you've passed, yeah, into the after you got to start learning, "Were we right? Were we wrong? What happened? What do people think?"

Lenny (00:51:54):
Can you talk more about this pricing learning/mistake you shared? What do you think you did wrong? What happened there?

Paul Adams (00:52:00):
We had a principle called align price to value. By the way, I think, pricing is incredibly difficult. A lot of the design team who work in pricing here, I say to them, it's one of the hardest design problems I know. I think onboarding is another one. Onboarding people into a product is also. People are like, "Oh hey, you just design a few steps and it's pretty easy. People will follow the steps." Again, deceptively difficult to design great onboarding.

(00:52:30):
So, I think pricing is deceptively difficult. But we had a principle around allowing price to value. People should pay based on the amount of value they get in the product, easy to say and incredibly hard to do. Value is subjective. The price, for some person they get 10 units of value. I think that's about $5. Someone else is like, "I'd pay $5,000 for those 10 units of value." So, the biggest mistake was a lot of mistakes compounded. And, this is an area where I think we were risk averse. We've ended up with too many pricing models. We've built on top of old competitive mistakes. And, it took a brave decision to say, "We're going to start again."

Lenny (00:53:18):
Wow, this feels like it could be a solo episode, just talking through your pricing lessons and journey. Maybe just is there a nugget of wisdom you could share for someone that's trying to think about pricing right now based on your experience?

Paul Adams (00:53:31):
Number one thing I would say is keep it simple. Keep it simple. It's so tempting to... With us, for example, a lot of SaaS products have add-ons, where you're like, "Hey, we built X and that's 10 bucks." Or 100,000, depends on what product you're selling. "We built X and that's the price of X. Hey, we've just built Y. Y is awesome and it's a new thing you can do, and it unlocks all these new capabilities. People shouldn't get that for free, because it's a new thing that didn't have. So let's charge more for Y, but that doesn't really work with the other... Okay, let's look at an add-on. Oh yeah, cool. People just add on." But then, later, now you've got people who have the add-on, and people who don't, and then you're like, "Add another thing." And so, we've added tiers, with products, tears, add-ons, tearing in the add-on. Oh my god. People can't understand their bill. So, my advice is keep it simple. Fight so hard to resist the temptation to add extra ways in which you price.

Lenny (00:54:43):
Amazing. I didn't think about going into this topic, but I'm glad that we touched on it.

Paul Adams (00:54:49):
Think I was talking about scars for life earlier. That's another scar for life.

Lenny (00:54:54):
All right. Let's keep talking about some frameworks. Another that I found that I loved is something that you call differentiation versus table stakes. What's that about?

Paul Adams (00:55:03):
It's like the Kano model, if you're familiar with that. But, it's very simple. I guess, we took the Kano model and just tried to make this really crazy simple version of it. Again, I'm a little bit allergic to things like this. I even hate myself for bringing up the Kano model. I'm allergic to people over intellectualizing frameworks. And like, "Oh, well if you've seen the new different law..." Of whatever. I'm like, "Keep things simple, practical, and pragmatic. And then, let's all, again, go back to work and start building the product, so that customers can benefit, because that's actually all that matters." And so, difference versus table stakes, very simple. I think people who adopt a product, or buy a product, or switch to a product, there's two driving forces. One is the attraction of the new solution, and that's basically differentiation. So what's different and better? But critically, what's different and better in ways that customers care about?

(00:56:00):
Again, back to all the failed projects, my lesson for a lot of these was, we were different and better in these Google projects in ways people didn't care about. All sorts of Google projects, like Google Wave was an amazingly innovative product that no one really cared about. So, be different and better in ways people care about. So that's the attraction that's like, "Oh, I want to check out that. That looks cool. I want to check that out. That looks better than what I have today." But, on the other side, there's a entry requirement or table stakes. To play the game, you got to have a certain amount of things. And so, they're table stake features. They're often very boring. They're real basic stuff, boring stuff, and easy to ignore, and easy to not build.

(00:56:44):
And again, a mistake with Intercom maybe over the years is that we were much more attracted to the differentiation and built a lot of that. So we went through different iterations of our roadmap, sometimes changing over the course of a year or two, where we were all the differentiation to realize that everyone loved it and really wanted to buy, but they couldn't, because we didn't have the basic report that they needed or we didn't have the basic permission feature that they needed. And then, the robot is built based on those... Trading off why do we need more differentiation or trading off why do we need to invest more table stakes? And so, these days, the basic Intercom today is we're 50/50 probably in terms of resources, but it has swung 70/30 in both directions at times.

(00:57:26):
The last piece about it is, I think it's really powerful to look at a roadmap or look at a proposed roadmap and ask yourself, which of these do things matters more to us, not to us actually to our customers right now? The other thing that we've talked a lot about here internally is if you're a startup and you're entering any established category, customer support for us, big established category, massive, a lot of table stakes, built up over years, decades. ServiceNow, Service Cloud, Salesforce, Zendesk, decades of table stake feature building. So to play the game, you need a lot of the table stakes, unless you have incredible differentiation. So from the early years of Intercom, people just buy us alongside Service Cloud or Zendesk. They just buy us alongside. They're like, "This Intercom thing..." We were like first modern messaging and modern UX. They were like, "We want that for our customers, alongside the big giant bag of table stakes." Because Intercom doesn't have any of those.

(00:58:26):
Then over the years, we've built the table stakes to a point where, okay, now we can fully play the game and people can switch, so they can swap Zendesk for Intercom. But it took us years to get there. And then hence, if you're a startup, you need to invest a lot more in differentiation. And then, over the years, I think you start to balance the books a bit.

Lenny (00:58:47):
I think what's interesting about this is one, it just gives you a way to think about looking at your roadmap. How much are we actually doing? And are we doing too much table stakes? Are we doing too much differentiation? So it gives you a awareness of what's happening. And I think, it's an interesting strategy as a startup like, "Do we spend years doing table stakes and then launch? Or is it go the way Intercom went, like differentiate first we'll build everything else later?" Wonder when it makes sense to go one or the other.

Paul Adams (00:59:13):
Yeah. And it probably depends on the market, different categories, and all sorts of things. Yeah.

Lenny (00:59:20):
Yeah. Awesome. Okay. The next framework is something that you call swinging the pendulum. What is that about?

Paul Adams (00:59:28):
I actually mentioned an example a bit earlier. Differentiation in table stakes was swinging the pendulum. So, swinging the pendulum means, you take a step back from everyday work life, and you make the observation that something's in an undesirable state. So, maybe it's, "Whoa, we've all the differentiation in the world, but people can't adopt the product, because we've never built any of these table stakes. It's undesirable." Or, "Oh, we've now built all these table stakes and we've not been investing in differentiation. And actually, we're not that attractive to people, because switching product is a pain. And we're not just attractive to people. Okay, so this undesirable state."

(01:00:08):
And then, so you go and fix it, but the temptation is that you over-correct. And we've done this so many times in so many domains, everything from, "Okay, we don't have enough differentiation." A year later, "Oh, wait a minute, we're missing all the table stakes. Okay, we're over there." So, product building is one, people is another one. Building out teams and people. Another big one was, I don't know, maybe five years into Intercom, we were on this high growth trajectory, really good classic startup before our pricing problems. And, we looked around and said, "None of us have done this before. I don't think that's good. Undesirable state. Do we even know what we're doing? We're just a bunch of random people. Do we know what we're doing? We need to hire some experts. We need to hire some experts. If we're going to go up market, we need market people who've done it before."

(01:01:07):
So, that was undesirable state, fix it by hiring people who've done it before. And then, we hired loads of people who've done it before, and what they did was brought the culture and ways of working of their prior company to Intercom. And so, we totally over-corrected, didn't work out in a lot of cases. In most cases, it didn't work out. Because, we weren't trying to be a bigger company, that already exists. We're trying to be us. So, I think, hiring and building teams is another where we really over-corrected to find out, "Okay, it's a balance here."

(01:01:43):
Related to hiring, one is generalists and specialists, similar theme. People who've done it before, or people who are specialized. And, we hired a bunch of specialists only to realize that they're not adaptable. And, in Intercom, we have a lot of ambiguity, and we lean into the ambiguity, and people who are highly specialized can thrive in big companies, really thrive. They're invaluable employees. But in a fluid startup-y culture with a lot of ambiguity, they can really drown, really struggle. Maybe the middle of this pendulum, landing in the middle is, "Let's hire someone who has done a bit of it and have a bit of specialism, not much, but enough to try and figure it out." So, we hire a lot of those people today.

Lenny (01:02:34):
First of all, I love all these stories of things that don't work out, because a lot of people don't like sharing these. And, this is what people want to hear, like, "Here's not everything was perfect. Here's a lot of mistakes that are made along the way." And, it feels like this framework is a result of just doing this too many times. Is the main lesson here generally avoid swinging the pendulum too far? Because sometimes, it's worth it, like in this case of AI, is like, "No, we're going all in." Or in mobile, it was worth going all in. I guess, yeah, what do you think of when I say that?

Paul Adams (01:03:04):
In talking to people about this before, sometimes the conclusion of the conversation is something like, it's the only way to do it. You actually can't do it a different way." And so, maybe the question is really, how high does the pendulum go? Versus, you got to swing it, and then it's like, how far do you swing it? And for sure, you're right. With AI, we are swinging it pretty high. Maybe I overestimated earlier, if AI is in the differentiation camp to mix the frameworks, we're still building a lot of table stakes features too, building depth into the product. And that's 50/50, I think I mentioned 50/50 earlier, so that's 50/50. So, we're not totally swinging it. It's swung, but we're also doing the other thing and balancing things out. So, I think you probably have to swing it. It reminds me to know where the boundary is, is what I was going to say.

(01:04:01):
It reminds me back to the olden days stories. I remember, at Google, privacy was really top of mind, to the point that it would block decisions, block product progress, just privacy circular conversations, so many circular conversations, and nothing ever got built or shipped. I worked on a project for a year at Google and we shipped nothing in the year, just circular conversations, which killed me at the time. So, when I went to Facebook, I realized they have a different approach to privacy. And again, I'm not advocating it's necessarily good, it certainly didn't help their brand. But, there was an idea that to know where the boundary is, you got to across it. And crossing it is painful. But, if you don't cross it, you'll never know. So if you think you're going up to the boundary and you stop before it, turns out it's actually miles over there.

(01:04:54):
So I think with a lot of this stuff, you don't really have a choice. You got to cross the boundary, feel the pain, be humble enough to realize you didn't get it right, and go again or whatever the corrective course is.

Lenny (01:05:12):
Yeah, get that pendulum off the even pivot thing that it's on. And then, let's fix that pendulum. Let's put it back.

Paul Adams (01:05:18):
Yeah.

Lenny (01:05:20):
Okay. Another framework that I read about briefly, and I love the general idea of it already, which is something that I think you call product market story fit.

Paul Adams (01:05:31):
Yeah.

Lenny (01:05:31):
What is that?

Paul Adams (01:05:33):
So yeah, with product market fit, pretty basic, well understood, very important. The way I describe product market fit is, you've got to build the right product for the right market. I think, by the way, as an aside, not enough people think about the market side of that equation. A lot of product people don't think about the market side. But for me, it's very simple. The market is the people, the problems they have, and how important the problems are to them. To have a good market, you need a lot of people with the same problem, and they need to care a lot about it. Going back to the Google social stuff, we found a lot of people with the same problem, but they didn't really care. They didn't really care. What they had was fine. So a lot of people with the same problem and a lot of energy around the problem and the product is the solution to that. The market's the who, the product's the what.

(01:06:21):
And, I don't know, in my career again, so a bunch of products that were built, there were good products in good markets, and they failed and I couldn't work it out. And eventually, I came back to this idea that... And maybe someone might say, "Paul, it's marketing. You're talking about marketing." But story, the story's wrong or the story's missing. And so, sometimes, it would be a great product in a great market explained in a convoluted way. I see that a lot. I used to see that a lot at Google again, just explained in a very complicated way over intellectualized. And, as a result, people are like, "What? What are you talking about?" You don't get their attention. And so, the story is really important, as important. And actually, sometimes you'll see not great products, certainly worse on paper... I'm trying to remember the Spotify competitor back in the day, people were like... What was the name of it?

Lenny (01:07:19):
Ordio?

Paul Adams (01:07:20):
Yeah, Ordio. Ordio was one of these where-

Lenny (01:07:20):
I like Ordio a lot.

Paul Adams (01:07:26):
... Yeah, all I've ever heard about Ordio was, "Amazing product."

Lenny (01:07:29):
Mm-hmm.

Paul Adams (01:07:30):
It's failed. And why did it fail? Spotify and Ordio had the same market. They were solving the same set of problems. Ordio was arguably the better product at the time. I don't know if that's true, but arguably the better. I also think Spotify's an incredible product. But, they got the story wrong. And so, again, I think, all product people, whether you're a designer, product manager, people in research, data science, need to think about the story all the time. Work of marketing, work of product marketing, and learn about how to explain the product, as much as how to build the product.

Lenny (01:08:03):
Mm-hmm. Makes me think about positioning and how important that is. And, we had April Dunford on the podcast very recently talking a lot about that.

Paul Adams (01:08:12):
Yeah. Yeah, she's excellent. Yeah, it is really, "Why are you better and can you explain why you're better?"

Lenny (01:08:21):
That's such an important point. A final area I wanted to touch on is jobs to be done. So we had the co-creator of Jobs to be Done on the podcast. We had Shyam Krishnan on the podcast. They very much disagree about how effective Jobs to be Done is. I know you guys are big on Jobs to be Done. So, what are your just general thoughts on the Jobs to be Done framework? How effective was it for you all? How do you use it? What do you find work? Doesn't work? Whatever comes up.

Paul Adams (01:08:47):
Yeah. I'll be totally honest, at the risk of finding people do this, we worked with Bob West years ago. I think Bob's a great guy. And we followed that model of Jobs to be Done more than the ODI, I think, is the other skill of thought. Anyway. I'll try say this in a simple way. We found Jobs to be Done really good. Very, very useful. But, in a very simple way... Again, back to this idea of simple frameworks, in a simple way, separately, there's so many people who spend so much of their energy debating the nuances and peculiarities of one version. Who cares? No one cares. Oh well, I don't care. They care obviously. But your customers don't care. People you're trying to build a product for don't care,. No one cares. That's a cool intellectual debate. But, for me, maybe this is too extreme. It doesn't really have any place in the work we do. We're just trying to build a great product.

(01:09:50):
And so, for us with Jobs to be Done, it was a really good way of us centering on the customer problem, focusing on not getting distracted, basing it in good solid research informed insight, that told us the thing people are trying to do. What is the thing people are trying to do? Again, energy. Do they have a lot of energy around it? Maybe the energy thing might've come from talking to Bob actually, now that I think about it. I think it did actually. I think, the idea of this idea that you need people who have a lot of energy around the problem. And you have to interview them for that most of the time to feel the energy they have. It's very easy to see if someone's apathetic versus into it.

(01:10:30):
So, we've had it pretty good. And, we invented this job stories thing by accident. I can't remember exactly what happened. But, I wrote out this way of writing a job story basically. Well, we didn't call it job stories, someone else called it that. We just, at the time, were like... I can't even remember. It was a trigger. And, anyway, we didn't even give it the thing a name, someone else named it, I think. And, I'm just like, "We're just trying to build a great product." So, we've had it really good in that way, really simple. And then, the other one that we use a lot still here is the four forces, which is this framework of Jobs to be Done. The four forces being... There's different forces when people try and switch product. And some of it's the differentiation, table stake stuff, like the attraction of the new solution, the reasons that you might not adopt it. Habits. People have anxieties.

(01:11:26):
Here's another funny story to tell you how much... The four forces is really good. Here's a funny story, I was saying earlier that Eoghan and Des were trying to convince me to leave Facebook, which I loved at the time, join and to come. They wrote out the four forces for me to join. And then, secretly, over a few beers, talked to me and fed me my anxieties. And basically worked me on the four forces. And I was like, "That is genius. That is ingenious. Maybe it's a bit... But it's ingenious." And so, the four forces is incredibly good at helping understand why people make decisions.

Lenny (01:12:07):
I love that a lot of your advice just continues to come back to, keep it simple, cut away anything that isn't necessary. And, I find the same exact thing with Jobs to be Done. I find it really useful as a framework for the podcast, the newsletter, but I think there's this endless set of processes and ways of optimizing that gets people distracted. And, often just slows everything down.

Paul Adams (01:12:28):
Yeah, yeah. And it's interesting and fun to talk about sometimes, really fascinating, unless you're an academic. But if you're working in a company that you're trying to build a software product for people to improve their lives in some small meaningful way, it doesn't matter. Just use the thing that helps you do that. That's the goal. And use the thing that helps you do that. And that's it.

Lenny (01:12:55):
With that, we've reached our very exciting lightning round. Are you ready?

Paul Adams (01:12:58):
I'm ready, yeah.

Lenny (01:13:00):
What are two or three books that you've recommended most to other people?

Paul Adams (01:13:04):
Yeah, the two books I recommend to everyone always, I have copies in my office here, It's Not How Good You Are, It's How Good You Want to Be. It's a book by Paul Arden who worked in advertising a long time ago. It's an excellent book. It shows people that you feel an unlimited potential if you think about it the right way, everyone does. The second book I recommend to everyone and buy for people and give to them is Principles by Ray Dalio. I'm a big fan of Ray Dalio. I think he's incredible. I'm a big believer in principles. A lot of us at Intercom are... I always get those two books. And they're totally different. The Paul Arden book, you can read it in 20 minutes. Principles is that thick.

Lenny (01:13:38):
What is a favorite recent movie or TV show that you really enjoyed?

Paul Adams (01:13:42):
Most recent is The Bear, which I came to late. The reason I love the show is because I think it somewhat celebrates the grind. And I think that's important. I worked in coffee shops a lot when I was younger, when I put myself through college and stuff. And, the grind is part of life, and the grind is a necessity to get things done, and make great things happen sometimes. And I like that about it. I really like that about it.

Lenny (01:14:09):
What is a favorite interview question you'd like to ask candidates?

Paul Adams (01:14:13):
Yeah, I'll give you a slightly different answer. I don't really have certain few questions for candidates. And I don't like answer question diversity. I don't like questions that rely on memory. Like, "Tell me about the last time you did X." Here's an amazing question I got given recently by Alyssa who used to work here. I had to do referral calls. So, you're interviewing someone, you want to give them the job and they've got referees, and of course, the referees they have are the best people that they've ever worked with and their favorite managers. So this question is, "What feedback will I be giving this person in their first performance review?" It's an amazing question, because the person can't dodge it. There's an answer. And, it's incredibly enlightening.

Lenny (01:14:55):
And that's a question you ask on reference calls?

Paul Adams (01:14:57):
Yeah, on reference calls.

Lenny (01:14:58):
That is such a good question. I love it.

Paul Adams (01:15:00):
Yeah, it's a amazing question. Yeah.

Lenny (01:15:02):
All right, what a gem. Thank you for sharing that. What is a favorite product you've recently discovered that you really love?

Paul Adams (01:15:09):
This is maybe cheating, but I go back to a lot of the AI products. I think ChatGPT Vision is mind-blowing. I've been playing with Rewind lately. I was a bit late to it. Des, and Kiran, and a bunch of people here, founders of Intercom, love Rewind, use it and love it. Thing's amazing. So I'm a bit late to that. But, it's just augmented memory. It's mind-blowing. So, Rewind's been fun.

Lenny (01:15:32):
And they just came out with a little audio thing that can record your actual day.

Paul Adams (01:15:36):
Yeah, I'm not so sure about that.

Lenny (01:15:39):
Yeah, got some flack.

Paul Adams (01:15:42):
Yeah.

Lenny (01:15:43):
I'm not so sure. I don't know. I don't know if it's real. It looked like not a real product when they launched in, but I think it's real.

Paul Adams (01:15:47):
And it tippy-toes into what's okay and not okay with AI. And, yeah. Yeah, it's a cool theory though, for sure.

Lenny (01:15:57):
What is a favorite life motto that you often come back to share with people, find helpful for yourself?

Paul Adams (01:16:04):
Yeah, I have a post-it on my monitor that says, "Only work on what matters most." It's on my monitor, a post-it. And it sometimes falls off, and I have to write it again. Only work on what matters most. And, it's amazing. I go into work, someone emails me, and I'm like, "Oh, God." I'm like, "Only work on what matters most." The second one related is, stop worrying about things you can't control. And so, I have two of those. And so, only working what matters most. Stop worrying about things you can't control. It just reduces the temperature. Again, life lessons learned. I sent a lot of dumb emails in my past, like, "Red Energy, oh my God, what are they thinking?" You wake up in Dublin to a San Francisco email. And you're like, "Oh god. Keyboard." And, if your monitor says these two things, you just don't do that. You just take a breath, get a coffee, come back. Does it really matter?

Lenny (01:17:02):
Beautiful. The second one, I think, I learned first from Seven Habits of Highly Effective People. Have you read that?

Paul Adams (01:17:02):
Oh, yeah.

Lenny (01:17:10):
Just think about the focus, the circle of things you can control, and then there's the circle of things you can influence, and then there's the things you have no control over. And, I find that really helpful myself. I love that you have it as a post-its. I feel like, I need to make post-its of all these lessons people share as their little mottos.

Paul Adams (01:17:26):
Yeah, the post-it on the monitor is a real life hack, I found a few years ago. Because it's dumb in a way. The posts on the monitor, it's in the way.

Lenny (01:17:34):
Wait, you actually put it on the monitor in the way of your screen?

Paul Adams (01:17:34):
Yeah, yeah.

Lenny (01:17:34):
Oh, wow.

Paul Adams (01:17:38):
It's in the bottom left, just covering the bottom. Because otherwise, if it wasn't there, I wouldn't look at. I make myself look at it.

Lenny (01:17:47):
Yeah. Wow. I haven't heard of people putting it over precious real estate on their monitor.

Paul Adams (01:17:53):
Yeah.

Lenny (01:17:53):
That works. What's the most valuable lesson your mom or your dad taught you?

Paul Adams (01:17:58):
The biggest one, again, so reductive and simple is to be nice to people. I think, being nice goes way further than people really realize. One thing that I've learned, again, the hard way through life is you have no idea what's going on in people's lives. You've no idea. People could have all sorts of really stressful, all sorts of personal stuff going on, and the reason they did the thing at work that you didn't like is because of that. And so, I try and think, "Be nice. You don't know what's going on. You might learn later. Don't act in a way you would regret." I think, being nice in life goes far further than most people give a credit for, because it's too much of a, I don't know, fluffy truism or whatever.

Lenny (01:18:54):
I 1000% resonate with that. I've been told I'm too nice and I had to become a little less nice. But, I still can't lose that. So I fully buy into that. My parents taught me a similar lesson.

Paul Adams (01:19:08):
Yeah. And sometimes it's hard. I'd never fired anyone before I joined Intercom, for example. I really did not like doing it. And, since then, I've done it quite a few times in a bunch of different circumstances, and realized it always works out for both sides. And the nicest thing to do is to do the harder thing. It's actually the nicer thing to do. People are relieved in this example. It's a nicer thing to do. So, it can be a complicated one.

Lenny (01:19:37):
I love it. Final question. You're Irish, you're based in Ireland. What is an Irish food you think people should definitely try out if they ever visit Ireland?

Paul Adams (01:19:50):
Can I cheat and say Guinness? Is that food?

Lenny (01:19:54):
Absolutely.

Paul Adams (01:19:56):
The Guinness in Ireland. People talk about this and it's true. The Guinness in Ireland is much, much better for a whole bunch of reasons. It's basically a fresh product and it's brewed here. It's the way they think about, it's like milk. Milk goes off, Guinness goes off. Guinness is older than a few days old, tends to start deteriorating. So, Guinness Ireland is amazing, because it's made here. The other thing I think that Ireland does really well is fish. Ireland has not had, by the way, the greatest reputation for culinary excellence over the years. I think Irish food in the States in particular is not good. But, the fish here is incredible. You can get incredible fish. And Ireland's obviously an island, so there's a lot of fish.

Lenny (01:20:37):
On the Guinness front, is there any way to get the good stuff not in Ireland? Or is that just you got to go?

Paul Adams (01:20:43):
No, there is actually. You just need to be near a brewery. So Guinness is brewed in Nigeria. There's a huge Guinness market in Nigeria.

Lenny (01:20:43):
I did not know that.

Paul Adams (01:20:53):
I think they actually use a different recipe, but it's brewed there. I think the brewery in the U.S. is somewhere in the east coast between New York and Eastern Canada. So, it's somewhere there. So, often, the Guinness in New York can be actually pretty good. The Guinness in San Francisco tends to be really bad. I remember talking to someone about this that works in Guinness. One of my friends, does a lot of work in Guinness. I think the boat carried the Guinness goes down through the Panama Canal back up to San Francisco. So, it's 12-weeks-old or something.

Lenny (01:21:25):
Wow. Did not think we would be learning about the travel path of Guinness from-

Paul Adams (01:21:31):
At least this is what I've heard. The Guinness has so many myths, you just don't really know what's true. But, these are the stories I've been told.

Lenny (01:21:38):
... Amazing. Paul, you are awesome. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out? And how can listeners be useful to you?

Paul Adams (01:21:46):
I have a handle, it's everywhere. Basically, P-A-D-D-A-Y. It's Paddy with an extra A. So, P-A-D-D-A-Y. That's everywhere. So, paddy@gmail, @Paddy. It's my handle everywhere. So, that's where you can find me. I'd love people to reach out to me, right, genuinely learn. I'd love to hear from people who think my AI talk is nonsense and it's more a crypto Web3. Or, I'd love to hear people who have alternative opinions and challenge mine. That's how I like to learn and get better. So, if people have those opinions, I'd love to hear them. I'd love to talk to them.

Lenny (01:22:25):
Be careful what you wish for. The YouTube comments are always a spicy place. We'll see what we see. Awesome, Paul. Thank you again so much for being here.

Paul Adams (01:22:33):
Yeah, thanks Lenny. I really appreciate it.

Lenny (01:22:35):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

