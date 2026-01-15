---
guest: Dan Shipper
title: 'The AI-native startup: 5 products, 7-figure revenue, 100% AI-written code.
  | Dan Shipper (Every)'
youtube_url: https://www.youtube.com/watch?v=crMrVozp_h8
video_id: crMrVozp_h8
description: 'Dan Shipper is the co-founder and CEO of Every. With just 15 people,
  Every publishes a daily AI newsletter, ships multiple AI products, and operates
  a million-dollar-a-year consulting arm—all...

  '
duration_seconds: 5697.0
duration: '1:34:57'
view_count: 81826
channel: Lenny's Podcast
keywords:
- growth
- metrics
- experimentation
- analytics
- subscription
- revenue
- hiring
- management
- strategy
- vision
- differentiation
- market
- persona
- design
- ux
---

# The AI-native startup: 5 products, 7-figure revenue, 100% AI-written code. | Dan Shipper (Every)

## Transcript

Lenny Rachitsky (00:00:00):
The business you're building, the team you're building, the way you're operating is the very bleeding edge of how companies are trying to operate in this AI era.

Dan Shipper (00:00:07):
We have a head of AI operations. She's just constantly building prompts and building workflows that I and everyone else on the team are just automating as much as possible.

Lenny Rachitsky (00:00:16):
What are some things that you believe about AI that most people don't?

Dan Shipper (00:00:20):
I hate the headlines that are like, "Entry-level jobs are taken away by AI." Whenever I see a kid with ChatGPT, I'm like, "Holy shit, they're going to go so much faster than any other person that I've worked with." We have this guy, he made a year's worth of progress in two months because every time I sat down with him and told him, "Okay, here's how you tell a story, here's how you think about a headline," he recorded all of it, put it into a prompt, and he never made the same mistake twice.

Lenny Rachitsky (00:00:40):
There's this sense we're getting to a place where you don't have to write any code, you have a product team not writing code at all.

Dan Shipper (00:00:46):
No one is manually coding anymore. Organizations like ours, people who are playing at the edge, we're doing things that, in three years, everybody else is going to be doing.

Lenny Rachitsky (00:00:55):
Today, my guest is Dan Shipper. Dan is the co-founder and CEO of Every, which is a company that is at the very bleeding edge of what is possible with AI. Their team of just 15 employees has built and shipped four different products. They publish a daily newsletter, and they have a consulting arm that helps companies adopt the latest AI best practices. On their product team, their engineers don't handwrite a single line of code and instead use an arsenal of agents who help them craft requirements and build their products.

(00:01:22):
Their editorial arm uses AI to publish better work faster, and they even have a person whose entire job is to help every employee at the company become more efficient using the latest AI workflows. In our conversation, Dan shares a bunch of tactics that they use internally to increase the leverage of their own employees, his personal AI tool stack, the one predictor that he's found for whether a company will successfully find huge productivity gains through AI, how he's building his company in a really unique way, a bunch of predictions for where AI is going, and so much more.

(00:01:53):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. And also, if you become an annual subscriber of my newsletter, you get a bunch of amazing products for free for one year, including Superhuman, Linear, Notion, Perplexity, Bolt, Granola and more. Check it out at lennysnewsletter.com and click bundle. With that, I bring you Dan Shipper.

(00:02:16):
This episode is brought to you by CodeRabbit, the AI code review platform transforming how engineering teams ship faster with AI without sacrificing code quality. Code reviews are critical, but time-consuming. CodeRabbit acts as your AI copilot providing instant code review comments and potential impacts of every pull request. Beyond just flagging issues, CodeRabbit provides one-click fix suggestions and lets you define custom code quality rules using ast-grep patterns, catching subtle issues that traditional static analysis tools might miss. CodeRabbit also provides free AI code reviews directly in the IDE. It's available in VS Code, Cursor and Windsurf.

(00:02:55):
CodeRabbit has so far reviewed more than 10 million PRs, installed on one million repositories, and is used by over 70,000 open source projects. Get CodeRabbit for free for an entire year at coderabbit.ai using code Lenny. That's coderabbit.ai. Today's episode is brought to you by DX. If you're an engineering leader or on a platform team, at some point, your CEO will inevitably ask you for productivity metrics.

(00:03:24):
But measuring engineering organizations is hard, and we can all agree that simple metrics like the number of PRs or commits doesn't tell the full story. That's where DX comes in. DX is an engineering intelligence solution designed by leading researchers, including those behind the DORA and SPACE frameworks. It combines quantitative data from developer tools with qualitative feedback from developers to give you a complete view of engineering productivity and the factors affecting it.

(00:03:51):
Learn why some of the world's most iconic companies like Etsy, Dropbox, Twilio, Vercel, and Webflow rely on DX. Visit DX's website at getdx.com/lenny. Dan, thank you so much for being here and welcome to the podcast.

Dan Shipper (00:04:11):
Thank you for having me. I've obviously been a huge fan for a long time and so it's an honor to be here.

Lenny Rachitsky (00:04:16):
It's my honor, Dan. I feel like this is a podcast that was meant to be. I'm so happy we're finally doing this. There's so damn much that I want to talk about; there's so damn much we can talk about. I thought it'd be fun to start with just some hot takes.

(00:04:29):
And the reason I want to start here is I feel like you spend more time thinking about AI, building with AI, using AI, evaluating AI than anyone else I know nearly. And so I really respect your insights and your perspectives on where things are going. So let me just ask you this question and see where this goes. What are some things that you believe about AI using AI tools that most people don't believe?

Dan Shipper (00:04:55):
I'm going to go with my hottest take, and this is the take that I have the least evidence for. So let's just start with that. I have other more well-reasoned takes to give you, but this is my hottest one, which is I think that AI may be one of the biggest force for reshoring American jobs. And so I think everyone is worried about it unemploying people. And for sure, it will change the skills needed to do the jobs that you're doing, but I think it may actually reshore a lot of jobs, and it'll do that in two ways.

(00:05:27):
One is, there are a lot of expensive services that rich people and big companies are paid for right now, so in-house counsel or call center or whatever. And what cheap intelligence does is it makes those kinds of things affordable for small companies and individuals. So it stimulates demand. The other thing that it does is it allows people who are in those jobs to serve more people cheaply. It may not get rid of customer service, for example, but it may allow 10 people in the Midwest, who would normally be working at a call center, to serve hundreds of thousands or millions of people. Maybe that's too much, but a lot more people than they would ordinarily if they were the ones on the phone all the time.

(00:06:22):
And so it becomes much more cost-effective for American companies to hire people in the US. And I think the people in the US are going to be better, in a lot of cases, at using these AI tools to do work. So I think it may actually make it more effective to have those jobs in the US run by people sitting in the US who are using it to get work done. And also, the model companies are here too. So there's a lot of American stuff happening, and you can decide whether or not you think that's a good thing, but I think it's quite lost in the conversation over whether AI will get rid of jobs.

Lenny Rachitsky (00:06:58):
I like optimistic takes about AI, so this is great. And to your point, TBD if this is good for other countries, but good for the US. What else? What else you got? What other hot takes?

Dan Shipper (00:07:10):
Okay. Another big hot take, and this is less contrarian and more just, I think, people are truly sleeping on it. I think people are truly sleeping on how good Claude Code is for non-coders. And I'll extend this to not just Claude Code, but Google just came out with the Gemini CLI command-line interface. So things like that. And I'll tell you for people who are listening that don't know what Claude Code is. Claude Code is just the command-line interface. It's those black terminals that programmers use. It's a command-line interface that you can boot up. It has access to your file system, it knows how to use any kind of terminal command and it knows how to browse the web, all that kind of stuff.

(00:07:47):
You can give it something to do and it will go off and it'll run for 20 or 30 minutes and complete a task autonomously, agentically. Especially with Claude Opus 4 that just came out, it's this gigantic leap forward in AI's ability to work by itself. And Claude Code can even spawn multiple sub-agents that do a bunch of tasks in parallel and it's incredibly useful for programmers. Everybody inside of Every is using it all day, every day. Everyone's agent-pilled. They've got 15 agents doing all this kind of stuff. It's crazy.

(00:08:18):
But non-programmers don't use it because it's intimidating to use the terminal. But for example, you can download all your meeting notes and put it in a folder and just be like, "Okay, I want you to read every single one of my meeting notes and tell me..." Something that I do, for example, is, "Tell me all the time that I subtly avoided conflict."

(00:08:38):
And it writes a little to-do list for itself. It can have a little notebook, it can go and read each little thing and then write into its notebook, go down its to-do list and give you a summarized answer over multiple turns. So it's not just stuffing everything into context, which is what you'd be doing with ChatGPT chat or a regular Claude chat. It's actually processing every single file that you give it. And so I think it's incredibly powerful for any kind of task that involves processing a lot of text.

Lenny Rachitsky (00:09:06):
So as a simple way to think about this, you basically have an agent on your local computer that can read your local files and do your bidding.

Dan Shipper (00:09:14):
Yes, exactly. And it can do that for long amounts of time without going off the rails.

Lenny Rachitsky (00:09:21):
Interesting. And so there's a small hurdle that non-technical people have to overcome, which is using their terminal and giving commands, but once they get it running, it's just you talk to it in English and ask it to do stuff.

Dan Shipper (00:09:32):
Exactly.

Lenny Rachitsky (00:09:33):
So the hot take here is just Claude Code, which most people think is for engineers, is the most underrated tool for non-technical people.

Dan Shipper (00:09:42):
Yeah, exactly.

Lenny Rachitsky (00:09:43):
What are some other ways you imagine people seeing this? This meeting note example is really cool and I could see people using this. What else have you seen or thinking about?

Dan Shipper (00:09:52):
Something that I've done a lot, so I'm a writer for a lot of my job. And I know you're going to ask me about books I love, so I'm going to give you a sneak peek, which is I love War and Peace. I just read it for the third time.

Lenny Rachitsky (00:10:03):
Wow, that's a long book.

Dan Shipper (00:10:06):
It's so long, but it's so good. I think Tolstoy is a brilliant writer. And one thing that I wanted to do is I was like, "I want to inflect some of my writing with some of Tolstoy's style." And the way I did that is I think he's incredible at these little subtle sentences where he shows you what a character is thinking and feeling just by how they behave, how they move their face or the mismatch between the intonation in their voice and the expression in their eyes, all that kind of stuff. He's just an incredible student of human behavior and psychology.

(00:10:36):
And so I just downloaded War and Peace to my computer, which you can do because it's public domain. And then I had Claude read the first three chapters of War and Peace and pull out all of those descriptions, and then make a guide for itself for how to do character descriptions like Tolstoy. And you could totally do this with a regular Opus command, but you couldn't put all of War and Peace into it. It would take a lot more hand holding to get it to do this. And it just did this by itself without my really intervening.

