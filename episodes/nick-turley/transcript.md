---
guest: Nick Turley
title: 'Inside ChatGPT: The fastest growing product in history | Nick Turley (OpenAI)'
youtube_url: https://www.youtube.com/watch?v=ixY2PvQJ0To
video_id: ixY2PvQJ0To
description: Nick Turley is Head of ChatGPT, the fastest-growing product in history,
  with 700 million weekly active users (10% of the world's population). He was part
  of the original hackathon team that built ChatGPT.
duration_seconds: 5738.0
duration: '1:35:38'
view_count: 184717
channel: Lenny's Podcast
keywords:
- growth
- retention
- metrics
- iteration
- experimentation
- analytics
- pricing
- monetization
- subscription
- revenue
- hiring
- team building
- culture
- management
- strategy
---

# Inside ChatGPT: The fastest growing product in history | Nick Turley (OpenAI)

## Transcript

Lenny Rachitsky (00:00:00):
You were a product leader at Dropbox, then Instacart. Now, you're the PM of the most consequential product in history.

Nick Turley (00:00:05):
I didn't know what I would do here because it was a research lab. My first task was I fix the blinds, or something like that.

Lenny Rachitsky (00:00:11):
When someone offers you a rocket ship, don't ask which seat.

Nick Turley (00:00:13):
We set out to build a super assistant. It was supposed to be a hackathon code base.

Lenny Rachitsky (00:00:16):
What was it called before?

Nick Turley (00:00:17):
It was going to be Chat with GPT-3.5 because we really didn't think it was going to be a successful product.

Lenny Rachitsky (00:00:21):
And then Sam Altman is just like, "Hey, let me tweet about it."

Nick Turley (00:00:23):
This is a pattern with AI, you won't know what to polish until after you ship. My dream is that we ship daily.

Lenny Rachitsky (00:00:28):
By the time people hear this, they're going to have their hands on GPT-5.

Nick Turley (00:00:31):
About 10% of the world population uses every week. With scale comes responsibility. It just feels a little bit more alive, a bit more human. This model has taste.

Lenny Rachitsky (00:00:38):
Kevin Weil, your CPO, said to ask you about this principle of, "Is it maximally accelerated?"

Nick Turley (00:00:43):
I just really want to jump to the punchline, "Why can't we do this now?" I always felt like part of my role here is to just set the pace and the resting heartbeat.

Lenny Rachitsky (00:00:49):
Everyone is always wondering, "Is Chat the future of all of this stuff?"

Nick Turley (00:00:52):
Chat was the simplest way to ship at that time. I'm baffled by how much it took off, even more baffled by how many people have copied.

Lenny Rachitsky (00:00:58):
ChatGPT is now driving more traffic to my newsletter than Twitter.

Nick Turley (00:01:02):
That is the type of capability that has been incredibly retentive. I've been really excited about what we've been doing in search.

Lenny Rachitsky (00:01:06):
Can you give us a peek into where this goes long-term?

Nick Turley (00:01:09):
ChatGPT feels a little bit like MS-DOS. We haven't built Windows yet, and it will be obvious once we do.

Lenny Rachitsky (00:01:15):
Today, my guest is Nick Turley. Nick is Head of ChatGPT at OpenAI. He joined the company three years ago, when it was still primarily a research lab. He helped come up with the idea of ChatGPT and took it from 0 to over 700 million weekly active users, billions in revenue, and arguably the most successful and impactful consumer software product in human history. Nick is incredible. He's been very much under the radar. This is the first major podcast interview that he has ever done, and you are in for a treat. We talk about all the things, including the just launched GPT-5.

(00:01:50):
A huge thank you to Kevin Weil, Claire Vo, George O'Brien, Joanne Jang, and Peter Deng for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app, or YouTube. And if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Check it out lennysnewsletter.com and click, "bundle". With that, I bring you Nick Turley.

(00:02:21):
This episode is brought to you by Orkes, the company behind open source Conductor, the orchestration platform powering modern enterprise apps and agentic workflows. Legacy automation tools can't keep pace. Siloed, low-code platforms, outdated process management, and disconnected API tooling falls short in today's event-driven, AI-powered agentic landscape. Orkes changes this. With Orkes Conductor, you gain an agentic orchestration layer that seamlessly connects humans, AI agents, APIs, microservices, and data pipelines in real time at enterprise scale, visual and code-first development, built-in compliance, observability, and rock-solid reliability, ensure workflows evolve dynamically with your needs. It's not just about automating tasks, it's orchestrating autonomous agents and complex workflows to deliver smarter outcomes faster. Whether modernizing legacy systems or scaling next-gen, AI-driven apps, Orkes accelerates your journey from idea to production. Learn more and start building at orkes.io/lenny, that's orkes.io/lenny.

(00:03:22):
This episode is brought to you by Vanta, and I am very excited to have Christina Cacioppo, CEO and co-founder of Vanta, joining me for this very short conversation.

Christina Cacioppo (00:03:31):
Great to be here. Big fan of the podcast and the newsletter.

Lenny Rachitsky (00:03:34):
Vanta is a longtime sponsor of the show, but for some of our newer listeners, what does Vanta do and who is it for?

Christina Cacioppo (00:03:41):
Sure. So we started Vanta in 2018, focused on founders, helping them start to build out their security programs and get credit for all of that hard security work with compliance certifications, like SOC 2 or ISO 27001. Today, we currently help over 9,000 companies, including some startup household names, like Atlassian, Ramp, and LangChain, start and scale their security programs, and ultimately build trust by automating compliance, centralizing GRC, and accelerating security reviews.

Lenny Rachitsky (00:04:12):
That is awesome. I know from experience that these things take a lot of time and a lot of resources, and nobody wants to spend time doing this.

Christina Cacioppo (00:04:20):
That is very much our experience, but before the company, and some extent, during it, but the idea is, with automation, with AI, with software, we are helping customers build trust with prospects and customers in an efficient way. And our joke, we started this compliance company so you don't have to.

Lenny Rachitsky (00:04:36):
We appreciate you for doing that, and you have a special discount for listeners. They can get $1,000 off Vanta at vanta.com/lenny, that's vanta.com/lenny for $1,000 off Vanta. Thanks for that, Christina.

Christina Cacioppo (00:04:50):
Thank you!

Lenny Rachitsky (00:04:55):
Nick, thank you so much for joining me, and welcome to the podcast.

Nick Turley (00:04:59):
Thanks for having me, Lenny.

Lenny Rachitsky (00:05:00):
I already had a billion questions I wanted to ask you, and then you guys decided to launch GPT-5 the week that we're recording this. So, now, I have at least 2 billion questions for you. I hope you have a lot of time. First of all, just congrats on the launch. It's coming tomorrow, the day after recording this. Just congrats. How are you feeling? I imagine this is an ungodly amount of work and stress. How are you doing?

Nick Turley (00:05:22):
It's a busy week, but we've been working on this for a while, so it also feels really good to get it out.

Lenny Rachitsky (00:05:27):
So, by the time people hear this, they're going to have their hands on GPT-5, the newest ChatGPT. What's the simplest way to just understand what this is, what it unlocks, what people can do with it? Give us the pitch.

Nick Turley (00:05:39):
I'm so excited about GPT-5. I think for most people, it's going to feel like a real step change. If you're the average ChatGPT user, and we have 700 million of them this week, you've probably been on GPT-4o for a while. You probably don't even think about the model that powers the product. And GPT-5, it just feels categorically different. I'll talk about a lot of the specifics, but at the end of the day, the vibes are good, at least we feel that way. We hope that users feel the same. And increasingly, that is the thing that I think most people notice, right? They don't look at the academic benchmarks. They don't look at evaluations. They try the model and see what it feels like. And just on that dimension alone, I'm so excited. I've been using it for a while, but it is also the smartest, most useful, and fastest frontier model that we've ever launched.

(00:06:33):
On pure SMARTs, one way to look at that is academic benchmarks on many of the standard ones, whether or not it's math, or reasoning, or just raw intelligence. This model is state of the art. I'm especially excited about its performance on coding, whether or not that's SWE-bench, which is a common benchmark, or actually front-end coding is really, really good as well, and that's an area where I feel like there's the true step change improvement in GPT-5. But really, no matter how you measure the SMARTs, it's quite remarkable, and I think people are going to feel the upgrade, especially if they weren't using o3 already.

(00:07:13):
And the second thing beyond SMARTs is it's just really useful. Coding is one axis of utility, whether or not you have coding questions or you're vibe coding an app, but it's also a really good writer. I write for a living, internally, externally. I just wrote a big blog post that we published Monday, and this thing is such an incredible editor. And compared to some of the older models, it's got taste, which I think is really exciting. And to me, that's something that is truly useful in my day-to-day. And there's a bunch of other areas, like it's state of the art on health, which is useful when you need it, but again, the thing you can't really express in use cases or data is the vibe of the model. And it just feels a little bit more alive, a bit more human in a way that is hard to articulate until you try it. So, feel good about that.

(00:08:06):
And yeah, as mentioned, it's faster. It thinks, too, just like o3 did, but you don't have to manually tell it to do that. It'll just dynamically decide to think when it needs to. And when it doesn't need to think, it just responds instantly, and that ends up feeling quite a bit faster than using o3 did. And then maybe the thing that's most exciting is that we're making it available for free, and that's one of those things that I feel like we can uniquely do at OpenAI. Because many companies, I think, if they have a subscription model like us, they would gate it behind their paid plan. And for us, if we can scale it, we will, and that just feels awesome. We did that with 4o as well. So, everyone is going to be able to try GPT-5 tomorrow, hopefully.

Lenny Rachitsky (00:08:46):
How long does something like this take? I don't know if there's a simple answer to this, but just how long have you guys been working on GPT-5?

Nick Turley (00:08:51):
We've been working on it for a while. You can view GPT-5 as a culmination of a bunch of different efforts. We had a reasoning tech, we had a more classic post-screening methodologies, and therefore, it's really hard to put a beginning on it, but it really is the end point of a bunch of different techniques that we began for a while.

Lenny Rachitsky (00:09:14):
Can you give us a peek into the vision for where ChatGPT is going, GPT in general is going? If you look at on the surface, it's been the same idea with a much smarter brain for a long time. I'm curious where this goes long-term.

Nick Turley (00:09:28):
So, to maybe back up a bit, now, you think of ChatGPT as, "Is this going to be ubiquitous product?" Again, about 10% of the world population uses every week.

Lenny Rachitsky (00:09:37):
Holy shit.

Nick Turley (00:09:39):
I think we have 5 million business customers now. It's an established category in its own right. But really, when we started, we set out to build a super assistant, that's how we talked about it at the time. In fact, the code base that we use is called SA Server. It was supposed to be a hackathon code base, but things always turn out a little bit differently. So, yeah, in some ways, that is still the vision. The reason I don't talk about it more than I do is because I think assistant is a bit limiting in terms of the mental model we're trying to create. You think of this very personified human thing, maybe utilitarian, maybe a... And frankly, having an assistant is not particularly relatable to most people, unless they're in Silicon Valley and they're a manager, or something like that. So it's imperfect.

(00:10:24):
But really, what we envision is this entity that can help you with any task, whether or not that's at home, or at work, or at school, really any context, and it's an entity that knows what you're trying to achieve. So, unlike ChatGPT today, you don't have to describe your problem in menu to detail because it already stands your overarching goals and has context on your life, et cetera. So, that's one thing that we're really excited about. The inverse of giving it more inputs on your life is giving it more action space. So, we're really excited to allow it to do, over time, what a smart, empathetic human with a computer could do for you. And I think the limit of the types of problems that you can solve for people, once you give it access to tools like that, is very, very different than what you might be able to do in a chatbot today. So, that's more outputs.

(00:11:19):
And I often think, "Okay, I'm a general intelligence. What happened if I became Lenny's intern, or something?" And I wouldn't be particularly effective despite having both of those attributes that I just mentioned, and it's because I think this idea of building a relationship with this technology is also incredibly important. So, that's maybe the third piece that I'm excited about is building a product that can truly get to know you over time. And you saw us launch some of those things with improved memory earlier this year, and that's just the beginning of what we're hoping to do so that it really feels like this is your AI. So, I don't know if supersystem is still the right exact analogy, but I think people just think of it as their AI. And I think we can put one in everyone's pocket and help them solve real problems, whether or not that's becoming healthy, whether or not that's starting a business, whether or not that's just having a second opinion on anything. There's so many different problems that you can help with people in their daily life, and that's what motivates me.

Lenny Rachitsky (00:12:16):
So an interesting between the lines that I'm reading here is the vision is for it to be an assistant for people not to replace people. It feels like a really important piece of the puzzle. Maybe just talk about that.

Nick Turley (00:12:29):
AI is really scary to people, and I understand there's decades of movies on AI that have a certain mental model baked in. And even if you just look at the technology today, everyone, I think, has this moment where the AI does something that was really deeply personal to them and you're thought, "Hey, AI can never do that." For me, it was weird music theory things where I was like, "Wow, this thing actually understands music better than I do," and that's something I'm passionate about. And so it's naturally scary. And I think the thing that's been really important to us for a long time is to build something that feels like it's helpful to you, but you're in the driver's seat, and that's even more important as the stuff becomes agentic, the feeling of being in control, and that can be small things.

(00:13:15):
We built this way of watching what the AI is doing when it's in agent mode. And it's not that you actually are going to watch it the whole time, but it gives you a mental model and makes you feel in control in the same way that, when you're in a Waymo, you get that screen, for those of you who've tried Waymo. You can see the other cars. It's not like you're going to actually watch, but it gives you the sense that you know how this thing works and what's happening, or we always check with you to confirm things. It's a little bit annoying, but it puts you in the driver's seat, which is important. And for that reason, we always view technology and the technology that we build as something that amplifies what you're capable of, rather than replacing it, and that becomes important as the deck gets more powerful.

Lenny Rachitsky (00:13:53):
Okay. So you mentioned the beginnings of ChatGPT. I was reading in a different interview. So you joined OpenAI. ChatGPT was just this internal experimental project that was basically a way to test GPT-3.5, and then Sam Altman is just like, "Hey, let me tweet about it, maybe see if people find this interesting," yada yada, yada. It's the most successful consumer product in history, I think both in growth rate in users and revenue, and just absurd. Can you give us a glimpse into that early period before it became something everyone is obsessed with?

Nick Turley (00:14:24):
Yeah. So we had decided that we wanted to do something consumer-facing, I think, right around the time that GPT-4 finished training, and it was actually mainly for a couple of reasons. We already had a product out there, which was our developer product. That's actually what I came in to help with initially, and that has been amazing for the mission. In fact, it's grown up. And now, it's the OpenAI platform with, I don't know, 4 million developers, I think. But at that time, it was early stage, and we were running into some constraints with it because there was two problems. One, you couldn't iterate very quickly because, every time you would change the model, you'd break everyone's app. So, it was really hard to try things.

(00:15:03):
And then the other thing was that it was really hard to learn because the feedback we would get was the feedback from the end user to the developer to us. So it was very disintermediated, and we were excited to make fast progress towards AGI and it just felt like we needed a more direct relationship with consumers. So we were trying to figure out where to start. And in classic OpenAI fashion, especially back then, we put together a hackathon of enthusiasts of just hacking on GPT-4 to see what awesome stuff we could create and maybe ship to users, and everyone's idea was some flavor of a super assistant. They were more specific ideas, like we had a meeting bot that would call into meetings, and the vision was maybe it would help you run the meeting over time. We had a coding tool, which full circle now, probably ahead of its time. And the challenge was that we tested those things, but every time we tested these more bespoke ideas, people wanted to use it for all this other stuff because it's just a very, very generically powerful technology.

(00:16:04):
So, after a couple of months of prototyping, we took that same crew of volunteers, and it was truly a volunteer group, right? We had someone from the supercomputing team who had built an iOS app before. We had someone on the research team who had written some backend code in their life. They were all part of this initial ChatGPT team, and we decided to ship something open-ended because we just wanted a real use case distribution. And this is a pattern with AI, I think, where you really have to ship to understand what is even possible and what people want, rather than being able to reason about that a priori. So, ChatGPT came together at the end because we just wanted the learnings as soon as we could, and we shipped it right before the holiday thinking we would come back and get the data and then wind it down. And obviously, that part turned out super differently because people really liked the product as is.

(00:16:56):
So I remember going through the motions of like, "Oh, man, dashboard is broken. Oh, wait, people are liking it. I'm sure it's just going viral and stuff is going to die down," to like, "Oh, wow, people are retaining, but I don't understand why." And then eventually, we fell into product development mode, but it was a little bit by accident.

Lenny Rachitsky (00:17:14):
Wow. I did not know that ChatGPT emerged out of a hackathon project. Definitely the most successful hackathon project.

Nick Turley (00:17:21):
I like to tell this story when we do our hackathons because I really do want people to feel like they can ship their idea, and it's certainly been true in the past, and we'll continue to make it true.

Lenny Rachitsky (00:17:32):
If you don't want to share these things, but I wonder who that team was.

Nick Turley (00:17:34):
The team is largely still around. Some of the researchers working on GPT-5, actually, were always part of the ChatGPT team. Engineers are still around. Designers are still around. I'm still here, I guess. So, yeah, you've got the team still running things, but obviously, we've grown up tremendously, and we've had to because with scale comes responsibility. And we're going to hit a billion users soon and you have to begin acting in a way that is appropriate to that scale.

Lenny Rachitsky (00:18:06):
Okay. So let me spend a little time there. So, I don't know if this is 100% true, but I believe it is that ChatGPT is the fastest growing, most successful consumer product in history. Also, the most impactful on people's lives. It feels like it's just part of the ether of society now. It's just my wife talks to it. Every question I have, I go to it, voice mode. My wife is just like, "Let me check with ChatGPT." It's just such a part of our life now, and I think it's still early. So many people don't even know what the hell is going on. Just as someone leading this, do you ever just take a moment to reflect and think about just like, "Holy shit"?

Nick Turley (00:18:45):
I have to. It's quite humbling to get to run a product like that, and I have to pinch myself very frequently, and I also have to sometimes sit back and just think, which is really hard when things are moving so quickly. I love setting a fast pace at the company, but in order to do that with confidence, I need at least one day every week that I'm entirely unplugged and I'm just thinking about what to do and process the week, et cetera.

(00:19:14):
And the other thing is I've never ever worked on a product that is so empirical in its nature where, if you don't stop, and watch, and listen to what people are doing, you're going to miss so much, both on the utility and on the risks, actually. Because normally, by the time you ship a product, you know what it's going to do. You don't know if people are going to like it, that's always empirical, but you know what it can do. And with AI, because I think so much of it is emergent, you actually really need to stop and listen after you launch something and then iterate on the things people are trying to do and on the things that aren't quite working yet. So, for that reason alone, I think it's very important to take a break and just watch what's going on.

Lenny Rachitsky (00:20:03):
Okay. So you take a day off every week... not off. Okay, that's not the right way to put it. You take a day of thinking time, deep work.

Nick Turley (00:20:12):
I need it. Yeah, yeah, yeah. And I need to hard unplug on a Saturday, or something like that. Obviously-

Lenny Rachitsky (00:20:16):
On a Saturday [inaudible 00:20:16].

Nick Turley (00:20:16):
But it's just not possible otherwise. This has been a giant marathon for three years now. Yeah.

Lenny Rachitsky (00:20:25):
Like a sprint marathon.

Nick Turley (00:20:26):
Sprint marathon, that's right, or interval training, or something. I don't know how to exactly describe the OpenAI launch cadence, but you've got to set yourself up in a way that is sustainable. Even if this wasn't AI and it didn't have the interesting attributes that I just mentioned, I think you would need to do that. But especially with AI, it's important to go watch.

Lenny Rachitsky (00:20:45):
So, along those lines, I talked to a bunch of people that work with you, that work at OpenAI. Joanne specifically said that urgency and pace are a big part of how you operate, that that's just something you find really important, to create urgency within the team constantly, even when you are the fastest growing product in history, growing like crazy. Talk about just your philosophy on the importance of pace and urgency on teams.

Nick Turley (00:21:08):
Well, it's nice of her to say that. Two things, with ChatGPT, when we decided to do it, we had been prototyping for so long and I was just like, "In 10 days, we're going to ship this thing," and we did. So, that was maybe a moment in time thing where I just really wanted to make sure that we go learn something. Ever since then, I spent so much time thinking about why ChatGPT became successful in the first place, and I think there was some element of just doing things where there was many other companies that had technology in the LLM space that just never got shipped. And I just felt like, of all the things we could optimize for, learning as fast as possible is incredibly important. So I just started rallying people around that, and that took different forms.

(00:21:55):
For a while, when we were of that size, I just ran this daily release sync and had everyone who was required to make a decision in it, and we would just talk about what to do and to pivot from yesterday, et cetera. Obviously, at some point, that doesn't scale, but I always felt like part of my role here, obviously, was to think about the direction of the product, but also to just set the pace and the resting heartbeat for our teams. And again, this is important anywhere, but it's especially important when the only way to find out what people like and what's valuable is to bring it into the external world. So, for that reason, I think it's become a superpower of OpenAI, and I'm glad that Joanne thinks that I had some part in that, but it really has taken a village.

Lenny Rachitsky (00:22:38):
I love this phrase, "the resting heart rate of your team". That's such a perfect metaphor of just the pace of being equivalent to your resting heart rate.

Nick Turley (00:22:46):
I actually learned that at Instacart, when I showed up there, because we were in the pandemic and it was all hands on deck. For a while, there was this... I think there was a company-wide stand-up because we disbanded all teams. We were just trying to keep the site up. And for me, I had been used to taking my sweet time and just thinking really hard about things, and that's important, but I really learned to hustle over there, and I think that's come in handy at OpenAI.

Lenny Rachitsky (00:23:12):
Okay. So, along these same lines, I asked Kevin Weil, your CPO, what to ask you, and he said to ask you about this principle of, "Is it maximally accelerated?" Talk about that.

Nick Turley (00:23:22):
That's funny, we have a Slack emoji, apparently, for this now because I used to say that. Now, I try to paraphrase. Sometimes, I just really want to jump to the punchline of like, "Okay, why can't we do this now?" or, "Why can't we do it tomorrow?" And I think that it's a good way to cut through a huge number of blockers with the team and just instill... especially if you come from a larger company. At some point, we started hiring people from larger tech companies. I think they're used to, "Let's check in on this in a week," or, "Let's circle back next quarter to see if we can go on the plan." And I just, as a-

Nick Turley (00:24:00):
... on the plan and I just kind of as a thought exercise, always like people asking, "Okay, if this was the most important thing and you wanted to truly maximally accelerate it, what would you do?" That doesn't mean that you go do that, but it's really a good forcing function for understanding what's critical path versus what can happen later. And I've just always felt like execution is incredibly important. These ideas, they're everywhere. Everyone's talking about a personal AI, you might've seen news on that and I really think that execution is one of the most important things in the space and this is a tool. So, it's funny that that became a meme. It's like a little pink Slack emoji that people just put on whatever they're trying to force the question.

Lenny Rachitsky (00:24:45):
I was going to ask, what theme [inaudible 00:24:47]. So, it's a little pink, is there something in there like-

Nick Turley (00:24:48):
It's a Comic Sans emoji that says, is this maximally accelerated?

Lenny Rachitsky (00:24:53):
Okay. And so, the kind of the culture there is when someone is working on something, the push is, is this maximally accelerated? Is there a way we can do this faster? Is there anything we can unblock?

Nick Turley (00:25:02):
Yeah. And we use that sparingly, right? Because it needs to be appropriate to the context. There's some things where you don't want to accelerate as quickly as possible because you kind of want process. And we're very, very deliberate on that where your process is a tool. And one of the areas where we have an immense amount of process is safety. Because A, the stakes are already really high, especially with these models, GPT-5 which is a frontier in so many different ways. But B, if you believe in the exponential, which I do and most people who work on this stuff do, you have to play practice for a time where you really, really need the process for sure, sure, sure. And that's why I think it's been really important to separate out the product development velocity, which has to be super high from, for things like frontier models, there actually needs to be a rigorous process where you red team, you work on the system card, you get external input, and then you put things out with confidence that it's gone through the right safeguards.

(00:26:02):
So, again, it's a nuanced concept, but I found it very, very useful when we needed and for everything product development, you're a dead on arrival, so it's important to get stuff out.

Lenny Rachitsky (00:26:11):
We got to open source those memes so that other teams can build on this approach.

Nick Turley (00:26:16):
Absolutely.

Lenny Rachitsky (00:26:17):
So, interestingly with ChatGPT, and it's not a surprise, but not only is it the fastest-growing, most successful consumer product ever, retention is also incredibly high. People have shared these stats that one month retention is something like 90%, six month retention is something like 80%. First of all, are these numbers accurate? What can you share there?

Nick Turley (00:26:39):
I'm obviously limited on what exactly I can share, but it is true that our retention numbers are really exciting and that is actually the thing we look at. We don't care at all how much time you spend in the product. In fact, our incentive is just to solve your problem and if you really like the product, you'll subscribe, but there's no incentive to keep you in the product for long. But we are obviously really, really happy if over the long run, three month period, et cetera, you're still using this thing. And for me, this was always the elephant in the room early on. It's like, "Hey, this may be a really cool product, but is this really the type of thing that you come back to?" And it's been incredible to not just see strong retention numbers, but just see an improvement in retention over time even as our cohorts become less of an early adopter and more the average person, so.

Lenny Rachitsky (00:27:29):
Yeah. So, that note is something that I don't think people truly understand how rare this is when a product... The cohort of users comes, tries it out and then retention over time goes down and then it comes back up, people come back to it a few months later and use it more. It's called a smiling curve, a smile curve, and that's extremely rare.

Nick Turley (00:27:48):
Yeah, yeah. Yeah. There's some smiling going on that's just on the team and I feel like have technology, some of it is not the product. I think people are actually just getting used to this technology in a really interesting way, where I find, and this is why the product needs to evolve too, that this idea of delegating to an AI, it's not natural to most people. It's not like you're going through life and figuring out what can I delegate? Certain sphere of Silicon Valley does that because they're in a self-optimization mode and they're trying to delegate everything they can. But I think for most people in the world it's actually quite unnatural. And you really have to learn, "Okay, what are my goals actually and what could another intelligence help me with?"

(00:28:26):
And I think that just takes time and people do figure it out once they've had enough time with the product. But then of course there's been tons of things that we've done in the product too, whether or not it's making the core models better, whether or not it's new capabilities like search and personalization and all that kind of stuff, or just standard growth work too, which we're starting to do. That stuff matters too, of course.

Lenny Rachitsky (00:28:49):
So, you might be answering this question already, but let me just ask it directly. People may look at this and be like, "Okay, they're building this kind of layer on top of this God-like intelligence. Of course it will grow incredibly fast and retention will be incredible. What do you guys actually doing that sits on top of the model that makes it grow so fast and retain so much?" Is there something that has worked incredibly well that has moved metrics significantly that you can share?

Nick Turley (00:29:18):
One thing we've learned, I'll answer that question in a minute, but one thing we've learned with ChatGPT is that there really is no distinction between the model and the product. The model is the product and therefore you need to iterate on it like a product. And by that I mean obviously you typically start by shipping something very open-ended, at least if you're OpenAI [inaudible 00:29:38] that's kind of a playbook. But then you really have to look at what are people trying to do? Okay, they're trying to write, they're trying to code, they're trying to get advice, they're trying to get recommendations and you need to systematically improve on those use cases. And that is pretty similar to product development work. Obviously the methodology is a bit different, but discovery is the same. You got to talk to people, you got to do data science and you got to try stuff and get feedback.

(00:30:04):
So, that's one chunk of work that we've been very consciously doing is improving the model on the use cases people care about. And there's also such thing as vibes because I'm sure you know and that's one of the things that I'm excited about in GPT-5 is that the vibes are really good. So, that too is, we have a model behavior team and they really focus on what is the personality of this model and how does it speak and talk. So, there's that kind of work. I would say that's maybe a third of the retention improvements that we see or so just roughly. And then I think another third is what I would call product research capabilities. They're research driven for sure. They have a research component, but they're really new product features or capabilities. And search is one example of that where if you remember in the olden days, maybe 20 months ago or something, you would talk to ChatGPT and it'd be like, "As of my knowledge cut off..." Or, "I can't answer that because that happened to recently," or something like that.

(00:31:00):
And that is the type of capability that has been incredibly retentive and for good reason. It just allows you to do more with the product personalization, like this idea of advanced memory where it can really get to know you over time is another example of a capability like that. I think that's another good chunk. And then the third stuff is the stuff you would do in any product and those things exist too. Not having to log in was a huge hit because it removed a ton of the friction. I think we had this intuition from the beginning, but we never got to it because we didn't have enough GPU or other constraint to really go do that. So, there's the traditional product work too. So, I often think about it as roughly a third, a third, a third, but really we're still learning and we're planning to evolve the product a ton, which is why I'm sure there's going to be new levers.

Lenny Rachitsky (00:31:52):
You mentioned something that I want to come back to real quick. You said that it was something like 10 days from Hackathon to Sam tweeting about ChatGPT being live?

Nick Turley (00:32:01):
The Hackathon happened much earlier and we were prototyping for a long time, but at some point we basically ran out of patience on trying to build something more bespoke. And again, that was mostly because people always wanted to do all this other stuff whenever we tested it. So, it was 10 days from when we decided we were going to ship to when we shipped. And the research we'd been testing for a long time, it was kind of an evolution of what we'd called instruction following, which was the idea that instead of just completing the sentence, these models could actually follow you instructions. So, if you said summarize this, it would actually do so. And the research had evolved from that into a chat format where we could do it multi-turn. So, that research took way longer than 10 days and that kind of baking in the background, but the productization of this thing was very, very fast and lots of things didn't make it in.

(00:32:50):
I remember we didn't have history, which of course was the first user feedback we got. The model had a bunch of shortcomings and it was so cool to be able to iterate on the model. The thing I just talked about, treating the model as a product was not a thing before ChatGPT because we would ship in more hardware where there'd be a release GPT-3 and then we would start working on GPT-4 and these weird giant big spend R&D projects that would take a really long time and the spec was whatever the spec was and then you'd have to wait another year. And ChatGPT really broke that down because we were able to make iterative improvements to it just like software. And really, my dream is that it would be amazing if we could just ship daily or even hourly like in software land because you could just fix stuff, et cetera. But there's of course all kinds of challenges in how you do that while keeping the personality intact while not regressing other capabilities. So, it's an open field to get there.

Lenny Rachitsky (00:33:42):
That's such a good example of is it maximally accelerated? Okay, we're going to ship ChatGPT 10 days.

Nick Turley (00:33:48):
[inaudible 00:33:48]-

Lenny Rachitsky (00:33:48):
Holy moly. We've been talking about ChatGPT. Clearly it's kind of a chat interface. Everyone's always wondering is chat the future of all of this stuff? Interestingly, Kevin Weil made this really profound point that has always stuck with me when he was on the podcast that chat is actually a genius interface for building on a super intelligence because it's how we interact with humans of all variety of intelligence. It scales from someone at the lower end to a super smart person. And so, it's really valuable as a way to scale this spectrum. Maybe just talk about that and is chat the long-term interface for ChatGPT, I guess it's called ChatGPT.

Nick Turley (00:34:27):
I feel like we should either drop the chat or drop the GPT at some point because it is a mouthful. We're stuck with the name, but no matter what we do, the product will evolve. I think that I agree that there's something profound about natural language. It just really is the most natural form of communicating to humans and therefore it feels important that you should be communicating with your software in natural language. I think that's different from chat though. I think chat was the simplest way to ship at the time. I'm baffled by how much it took off as a concept. Even more baffled by how many people have copied the paradigm rather than trying out a different way of interacting with AI. I'm still hoping that will happen. So, I think natural language is here to stay, but this idea that it has to be a turn-by-turn chat interaction I think is really limiting.

(00:35:24):
And this is one of the reasons I don't love the super system analogy, even though we used to always use it is because if you think that way, then you kind of feel like you're talking to a person and GPT-5 it's amazing at making great front-end applications. So, I don't see a reason why you wouldn't have AIs that can render their own UI in some way. And you obviously want to make that predictable and feel good. But it feels limiting to me to think of the end-all-be-all interface as a chatbot. It actually kind of feels dystopian almost where I don't want to use all my software through the proxy of some interface. I love being in Figma, I love being in Google Docs. Those are all great products to me and they're not chatbots.

(00:36:07):
So, yes on natural language, but no on chat is where I would describe my point of view. And I'm just hoping in general that we see more consumer innovation on how people interact with AI because there's so many possibilities and you just got to try stuff. That's why chat stuck is we just did it and people liked it. So, I'm hoping that we see more there and we'll try to do our part.

Lenny Rachitsky (00:36:31):
So, you mentioned that you kind of got stuck with this name ChatGPT. Maybe this is part of the answer, but I'm curious just are there any accidental decisions you guys made early on that have stuck and have essentially become history changing?

Nick Turley (00:36:45):
There's so many and it is funny, because you have no time to think about them and then they end up being super consequential. The day was one, we went from chat with GPT-3.5 to ChatGPT the night before, slightly better but still really bad.

Lenny Rachitsky (00:36:58):
What was it called before?

Nick Turley (00:36:59):
It was going to be Chat with GPT-3.5 because we really didn't think it was going to be successful product. We were trying to actually be as nerdy as we could about it because that's really what it was. It was a research demo, not a product. So, we didn't think that was bad. But I think that in the original release, making it free was a big deal. I don't think we appreciate that because the GPT-3.5 model was in our API for at least six months prior to that. I think anyone could have built something like this. It might not have been quite as good on the modeling side, but I think it would've taken off. So, making it free and putting a nice UI on it, very consequential in the way that you take for granted now. And this is why I think that A, distribution and the interface are continuously important even in 2025.

(00:37:48):
The paid business, which now it's a giant business both in the consumer space and in the enterprise space. The birth of that was just to turn away demand originally. It was not like we brainstormed, "Oh, what is the best monetization model for AI?" It was really what monetization model or what mechanism would allow us to turn away people who are less serious than the people who are really trying to use it? And subscriptions just happened to have that property and it grew into a large business. I think shipping really funky capabilities before they were polished is another thing where that feels like a tactical decision, but it became a playbook because we would learn so much. Remember when we shipped Code Interpreter, we learned so much after we shipped it. Now it's known as I think data analysis in ChatGPT or something like that just because we actually got real world use cases back that we could then optimize. So, I think there's been a lot of decisions over time that proved pretty consequential, but we made them very, very quickly as we have to, so.

Lenny Rachitsky (00:38:53):
The $20 a month feels like an important part of this. Feels like everybody's just doing that now and-

Nick Turley (00:38:57):
On that one actually, I remember I had this kind of panic attack because we really needed to launch subscriptions because at the time we were taking the product down every time. It was, I don't know if you remember, we had this fail whale, there's a little [inaudible 00:39:09] generated poem on it. So, they were like, "We had to get this out." And I remember calling up someone I greatly respect who's incredible at pricing and I was like, "What should I do?" And we talked a bunch and I just ran out of time to incorporate most of that feedback. So, what I did do is ship a Google Form to Discord with, I think the four questions you're supposed to ask on how to price something-

Lenny Rachitsky (00:39:32):
[inaudible 00:39:32]?

Nick Turley (00:39:33):
Yeah, exactly. It literally had those four questions and I remember distinctly A, you [inaudible 00:39:38] a price back and that's kind of how we got to $20. But B, the next morning, there was a press article on you won't believe the four genius questions the ChatGPT team asked to price their... It was like if only you knew. So, there's something about building in this extreme public where people interpret so much more intentionality into what you're doing than might've actually existed at the time. But we got with the $20. We're debating something slightly higher at the time. I often wonder what would've happened because so many other companies ended up copying the $20 price point. So, I'm like, "Did we erase a bunch of market cap by pressing it this way?" But ultimately I don't care because the more accessible we can make this stuff, the better. And I think this is the price point that in Western countries has been reasonable to a lot of people in terms of the value that they get back.

(00:40:27):
And most importantly, we were able to push things down to the free tier semi-regularly and we always do that when we can [inaudible 00:40:35], but-

Lenny Rachitsky (00:40:35):
So, the survey, just to give the official name, the Van Westendorp survey is how you guys ended up pricing ChatGPT?

Nick Turley (00:40:42):
It was the top Google result. This was before ChatGPT has real-time information. Otherwise, it could have maybe price itself, but it was Discord plus Google Form plus a blog post on that methodology that got us there.

Lenny Rachitsky (00:40:54):
That is incredible. What a fun story. This is the survey that Rahul Vohra at Superhuman popularized in his first- round article-

Nick Turley (00:41:00):
Yeah. Yeah, yeah, that's right. That's right. Definitely don't bring me on here as a pricing expert, I think you have got better people for that.

Lenny Rachitsky (00:41:08):
Whether it was right or wrong, it is now the fastest-growing, insane revenue generating business in the world. So, I wouldn't feel too bad.

Nick Turley (00:41:16):
No, it worked out. Yeah.

Lenny Rachitsky (00:41:17):
It worked out. And by the way, I'm on the $200 a month tier, so there's clearly a room-

Nick Turley (00:41:22):
Thank you. Thank you.

Lenny Rachitsky (00:41:25):
... [inaudible 00:41:25]-

Nick Turley (00:41:25):
The story of that one is interesting too because originally the purpose of the Plus plan was to be able to ship first uptime and then be able to ship capabilities that we couldn't scale to everyone. And at some point it got so many people in the Plus tier that had just lost that property. So, the main reason we came up with the $200 tier is just we had so much incredible research that's actually really, really powerful. Like o3 Pro or tomorrow GPT-5 Pro and just having a vehicle of shipping that to people who really, really care is exciting even though it kind of violates the standard way a SaaS page should look, it's a little jarring to see the 10X jump. So, thank you for being a subscriber on that and thank you everyone else who's watching you subscribed to any tier, it's great.

Lenny Rachitsky (00:42:10):
I'm just going to throw a fishing line into this pond of are there any other stories like this? You shared this incredible story of Chat with GPT-3.5 being the original name, how you came up with pricing. Is there anything else?

Nick Turley (00:42:22):
Enterprise is interesting one too because we've seen so much incredible adoption in the Enterprise and it's sort of objectively crazy to try to take on building a developer business and a consumer business and an enterprise business and all at once. But the story there is in like month one or two, it was very clear that most of the usage was work usage, actually much more than today where you've got so many consumers on the product and it's kind of sort of transcended into pop culture. But at the time it was writing, coding, analysis, that kind of stuff. And we were pretty quickly in organically in 90% of Fortune 500 companies in a way that I had seen maybe at Dropbox back when that was my two jobs ago where we had a similar story. And since then there's been more PLG companies. But the real reason we did Enterprise, remember we were debating should we do enterprise or should we launch an iOS app because that's how small the team was.

(00:43:22):
The reason we did is we were starting to get banned in companies because they all felt rightfully or wrongfully that the privacy and deployment story, et cetera wasn't there. So, I was just like, "Man, we have to do something. We're going to miss out on a generational opportunity to build a work product." And we've literally defined AGI as outperforming most humans at economically valuable work or I'd probably [inaudible 00:43:45] that, but I think that's the way we put it. And so, I feel like we had to be present there and it was a fairly quick decision at the time, but it's grown into an immense business. We just hit 5 million business subscribers up from 3 million, I think a month or two ago. So, it is kind of the spinoff that it's taking a life of its own that I'm really, really excited about for [inaudible 00:44:11]-

Lenny Rachitsky (00:44:11):
That is a lot to be handling the platform essentially the API, the consumer product, the fastest-growing, most successful product in history and also the B2B side, which is clearly a massive business. Do you have any kind of heuristics for how to make these trade-offs do all this at once and stay sane and be successful?

Nick Turley (00:44:30):
That's a good question. And first off, I don't run the developer stuff anymore. We found someone way more competent to do that and he's amazing. So, I still look after the various forms of chat, but luckily you don't have to make that trade-off OpenAI does. And I can get into that too, but it keeps me a little bit more sane. I will say that you kind of have to practice in two different ways when you're building on this AI stuff. One is sort of working backwards from the model capabilities and that is much more art than science, where I think you really need to look at what tech do we have available and what is the most awesome way to productize it? And if you applied to some sort of PM framework to that, I think you would do something horrible wrong. Because if you have tech that's, for example, GPT-5 is really, really good at front-end coding now, I think that means you've got to reprioritize it.

(00:45:27):
You got to actually bring that capability to life. Maybe that's making ChatGPT better at vibe coding and rendering applications. Maybe that's more like leveraging the taste of the model to make the UI more expressive. There's a number of things we could do, but you kind of have to replan and reprioritize and that is more important than any particular audience segmentation. It's really just looking at what is the magic thing we have and how do you make it shine. Voice is a similar thing. It wasn't like our customers need voice, they're begging for it or something like that. It was like, "Wow, we figured out a way how to make these things anything in, anything out." What is a creative awesome way to productize that and then we can see what people do. So, I think that's one chunk of it. But then the other chunk of it really is more like classic product management where you need to listen to customers and then when your customers are really different, that can be confusing because ChatGPT is a very general purpose product.

(00:46:23):
We see when you look at end users, there's actually an immense amount of overlap in terms of what they want. Primitives like projects or history search or sharing and collaboration, all those kinds of things. They are actually very, very present. Whether or not you're talking to people at work or you're talking to people at home, at school, there's slightly different mechanics sometimes, but they're largely similar investments that I think we can get a lot of mileage out of. And then there's Enterprise-specific work that we just have to do. You've got to do HIPAA, you got to do SOC 2, you've got to do all those things if you want to be a serious player. And those are just non-negotiable. So, it's complex as you correctly identified, but it's kind of the curse of working on a very open-ended and powerful technology.

(00:47:11):
One analogy that someone at OpenAI who I really respect, he's like, "We're kind of like Disney, where Disney has this one kind of creative IP, which is their content, and they have cruises and they have theme parks and they have comics and they have all these different things." And I think we have amazing models, but there's all these different ways that you can productize them and we kind of just have to maximize the impact in all these different ways.

Lenny Rachitsky (00:47:38):
As you were talking, I was thinking about how usually horizontal platforms that are just so general and can do so much take a long time to take off because people don't know what to do with them. They're not amazing at anything. And this is an amazing counter example where it took off immediately and everyone figured it out and then over time they figured it out more and more.

Nick Turley (00:47:54):
But I think the reason why is because it just went live. Talk about another consequential decision actually. We were debating waitlist, no waitlist because we-

Nick Turley (00:48:00):
Actually we were debating waitlist/no waitlist because we really knew we couldn't scale the engineering systems. And the fact that there was no waitlist, which no open AI release had worked like that before, ended up being consequential because you were able to watch what everyone else was doing live. So I think when you launch these things all at once for everyone, there really is a special moment where you can see what other people are doing and learn from that.

(00:48:25):
And a lot of that is actually out of product. There's these crazy TikTok posts that go viral and they have like 2, 000 use cases in the comments. And I go through those in detail because it's not like I knew about those use cases either. They're very, very emergent and I just go through the comments and process because there's so much to learn. And for that reason, I think we get to skip the empty box problem a little bit because so much learning is happening out of product as people are watching each other either in IRL or online.

Lenny Rachitsky (00:48:55):
That is so interesting because you think about Airtable, you think about Notion, all these companies, they took years to just build and craft and think and go deep on what it could be.

Nick Turley (00:49:04):
It's like they compare Airtable, which they had to do templates, they had to do all these kind of things of taking the horizontal product and making it use case driven. They compare it to the Instant Pot, which there's recipes being shared everywhere online. There's this whole ecosystem around it. I think we were really lucky with ChatGPT that that happened where there's just users sharing use cases with other users everywhere. And therefore I think we got very lucky by jumping ahead on that journey.

Lenny Rachitsky (00:49:40):
And it feels like a quarter there is Sam had big following and everyone would pay attention to something you launch. So that's a really interesting new strategy for launching horizontal product. With a huge distribution channel, just launch it and see what comes up.

Nick Turley (00:49:51):
Yeah. And of course I'm actually really excited to take some of that into the product. I think we shouldn't rest on the fact that there's so much out product discovery happening. I actually think for the average consumer, it would be amazing if the product did a little bit more work on really exposing to you what is possible.

(00:50:07):
I still feel like ChatGPT feels a little bit like MS-DOS, like we haven't built Windows yet. And it'll be obvious once we do, but there's something that feels a little bit like... Imagine MS-DOS had gone viral and you were just trying to hack little conversation starters onto it. That might've missed sort of the big picture in terms of how to really communicate affordances and value to people. And so I think there's actually a ton more product work to do in addition to just seeing use cases spread.

Lenny Rachitsky (00:50:33):
Are you able to share just what you think that might look like? This Windows version of ChatGPT?

Nick Turley (00:50:37):
I'll let you know when we figure it out. We're hiring. I think there's so many interesting product problems here.

Lenny Rachitsky (00:50:42):
Okay, got it. By the way, I also love that TikTok was like your feedback channel.

Nick Turley (00:50:49):
Those common threads, they're just so wild. And also the love that people have for it, the excitement with which you're sharing their product, I feel like it's special that people are so excited to share what they're doing with your product. And I don't take that for granted either.

Lenny Rachitsky (00:51:06):
This episode is brought to you by PostHog, the product platform your engineers actually want to use. PostHog has all the tools that founders, developers, and product teams need, like product analytics, web analytics, session replays, heat maps, experimentation, surveys, LLM observability, air tracking and more.

(00:51:25):
Everything PostHog offers comes with a generous free tier that resets every month. More than 90% of customers use PostHog for free. You are going to love working with a team this transparent and technical. You'll see engineers landing pull requests for your issues and their support team provides code level assistance when things get tricky.

(00:51:42):
PostHog lets you have all your data in one place. Beyond analytics events, their data warehouse enables you to sync data from your Postgres database, Stripe, HubSpot, S3, and many more sources.

(00:51:53):
Finally, their new AI product analyst, Max AI, helps you get further faster, get help building complex queries and setting up your account with an expert who's always standing by. Sign up today for free at PostHog.com/lenny and make sure to tell them Lenny sent you. That's posthog.com/lenny.

(00:52:13):
How do you find emerging use cases these days? I imagine the volume is very high. Do you have kind of a trick for figuring out, "Oh, here's a new thing we should really think about?"

Nick Turley (00:52:22):
Before I built the product team, I actually built the data science team because I was getting frustrated. I was talking to as many users as I could. And my calendar the weeks after ChatGPT, it was just 15 minute user interview the whole week through. It was usually I stopped doing interviews when I can predict what the next person's going to say. That's how I know I've talked to enough users, but it just wasn't happening. I just kept getting new stuff.

(00:52:46):
So data is one way out where I think we have conversation classifiers that without us having to look at the conversations, allow us to figure out what are people talking about, what use cases are taking off, et cetera. And I think that's very, very helpful. The quality of the stuff is important for empathy. Even though you're never going to get a rap on all the use cases people have, I still spend a huge amount of my time doing that. And then yeah, things like those TikToks, collections of threads, I think they're really, really useful. It's just fun to watch people talk to each other about the various use cases that they have.

Lenny Rachitsky (00:53:22):
Is there kind of a new margin use case that you're excited about or is there a really unusual use of ChatGPT that you think about that'd be fun to share?

Nick Turley (00:53:30):
I mentioned this earlier, but I had always conceptualized ChatGPT as a worky product, whether or not you're at home or you at work. I feel like getting help with your taxes is very similar to the types of things you do at work where planning a trip is actually very similar to planning an event for work. So I always felt like, "Okay, this thing is going to kind of be a productivity tool."

(00:53:51):
And I think something has happened, I realized, a few months where that has begun to change and I really do think the fact that you have consumers turning to this thing for day-to-day advice, helping them have better relationships... People talk about how this thing saved their marriage is really exciting to me because they use it to process their own emotions, get feedback on their communication style. They just have a buddy to talk to about really difficult things. And that comes with a ton of responsibility and work that we have to do to make those things like life advice great, but it also is really, really important to me because you can't run away from those use cases. You have to run towards them and make them awesome. And that's part of what we're trying to do. So that emergent behavior is really, really cool.

(00:54:41):
And more broadly, I'm so excited about education. I'm so excited about health. I think it would really be a waste if we didn't take the opportunity of using ChatGPT to really, really help people. And I think we've just begun to scratch the surface on that. So there's many aspirational use cases that I want to make happen.

Lenny Rachitsky (00:55:05):
Along those lines, an interesting use case I've recently had, I feel like it's going to be really helpful for couples that are disagreeing about something when they need a third opinion. I just had this recently where my wife's like, "You can't heat a whole thing that you're going to only eat part of in the microwave and then put it back in the fridge." It's like, "What's the problem? I'll heat it up, I'll put it back in the fridge." And she's like, "No, that's really dangerous." I'm like, "Let's ask ChatGPT." And that fact that she so trusts ChatGPT now and relies on it throughout the day, it's such a valuable third independent party that we can go to.

Nick Turley (00:55:35):
Yeah, yeah, totally. And a lot of those micro-interactions talk about interesting product work, right? Those are micro-interactions that are important. Did it definitively weigh in or did it help you guys think through that disagreement and solve it on your own? I think those details actually matter a lot and it's where we're spending a bunch of time.

Lenny Rachitsky (00:55:54):
Along those lines, there was this whole launch of the very sycophantic version of ChatGPT where it was just, " You are the best person in the world. Everything you tell me is amazingly correct." Are you able to tell us just what happened there?

Nick Turley (00:56:08):
Yeah, we have all kinds of collateral online because we really felt like we should over-communicate on how we discovered it, what we did about it, et cetera. So I encourage people to check that out. We have a whole retro on that model release.

(00:56:24):
But basically what happened is that we pushed out an update that made the model more likely to tell you things that sound good in the moment, "You're totally right. You should break up with your boyfriend" or something like that. That's just really dangerous. We took it more seriously than you even might expect because again, at current technology levels, you can kind of laugh about it. Maybe it's like, "Ha-ha. This thing's always complimenting me. I thought it was just me. I saw all those comments online." But it actually is really important to make sure that these models are optimized for the right things.

(00:57:01):
And we have an immense, I think, luxury to have a mission that affords us to really help people, a business model that does not incentivize maximizing engagement or time spent in the product, right? So it's really important to us that you feel like this product is helping you with your goals, whether not that's your current goals or even your long-term goals.

(00:57:25):
And oftentimes being extremely complimentary with the user isn't actually in service of that. So we instilled new measurement techniques. Whenever we put these models in contact with reality and we learn about a problem, we actually go back and make sure we have good metrics for this stuff. So we measure sick efficiency now with every release to make sure we don't regress and actually improve on that metric. GPT-5 is an improvement, which is really exciting for me, but we have more work from there.

(00:57:54):
And more broadly, it caused us to articulate our point of view. I actually spent a bunch of time on a blog post that we just published on Monday on what we're optimizing ChatGPT for. And it really is to help you thrive and achieve your goals, not to keep you in the product. And so there was a bunch of good outcomes from that incident. It's a good example of how contact for reality is not just important for the use cases, but also for learning what to avoid because you would've never discovered this issue purely in a lab unless you actually heard from physicians.

Lenny Rachitsky (00:58:26):
I am excited to read that blog post then. I was going to ask you this. Just like how you-

Nick Turley (00:58:29):
Yeah, have your feedback on it.

Lenny Rachitsky (00:58:31):
Yeah. I guess is there anything more there of just how you... Because this tension is so difficult, helping people feel supported, but not just letting them believe everything they want to believe. Is there anything more you can share there? Just trying to find that middle ground.

Nick Turley (00:58:43):
Incentives are important. There is a famous saying, "Show me the incentive and I'll show you the outcome."

Lenny Rachitsky (00:58:48):
Charlie Munger maybe?

Nick Turley (00:58:49):
Yeah, I think that's where it came from, right?

Lenny Rachitsky (00:58:50):
Yeah.

Nick Turley (00:58:52):
Yeah, I think that's very, very important. So I would take a good look at our mission, our business model, the type of product we're trying to build. And I really think that ChatGPT is a very special product because I think in vast majority of cases, it makes you leave it feeling better or not worse and feeling like you're achieving something you're trying to do. So I think that those incentives really matter because it helps you reason about, "Okay, when there isn't behavior in the wild, that's not good. Was that a bug or was that by design? And with [inaudible 00:59:29] I can very much say that to us that's a bug.

(00:59:31):
And then on the forward-looking work, there's so many kind of challenging scenarios to get right. And you could easily run away from these use cases. Like you and your wife going to this thing for input on a relationship, a question or a dispute, you could very easily run away if you were totally risk avoidant and say, " Sorry, I can't help you with that." I think that's what most tech companies do when they hit a certain scale, they run away from these use cases. And I think it's a lost opportunity to help people.

(01:00:08):
So we want to run towards these use cases by making the model behavior really, really great. That can mean connecting you with external resources when you're struggling. That can mean not directly answering your question, but instead of giving you a helpful framework in the case of like, "Should I break up with my boyfriend?" ChatGPT should probably not answer that question for you, but it should help you think through that question in the way that a thoughtful companion would. So I think it's really important to do the work because I think the upside is immense.

Lenny Rachitsky (01:00:37):
That is a really profound point you're making there, that if most companies, if their users want to ask them something risky like getting medical advice or, "Should I break up with my partner?" or, "what should I do with this big problem I have?"

Nick Turley (01:00:51):
I feel like we would have immense regret if you had a model that was state-of-the-art on health bench, which is, GPT-5 is a state of the art on a bunch of these medical benchmarks, and you didn't use that to help people, you just disabled that use case because you wanted to avoid all possible downside. I think the duty is to make it awesome and to do the work, talk to experts, figure out how good it really is, where it breaks down, communicate that. And I think this technology is too important and has too much potential positive impact on people to run away from these high stakes excuses.

Lenny Rachitsky (01:01:27):
And fast-forward to today, it's saving lives regularly. It's probably saving relationships regularly. Such a consequential decision, which I imagine was made early on.

Nick Turley (01:01:36):
Yeah. We're just at the beginning of watching how this stuff can transform people. It's incredibly democratizing. If you compare, you roll out of this with the roll out of the personal computer, computers were so scarce when they first came out. And this stuff is ubiquitous in a way where you have access to a second opinion on medical stuff, you have access to a relationship buddy, you have access to a personal tutor on literally any topic that makes you curious. It's really, really special that we get to do that. Unique point in history.

Lenny Rachitsky (01:02:15):
Let me zoom out a bit and talk about OpenAI and just product in general. So you've worked at traditional, let's say traditional product companies, Dropbox, Instacart. Now you're at OpenAI. What's maybe the most counterintuitive lesson you've learned by building products from your time at OpenAI?

Nick Turley (01:02:33):
Each time I always tried to pick the maximally different job whenever I made a job change. So after Dropbox, I was craving a real world product because it was just so different than working on SaaS, et cetera. And after Instacart, I was craving on working on something that intellectually was interesting and had this kind of invoked the nerd in me. And so I've always looked for things that are really different.

(01:02:59):
And then once I showed up at these places, I tried to understand what makes that place successful, what is truly the thing that they cracked and how we can lean in that into that even more.

(01:03:11):
I think I spent a lot of time thinking about this with OpenAI, especially after ChatGPT. Before that it was kind of a moot point because we didn't really have much revenue or products or anything like that. There's a few things that come to mind that have driven many decisions. One is the empiricism. We talked about that a bit. The fact that you can only find out by shipping, which is why maximally lean into that. And that's a huge part of why we ship so much.

(01:03:46):
One of them is that amazing ideas come from anywhere. The thing about running a research lab is you really don't tell people what to research. That's not what you do. And we inherited that culture even as we become a research and product company. So just letting people do things who have amazing ideas rather than being the gatekeeper or prioritizer of everything or something like that has been proven immensely valuable to us. And that's where much of the innovation comes from, is empowered smart people on any function really. So that was a good inheritance from what I think made OpenAI successful and makes us successful.

(01:04:23):
The interdisciplinariness of really making sure that you put research and engineering and design and product together rather than treating them as silos. I think that's the thing that has made us successful and that you see come through in every product we ship. Like if we're shipping a feature and it doesn't get 2X better as the model gets 2X smarter, it's probably not a feature we should be shipping. Not always true. SOC 2 doesn't get better with [inaudible 01:04:48] models, but I think for many of the core capabilities, that's a good litmus test.

(01:04:52):
So I've always found you really have to lean into why is this place successful and then maximally accelerate that, so to speak, because it's what allows you to turn something that feels like an accident into something that is a repeatable label.

Lenny Rachitsky (01:05:07):
So you talked about this kind of collaboration between researchers and product people. And you've been at the beginning of ChatGPT from day one to today, from zero to 700 million weekly active users. Not just registered users, weekly active users. How have you approached building out that team over time?

Nick Turley (01:05:24):
One of the other inheritances of being in a research lab is that you take recruiting really seriously. That's something that AI labs know every person matters. But many tech companies that go through hyper growth and they kind of lose their identity, they lose their talent bars, they just have chaos. So we've always had this tendency to run relatively lean.

(01:05:51):
So it is a small team that is running ChatGPT. I take co inspiration from WhatsApp where it was a very small team running a very global-scale product. And then more importantly, you have to treat hiring a little bit more like executive recruiting and less like just pure pipeline recruiting where you really need to understand what is the gap you're trying to fill on each team, what is the specific skill set and how do you fill it.

(01:06:17):
To give you an example, I'm a product person at heart, but sometimes a team doesn't need a product person because there's already someone doing that role. In many cases, we have a really talented engineering leader who has amazing product sense, or we have a researcher who has product ideas. And in my mind they can play that role. And maybe we have something else missing instead. Maybe we need a little bit more front-end or something like that.

(01:06:41):
In other cases, maybe what you're missing is incredible data scientists. So I really like to go through every single team and figure out what is the skill sets that that team needs and how do you put it together from principles rather than just assuming, "Hey, we're going to do a bunch of pipeline recruiting for all these different roles" and then people will find a team later. So I think that's always felt really important to me. And it's the way that you keep your team really small, yet super high throughput.

(01:07:08):
It also allows you to hire people who I think Keith Rabois calls us like barrels, I think. [inaudible 01:07:15] barrel's an ammunition where he thinks... I think this comes from him, but the idea being that sort of the throughput of your org depends on how many barrels you have, which is people who can make stuff happen. And then you can add ammunition around them, which is people helping those people. I think that's been really true for our recruiting too where we try to maximize the number of empowered people who can ship because that's how you have a small team and still get the ton done.

(01:07:43):
So there's a couple of things, and I spent a lot of time on vibes too with each team because I think one of the things that is challenging when you try to do research and product together is that the cultures are different. People have different backgrounds. And I think to make that go super well, you need to spend time team building and making sure that people have a huge amount of trust for each other's skill sets, feel like they can think across their boundaries. I really believe that product is everyone's job, for example. And for that reason, the recruiting doesn't stop when the people are on the door. It actually starts because you have to start making the teams awesome.

Lenny Rachitsky (01:08:24):
Is there something you do with team building that would be fun to share? Just like something you do to create [inaudible 01:08:28]?

Nick Turley (01:08:28):
I just love whiteboarding with teams. I just love getting into a generative mindset. It breaks down everything. So that's the thing that I try. It's not particularly creative, but I found it to be a universal tool where the minute you can get people to stop thinking about what's my job versus the other person's job and more like we're all in a room trying to crack something together, that is incredible.

Lenny Rachitsky (01:08:50):
You mentioned this idea of first principles. This came up actually when I talk to a lot of people about you, is this something you're really big on. A lot of people talk about first principles, most people are like, " I don't really understand," or they think they're amazing at thinking from first principles. Is there something you can share of just what it actually looks like to think from first principles as maybe an example that comes to mind where you really went to first principles and came up with something unexpected?

Nick Turley (01:09:15):
Yeah, this is not something I'd ever say about myself. It's nice that someone else would say it, but it's a mysterious thing. Yeah, I think you just really got to get to ground truth on what you're really trying to solve. For example, as I mentioned with the recruiting thing, I'm not dogmatic that you have to have a product manager and an engineering manager and a designer or whatever. We're just trying to make an awesome team that can ship. So in that case, first principles means just really understanding what we actually need and what we're missing rather than applying a previously learned process or behavior. So I think that's a good example.

(01:09:54):
Another good example of I think being first principles in this environment is, does this feature need to be polished? We get a lot of crap for the model chooser, and I own it. I've tried to say that to everyone who will listen. For those who don't know model chooser, it's this giant drop down in the product that is literally the anti-pattern of any good product traditionally.

(01:10:16):
But if you are actually recent from scratch, is it better to wait until you got a polished product or to ship out something raw even if it makes less sense and start learning and getting into people's hands? I think a company with a lot of process or a lot of just learned behaviors will make one call, which is, we have a quality bar when we ship, and that's what we do. If your first principle is about it, I think you're like, "You know what? We should ship. It's embarrassing, but that's strictly less bad than not getting the feedback you wanted."

(01:10:51):
So I think just approaching each scenario from scratch is so important in this space because there is no analogy for what we're building. You can't copy an existing thing. There is no, "Are we an Instagram or are we a Google or a productivity tool or something like that?" I don't know. But you can learn from everywhere, but you have to do it from scratch. And I think that's why that trait tends to make someone effective at OpenAI, and it's something we test for in our interviews too.

Lenny Rachitsky (01:11:23):
So this theme keeps coming up, and I think it's just important to highlight something that you keep coming back to, which is this trade-off of speed and polish and how in this space, speed is more important, not just to stay ahead, but to learn what the hell people actually want to do with this thing. Is there anything more that you think people just may be missing about why they need to move so fast in the space of AI?

Nick Turley (01:11:46):
Yeah. I mean, the boring answer would be, oh, it's competitive and everyone's in AI and they're trying to compete each other. I think that's maybe true, but that's not the reason that I believe this. The reason really is that you're going to be polishing the wrong things in the space. You absolutely should polish-

Nick Turley (01:12:00):
You're going to be polishing the wrong things in this space. You absolutely should polish things like the model output, et cetera, but you won't know what to polish until after you ship. And I think that is uniquely true in an environment where the properties of your product are emergent and not knowable in advance. And I think that many people get that wrong because they think the best product people tend to be craftspeople and they have a traditional definition of craft. I also think it would be easy to use all what I just said as an excuse not to eventually build a great product. So I often tell my teams that shipping is just one point on the journey towards awesomeness, and you should pick that point intentionally where it doesn't have to be the end of your iteration at all. It can be the beginning, but you better follow through.

(01:12:50):
So we've been doing a bunch of work, especially over the last quarter of really cleaning up the UI of ChatGPT. I'm really excited to do the same for the sort of the response layouts and formats next. Simply because once you know what people are doing, there's no excuse to not polish your product. It's just really, in a world where you don't know yet, you might get very distracted.

(01:13:09):
So it's situational. Again, you kind of have to be first principles about it. But I do think using velocity, especially early on, as a tool... Actually this has been said about consumer social for example. It is not the first space where people have said, "Hey, you just got to try 10 things because you're probably going to be wrong." So I don't think this has never existed before as a dynamic either, but I do think with AI, it's important to internalize.

Lenny Rachitsky (01:13:32):
And there's also an element of the models are changing constantly and so you may not even realize what they're capable of, I imagine.

Nick Turley (01:13:38):
Totally. The models are changing and the best way to improve them, whether or not you're a lab or actually just someone who's doing context engineering or fine-tuning a model maybe, you need failure cases, real failure cases, to make these things better. The benchmarks are increasingly saturated. So really you need real-world scenarios where your product or model is not actually doing the thing it was supposed to do, and the only way you get that is by shipping, because you get back to use case distribution and you can make those things good. And therefore, it's actually the best way to then go articulate to your team, especially your ML teams, what [inaudible 01:14:17] climb on? It's like, "Oh, people are trying to do X and the model's failing in ways. Why? Now let's make those things really good."

Lenny Rachitsky (01:14:23):
This point about failure cases makes me think about something that both Kevin Weil and Mike Krieger shared, which is that evals are becoming a huge new skill that product people need to get good at because so much of product building is now writing evals. Is there something there you want to share?

Nick Turley (01:14:41):
My entire OpenAI journey has been this journey of rediscovering eternal product wisdom and principles in like slightly new contexts. So I remember I started writing evals before I knew what an eval was because I was just outlining very clearly specified ideal behavior for various use cases until someone told me, "Hey, you should make an eval." And I realized there was this entire world of research evaluation benchmarks that had nothing to do with the product that I was trying to make. And I was like, "Wow, this might be the lingua franca of how to communicate what the product should be doing to people who do AI research." And that really clicked for me.

(01:15:23):
And at the end of the day, it's not that different from the wisdom of, you ought to articulate success before you do anything else. It's just a new mechanism for doing that. But you can do it in a spreadsheet, you do it anywhere, and I really wanted to mystify it for people who hear that term. It's not some technical magic that you have to understand. It's really just about articulating success in a way that is maximally useful for training bots.

Lenny Rachitsky (01:15:50):
Awesome. I have a post coming out soon that gives you a very good how-to for PMs have how to write evals.

Nick Turley (01:15:56):
I would love to read it. And I hope you agree with what I just said because maybe there's [inaudible 01:16:02] to it.

Lenny Rachitsky (01:16:02):
Absolutely. Absolutely. And now there's all these tools that make this easier for you.

Nick Turley (01:16:04):
Totally.

Lenny Rachitsky (01:16:04):
Okay, so this basically backs up this point that this is just a very important skill that product teams and builders need to get good at.

Nick Turley (01:16:12):
Yeah. Yeah.

Lenny Rachitsky (01:16:13):
Okay. Just a few more questions. I know you have a lot going on today. One is that this trend of ChatGPT being a big driver of growth for traffic to sites, for products. For example, ChatGPT is now driving more traffic to my newsletter than Twitter, which completely shocked me. I just was looking at my stats, I'm like, "What the hell? This is not something I knew was coming." So just I guess thoughts on the future of this, how you think about just ChatGPT driving growth and traffic to products and sites?

Nick Turley (01:16:48):
I'm really excited about it because in the same way that I find it dystopian to talk to everything through a chat bot, I also find it dystopian to not have amazing new high quality content out there. And for that reason, I talked a little bit earlier about search and have that solved a really important user problem early on because you had this knowledge cutoff thing and you suddenly could talk about anything. Very obvious in retrospect. A, it wasn't just a user problem, it was an ecosystem problem where the original ChatGPT, it didn't have outlinks, it would just answer your question, it would keep you in the product. And even if you wanted to keep reading or go deeper, there was no way for us to drive traffic back to the content ecosystem. And I've been really excited about what we've been doing in search, not just because it gives people more accurate answers, but because it allows us to surface really high quality content, like this podcast, to people who want to see it.

(01:17:47):
And of course there's so many interesting questions about, well in the Google era, there was the search engine optimization and there was clearly understood mechanisms of how to show up and get more traffic. So I get a lot of questions from people, like, "What is the equivalent of that? The AI era, if I'm Lenny and I want to 10X the traffic to my podcast, what do I actually need to do?" And the truth is we don't have amazing answers there simply because the way to appeal to an AI model ideally is the same way that you would appeal to a real user, because the model's supposed to proxy the interest of the user and nothing else. At least that's how I want our product to work. And for that reason, my advice is super lame, which is make really high quality content, which is not as actionable as I think people making content would ideally like. And I think this is why we have more work to do because maybe there's a better mechanism or protocol that we could come up with.

(01:18:42):
But I'm excited this is driving meaningful traffic for you, and I hope that other people making great content start to feel this way because, again, it's a very new scenario.

Lenny Rachitsky (01:18:52):
There's two acronyms people have been using for this specific skill of AI driven SEO. I think one is AEO, which is answer engine optimization. The other is GEO. I forget the G one.

Nick Turley (01:19:04):
Generative... Yeah, I don't know.

Lenny Rachitsky (01:19:06):
Generative, yeah, AI optimization.

Nick Turley (01:19:08):
Yeah.

Lenny Rachitsky (01:19:08):
Do you have a favorite of those two? [inaudible 01:19:10]-

Nick Turley (01:19:10):
No, no. I try to shy away from these terms unless they become inevitable just because I'm not entirely sure yet if that should be a concept or not. Again, I think ideally, ChatGPT understands your goals and therefore understands what content would be interesting to you. And the content creator's job is to share enough information and metadata about that content such that the AI model can make a user-aligned decision. And therefore, I'm not sure if giving this thing a name and making a thing is what we should be doing or not. I'm very eager to learn from folks making content about what this could look like because. Again, we're still working through.

Lenny Rachitsky (01:19:59):
Along these lines, another question people think about is you have GPTs, which are kind of these custom GPT apps that you can build to answer very specific use cases. There's always this question of, you're going to build an app store where I can plug in my product into ChatGPT, monetize that. Is there stuff there that you could talk about that might be coming someday?

Nick Turley (01:20:19):
GPTs are cool. They're kind of ahead of their time in the sense that we built that kind of concept before you could really build very differentiated things. At least in the consumer space, your learning GPT is going to be pretty similar to what the model could already do out of the box. So it's mainly a way of articulating a use case to people, but it doesn't have enough tools yet to make something that feels like an app, so to speak.

(01:20:47):
Different in the enterprise by the way. We're seeing a ton of adoption of GPTs there because just every single company has very bespoke business processes and problems, etc. And it's a really, really useful tool there. They also have unique data that they can hook up to these things that it can retrieve over. So we've seen a lot of success there.

(01:21:05):
I think the idea is the right one, and I think we're going to figure out a good mechanism for it. Because when you have so much capability packed into AI, it feels really powerful to allow people to package that up in ways that have a clear affordance, a clear use case, and are differentiated from each other. I also would love it if you could start a business on ChatGPT. I think there really is a world where, as this thing hits a billion user scale, it can get you distribution, it can get you started on making something in the same way that people built on the internet and there was entirely new businesses to be built.

(01:21:41):
So I think we'll have more to share there in the future. GPT's was an early stab. And I'm just excited to evolve the thinking there as the models get good and our reach increases as well.

Lenny Rachitsky (01:21:51):
Amazing. That is really cool. I'm really excited to see what you guys do there. Okay. Completely different direction. Something that I know about you is you studied philosophy in college.

Nick Turley (01:22:02):
I did.

Lenny Rachitsky (01:22:02):
Computer science and philosophy, right? A combo.

Nick Turley (01:22:05):
Yeah. I started as a philosophy major and took one coding class because I really liked logic, and programming was most similar to that. And then I fell in love with coding and then eventually computer science, and I just kept doing more and more of it. But until then, I'd never really thought of myself as a technical person, so it was kind of a late discovery in my life that I'm very grateful for.

Lenny Rachitsky (01:22:27):
What an incredible combination for someone leading this product [inaudible 01:22:30].

Nick Turley (01:22:30):
It's true. It is really coming in full circle in a way that I couldn't have predicted. The amount of questions you have to grapple with are truly super interesting. And philosophy, it's not a traditionally practical skill, but it does really teach you to think things through from scratch and to articulate a point of view, and I think that has come in handy numerous times.

Lenny Rachitsky (01:22:51):
Is there a specific philosopher or school that has been most handy to you, or is there more just the general [inaudible 01:22:57]?

Nick Turley (01:22:56):
Oh, there's so many.

Lenny Rachitsky (01:22:56):
okay.

Nick Turley (01:22:57):
I wrote my senior thesis on whether and why rational people can disagree, which also comes in handy when a lot of people with very different values have opinions on your model behavior or on how things should work. So I really like 20th century analytical philosophers. It's kind of dirty stuff, but I don't know if I have a favorite. It's too many to count. But that's the kind of stuff I like. And some of it ends up being quite analytical. You have let P be this theory of love and let Q be this other theory of love, and then you do some sort of symbolic manipulation. So it is just as much a brain thought exercise as it is... Or it's much more that than practical, but it taught me how to think in a way that continues to be pretty valuable.

Lenny Rachitsky (01:23:48):
Incredible. What a cool combo of skills and background. Last question before we get to very exciting lightning round. So you were a product leader at Dropbox, then Instacart, now you're the PM of arguably the most consequential product in history. How did you land in this role? What was the story of joining OpenAI and taking on this work?

Nick Turley (01:24:10):
Every single career decisions I ever made, including my first one out of college, was just figuring out who are the smartest people I know that I want to hang out with and learn from, and can I work with them? And I don't know how to vet companies, I don't know how to really logically think through what space is going to take off or something like that, but I just do feel like I have a sense on people. And for Dropbox, I followed the head teaching assistant for a class that I was TA-ing. And for Instacart, I followed some of the smartest product people I knew. And for OpenAI, the person who recruited me, Joanne, I had messaged her about getting off the DALL·E waitlist and she said, "Only if you interview here." So she turned it into a reverse recruiting thing.

(01:25:02):
And initially, honestly, I didn't know what I would do here because it was a research lab and I was a product person and they said, "Don't worry, we'll figure it out." And they were sort of being cagey. And I thought they were being cagey because it's OpenAI and they can't share anything, but they were being cagey because we actually just didn't know yet at the time. So I showed up and I did everything under the sun and it definitely wasn't product. It was like, I think my first task was fix the blinds or something like that. And then I started sending out NDAs for people because they needed some operational help. And then I started asking, "Wait, why am I sending out NDAs? Oh, so we could talk to users." And I was like, "Talking to users, that sounds like the thing I know how to do." And I quickly stumbled into doing product work, and then eventually leading a bunch of product work. But it was organic by just showing up and doing what had to be done because, again, the company I joined was not a product company by any.

Lenny Rachitsky (01:26:00):
Wow. This is such a good example of, I don't know if you think of it this way, but when someone offers you a seat on a rocket ship, don't ask which seat. [inaudible 01:26:07].

Nick Turley (01:26:08):
Yeah, so I didn't know it was a rocket ship. I kind of got nerd sniped is what I would describe it as. Where as I prepared for the conversation to get off the DALL·E waitlist really, I just started reading about the space and that piqued the philosophy brain and then also actually the computer science brain. I was like, "Wait, this is cool." Then I started reading all the academic papers of that era. So it was intellectual itch and the people, but then I stayed for the product opportunity, obviously. Post ChatGPT, when that took off, realized that we'd built a rocket ship where we'd launched it while building it, maybe is the analogy. But I can't say that it felt like a hyped job or anything like that when I applied.

Lenny Rachitsky (01:27:00):
So a lesson there is, as you said, follow the smartest people you know. There's also just this thread of follow things that are interesting to you. Just you playing with DALL·E led to this opportunity.

Nick Turley (01:27:10):
Yeah, yeah. And actually that's something we still test for is curiosity is an attribute that we think matters so much more than your ML knowledge. I'm not making a comment on research hiring. I think you do need some ML knowledge, I'm afraid. But for product and engineering and design people, and those kinds of functions, I actually think that if you are just curious about the stuff works, it doesn't matter at all if you've never done it before. In fact, if you were to filter for people who've done it before, you would have a very narrow filter of very lucky people rather than necessarily the best people you can get. So I think we've scaled that. Certainly what got me here, but I think it's actually, just generically, been a good predictor of success at OpenAI.

Lenny Rachitsky (01:27:50):
Nick, I told you I had a billion... I said I had 2 billion questions to ask you. I feel like I've asked a lot. I feel like I still have a billion left. But I know, you told me right after this you, have a big GPT- 5 check-in that you got to get to. So-

Nick Turley (01:28:01):
We got to ship.

Lenny Rachitsky (01:28:03):
We got to ship. Better ship now that this is recorded and we're putting this out.

Nick Turley (01:28:08):
This is true. [inaudible 01:28:08].

Lenny Rachitsky (01:28:09):
This is the forcing function. Okay, so before we get to a very exciting lightning round, is there anything else that you want to share, leave listeners with, think is important to share?

Nick Turley (01:28:20):
I try to share a little bit about how I made decisions because I hope to... I'm not that far out of school. I relate a lot to people who are coming in the job market, who are trying to figure out what to do with their life right now. And I feel very confident that if you surround yourself with people that give you energy and if you follow the things you're actually curious about, that you're going to be successful in this era. So my parting advice to folks really is put yourself around good people and do the things you're actually passionate about. Because in a world where this thing can answer any question, asking the right question is very, very important. And the only way to learn how to do that is to nurture your own curiosity. So it worked for me and it's the one repeatable thing that I can share. Everything else is luck.

Lenny Rachitsky (01:29:15):
This is counter to what a lot of people are doing right now, which is follow the money. Where can I make the most? How do I grow this thing and make $100 million? All these people that are getting these crazy offers were not planning to make a lot of money doing this.

Nick Turley (01:29:27):
It's quite interesting to see that stuff play out because I think all these people entered school for genuine reasons. They were excited about the space, they were researching it, they were pursuing knowledge, and I'm happy that that's being rewarded. And I don't know what the rewards will look like in the future, especially in a post-AGI world. But I just a feeling that if you follow that advice, you'll end up okay.

Lenny Rachitsky (01:29:54):
With that, Nick, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Nick Turley (01:29:59):
Sure, yeah.

Lenny Rachitsky (01:30:00):
What are two or three books that you find yourself recommending most to other people?

Nick Turley (01:30:04):
In the product space, probably things like High Output Management or The Design of Everyday Things, or those kind of classic type things because I think they're extremely applicable in AI.

Lenny Rachitsky (01:30:13):
We talked about philosophy. I don't know, is there a philosophy book you're like, "Here's the one to read if you're getting into this."

Nick Turley (01:30:17):
Oh man. Anything by Rawls and Nozick. I like the political stuff. I think it's really fun. That is a type of thing I recommend. I don't think there's a practical reason to read that stuff, but I will nerd out about it with you. So at your own peril.

Lenny Rachitsky (01:30:32):
Do you have a favorite recent movie or TV show you've really enjoyed? If you've had time to watch anything.

Nick Turley (01:30:36):
I think you've got to do a little bit of sci-fi to be in this space. You shouldn't copy any of it, but I think you learn from it. So regularly re-watch Her and Westworld. Severance was great. I think that's the stuff that, when I have time, I'll meddle with.

Lenny Rachitsky (01:30:56):
That is awesome. I love that those are the two. Of all the sci-fi movies, those are the ones you resonate most with and find most interesting and valuable.

Nick Turley (01:31:03):
Yes, but that's probably my own limitation, so I'm sure there's more to discover.

Lenny Rachitsky (01:31:08):
By the way, have you read Fire Upon the Deep, that sci-fi book?

Nick Turley (01:31:08):
No.

Lenny Rachitsky (01:31:13):
Okay. I don't know if you have time to read this book, but I think you would love it. It's such a good-

Nick Turley (01:31:16):
Oh, man. Okay.

Lenny Rachitsky (01:31:17):
... AI oriented sci-fi space opera sort of book.

Nick Turley (01:31:20):
Great.

Lenny Rachitsky (01:31:21):
Yeah.

Nick Turley (01:31:22):
I'll check it out, thank you.

Lenny Rachitsky (01:31:22):
Okay. Off tangent.

Nick Turley (01:31:22):
Yeah, yeah, yeah. For sure.

Lenny Rachitsky (01:31:26):
Okay. Do you have a favorite product you've recently discovered that you really love?

Nick Turley (01:31:29):
I actually don't. I am at extreme capacity. It's kind of interesting. API developers ask me like, "Hey, are you going to copy all of our products?" It's like, I actually just do not have time to follow up what's going on outside of OpenAI because the pace here is so, so intense. So don't have good recs for you, I'm afraid.

Lenny Rachitsky (01:31:54):
That's a comforting answer, I think, to a lot of product companies. Go figure. Nick has no time to even listen to our stuff. Oh man. Okay. Do you have a favorite life motto that you find yourself using when things are tough, sharing with friends or family that other people find useful?

Nick Turley (01:32:10):
Being the average of the five people you spend the most time with is a thing that I really internalize, both in my personal life, where there's people who give me energy and who lift me up and make me a better person. My fiance is one of those people, but there's many people in my life. But then there's also just, at work, there's the equivalent. And again, that's how I've made all the career decisions. It's like who do I want to learn from? So I apply that principle constantly.

Lenny Rachitsky (01:32:36):
Final question, everybody I talked to told me that you are a very good jazz pianist. You have won competitions. I think you were planning to do this as your main thing and then you somehow took the side quest.

Nick Turley (01:32:47):
Yeah, I chickened out that at the very last minute, but I was going to go to school for music. And that's still my, hopefully, chapter two.

Lenny Rachitsky (01:32:55):
Wow. I love that that might still happen.

Nick Turley (01:32:58):
Might still happen. Now I'm in some for fun bands and we will kick from time to time. It's like the one thing I can do when I'm otherwise super tired and can't think anymore because it balances me out in good ways. But yeah, hopefully I'll get to do more of it in the future.

Lenny Rachitsky (01:33:16):
Is there any analogs between music and your job? Anything that you find-

Nick Turley (01:33:20):
Yeah, actually. I feel like you could think of software development as, or being a product person, as you could be a conductor of an orchestra or you could be in a jazz band. And I think of it as a jazz band where I don't believe in the idea of everyone having this set part that they have to play and me kind of telling people when to play. I love how in jazz, or other forms of improvised music, you're kind of riffing off of each other and you listen to what one person played and then you play something back. And I think that great product development is like that, in the sense that ideas could come from anywhere. It shouldn't be a scripted process. You should be trying stuff out, having fun, having play in what you do. So I use that analogy a lot. For those who like music, it tends to resonate.

Lenny Rachitsky (01:34:13):
Nick, I am so thankful that you made time for this. I know today is insane. Tomorrow's going to be even more insane for the entire world. They have no idea what's coming. Thank you so much for doing this. Two final questions. Where can folks find you if you want them to find you online? Where can folks find GPT-5 potentially. And then just how can listeners be useful to you?

Nick Turley (01:34:31):
Just use the product. You don't even have to pay. Should be your default model starting tomorrow and just use it and don't think about models anymore. Unless you want to and you're a Pro user, in which case you get all the old models. So rest assured. And useful, honestly, I learned so much from people at large and ChatGPT users, et cetera, so just keep doing your thing. I am watching and learning, and I appreciate all the feedback. So I'm sure after we fix the model chooser, you guys will roast me for something else and I'll take it. So keep it coming.

Lenny Rachitsky (01:35:05):
Amazing. Nick, thank you so much for being here.

Nick Turley (01:35:08):
Thanks for having me, Lenny.

Lenny Rachitsky (01:35:09):
And good luck tomorrow.

Nick Turley (01:35:10):
Thanks.

Lenny Rachitsky (01:35:11):
Bye everyone.

(01:35:13):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.

