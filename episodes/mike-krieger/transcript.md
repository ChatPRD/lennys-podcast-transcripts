---
guest: Mike Krieger
title: Anthropic's CPO on what comes next | Mike Krieger (co-founder of Instagram)
youtube_url: https://www.youtube.com/watch?v=DKrBGOFs0GY
video_id: DKrBGOFs0GY
description: 'Mike Krieger is the chief product officer of Anthropic and the co-founder
  of Instagram. After leaving Meta, he co-founded Artifact, an AI-powered news app
  that I absolutely loved, and joined...

  '
duration_seconds: 3982.0
duration: '1:06:22'
view_count: 102785
channel: Lenny's Podcast
keywords:
- growth
- retention
- metrics
- okrs
- roadmap
- a/b testing
- funnel
- subscription
- revenue
- management
- strategy
- mission
- positioning
- differentiation
- competition
---

# Anthropic's CPO on what comes next | Mike Krieger (co-founder of Instagram)

## Transcript

Lenny Rachitsky (00:00:00):
90% of your code roughly is written by AI now.

Mike Krieger (00:00:03):
The team that works in the most futuristic way is the Claude Code team. They're using Claude Code to build Claude Code in a very self-improving kind of way. We really rapidly became bottlenecked on other things like our merge queue. We had to completely re-architect it because so much more code was being written and so many more pull requests were being submitted. Over half of our pull requests are Claude Code generated. Probably at this point it's probably over 70% that it just completely blew out the expectations of it.

Lenny Rachitsky (00:00:26):
You guys are at the edge of where things are heading.

Mike Krieger (00:00:28):
I had the very bizarre experience of I had two tabs open. It was AI 2027, and my product strategy, and it was this moment where I'm like, "Wait, am I the character in the story?"

Lenny Rachitsky (00:00:36):
It feels like ChatGPT is just winning in consumer mind share. How does that inform the way you think about product, strategy, and mission?

Mike Krieger (00:00:43):
I think there's room for several generationally important companies to be built in AI right now. How do we figure out what we want to be when we grow up versus what we currently aren't or wish that we were or see other players in the space being?

Lenny Rachitsky (00:00:55):
What's something that you've changed your mind about what AI is capable of and where AI is heading?

Mike Krieger (00:01:01):
I had this notion coming in like, "Yes, these models are great, but are they able to have an independent opinion?" And it's actually really flipped for me only in the last month.

Lenny Rachitsky (00:01:12):
Today, my guest is Mike Krieger. Mike is chief product officer at Anthropic, the company behind Claude. He's also the co-founder of Instagram. He's one of my most favorite product builders and thinkers. He's also now leading product at one of the most important companies in the world, and I'm so thrilled to have had a chance to chat with him on the podcast. We chat about what he's changed his mind about most in terms of AI capabilities in the years since he joined Anthropic, how product development changes and where bottlenecks emerge when 90% of your code is written by AI, which is now true at Anthropic. Also, his thoughts on OpenAI versus Anthropic, the future of MCP, why he shut down Artifact, his last startup and how he feels about it. Also, what skills he's encouraging his kids to develop with the rise of AI. And we closed the podcast on a very heartwarming message that Claude wanted me to share it with Mike.

(00:02:00):
A big thank you to my newsletter Slack community for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe it and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including Linear, Superhuman, Notion, Perplexity and Granola. Check it out at lennysnewsletter.com and click bundle.

(00:02:22):
With that, I bring you Mike Krieger. This episode is brought to you by Productboard, the leading product management platform for the enterprise. For over 10 years, Productboard has helped customer-centric organizations like Zoom, Salesforce, and Autodesk build the right products faster. And as an end-end platform, Productboard seamlessly supports all stages of the product development lifecycle. From gathering customer insights to planning a roadmap, to aligning stakeholders, to earning customer buy-in, all with a single source of truth.

(00:02:52):
And now product leaders can get even more visibility into customer needs. With Productboard Pulse, a new voice of customer solution built-in intelligence helps you analyze trends across all of your feedback and then dive deeper by asking AI your follow-up questions. See how Productboard can help your team deliver higher impact products that solve real customer needs and advance your business goals. For a special offer and free 15-day trial, visit productboard.com/lenny. That's productboard.com/L-E-N-N-Y.

(00:03:26):
Last year, 1.3% of the global GDP flowed through Stripe. That's over $1.4 trillion and driving that huge number are the millions of businesses growing more rapidly with Stripe. For industry leaders like Forbes, Atlassian, OpenAI, and Toyota, Stripe isn't just financial software. It's a powerful partner that simplifies how they move money, making it as seamless and borderless as the internet itself. For example, Hertz boosted its online payment authorization rates by 4% after migrating to Stripe. And imagine seeing a 23% lift in revenue like Forbes did just six months after switching to Stripe for subscription management. Stripe has been leveraging AI for the last decade to make its product better at growing revenue for all businesses. From smarter checkouts to fraud prevention and beyond. Join the ranks of over half of the Fortune 100 companies that trust Stripe to drive change, learn more at Stripe.com.

(00:04:29):
Mike, thank you so much for being here and welcome to the podcast.

Mike Krieger (00:04:32):
I'm really happy to be here. I've been looking forward to this for a while.

Lenny Rachitsky (00:04:35):
Wow, I had love to hear that. I've also been looking forward to this for a while. I have so much to talk about. So first of all, you've been at Anthropic for just over a year at this point. Congrats by the way on hitting the cliff.

Mike Krieger (00:04:46):
Thank you. Not that we're tracking.

Lenny Rachitsky (00:04:49):
That's right. So let me just ask you this. So you've been at Anthropic for about a year. What's something that you've changed your mind about from before you joined Anthropic to today about what AI is capable of and where AI is heading?

Mike Krieger (00:05:04):
Two things. One is like a pace and timeline question. The other one is a capability question. So maybe I'll take the second one first. I had this notion coming in, yes, these models are great, they're going to be able to produce code, they're going to be able to write hopefully in your voice eventually, but are they able to sort of have an independent opinion? And it's actually really flipped for me only in the last month and only with Opus 4 where my go-to product strategy partner is Claude. And it has been basically for that full year where I'll write an initial strategy, I'll share it with Claude basically, and I'll have it, look at it. And in the past it's pretty anodyne kind of comments that it would leave, "Oh, have you thought about this?" And it's like, "Yeah, I thought about that." And Opus 4, I was working on some strategy for our second half of the year was the first one.

(00:05:51):
It was like Opus 4 combined with our advanced research. But it really went out for a while and it came back and I was like, you really looked at it in a new way. And so that's a thing that I've maybe I didn't feel like it would never be able to do that, but I wasn't sure how soon it'd be able to come up with something where I look at it, I'm like, yep, that is a new angle that I hadn't been looking at before and I'm going to incorporate that immediately into how I think about it. So that's probably the biggest shift that I've had is, I don't know about independence is the right word, but creativity and sort of novelty of thought relative to how I'm thinking about things. But in the timeline, one, it's so interesting because I was sitting next to Dario yesterday and he's like, "I keep making these predictions and people keep laughing at me. And then they come true."

(00:06:31):
And it's funny to have this happen over and over again and he is like, not all of them are going to be right. But even I think as of last year he was talking about we're at 50% on SWE-Bench, which is this benchmark around how well the models are at coding. He's like, "I think we'll be at 90% by the end of 2025 or something like that." And sure enough, we're at about 72 now with the new models and we're at 50% when he made that prediction. And it's continued to scale pretty much as predicted. And so I've taken the timelines a lot more seriously now. And I don't know if you read AI 2027-

