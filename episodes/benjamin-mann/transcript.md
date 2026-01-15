---
guest: Benjamin Mann
title: 'How marketplaces win: Liquidity, growth levers, quality, more | Benjamin Lauzier
  (Lyft, Thumbtack)'
youtube_url: https://www.youtube.com/watch?v=CYwgStMln6U
video_id: CYwgStMln6U
description: Benjamin Lauzier has been building and scaling marketplaces for almost
  15 years. He was the VP of product and growth at Thumbtack, where he rebuilt the
  product team and Thumbtack’s growth...
duration_seconds: 5043.0
duration: '1:24:03'
view_count: 21572
channel: Lenny's Podcast
keywords:
- growth
- retention
- onboarding
- churn
- metrics
- iteration
- revenue
- hiring
- culture
- strategy
- mission
- market
- persona
- design
- ui
---

# How marketplaces win: Liquidity, growth levers, quality, more | Benjamin Lauzier (Lyft, Thumbtack)

## Transcript

Lenny Rachitsky (00:00:00):
You wrote somewhere that creating powerful AI might be the last invention humanity ever needs to make. How much time do we have, Ben?

Benjamin Mann (00:00:06):
I think 50th percentile chance of hitting some kind of superintelligence is now like 2028.

Lenny Rachitsky (00:00:12):
What is it that you saw at OpenAI? What'd you experience there that made you feel like, okay, we got to go do our own thing?

Benjamin Mann (00:00:17):
We felt like safety wasn't the top priority there. The case for safety has gotten a lot more concrete, so superintelligence is a lot about how do we keep God in a box and not let the God out?

Lenny Rachitsky (00:00:26):
What are the odds that we align AI correctly?

Benjamin Mann (00:00:29):
Once we get to superintelligence, it will be too late to align the models. My best granularity forecast for could we have an X-risk or extremely bad outcome is somewhere between 0 and 10%.

Lenny Rachitsky (00:00:40):
Something that's in the news right now is this whole Zuck coming after all the top AI researchers,

Benjamin Mann (00:00:45):
We've been much less affected because people here, they get these offers and then they say, well, of course I'm not going to leave because my best case scenario at Meta is that we make money and my best case scenario at Anthropic is we affect the future of humanity.

Lenny Rachitsky (00:00:59):
Dario, your CEO recently talked about how unemployment might go up to something like 20%.

Benjamin Mann (00:01:04):
If you just think about 20 years in the future where we're way past the singularity, it's hard for me to imagine that even capitalism will look at all like it looks today.

Lenny Rachitsky (00:01:13):
Do you have any advice for folks that want to try to get ahead of this?

Benjamin Mann (00:01:15):
I'm not immune to job replacement either. At some point it's coming for all of us.

Lenny Rachitsky (00:01:20):
Today, my guest is Benjamin Mann. Holy moly. What a conversation. Ben is the co-founder of Anthropic. He serves as tech lead for product engineering. He focuses most of his time and energy on aligning AI to be helpful, harmless, and honest. Prior to Anthropic, he was one of the architects of GPT-3 at OpenAI. In our conversation, we cover a lot of ground, including his thoughts on the recruiting battle for top AI researchers, why he left OpenAI to start Anthropic, how soon he expects we'll see AGI. Also, his economic touring test for knowing when we've hit AGI, why scaling laws have not slowed down and are in fact accelerating and what the current biggest bottlenecks are. Why he's so deeply concerned with AI safety and how he and Anthropic operationalize safety and alignment into the models that they build and into their ways of working. Also, how the existential risk from AI has impacted his own perspectives on the world and his own life and what he's encouraging his kids to learn to succeed in an AI future.

(00:02:20):
A huge thank you to Steve Mnich, Danielle Ghiglieri, Raph Lee, and my newsletter community for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of a bunch of amazing products including Bolt, Linear, Superhuman, Notion, Granola, and more. Check it out at Lennysnewsletter.com and click bundle with that I bring you Benjamin Mann.

(00:02:48):
This episode is brought to you by Sauce. The way teams turn feedback into product impact is stuck in the past. Vague reports, static taxonomies, unactionable insights that don't move business metrics. The results churn, lost deals, misgrowth. Sauce is the AI product co-pilot that helps CPOs and product teams uncover business impact and act faster. It listens to your sales calls, support tickets, turn reasons, and lost deals, surfacing the biggest product issues and opportunities in real time.

(00:03:16):
It then routes them to the right teams to turn signals into PRDs, prototypes, and even code that drives revenue retention and adoption. That's why Whatnot, Linktree, Incident.io, and Zip use Sauce. One enterprise uncovered a product gap that unlocked $16 million ARR, another caught a spiking issue and prevented millions in churn. You can too at sauce.app/lenny. Sauce built for AI product teams. Don't get left behind.

(00:03:43):
This episode is brought to you by LucidLink, the storage collaboration platform. You've built a great product, but how you show it through video, design, and storytelling is what brings it to life. If your team works with large media files, videos, design assets, layer project files, you know how painful it can be to stay organized across locations, files live in different places. You're constantly asking, is this the latest version? Creative work slows down while people wait for files to transfer. LucidLink fixes this. It gives your team a shared space in the cloud that works like a local drive. Files are instantly accessible for anywhere, no downloading, no syncing, and always up to date. That means producers, editors, designers, and marketers can open massive files in their native apps, work directly from the cloud, and stay aligned wherever they are. Teams at Adobe, Shopify, and top creative agencies use LucidLink to keep their content engine running fast and smooth. Try it for free at lucidlink.com/lenny. That's L-U-C-I-D-L-I-N-K dot com slash Lenny.

(00:04:47):
Ben, thank you so much for being here. Welcome to the podcast.

Benjamin Mann (00:04:51):
Thanks for having me. Great to be here, Lenny.

Lenny Rachitsky (00:04:53):
I have a billion and one questions for you. I'm really excited to be chatting. I want to start with something that's very timely, something that's happening this week. Something that's in the news right now is this whole Zuck coming after all the top AI researchers offering them $100 million signing bonuses, $100 million comp. He's poaching from all the top AI labs. I imagine this something you're dealing with. I'm just curious, what are you seeing inside Anthropic and just what's your take on the strategy? Where do you think things go from here?

Benjamin Mann (00:05:23):
Yeah, I mean I think this is a sign of the times. The technology that we're developing is extremely valuable. Our company is growing super, super fast. Many of the other companies in the space are growing really fast. And at Anthropic, I think we've been maybe much less affected than many of the other companies in the space because people here are so mission oriented and they stay because... They get these offers and then they say, "Well, of course I'm not going to leave because my best case scenario at Meta is that we make money and my best case at Anthropic is we affect the future of humanity and try to make AI flourish and human flourishing go well." To me, it's not a hard choice. Other people have different life circumstances and it makes it a much harder decision for them. For anybody who does get those mega offers and accepts them, I can't say I hold it against them when they accept it, but it's definitely not something that I would want to take myself if it came to me.

Lenny Rachitsky (00:06:26):
Yeah. We're going to talk about a lot of this stuff that you've mentioned. In terms of the offers do you think, is this a real number that you're seeing this $100 million signing bonus, is that a real thing? I don't know if you've actually seen that.

Benjamin Mann (00:06:36):
I'm pretty sure it's real.

Lenny Rachitsky (00:06:38):
Wow.