(00:11:05):
I had it download a Russian version of War and Peace and the English version, and then start comparing different scenes that I love to tell me about things that I might've missed in the translations, so that you can get as deep and weird and nerdy for whatever subfield you care about as you want to. Same thing for if you've got tons of customer interviews or tons of customer data you want to go through, it's incredibly powerful for going and figuring stuff out from big data sets like that.

Lenny Rachitsky (00:11:30):
You actually inspired me to use... This is not what you're describing, but it's also something that's very cool. This is going to sound so nerdy. I'm reading Anna Karenina right now.

Dan Shipper (00:11:40):
Yes.

Lenny Rachitsky (00:11:41):
Also Tolstoy. And this is recommended by a previous podcast guest. And so I was like, "All right, I got to read this." Also very long. I'm on my Kindle, I'm just like, "All right, 13% in, I've been reading for months."

Dan Shipper (00:11:52):
Hot take, I think War and Peace is better than Anna Karenina, especially for a tech person. But they're both good.

Lenny Rachitsky (00:11:57):
Okay, there we go. There's my year. I saw you tweet this use case that I love that I've been using, which is just while I'm reading, having ChatGPT voice sitting around and then just asking it questions. Because you don't actually have to feed it the book, it knows the whole book. And Anthropic just shared this. I don't know if they shared or someone found this in their legal briefings that they actually bought tons of books and scanned them themselves, is how they did fair use.

(00:12:23):
And so it has all this context. So just sitting there and asking it, "What the heck is this thing in Russian society?" is super fun. Okay, so this is awesome. So the tip here is just coming back to your hot take. The tip is you basically can have an agent using local files and doing all kinds of cool stuff on your computer versus having to upload it into projects or into your prompts and things like that. Super cool. So the bet here is that people are going to discover this and start using this just day to day.

Dan Shipper (00:12:53):
I think they absolutely will. And I also think probably the model companies are going to start making this more accessible. I think one of the things that will just come from Claude Code and other things like it into everything else you use, whether it's on the web or wherever, is all of the original AI apps were pasting a chat box into an existing UI. So you've got Copilot, it's got the auto-complete in the IDE. You've got Cursor, it's got a little sidebar with a little chat. And the difference with Claude Code is you never look at the code. It's not meant for coding, it's not meant for coding by hand.

(00:13:34):
It's meant for you to say, "I want you to get something done," and it goes and does it. And I think we're just getting to a point where for pretty much all the usual applications, AI is going to be good enough that we can get rid of the interfaces more or less where you're digging into all the things that it's actually doing and you're interleaved with its execution and you're more just like, "I'm delegating, it's going to go do it."

Lenny Rachitsky (00:13:58):
Yeah. I had Cursor's CEO, Michael Truell, on the podcast, and this is his big vision is, "What comes after code?"

Dan Shipper (00:14:05):
English.

Lenny Rachitsky (00:14:06):
Exactly. Exactly. I also just had the founder of Base44 on the podcast who built this company, sold for 80 million bucks to Wix. And he shared that he's been around for six months, the company. For the last three months, he hasn't touched a single line of front-end code, all Cursor and other tools he's using. So this is happening.

Dan Shipper (00:14:27):
Same thing for people inside of Every, no one is manually coding anymore.

Lenny Rachitsky (00:14:32):
Okay. Definitely need to talk about that. Before we do, any other hot takes that you want to throw out there?

Dan Shipper (00:14:38):
I have one other hot take, which is I have a definition for AGI. And so AGI is famously hard to define. What does it mean for it to be artificial general intelligence? The Turing test was one, but we'd pretty much blown past the Turing test in a lot of ways. So we have no good one. And so what I have noticed is that you can tell how much better AI is getting by how long a leash you can give it to do work.

(00:15:09):
So with Copilot, you can tab complete and that was the beginning. With ChatGPT, you ask it a question and it returns a response and that's maybe slightly better than a tab complete. And then now with Claude Opus 4 and Gemini and all that kind of stuff, also with deep research, it can go off and work for 20 or 30 minutes. So that leash is getting longer where you have to intervene.

(00:15:34):
And I was thinking about this and it reminded me of Winnicott, who was a child psychologist. He wrote this book called Playing & Reality. And his conceptualization for what it means to become an adult, what it means to go from being an infant to a child to an adult is when you're first born, you're effectively fused with usually your mother, your caregiver. There's no difference between you and her or you and whoever your caregiver is.

(00:16:02):
And growing up is this process of being gradually let down in certain moments where you can handle being let down. So you learn that there's a separation between you and your caregiver. So for infants, it's instead of being fused at the hip for every hour of every day, you get left alone. Maybe you get left alone to cry it out. Who knows if that's the right thing to do with infants? A lot of consternation there. But that's teaching you that there's a separation between you and your mom or you and your dad. There's not going to always be someone to pick you up.

(00:16:38):
And raising a child is about knowing when they're ready to be let down a little bit and have to stand up on their own. So I think there's that same leash with human development. You get longer and longer periods of time where you can be on your own. So we're still in the 20 to 30 minutes is maybe... I don't know, you probably can't leave a toddler alone for 20 or 30 minutes, but it's a little bit older than a toddler.

Lenny Rachitsky (00:17:02):
Maybe 20, 30 seconds.

Dan Shipper (00:17:06):
With a toddler, you can be in the same room but not interacting with them every single second for 20 minutes sometimes. So it's around there. I think we have that similar leash with AGI. And so I think a good definition of AGI is when does it become economically profitable for people to run agents indefinitely? So it just never turns off. It's a Claude Code that's always running, it's always doing something, you just never turn it off, and you don't need to because you know that it's worthwhile to keep it on.

(00:17:41):
It's never waiting for you to be like, "Okay, next thing." It'll always respond to you when you're like, "Okay, next thing." But it's off just essentially living its life like a teenager and that is profitable for you. You'd rather have it do that than just wait for you to tell it what to do next.

Lenny Rachitsky (00:17:56):
Interesting.

Dan Shipper (00:17:56):
I think that's a good definition of AGI.

Lenny Rachitsky (00:17:58):
The profitable piece is also just the cost of running that thing and having it.

Dan Shipper (00:18:02):
It's partly the cost and partly the value. And obviously, you can game this a little bit and be like, "Cool, I'm just going to tell Claude to run in a loop forever." But I'm talking about more than that, more widespread adoption of agents that work all the time. And I like the profitable thing, because if it costs a little bit of money and the bar is profitability, it has to actually be doing something useful for you to keep it on.

Lenny Rachitsky (00:18:29):
It's interesting how the metaphor of a senior employee and autonomy and essentially the more autonomous they are, the less instruction you have to give, the less reviews you have to do, is also just directly correlated with how senior they are.

Dan Shipper (00:18:44):
Totally.

Lenny Rachitsky (00:18:45):
Okay, great. Anything else along these lines?

Dan Shipper (00:18:48):
I have plenty of them. I hate the headlines that are like, "It's going to replace jobs," or "It's going to unemploy two thirds of the workforce." I don't think that's true. I hate headlines that are like, "You don't use your brain when you use ChatGPT," or another good headline is, "Doctors alone, doctors plus AI, or just AI, which one is better? AI is better, therefore, doctors are going to be outmoded."

(00:19:18):
All that stuff is, I think, pretty dumb. So for the doctors plus AI example, I think it's important to recognize that using AI is a skill. And so if you study doctors in a vacuum that don't really have a lot of experience with AI, you could probably create a situation such that it's better to just use an AI. And sometimes it is going to be better. But there's so many contexts that doctors need to make decisions and do things that it's really hard to take one study and make any conclusion about that.

(00:19:52):
And it's especially hard when you're dealing with a technology that's developing so rapidly that doctors can't really be expected to be experts at it yet. But I would guess in five or 10 years, that will be totally and completely different. For the student example or the "AI turns your brain off" example, I think it's really important to understand that in the history of technology, it has always been the case that you give up certain skills in order to get other ones. For example, Plato is famously very skeptical of writing because he thought it would harm your memory. And it did. We don't remember things quite as well as they did back in the day because they had to remember long epic poems to entertain each other.

(00:20:37):
But I think writing is a worthwhile trade for having a slightly worse memory. And I think something similar is going on with AI where you may be slightly less engaged in certain tasks, but if you use it right, you're going to be way more engaged in other tasks where you have much more power. And so you can construct a study that says brain connectivity goes down when you use AI in the same way that you could construct a study that says people's memory are worse when they have writing skills. But I don't think anyone would want to go back to a world where no one was literate.

Lenny Rachitsky (00:21:10):
That is super interesting. There's all these studies that are showing the benefits of AI to students with these studies in Nigeria and just how fast people progress. So I think it's really important, this context you're sharing that you will lose some things, but the hope is the gain is much higher, and so far it seems like it will be.

Dan Shipper (00:21:27):
Yeah. I think people always, especially at the beginning of a tech hype cycle or a revolution paradigm shift, it's always easy to underestimate how quickly things are going to change. And the example I always use is, I live in Brooklyn and the tailor down the street from me doesn't accept credit cards. Credit cards have been around for a long time, so it takes a long time for technology like this to be adopted even in the best case.

(00:21:55):
And I think it's really easy to underestimate how complex specific contexts are that humans know how to deal with. And just because you can get a really good score on a test... It's incredible. I love AI, it's so incredible, but it doesn't actually give you an intuition for how difficult it is to actually be replacing specific parts of work or activities that you would do. I think a really good thing to give you maybe a little bit of an intuition for it is I built this thing over a weekend a month ago that was, "0.3, can it predict what I'm going to say in a meeting?"

(00:22:45):
That's a benchmark. It's the CEO benchmark. And the reason I did that is because the gold standard for OpenAI for testing how powerful a model is, is they test it on their internal code base. So they say, "How good is the new model at predicting what comes next in our internal code base?" Because that's not anywhere out on the internet. So it's a really good benchmark for that. And so I was like, "Well, my meeting transcripts aren't anywhere on the internet. A lot of what I say is on the internet and there's some overlap, but it'd be interesting."

(00:23:19):
And so I ran a bunch of the frontier models on this, on just my Granola transcripts, and they're pretty bad. They are pretty bad, and it's not because they're not smart. There's this real push now. Tobi from Spotify coined this term called "context engineering," which is getting the context to the model, the right context at the right time, is at least half the performance.

(00:23:43):
And I think that's 100% true. It's something that I've been writing about for three years. At the time, I called it knowledge orchestration. I think context engineering is probably a better term. But it's totally true, and that's a very, very hard problem to solve. It's not just a one- shot problem where it's gigantic context window and we're done. It's going...