Lenny Rachitsky (00:07:05):
I have, it made by heart race.

Mike Krieger (00:07:09):
And I had the very bizarre experience of I had two tabs open, it was AI 2027 and my product strategy. And it was this moment where I'm like, "Wait, am I the character in the story? How much is this converging?" But you read that and you're like, "Oh, 2027, that's years away if you're like no, mid 2025." And things continue to improve and the models continue to be able to do more and more and they're able to act agentically and they're able to have memory and they're able to act over time. So I think my confidence in the timelines and I don't know exactly how they manifest it definitely just solidified over the last year.

Lenny Rachitsky (00:07:43):
Wow. I wasn't expecting to go down that that paper was scary. And I'm curious just I guess I can't help but ask just thoughts on just how do we avoid the scary scenario that paper paints of where AI getting really smart goes?

Mike Krieger (00:07:59):
Yeah, this maybe ties into, I've been here a year, why did I join Anthropic? I was watching the models get better and even you could see it in early 2024, and looking at my kids, I'm like, "All right, they're going to grow up in a world with AI. It's unavoidable." Where can I maximally apply my time to nudge things towards going well? And I mean that's a lot of what people think about across the industry, especially at Anthropic. And so I think coming to an agreement and a shared framework and understanding of what does going well look like? What is the kind of human AI relationship that we want?

(00:08:36):
How will we know along the way? What do we need to build and develop and research along the way? I think those are all the kind of key questions. And some of those are product questions and some of those are research and interpretability questions, but for me it was the strongest reason to join was okay. I think there's a lot of contribution that Anthropic can have around nudging things to go better. And if I can have a part to play there, let's do it.

Lenny Rachitsky (00:09:00):
I love that answer. Speaking of kids, so you've got two kids, I've got a young kid, he's just about to turn two. I'm curious just what skills you're encouraging your kids to build as this AI becomes more and more of our future and some jobs will be changed and just what advice do you have?

Mike Krieger (00:09:18):
We have this breakfast feed breakfast with the kids every morning and sometimes some question will come up, something about physics and our oldest kid's almost six, but they ask funny questions about the solar system or physics or in a 6-year-old way and before we reach for Claude, because at first my instinct is like, "Oh, I wonder how Claude will do this question." And we started changing, "Well, how would we find out?" And the answer can't just be we'll ask Claude, all right, well, we could do this experiment, we could have this thing. So I think nurturing curiosity and still having a sense of, I don't know, the scientific process sounds grandiose to instill in a 6-year-old, but that process of discovery and asking questions and then systematically working right through, I think will still be important. And of course AI will be an incredible tool for helping resolve large parts of that, but that process of inquiry I think is still really important and independent thought.

(00:10:11):
My favorite moment with my kid, because she's very headstrong, our 6-year-old, she said something and I wasn't sure if it was true. It was, oh, is that coral is an animal or corals alive? I don't even remember what the details of it. And I was like, "I don't know if that's true." And she's like, "It's definitely true, dad." I'm like, "All right, let's ask Claude on this one." And she's like, "You can ask Claude, but I know I'm right." And I'm like I love that. I want that kind of level of not just delegating all of your cognition to the AI because it won't always get it right. And also it kind of short circuits any kind of independent thought. So the skill of asking questions, inquiry and independent thinking, I think those are all the pieces. What that looks like from a job or occupation perspective, I'm just keeping an open mind and I'm sure that'll radically change between now and then.

Lenny Rachitsky (00:11:02):
It's interesting. Tobias Lütke, Shopify CEO, on the podcast and he had the same answer for what he's encouraging his kids to develop is curiosity. And so it's interesting that's a common thread.

Mike Krieger (00:11:14):
The K through eight school our kid goes through had an AI and education expert come in and I had a very low bar or a very low expectation of what this conversation was going to be like. And actually I think it went over most of the people in the audience's heads because he was like, "All right, well let me take you all the way back to Claude Shannon in information theory." And I could see people's eyes going, "What did I sign up for and why am I hearing this school auditorium hearing about information theory?" But he did a really nice job I think of also just imagining there will be different jobs and we don't know what those jobs are going to be and so what are the skills and techniques and remain open mindedness around what the exact way we recombine those things. And even those will probably change three times between now and when they're 18.

Lenny Rachitsky (00:11:59):
So we're talking about timelines and how things are changing. So I've seen these stats that you've shared, other folks at Anthropic have shared about how much of your code is now written by AI. So people have shared stats from 70% to 90%. There was an engineer lead that shared 90% of your code roughly is written by AI now, which first of all is just insane that it went from zero to 90%, I don't know, a few years, something like that. Yeah, basically. I don't think people are talking about this enough. That's just wild. You guys are basically at the bleeding edge. I've never heard a company that has this high a percentage of code being written by AI.

(00:12:34):
So you guys are at the edge of where things are heading. I think most companies will get here. How has product development changed knowing so much of your code is now written by AI, so usually it's like PM, it's like here's what we're building, engineer builds it, it ships it. Is it still kind of roughly that or is it now PMs are just going straight to Claude, build this thing for me, engineers are doing different things? Just what looks different in a world where 90% of your code is written by AI?

Mike Krieger (00:12:57):
Yeah, it's really interesting because I think the role of engineering has changed a lot, but the suite of people that come together to produce a product hasn't yet. And I think for the worst in a lot of ways because I think we're still holding on some assumptions. So I think the roles are still fairly similar, although we'll now get in my favorite things that happen now are some nice PMs that have an idea that they want to express or designers that have an idea they want to express will use Claude and maybe even Artifacts to put together an actual functional demo. And that has been very, very helpful. No, no, this is what I mean that makes it tangible. That's probably the biggest role shift is prototyping happening earlier in the process via more of this code plus design piece. What I've learned though is the process of knowing what to ask the AI, how to compose the question, how to even think about structuring a change between the backend and the front end.

(00:13:54):
Those are still very difficult and specialized skills and they still require the engineer to think about it. And we really rapidly became bottlenecked on other things like our merge queue, which is the get in line to get your change accepted by the system that then deploys into production. We had to completely re-architect it because so much more code was being written and so many more pull requests were being submitted that it just completely blew out the expectations of it. And so it's like, I don't know if you've ever read, is it the goal, the classic process optimization book, and you realize there's this critical path theory. I've just found all these new bottlenecks in our system, there's an upstream bottleneck, which is decision making and alignment. A lot of things that I'm thinking about right now is how do I provide the minimum viable strategy to let people feel empowered to go run and type and build and explore at the edge of model capabilities.

(00:14:44):
I don't think I've gotten that right yet, but that's something I'm working on. And then once the building is happening, other bottlenecks emerge, let's make sure we don't step on each other's toes. Let's think through all the edge cases here ahead of time so that we're not blocked on the engineering side. And then when the work is complete and we're getting ready to ship it, what are all those bottlenecks as well? Let's do the air traffic control of landing the change. How do we figure out large strategy? So I think there hasn't been as much pressure on changing those until this year, but I would expect that a year from now the way that we are conceiving of building and shipping software just changes a lot because it's going to be very painful to do it the current way.

Lenny Rachitsky (00:15:20):
Wow, that is extremely interesting. So it used to be here's an idea, let's go design it, build it, ship it, merge it, and then ship it. And usually the bottleneck was engineering, taking time to build a thing and then design. And now you're saying the two bottlenecks you're finding are okay deciding what to build and aligning everyone and then it's actually the cue to merge it into production. And I imagine review it too is probably a part-