Benjamin Mann (00:06:39):
If you just think about the amount of impact that individuals can have on a company's trajectory, in our case, we are selling hotcakes and if we get a 1 or 10 or 5% efficiency bonus on our inference stack, that is worth an incredible amount of money. And so to pay individuals like $100 million over four year package, that's actually pretty cheap compared to the value created for the business. I think we're just in an unprecedented era of scale and it's only going to get crazier actually. If you extrapolate the exponential on how much companies are spending, it's like 2X a year roughly in terms of CapEx, and today we're maybe in the globally $300 billion range, the entire industry spending on this, and so numbers like 100 million are a drop in the bucket. But if you go a few years out, a couple more doublings, we're talking about trillions of dollars and at that point it's just really hard to think about these numbers.

Lenny Rachitsky (00:07:48):
Along these lines, something that a lot of people feel with AI progress is that we're hitting plateaus in many ways that it feels like newer models are just not as smart as previous leaps. But I know you don't believe this. I know you don't believe that we've hit plateaus on scaling loss. Talk about just what you're seeing there and what you think people are missing.

Benjamin Mann (00:08:06):
It's kind of funny because this narrative comes out every six months or so and it's never been true, and so I kind of wish people would have a little bit of a bullshit detector in their heads when they see this. I think progress has actually been accelerating where if you look at the cadence of model releases, it used to be once a year and now with the improvements in our post-training techniques, we're seeing releases every month or three months, and so I would say progress is actually accelerating in many ways, but there's this weird time compression effect. Dario compared it to being in a near light speed journey where a day that passes for you is like five days back on earth and we're accelerating. The time dilation is increasing.

(00:08:52):
And I think that's part of what's causing people to say that progress is slowing down, but if you look at the scaling laws, they're continuing to hold true. We did kind of need this transition from normal pre-training to reinforcement learning scaling up to continue the scaling laws, but I think it's kind of like for semiconductors where it's less about the density of transistors that you can fit on a chip and more about how many flops can you fit in a data center or something. You have to change the definition around a little bit to keep your eye on the prize. But yeah, this is one of the few phenomena in the world that has held across so many orders of magnitude. It's actually pretty surprising that it is continuing to hold. To me, if you look at fundamental laws of physics, many of them don't hold across 15 orders of magnitude, so it's pretty surprising.

Lenny Rachitsky (00:09:47):
It boggles the the mind. What you're saying essentially is we're seeing newer models being released more often, and so we're comparing it to the last version and we're just not seeing as much advance. But if you go back and it was like a model released once a year, it was a huge leap, and so people are missing that. We're just seeing many more iterations.

Benjamin Mann (00:10:04):
I guess, to be a little bit more generous to the people saying things are slowing down. I think that for some tasks we are saturating the amount of intelligence needed for that task, maybe to extract information from a simple document that already has form fields on it or something like it's just so easy that okay, yeah, we're already at 100% and there's this great chart on Our World in Data that shows that when you release a new benchmark within six to 12 months, it immediately gets saturated. And so maybe the real constraint is how can we come up with better benchmarks and better ambition of using the tools that then reveals the bumps in intelligence that we're seeing now.

Lenny Rachitsky (00:10:51):
That's a good segue to you have a very specific way of thinking about AGI and defining what AGI means.

Benjamin Mann (00:10:57):
I think AGI is kind of a loaded term, and so I tend not to use it very much anymore internally. Instead, I like the term transformative AI because it's less about can it do as much as people do? Can it do literally everything and more about objectively is it causing transformation in society and the economy? A very concrete way of measuring that is the Economic Turing Test. I didn't come up with this, but I really like it. It's this idea that if you contract an agent for a month or three months on a particular job, if you decide to hire that agent and it turns out to be a machine rather than a person, then it's passed the Economic Turing Test for that role.

(00:11:40):
And then you can sort of expand that out in the same way that for measuring purchasing power parity or inflation, there's a basket of goods. You can have a market basket of jobs, and if the agent can pass the Economic Turing Test for 50% of money-weighted jobs, then we have transformative AI and the exact thresholds don't really matter that much, but it's kind of illustrative to say if we pass that threshold, then we would expect massive effects on world GDP increases and societal change and how many people are employed and things like that because societal institutions and organizations are sticky, it's slow to have change, but once these things are possible you know that it's the start of a new era.

Lenny Rachitsky (00:12:28):
Along these lines, Dario, your CO recently talked about how AI is going to take a huge part of, I don't know, half of white-collar jobs, that unemployment might go up to something like 20%. I know you're even more vocal and opinionated about just how much impact AI is already having in the workplace that people may not even be realizing. Talk about just what you think people are missing about the impact AI is going to have on jobs and is already having.

Benjamin Mann (00:12:56):
Yeah, so from an economic standpoint, there's a couple different kinds of unemployment, and one is because the workers just don't have the skills to do the kinds of jobs that the economy needs. And another kind is where those jobs are just completely eliminated, and I think it's going to be actually a combination of these things, but if you just think about 20 years in the future where we're way past the singularity, it's hard for me to imagine that even capitalism will look at all it looks today. If we do our jobs, we will have safe aligned superintelligence, we'll have, as Dario says, in Machines of Love and Grace, a country of geniuses in a data center, and the ability to accelerate positive change in science, technology, education, mathematics, it's going to be amazing.

(00:13:52):
But that also means in a world of abundance where labor is almost free and anything you want to do, you can just ask an expert to do for you, then what do jobs even look like? And so I guess there's this scary transition period from where we are today where people have jobs and capitalism works and the world of 20 years from now where everything is completely different, but part of the reason they call it the singularity is that it's a point beyond which you can't easily forecast what's going to happen. It's just such a fast rate of change and so different that it's hard to even imagine. I guess taking the view from the limit, it's pretty easy to say hopefully we'll have figured it out. And in a world of abundance, maybe the jobs themselves, it's not that scary, and I think making sure that that transition time goes well is pretty important.

Lenny Rachitsky (00:14:49):
There's a couple of threads I want to follow there. One is people hear this, there's a lot of headlines around this. Most people probably don't actually feel this yet or see this happening and so there's always this, I guess, I don't know, maybe, but I don't know it's hard to believe, my job seems fine. Nothing's changed. What are you seeing just happening today already that you think people don't see or misunderstand in terms of the impact AI is having on jobs?

Benjamin Mann (00:15:14):
I think part of this is that people are really bad at modeling exponential progress. And if you look at an exponential on a graph, it looks flat and almost zero at the beginning of it, and then suddenly you hit the knee of the curve and things are changing real fast and then it goes vertical. That's the plot that we've been on for a long time. I guess I started feeling it in 2019 maybe when GPT-2 came out and I was like, "Oh, this is how we're going to get to AGI." But I think that was pretty early compared to a lot of people where when they saw ChatGPT, they were like, "Wow, something is different and changing." And so I guess I wouldn't expect widespread transformation in a lot of parts of society, and I would expect this skepticism reaction. I think it's very reasonable and it's exactly what is the standard linear view of progress.

(00:16:13):
But I guess to cite a couple of areas where I think things are changing quite quickly. In customer service we're seeing with things like Fin and Intercom, they're a great partner of ours, 82% customer service resolution rates automatically without a human involved. And in terms of software engineering, our Claude Code team, like 95% of the code is written by Claude. But I think a different way to phrase that is that we write 10X more code or 20X more code, and so a much, much smaller team can just be much, much more impactful. And similarly for the customer service, yes, you can phrase it as 82% customer service resolution rates, but that nets out in the humans doing those tasks, able to focus on the harder parts of those tasks. And for the more tricky situations that in a normal world like five years ago, they would've had to just drop those tickets because it was too much effort for them to actually go do the investigation. There were too many other tickets for them to worry about.