Dan Shipper (00:24:00):
... that problem, where it's like gigantic context window and we're done. I think it's going to get better over time, but the minute it gets good at predicting what I'm going to say next in a meeting, I'm just going to use it as a tool, and that's going to change the entire dynamic of what I say next in a meeting. So it's not as easy as it seems.

Lenny Rachitsky (00:24:18):
Interesting. I imagine you can build a GPT from that. And then, instead of having a meeting with Dan now, just talk to this thing, and he'll make decisions.

Dan Shipper (00:24:26):
Yes, definitely. And I mean we do this a little bit. It's not the same as being able to predict exactly what I'm going to say in a meeting. But I think if you're a CEO, or founder, or manager, it's really stunning how much of your job is just repeating yourself. And that is one of the best things about this AI, particularly AI revolution, is that you don't have to repeat yourself.

(00:24:48):
And so we had it last quarter. I tend to set one or two quarterly goals. And one of my big goals for us last quarter was don't repeat yourself. So I don't want ever say the same thing in a meeting twice, if I can help it. So for us, at Every, one of the big parts of Every is we have a daily newsletter. And I'm spending a lot of time giving feedback on headlines, or giving feedback on, "How do you write an intro," or "Is this idea any good," that kind of stuff.

(00:25:15):
And we've started to codify all of that into prompts that basically... It's not the same as mimicking me. It can't exactly say exactly what I'm going to say in a meeting, but it pushes my taste out to the edge so that writers who are not able to talk to me, by the time I see it, they've already talked to some simulation of a simulation of me. And that's incredibly powerful.

Lenny Rachitsky (00:25:41):
Let's follow this thread. This is exactly where I want it to go. I feel like the business you're building, the team you're building, the way you're operating is the very bleeding edge of how companies will operate and are trying to operate in this AI era. You guys are trying to be super AI-first. And it's super aligned with just so much of your writing. There's just so much reason to study what you guys are doing. So-

Dan Shipper (00:26:04):
Well, thank you.

Lenny Rachitsky (00:26:05):
Yes. And this is benefiting all of us, so thank you. So first of all, just tell people what the heck Every is, and then share a few insights into just how you operate. It's funny that you laugh at [inaudible 00:26:20] whatever you say.

Dan Shipper (00:26:20):
Everyone asks that because it's a very weird shape of a company. You can actually see other companies that have this shape from earlier eras, but it's less common. It doesn't make as much sense.

(00:26:33):
And I think it's newly enabled by AI, and we can talk about why. But the way that I typically talk about Every is we do ideas and apps at the edge of AI. So the core of the business is we have a daily newsletter. We've been doing it for about five years. We have about 100,000 subscribers. All of the people from the top AI labs read us. Anyone who's basically interested in or working in AI at the frontier and wants to know what's on reads us.

(00:27:00):
We do a lot of... For example, whenever OpenAI or Anthropic drop a new model, we get our hands on it early, and then we get to play with it and write about it, which it's my ideal job. I love it. It's the best.

Lenny Rachitsky (00:27:14):
It sounds like it.

Dan Shipper (00:27:14):
I don't if I can curse on this podcast, but-

Lenny Rachitsky (00:27:15):
You can.

Dan Shipper (00:27:15):
... it's the fucking best.

Lenny Rachitsky (00:27:18):
Perfect. Excellent use. And you call those "vibe checks", is that the-

Dan Shipper (00:27:22):
Yeah, we call them vibe checks-

Lenny Rachitsky (00:27:22):
Vibe checks, love those.

Dan Shipper (00:27:24):
... which I think is really important because... And this gets to the next part, the apps part of what we do. I think it's really important to do vibe checks and to call them vibe checks because they're about how does it feel to use this thing and how does it feel to use it for work for things that you would normally use it for in your job or in your life. Because I think that captures something that standard benchmarks just don't capture and really can't. And the best people to tell... to write a vibe check are people that are actually at the edge using it for stuff.

(00:27:57):
And so what we've found over time is we have... We love, we think the best writing and content about technology is from people that are actually using it and building with it. And so we've always had this sort of function, where we're always building little experiments in addition to our writing, and that helps us write great stuff. And that has turned into a suite of apps that we run internally. And the people who are building those apps are also writers, and they're contributing to things like vibe checks.

(00:28:27):
So you get a really inside look into how is this stuff being built from people who are actually using it every day. And the suite of apps that we have, one's called Cora. We just launched Cora publicly on the day that we're recording this, which is really awesome.

Lenny Rachitsky (00:28:39):
Congratulations.

Dan Shipper (00:28:40):
Thank you. You can think of it like a chief of staff, an AI chief of staff for your email. It helps you manage your email with AI. It's very cool. We can go into more of it later. We have another one called Sparkle, which is an AI file cleaner. We have another one called Spiral that does content automation with AI. We originally incubated Lex, which is an AI document writer, which we spun out into its own company, and my Every co-founder runs that.

(00:29:05):
And basically we bundle everything together. So you pay one price, and you get access to all of the software that we make, and we're constantly putting new stuff in the bundle. And I can tell you more about what kinds of things do we like to incubate and how do we like to incubate it because I think there's some really interesting, special things in there.

(00:29:21):
But I've been blabbering for a while, so I'll stop there.

Lenny Rachitsky (00:29:23):
There's also a consulting firm, which I want to talk about, but let's hold off on that.

Dan Shipper (00:29:25):
Yeah, we have consulting.

Lenny Rachitsky (00:29:26):
Yeah.

Dan Shipper (00:29:27):
We also do that, and that's the third leg of the stool in the business. It doesn't fit quite as nicely into my ideas in app streaming, but we spend a lot of time with big companies, where we teach them basically how to be AI-first. We train all the people on how to use AI. And it's very cool, it's really fun, and a very important part of what we do.

Lenny Rachitsky (00:29:47):
That feels like a billion-dollar business right there. I want to come back to it.

Dan Shipper (00:29:50):
[inaudible 00:29:50].

Lenny Rachitsky (00:29:51):
Because everybody wants to learn this.

(00:29:53):
Okay, so share a few ways that you guys operate. You mentioned that your team doesn't write any code. What are just some ways that allow you to operate this efficiently? I know your team's really small. You have a daily newsletter, you have three, four products, you have a consulting arm. How big is the team at Every?

Dan Shipper (00:30:10):
We have 15 people.

Lenny Rachitsky (00:30:11):
15 people? Okay.

Dan Shipper (00:30:12):
Yeah.

Lenny Rachitsky (00:30:12):
So just give us insight into some of the ways you operate that are at the bleeding edge.

Dan Shipper (00:30:16):
Okay, so a couple of things. One, and I think everyone should do this, is we have a head of AI operations. I sit with her once a week. And every time I'm doing something repetitively, we put it in a to-do list. And she's just constantly building prompts, and building workflows, and stuff like that so that I and everyone else on the team are just automating as much as possible. And I think that has been a big unlock because it's really hard to...

(00:30:44):
If you're working in a job all day, you're fighting fires, and you're like, "Okay, am I going to do this in the way that I know how or am I going to do it in the new way that might not work?" I don't want to spend a bunch of time [inaudible 00:30:54] you're building some no-code automation. I don't want to do that. And having an AI operations lead lets you basically identify those things and have them solved without people who are doing the work actually having to take time to do it, which I think makes it much more likely it happens.

(00:31:10):
There's always a trick with that, where it's like you have to make sure it gets used. So it's basically you're developing little applications internally, but if you're good at making applications people use, it's great. Highly recommend having an AI operations lead.

Lenny Rachitsky (00:31:23):
I imagine you saw the [inaudible 00:31:25] Quora tweeted about this, wanting to hire exactly this sort of person.

Dan Shipper (00:31:29):
Yeah.

Lenny Rachitsky (00:31:29):
So clearly this is a trend.

Dan Shipper (00:31:31):
Yeah.

Lenny Rachitsky (00:31:31):
So the idea is your point that this needs to be somebody who's outside of the day-to-day work of the company, and is specifically focused on helping the team be more efficient with AI?

Dan Shipper (00:31:43):
Yeah. Yeah.

Lenny Rachitsky (00:31:44):
And then is this person mostly just you automating you, or can they help other people? Are they helpful-

Dan Shipper (00:31:49):
No, she helps everyone, basically.

Lenny Rachitsky (00:31:49):
Everyone? Okay.

Dan Shipper (00:31:51):
Where we're starting right now is with the editorial operation. So there's so much stuff in the editorial operation, where I or our editor in chief, Kate... Kate, is constantly doing little, small copy edits to make sure everything is in Every style, and it takes hours a day. And so now Opus is at a point where you can give it a style guide and a prompt, and it will go through anything you're writing, and copy edit it, which is amazing.

(00:32:24):
The trick is it's not just building that. You also have to get Kate to be like, "Did you put this through the prompt yet," anytime someone gives her something. So there's a little bit of behavioral update too that has to happen, which I think is a really interesting organizational challenge.

(00:32:38):
And I think for us it's a little easier because everybody inside the org is very AI-first and just wants to go do it. We don't have anyone really who's like, "I don't know. I don't really want to do this." And that's a whole different challenge, which I think a lot of organizations face, but there's always a problem of getting people to use it.

Lenny Rachitsky (00:32:55):
That is super cool. What is her background, this AI operations person?

Dan Shipper (00:32:59):
Her name is Katie Parrott. She actually does a lot of ghostwriting for us. So she also, when people inside of Every who are builders... Often they just write themselves, but sometimes they want help, and she'll help them write about whatever they're working on. So that's how she started with us. She still does that, but she also spends a lot of time doing the AI operation stuff.

(00:33:20):
And then before that, she worked at Animalz, which is a content marketing agency, one of the top content marketing agencies. And they're very process oriented. And I think the reason Katie is so good is because she's incredibly good at that kind of process stuff or thinking about that, but she's also a great writer and she's also just incredibly excited about AI. She just wants to tinker and wants to use it. And that was the thing that got me to be like, "Okay, you should just come and do that. Instead of just ghostwriting, we should add this to your plate." And it's been really fantastic.

(00:33:58):
At minimum, you really just want someone who's just like, "I want to tinker. I want to build stuff." There's also people who have a little bit more of that process orientation. I think that is important. And to the extent they understand the craft of the thing that they're trying to build for, that also helps a lot.

Lenny Rachitsky (00:34:14):
This is an amazing tip. I feel like everyone's going to start hiring these people.

Dan Shipper (00:34:17):
I think so. There's a couple other people who talk about this. I heard Rachel Woods, who's another... She thinks a lot of AI stuff. She's talking about it. I think it's becoming a thing, and I think it's really important, and it just bleeds out into every other part of the org.