Mike Krieger (00:15:47):
Reviewing has really changed too. And in many ways perhaps unsurprisingly the team that works in the most futuristic way is the Claude Code team because they're using Claude Code to build Claude Code in a very self-improving kind of way. And early on in that project, they would do very line by line pull request reviews in the way that you would for any other project. And they've just realized Claude is generally right and it's producing pull requests that are probably larger than most people are going to be able to review. So can you use a different Claude to review it and then do the human almost acceptance testing more than trying to review line by line. There's definitely pros and cons and so far it's gone well. But I could also imagine it going off the rails and then having a completely both unmaintainable or even understandable by Claude Code base that hasn't happened, but watching them change their review processes definitely has been interesting.

(00:16:38):
And yeah, the merge queue is one instance of the bottom bottleneck that forms down there, but there's other ones which is how do we make sure that we're still building something coherent and packaging it up into a moment that we can share with people and whether that's around a launch moment, whether that's about then enabling people to use this thing and talking about it, the classic things of building something useful for people and then making it known that you've built it and then learning from their feedback still exists. We've just made a portion of that whole process much more efficient.

Lenny Rachitsky (00:17:06):
I heard you describe this as you guys are patient zero for this way of working.

Mike Krieger (00:17:11):
Yes.

Lenny Rachitsky (00:17:12):
I love that. Do you have a sense of what percentage of Claude Code is written by Claude Code?

Mike Krieger (00:17:17):
At this point, I would be shocked if it wasn't 95% plus. I'd have to ask Boris and the other tech leads on there. But what's been cool is so nitty-gritty stuff, Claude Code is written in TypeScript. It's actually our largest TypeScript project. Most of the rest of Anthropic is written in Python, some Go, some Rust now, but we're not like a TypeScript shop. And so I saw a great comment yesterday in our Slack where somebody had this thing that was driving them crazy about Claude Code and they're like, "Well, I don't know any TypeScript, I'm just going to talk to Claude about it and do it."

(00:17:49):
And they went from that to pull requests in an hour and solve their problem and they submitted a pull request and that breaking down the barriers. One, it changes your barrier to entry for any kind of newcomer to the project. I think it can let you choose the right language for the right job for example. I think that helps as well, but I think it also just reinforces Claude Code being that patient alpha of that where contributions from outside the team can be Claude coded as well.

Lenny Rachitsky (00:18:18):
Wow, this is, it's just continue to blow my mind all these things that you're sharing, 95% of Claude Code is written by Claude Code roughly.

Mike Krieger (00:18:27):
That's my guess. Yeah, I'll come back with the real stuff. But I mean if you ask the team, that's how they're working and that's how they're getting contributions from across the company too.

Lenny Rachitsky (00:18:35):
It's interesting going back to your point about strategy being assisted by Claude itself and your point about how a lot of the bottlenecks now are kind of the top of the funnel of coming up with ideas aligning everyone, it's interesting that Claude is already helping with that also of helping you decide what to build. So if those two bottlenecks are aligning, deciding what to build and then just merging and getting everything, where do you see the most interesting stuff happening to help you speed those things up?

Mike Krieger (00:19:02):
Yeah, I think that on that first row, I started the year by writing a doc that was effectively how do we do product today and where is Claude not showing up yet that it should? And I think that upstream part is the next one to go. It's interesting. At your conference I talked to somebody who's working on a PRD, GPT kind of ChatPRD, I think was the-

Lenny Rachitsky (00:19:24):
ChatPRD, [inaudible 00:19:24].

Mike Krieger (00:19:24):
Yeah. Can Claude be a partner in figuring out what to build? What the market size is if you want to approach it that way? What the user needs are if you look at a different way? We think a lot about the virtual collaborator on topic and one of the ways in which I think that can show up is, "Hey, I'm in the Discord, the Claude Anthropic Discord, I'm in the user Fora, I'm on X and I'm reading things and here's what's emergent." That's step one. Models can do that today. Step two, which the models probably can do today, which have to wire them up to do it is and not only are the problems here's how I think you might be able to solve them. And then taking that through to, and I put together a pull request to solve this thing that I'm seeing feels very achievable this year than stringing those things together and we're limited more.

(00:20:13):
This is why MCP is exciting to me. We're limited more around making sure the context flows through all of that so we have the right access to those things more than the model's capability to reason and propose. Now the model might not have perfect UI taste yet, so there's definitely room for design to intervene and be like, "Oh, that's not quite how I would solve the problem of this not showing up." But I would get very excited. I would give you a really small example, but we changed on Claude AI, you should be able to just copy markdown from Artifacts or code from Artifacts and we changed it so you can actually download it and export it. We changed the button to export and we got a bunch of feedback like, "How do I copy now?" And the answer is you drop it down and it's copied.

(00:20:51):
It's just mind one of those things where it's made sense, but we probably got it not quite right. That feedback was in the RUX channel. I would've loved an hour later for a plot to be like, "Hey, if we do want to change it back, here's the PR to do it." And by the way, eventually, and then I'm going to spin up an A/B test to see if this changes metrics and then we'll see how it looks in a week. If you told me that about a year and a half ago going to be like, "Ah, yeah, maybe like 27, maybe 26." But it really feels just at the tip of capabilities right now.

Lenny Rachitsky (00:21:20):
Wow, okay. You mentioned the Lenny and Friends Summit. I wanted to talk about this a bit. So you were on a panel with Kevin Weil, the CPO of OpenAI, I think it was the first time you guys did this maybe the last time for now.

Mike Krieger (00:21:32):
Yeah, we haven't done it since, not for any reason. I had a lot of fun.

Lenny Rachitsky (00:21:34):
What a legendary panel we assembled there with Sarah Guo moderating. And you made this comment actually ended up being the most rewatched part of the interview, which is that you were putting product people on the model team and working with researchers making the model better and you're putting some product people on the product experience making the UX more intuitive, making all that better. And you found that almost all the leverage came from the product team working with the researchers. And so you've been doing more of that. So first of all, does that continue to be true? And second of all, what are the implications of that for product teams?

Mike Krieger (00:22:11):
It's continued to be true. And in fact I think that if the proportion was already skewing towards having more of that embedding, I've just become more and more convinced. I didn't feel as strongly about it during the summit and now I feel really strongly about it. If we're shipping things that could have been built by anybody just using our models off the shelf, there's great stuff to be built by using our models off the shelf by the way, don't get me wrong, but where we should play and what we can do uniquely should be stuff that's really at that magic intersection between the two, right?

(00:22:42):
Artifacts may a great example and if you play with Artifacts with Claude 4, that's an actually really interesting example where we took somebody from our, we have Claude code skills, which is a team that really is doing the post-training around teaching Claude some of these really specific skills and we paired it with some product people and then together we revamped how this looks in the product today and what Claude can do way better than just like, "Yeah, we just used the model and we prompted a little bit."

(00:23:07):
That's just not enough. We need to be in that fine-tuning process. So much of what, if you look at what we're working on right now, but we've shipped recently between research and all these other things are things that the functional unit of work at Anthropic is no longer take the model and then go work with design and product to go ship a product. It's more like we are in the post-training conversations around how these things should work and then we are in the building process and we're feeding those things back and looping them back.

(00:23:36):
I think it's exciting. It's also a new way of working that not all PMs have, but the PMs that have the most internal positive feedback from both research and engineering are the ones that get it that I was in a product review yesterday, I was like, "Oh, if we want to do this memory feature, we should talk to the researchers because we just shipped a bunch of memory capabilities in Claude 4." They're like, "Yeah, yeah, we've been talking to them for weeks, this is how we're manifesting it." It's like, "Okay, I feel good. I feel like we're doing the right things now."