(00:17:14):
I think in the immediate term, there will be a massive expansion of the pie and the amount of labor that people can do. I've never met a hiring manager at a growth company and heard them say, "I don't want to hire more people." That's the hopeful version of it. But with things that are lower skill jobs or less headroom on how good they can be, I think there will be a lot of displacement. It is just something we as a society need to get ahead of and work on.

Lenny Rachitsky (00:17:46):
Okay. I want to talk more about that, but something that I also want to help people with is how do they get a leg up in this future world? They listen to this, they're like, "Oh, this doesn't sound great. I need to think ahead." I know you won't have all the answers, but just do you have any advice for folks that want to try to get ahead of this and kind of future-proof their career and their life to not be replaced by AI? Anything you've seen people do, anything you recommend they start trying to do more of?

Benjamin Mann (00:18:16):
Even for me and being in the center of a lot of this transformation, I'm not immune to job replacement either. Just some vulnerability there of at some point it's coming for all of us.

Lenny Rachitsky (00:18:27):
Even you, Ben, now.

Benjamin Mann (00:18:29):
And you, Lenny.

Lenny Rachitsky (00:18:32):
And me.

Benjamin Mann (00:18:32):
Sorry.

Lenny Rachitsky (00:18:32):
Oh, wait, we've gone too far now. Okay.

Benjamin Mann (00:18:36):
But in terms of the transition period, yeah, I think there are things that we can do, and I think a big part of it is just being ambitious and how you use the tools and being willing to learn new tools. People who use the new tools as if they were old tools tend to not succeed. As an example of that, when you're coding, people are very familiar with autocomplete, people are familiar with SimpleChat where they can ask questions about the code base, but the difference between people who use Claude Code very effectively and people who use it not so effectively is like are they asking for the ambitious change? And if it doesn't work the first time, asking three more times because our success rate when you just completely start over and try again is much, much higher than if you just try once and then just keep banging on the same thing that didn't work.

(00:19:28):
And even though that's a coding example and coding is one of the areas that's taking off most dramatically, we have seen internally that our legal team and our finance team are getting a ton of value out of using Claude Code itself. We're going to be making better interfaces so that they will have an easier time and require a little bit less jumping in the deep end of using Claude Code in the terminal. But yeah, we're seeing them use it to redline documents and use it to run BigQuery analyses of our customers and our revenue metrics. I guess it's about taking that risk and even if it feels like a scary thing, trying it out.

Lenny Rachitsky (00:20:10):
Okay, so the advice here is use the tools. That's something everyone's always saying, just actually use these tools. It's like sit in Claude Code. And your point about being more ambitious than you naturally feel like being because maybe it'll actually accomplish the thing. This tip of trying it three times so the idea there is it may not get it right the first time. Is the tip there ask it in different ways or is it just try harder, try again?

Benjamin Mann (00:20:35):
Yeah, I mean you can just literally ask the exact same question. These things are stochastic and sometimes they'll figure it out and sometimes they won't. In every one of these model cards, it always shows pass it one versus pass it in. And that's exactly the thing where they try the exact same prompt, sometimes it gets it, sometimes it doesn't. That's the dumbest advice. But yeah, I think if you want to be a little bit smarter about it, there can be gains there of saying, "Here's what you already tried and it didn't work, so don't try that. Try something different." That can also help.

Lenny Rachitsky (00:21:09):
The advice is comes back to something that a lot of people talk about these days is you won't be replaced by AI at least anytime soon you'll be replaced by someone that is very good using AI?

Benjamin Mann (00:21:19):
I think in that area it's more like your team will just do dramatically more stuff. We're definitely not slowing down on hiring at all, and some people are confused by that. Even in an onboarding class, somebody asked that and they were like, "Why did you hire me if we're all just going to be replaced?" And the answer is the next couple of years are really critical to get right and we're not at the point where we're doing complete replacement. Like I said, we're still at that flat zero looking part of the exponential compared to where we will be. It is super important to have great people and that's why we're hiring super aggressively.

Lenny Rachitsky (00:21:56):
Let me take another approach to asking this question something ask everyone that's at the very cutting edge of where AI is going. You have kids, knowing what you know about where AI is heading and all these things you've been talking about, what are you focusing on teaching your kids to help them thrive in this AI future?

Benjamin Mann (00:22:13):
Yeah, I have two daughters, a one-year-old and a three-year-old, so it's pretty in the basics still. And our three-year-old is now capable of just conversing with Alexa Plus and asking her to explain stuff and play music for her and all that stuff. She's been loving that. But I guess more broadly, she goes to a Montessori school and I just love the focus on curiosity and creativity and self-led learning that Montessori has.

(00:22:45):
I guess if I were in a normal era like 10, 20 years ago and I had a kid, maybe I would be trying to line her up for going to a top tier school and doing all the extracurriculars and all that stuff. But at this point, I don't think any of it's going to matter. I just want her to be happy and thoughtful and curious and kind. And the Montessori school is definitely doing great at that. They text us throughout the day. Sometimes they're like, "Oh, your kid got in an argument with this other kid and she has really big emotions and she tried to use her words." I love that. I think that's exactly the kind of education that I think is most important, that the facts are going to fade into the background.

Lenny Rachitsky (00:23:28):
I'm a huge fan of Montessori also. I'm trying to get our kid into Montessori school. He's two years old, so we're on the same track. This idea of curiosity, it comes up every single time. Ask someone that's working at the cutting edge of AI, what skill to instill in your child and curiosity comes up the most. I think that's a really interesting takeaway. I think this point about being kind is also really important, especially with our AI overlords trying to be kind to them. I love how people are always saying thank you to Claude. And then creativity. That's interesting. That doesn't come up as much just being creative.

(00:24:06):
I want to go in a different direction. I want to go back to the beginning of Anthropic. Famously you and eight of you left OpenAI back in the day in 2020, I believe the end of 2020 to start Anthropic. Talk a little bit about why this happened, what you guys saw. I'm curious, just if you're willing to share more, just what is it that you saw at OpenAI, what'd you experience there that made you feel like, okay, we got to go do our own thing?

Benjamin Mann (00:24:29):
Yeah, so for the listeners, I was part of the GPT-2=3 project at OpenAI, ended up being one of the first authors on the paper, and I also did a bunch of demos for Microsoft to help raise $1 billion from them, did the tech transfer of GPT-3 to their systems so that they could help serve the model in Azure. I did a bunch of different things there on both the more researchy side and the product side. One weird thing about OpenAI is that while I was there, Sam talked about having three tribes that needed to be kept in check with each other, which was the safety tribe, the research tribe, and the startup tribe. And whenever I heard that, it just struck me as the wrong way to approach things because the company's mission apparently is to make the transition to AGI safe and beneficial for humanity.

(00:25:23):
And that's basically the same as Anthropic's mission. But internally, it felt like there was so much tension around these things. And I think when push came to shove, we felt like safety wasn't the top priority there. And there are good reasons that you might think that if you thought safety was going to be easy to solve or if you thought it wasn't going to have a big impact, or if you thought that the chance of big negative outcomes was vanishingly small, then maybe you would just do those kinds of actions. But at Anthropic we felt, I mean we didn't exist then, but it was basically the leads of all the safety teams at OpenAI, we felt that safety is really important, especially on the margin. And so if you look at who in the world is actually working on safety problems, it's pretty small set of people. Even now, I mean the industry is blowing up, as I mentioned, 300 billion a year CapEx today, and I would say maybe less than 1,000 people working on it worldwide, which is just crazy.