(00:34:33):
So we're doing this inside of the editorial org, but there's a lot of copy that goes out on Cora. And by the way, Cora is spelled C-O-R-A, so it's different from Q-U-O-R-A, slightly confusing. There's a lot of copy that goes out on Cora, or Spiral, or Sparkle that we want to have that same Every quality bar for. And so we have engineers sending Kate, like, "Here's the Figma file. Can you go and do copy edits?" And that sucks for everybody. And Kate is one person, and it's just really hard to do that.

(00:35:04):
So one thing that we did, Nityesh, who's one of the engineers on Cora, built a Claude Code command that just uses that prompt, and checks through the entire code base for all the copy edits, and then creates a pull request on GitHub, and then sends the pull request to Kate. So she's just looking at the pull request, and being like, "Does this make sense?"

(00:35:26):
And so you can translate that prompt into, for example, a format that engineers can use. And suddenly your engineering team is writing marketing copy in the style you want. I think that's so cool.

Lenny Rachitsky (00:35:36):
That is extremely cool. I'm going to take us on a little tangent. You keep mentioning-

Dan Shipper (00:35:42):
[inaudible 00:35:42].

Lenny Rachitsky (00:35:42):
... Claude, and I'm curious just what is in the stack of tools that you find yourself using, your team ends up using. It seems like Claude is a core part of it.

Dan Shipper (00:35:51):
I do love Claude. I would say I'm generally... My first thing that I open is o3. I'm a ChatGPT boy. And I think o3 is super high quality. I think it's great for writing, it's great for coding, it's great for all that stuff. And what it has that really makes a difference still from Claude is it has memory. And I just love that. I've spent so much time yelling at ChatGPT about, "I need my writing to be punchy and concise." And it just knows that now.

(00:36:20):
So I think when I ask it to write something for me, it's actually better than yours. Or maybe not yours, but your average ChatGPT user. And I also find I use it a lot for self-reflection and personal growth type stuff. So it knows me. So when I send it a meeting transcript, and I'm like, "How did I do?" It's like, "Well, you did that thing that you normally do, but you're way better on this other thing." And I like that. I think that's really great. So day-to-day, o3, that's my go-to.

(00:36:49):
I think Claude Opus is... First of all, Claude Code, everyone inside Every, that's basically what we use. If you're building something, you're using Claude Code. It's crazy. It's so good.

(00:37:01):
Gemini just came out with something, so I'm very excited to try that because I think that's the model that we use most for the apps that we build, inside the apps. It's incredibly powerful and it's incredibly cheap, which is great. So I want to try the CLI tool that they came out with.

(00:37:17):
We also use Codex a bit, which is OpenAI's coding tool. And that's for, like, "I want a one-off, self-contained... I want to pick off this little feature."

(00:37:27):
What else do I use? Going back to Claude, Claude Opus 4 can do something that no other model, except one other model that I can't talk about... can do something that no-

Lenny Rachitsky (00:37:39):
[inaudible 00:37:39].

Dan Shipper (00:37:39):
... other model can do.

Lenny Rachitsky (00:37:40):
Okay, we won't go there. We don't want to get you in trouble. Okay, go on.

Dan Shipper (00:37:44):
But yeah, no other model can do this. Which is earlier versions of Claude, and I think generally versions of other models, when you ask them, "Is this piece of writing any good," Claude, for example, would always give it a B+. And then if you did another turn of the same conversation, you're like, "I updated this," it would always go to A-. And then if you give it another turn, it would go to A.

(00:38:07):
So it doesn't have the same kind of gut. It's thinking about what you probably want hear too much. And there's various methods that you can use to prompt engineer around this, like give it a template or whatever. And they sort of worked, but it just still doesn't have that thing where it's like, "Can it tell if writing is interesting or any good? Does it have that gut sense?" And Opus 4 has it. It's really wild. And I think that's super important because it opens up all these use cases where you might want to use a language model as a judge. So for us, for example, we're working on a new version of our product Spiral, which does content automation. You've used that in the past. And we're doing essentially Claude Code, but for content style product, where you say, "I want it to write a tweet," you give it all the documents, it has a bunch of memories, it creates a to-do list for itself, and then it goes and writes.

(00:39:04):
And one of the things that is so interesting is now, because it can judge things, part of its to-do list is, "Okay, I wrote three tweets. I'm going to judge whether I think these are any good," and then it can improve before it comes back to you.

(00:39:21):
And that's just a huge, huge unlock, that we were struggling for three months to build this crazy system to try to get it to judge writing. And then Opus 4, just one-shotted it, and we're like, "Great, this product works. Let's start chipping it." So yeah, I love it for that.

Lenny Rachitsky (00:39:37):
Are there any other AI tools that you just use regularly? You mentioned Granola, even outside of the bottles. So what are some that you think maybe people are sleeping on?

Dan Shipper (00:39:46):
I use Granola. So I used to use Super Whisper and Whisper flow, which I think are fantastic. We have an internal version of that called Monologue that will be shipping in a month or so that I use now, but you can think of them as roughly equivalent. And I think generally speech to text interfaces are the future, and more people should be using them, and more people should be building them as affordances. We use Notion all the time, and I specifically use their meeting recording. I think that's mostly the stack.

Lenny Rachitsky (00:40:17):
Okay. That was really helpful and super interesting.

(00:40:20):
This episode is brought to you by PostHog, the product platform your engineers actually want to use. PostHog has all the tools that founders, developers, and product teams need, like product analytics, web analytics, session replays, heat maps, experimentation, surveys, LLM observability, air tracking, and more.

(00:40:39):
Everything PostHog offers comes with a generous free tier that resets every month. More than 90% of customers use PostHog for free. You are going to love working with a team this transparent and technical, you'll see engineers landing pull requests for your issues, and their support team provides code-level assistance when things get tricky.

(00:40:56):
PostHog lets you have all your data in one place beyond analytics events. Their data warehouse enables you to sync data from your Postgres database, Stripe, HubSpot, S3, and many more sources.

(00:41:07):
Finally, their new AI product analyst, MaxAI, helps you get further faster. Get help building complex queries and setting up your account with an expert who's always standing by. Sign up today for free at posthog.com/lenny and make sure to tell them Lenny sent you. That's posthog.com/lenny.

(00:41:28):
Let's go back to ways that your team operates. You mentioned having Kate. Was that her name?

Dan Shipper (00:41:33):
Yeah.

Lenny Rachitsky (00:41:33):
Okay. What else? What else do you do that you think other companies should be doing or will eventually start doing?

Dan Shipper (00:41:39):
So the Cora team, which is Kieran and Nityesh, basically-

Lenny Rachitsky (00:41:43):
[inaudible 00:41:43] that's the team, two people?

Dan Shipper (00:41:44):
That's the team, yeah. Well, with Cora, it's Kieran, Nityesh, and 15 Claude Code instances, so it's more powerful than you think.

Lenny Rachitsky (00:41:53):
I love that. This is just, again, a glimpse into the future.

Dan Shipper (00:41:58):
One of the things that we do that I think is really cool, and they basically invented this, I had nothing to do with this, is they invented the idea of compounding engineering. So basically, for every unit of work, you should make the next unit of work easier to do.

(00:42:16):
So an example is, in a Claude Code world, where you're not coding a lot, you end up spending a lot of time essentially typing PRDs. Like, "Here's a document with exactly the stuff that I need to do," right? And so you could just be like, "Okay, cool. That's my job now. I'm going to just write PRDs." And so each successive PRD, it's the same amount of work.

(00:42:45):
Or you could spend a little bit of time being like... There's a sort of platonic ideal of a PRD. And what I'm going to do is write a prompt that can take my rambling thoughts and then turn that into a PRD. And so you spend a little bit of work to make all of the next PRDs that you're doing easier to write because you're writing less of them.

(00:43:08):
And so finding those little speed-ups, where every time you're building something, you're making it easier to do that same thing next time, I think gets you a lot more leverage in your engineering team.

(00:43:20):
And so, yeah, we have Kieran and Nityesh. And Cora, it just became public. It was in private beta. It had 2,500 active users. And there's millions of emails going through it. And that's one of the products that we do as a 15-person company. It's kind of crazy.

Lenny Rachitsky (00:43:37):
It is crazy. How do you do the speed-up thing? Is it prompts that they continue to refine [inaudible 00:43:44]?

Dan Shipper (00:43:44):
A lot of it is prompts, and automations, and stuff like that. Yeah.

Lenny Rachitsky (00:43:47):
Got it. For automations, what's the tool? What's the tool you use for automating automations?

Dan Shipper (00:43:52):
What they're using a lot of is Claude Code. So you can do slash commands in Claude Code, which are repeated prompts that you're doing.

Lenny Rachitsky (00:44:01):
Got it. Okay. So basically they're building a library of prompts that make the process, of, "Here's what I want to build," to a good solid PRD that you can feed into Claude Code more correct and more efficient?

Dan Shipper (00:44:13):
Exactly.

Lenny Rachitsky (00:44:14):
Super interesting. And they just keep a file or they put this into a project? Is that how they store this stuff?

Dan Shipper (00:44:14):
It's a GitHub. It's a GitHub GitHub-

Lenny Rachitsky (00:44:22):
[inaudible 00:44:22].

Dan Shipper (00:44:22):
... where they can share it with each other.

(00:44:24):
Another thing that they do, which I think is very cool, is they use a bunch of Claudes at once, but then they're also using three other agents. There's an agent called Friday that they love.

Lenny Rachitsky (00:44:36):
That's an AI Asian product called Friday?

Dan Shipper (00:44:38):
Yeah, yeah.

Lenny Rachitsky (00:44:38):
Hadn't heard of that. Okay, interesting.

Dan Shipper (00:44:40):
There's another one called Charlie that they really love. And in particular, I think the thing they like about Charlie... We have a whole video about this, which I can send to you.

Lenny Rachitsky (00:44:47):
Yeah, I'll point to it.

Dan Shipper (00:44:48):
They did an S-tier through F-tier of AI agents, which I think is so funny. And one of the things I really like about Charlie is that it lives in GitHub, so when you get a pull request, you can just be like, at Charlie, "Can you check this out?" And that seems to work really well to have different agents that have maybe slightly different perspectives. It's like different people that have different perspectives and have different taste.

(00:45:15):
Kieran, he's one of those serious Rails-files, who they just love Rails, and they love the way that Rails feels, and so I think he has a real sensitivity to... Okay, this agent, ChatGPT for example, it feels very terse, and minimal, and professional, and it has a particular kind of style that maybe he likes. Versus, I don't know, Claude is a slightly different style. And I think all of that is so interesting that these things have personalities, and that that changes what you might want to use it for or why you might want to use three of them at once.