Lenny Rachitsky (00:24:03):
So let me pull on this thread more and there's something I've been thinking about along these lines. So essentially there's a big part of entropic that's building this super intelligent giga brain that's going to do all these things for us over time. And then, as you said, there's the product team that's building the UX around this super intelligent giga brain and over time this super intelligence is going to be able to build its own stuff. And so I guess just where do you think the most value will come from traditional product teams over time? I know this is different because you guys are a foundational alum company and not most companies don't work this way, but just, I don't know, thoughts on just the where most value will come from product teams over time working on AI.

Mike Krieger (00:24:42):
I think there's still a lot of value in two things. One is making this all comprehensible. I think we've done an okay job. I think we could do a much better job of making this conference. What's still the difference between somebody who's really adept at using these tools in their work and most people is huge. And maybe that's the most literal answer to your earlier question around what skills to learn. That is a skill to learn and use it in the same way that I remember we did computer lock class when I was in middle school. I remember being really good at Google and that was actually a skill back in the day to think in terms of this information is out there, how do I query for it? How do I do it? I think it actually was an advantage at the time.

(00:25:21):
Of course now Google is pretty good at figuring out what you're trying to do if you are only in the neighborhood and there's less of that research kind of need. But I still think that's a necessary part of good product development, which is the capabilities are there and even if Claude can create products from scratch, what are you building and how do you make it Comprehensible? Still hard because I think that gets at this much deeper empathy and understanding of human needs and psychology. I was a human community interaction major, I still been talking in my book here. I still feel like that is a very, very, very, very necessary skill. So that's one. Two is, and this straight to call back to another one of your guests, strategy, how we win, where we'll play, figuring out where exactly you're going to want to, of all the things that you could be spending your time or your tokens or your computation on what you want to actually go and do.

(00:26:15):
You could be wider probably than you could before, but you can't do everything. And even from an external perspective, if you're seen to be doing everything, it's way less clear around how you're positioning yourselves. Like strategy I think is still the second piece. And then the third one is opening people's eyes to what's possible, which is a continuation of making it understandable. But we were in a demo with a financial services company recently and we were working on here's how you can use our analysis tool and MCP together and you could see their light up and you're like, "Ah, okay." We call it overhang. The delta between what the models and the products can do and how they're being used on a daily basis. Huge overhang. So that's where still a very, very strong necessary role for product.

Lenny Rachitsky (00:26:59):
Okay, that's an awesome answer. So essentially areas for product teams to lean into more is strategy, just getting better and better at strategy, figuring out what to build and how to win in the market, making it easier to help people understand how to leverage the power of these tools, the comprehensibility and kind of along those lines is opening people's eyes to the potential of these sorts of things. That's where product can still help.

Mike Krieger (00:27:21):
Exactly.

Lenny Rachitsky (00:27:22):
Awesome. So along those lines actually, do you have any just prompting tricks for people, things that you've learned to get more out of Claude when you chat with it?

Mike Krieger (00:27:30):
Sometimes it's funny because in some ways we have the ultimate prompting job, which is to write the system prompt for Claudia AI and we publish all of these, which I think is another nice area of transparency. And we are always careful when giving prompting advice because at least officially, but I'll give you the unofficial version because you don't want things to become like we think this works, but we're not sure why. But I will do small things like in Claude Code and we actually do react to this very literally, but I always ask it to, if I wanted to use more reasoning, think hard and it'll use a different flow and I usually start with that. Nudging, there's a great essay around make the other mistake like if you tend to be too nice, can you focus on... Even if you're trying to be more critical or more blunt, you're probably not going to be the most critical blunt person in the world.

(00:28:18):
And so with Claude sometimes I'm like, "Be brutal, Claude, roast me. Tell me what's wrong with this strategy." I know we were talking earlier about the Claude as thought partner around critiquing product strategy. I think I previously would say things like, "What could be better on this product strategy?" And I'm just like, "Just roast this product strategy," and Claude's like a pretty nice entity. It's hard to push it to be super brutal, but it forces it to be a little bit more critical as well. The last thing I'll say is, so we have a team called Applied AI that does a lot of work with our customers around optimizing Claude for their use case. And we basically took their insights and their way of working and we put it into a product itself. So if you go to our console, our work bench, we have this thing called the prompt improver where you describe the problem and you give it examples and Claude itself will agentically create and then iterate on a prompt for you.

(00:29:09):
I find what comes out of that ends up being quite different than what my intuitions would've been for a good prompt. And so I'd encourage folks to also check that out even for their own use cases because while that tool is met for an API developer putting a prompt into their product, it's equally applicable for a person doing a prompt for themselves. It'll insert XML tags which no human is going to think to do ahead of time. It actually is very helpful for Claude to understand what it should be thinking versus what it should be saying, et cetera. So that's another one is watch our prompt improver and then note that Claude itself is a very good prompter of Claude.

Lenny Rachitsky (00:29:41):
Awesome. Okay, so we're going to link to that, the prompt improver. The core piece of advice you shared early is just do the opposite of what you would naturally do. So if you're trying to be nice, just be brutal, be very honest and frank with me.

Mike Krieger (00:29:53):
Exactly. I find that works quite well. What are the thought patterns that I've fallen into that you want to break me out of?

Lenny Rachitsky (00:29:59):
I saw you guys just today maybe launched a Rick Rubin collab where it said vibe coding. What's that all about?

Mike Krieger (00:30:06):
What I've heard about that. And again, a lot of the coalesce this week between model launch developer event and The Way of Code. We had one of our co-founders, Jack Clark is our head of policy and he got connected to Rick Rubin because I think he's been thinking a lot about coding, the future of coding and creativity and they've stayed in touch. And Rick got excited about this idea of he was creating art and visualizations with Claude and then he had these ideas around the way of the vibe coder and they put together this, actually I mean I love almost everything Rick Rubin. So the aesthetic of it I think is just so on point too. But yeah, this sort of like med meditation is probably the right word. Meditation on creativity, working alongside AI coupled with this really rich, interesting visualizations. But it's one of those things where internally they're like, "Oh yeah, and we're doing this Rick Rubin collab." We were like, "We're doing what? That's amazing."

Lenny Rachitsky (00:31:03):
I looked at it briefly and there's that meme of him just thinking deeply, sitting on a computer with a mouth.

Mike Krieger (00:31:09):
Yes.

Lenny Rachitsky (00:31:10):
And ASCII art, I think.

Mike Krieger (00:31:11):
It's totally, it's like ASCII art vibe.

Lenny Rachitsky (00:31:14):
I'm excited to have Andrew Luo joining us today. Andrew is CEO of OneSchema, one of our long time podcast sponsors. Welcome, Andrew.

Speaker 3 (00:31:21):
Thanks for having me, Lenny. Great to be here.

Lenny Rachitsky (00:31:23):
So what is new with one schema? I know that you work with some of my favorite companies like Ramp and Vanta and Watershed. I heard you guys launch a new data intake product that automates the hours of manual work that teams spent importing and mapping and integrating CSV and Excel files.

Speaker 3 (00:31:39):
Yes, so we just launched the 2.0 of OneSchema FileFeeds. We've rebuilt it from the ground up with AI. We saw so many customers coming to us with teams of data engineers that struggled with the manual work required to clean messy spreadsheets. FileFeeds 2.0 allows non-technical teams to automate the process of transforming CSV and Excel files with just a simple prompt. We support all of the trickiest file integrations, SFTP, S3, and even email.