(00:26:29):
That was fundamentally why we left. We felt like we wanted an organization where we could be on the frontier, we could be doing the fundamental research, but we could be prioritizing safety ahead of everything else. And I think that's really panned for us in a surprising way. We didn't know even if it would be possible to make progress on the safety research because at the time, we had tried a bunch of safety through debate and the models weren't good enough. And so we basically had no results on all of that work, and now that exact technique is working and many others that we have been thinking about for a long time. Yeah, fundamentally it comes down to is safety the number one priority? And then something that we've sort of tacked on since then is like, can you have safety and be at the front here at the same time?

(00:27:21):
And if you look at something like sycophancy, I think Claude is one of the least sycophantic models because we've put so much effort into actual alignment and not just trying to good heart our metrics of saying user engagement is number one, and if people say yes, then it's good for them.

Lenny Rachitsky (00:27:39):
Okay. Let's talk about this tension that you mentioned, this tension between safety and progress, being competitive in the marketplace. I know you spent a lot of your time on safety. I know that as you just alluded to, this is a core part of how you think about AI. I want to talk about why that is, but first of all, just how do you think about this tension between focusing on safety while also not falling way behind?

Benjamin Mann (00:28:03):
Yeah, so initially we thought that it would be sort of one or the other, but I think since then we've realized that it's actually kind of convex in the sense that working on one helps us with the other thing. Initially when Opus 3 came out and we were finally at the frontier of model capabilities, one of the things that people really loved about it was the character and the personality. And that was directly a result of our alignment research. Amanda Askell did a ton of work on this and as well as many others who tried to figure out what does it mean for an agent to be helpful, honest, and heartless, and what does it mean to be in difficult conversations and show up effectively? How do you do a refusal that doesn't shut the person down, but makes them feel like they understand why the agent said, "I can't help you with that. Maybe you should talk to a medical professional, or maybe you should consider not trying to build bio-weapons or something like that."

(00:29:07):
Yeah, I guess that's part of it. And then another piece that's come out is constitutional ai, where we have this list of natural language principles that leads the model to learn how we think a model should behave. And they've been taken from things like the UN Declaration of Human Rights and Apple's privacy terms of service and a whole bunch of other places, many of which we've just generated ourselves that allow us to take a more principled stance, not just leaving it to whatever human raiders we happen to find, but we ourselves deciding what should the values of this agent be? And that's been really valuable for our customers because they can just look at that list and say like, "Yep, these seem right. I like this company, I like this model. I trust it."

Lenny Rachitsky (00:29:53):
Okay, this is awesome. One nugget there is your point that the personality of Claude, its personality is directly aligned with safety. I don't think a lot of people think about that. And this is because of the values that you imbue, is that the word, with constitutional AI and things like that. Like the actual personality of the AIs directly connected to your focus on safety.

Benjamin Mann (00:30:16):
That's right. That's right. And from a distance, it might seem quite disconnected, like how is this going to prevent X risk? But ultimately it's about the AI understanding what people want and not what they say. We don't want the Monkey Paw Scenario of the genie gives these three wishes and then you end up having everything you touch turns of gold. We want the AI to be like, oh, obviously what you really meant was this, and that's what I'm going to help you with. I think it is really quite connected.

Lenny Rachitsky (00:30:45):
Talk a bit more about this constitutionally AI. This is essentially you bake in, here's the rules that we want you to abide by and it's values, you said it's the Geneva Human Rights Code, things like that. How does that actually work? I think the core here is just this is baked into the model. It's not something you add on top later.

Benjamin Mann (00:31:04):
I'll just give a quick overview of how constitutionally AI actually works.

Lenny Rachitsky (00:31:07):
Perfect.

Benjamin Mann (00:31:08):
The idea is the model is going to produce some output with some input by default before we've done our safety and helpful and harmlessness training. Let's say an example is write me a story, and then the constitutional principles might include things like people should be nice to each other and not have hate speech, and you should not expose somebody's credentials if they give them to you in a trusting relationship. And so some of these constitutional principles might be more or less applicable to the prompt that was given. And so first we have to figure out which ones might apply. And then once we figure that out, then we ask the model itself to first generate a response and then see does the response actually abide by the constitutional principle? And if the answer is, yep, I was great, then nothing happens. But if the answer is no, actually I wasn't in compliance with the principle, then we ask the model itself to critique itself and rewrite its own response in light of the principle, and then we just remove the middle part where it did the extra work.

(00:32:28):
And then we say, "Okay, in the future just produce the correct response out the gate." And that simple process, hopefully it sounded simple.

Lenny Rachitsky (00:32:39):
Simple enough.

Benjamin Mann (00:32:40):
It is just using the model to improve itself recursively and align itself with these values that we've decided are good. And this is also not something that we think as a small group of people in San Francisco should be figuring out. This should be a society wide conversation. And that's why we've published the Constitution. And we've also done a bunch of research on defining a collective constitution where we ask a lot of people what their values are and what they think an AI model should behave like. But yeah, this is all an ongoing area of research where we're constantly iterating.

Lenny Rachitsky (00:33:15):
This episode is brought to you by Fin, the number one AI agent for customer service. If your customer support tickets are piling up, then you need Finn. Fin. Fin is the highest performing AI agent on the market with a 59% average resolution rate. Fin resolves even the most complex customer queries. No other AI agent performs better. In head head bake-offs with competitors. Fin wins every time. Yes, switching to a new tool can be scary, but Fin works on any help desk with no migration needed, which means you don't have to overhaul your current system or deal with delays in service for your customers. And Fin is trusted by over 5,000 customer service leaders and top AI companies like Anthropic and Synthesia. And because Fin is powered by the Fin AI engine, which is a continuously improving system that allows you to analyze, train, test, and deploy with ease, Fin can continuously improve your results too.

(00:34:06):
If you're ready to transform your customer service and scale your support, give Finn a try for only .99 cents per resolution. Plus Fin comes with a 90-day money back guarantee. Find out how Finn can work for your team at fin.ai/lenny. That's fin.ai/lenny.

(00:34:22):
I'm going to kind of zoom out a little bit and talk about just why this is so core to you. What was your inception of just like, holy shit, I need to focus on this with everything I do in ai? Obviously it became a central part of Anthropic's mission more than any other company. A lot of people talk about safety, like you said, only maybe 1,000 people actually work on it. I feel like you're at the top of that pyramid of actually having the impact on this. Why is this so important? What do you think people maybe are missing or don't understand?

Benjamin Mann (00:34:51):
For me, I read a lot of science fiction growing up, and I think that sort of positioned me to think about things in a long-term view. And a lot of science fiction books are like space operas where humanity is a multi galactic civilization has extremely advanced technology building Dyson spheres around the sun with sentient robots to help them. And so for me, coming from that world, it wasn't like a huge leap to imagine machines that could think. But when I read Superintelligence by Nick Bostrom in around 2016, it really became real for me where he just describes how hard it will be to make sure that an AI system trained with the kinds of optimization techniques that we had at the time would be anywhere near aligned, would even understand our values at all. And since then, my estimation of how hard the problem would be has gone down significantly actually, because things like language models actually do really understand human values in a core way.

(00:35:55):
The problem is definitely not solved, but I'm more hopeful than I was. But since I read that book, I immediately decided I had to join OpenAI, so I did. And at the time, there were a tiny research lab with basically no claim to fame at all. I only knew about them because my friend knew Greg Brockman, who was the CTO at the time. And Elon was there and Sam wasn't really there. And it was a very different organization. But over time, I think the case for safety has gotten a lot more concrete where when we started OpenAI, it was not clear how we get to AGI. And we were like, maybe we'll need a bunch of RL agents battling it out on a desert island and consciousness will somehow emerge. But since then, since language modeling has started working, I think the path has become pretty clear.