Lenny Rachitsky (00:45:49):
That is so fascinating. It makes me think about Peter Deng's conversation again, where he talks about his hiring strategy and one of his key lessons. And he ended up hiring the current head of product for ChatGPT, the current head of marketing at ChatGPT, the current head of engineering because he hires these incredible people.

(00:46:07):
And his philosophy is to hire a team of Avengers, where everyone is strong at certain things, and together they're the perfect team, versus everyone... versus the best at everything. And it's interesting that you can almost do that with different product, different agents from different companies.

Dan Shipper (00:46:22):
You definitely can.

Lenny Rachitsky (00:46:23):
And it makes me feel like there's a bigger market than people think potentially, where people will want different companies, agents, not just all Devins or not all Codexes.

Dan Shipper (00:46:30):
I think there really is. It's definitely not one agent to rule them all at all.

Lenny Rachitsky (00:46:35):
So interesting.

Dan Shipper (00:46:36):
Yeah.

Lenny Rachitsky (00:46:36):
Oh, my God. The two people on the Cora team, what's their background? Are they both engineers or what are they?

Dan Shipper (00:46:42):
They're both engineers.

Lenny Rachitsky (00:46:43):
Okay.

Dan Shipper (00:46:44):
Kieran's got this crazy background, where... They both have really interesting backgrounds. Kieran's got this crazy background, where he was previously VP Eng at a startup, so was effectively the CTO of a startup, or maybe two startups, and was one of the founders. But before that, he was a composer, a professional composer. And before that, he was a baker. So we did a team retreat in France last year, and he taught us all how to make croissants. My croissant was horrible. His was beautiful.

Lenny Rachitsky (00:47:14):
Seems [inaudible 00:47:16].

Dan Shipper (00:47:16):
And generally, I think that kind of multidimensional type of talent is the kind of person that I love having at Every. Because we're all generalists. We all want to use AI for all these weird, awesome, creative things. And someone who has that background is going to have a good taste for not only agents, but, "What should the landing page look like," or whatever. Which I think is increasingly important, where you're trying to scale a team of generalists of 15 people to five products. So that's Kieran's background.

(00:47:43):
Natasha's background is... I'm jealous because he only started learning to code when ChatGPT came out. He had wanted to learn to code forever, and he's only known how to code in an AI era. And I keep telling him, "Dude, I learned to program in middle school from books." I had to go to Barnes & Noble and buy a book. And there was nothing... I couldn't Google any-

Dan Shipper (00:48:00):
I had to go to Barnes and Noble and buy a book and there was nothing... I couldn't Google anything about why this function wasn't working.

Lenny Rachitsky (00:48:08):
No Stack Overflow even back then.

Dan Shipper (00:48:10):
Yeah, yeah. There wasn't that overflow. There was weird BB net forums and stuff that I was like 12 and I probably shouldn't have been on there or whatever. So he has gone so much faster than any other engineer, I think in a pre AI era. And I see the same thing in the rest of the company. I think there's this huge question about what happens when kids... Entry level jobs are taken away by AI. And my take is like that's worth thinking about and it's possible that that might be a problem at some point. But my take is whenever I see a kid with ChatGPT, I'm like, holy shit, they're going to grow so much faster than any other person that I've worked with. We have this guy Alex Duffy who works with us, he writes for Context Window and he just launched, we taught AIs how to play diplomacy with each other, which is really cool.

(00:49:08):
And he did that whole thing and I think he's really, really, really talented. And when he came to us, I guess almost a year ago now, it was one of those classic cases which I've seen over and over at every... Which is, you have great ideas, but you're not a good writer yet and it's really hard for me to do anything with you until you're good enough at it. So I have to give you small little things until you get better and blah, blah, blah, whatever. And what I noticed with him is he was just making a year. He made a year's worth of progress in two months because every time I sat down with him and told him, okay, here's how you tell a story. Here's how you think about a headline. He recorded all of it, put it into a prompt, and he never made the same mistake twice.

(00:49:49):
And I think he's so much accelerated from where he would have been because of this stuff, and I see that in lots of other parts of the work. So Natasha is another good example. And so I think generally people are going to figure out that some 20-year-old with ChatGPT subscription is super powerful if you just mentor them. And I think that's great.

Lenny Rachitsky (00:50:11):
Man, there's so many threads I could follow here. There's all this fear of entry level people will never... The roles are disappearing for entry level people and so how will we ever have senior people if these people can't learn to do things as an entry level person? And what you're saying is ChatGPT and these tools help you accelerate really quickly so you don't really need to be at the bottom rung for a long time.

Dan Shipper (00:50:33):
Yeah. You're effectively learning how to be one level above the entry level from the beginning and this is sort of my whole allocation economy thesis where when you look at skills are going to be valuable in the AI era, one big group of skills are the skills of managers. Today, they're human managers, tomorrow everyone's a model manager. Right now, AI is not... Right now, management skills are not broadly distributed, because it's very expensive, another expensive thing that... So 8% of the workforce is managers. It's now going to be much cheaper to manage, so more people are going to have to do it. And so that's the thing that kids, 20-year-olds, whatever, I see is now are going to start to have to learn in addition to, it's not like you can just say, okay, go do it and then come back. You have to be able to go into the work that's being done and help make it better. But they're learning both at the same time. They're learning how to manage and how to do the actual work so that they're good at it.

Lenny Rachitsky (00:51:36):
And the managing here is managing agents. Right?

Dan Shipper (00:51:41):
Yeah. You're managing AI.

Lenny Rachitsky (00:51:43):
And so coming back to your point about how this core team, and I guess you said everyone doesn't write code, zero code written, now it's just managing agents that are writing code for you.

Dan Shipper (00:51:54):
Yeah.

Lenny Rachitsky (00:51:55):
Okay. I've never heard of a company at this stage, so this is extremely cool. So the workflow is they give it, here's what I want. I refine it using this cool prompts library that they build on and agents build code, write the code. Then basically the time is spent reviewing code and then reviewing the output. What does it look like? What does it feel like? And then continuing to refine, wow. So you guys are at where Michael from Cursor said we will be. So I chatted with him a few months ago. He said in a year, this is where he thinks the thing will be. We're not looking at code anymore. You guys are already there. Although you were looking at code. Okay, you're still looking at code.

Dan Shipper (00:52:33):
They definitely are looking at code. So you're doing a code review before you do anything. And I do think Danny, who runs Spiral, which is the cloud code for content tool I was talking about that we're building, he spent a couple of days digging into the internals of some third party library that we were interested in just because it's helpful to know, it's helpful to understand those things, but then he's not actually writing any code. Once he understands it, he's just off telling cloud code what to do. And I think that's really important.

Lenny Rachitsky (00:53:08):
This is an insane milestone we're hitting here. There's this sense we're getting to a place where you don't need to really understand code, you don't have to write any code. We'll get there and you guys are there. I think this is so easy to overlook how wild this is. You have a product team not writing code at all.

Dan Shipper (00:53:26):
It is really wild. I think it's really wild in particular, just having a small group of people that have... Everyone has all these different skills. Everyone's a generalist, everyone's AI forward. So what you can do in an environment like that with just still a small team is crazy. And you're kind of inventing all these new principles for how do we work together, how do we do engineering, all that kind of stuff. And I think that's what makes the writing... That's why I like doing that is because the writing that we do from that I think is really good because we can talk about it from a sort of position of experience, but I do want to say something else which is we're not at a point yet where the people that work at every could do what they do if they didn't know how to code.

Lenny Rachitsky (00:54:08):
Yeah, this is what I was going to ask.

Dan Shipper (00:54:10):
Which is a different bar, and I think for a long time it's going to be valuable to know how to code for a long time, but this is a progression that is not a new progression. So for example, when I was in middle school learning to code, the new hot thing was scripting languages, which is Python and JavaScript. But if you were a real programmer, you would understand the language underlying Python and JavaScript, which is written in C. and scripting language weren't totally real. And in order to really do anything interesting, you had to be able to learn both parts of the stack. Same thing for C programmers, when I guess in the seventies C was invented, it was like you got to be able to write assembly.

(00:54:59):
And English is just a layer on top of scripting languages. So I think all of those things were right in the sense that there's... Especially during transitions, there's a lot of reasons why it's important to be able to go down a layer in the stack and it gets less and less frequent over time, but that still takes a long time. And there's some times when even if you're a JavaScript or a Python programmer, it's useful to know how that stuff works, how it's written, and see how it's implemented. Today it's much less important than it used to be, but that took 10 or 20 years. And I think that the same thing is going to be true for programming. Having that skill is super important and will accelerate you significantly. It will sort of start to get less important over time, but we're not close to that yet.

Lenny Rachitsky (00:55:44):
Okay. That's a really important point. I'm glad you went there. So do you have a sense of how far we might be from you hiring someone to build another product that isn't an engineer?

Dan Shipper (00:55:54):
Like a real SaaS product?

Lenny Rachitsky (00:55:57):
So hey, we have this idea we want to bring someone on to actually lead it.

Dan Shipper (00:56:00):
Very far. Not within sight, but there's a lot of things that could be products that are a level down from that I think that you could do almost now. So an example, we were talking about DIA, the new AI browser from the browser company. DIA has these things called skills, which are effectively little AI apps that you can run in the browser. You can prompt them and they run on the web page and do work for you. A non-technical person can build that, same thing for custom GPTs from ChatGPT. A non-technical person can definitely build that. So I think while I will definitely maintain that we're not anywhere close to anybody being able to build a conventional SaaS app with zero programming knowledge, aside from just a demo, there are going to be other forms of software.

(00:56:55):
One of my things is like software is becoming content. There's going to be other forms of software that don't look like the software today, but you can run, start and run as a business, as a non-technical person even if you don't know how to code. And that'll happen very soon. I mean, it's already kind of happening. It doesn't look like the thing that you're asking about. It's sort of like the difference between a Hollywood movie and a YouTube video.

Lenny Rachitsky (00:57:17):
I think that's really reassuring to a lot of people. Basically what you're seeing is AI just supercharges people who have a skill and allows them to do a lot more.

Dan Shipper (00:57:25):
Yeah.

Lenny Rachitsky (00:57:26):
Okay. Is there any other way that you guys operate that is really interesting that might be worth sharing that helps you operate really quickly, helps you do more with less?