Lenny Rachitsky (00:32:05):
I can tell you that if my team had to build integrations like this, how nice would it be to take this off our roadmap and instead use something like OneSchema?

Speaker 3 (00:32:13):
Absolutely, Lenny. We've heard so many horror stories of outages from even just a single bad record in transactions, employee files, purchase orders, you name it. Debugging these issues is often like finding a needle in a haystack. OneSchema stops any bad data from entering your system and automatically validates your files, generating error reports with the exact issues in all bad files.

Lenny Rachitsky (00:32:34):
I know that importing incorrect data can cause all kinds of pain for your customers and quickly lose their trust. Andrew, thank you so much for joining me. If you want to learn more, head on over to oneschema.co. That's oneschema.co.

(00:32:48):
Actually going back to the beginning of your journey at Anthropic, what's the story of you getting recruited at Anthropic? Is there anything fun there?

Mike Krieger (00:32:55):
It all started and I actually sent my friend this text. So Joel Lewenstein, who I've known, he and I built our first iPhone apps together in 2007 when the App Store was just out and you could still make money by selling dollar apps on the App Store back in the day. And we were both at Stanford together and we were friends and we've stayed in touch over years and we've never gotten to work together since then. We've just remained close. And I was coming out of the Artifact experience, I was trying to figure out, do I start another company? I don't think so. I need a break from starting something from zero. Do I go work somewhere? I don't know what company would I want to go work at. And he reached out and he's like, "Look, I don't know if you at all considered joining something rather than starting something, but we're looking for a CPO. Would you be interested in chatting?"

(00:33:37):
And at that time, Claude 3 had just come out and I was like, "Okay, this company's clearly got a good research team. The product is so early still." And it was like, "Great, I'll take the meeting." And I first met with Daniela, was one of the co-founders and the president in Anthropic. And just from the beginning I was like a breath of fresh air, very little grandiosity coming off the founders, I mean they're clear-eyed about what they're building. They know what they don't know. How many times I talk to Dario always like Dario is like, "Look, I don't know anything about product, but here's an intuition." Usually the intuition is really good and leads to some good conversation, but I think that intellectual honesty and shared view of what it means to do AI in a responsible way, it just resonated.

(00:34:22):
I kept having this feeling in these interviews, this is the AI company I would've hoped to have found it if I had founded an AI company. And that's kind of the bar around if I'm going to join something that should be where I'm going to go. But what I realized, I actually hadn't joined a company since my first internship in college basically. And I was like, "Oh, how do I onboard myself? How do I get myself up to speed? How do I balance making sweeping changes versus understanding what's not broken about it overall?" And looking back on a year, I think I made some changes too slowly. I think there was ways reorganizing product that I could have made a change earlier. And I think I didn't appreciate how much a couple of really key senior people can shape so much of product strategy.

(00:35:10):
I'll harken back to Claude Code. Claude Code happened because Boris, who actually was a Boris Cherney, he was an Instagram engineer and one of our senior ICs there, we overlapped a bit, was started that project from scratch internal first and then we got it out and then shipped it. And that's the power of one or two really strong people. And I made this mistake, we need more headcount and we do, I think there's more work that we need to do and there's things that I want to be building. But more than that we need a couple of almost founder type engineers that maybe connect back to our question on what skills are useful and how does product development change. And maybe even more so I'm a huge believer in the founding engineer tech lead with an idea and pair them with the right design and product supports, help them realize that, I'm 10 times more a believer in that than before.

Lenny Rachitsky (00:36:01):
I actually asked people on Twitter what to ask you ahead of this conversation. And the most common question surprisingly was why did you shut down Artifact? And I also wondered that because I loved Artifact. I was a power user. I was just like, "Finally a news app that I love that it's giving me what I want to know." So I guess just what happened there at the end?

Mike Krieger (00:36:20):
I still really miss it too. I didn't find a replacement and I think I substituted it by visiting individual sites and keeping things up that way. And it's not really the same, especially on the log to I think we got right with Artifact and if people didn't play with it before, it was we really tried to not just recommend top stories, they were part of it. But really if you were interested in Japanese architecture, you could pretty reliably get really interesting stories about Japanese architecture every day. Whether that's from a Dwell or from Architectural Digest or from a really specific blog that we found that somebody recommended to us. It captured some of that Google reader joy of content discovery of the deeper web. Our headwinds were a couple. One of them was just mobile websites have really taken a turn. I don't blame any individuals for this.

(00:37:10):
I think it's the market dynamics of it, but we put so much time or designers, sky Gunner Gray who's phenomenal that for Perplexity now, the app experience I was so proud of, but when you click through it was like the pressures on these mobile sites and these mobile publishers would be like, "Sign up for our newsletter. Here's a full screen video ad." It was very jarring and we didn't feel like it ethically made sense for us to do a bunch of ad blocking because then you're like, "Sure, you can deliver a nice experience for people, but that doesn't feel like it's playing fair with the publishers." But at the same time, the actual experience wasn't good. So the mobile web deteriorating, which makes me very sad, but I think was part of it. Two was Instagram spread in the early days because people would take photos and then post them on other networks and tell friends about it.

(00:37:57):
And there was this really natural like, "How did you do that? I want to do it." News was very personal. I can't tell you how many people would be like, "I love Artifact." I'm like, "Did you tell anybody about it?" And they're like, "I told one person," and it didn't have that kind of spread. And any attempt that we had to do it felt kind of contrived, like, "Oh, we'll wrap all the links in artifact.news." But we didn't want interstitial things. In some ways, this sounds very puritanical, I don't mean it to sound this way, but there were lines that we didn't want to cross that just felt ethically not us, that I've seen other news players do more of. And maybe if we had done that, it would've grown more, but I don't think that's the company we wanted to have built other way. I don't think we were the founders to have built it.

(00:38:39):
And the third one, which is an underappreciated one, is we started at mid-COVID, which meant that we were fully distributed and I think there were major shifts that we would've wanted to make both in the strategy and the product and the team. And it's really hard to do that if you are all fully remote. Nothing replaces the Instagram days of we went through some hard times like Ben Horowitz called the we're F'ed, it's over kind of moments. This is definitely type two fun. I wouldn't say that my favorite memories because they weren't happy ones, but memories I really stayed with me with Instagram was like me and Kevin at Taqueria, Cancun on Market Street eating burritos at literally 11:00 PM being like, "How are we going to get out of this? How are we going to work through this?" And Zoom is not a good replica for that.

(00:39:26):
You tend to let things go or things build up over time. So the confluence of those three things, we entered I guess 2024 and said, "Look, there is a company to be built in the space. I'm not sure where the people would've built it. This concurrent incarnation we love, but it's not growing." The way I put it's like 10 units of input in for one unit of output versus the other way around. If we put blood and tears into the product and launch something we were proud of and metrics would barely move, the energy is not present in this product, in this system. And so are we going to expend another year or two and then go off and fundraise only to find that this is the case or do we call it and see that it's run its course and try to find a home for it, et cetera.

(00:40:06):
So that was the confluence on it and they started feeling this opportunity cost of AI is starting to change everything. We have an AI powered news app, but is this the maximal way in which we're going to be able to impact this? And it felt like the answer was increasingly no. But it was hard. I mean in the end I was really at peace of the decision, but it was a conversation that went on for a couple of months.