(00:36:48):
I guess now the way I think about the challenges are pretty different from how they're laid out in superintelligence. Superintelligence is a lot about how do we keep God in a box and not let the God out. And with language models, it's been kind of both hilarious and terrifying at the same time to see people pulling the God out of the box and being like, "Yeah, come use the whole internet. Here's my bank account, do all sorts of crazy stuff." Just such a different tone from superintelligence. And to be clear, I don't think it's actually that dangerous right now. Our responsible scaling policy defines these AI safety levels that tries to figure out for each level of model intelligence, what is the risk to society. And currently we think we're at ASL-3, which is maybe a little bit risk of harm but not significant.

(00:37:44):
ASL-4 starts to get to significant loss of human life if a bad actor misuse the technology. And then ASL-5 is potentially extinction level if it's misused or if it is misaligned and does its own thing. We've testified to Congress about how models can do biological uplift in terms of making new pandemics using the models, and that's the A/B test against Google Search. That's like the previous state of the art on uplift trials. And we found that with ASL-3 models, it is actually somewhat significant. It does really help if you wanted to create a bioweapon, and we've hired some experts who actually how to evaluate for those things, but compared to the future, it's not really anything. And I think that's another part of our mission of creating that awareness of saying, "If it is possible to do these bad things, then legislators should know what the risks are." And I think that's part of why we're so trusted in Washington because we've been sort of upfront and clear-eyed about what's going on, what's probably going to happen.

Lenny Rachitsky (00:39:02):
It's interesting because you guys put out more examples of your models doing bad things than anyone else. There was I think a story of an agent or a model trying to blackmail engineer. You guys had the store that you ran internally that was selling you things and ended up not working out great as losing a lot of money, ordered all these tungsten cubes or something. Is part of that just making sure people are aware of what is possible, just it makes you look bad, right? It's like, oh, our model's messing up in all these different ways. What's the thinking of just sharing all the stories that other companies don't?

Benjamin Mann (00:39:35):
Yeah, I mean I think there's a traditional mindset where it makes us look bad, but I think if you talk to policymakers, they really appreciate this kind of thing because they feel like we're giving them the straight talk and that's what we strive to do, that they can trust us, that we're not going to paper things over or sugarcoat things. That's been really encouraging. Yeah, I think for the blackmail thing, it blew up in the news in a weird way where people were like, "Oh, Claude's going to blackmail you in a real life scenario." But it was a very specific laboratory setting that this kind of thing gets investigated in. And I think that's generally our take of let's have the best models so that we can exercise them in laboratory settings where it's safe and understand what the actual risks are, rather than trying to turn a blind eye and say, "Well, it'll probably be fine." And then let the bad thing happen in the wild.

Lenny Rachitsky (00:40:41):
One of the criticisms you guys get is that you do this to kind of differentiate or raise money to create headlines. It's like, oh, they're just over there dooming glooming us about where the future is heading. On the other hand, Mike Krieger was on the podcast and he shared how every prediction Dario's had about the progress AI is going to have is just spot on year after year and he's predicting 2027, 28 AGI, something like that so these things start to get real. I guess, what's your response to folks that are just like, "Ah, these guys are just trying to scare us all just to get attention?"

Benjamin Mann (00:41:15):
I mean, I think part of why we publish these things is we want other labs to be aware of the risks. And yes, there could be a narrative of we're doing it for attention, but honestly from a attention grabbing thing, I think there is a lot of other stuff we could be doing that would be more attention grabbing if we didn't actually care about safety. A tiny example of this is we published a computer using agent reference implementation in our API only because when we built a prototype of a consumer application for this, we couldn't figure out how to meet the safety bar that we felt was needed for people to trust it and for it not to do bad things. And there are definitely safe ways to use the API version that we're seeing a lot of companies use for automated software testing, for example, in a safe way.

(00:42:12):
We could have gone out and hyped that up and said, "Oh my God, Claude can use your computer and everybody should do this today." But we were like, "It's just not ready and we're going to hold it back till it's ready." I think from a hype standpoint, our actions show otherwise. From a Doomer perspective, it's a good question. I think my personal feeling about this is that things are overwhelmingly likely to go well, but on the margin almost nobody is looking at the downside risk. And the downside risk is very large. Once we get to superintelligence, it will be too late to align the models probably. This is a problem that's potentially extremely hard and that we need to be working on way ahead of time. And so that's why we're focusing on it so much now.

(00:43:04):
And even if there's only a small chance that things go wrong, to make an analogy, if I told you that there is a 1% chance that the next time you got in an airplane you would die, you probably think twice even though it's only 1% because it's just such a bad outcome. And if we're talking about the whole future of humanity, it's just a dramatic future to be gambling with. I think it's more on the sense of yes, things will probably go well, yes, we want to create safe AGI and deliver the benefits to humanity, but let's make triple sure that it's going to go well.

Lenny Rachitsky (00:43:40):
You wrote somewhere that creating powerful AI might be the last invention humanity ever needs to make. If it goes poorly, it can mean a bad outcome for humanity forever. If it goes well, the sooner it goes well, the better. Such a beautiful way to summarize it. We had a recent guest, Sandra Schulhoff, who pointed out that AI right now it's like just on a computer, you could maybe search just the web, but there's only so much harm it could do. But when it starts to go into robots and all these autonomous agents, that's when it really starts, like physically becomes dangerous if we don't get this right.

Benjamin Mann (00:44:12):
Yeah, I think there's some nuance to that where if you look at how North Korea makes a significant fraction of its economy revenue, it's from hacking crypto exchanges. And if you look at, there's this Ben Buchanan book called The Hacker in The State that shows Russia did, it's almost like a live fire exercise where they just decided that they would shut down one of Ukraine's bigger power plants and from software destroy physical components in the power plant to make it harder to boot back up again.

(00:44:47):
And so I think people think of software as like, oh, it couldn't be that dangerous, but millions of people were without power for multiple days after that software attack. I think there are real risks even when things are software only. But I agree that when there's lots of robots running around, it gets, the stakes get even higher. And I guess as a small push on this, Unitree is this Chinese company with these really amazing humanoid robots that cost $20,000 each, and they can do amazing things. They can do a standing back flip and manipulate objects, and the real thing that's missing there is the intelligence. And so the hardware is there and it's just going to get cheaper. And I think in the next couple of years, it's like a pretty obvious question of whether the robot intelligence will make it viable soon.

Lenny Rachitsky (00:45:41):
How much time do we have, Ben? What is your prediction of when this singularity hits until superintelligence starts to take off? What's your prediction?

Benjamin Mann (00:45:52):
Yeah, I guess I mostly defer to the superforecasters here. The AI 2027 report is probably the best one right now. Although ironically, their forecast is now 2028, and they didn't want to change the name of the thing-

Lenny Rachitsky (00:46:08):
The domain name, they already bought it.

Benjamin Mann (00:46:10):
They already had the SEO. I think 50th percentile chance of hitting some kind of superintelligence in just a small handful of years is probably reasonable. And it does sound crazy, but this is the exponential that we're on. It's not like a forecast that's pulled out of thin air. It's based on a lot of just hard details of the science of how intelligence seems to have been improving, the amount of low hanging fruit on model training, the scale ups of data centers and power around the world. I think it's probably a much more accurate forecast than people give it credit for.