Dan Shipper (00:57:38):
I mean, I would love to talk about how we think about building products, what products to build, what do we end up building? Because I think that there's something sort of special about it that probably there's a playbook that is useful for people. So when I think about... This is only sort of snapped into focus recently. So a lot of this was just doing it intuitively without really a thought for it. But when I think about the kind of things that we have ended up incubating, it's basically goes back to something I said at the beginning, which is there are these things that were historically really expensive that only rich people or big companies could buy. So a chief of staff for your email, I think a therapist or a lawyer is another interesting example. Someone to organize your closet or organize your computer is another example. Someone to go straight for you, that are becoming orders of magnitude cheaper so that everyone can use them even if you're at a small startup.

(00:58:39):
And so basically when you're running, we are sort of this AI first company. You're running into all these little things where you're like, I wish I had a ghost writer right now, but ghost writers are really expensive. Or I wish I had a lawyer but it would cost me like $25,000. Lawyers are really expensive and there's a lot more demand for those services than can be fulfilled because they're so expensive. And what AI does is it allows you to be like, oh, I could just use cloud for that. I can use ChatGPT for that. And so you're able to use the demand that you have that we can afford a lawyer. We have ghost writers, but there's a lot more that we can't do because we can't afford it. So we still have our lawyer and we still have our ghost writers, but we just do a lot more of that stuff.

(00:59:27):
And so we notice that. We start to then use ChatGPT and cloud first, these general purpose tools to try it and see is this useful? Does this actually work? All that kind of stuff. And then if it does, we will unbundle it into its own separate thing that becomes an app. And I think what's really special about this time is the entire game board has been totally reset in terms of things you can build. Where five years ago it was like you're going to build another Notes app. We've been building notes app for forever, another B2B SAS app. It's all the same stuff in slightly different packaging. And now it's totally new territory. No one knows what's going on. Everyone's inventing it as it happens. All these new workflows are being created in a very similar way to, I don't know, for example, when spreadsheets were first a thing on computers, we were figuring out all these new workflows on spreadsheets.

(01:00:24):
They got unbundled in the B2B SAS, same thing for ChatGPT and Claude. And what's really cool is you can be like, cool, I'm using using ChatGPT for this. It's really useful for me. And you might be one of the first people to really notice that. And then because everybody that works at Every is AI first and came to us because they reads Every, they read Every, so we all have the same vibe and we're all kind of doing similar stuff. They become our first users. So we measure the success of the product by is it a banger inside of Every, monologue the app that I was talking to you about, everyone just started using it and we're like, okay, we've got something here.

(01:01:05):
And what's really interesting then is if everyone inside of Every uses it and people read Every, they have a similar vibe to us too, so they become the next set of users. And that's a really, I think, interesting pipeline for building applications or building apps. It's a totally new greenfield so that all the stuff you're thinking about, it's probably new, which is really cool. And over time, what I think is organizations like ours, people who are playing at the edge, we're doing things that in three years everybody else is going to be doing. So it may be kind of niche for now, but it will be a big deal in three years when everyone else has the same needs that we do.

Lenny Rachitsky (01:01:45):
That is really cool. What I'm hearing is GPT wrappers are a good idea and are worth building.

Dan Shipper (01:01:50):
100% thank you. GPT wrappers are amazing and they've been much maligned for absolutely no reason and people don't understand how absolutely valuable they are.

Lenny Rachitsky (01:02:03):
I think there's also just you guys raised a sip seed round. This is a good time to maybe talk about that. Just these products don't have to become some mega-billion dollar hits. You kind of have this portfolio of companies, you have the content business. So I think there's a really interesting approach to how big these need to get to be successful. Maybe just talk about that.

Dan Shipper (01:02:25):
Yeah. I really want Every to be an institution that teaches people how to live a better, more human life with technology, particularly with AI. And both teaches them how to do it with writing and the content we make and then builds tools for them to do that. But I think fundamental to building an institution is, at least for me, the way I would like to do it is I want internally it to feel like this creative playground where we have the opportunity to take risk and do stuff and do weird stuff that just doesn't make any sense. We can't justify anyone, but we just feel like it would be fun. And so I think I'm always playing with that dynamic tension between institution serious, we want this to be lasting and important and it should just be fun. Let's play around. And I think having that tension is really valuable.

(01:03:16):
And so I've always been sort of hesitant to raise a lot of money because I think it locks you into having to be that serious thing that's totally going for it. And there's lots of companies that figure out that balance. But just for me personally as a founder, I'm like, I want to keep the optionality alive and I want to keep the kind of playful feeling alive. And I think part of that comes from I know I have the control to do what I want more or less. There's probably also some deeper psychological things going on there, which I'm happy to talk about if you want to get into it. But I think there's also just... That's what I want. And so when we started Every, we raised a very small 700K pre-seed round, and this was at the height of the creator economy.

(01:03:59):
So we both started our newsletters. He and I started our newsletters around the same time. It was the hypest, craziest thing. People were throwing money around. It was wild. But we raised 700K because it was like, I want to raise enough for us to be able to experiment, have a little cash cushion, but not so much that it locks us into anything. And we sent an email to all of our investors being like, and you're one of our investors, so you've probably got this email.

Lenny Rachitsky (01:04:22):
Tiny investor. But I'm in there, I'm in there.

Dan Shipper (01:04:26):
We sent an email to everyone being like, this is probably not a venture business, so you should not expect us to raise again. And we even raised on this slightly modified safe that gave everyone the option to convert to equity in three years, even if we didn't raise more money. So we did it in a way that allowed us the option to get really big and do the traditional thing and also the option to do it the way we want to do it. Maybe it's not a huge business, but we love it. That's great. And we did the same thing for this recent round where we raised up to 2 million from Reid Hoffman and starting line VC. And we did it as what I've been calling a sip seed round, which is basically they've committed $2 million, but we can pull it down whenever we want and we just do it on a safe at a set cap.

(01:05:12):
And for me, that's really helpful because it allows me psychologically to take a lot more risk. If we go to zero on the bank account, I can get more money. Great. I don't have to think about it. But what's also really helpful is I'm not, and the rest of the team is not staring at a gigantic number in the bank account being like, cool, we can burn this. Let's burn it. And also for our investors, I think Reid very much wants us to succeed, but I don't think he cares what size of business this is. I think he's more philosophically aligned with the thing that we're trying to do. And if it becomes a huge business, he's psyched for it. And I think that kind of alignment is what I was looking for. I think there's this core creative spirit to the thing that I want to maintain and I really care about having a big impact.

(01:06:03):
But I think there's a lot of ways to have an impact. And one of them is building a $10 billion business. I think another way is really changing how people see the world, see themselves in the world. And I think that's what stories do. And you don't necessarily... Sometimes you do that by building a gigantic company, but you don't necessarily always have to do that. A lot of the stories that we care about most are from people who maybe they weren't rich at all. And so I really like creating this place where we can make a really good business. And I care a lot about that. But also the core of the soul of it is about changing how people see themselves in the world.

Lenny Rachitsky (01:06:40):
I love that you've kind of innovated a new middle ground way of fundraising, not bootstrap and not just regular VC. It's a seed. And I love that this two... If I raised 50 million, it'd be like, okay, I get it. Let's not put 50 million in our bank account, but you do have 2 million. It's too much for us. We don't want to see that in our account.

Dan Shipper (01:07:01):
That's another thing. And we'll see how this ages. I might be back here in two years crying the blues because we didn't raise enough money or whatever. Who knows? But that's the other thing is I do think we can get so much further with very small amounts of money. Like Cora, I think all in to build Cora, we've spent maybe 300K, Maybe. That's crazy because-

Lenny Rachitsky (01:07:24):
And that includes salaries?

Dan Shipper (01:07:27):
Includes salaries. Yeah.

Lenny Rachitsky (01:07:27):
Wow.

Dan Shipper (01:07:28):
This product was not even technically possible even if you had billions of dollars three years ago. Not possible because you can't do email summarizing and automatic responses and all that kind of stuff without GPT. So not only was it totally impossible, but now we can get with two engineers, we can get the amount done that would've taken a team of 20 people. And I think that means that we need less money. And I don't think that VC has really caught up to that yet. And I think there are other companies that are doing... There's a term called seed strapping, so there are other companies that are starting to wake up to this too. And I'm curious about how it changes the VC model. For sure for us, we have a specific incubation model, which is a bit different from a VC model. And I think there's some differentiation in the stuff that we can do with founders, which is kind of cool. But yeah, I'm just trying to figure out a shape that works for me and that's different from other people and we'll see how this goes.

Lenny Rachitsky (01:08:41):
We'll revisit in a couple years. Seems like it's going great from the outside. I'm going to ask about a couple other things before we wrap up. One is around this consulting arm that you have. I think it's really interesting because like I said, I feel like this could be a billion-dollar business. I feel like every company right now is trying to figure out what the hell's everyone else figured out that we're not doing. I've had so many emails from chief product officers at companies being like, can you introduce me to some chief product officers that have done cool things with AI that we should learn from? So many people and I would just introduce them to each other and it's cool because you guys are basically solving that problem for a lot of companies.

(01:09:18):
So one is just maybe share a bit about what that side of the business for folks. And then two, I feel like I imagine you've seen companies that have done this really well, have adopted AI, things have worked really well, they found really good productivity gains, and then you found companies that don't. What do you find is the difference between those two?

Dan Shipper (01:09:35):
I love this question and I have a very specific opinion about this. So one, yeah, the consulting arm, basically we spend all of our time playing around with new models, writing about them and building stuff with them. And we have a big audience. So naturally we've gotten companies over time being like, can you just come and teach us how to do this? And so we started to do that. This is pretty nascent. It's probably been over the last six to nine months, but it's a pretty big business now. It'll probably double this year. Last year we did about a million. Maybe it'll be more this year. We'll see. It depends on a couple... We have a couple of big contracts out, so it might be way more than that.

Lenny Rachitsky (01:10:13):
A billion. I predict a billion dollars in a few years.

Dan Shipper (01:10:17):
But yeah, basically people are like, can you come help us learn how to do this? So what we do is we spend some time going and researching your organization. So we go in and try to understand what are all the different teams doing, what are the repetitive tasks, some of the stuff we were talking about earlier. And then what we will do is first we present a little report, tells you here's everything that we found. Here's not only that, but you have a chatbot where you can chat with all the interviews that we did and you can pull out your own insights. We have a whole dashboard where it shows you, here are the teams that are really into this, here are the teams that are not. Here's how much leverage you might be able to get on different teams based on the interviews and based on the AI analysis.

(01:10:57):
It's pretty cool. And that's an app that I coded over a weekend with Devin a year ago. And then Alex runs part of the consulting has helped upgrade it. Then what we do is we have a training curriculum. So we go in and train each team and we customize it based on the interviews that we do. Because one of the interesting things about AI is it's such a general purpose technology, and I think people who work inside companies, 10% of them are like, I'm super curious about this. 10% are like, I will never touch this. And 80% are like, if you tell me how to do it for my job, I'll do it.