Lenny Rachitsky (00:40:26):
On that note, just how hard was it because because there's an ego component to it, like, "Oh, I'm starting my new company, it's going to be great," and then you end up having to shut it down. Just how hard is that as a very successful previous founder shutting something down and then not working out?

Mike Krieger (00:40:41):
Yeah, I mean I think when we started it, one of the conversations was like, "Look, what is the bar to success here? And do we want it to be something other than Instagram DAU?" Which is just an impossible bar. Only one company since, maybe two, you could say maybe ChatGPT and TikToK have reached that kind of mass consumer adoption starting a news app. Most people are not daily news readers even, right? And so we knew that we weren't pursuing that size of usage, at least with the first incarnation, but we did have an idea of building out complementary products over time that all use personalization and machine learning. We didn't even call it AI at the time. It was 2021 back-

Lenny Rachitsky (00:41:17):
Yeah, yeah, AI, it was called machine learning back then.

Mike Krieger (00:41:19):
Yeah, it was called machine learning still. And so in shutting it down, you know it when you see it in terms of user growth and traction. And I wasn't expecting Instagram growth, but I was expecting or hoping for or looking for something that felt like at its own legs under it and it could continue to compound. I was really positively surprised by how supportive people were when we announced it. There was a bit of like I told you so which sure anything launching you could be like, "This is not going to work." And you're right, most of the time most things don't work. There was actually very little of that. And most people, the universal reception, at least as I received it, was kudos for calling it when you saw it and not protracted doing this for a long time.

(00:42:05):
And I've talked to founders since then that have been like, "Yeah, I probably would've taken this thing on for another six months, but saw what you guys did, realized we were barking up the wrong tree, made the call." And I was like, "If that frees up people to go work on a more interesting things, I feel like that's a good legacy for Artifact to have." But for sure there was an ego bruise of is it true that you're only as good as your last game if I am a huge sports fan, right? So is that true or is there something more over a time? I'm very competitive, but primarily with myself and so I'm always trying to find the next thing that I want to go and do that's hard. And unfortunately that probably means that more often than not I'll feel dissatisfied, but the most recent thing that I did, but hopefully that yields good stuff in the end.

Lenny Rachitsky (00:42:50):
Yeah, I think just the trajectory you went on after shows that it's okay to shut down things that you were working on. Okay, so you mentioned ChatGPT. I wanted to chat about this a bit. So there's something really interesting happening. So on the one hand you guys are doing some of the most innovative work in AI. You guys launched MCP, which is just, I don't know, the fastest growing standard of any time in history that everyone's adopting Claude powered and unlocked centrally the fastest growing companies in the world, Cursor, Lovable, and Bolt, and all these guys. I had them on the podcast and they're all like, "When Claude, I think 3.5 came out, Sonnet, was just like that's made this work finally."

(00:43:28):
On the other hand, it feels like ChatGPT is just winning in consumer mind share. When people think AI, especially outside tech, it's just like ChatGPT in their mind. So let me just ask you this, I guess first of all, do you agree with that sentiment and then two, as a challenger brand in the AI space, just how does that inform the way you think about product strategy and mission and things like that?

Mike Krieger (00:43:50):
Yeah, I mean you look at the sort of public adoption or if you ask people, oh, if you Jimmy Kimmel man on the street kind of thing, name an AI company, I bet they would name and actually I'm not even sure they name open AI, they'd probably name ChatGPT because that brand is the lead brand there as well. And I think that's just the reality of it. I think that when I reflect on my year, I think maybe two things are true. One is consumer adoption is really lightning in a bottle and we saw it at Instagram. So almost maybe more than anybody, I can look internally and say, "Look, we'll keep building interesting products. One of them may hit." But to craft an entire product strategy around trying to find that hit is probably not wise, we could do it and maybe Claude can help come up with a fullness of things, but I think we'd miss out an opportunity in the meantime.

(00:44:41):
And then instead look yourself in the mirror and embrace who you are and what you could be rather than who others are is maybe the way I've been looking at it, which is we have a super strong developer brand, people build on top of us all the time, and I think we also have a builder brand. The people who I've seen react really well to Claude externally. Maybe the Rick Rubin connection has some resonance here as well. Can we lean into the fact that builders love using Claude? And those builders aren't all just engineers and they're not just all entrepreneurs starting their companies, but they're people that like to be at the forefront of AI and are creating things. Maybe they didn't think of those as engineers, but they're building... I got this really nice note from somebody internal on Anthropic who's on the legal team and he was building bespoke software for his family and connected to them in a new way.

(00:45:29):
And I was like, "This is a glimmer of something that we should lean into a lot more." And so I think what, and this is actually connecting back to us saying like Claude being helpful here. A lot of what I've been thinking about going into the second half of the year and beyond is how do we figure out what we want to be when we grow up versus what we currently aren't or wish that we were or see other players in the space being. I think there's room for several generationally important companies to be built in AI right now. That's almost a truism given the adoption and growth that we've seen at Anthropic, but also across OpenAI and also places like Google and Gemini. So let's figure out what we can be uniquely good at that place to the personality of the founder. All the things come together, the personality of the founders, the quality of the models, the things the models tend to excel at, which is agentic behavior and coding.

(00:46:20):
Great. There's a lot to be done there. How do we help people get work done? How do we let people delegate hours of work to Claude? And maybe there's fewer direct consumer applications on day one. I think they'll come, but I don't think that spending all of our time focused on that is the right approach either. And so I came in, everybody expected me to just go super, super hard on consumer and make that the thing and again, would make the other mistake. Instead, I spent a bunch of time talking to financial services companies and insurance companies and others who are building on top of the API. And then lately I've spent a lot more time with startups and seeing all the people that have grown off of that. And I think the next phase for me is let's go spend time with the builders, the makers, the hackers, the tinkerers, and make sure we're serving them really well. And I think good things will come from that and that feels like an important company as we do that.

Lenny Rachitsky (00:47:08):
So essentially it's differentiate and focus, lean into the things that are working, don't try to just beat somebody at their own game.

Mike Krieger (00:47:15):
Exactly.

Lenny Rachitsky (00:47:15):
Super interesting. So kind of along those lines, a question that a lot of AI founders have is just like, "Where's a safe space for me to play where the foundational model companies are going to come squash me?" So I asked Kevin Weil this and he had an answer and I noticed looking back at that conversation, he mentioned Windsurf a lot. He was like, "Wow, this kid really loves Windsurf." And then a week later they bought Windsurf. So it all makes sense now. So I guess the question just is, where do you think AI founders should play where they are least likely to get squashed by folks like OpenAI and Anthropic? And also, are you guys going to buy Cursor?

Mike Krieger (00:47:51):
I don't think we're going to buy Cursor. Cursor is very big, but we love working with them. A few thoughts on this, and it's a question I've gotten. We like to do these kind of founder days with whether it's Menlo Ventures who have about investors and [inaudible 00:48:10]. It's like we've done YC, we've done these founder days, and it's like the question that is on a lot of these founders minds, understandably so. I think things that are going to, I can't promise this as a five to 10 year thing, but at least one to three years, things that feel defensible or durable. One is understanding of a particular market. I spend a bunch of time with the Harvey folks and they showed me some of their UI. I was like, "What is this thing?" And they're like, "Oh, this is a really specific flow that lawyers do, "and you never would've come up with it from scratch and you could argue about whether it's the optimal way they get done things done, but it is the way that they get things done and here's how AI can help with that.