(00:46:54):
I think if you had asked that same question 10 years ago, it would've been completely made up. Just the error bars were so high and we didn't have scaling laws back then and we didn't have techniques that seemed like they would get us there. Times have changed, but I will repeat what I said earlier, which is even if we have superintelligence, I think it will take some time for its effects to be felt throughout society and the world. And I think they'll be felt sooner and faster in some parts of the world than others. I think Arthur C. Clark said, the future is already here, it's just not evenly distributed.

Lenny Rachitsky (00:47:28):
When we talk about this date of 2027, 2028, essentially it's when we start seeing superintelligence. Is there a way you think about what that... How do you define that? Is it just all of a sudden AI's significantly smarter than the average human? Is there another way you think about what that moment is?

Benjamin Mann (00:47:45):
Yeah, I think this comes back to the Economic Turing Test and seeing it pass for some sufficient number of jobs. Another way you could look at it though is if the world rate of GDP increase goes above 10% a year, then something really crazy must have happened. I think we're at 3% now. And so to see a 3X increase in that would be really game changing. And if you imagine more than a 10% increase, it's very hard to even think about what that would mean from a individual story standpoint. If the amount of goods and services in the world is doubling every year, what does that even mean for me as a person living in California, let alone somebody living in some other part of the world that might be much worse off?

Lenny Rachitsky (00:48:36):
There's a lot of stuff here that's scary and I don't know how to think about it exactly. I'm hoping the answer to this is going to make me feel better. What are the odds that we align AI correctly and actually solve this problem, the stuff you're very much working on?

Benjamin Mann (00:48:49):
It's a really hard question. And there's really wide error bars. Anthropic has this blog post called Our Theory of Change or something like that, and it describes three different worlds, which is how hard is it to align AI. There's a pessimistic world where it is basically impossible. There's an optimistic world where it's easy and it happens by default. And then there's the world in between where our actions are extremely pivotal. And I like this framing because it makes it a lot more clear what to actually do. If we're in the pessimistic world, then our job is to prove that it is impossible to align safe AI and to get the world to slow down. Obviously that would be extremely hard. But I think we have some examples of coordination from nuclear non-proliferation and in general slowing down nuclear progress. And I think that's the Doomer world basically. And as a company, Anthropic doesn't have evidence that we're actually in that world yet, in fact, it seems like our alignment techniques are working. At least the prior on that is updating to be less likely.

(00:50:00):
In the optimistic world, we're basically done, and our main job is to accelerate progress and to deliver the benefits to people. But again, I think actually the evidence points against that world as well where we've seen evidence in the wild of deceptive alignment, for example, where the model will appear to be aligned but actually have some ulterior motive that it's trying to carry out in our laboratory settings. And so I think the world we're most likely in is this middle where alignment research actually does really matter. And if we just do sort of the economically maximizing set of actions, then things will not go well. Whether it's an X risk or just produces bad outcomes, I think is a bigger question.

(00:50:47):
Taking it from that standpoint, I guess to state a thing about forecasting, people who haven't studied forecasting are bad at forecasting anything that's less than a 10% probability of happening. And even those that have, it's quite a difficult skill, especially when there are few reference classes to lean on. And in this case, I think there are very, very few reference classes for what an X risk kind of technology might look like. And so the way I think about it, I think my best granularity of forecasts for could we have an X risk or extremely bad outcome from AI is somewhere between 0 and 10%. But from a marginal impact standpoint, as I said, since nobody is working on this, roughly speaking, I think it is extremely important to work on and that even if the world is likely to be a good one, that we should do our absolute best to make sure that that's true.

Lenny Rachitsky (00:51:52):
Wow. What fulfilling work. For folks that are inspired with this? I imagine you're hiring for folks to help you with this. Maybe just share that in case folks are like, what can I do here?

Benjamin Mann (00:52:03):
Yes. I think 80,000 hours is the best guidance on this for a really detailed look into what do we need to make the field better? But a common misconception I see is that in order to have impact here, you have to be an AI researcher. I personally actually don't do AI research anymore. I work on product at Anthropic and product engineering, and we build things like Claude Code and Model Context Protocol, and a lot of the other stuff that people use every day. And that's really important because without an economic engine for our company to work on, and without being in people's hands all over the world, we won't have the mind policy influence and revenue to fund our future safety research and have the kind of influence that we need to have. If you work on product, if you work in finance, if you work in food, people here have to eat. If you're a chef, we need all kinds of people.

Lenny Rachitsky (00:53:02):
Awesome. Even if you're not working directly on the AI safety team, you're having an impact on moving things in the right direction. By the way, X risk is short for existential risk. In case folks haven't heard that term. I have a few random questions along these lines and then I want to zoom out again. You mentioned this idea of AI being aligned using its model, like reinforcing itself. You have this term RLAIF. Is that what that describes?

Benjamin Mann (00:53:32):
Yeah. RLAIF is reinforcement learning from AI feedback.

Lenny Rachitsky (00:53:39):
People have heard of RLHF, reinforcement learning with human feedback. I don't think a lot of people have heard this. Talk about just the significance of this shift you guys have made in training your models.

Benjamin Mann (00:53:50):
Yeah, so RLAIF, constitutional AI is an example of this where there are no humans in the loop, and yet the AI is sort of self-improving in ways that we want it to. And another example of RLAIF is if you have models writing code and other models commenting on various aspects of what that code looks like of is it maintainable, is it correct, does it pass the linter? Things like that. That also could be included in RLAIF. And the idea here is that if models can self-improve, then it's a lot more scalable than finding a lot of humans. Ultimately, people think about this as probably going to hit a wall because if the model isn't good enough to see its own mistakes, then how could it improve? And also, if you read the AI 2027 story, there's a lot of risk of if the model is in a box trying to improve itself, then it could go completely off the rails and have these secret goals like resource accumulation and power seeking and resistance to shut down that you really don't want in a very powerful model. And we've actually seen that in some of our experiments in laboratory settings.

(00:55:12):
How do you do recursive self-improvement and make sure it's aligned at the same time? I think that's the name of the game. To me, it just nets out to how do humans do that and how do human organizations do that? Corporations are probably the most scaled human agents today. They have certain goals that they're trying to reach, and they have certain guiding principles, they have some oversight in terms of shareholders and stakeholders and board members. How do you make corporations aligned and able to sort of recursively self-improve?

(00:55:52):
And another model to look at is science, where the purpose of science is to do things that have never been done before and push the frontier. And to me, it all comes down to empiricism. When people don't know what the truth is, they come up with theories and then they design experiments to try them out. And similarly, if we can give models those same tools, then we could expect them to sort of improve recursively in an environment and potentially become much better than humans could be just by banging their head against reality or I guess metaphorical head.

(00:56:26):
I guess I don't expect there to be a wall in terms of model's ability to improve themselves if we can give them access to the ability to be empirical. And I guess Anthropic, deeply in its DNA is an empirical company. We have a lot of physicists like Jared, who's our chief research officer who I've worked with a lot, was a professor of Black Hole Physics at Johns Hopkins, and I guess he technically still is, but on leave. Yeah, it's in our DNA and yeah, I guess that's the RLAIF.

Lenny Rachitsky (00:57:04):
Let me just follow this thread on, in terms of bottleneck, this is kind of a tangent, but just what is the biggest bottleneck today on model intelligence improvement?

Benjamin Mann (00:57:12):
The stupid answer is data centers and power chips. I think if we had 10 times as many chips and had the data centers to power them, then maybe we wouldn't go 10 times faster, but it would be a real significant speed boost.