(01:11:31):
And so we customize the training to be like, here are the exact prompts you're going to use and here's the exact situations you're going to use them. And that really, I think helps drive the adoption. We spend four weeks with each team, an hour a week, that kind of thing. It seems to be really cool. And then we'll often also after this, go and build automations and do some of the AI operations stuff we were talking about earlier. Companies really like it. I think we work with a lot of big hedge funds and PE firms and big companies, all that kind of stuff. To your-

Dan Shipper (01:12:00):
Companies, all that kind of stuff. To your second question, which is, "What separates the good companies from the bad, or the companies that end up adopting this?," I think the number one predictor is, "Does the CEO use ChatGPT?," or insert your own chatbot. If the CEO is in it all the time, being like, "This is the coolest thing," everybody else is going to start doing it. If the CEO is like, "I don't know, this is for someone else," no one else is going to be able to lead that charge, and they're either going to have ... Either they're going to be negative on it, and so definitely no one's going to do it, or they're going to have way unrealistic expectations because they have no intuition for what's possible, and they're just going to get really disappointed.

(01:12:47):
But the CEOs that are using it all the time are able to both drive the excitement and set reasonable expectations for what can be achieved, and so those things end up working really well, and the people that do this really well ... So, for example, we work with a hedge fund called Walleye, which I had the founder on my podcast, AI and I, a few weeks ago, their gigantic $10 billion hedge fund. One of the things that they do, which I think they're basically the model for how to do this, first thing you did, which a lot of CEOs are doing is send the, "We're an AI-first company" email. Everyone's got the memo.

(01:13:20):
You just got to really do it, and one of the things he said in his memo, which I love, is, "I wrote this email with ChatGPT, and you should too." So you got to like ...

Lenny Rachitsky (01:13:30):
In the memo.

Dan Shipper (01:13:30):
Yeah. You got to lead from the front in that way. And then, what he does in, I think what a lot of other really cool companies do is they're doing weekly meetings where people share prompts and share use cases. They do a weekly email to their entire company, being like, "Okay, here are our usage stats for ChatGPT. Here are the people that came up with a new prompt and contributed to it."

(01:14:00):
Create this sort of awareness and momentum, because going back to the point I made earlier, about 10% of people are early adopters, those are the people inside of a company that you need to find and highlight because they're going to just go spend all this time figuring out what works, and then all you have to do is translate what they learn into the rest of the organization. And so if you create forums for them to be rewarded, you're going to automatically transfer a lot of their learnings to everybody else, and encourage more of it, and I think that's kind of the secret.

Lenny Rachitsky (01:14:32):
That is awesome. I love this advice. So just to reflect back, what you just shared, a few kind of tactics you find that you encourage within companies, one is just send this memo, the Toby memo. I don't know if that's the right way to describe it, who I think it was first along these lines just, "We're AI-first." It's going to be part of your performance review.

(01:14:50):
It's going to be asking, "Can you do it in AI before you could talk to anyone else?," all these things, and then just note, "I wrote this using ChatGPT's," it's a great idea. This idea of a weekly meeting, so it's like a live or Zoom meeting, where people share, "Here's the thing I've learned about using AI," and then this weekly stats email of, "Here's how much we're using ChatGPT across the org. Here's some people that did some awesome work."

Dan Shipper (01:15:12):
Yeah.

Lenny Rachitsky (01:15:13):
Amazing. And I especially love this very simple heuristic of, "If you're a CEO, uses ChatGPT or Claude, or whatever daily, it's going to work out."

Dan Shipper (01:15:22):
Yeah.

Lenny Rachitsky (01:15:23):
That is super cool. I know it's early, but what kind of impact have you seen from a company, kind of leaning into this and adopting AI widely? Anything you've seen either anecdotally or numbers-wise?

Dan Shipper (01:15:34):
It's early. It's really hard to say other than ... I think generally, people who do this well now feel like they can do way more work than they used to without having to hire more people, and so they're just going further faster at the same budget. I don't see a lot of people being like, "Cool. We're going to fire a bunch of people."

(01:15:58):
Also, I don't really want to do consulting work like that. That sucks. But we've never had to say no. Mostly, people are like, "Cool. I'm just going to go further with the people that I have."

(01:16:08):
I think also, back to kind of the first point I made about reshoring American jobs, I have seen some companies, not the ones that we worked with, but I have seen some companies of people that I'm friends with, where they're like, "We have a call center somewhere, but I think I can get the same amount done with two employees in the U.S. that use one of these customer service platforms." They're still not totally automatic. I think that Klarna CEO thing, that was bullshit. But, yeah, you can have a couple people in the U.S. that maybe you pay a little bit less to than you would for 100 people somewhere else, and obviously, that's the calculus that everyone has to make for themselves, but I've definitely seen that happen, and yeah, I think that's the get more done with the same amount of people.

Lenny Rachitsky (01:17:03):
Maybe to close out our conversation, I want to come back to this idea that you referenced, but I want to spend a little more time on this, which is this idea of the allocation economy. If I understand it correctly, we've been in this knowledge economy, where people get paid to do a thing, and your thesis is that we're moving to this allocation economy, where the manager skills become more important, and we're going to be spending more of our time managing. And I think what's amazing about this is it also tells you which skills will matter more in the future, which is something I think a lot of people are thinking about. So maybe just answer that question and share whatever you think is important to share to give people a sense of what you're thinking.

Dan Shipper (01:17:38):
Yeah. So this is based on our article I wrote two, two and a half years ago. So this is back before agents were even thought of as viable. And I was really trying to think about, "How do I express what ... In my experience, using this every day, what skills are useful for me?," because I think that'll be the case for a lot of other people, and I think that's kind of the best method, I think, to do these sorts of predictions, is you have to be doing it all the time yourself, and then that informs your opinion about this stuff.

(01:18:14):
So what I noticed using, at the time, like GPT-3 or maybe GPT-4, was that I was spending a lot of time, for example, thinking about, "How do I communicate the problem? How do I gather the right information for the problem? How do I put it in the right way so that the model that I'm working with gets it? How do I pick which model to give it to you, and how do I maybe divide up the task to be like, 'Okay, this model does this, this model does this,' based on what I know to be like, 'What's good and what's bad?'? How do I give them feedback?"

(01:18:50):
"How do I have a vision for what I want and a set of criteria for whether it's good?" All that stuff is exactly how I found myself using these tools, and I was like, "Oh, that's just managing." And once that clicks for you, I think you'll start to see a lot of other things. So a really good example is there's a big complaint that it's like, "Well, how can I have AI do this? I can't trust that they're going to do it well, so I just do it myself."

(01:19:22):
And I'm just like, "Yeah, that's exactly what Every first-time manager says." You always have this problem, where you're like, "Okay. Well, if I delegate it, it's not done in the way that I want it to be done. If I do it myself, I get no leverage." And so that's how a manager has to learn how to be a manager is like, "When do I lean in and maybe micromanage a little bit, and when can I delegate, and how can I trust it, and how do I divide up the task and all that kind of stuff?"

(01:19:45):
And so I think there's a lot of overlap in those skills. And those skills are not broadly distributed right now, but they will be in the future because it will be so much cheaper to be a manager.

Lenny Rachitsky (01:19:57):
And specifically, I was looking at the article you wrote, the skills that you highlight will be more valuable is evaluating talent, vision, taste, and to your point, when to get into the details, when it makes sense to dive in.

Dan Shipper (01:20:11):
Yeah.

Lenny Rachitsky (01:20:12):
Awesome. And then, there's also kind of a connected point you made that you referenced, which is that generalists will become more and more valuable in the future. You mentioned that everyone at Every is a generalist.

Dan Shipper (01:20:20):
Yeah.

Lenny Rachitsky (01:20:21):
Share a little bit about that.

Dan Shipper (01:20:22):
Yeah. I find ... I mean, maybe it's because I'm a generalist, so you should take this with a grain of salt.

Lenny Rachitsky (01:20:27):
Same, same.

Dan Shipper (01:20:28):
But I think that's one of the things that has made AI so awesome for me, is I love to dabble in different things. So it's like in one day, I can be coding an app, and making a video, and making images, and writing, and all that kind of stuff, and ChatGPT is right there with me. And I think basically what has happened, as civilization has progressed from Ancient Greece to now, is what we've discovered is the more that we specialize, the better we can coordinate across many different people. And so it's like the Adam Smith, like there's a pin factory and someone's making a pin or whatever his thing is, is specialization against our trade. And there have been a lot of really good impacts of that.

(01:21:18):
One of my favorite examples of this is back to Ancient Greece, Ancient Athens. Athens was a civilization of generalists, at least for citizens. They have a bad history with women and people who are slaves, but let's just put that to the side for a second. If you're a citizen, generalist. You could be expected to be a fighter, a judge, a juror, maybe a general.

(01:21:46):
You could expect it to have many different roles inside of your society in your lifetime. That changed though, because Athens became an empire. And as it became an empire, if you're going to send a general off to go and invade Sicily or whatever, you want that person to be pretty skilled. And so it started to break the general kind of thing into people start to have specific roles, and they coordinate with each other and all that kind of stuff, and I think that pattern has actually been really good for developing civilization, but it's also, in a lot of ways, it is not as fun. It's actually really cool to be a well-rounded person. And I think the interesting thing about AI is that it's a little bit like, you can think of it like having 10,000 PhDs in your pocket.

(01:22:36):
It knows so much about every little branch of human knowledge and every art form and every way of making things or building things, and you just have access to that, so it's doing a lot of the ... It's good for doing a lot of the specialized tasks that you might've had to spend 10 years getting good at learning about this particular species of cicada, so you know exactly how they reproduce. But now, you've got this thing in your pocket that can tell you all about that in any given context at any given time, and so you're empowered to jump a lot more between all those different domains of skill, and you can get more done as, for example, like a founder, where I think we can stay at 15 people much longer than we would be able to. So the people inside of Every can stay generalists for much longer, and I think that that may sort of ripple out into the rest of the economy, where instead of gigantic, massive corporations, where each person is doing one little button turning, you have many more smaller organizations with more generalists, and I think that would actually be a really good thing.

Lenny Rachitsky (01:23:44):
This reminds me, I was talking to my personal trainer that I'm trying out for a little bit, and she said that she's a very big vision, kind of high-level person, and not good at executing, like we're staying organized, and ChatGPT is such a godsend for her, because she's just like, "Here's what I want to do roughly. Just help me get it done."

Dan Shipper (01:24:01):
That's great. I love that.