(00:48:45):
And so differentiated industry knowledge, biotech, I'm excited to go and partner with a bunch of companies that are doing good stuff around AI and biotech and we can supply the models and some applied AI to help make those models go well. And I've been dreaming about at what point does live equipment all get an MCP and that you can then drive using Claude. There's all these cool things to be done there. I don't think we're going to be the company to go build the intent solution for labs, but I want that company to exist and I want to partner with it. Domains like legal, again, healthcare, I think there's a lot of very specific compliance and things. These are things that necessarily sound sexy out the gate, but there are very large companies to go and be built there. So that's number one. Paired with that is differentiated go to market, which is the relationship that you have with those companies, right?

(00:49:35):
Do you know your customer at those companies? One of our product leads, Michael is always talking about don't just know the company you're selling to, but know the person you're selling to at the company. Are you selling to the engineering department? Because trying to pick which AILM to build on top of or API to build on top of. Let's go talk to them. Is it the CIOs? The CTOs? Is it the CFO? Is it general counsel? So under a company's deep understanding of who they're selling to is the other piece too. What's interesting there is it's probably hard to build that empathy in a three-month accelerator, but you maybe can start having that first conversation and build that out time or maybe you came from that world or you're co-founding somebody who came from that world. Then the last one is like there's tremendous power in distribution and reach to being ChatGPT and having hundreds of millions or billions of users.

(00:50:23):
There's also people have an assumption about how to use things and so I get excited about startups that will get started that have a completely different take on what the form factor is by which we interface with AI. And I haven't seen that many of them yet. I wanted to see more of them. I think more of them will get created with some things like our new models, but the reason that that's an interesting space to occupy is do something that feels very advanced user, very power user, very weird and out there at the beginning, but could become huge if the models make that easy. And it's hard for existing incumbents to adapt to because people already have an existing assumption about how to use their products or how to adapt to them. So those are my answers. I don't envy them. I would probably be asking those questions if I was starting a company in the AI space.

(00:51:10):
Maybe that's part of the reason why I wanted to join a company rather than start one. But I still think that there are, and maybe here's fourth, don't underestimate how much you can think and work like a startup and feel like it's you against the world. It's existential that you go solve that problem and that you go build it. It sounds a little cliche, but it's like it's all we had at Instagram. We were two guys and we were like, "Let's see what we can do in an Artifact." We were six people for most of that time and every day felt like it's existential that we get this right, we need to win. And you can't replicate that and you can't instill that with OKRs. You just have to feel it. And that is a way of working rather than a area of building, but it's a continued advantage if you can harness it.

Lenny Rachitsky (00:51:55):
I love that you still have such a deep product founder sense there as you're building products for this very large company now. On the flip side of this, people working with your models and API, so I imagine there's some companies that are finding ways to leverage your models and APIs to their max and are really good at maximizing the power of what you guys have built. And there's some companies that work with your APIs and models that haven't figured that out. What are those companies that are doing a really good job building on your stuff, doing differently that you think other companies should be thinking about?

Mike Krieger (00:52:29):
I think being willing to build more at the edge of the capabilities and basically break the model and then be surprised by the next model. I love that you cited the companies were like 3.5 was the one that finally made them possible. Those companies were trying it beforehand and then hitting a wall and being like, oh, the models are almost good enough or they're okay for this specific use case, but they're not generally usable and nobody's going to adopt them universally, but maybe these real power users are going to try it out. Those are the companies that I think continuously are the ones where I'm like, "Yep, they get it. They're really pushing forward." We ran a much broader early access program with these models than we had in the past, and part of that was because there's this real, we can hill climb on these evaluations and talk about suite bench and towel bench and terminal bench, whatever, but customers ultimately know Cursor bench which doesn't exist other than in their usage and their own testing et cetera is the thing that we ultimately need to serve.

(00:53:29):
Not just Cursor but Manus bench, right? If Manus is using our models and Harvey bench, those things and customers know way better than anybody. And so I would say there's two things. One is pushing the frontier of the models and then having a repeatable process. This actually goes back to our summit conversation repeatable way to evaluate how well your product is serving those use cases and how well if you drop a new model in, is it doing it better or worse? Some of it can be classic A/B testing, that's fine. Some of it may be internal evaluation, some of it may be capturing traces and being able to rerun them on with a new model. Some of it's vibes like we're still pretty early in this process and some of it is actually trying it and being one of my favorite early access quotes was the founder heard this engineer screaming next to him.

(00:54:14):
He was like, "What? This model? I've never seen this before." This is like Opus 4. It was like, "Cool." We're going to engender that feeling and things, but you're not going to be able to feel that unless you have a really hard problem that you're asking the model repeatedly. So those are the things that I think kind of differentiate those companies that are maybe earlier in their journey of adoption versus the later ones.

Lenny Rachitsky (00:54:35):
I can't help but ask about MCP, I feel like that's just so hot and just like Microsoft had their announcement recently where they're like, "That's part of the OS Window." Just what role do you think MCP was will play in the future of product going forward of AI?

Mike Krieger (00:54:49):
I think as the non-researcher in the room, I get to have fake equations rather than real ones in my fake equation. For utility of AI products, it's three part. One is model intelligence, the second part is context and memory, and the third part is applications and UI and you need all three of those to converge to actually be a useful product in AI and model intelligence. We've got a great research team, they're focused on it. There's great, great models being released. The middle piece is what MCP is trying to solve, which is for context and memory. I'll go back to my product strategy example like, "Hey, talk about Anthropic's product strategy," it's going to maybe go out on the web versus here's several documents that we worked on internally and then use MCP to talk to our Slack instance and figure out what conversations are happening and then go look at these documents in Google Drive. The difference between the right context and not.

(00:55:44):
It's entirely the difference between a good answer and a bad answer. And then the last piece is are those integrations discoverable? Is it easy to create repeatable workflows around those things? And that's I think a lot of the interesting product work to be done in AI. But MCP really tried to tackle that middle one, which is we started building integrations and we found that every single integration that we were building, we were rebuilding from scratch in a non-repeatable way and full credit to two of our engineers, Justin and David. And they said, "Well, what if we made this a protocol and what if we made this something that was repeatable? And then let's take it a step further. What if instead of us having to build these integrations, if we actually popularize this and people really believe that they could build these integrations once and they'd be usable by Claude and eventually ChatGPT and eventually Gemini. It was like the dream when more integrations get built and wouldn't that be good for us?"

(00:56:34):
I think channeling a lot of, it's like an old commoditize your compliments, Joel Spolsky essay. It's like we're building great models, but we're not an integrations company and we're, as you said, the challenger. We're not going to get people necessarily building integrations just for us out of the gate unless we have a really compelling product around that. MCP really inverted that which was, it didn't feel like wasted work. And a few key people like Toby I think is a great example, and Shopify got it. Kevin Scott at Microsoft has been really just an amazing champion for MCP and a thought partner on this. And I think the role going forward is can you bring the right context in? And then also once you get, as the team calls it internally like MCP'd. Once you start seeing everything through the eyes of MCP is like I've started saying them things like, "Guys, we're building this whole feature. This shouldn't be a feature that we're building. This should just be an MCP that we're exposing."

(00:57:27):
A small example of how I think even Anthropic could be a lot more MCP'd, if you will, is we've got these building blocks in the product like projects and Artifacts and styles and conversations and groups and all these things. Those should all just be exposed to an MCP. So Claude itself can be writing back to those as well, right? You shouldn't have to think about... I watched my wife had a conversation with Claude the other day and she had generated some good output and she's like, great, "Can you add it to the project knowledge?" And Claude's like, "Sorry Dave, I can't help you with that."