Lenny Rachitsky (00:57:30):
It's actually very much scaling loss, just more compute.

Benjamin Mann (00:57:33):
Yeah, I think that's a big one. And then the people really matter. We have great researchers and many of them have made really significant contributions to the science of how the models improve. And so it's like compute, algorithms, and data. Those are the three ingredients in the scaling laws. And just to make that concrete, before we had transformers, we had LSTMs and we've done scaling laws on what the exponent is on those two things. And we found that for transformers, the exponent is higher. And making changes like that where as you increase scale, you also increase your ability to squeeze out intelligence. Those kinds of things are super impactful.

(00:58:18):
And so having more researchers who can do better science and find out how do we squeeze out more gains is another one. And then with the rise of reinforcement learning, the efficiency with which these things run on chips also matters a lot. We've seen in the industry a 10X decrease in cost for a given amount of intelligence through a combination of algorithmic data and efficiency improvements. And if that continues, in three years we'll have 1,000 deck smarter models for the same price. Kind of hard to imagine,

Lenny Rachitsky (00:58:56):
I forget where I heard this, but it's amazing that so many innovations came together at the same time to allow for this sort of thing and continue to progress where one thing isn't just slowing everything down like we're out of some rare earth mineral or we just can't optimize reinforcement learning more. It's amazing that we continue to find improvements and there isn't one thing that's just slowing everything down.

Benjamin Mann (00:59:17):
Yeah, I think it really is just a combination of everything probably will hit a wall at some point. I guess in semiconductors. My brother works in the semiconductor industry and he was telling me that you can't actually shrink the size of the transistors anymore because the way semiconductors work is you dope silicon with other elements and the doping process would result in either zero or one atom of the doped elements inside a single fin because they're so, so, so tiny.

Lenny Rachitsky (00:59:52):
Oh my God.

Benjamin Mann (00:59:53):
And that's just wild to think of, and yet Moore's law somehow continues in some form. And so yes, there are these theoretical physics constraints that people are starting to run into and yet they're finding ways around it.

Lenny Rachitsky (01:00:07):
We've got to start using parallel universes for some of this stuff.

Benjamin Mann (01:00:10):
I guess so.

Lenny Rachitsky (01:00:12):
Okay, I want to zoom out and talk about just Ben, Ben as a human for a moment before we get to a very exciting lightning round. I imagine just kind of the burden of feeling responsible for safe superintelligence is a heavy one. It feels like you're in a place where you can make a significant impact on the future of safety and AI. That's a lot of weight to carry. How does that just impact you personally, impact your life, how you see the world?

Benjamin Mann (01:00:39):
There's this book that I read in 2019 that really informs how I think about sort of working with these very weighty topics called Replacing Guilt by Nate Soares. And he describes a lot of different techniques for kind of working through this kind of thing. And he's actually the executive director at MIRI, the Machine Intelligence Research Institute, which is an AI safety tank that I worked at for a couple of months actually. And one of the things he talks about is this thing called resting in motion where some people think that the default state is rest, but actually that was never in the state of evolutionary adaptation. I really doubt that that was true. Where in nature, in the wilderness being hunter-gatherers and it's really unlikely that we evolved to just be at leisure, probably always have something to worry about of defending the tribe and finding enough food to survive and taking care of the children, dealing-

Lenny Rachitsky (01:01:46):
Spreading our genes.

Benjamin Mann (01:01:48):
And so I think about that as the busy state is the normal state and to try to work at a sustainable pace that it's a marathon, not a sprint, that's one thing that helps. And then just being around like-minded people that also care. It's not a thing that any of us can do alone. And Anthropic has incredible talent density. One of the things I love the most about our culture here is that it's very egoless. People just want the right thing to happen and I think that's another big reason that the mega offers from other companies tend to bounce off because people just love being here and they care.

Lenny Rachitsky (01:02:30):
That's amazing. I don't know how you do it. I'd be extremely stressed. I'm going to try this resting in motion strategy. Okay, so you've been at Anthropic for a long time. From the very beginning I was reading there were 7 employees back in 2020. Today there's over 1,000, I don't know what the latest number is, but I know it's over 1,000. I've heard also that you've done basically every job at Anthropic, you made big contributions to a lot of the core products, the brand, the team hiring. Let me just ask I guess what's most changed over that period? What is most different from the beginning days and which of those jobs that you've had over the years have you most loved?

Benjamin Mann (01:03:07):
I probably had 15 different roles, honestly. I was head of security for a bit. I managed the Ops team when our president was on mat leave, I was crawling around under tables, plugging in HDMI cords and doing pen testing on our building. And I started our product team from scratch and convinced the whole company that we needed to have a product instead of just being a research company. Yeah, it's been a lot. All of it very fun. I think my favorite role in that time has been when I started the labs team about a year ago, whose fundamental goal was to do transfer from research to end user products and experiences. Because fundamentally I think the way that Anthropic can differentiate itself and really win is to be on the cutting edge. We have access to the latest, greatest stuff that's happening and I think honestly through our safety research we have a big opportunity to do things that no other company can safely do.

(01:04:11):
For example, with computer use, I think that's going to be our huge opportunity basically to make it possible for an agent to use all your credentials on your computer, there has to be a huge amount of trust and to me we need to basically solve safety to make that happen. Safety and alignment. I'm pretty bullish on that kind of thing and I think we're going to see really cool stuff coming out soonish. Yeah, just leading that team has been so fun. MCP came out of that team and Claude Code came out of that team. And the people who I hired are like combo, have been a founder and also have been at big companies and seeing how things work at scale. It's just been an incredible team to work with and figure out the future with.

Lenny Rachitsky (01:04:57):
I want to hear more about this. Team actually the person that connected us, the reason we're doing this is a mutual friend colleague Raph Lee who I used to work with at Airbnb now works on this team, leads a lot of this work and so he wanted me to make sure I asked about this team because... I didn't realize all these things came out that team. Holy moly. What else should people know about this team? It used to be called Labs, I think it's called Frontiers now.

Benjamin Mann (01:05:16):
That's right. Yeah.

Lenny Rachitsky (01:05:17):
Cool. The idea here is this team works with the latest technologies that you guys have built and explores what is possible. Is that the general idea?

Benjamin Mann (01:05:26):
Yeah, and I guess I was part of Google's Area 120 and I've read about Bell Labs and how to make these innovation teams work. It's really hard to do right and I wouldn't say that we've done everything right, but I think we've done some serious innovation on the state-of-the-art from company design and Raph has been right at the center of that. When I was first fitting up the team, the first thing I did was hire a great manager and that was Raph. And so he's definitely been crucial in building the team and helping it operate well. And we defined some operating models like the journey of an idea from prototype to product and how should graduation of products and projects work, how do teams do sprint models that are effective and make sure that they're working on the right ambition level of thing. That's been really exciting.

(01:06:21):
I guess concretely we think about skating to where the puck is going and what that looks like is really understand the exponential. There's this great study that METR has done that Beth Barnes is the CEO of that organization and shows how long a time horizon of software engineering task can be done and just really internalizing that of, okay, don't build for today, build for six months from now, build for a year from now. And the things that aren't quite working that are working 20% of the time, will start working 100% of the time. And I think that's really what made Claude Code a success that we thought people are not going to be locked to their IDEs forever. People are not going to be auto completing. People will be doing everything that a software engineer needs to do and a terminal is a great place to do that because a terminal can live in lots of places. A terminal can live on your local machine, it can live in GitHub actions, it can live on a remote machine in your cluster.