Lenny Rachitsky (01:24:03):
And so, yeah. And it really made me think about just how much value all this stuff is going to unlock. This was amazing. It was everything I wanted it to be. But with that, we reached our very exciting lightning round. Dan, are you ready?

Dan Shipper (01:24:14):
I'm ready.

Lenny Rachitsky (01:24:15):
Here we go. What are two or three books that you find yourself recommending most to other people?

Dan Shipper (01:24:21):
Well, I already recommended one, which is War and Peace. Definitely got to read that. If you want a like Tolstoy primer, I would read The Death of Ivan Ilyich. Another good one is A Swim in a Pond in the Rain, which is by George Saunders, and that's a collection of Russian short stories that is also about writing. And in particular, I really like the Russians because a lot of the Russian novelists are dealing with the effects of technology on the traditional Russian way of life, and they're very kind of in this really interesting middle ground between a sort of romantic outlook on the world and a more rationalist like, " We're progressing, we're making progress."

(01:25:02):
And that's one of the things you'll find in Anna Karenina, oh, and ... God, what's the guy's ... Levin is out in the fields with the peasants, doing the scythe thing. That's Tolstoy kind of thinking about, "Oh, what would it be like, instead of being a nobleman who's trying to make farms way more efficient, I was just like with my scythe, that was really happy?" Anyway, so they're dealing with a lot of similar stuff to, I think AI.

(01:25:27):
The Master and His Emissary is another really good one, and that's about basically how the different hemispheres of the brain view reality. It's really, really good, and I think it relates to a lot of AI stuff too. Yeah, I think those are my three or four. Yeah.

Lenny Rachitsky (01:25:44):
Excellent list. I think nobody's mentioned any of these, so that's always a good sign. Do you have a favorite recent movie or TV show you've really enjoyed?

Dan Shipper (01:25:53):
Yes. I really love Deadwood. Have you seen it?

Lenny Rachitsky (01:25:58):
I absolutely love it. I remember when they stopped it for some reason. I think he had to go do something else at HBO. It was so sad.

Dan Shipper (01:25:59):
Yeah.

Lenny Rachitsky (01:26:06):
It's amazing, yeah.

Dan Shipper (01:26:06):
Yeah.

Lenny Rachitsky (01:26:07):
Yeah.

Dan Shipper (01:26:07):
David Milch is incredible, national treasure, incredible writer. But what I really love about it, and I only recently watched it, is he talks about Deadwood being about how order forms out of chaos. So it's this like frontier town, people are going to it, and there's no law, there's no rules. And by season three, there's a mayor, and all the industry has come in, and it's like a real proper town, and I just love that. And I think there's a lot of parallels from the Western frontier to technology frontiers, and so I think that show is a really interesting study in that kind of dynamic.

Lenny Rachitsky (01:26:50):
I love how everything connects to how tech works and how AI came to be. I love this.

Dan Shipper (01:26:57):
Thank you.

Lenny Rachitsky (01:26:58):
Do you have a favorite product you've recently discovered that you really love?

Dan Shipper (01:27:00):
I don't have a good answer for that because I just spent a lot of time using our internal products, but my stock answer is Granola. So I do really love Granola. My one gripe with them, and I hope they listen to this podcast, is I really want to export all my notes. I want an API, but other than that, I think it's a fantastic product.

Lenny Rachitsky (01:27:18):
That is definitely the most mentioned product in this segment for the past couple months, so good job, Granola. I can't help but mention, you get a year free of Granola if you become an annual subscriber of my newsletter. Well, what a freaking deal. And not just you, but your whole company gets free Granola for a year. What a deal.

Dan Shipper (01:27:34):
This is not a paid promotion by me. That's just how I feel. So I'm glad it's part of the bundle.

Lenny Rachitsky (01:27:41):
Yeah, incredible. Okay. Do you have a favorite life motto that you often come back to find useful in work or in life?

Dan Shipper (01:27:47):
So basically, I use ChatGPT all the time, and it has memory. So I was like, "I'm going on Lenny's podcast. What would my life motto be?," and it said, "Your life motto is witness deeply, build bravely. You prize slow, attentive seeing, whether it's reading Tolstoy, tracking meditation themes, or X-raying a David Milch paragraph." So it's hitting all the stuff I just mentioned, which is really funny.

(01:28:10):
And then, Build bravely, you turn those insights into concrete things, like Every in Quora and longform essays and all that kind of stuff. So I think there's something about that. Actually, this reminds me, this actually reminds me of the actual motto, which is ... And I didn't come up with this. I think it's like Pliny the Younger said, "Do things worth writing about, and write things worth reading." Seems like a pretty good summation.

Lenny Rachitsky (01:28:31):
Do things worth writing about and read things worth reading.

Dan Shipper (01:28:34):
Write things worth reading.

Lenny Rachitsky (01:28:36):
Write things worth reading. That should be the motto of both of our newsletters.

Dan Shipper (01:28:41):
Yeah.

Lenny Rachitsky (01:28:41):
That is really good. Okay. And by the way, I love that you asked ChatGPT, "What's my life motto?"

Dan Shipper (01:28:48):
And wait, this is interesting. So it didn't give me the answer, but inspired the answer.

Lenny Rachitsky (01:28:51):
Yeah.

Dan Shipper (01:28:52):
And I think that's actually exactly how I use it.

Lenny Rachitsky (01:28:55):
[inaudible 01:28:55] Wow. It's an extension of our brains already.

Dan Shipper (01:28:57):
Yeah.

Lenny Rachitsky (01:28:57):
Last question. I was reading somewhere, where you wrote that you stopped writing at one point. You were just like, "I need to do other things, I need to build this company," and then you realize, "I need to get back to writing," because things started going sideways. And I feel like this is such an interesting corollary to a lot of the stuff you talked about, of just things that make you happy, stay close to enjoy. Just share what happened there, because I didn't know that.

Dan Shipper (01:29:23):
This is definitely not a lightning round thing, so I'll expound, but I'll try to do it as quickly as possible.

Lenny Rachitsky (01:29:29):
Perfect.

Dan Shipper (01:29:30):
I think generally, when you're building a company, even if you do it the way that I do it or did it, which is you don't raise a lot of money and you try to stay in control, there's a big temptation to try to run the company in the way you think you should. And I have this weird thing where I'm like, "I really love writing, but I also really love business," and there were not a lot of models for me of people who had successful businesses that were also writers. It turns out there are, but I didn't know about that for a while. And so early on at Every, it was growing really well, because I was writing a lot, and Nathan was writing a lot. And when I stopped writing, the business didn't work as well because media businesses don't follow the same pattern as tech startups, because if you're a media business and you are a founder who then hires people to make the product, which is right, if you have product market fit before, you lose it, and maybe you hire people that are good writers, but that's hard. It's total opposite pattern for startups. So you build the first version of the product, and then you hire people to build the rest of it, and so that's what I did. And I also really struggled with, "Okay, what are the implications for that and for my career," and I think it was hard for me to admit, like I actually want to write because I just didn't have any examples of someone being the kind of writer that I wanted to be. And what's really interesting is three years into the business ... The business has been pretty flat.

(01:30:57):
I was pretty miserable because I was not doing the thing that I really wanted to do, and I asked ChatGPT, I was like, "Are there any examples of writers that have built businesses?" And it was like, "Yeah, Joel Spolsky, who built Trello and Stack Overflow. There's Jason Fried who I've known for a long time, and I've always looked up to, but I forgot about in this context. There is Sam Harris who's got a great podcast, and he's got a gigantic meditation app. There is Bill Simmons, who's incredible podcaster and also built The Ringer, sold to Spotify for a couple hundred million bucks.

(01:31:32):
There's a lot of these people, and there are patterns that they use to build companies that are pretty well-understood. They're just not typical Silicon Valley patterns. And so I was like, "Cool. I just want to be a writer. I think it'll be really fun."

(01:31:48):
And so I sort of flipped. I still have the builder, entrepreneur, founder part of my identity, but I sort of flipped it to be like writing is at the center, and I'm unapologetic about it, and that's actually good for the business. It's good for me and it's good for the business. And the more I've leaned into that, doing the thing that ... If you told anyone that you're starting a business, where it's like, "Well, we're going to be a newsletter, and we're going to incubate all these apps, and we're going to do consulting and whatever," they would be like, "You're nuts."

(01:32:14):
"Everyone wants to do that. Of course, Every founder wants to do that, but you have to focus. You can't write, whatever." But every time I've kind of just leaned into something that feels like the most, the ultimate luxury of my hidden secret desire, it's actually worked a lot better, and I think you end up ... What it really is, is there's a huge tax to doing something every day that you don't quite like that much, or you're not quite a fit for, and by sort of giving into those secret desires, you end up finding a shape for the work that you do and the business that you build that is good for you, and that's always going to be a somewhat unique shape from other businesses that have been built.

(01:32:54):
It's always going to rhyme with other things, but I think finding that unique shape, instead of just kind of cargo culting, like what you think a company should look like is definitely a much better way to be successful, and it's also a much better way to live.

Lenny Rachitsky (01:33:08):
I think this is going to hit hard with a lot of people who are listening, who are maybe founders or want to be founders, and this resonates with a lot of people that have been on this podcast sharing similar lessons. Dan, this was incredible. Two final questions. Where can folks check out Every, find you online, and how can listeners be useful to you?

Dan Shipper (01:33:24):
So you can find us at every.to. I'm also on Twitter at @danshipper. You can go there to check out our products, our newsletter, if you want to stay on top of AI, all that kind of stuff. I also have a podcast. It's called AI and I.

(01:33:41):
You can find it on YouTube and on Spotify. And how can people be useful? Honestly, I think that the most useful thing for someone like me, based on what I want to do, is I want people to find interesting, cool ways to use AI that actually helps make their lives better. So just go do that, and tell me about it, and I think that'll be great, and so-

Lenny Rachitsky (01:34:01):
What's the best way to tell you? Is it comments on your YouTube show? Is it emailing you, DM you?

Dan Shipper (01:34:05):
I would say tweet me.

Lenny Rachitsky (01:34:08):
Yeah.

Dan Shipper (01:34:09):
If you subscribe to Every, you can also reply to those emails, and they eventually get forwarded to me. So tweet me. Reply to Every. And if you want to comment on YouTube, great. I'm not in the YouTube comments as much as I should be, though.

Lenny Rachitsky (01:34:22):
Don't do that. Maybe don't do that.

Dan Shipper (01:34:23):
Yeah.

Lenny Rachitsky (01:34:25):
Okay. Well, Dan, this was incredible. Thank you so much for sharing. Thanks for being here.

Dan Shipper (01:34:29):
Thanks for having me.

Lenny Rachitsky (01:34:30):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