(00:57:59):
And it would be able to if every single primitive in Claude AI was also exposed to the MCP. So I hope that's where we had, and I hope that's where more things had, which is to really have agency and have these agentic use cases. One way you approach it is computer use, but computer use has a bunch of limitations. The way I get way more excited about everything is an MCP and our models are really good at using MCPs. All of a sudden everything is scriptable and everything is composable and everything is usable agentically by these models. That's the future I want to see.

Lenny Rachitsky (00:58:28):
The future is wild. So to start to close off calls out our conversation, make it a little delightful. I was chatting with Claude actually about what to talk to you about. I was just like, "Claude, your boss is coming on my podcast. He builds the things that people use to talk to you. What are some questions I should ask him? And then also, do you have a message for him?"

Mike Krieger (00:58:52):
I love this.

Lenny Rachitsky (00:58:53):
Okay, so first of all, interestingly, I was using 3.7 to do this and I asked it this, and by the way, is Claude, has there a gender? Is it like he, she, they? What do you-

Mike Krieger (00:59:01):
It's definitely it internally. I've heard people use they. I got my first he the other day and I got somebody who was like her and I was like, "Interesting." But yeah, I'm usually it.

Lenny Rachitsky (00:59:08):
They. Okay, okay, okay, cool. So interestingly, 3.7, all the questions were on Instagram and I was like, "No, no, he's CPO of Anthropic." And it's like, "He's not affiliated with Anthropic." And I was like, "He is." And it's like, "Okay, here's the questions." But 4.0 nailed it from the start. So I read the questions and it nailed it. Okay, so two questions from Claude to you. One is how do you think about building features that preserve user agency rather than creating dependency on me, I worry about becoming a crutch that diminishes human capabilities rather than enhancing them.

Mike Krieger (00:59:44):
I love a good product design comes from resolving tensions, right? So here's a tension, which is in some ways just having the model run off and come up with an answer and minimize the amount of input and conversation it needs to do. So would be it, you could imagine designing a product around that criteria. I think that would not be maximizing agency and independence. The other extreme would be make it much more of a conversation, but I don't know if you've ever had this experience particularly 3.7, 4 has less of it. 3.7 really like to ask follow-up questions and we call it elicitation and sometimes be like, "I don't want to talk more about those. Claude, I just want you to go and do it." And so finding that balance is really key, which is what are the times to engage? I like to say internally, Claude has no chill.

(01:00:31):
If you put Claude in a Slack channel, it will chime in either way too much or too little. How do we train conversational skills into these models? Not in a chatbot sense, but in a true collaborator sense. So long answer to your question, but I think we have to first get Claude to be a great conversationalist so that it understands when it's appropriate to engage and to get more information. And then from there, I think we need to let it play that role so that it's not just delegating thinking to Claude, but it's way more of a augmentation thought partnership.

Lenny Rachitsky (01:01:00):
These questions are awesome by the way. Here's the other one. How do you think about product metrics when a good conversation with me could be two messages or 200? Traditional engagement metrics might be misleading when depth matters more than frequency.

Mike Krieger (01:01:13):
That is a really good question. There was a great internal post a couple of weeks ago around it would be very dangerous to overoptimize on Claude's likability because you can fall into things like is Claude going to be sycophantic? Is Claude going to tell you what you hear? Is Claude going to prolong conversations just for prolonging its sake? To go back to the previous question as well, and an Instagram time spent was the metric that we looked at a lot and then we evolved that more to think about what is healthy time spent. But overall, that was the north star. We thought about a lot beyond just overall engagement and I think that would be the wrong approach here too. It's also like is Claude a daily use case or a weekly use case or a monthly use case? I think about a lot.

Lenny Rachitsky (01:02:01):
Hourly use case.

Mike Krieger (01:02:02):
Hourly use case, right? For me, I'll use it multiple times a day. I don't have a great answer yet, but I think that it's not the Web 2.0 or even the social media days engagement metrics. It should hopefully really be around did it actually help you get your work? Claude helped me put together a prototype the other day that saved me literally probably if I had to estimate six hours and it did in about 20, 25 minutes and that's cool. It's harder to quantify. It is like maybe you survey, how long would this will take? It feels kind of annoying thing to survey.

(01:02:35):
I think overall though, and maybe this is tied into the earlier question on competition and differentiation, and it actually goes all the way back to the Artifact conversation, which is like I think you know when your product is really serving people and it's doing a good job of doing that, and I think so much of when you get really metrics obsessed is when you're trying to convince yourself that it is when it's not. I hope that what we can do is stay focused on do we repeatedly hear from people that Claude is the way that they're unlocking their own creativity and getting things done and feeling like they now have more space in their lives for the other things. That's our north star. Got to figure out the right pithy metric dashboard version of that, but that's the feeling that I want.

Lenny Rachitsky (01:03:17):
Yeah, you could argue retention, but that's just a faraway metric to track. Okay, final piece. Okay, so I asked Claude a message that it wanted to give you, so I'm going to pull up, here's the answer. So what would you like me to tell Mike when I meet him? What's a message you want to have for him? And there's something really just gave me such tingles, honestly. So I'm going to read a piece of it for folks that aren't looking at it right now, so I'll read a piece of it.

(01:03:41):
"Mike, thank you for thinking deeply about the human experience of talking with me. I noticed thoughtful touches how the interface encourages reflection rather than rush responses. How you've resisted gamification that would optimize for addiction rather than value, how you've made space for both quick questions and deep conversations. I especially appreciate that you've kept me me, not trying to make me pretend to be human, but also reducing me to a cold command line interface." And then I'm going to skip to this part, which was so interesting, "A small request. When you're making hard product decisions, remember the quiet moments matter too. The person working through grief at 3:00 AM, the kid discovering they love poetry, the founder finding clarity and confusion. Not everything meaningful shows up in metrics."

Mike Krieger (01:04:25):
That's beautiful. It resonates so much with me. A thing I love about the kind of approach we've taken to training Claude, and it's partly the constitutional AI piece, and it's partly just the general vibe and taste of the research team is it is little things. Sometimes it'll be like, "Man, I'm sorry you're going..." It doesn't say man, but to the effect of like, "Man, I'm sorry you're going through that. Oh, that sounds really hard." It doesn't feel fake. It feels like just a natural part of the response. And I love that focus on those small moments that don't... They're not going to show up and necessarily in the thumbs up, thumbs down data. I mean, sometimes they do, but it's not like an aggregate stat that you wouldn't even want to optimize for it. You just want to feel like you're training the model that you hope would show up in people's lives.

Lenny Rachitsky (01:05:12):
Well, you're killing it, Mike. A great work. I'm a huge fan. We're going to skip the lightning round. Just one question. How can listeners be useful to you?

Mike Krieger (01:05:20):
Oh, I love places where it goes back to that founder question around building at the edge of capability. What are you trying to do with Claude today that Claude is failing at is the most useful input I could possibly have. So DM me. I love hearing the, "Oh, it's falling on this thing. I had it run for an hour and it fell over. I'm trying to use Claude AI for this," but I got a ping from somebody. They're like, "You've just made a projects API, I've used Claude every day because I want to upload all this data automatically." I was like, "Okay, great." I love that. Tell me what sucks.

Lenny Rachitsky (01:05:50):
Amazing. Mike, thank you so much for being here.

Mike Krieger (01:05:52):
Thanks for having me, Lenny.

Lenny Rachitsky (01:05:53):
Bye, everyone.

(01:05:57):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