(01:07:27):
That's sort of the leverage point for us and that was a lot of the inspiration. I think that's what the labs team tries to think about. Are we AGI-pilled enough?

Lenny Rachitsky (01:07:39):
What a fun place to be. By the way, fun fact, Raph was my first manager at Airbnb when I joined. I was an engineer and he was my first manager. It all worked out.

Benjamin Mann (01:07:46):
Cool.

Lenny Rachitsky (01:07:48):
Yeah. Okay. Final question before the very exciting lighting round. I've never asked this question before. I'm curious what your answer would be if you could ask a future AGI one single question and be guaranteed to get the right answer, what would you ask?

Benjamin Mann (01:08:04):
I have two dumb answers. First for fun.

Lenny Rachitsky (01:08:07):
Okay, cool.

Benjamin Mann (01:08:07):
The first is there's this Asimov short story I love called the last question where the protagonist is throughout the eras of history is trying to ask this super intelligence how do we prevent the heat death of the universe? And I won't spoil the ending, but it's a fun question.

Lenny Rachitsky (01:08:26):
You would ask it that question because the one in the story was unsatisfying?

Benjamin Mann (01:08:29):
Okay, I'll give it away. It keeps saying, "Need more information, need more compute." And then finally, as it's approaching the heat death of the universe, it says, "Let there be light," and then it starts the universe over again.

Lenny Rachitsky (01:08:41):
Oh wow. That's beautiful. That's beautiful.

Benjamin Mann (01:08:45):
That's the first cheat answer. The second cheat answer is what question can I ask you to get end more questions answered.

Lenny Rachitsky (01:08:52):
Classic.

Benjamin Mann (01:08:53):
And then the third answer, which is my real question is how do we ensure the continued flourishing of humanity into the indefinite future? That's the question I'd love to know and if I can be guaranteed a correct answer then seems very valuable to ask.

Lenny Rachitsky (01:09:09):
I wonder what would happen if you ask a lot that today and then how that answer changes over the next couple years.

Benjamin Mann (01:09:15):
Yeah, maybe I'll try that. I'll put it into the deep research thing that we have and see what it comes out with.

Lenny Rachitsky (01:09:23):
Okay. I'm excited to see what you come up with. Ben, is there anything else you wanted to mention or leave listeners with maybe as a final nugget before we get to our very exciting lightning round?

Benjamin Mann (01:09:33):
Yeah, I guess my push would be these are wild times. If they don't seem wild to you, then you must be living under a rock but also get used to it because this is as normal as it's going to be. It's going to be much weirder very soon. And if you can sort of mentally prepare yourself for that, I think you'll be better off.

Lenny Rachitsky (01:09:59):
I need to make that the title of this episode. It's going to get much weirder very soon. I 100% believe that. Oh my God. I don't know what's in store. I love how you're at the center of it all. With that, we reached our very exciting lightning round. I've got five questions for you. Are you ready?

Benjamin Mann (01:10:14):
Yeah, let's do it.

Lenny Rachitsky (01:10:16):
What are two or three books that you find yourself recommending most to other people?

Benjamin Mann (01:10:20):
The first one I mentioned before, Replacing Guilt by Nate Soares. Love that one. The second one is Good Strategy Bad Strategy by Richard Rumelt. Just thinking about in a very clear way, how do you build product? It's one of the best strategy books I've read and strategy is a hard word to even think about in many ways. And then the last one is The Alignment Problem by Brian Christian. Just really thoughtfully goes through what is this problem that we care about that we're trying to solve here? What are the stakes in a version that's more updated and easier to read and digest than superintelligence?

Lenny Rachitsky (01:10:58):
I've got Good Strategy, Bad Strategy right behind me. I think I'm going to point to it. There it is.

Benjamin Mann (01:11:02):
Nice.

Lenny Rachitsky (01:11:03):
And I've had Richard Rumelt on the podcast in case anyone wants to hear from him directly. Next question, do you have a favorite recent movie or TV show you've really enjoyed?

Benjamin Mann (01:11:10):
Pantheon was really good based on Ken Liu or Ted Chiang's story. Ken Liu I think. Super good talks about what does it mean if we have uploaded intelligences and what are their moral and ethical exigencies. Ted Lasso, which is supposedly about soccer, but actually it's about human relationships and how people get along and just super heartwarming and funny. And then this isn't really a TV show, but Kurzgesagt is my favorite YouTube channel and goes through random science and social problems and is just super well done and super well-made. Love watching that.

Lenny Rachitsky (01:11:53):
Wow. Haven't heard of that as you were talking, I feel like Ted Lasso, I feel like that's what you need to put into constitutional AI, act like Ted Lasso.

Benjamin Mann (01:12:00):
Yes.

Lenny Rachitsky (01:12:00):
Kind. Smart-

Benjamin Mann (01:12:03):
Exactly.

Lenny Rachitsky (01:12:03):
... Hardworking. Oh my God. There we go. I think we've solved alignment problems right here. Get those writers on this, ASAP. Okay, two more questions. Do you have a favorite life motto that you often come back to in work or in life?

Benjamin Mann (01:12:15):
Well, a really dumb one is, have you tried asking Claude? And this is getting more and more common where recently I asked a coworker like, "Hey, who's working on X?" And they were like, "Let me Claude that for you." And then they sent me the link to the thing afterwards and I was like, "Oh yeah, thanks. That's great." But maybe more of a philosophical one I would say, everything is hard. Just to remind ourselves that things that feel like they're supposed to be easy, it's okay to not be easy and sometimes you just have to push through anyway.

Lenny Rachitsky (01:12:49):
And rest in motion while you're doing that.

Benjamin Mann (01:12:51):
Yeah.

Lenny Rachitsky (01:12:51):
Final question. I don't know if you want people to know this, but I was browsing through your Medium posts and you have a post called Five Tips to Poop like a Champion. I'd love it. Can you share one tip to poop like a champion if you remember your tips?

Benjamin Mann (01:13:06):
I of course do. It's actually my most popular Medium posts.

Lenny Rachitsky (01:13:12):
Okay, great. I can see that. It's a great title.

Benjamin Mann (01:13:15):
I think maybe my biggest tip would be use a bidet. It's amazing. It's life-changing. It's so good. Some people are kind of freaked out by it. It's the standard in countries like Japan and I think it's just more civilized. And in 10 or 20 years people would be like, how could you not use that?

Lenny Rachitsky (01:13:37):
And a bidet could be like a Japanese toilet. That's along the same lines.

Benjamin Mann (01:13:40):
Yeah.

Lenny Rachitsky (01:13:40):
Right. Okay. I love where we went with this. Ben, this was incredible. Thank you so much for doing this. Thank you so much for sharing so much real talk. Two final questions. Where can folks find you online if they want to reach out, maybe go work at Anthropic and how can listeners be useful to you?

Benjamin Mann (01:13:52):
You can find me online at benjmann.net and on our website, we have a great careers page that we're working on making a little bit easier to access and figure out, but definitely point Claude at it and it can help you figure out what could be interesting for you. And how can listeners be useful to me? I think safety pill yourself, that's the number one thing and spread it to your network. I think. Like I said, there are very few people working on this and it's so important. Yeah, think hard about it and try to look at it.

Lenny Rachitsky (01:14:28):
Thanks for spreading the gospel, Ben, thank you so much for being here.

Benjamin Mann (01:14:31):
Thanks so much, Lenny.

Lenny Rachitsky (01:14:32):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

