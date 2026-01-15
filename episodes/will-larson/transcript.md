---
guest: Will Larson
title: The engineering mindset | Will Larson (Carta, Stripe, Uber, Calm, Digg)
youtube_url: https://www.youtube.com/watch?v=Z9ftpRhRiJE
video_id: Z9ftpRhRiJE
description: 'Will Larson is the chief technology officer at Carta. Prior to joining
  Carta, he was the CTO at Calm and held engineering leadership roles at Stripe, Uber,
  and Digg. He is the author of two...

  '
duration_seconds: 4613.0
duration: '1:16:53'
view_count: 36504
channel: Lenny's Podcast
keywords:
- growth
- retention
- metrics
- roadmap
- funnel
- conversion
- monetization
- revenue
- hiring
- culture
- leadership
- management
- strategy
- competition
- market
---

# The engineering mindset | Will Larson (Carta, Stripe, Uber, Calm, Digg)

## Transcript

Will Larson (00:00:00):
I think that we often treat engineers a little bit like children instead of giving them the responsibilities and ability to actually thrive as adults. And so like, "Oh, the engineers won't want to do that work." Well, that's actually not good for the engineers to be sheltered from what is important. And so actually one of the, I think, highlights is that I think we're coming back this moment where we can actually treat engineers like our peers and put them into really senior leadership roles and not have this kind of baseline assumption of like, "Oh, we have to coddle them or hide them from the real problems." And this is how they're going to get the opportunity to grow as well.

Lenny (00:00:35):
Today, my guest is Will Larson, one of the most requested guests I've had on this podcast. Will is currently CTO at Carta. He's been a software engineering leader at Stripe, Uber, and Calm. He's the author of two essential books for all engineers, An Elegant Puzzle and Staff Engineer, and he's releasing his newest book The Engineering Executive's Primer in February of next year. He also publishes regularly on his blog at lethain.com, which is a must read for every engineer and eng leader.

(00:01:05):
In our conversation, Will shares advice on developing your engineering strategy and strategy in general, how to improve the relationship between an eng manager and a PM, how he finds time to write, while also working an intense full-time job, how he recommends approaching measuring engineering productivity, how to develop your company values, an amazing story about his time at Digg and so much more. Will is such a gem of a human and leader and I'm excited to bring you this episode. With that, I bring you Will Larson after a short word from our sponsor.

(00:01:39):
Today's episode is brought to you by DX, a platform for measuring and improving developer productivity. DX is designed by the researchers behind frameworks such as Dora, Space and DevEx. If you've tried measuring developer productivity, you know that there are a lot of basic metrics out there and a lot of ways to do this wrong. And getting that full view of productivity is still really hard. DX tackles this problem by combining qualitative and quantitative insights, giving you full clarity into how your developers are doing.

(00:02:07):
DX is used by both startups and Fortune 500 companies, including companies like Twilio, Amplitude, eBay, Brex, Toast, Pfizer, and Proctor and Gamble. To learn more about DX and get a demo of their product, visit their website at getdx.com/lenny. That's getdx.com/lenny.

(00:02:28):
Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file. And building a spreadsheet importer becomes a never ending sync for your engineering and support resources. You keep adding features to your spreadsheet importer, but customers keep running into issues. Six months later, you're fixing it. Another date conversion edge-case bug. Most tools aren't built for handling messy data, but OneSchema is. Companies like Scale AI and Pave are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences.

(00:03:02):
From embeddable CSV import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like error online 53 and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product. For listeners of this podcast, OneSchema is offering a $1,000 discount. Learn more at oneschema.co/lenny.

(00:03:36):
Will, thank you so much for being here and welcome to the podcast.

Will Larson (00:03:40):
Thank you so much. Super, super excited to be here.

Lenny (00:03:42):
So many people have suggested that I bring you on this podcast. You have a lot of fans out there and I am excited to be digging into engineering topics, which we don't do enough of on this podcast. So thank you for making time for this.

Will Larson (00:03:54):
No, thanks. I hope to be a good early engineering guest before you pivot entirely to engineering at some point in the future.

Lenny (00:04:04):
Wow, I love that. How cool would that be? I was an engineer actually when I started my career. How interesting would that be if we come full circle? Anyway, I thought it'd be fun to start with just what is changing in engineering? It feels like there's been a lot that has changed over the past few years, especially from kind of the ZIRP zero interest rate era to today's market, which is very different. What have you seen most change from an engineer's perspective and then just also what are you telling eng leaders about how to handle all this change?

Will Larson (00:04:32):
I think it's a pretty strange time in the market. So I think that I started working and right before the 2008 kind of crash. And so the first two years there were not so good. When I joined Yahoo, there was a layoff basically every four months. There was a layoff of some sort. It's pretty chaotic. But then we got into the last decade and it was just smooth. So numbers went up, revenue went up, headcount went up and people started learning how to build really large teams.

(00:05:02):
People started learning how to hire a lot. When I was at Uber, some days I would do six interviews back to back. I would just be in a conference room and at some point you can't even remember who you're talking to because you talk to so many people, one after another after another. You just have some scrambled notes you're trying to decode afterwards.

(00:05:20):
Pretty different now. A lot of engineering managers are spending half their time or more hiring 18 months ago and now they're doing two interviews a month or less. Maybe zero interviews a month. So there's a real shift in just the amount of time people are putting into hiring. Instead, all these different competencies that have become more critical or a really great engineering director might've just been spending their time hiring really well and that could be a top performer and now that person can't actually demonstrate what they're great at.

(00:05:51):
So that person might be perceived as a low performer if they're not also figuring out how to lead the team, getting deeper into the details and also sometimes getting into the figuring out what is the right allocation, what is the right sizing of the engineering teams, this is stuff that we weren't talking about much or maybe if you really pissed off the CEO, maybe an infrastructure you just grew a little bit slower next year, but different ballgame at this point where teams are actually disappearing, teams are getting cut down, teams are getting consolidated. And that's just something that we've avoided for that ZIRP era that now we become a core part of a lot of the job.

Lenny (00:06:27):
It feels like also engineers... They used to have a lot of leverage over companies, inside companies. I imagine that's also changing in a big way.

Will Larson (00:06:37):
I think that's true. I think this actually has been bad for engineers in some way. One of my hobby horses is that I think that we often treat engineers a little bit like children instead of giving them the responsibilities and ability to actually thrive as adults. And so like, "Oh, the engineers won't want to do that work."

(00:06:53):
Well, that's actually not good for the engineers to be sheltered from what is important. Actually one of the, I think ,highlights is that I think we're coming back this moment where we can actually treat engineers like our peers and put them into really senior leadership roles and not have this baseline assumption of like, "Oh, we have to coddle them or hide them from the real problems." And this is how they're going to get the opportunity to grow as well. That's a highlight for me and the shift recently.

Lenny (00:07:18):
I have definitely worked with that and experienced that where you don't want to piss off engineers. And so are you saying that because that's changing, leaders maybe don't have to worry as much about upsetting engineers plus you just generally think we shouldn't treat engineers that way?

Will Larson (00:07:33):
Yeah, I think a little bit of both, but I think there's been, in this previous era, where hiring and retention were one of the biggest ways you evaluated middle management. Losing team members was huge, huge issue. And so you started to coddle a little bit, which is actually bad, again, bad for the engineers, bad for the teams, bad for everyone, bad for efficiency of the organization. But now something that I love is we get to give engineers real hard problems and we get to actually hold them accountable. And that means we can put them in senior roles.

(00:08:07):
One of the things that I've been pushing on, I wrote my last book, Staff Engineer about what is the career path for senior engineers. One of the challenges is if we aren't comfortable holding engineers accountable because we just want to retain all the engineers, then we can't put them in senior roles. And so I think we're actually seeing a bit of a shift where we can actually hold them accountable, which means we can put them in senior roles, which means the engineers can actually get what they've been trying to get the entire time, but we haven't been able to because we've been coddling them a little bit too much.

Lenny (00:08:33):
Okay. So there's a few directions I want to go and I'm just going to poke around and see where we go. The first is you're a big advocate of systems thinking. We were chatting about this before. I think a lot of people have heard this term systems thinking and there's books about it. It's sounds great. I want to be a systems thinker. What does that actually mean? How do you find you apply it in your work? How do people get better at this way of thinking?

Will Larson (00:08:57):
A lot of the least successful but smartest people I've worked with were really strong systems thinking advocates. And so I do want to say every kind of framework has a lot of downsides. There's no framework that people can apply consistently, universally, and get good results. And so briefly on this one, what I see is often people will find a spot where their system and reality are in conflict and they'll be like, "Reality is wrong." And so what's a concrete example?

(00:09:28):
At Stripe, we worked on incident management. And so Stripe pretty important company where our API is available. If the API is down, you lose money and if you lose a lot of money, you leave Stripe because you're pretty upset about that. The number one thing businesses need to do is to collect money successfully for the service that they're selling, right? Stripe is super important.

(00:09:49):
And so we did a lot of analysis on incidents trying to understand why things weren't working, what we could do better, but we got so caught up in the analysis that we lost track of whether we're actually improving things. And it took us a while to figure that out because we were so stuck in the systems thinking model and it's not like, "Oh, the team was wrong." It's like, "I was wrong." I was caught up in that model myself, to realize like, "Hey, we weren't actually prioritizing improvements, we were just prioritizing measurement." And you can't keep measuring. There's measure twice, cut once. Sure, but you don't measure infinite times and never get to cut.

(00:10:25):
And you do have to cut at some point to actually make impact. But we just got caught a little bit there. I think a lot of people who get too far in systems thinking make the same mistake where they think reality is wrong and reality is never wrong. Reality is always right. Your model is always wrong if it's in conflict with reality. But that conflict, that gap is really interesting and that's where you can learn.

(00:10:49):
And so I had this model. It's really clean. It represents your hiring pipeline that moving through different steps. It represents your incidents and how you remediate incidents. It can model almost anything pretty quickly when you get good at it. And then understanding how reality is in conflict with that, you start to understand where your mental model is wrong and then you can go educate yourself and improve the model and just keep doing that.

(00:11:12):
At some point the model is close enough and you can stop doing that and go actually do the work. So that the biggest thing I tell people is this is a great way to learn, but you also have to do things. You can't just learn. That's not our entire job.

Lenny (00:11:25):
To make it a little more concrete, how would you best describe this idea of systems thinking? What's a good way to just like, "Okay. I get what you're talking about?"

Will Larson (00:11:32):
This is probably a better place to start versus a rambling anecdote about using it.

Lenny (00:11:38):
We can go backwards. It'll be great.

Will Larson (00:11:41):
Systems thinking is basically you try to think about stocks and flows. So stocks are things that accumulate and flows are kind of the movement from a stock to another thing. So what's a simple example of a stock? A stock could be the number of fish in a lake. A stock could be the number of people fishing in a lake. And so a flow between those two could be the number of fish in a lake will decrease at some rate based on the number of people fishing in that lake.

(00:12:08):
So if there's a ton of fishers, the stock of fish will go down faster. There's only a couple of fish, IT will go down slower. But also then there's these flows which kind of dictate that where if we've got much more efficient fishermen, the flow of fish out might go down, but also the fish do reproduce. So then there's another flow going back. So based on the current number of fish and the reproduction rate, the current number of fishers and their fishing rate, you start to see how these can evolve over time. And a lot of this.

(00:12:38):
So first always recommend Thinking In Systems by Donella Meadows. Really phenomenal book. And a lot of her work is also kind of referencing the work in Silent Spring by Rachel Carson, which talks about how small amount of carcinogens or something low in the ecosystem or the food chain rather as they get consumed by predators further and further up get concentrated. And that's a kind of a classic systems thinking problem to think about where you wouldn't think a small amount of carcinogens and a small fish actually matter. But as they go up the food chain, they start to concentrate it and an unexpected change can happen.

Lenny (00:13:14):
So then going back to your example of the hiring pipeline, let's come back to that to help connect this definition, which I've never heard, which is awesome, very clear to how you actually implemented say in hiring.

Will Larson (00:13:23):
The first thing to do is to get a model out there of any sort. And so you think about your stocks. And so in a hiring pipeline you might have potential candidates and this could be basically infinite, and then you have a couple of inflows. So you could have sourced, you could have outreach, you could have referrals, and then you have the candidates and those... How many people get sourced. There's probably a function of number of sources you have dedicated to a role. So you'd have another stock of how many sources you have and then that would impact the rate going from potential candidates to actual candidates you've sourced.

(00:13:59):
And then from candidates that you have in that box, you'd have a conversion rate for people who pass the first recruiter screen and that would move into step two of your process. And then from step two you have maybe a hiring manager screen and that would be another conversion rate. So you can see over time how the candidates of the infinite potential candidates like wandering around LinkedIn, posting about their deep thoughts, convert into actual people, your first, your second, your third.

(00:14:26):
But then as you get deeper into it, you start to actually see interesting things. And so for a lot of candidate or a lot of pipelines, the biggest issue is hiring managers don't want to extend any offers because the hiring managers can't get to confidence on any candidate. And you'll see in this pipeline, you'll see a ton of candidates getting to offer stage, but almost none of them converting from a potential offer to actually offer. And then you can say, "Hey, here's the problem. You need to go work with the recruiter and the hiring managers on getting conviction about who they should hire.

(00:14:56):
Classic problem with early managers, right? Here's a second problem. Manager wants to extend a ton of offers. They do extend them and none of them actually accept. And so that focuses you on the second problem. But there's a third potential world where actually you're just not getting enough candidates in. You're actually doing a great job of making decisions, great job of closing candidates. There's just not enough candidates coming in. And so by looking at this and you can build this model, then you can go to your applicant tracking system, a greenhouse or whatever and pull the historicals and you can just see how the historicals work versus how you'd expect it to work.

(00:15:32):
You can see the drop-offs and this helps you figure out where should you go try to fix things first. I think we've all worked in companies where you roll out big changes with no data behind them because like, "Oh, it feels like we're not hard enough in how we evaluate candidates or something." You go change a bunch of stuff. But often the real problem might be that the hiring managers making offer extensions to people who never passed the loop anyway. It's just the managers are issuing too many offers because they're panicking. And man, less true now, but a decade... Or not a decade, two years ago, hiring managers panicking to get offers out, that was a real thing that happened a lot. And this just helps you take a complex kind of abstract problem and turn it into something you can actually work in a systematic way.

Lenny (00:16:17):
I feel like product managers will either naturally do it things this way already because a lot of them think in funnels. And it's interesting to hear this version of it of this idea of just following the stock through the flow of the different steps. Awesome. Another thing that I know that you are very passionate about and spend a lot of time thinking about is engineering strategy. I think you have this kind of feeling like engineers don't think enough about the end strategy. Every other function has a strategy and engineers often don't. Talk about what you find there and what your advice is around that.

Will Larson (00:16:52):
First, I start to question whether any function has a strategy at most companies. My general experience is that there's very rarely a written strategy for any company. Sometimes it's a value statement. It's like we build the highest quality products and you're like, "Good. Okay. What do I do with that?" You're like, "Build a high quality product." You're like, "Okay. I don't don't know what that means."

(00:17:15):
Engineering often has this problem where I think people will make comments in their culture amp or their quarterly surveys or whatever. It's like, "Hey, the strategy is not clear or where's the engineering strategy?" And the biggest thing I tell people when they complain and then engineers complain about the product strategy. The PMs don't have any strategy or the business has no strategy. And the reality is product eng and business always have a strategy. It's just often not written down.

(00:17:45):
And so the first thing I want to do is I push people not to get caught up on the fact that there's no template out there, which is product strategy that someone has forked and filled in. It doesn't mean you don't have a strategy. You do have a strategy. It's maybe a little bit hard to articulate and maybe it's applied inconsistently across different layers of the product reporting chain because it's not written down. But it's never true that there's no product strategy. There's always a product strategy. Sometimes it's bad, but there's always one. And true for engineering as well. There's always an engineering strategy. Just sometimes it's bad.

(00:18:21):
The first rule of strategy is that if you write it down, then you can improve it. If it's not written down, it's hard to say if this PM is just not a good PM or if they're trying to apply the strategy that they've misunderstood or if they actually are correctly applying the strategy from the head of product that's just not appropriate to the problems they're working on, how do you debug any of that?

(00:18:43):
If you have a written document, even if it's not a super compelling strategy, at least you can start debugging. It's like, "Hey, the head of product should improve the clarity of this document. Hey, this DM actually isn't applying it correctly. Hey, the strategy actually isn't appropriate for this one business unit where it makes sense for the others."

(00:19:02):
So that's the first thing I think about. But the second big theme on strategy I think about is that often good strategy is so boring. It's hard to talk about. For example, on the engineering side of thing, a common strategy that's really good but very boring is we only use the tools we have today. So a lot of times you'll get engineers that want to introduce new programming languages, new databases, new cloud providers. And a really good strategy for almost all companies is like we just use the standard kit we already have today.

(00:19:39):
And at Carta, when I joined one of the engineers, Eric Vogel wrote the standard kit and that is our strategy of the tools we use. And you know what? Some people are really frustrated by that and I feel for them. It feels like they're losing control, but the power of these boring strategies is that it focuses people's energy on the problems that we value as a company. And so it is painful coming into alignment if you're kind of slightly misaligned over time, but boring strategies that tell you what actually matters and aligns you with what the company actually caress about are really good for you even if they're a little bit annoying at a time. And I can expand on this idea a lot, but I won't ramble indefinitely on it.

Lenny (00:20:21):
Well, maybe what might be helpful is what are some other examples of engineering strategies that you've seen just to give people even more just like, "Oh yeah, maybe this should be part of our strategy."

Will Larson (00:20:31):
So first, what is a definition of strategy? And the best one I've ever seen is from Richard Rumelt. He wrote Good Strategy, Bad Strategy.

Lenny (00:20:40):
He's coming on the podcast.

Will Larson (00:20:42):
Amazing. He also wrote, The Crux I think came out this year sometime, which I also read. I think both great and just a phenomenal thinker who has so much depth. I think one of the challenges of writing about strategy is you're like, I've seen two things and I write the book, but I think the thing that's impressive about Richard Rumelt is he's seen so many different scenarios that he's able to really operate from both the particular but also the general and dataset in a really interesting way. Another book with similar characteristics is How Big Things Get Done by... I forget the authors, but really amazing dataset of how mega projects kind of succeed and fail.

(00:21:21):
But anyway, Richard Rumelt, definition of strategy is basically three components. There's a diagnosis. What is the current status quo? What are the things that are real today? There are guiding policies which are basically based on the diagnoses, how do you want to address them? And there's actions. And actions are how are we going to implement these guiding policies. He talks a lot about actions because concerned about this idea of inert strategy where you have like, "We're going to deprecate our old product features we don't use, but no one deprecates any of them."

(00:21:52):
So he's really concerned about this non implementation kind of useless strategy that doesn't do anything. On engineering, I'm a little bit less worried about that. I think strategy is more interesting on engineering in terms of clarifying how we make future decisions. And so what are a few examples of that? At Uber, we only used our own data centers. We didn't use the cloud. And this has changed since the era I was there, but in the 2014 era, no cloud, and we had a strict no cloud policy. And this was annoying because we had to indent everything ourselves or run copies of everything ourselves.

(00:22:28):
But it also meant that we were able to spin up in China in literally three months and some surreal stories from that. We couldn't fit our racks into the data centers, so they had to take the roof off the data center and lift the racks in with the crane.

Lenny (00:22:43):
Holy shit.

Will Larson (00:22:43):
Just tons of stories and all this had done in three months and truly phenomenal. And Uber wasn't in China for very long, so in some ways you're like, we did all that just a leave? But they left with a nice stake of Didi Kuaidi and not a bad outcome overall. But I think that strategy, we run everything in data centers. We don't use the cloud, meant we were able to move in and out of different geopolitical constraints and companies that relied on cloud presence simply can't. There are fully constrained by where AWS or Google Cloud or Azure have built out. So that's one good example.

(00:23:21):
Another good example at Stripe was this idea of we run a Ruby monolith and that's what we did and that's evolved a bit since then. There's more Java and the Stripe of 2023 than there was in the stripe of 2016 or the 2012 or whatnot. But that policy really focused the engineers on building innovative features for our users rather than building different tooling to support different programming languages. And so in both cases, both the Uber policy around running our own data centers and the Stripe policy around Ruby monoliths, a lot of engineers hated these.

(00:24:02):
But the goal of good strategy is not to appease everyone. The goal of good strategy is to dictate how we invest the limited capacities we have or the limited capabilities we have into the problems we care about. And I think both of them were really effective towards that end.

Lenny (00:24:17):
A common theme across all these examples is essentially constraint, deciding we will constrain our options to move faster and focus on the things that really matter.

Will Larson (00:24:28):
In solving the constraints is to me, I think the most interesting thing that strategy really does, and I think when we talk about bad strategy usually is because the diagnosis is bad and it's usually because people are exerting what they want to be true on constraints where it's like, "Hey, we can do all of these projects at once." And often that's just not true, but it's hard to convince people that when they're the CEO or they are really committed to believing it, but almost all bad strategies basically come down from a willful disbelief of what an accurate diagnosis is, which means then your guiding policies are kind of incoherent to begin with.

Lenny (00:25:08):
Awesome. I'm excited for that episode of Richard where we're going to go real deep into strategy, but maybe just as a lasting topic around there, if someone listening wanted to get better at say end strategy specifically or a strategy in general, is there anything you recommend they do? Is it read these books? Is there anything else?

Will Larson (00:25:26):
If people want to get good at strategy, there's a lot of different types of strategy, but here are some things I'd really recommend. First, I think the Richard Rumelt book, I think Good Strategy, Bad Strategy is probably the right starting point. I think The Crux also quite good, but maybe I would read that one second. Great overview of how to think about strategy. Also Thinking in Systems, I mentioned that before related to systems thinking, a big part of strategy is being able to model the reality so we can improve your diagnosis.

(00:25:56):
So I think that one is really quite good as well. If you get into the engineering side of things, there's a lot of interesting books here. There's Technology Strategy Patterns by Evan Hewitt. There's The Value Flywheel effect by Anderson, McCann and O'Reilly. The Phoenix Project by Kim, Behr, Spafford, which is a modern rewrite of The Goal by Goldratt. But I think there's still the missing canonical book is kind of missing on this one. So I took a stab at strategy and my upcoming book, which is coming out the Engineering Executives Primer coming out early next year.

(00:26:33):
Also, took a stab at it. In staff engineer my previous book, but I still think there's a missing book here. So I am dreaming of writing an engineering strategy book for my next project, although we'll see if that actually comes together.

Lenny (00:26:48):
Well, let's actually follow that thread of writing something I was definitely hoping to chat about. You write a lot. You've written two, three, four-ish. You're writing a new book. How many books you've published? Two books and there's a third one coming up.

Will Larson (00:27:00):
So I have two books. First one with Stripe Press, the second one, self-published and the third one with the Riley coming out in two months effectively.

Lenny (00:27:08):
Okay. And then also many, many blog posts for many, many years. I asked a few people what to ask you, and this came up a lot, Gergely Orosz and Alex Xu from ‎ByteByteGo both asked just this question of just, "How do you make time to write as much as you do?" And then I also, I'll ask this too and just answer it either first or second, just what impact has writing had on your career? Why do you keep doing it?

Will Larson (00:27:37):
I feel really strongly that you can write a lot more if you write what you want to write. And so this is one of the reasons I don't write for financial gain and I don't write very much on a schedule, so I've done a few pieces for magazines, et cetera, but I find that actually really draining to be you have a topic, you have to agree on the topic. If a topic starts missing what you want to write about, you can't fix it a lot of the time and you're also on this deadline. You're like, "Ah, I'm screwing up. I need to ship this. It needs to be done tomorrow."

(00:28:12):
I just find that really draining. Conversely, when I own the schedule, when I get to write about, "Hey, I'm writing out something." So I started writing this infrastructure engineering book a couple of years ago. It just wasn't there. I just couldn't get it to come together and so I just stopped. I'm not writing it anymore. Maybe I'll come back to it at some point, but probably not.

(00:28:34):
To me, the biggest strength of writing what you want is you get to write where there's energy and you don't have to write where there's no energy, which takes you really, really negative. And this also ties into how I write books, which is that I basically write the entire thing before I start working with a publisher. And if you are, I think diligent and good at anticipating what their concerns are going to be, you can mostly reuse the content that you're trying to write. This is also easier in the sorts of books I write.

(00:29:05):
I think harder to do in a really technical introduction to MySQL or something, you can't just resequence those chapters and pretend it's going to work. Those chapters build in a different way than the sort of business book that I write does. Writing the stuff that's energizing and just giving up on the stuff that's not energizing, that's how I write a lot and how I've been writing for 16 some years. And the way I keep doing it is just by writing what's energizing and what I'm thinking about now.

(00:29:38):
I don't write what I'm not thinking about and I don't write for any audience, I just write what is interesting to me. And that means some people don't like it and that's great. That's totally fine. It's not really for them, it's for people who want to follow the ride and that's where I focus.

Lenny (00:29:57):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate your growth. Thousands of fast-growing companies like Gusto, Qom, Quora, and Modern Treasury trust Vanta to help build scale, manage and demonstrate their security and compliance programs and get ready for audits in weeks, not months. By offering the most in-demand, security and privacy frameworks such as SOC 2, ISO 27001, GDPR, HIPAA and many more, Vanta helps companies obtain the reports they need to accelerate growth, build efficient compliance processes, mitigate risks to their businesses, and build trust with external stakeholders.

(00:30:34):
Over 5,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2 and these other frameworks. For a limited time Lenny's podcast listeners get $1,000 off of Vanta. Go to vanta.com/lenny. That's vanta.com/lenny to learn more and to claim your discounts. Get started today.

(00:30:55):
Okay. There's a lot more I want to dig into here. How many posts have you written do you think over the 16 years?

Will Larson (00:31:00):
I would guess about a thousand. That would roughly be my assumption. I think there are a few years where I wrote hundreds of posts, and so if you do that like three years, it's not that hard to get to a thousand from there.

Lenny (00:31:16):
That's incredible, especially because you've had intense jobs for all of those years or most of those years. Very high pressure, fast growing hypergrowth companies. Somehow you find time to work. So first, let me just double click slash co-sign your advice here around paying attention to what gives you energy and working on things that you're actually curious about. This is exactly the advice I give to people. A lot of people start this full-time writer, creator life, and they're like, "What do people want? What do people want me to write about? What's popular? What's going to inspire go viral?"

(00:31:48):
And that's easy to do a couple times, but then you end up creating this job for yourself that you don't want. You don't want to be spending all your days writing about AI if you're not that excited by AI or whatever's hot these days. What I find is important is almost like 80, 90% of what you write has to be stuff you're excited about. And then maybe there's a bit of, "Here's what I know people really want. Here's what I know is going to do really well." Because otherwise you just burn out. You create a job for yourself that you don't want. Why would you do that?

Will Larson (00:32:13):
Yeah. I just a hundred percent agree with that. I think the other thing is that everyone converges on the same thing that they think people want. So it's crypto two years ago. It's like AI right now or it's counter AI. AI is going to ruin the world. It's hard to say something very novel because, one, everyone is trying to say something about it. Two, it's almost certainly not what you're that knowledgeable about where if you just stick in your lane, I think the biggest risk to writers is quitting.

(00:32:43):
A little bit like the 40-year career idea. The biggest risk to content creation of any sort is quitting soon because you get burned out. The biggest risk is not that you grow too slow initially. There's always this sense that you've missed the wave. It's too late to join Substack. The top writers are already there. You'll never be a top writer. It's too late to podcast. There's too many podcasts. You'll never make it. It's too late to join Medium. You'll never make it. There's too many Medium writers.

(00:33:11):
But it is just not true. If you just keep writing good stuff, you'll build an audience over time and you can take that audience from platform to platform. What really matters is finding something you can actually keep doing for the next decade. That's way harder than doing it for one year.

Lenny (00:33:25):
We have the same exact advice on this. This is exactly the things I tell everyone. When I joined Substack, I thought it was too late. I was like, "Man, it's over." And when I started this podcast like, "Oh man, there's a billion podcasts. How is it ever going to work?" So I so agree, and I also so agree on the fact that this whole thing is such a... It's a long game. There's a lot of people. I always say it's easy to start a newsletter, hard to keep it up. Nobody actually keeps it up because people are going to come and go. The thing that really separates success from failure is just people that can keep at it. There's not an end game to this. It's an infinite game and it's about being able to sustain that over the long term.

Will Larson (00:34:04):
You're not competing with other content creators. If you think of it as an infinite game, you're all working together. You can all help each other grow. There's no maximum number of product writers or thinkers who can be doing something. You're not less successful because [inaudible 00:34:22] exists or something like that. There's no competition there. It's like a false, false dichotomy.

Lenny (00:34:27):
Yeah. I totally agree with that. Unless there's so many and then all of a sudden what happens is the bar just gets higher, which is good because then people get better stuff and that's fine. That's happening anyway. Just the bar continues to increase because there's more and more content out there. And to me that's the ultimate thing you got to get right is just the bar. You just got to be at a high bar for anyone to care about anything you're writing about. And to your point, to do that well, you have to actually be excited about writing about it and have background and have something to contribute.

(00:34:59):
I'm just ranting here, but the way I think about this is you need to add something new to the conversation for anyone to pay attention because there's so much fluffy, superficial stuff. And to get anyone to care is you need to say something new that no one's heard before or share new information they haven't seen anywhere else.

Will Larson (00:35:15):
I totally agree. I could keep ranting about this for the entire time. I don't want to derail on this, but I totally agree.

Lenny (00:35:23):
We'll control ourselves. So then getting very tactical, I think this is what a lot of people are always wondering, how do you make time? What's your workflow? How do you make time for writing so that you keep at it with knowing you have an intense full-time job?

Will Larson (00:35:34):
I used to do things differently before I had a kid, so I have a three and a half year old and just timing your life just really shifts a lot once you have kids. But the biggest thing that I found is finding things to write about that also directly relate to what I'm working on. And this is where I can do something that helps me at work and helps me write at the same time because I think it's incredibly hard to find time to write about stuff that has nothing to do with your work.

(00:36:05):
And this distracts you from your work because these... Particularly if you're in a senior role, these can be pretty demanding jobs, but they're not demanding because you're responding to an urgent DM on Slack every five or six minutes. They're demanding because you need to make some really difficult decisions really well. And I think writing about related topics is a great way to refine your thinking and improve your performance. It's not like a conflict or you do one.

(00:36:34):
You either write or you do your job well. I think you can find a way to align. And so a lot of podcast folks do interviews with folks who are related to what they're thinking about at work, and that's a great way for them to learn, build their network, to refine their thinking, to test their thinking against experts in the field. It's not like in conflict with the work, it's in alignment. So that's one piece. But yeah, I've played around with my schedule a lot.

(00:36:58):
Before I had a kid, often Saturdays would be the writing day and so morning and early afternoon would just be writing. I can't do that anymore, so now I mostly write at night, which is tricky from an energy management perspective. But the biggest thing I would say is just if you're actually excited about something, you will find time and energy for it. If you're not excited about it and it's 9:00 PM, you're just going to get asleep. And so I really think that this is where you have to schedule a little bit deliberately, but the first thing we talked about around energy management, they really come together. When your schedule gets tight, if you're not energized, you just won't get it done. And why would you? It just doesn't make sense.

Lenny (00:37:41):
Just to close out this thread for someone that wants to do more writing knows that it's going to be valuable, but just hasn't any one tip that you would leave them with to get on this train?

Will Larson (00:37:51):
It depends why people want to write. I tell people, if you just want to write something that is going to help advance your career, you should really focus on writing two or three really good things and spend a ton of time drafting, revising, getting feedback. You just focus on making one great artifact or two or three great artifacts. You don't need to create a long-running blog where you publish every week. There's really no need to do that if your goal is just to create some artifacts that show you're a deep thinker, that help position you in the industry.

(00:38:21):
Don't start a newsletter if you just want to advance yourself in the industry a little bit. Just write two or three really good things. So that's the first thing I'd say. But if your goal is to write a lot consistently over time, my biggest advice would be just publish. And so there's a lot of people out there with stuff that hundreds of drafts and they've not published anything. And my thing is I publish almost everything I write. If there's something that I'm not going to publish, I don't start writing it because I have a quick check in my head like is this something I can write and publish?

(00:38:56):
And if my answer was like, "No, I just don't even start." And my accuracy has gotten higher over time as I've written more, but I published pretty much everything I write. That's why some of it is not that good. And that's okay. Again, I want to write. I want to get these ideas out. I want to show what I'm focused on and my evolution as a thinker trying to learn how to operate in these different roles in these different companies. I'm not writing trying to create a polished perfect thing, and also I'm not writing to maximize a reader's experience of reading it.

(00:39:27):
Some people don't like that, and I think that's a totally reasonable thing not to, but I think what I can bring you is my experience as an operator who's actively learning and thinking through. I think that's really valuable to other operators in the industry. In terms of giving you the perfect writing, I try to do that, closer to that. I don't know if I ever hit perfect writing, but that's where my books are. The books are taking a collection of thoughts over a couple of years, cleaning them up a little bit, packaging them. They're way higher quality than my typical writing.

(00:39:56):
But yeah, I would just publish a lot. Don't worry about the quality. Sometimes people will send you silly feedback and I just don't respond to that stuff anymore. You never know why people send you something like that. I think trying to debug people you don't know is a bad use of time. It's just kind of like, "Thank you. Move on to the next. Don't even spend time worrying about it."

Lenny (00:40:19):
I like that term debug people. I think people way overestimate how much anyone cares about what you put out. Most people are going to look at it for three seconds and be like, "Eh." That's the worst case scenario basically is just like, "I don't care about this." Not like, "Oh, Will is such a fool." What a dumb thing to say. Right? No one has time for that.

Will Larson (00:40:38):
And if they do, that's a them problem, right? The internet is a big place with a lot of people and there are people who are going to be having a really bad day when they encounter something you do and they're going to channel that anger at you or that frustration at you, but that's not about you. That's just like you happen to be there when they engage with it. You don't have to take that on. That's not your situation. It's okay.

Lenny (00:41:03):
Also, when you're just starting out, that's going to be the least stressful time to write because nobody knows it or sees it, so that's when it's like "Take all the crazy... Just do stuff." It only gets more stressful as you build an audience over time.

Will Larson (00:41:15):
Yeah, absolutely. Absolutely true.

Lenny (00:41:18):
Okay. Shifting topics. There's a lot of product managers that listen to this. Something PMs often wonder is how to have better relationships with their engineers, their eng managers. What advice could you give to product managers to build more productive happy relationships with their engineers and eng managers?

Will Larson (00:41:37):
So the core problem, and most of the EM PM peers that I've worked on... There's two core problems. So one, sometimes the incentives are misaligned and that's hard to navigate, but if you can just be honest with each other and understand the incentives, sometimes you can find a compromise, but sometimes the EMs and PMs will be misaligned because just their incentives are so far apart that there's no way to get to the bottom of it. And so this might be timeline related or saying yes to sales related. Or the engineer is like, "Hey, we definitely can't say yes to that." And the PMs are like, "Actually, we're going to say yes to it because really important for me getting promoted," or something like that.

(00:42:19):
Is it ever this simple? It's really never that simple. People create simplistic narratives to find villains that they work with. There are no villains in the workplace. They're just people with complex incentives that are doing complex things. But sometimes I talk to EMs who think, "Oh, the product manager is just saying yes because they want to get promoted because the salesperson will review their promotion or something."

(00:42:40):
The reality is never as simple. The reality is the business needs to sell stuff to remain functioning. You can't just say no and have the business succeed. That doesn't work either. So one, understanding the incentives. The other piece though, and I think this is the more common case or just that the EM or the PM just don't understand the other person's needs and they start arguing before understanding. So my biggest advice to both the EMs and the PMs, is before you try to solve the conflict, it's like pushing to ship this feature, pushing to change the approach. Just make sure you actually understand what they care about.

(00:43:17):
There is this idea that you have to make trade-offs and that there are tons of hard trade-offs to be made in the field, but my experience is if you really deeply understand what everyone wants, there's usually a compromised solution that gives everyone exactly what they want. That doesn't take more time. You just have to be willing to dig deeper into it and understand the true needs for each party, which is often not what they're saying by the way, which is part of the confusion.

Lenny (00:43:45):
On the incentives piece, is there anything you've seen work to fix that problem? Because if PM performance reviews are based on impact engineering, performance reviews are based on interesting projects or uptime, do you just work to change those ladder definitions? What actually can help that situation?

Will Larson (00:44:05):
So my biggest thing has been trying to force this idea that EM/PM pairs are peers and they generally have the same performance rating. And there's exceptions here. It could be the EM is clearly not performing and then it's not the PM's fault if the EM is can't show up to work. The team doesn't respect them. Sometimes there's clear non-performance, but generally hard situations are not situations where one person is obviously terrible. Those are easy to diagnose, those are the easy ones. But in cases where there's two folks who seem to be pretty good, but just the overall execution is not working out, I think this idea that same perf rating for both drives a level of one pain, but the right perspective.

(00:44:56):
Also, something that I think Carta has experimented a little bit with over time. Henry, our CEO has a blog post about trifectas in doing that, but not just for EM and for PM, but also for that business leadership as well where you all get graded the same score based on your ability to evaluate and solve for the entire set of constraints, not just your functional constraints.

Lenny (00:45:20):
Wow. That's so interesting. So your recommendation, something you're doing, it sounds like is the engineer manager and the PM get the same performance review rating? And so they're discussed in the same meeting.

Will Larson (00:45:33):
Our chief product officer, Vrushali and I spend a fair amount of time calibrating together and making sure... Again, there's cases where there's an exception because there's clear issues happening for someone. But on average that is what's happening. And I think people know that's what's happening because we told them that. And I think that's pretty powerful.

Lenny (00:45:55):
That is so interesting. I've never heard of that approach. That is definitely solving that problem of EM/PM or...

Will Larson (00:46:01):
Yeah, the incentives are shared now, which isn't perfect. It's still hard to balance them. They can still make the wrong trade-offs, but at least they understand the incentives are shared, which I think is a pretty powerful idea.

Lenny (00:46:15):
That is really interesting. I imagine some companies might even want to include design managers in that, take another step.

Will Larson (00:46:23):
The role and the primacy of different functions in different companies varies so much that it's hard to have a one size. You could also imagine where you want a staff engineer in that or not. And so I think very company specific. But yeah, I think design could absolutely be involved particularly for a design led company like an Airbnb or something like that.

Lenny (00:46:43):
Wow. So interesting. Maybe just as a final thought there, if a PM is having challenges with their EM, what do you think PMs maybe don't realize their engineering managers are finding important or maybe are stressed about that they're just like, "Oh wow, I never thought about that."

Will Larson (00:47:00):
I think one of the biggest challenges I've historically seen, particularly in the last decade is this idea that engineering managers have the job of giving their team interesting work. I think that that can put... You often see this in growth teams where the growth team is like, "Hey, we just need to do a ton of experiments." An engineer is like, "I want to build something brand new." And the eng managers in between those try to figure out, "Need to ship 50 experiments that are pretty boring and they want to do something brand new. I don't know how to do solve this."

(00:47:30):
So it's a tricky moment. And good EMs find the way to balance, but that's the biggest source of ongoing friction where the EMs have been told by their teams they need to do something that the PMs just have no visibility into. And it makes the EM seem totally unreliable partners because they're trying to solve these little bit of these invisible constraints. And that's where I think pushing further to understand, "Hey, you keep prioritizing this rewrite into a new programming language."

(00:48:00):
To me that seems like completely idiotic thing to be doing. What's going on? And then once you understand, you might not agree with them, but at least you can have an honest conversation about how to navigate those constraints versus just like, "Man, you won't believe what my EM partner did today. This bozo did blah, blah, blah." And having this victim villain mindset about your peers.

Lenny (00:48:24):
An adjacent topic that I wanted to spend some time on is measuring engineering velocity productivity. I think it's probably one of the most common and also maybe the most annoying questions eng leaders get is just how do I know if my engineers are moving as quickly as they can? How do we help them move faster? What advice do you give to eng leaders for eng teams just for how to measure productivity well?

Will Larson (00:48:44):
This is a question that's coming up even more in a moment when we're reducing a lot of the size of teams from the industry when the venture capitalists that are on the board for these venture-backed companies are pushing on the efficiency of engineering. Engineers are trying to figure out how do we represent this? How do we prove that we're appropriately productive for the amount of headcount and funding that we have as an organization?

(00:49:09):
And man, that's hard. So the first way that people focus on trying to answer these questions is just benchmarking by the amount of funding that you have. And that's pretty straightforward to do is a mechanical exercise. You get a data set from your venture capital funds or whatnot, and you figure out, "Okay. How much should we be spending in R&D? How much should we be spending in engineering? How much should we be sending on infrastructure engineering in R&D?" And you can benchmark this all out and figure out what the correct numbers are there.

(00:49:40):
The problem is this is a very mechanical and not very insightful, driven way. It'll get you a defensible answer. It's like the old, no one gets fired for buying IBM, which definitely hasn't been true in my career ever. But this idea that if you just have the right benchmarks, DCs won't judge you for spending too much in engineering, but this doesn't actually help you get to the right place. It just helps you get your board to be less angry at you, which is useful because it's hard to do good work when your board is angry at you.

(00:50:13):
But it's not useful in the sense that it doesn't actually help you run your organization effectively. So then there's the much harder mediator problem of how do you actually know if your R&D team or engineering team is effective? What I find is a couple of things. First, if you're a good leader and you talk to engineers, they will tell you... The engineers know if their teams are effective or not. And if they're not, they'll also tell you why not. And their diagnosis can be wrong, but there's a crumb you can start picking up and you can trace the crumbs to figure out what's wrong.

(00:50:49):
Often you'll have more experience to analyze the complaints to figure out what kind of the contributing causes are to them. But yeah, if you just go talk to the team on an ongoing basis, you'll know if they're effective or not and you can go work to solve those specific problems. But again, you can't tell your board, "Oh, it's fine. I talked to the teams that they're good." My intuition's spot on because how do they know if your intuition is good or not?

(00:51:17):
They're dealing with a huge portfolio and some of their leaders are talking to are good, and some of them have terrible intuition. How do they actually assess? I think it's tricky. What I've tried to do is basically two things. One, aligning engineering evaluation to the business and product goals. So I want us to be wholly accountable with the product goals. Well, we did a good job products like screwing up over there. Obviously, a lot of companies find comfort in doing that, but really we're here to support the product, to support our customers in doing something interesting. We're not here to build novel systems unless it supports the customer and the product.

(00:51:59):
So first try to align heavily there. Second, I think just showing the roadmap of the valuable things we've done in the last six months is really powerful. I think sometimes people are like, "I don't have anything to put there." And you're like, "Yeah, that's a real issue." Or if you have the ton of stuff to put there, that's great. I really find that if you just commit, show the number of meaningful, meaty things that have impact that you're doing and you can explain the impact, people will step back and give you space. If you can't populate that list, people will have concerns and rightly so, they should be concerned about that.

Lenny (00:52:36):
Is there any metrics or tools or anything like that that you find useful too? Because these are all awesome piece of advice, but I imagine everyone is always just like, "Give us this number we're tracking, give us this dashboard, see what engineers doing."

Will Larson (00:52:49):
So one of the most influential books in the last decade in software engineering leadership and infrastructure is Accelerate by Nicole Forsgren, Gene Kim, and I believe there's a third author on that one, but I'm forgetting right now. Really phenomenal book and it comes up with these four metrics. It comes up with lead time. It comes up with incident remediation time. It comes up with failure rate. And the fourth one of some sort. There's at least 50 different startups out there that are selling you dashboards that instrument these pieces of data and they want you to just evaluate your team on them.

(00:53:30):
The challenge is these are really good diagnosis metrics. And so hey, our deployments are slow. Why is that? How do we speed them up? But your deployments being slow doesn't make you a good company or a bad company, it just tells you where you should focus on improving. It doesn't actually change how you are. And similarly, if your lead time is quick or slow, it tells you where you should invest or it doesn't actually tell you if you should fire your engineers or something like that. That's way, way more details specific.

(00:54:00):
So people do like to see these metrics just like they see uptime metrics. A lot of engineers report on sprint points or stuff like that to their board, which are just totally, totally fake thing to be reporting on. But people get some comfort on it. So my biggest thing here is when people measure things, this isn't an engineering only problem, but when people measure, they take on the perspective of an expert and they can tell you why not to measure everything. They can tell you why every measure is wrong or inaccurate and they rule everything out and so they measure nothing and they go to someone who's not an expert and well actually there's no accurate measure to give.

(00:54:37):
They're not an expert is like you don't know what you're doing. And so you just have to get comfortable measuring something that's not perfect, but you can actually measure and reporting on it and then the measure that's imperfect as people ask questions, that's an opportunity to educate people on why the measure is imperfect. What are some things that misses or kind of the lies from the conversation.

(00:54:59):
Metrics are about educating the people consuming the metrics about the reality of the rich data underneath. They're not about this perfect data set that shows everything starting with something mediocre and the Dora metrics are really helpful for diagnosis, but if you have to, they can also be a good enough starting place to start reporting to your board or your CEO or to the other executives and then you're like, "Oh, there's all these problems with them."

(00:55:22):
Yes. There are all those problems with them, but that's this place you start and you educate people up from there to help them understand the nuances and that's how they become more sophisticated, understanding engineering, not by refusing to give them anything they can possibly measure.

Lenny (00:55:36):
Awesome. I'm glad that was your answer because we had Nicole on the podcast and she talked through Dora and all the frameworks that she recommends. And she even actually shared some benchmarks that she points people to that give you some sense of just like, "Are you in a good place roughly or not?" So we'll point people to that episode to dig deeper. Awesome. I'm glad that you're a fan.

(00:55:55):
Okay. Just a couple more questions before we get to our very exciting lightning round. One is around values, company values, org values. Do you have some really good advice for people for how to think about coming up with values? What do you share? What do you recommend to people that are trying to figure out what values they should define for their org and their company?

Will Larson (00:56:14):
I mean, values are really interesting, right? And different companies talk about values in different ways. I once worked at a company where the execs went to visit the Facebook campus. They saw the values written up on the wall and they took the Facebook values and wrote them up in our walls and that didn't do a whole lot. It maybe undermined people's confidence in the critical thinking of the executive team that just took these written up on Facebook walls and replicated it.

(00:56:39):
But I think those values did work well for Facebook and those values were meaningful for Facebook. And so first you can't do is just steal values. Value cargo culting. Users first. Great Amazon value. A lot of companies aren't users first and that's okay, but what's not okay is when you put, "Hey, we're users first," and then you actually show the decisions you're making and you clearly aren't users first.

(00:57:06):
So one of the things I think about is just honesty. And so good values have to be honest and so any value can be honest or there's no universally honest values. You can say something like, "We're thrifty." Or we can say something like we spend as much as we need to get the best value. Those are totally different and good companies are run both ways. So the first rule I think about a lot is honesty. You actually do what you claim you do and the value. The second one is applicability. You have to have value that you can actually figure out how to apply to your work.

(00:57:39):
And so one of Stripe's values was no longer a value I believe, but it's optimized globally. And so optimized globally is a really interesting problem because sometimes you'll have something you wanted for interesting value. Sometimes you want to do something and you're like, "Hey, I want to introduce a new programming language that's better for my team." For the organization overall, this is actually much worse for the organization so I'm not going to do it.

(00:58:03):
Uber didn't have this as a written value, but implicitly Uber's value was do what's good for your team and ignore everyone else because that will slow us down. So the two different companies had opposite values, but they're both very applicable. It's like how should we navigate decisions? Should I optimize for my team or for the organization? So those are applicable to real problems and they were honest where Uber was just like, "Don't worry about other people." Make it work for your team. And that's how they moved so fast because they just didn't worry.

Lenny (00:58:32):
Wasn't their value of toe-stepping, encouraging toe-stepping, something like that?

Will Larson (00:58:36):
Let builders build toe stepping. There were a number of values that could be interpreted in different ways and sometimes they got weaponized in various ways as all values do. But these are both interesting in different ways. And so number one is honest and two is applicable. Three is I think the last thing for a good value is this idea of reversibility. So there's some values that aren't actually usable. And so here's a good example. We build good software. Okay. But why would you ever not build good software? That doesn't make sense or we solve customer problems that matter. Good.

(00:59:22):
What company doesn't think they're solving customer problems that matter? And so there's certain values that just you can't apply. And so I think of these as identity values. These are really just you describing who you want to be or we care about our customers. Great. But who would say they don't care about that? There's certain values that I think of as just identity values and they're not wrong to have identity values, they just aren't very useful.

(00:59:51):
You can't actually use them for anything. And so I just always push people not to spend too much time on these because they feel good when you're an executive team debating what are these identity values? It's like we're kind to other people or sure that sounds good. We're a family. Sure, that sounds good. That one I guess is a little bit reversible. There's Netflix, which is like, "We're a team like a sports team. We're not a family." And so a little bit reversible, but not perfectly.

(01:00:20):
But yeah, these are the three that I found really useful for any value. Is it honest? Is it applicable? And can you reverse it? And if not, it's probably actually not helping the team make decisions.

Lenny (01:00:30):
These are great. It reminds me a lot of... I was there during Airbnb's period of coming up with values. Something that I would maybe add and maybe fits into one of these buckets is it needs to be clear who doesn't? There needs to be a group that doesn't quite fit because if everyone fits, you're not doing anything useful. What's the point? Which feels weird to say, why would not everyone fit in our big group of awesome company? But it's clear who is not a good fit, who doesn't belong basically. It's kind of like a cult a little bit like, "Who's not in our cult? Who doesn't belong?"

Will Larson (01:00:59):
But I agree. If it doesn't apply to anyone, then why bother saying it? It doesn't mean anything. And you could say it's actually the hiring filter where there are people who you've explicitly chosen not to hire because this wouldn't apply to them. Then I think it's useful because it helps you actually figure out who to bring in. But if it doesn't apply to anyone you're hiring or anyone that you have in the company, then it's just isn't worth having because you already have too many values. You are already trying to get rid of values because you have 17 and you need to get down to four where people can remember them. So if it doesn't apply to anyone, why bother having it at all?

Lenny (01:01:32):
Yeah. Integrity is a common one. Integrity. Everyone has that. Nobody wouldn't want integrity. What is unique?

Will Larson (01:01:38):
We're a non-integrity company. We're the company that thinks integrity is bad. That's not a real thing.

Lenny (01:01:45):
The other one I'll add to is honest. So Airbnb, we had six values initially. One of them was simplify and a year or two later everyone just realized we're not actually good at this. We want to simplify, but we're not great at this skill and values should describe who you are not who you want to be and aspire to be. So they cut two values including that one, and they're just like, "Let's just do these four because this is actually who we are. Let's be honest with ourselves."

(01:02:11):
Okay, final question. I wanted to visit Failure Corner, something that I've added recently to this podcast where people share a story of failure. And you have this amazing post about your experience with Digg and the rewrite that you all went through. I think it was the version four of Digg. Can you just tell that story and what happened? How much of a mess it ended up being?

Will Larson (01:02:33):
Yeah, Dig V4 is... I mean, it's still something I have a lot of fond memories for. There's one picture that I've kept and there's a picture of a lot of the engineers around this table in the middle of this giant office and they're serving sushi. We had waiters, caterers come in that day. They're serving sushi. They have plates with champagne flutes on it. There was a full bar and we're all around this table because the site is not up.

(01:03:03):
And so Digg before essentially what Kevin Rose or the board or some combination there realized is that Digg was losing to the social networks and that this idea of aggregated news was going to be outcompeted by the Twitters, the Facebooks, et cetera, if we didn't find a way to move to have a social component for it. It even outcompeted by Reddit longterm was kind of the fear. Although at the time that that was far from obvious. And so we needed to move to support social functionality and the previous version we simply couldn't get it to work.

(01:03:39):
So the decision that was done, I think two and a half years before I joined, and the shift about six months after I joined was they needed to do a complete rewrite in order to get there. This is a decision that never works out for anyone. So I think as someone with more experience, I could have predicted this wasn't going to work out. But I was earlier in my career. My PM counterpart at Yahoo, Das Kofinovsky. He went to Yahoo and he's like, "Come to Digg."

(01:04:10):
Worst case you'll make a couple hundred thousand in a year. Worst case. Probably really great outcome. Anyway, that's not what happened. The worst case was a little bit optimistic. So we go and the CEO got fired two days before I joined. So the current CEO left and then Kevin Rose came back for about six months, something like that. And we're just on the death march trying to get this thing out.

(01:04:37):
So we pushed really hard. This was before the cloud for the most part. So we wiped pretty much all of our existing servers to re-image them to the new software. We try to bring the site up and just keeps crashing. And so it basically takes us a month to get it fully functional again. And so that day sitting around that table with champagne and sushi, that's just like day one. And by 30 days in, most people aren't even trying to get the site back up anymore.

(01:05:08):
There's maybe five of us who are still trying. And we did. I think that was a really powerful moment for me. I think in the first two days myself and Rich Schumacher, one of the other engineers, we had to write a caching system from scratch, which got us half the way up. Really a terrible way to do software on a side note. I'm not recommending this to anyone. This was a series of anti-patterns kludged into a launch. But we got it partially up, but we had to restart it every 12 months.

(01:05:41):
Every 12 hours, every server had to be restarted even with the caching mechanism. And then about three weeks after that, I finally figured out what the core bug was, that was bringing us down every 12 hours. It was this incredibly simple issue that had just been hard to debug, basically related to the way that Python initiates variables used as default parameters. It's something super silly and we just had someone who hadn't written Python before who was working on the API code, so they didn't realize it's gotcha.

(01:06:15):
Then no one else caught it when it was reviewed and it just took a long time to debug. It was such a non-obvious. It didn't break anything, it was just doing a lot of extra load on the servers. We finally figured it out and it was just really remarkable experience pulling through. And you know what? The company still went to zero. So we had this at launch. I think we did this heroic, heroic stretch to get it working.

(01:06:43):
A couple weeks after that, a new CEO came in, did a round of layoffs. This is back I think 2012. The team nine months after I started was down to 30 people from about a hundred and it went downhill from there, from a business perspective. But we launched a lot of functionality, has really learned just a tremendous amount. And it kind of shaped what I think about in terms of early in your career, getting learning and going into a company that is maybe having a rough time.

(01:07:15):
I became a manager two and a half years into my career. Basically running the entire engineering team there because everyone who had a lick of sense quit or got laid off, and it was just complete idiot me trying to be the manager for the engineering org, wasn't qualified and no one would've given me that job, but I was the only one dumb enough to take it at that point. I learned so much and I really the kernel that turned into my entire career where it was that opportunity, even though at the time it was pretty grim.

Lenny (01:07:49):
That's an amazing story. I feel like a lot of these experiences were in the moment, it's just like, "What is going on? This is so bad and hard," end up being the most interesting and looking back end up being the most biggest teaching experiences. The ones you like bond over with people you work with like Apple. It always comes to mind where it's just like Steve Jobs's joke, people like crazy and then they look back and that was the best moment in my career.

Will Larson (01:08:12):
You would never voluntarily take on a lot of these really challenging things, but sometimes when they show up, you're with a group of people you really respect, you love working with and you want to overcome together. And that's really powerful experience. Even if Uber China was similar where if someone had been like, "Hey, do you want to go work on this Uber China migration?" I would've been like, "Absolutely not." But no one asked. They're just like, "Get this done," and so we did. I think these things are pretty remarkable.

Lenny (01:08:39):
And just to be clear, so Digg was down for a month basically during this period? Is that...

Will Larson (01:08:43):
So it basically didn't work properly for much of the month. It was like read only was back up in about three days, but the vast majority of the actual user functionality just wasn't working properly for pretty much an entire month and it was not that good. I mean not great, but that wasn't the biggest problem Digg had at that point. But it was one of the biggest problems that had at that point and it wasn't a real sign of things likely to go well for us. But like I said, you learn from those and I'm really proud that we and the team got it working, got it running even if ultimately we still went to zero and ran out of money and kind of sold for parts.

Lenny (01:09:32):
Do you think Digg could have made it? There was a world where Digg would've been a hugely successful business or do you think it was just way too late and it's the wrong product?

Will Larson (01:09:39):
The thing that really killed Digg is the change. It wasn't SEO driven. So monetization was from ads. Well, many companies including Digg claimed that it was the first in kind of stream, in feed like advertising company where Twitter has ads within the tweets or Facebook does. But Digg did that before Facebook or Twitter really innovated the ad format. But the vast majority of monetization was on these... We call them permalink pages, which is page 40. Then article we crawled and the vast majority of traffic for that was driven by Google search. And so there was an SEO change, which really is the thing that started creating the urgency for us to launch this migration.

(01:10:20):
SEO changed, traffic started going down, monetization was driven by that. And so we were already on fire by the time we tried to launch this. But I do think that I still want something like what Digg was trying to become today. Social news based on like what my friends are actually reading and liking merged with a global index of similar users who are interested in similar topics. It's still a product that I think Google Reader has some kind of similar components to it.

(01:10:49):
These are both interesting products solving interesting problems that have not for whatever reason been successful as businesses. And I do think there's a gap there still, but there's a lot of people trying unsuccessfully to fill it and there must be a reason why people struggle to fill it despite so many people trying.

Lenny (01:11:06):
Awesome. Will, is there anything else you want to share or leave people with before we get to our very fast lightning round because I know you have to run in about five minutes?

Will Larson (01:11:16):
I think we've covered a lot of it. New book coming out. New book coming out in February, Engineering Executive's Primer, O'Reilly. But that's probably it.

Lenny (01:11:25):
Awesome. Where do people find that? I know it's on O'Reilly. You can look at a preview of it even today, right?

Will Larson (01:11:29):
Yeah. O'Reilly, you can see the early copy. You can order it on Amazon as well, but it won't be shipping until February.

Lenny (01:11:37):
Okay. And then just to be clear, who's this for? It's for engineering executives by the sound of it.

Will Larson (01:11:42):
It's for engineering executives, but more so like anyone who wants to be one, anyone who's trying to figure out how to work with an engineering executive. So I think if you are struggling to understand why your CTO keeps doing boneheaded things, or if you want to side manage them, you're the head of product and you can't get the CTO to stop complaining about the engineers need more interesting projects to work on, this might be useful for you too.

Lenny (01:12:04):
Amazing. Okay. Ready for the lightning round?

Will Larson (01:12:07):
Let's do it.

Lenny (01:12:08):
What are two or three books you've recommended most to other people?

Will Larson (01:12:11):
So I talked about Thinking in Systems and Primer. I talked about Good Strategy, Bad Strategy, but I'll give you a third one, which is Don't Think of an Elephant by George Lakoff. It's a really interesting book about framing things in conversations that has really changed how I communicate.

Lenny (01:12:24):
Amazing. Favorite recent movie or TV show you've really enjoyed?

Will Larson (01:12:28):
I don't watch much TV or many movies anymore, but something I do still watch is Top Chef with my wife. She's a Top Chef, super fan. And there's something just very relaxing from these formulaic structured shows where you kind of know what's going to happen. There's no real consequences that matter too much and just escaping from real life to these formulas can be pretty peaceful.

Lenny (01:12:50):
No one has ever mentioned Top Chef before, so that's fun. Do you have a favorite interview question that you like to ask candidates that you're interviewing for a job?

Will Larson (01:12:58):
A lot of my interviews now are trying to help people decide if they actually want to join a company. And so my favorite question I ask now is like, "Hey, we've really loved you. You're going to come through. I think you're going to get a lot of offers from other companies too. I bet you'll have three or four really compelling offers because you're a fantastic candidate. How are you going to figure out really specifically which of those options are right for you?"

(01:13:22):
I think it forces people to tell you what they want and then you tell them why you have that more than anyone else, and then you can actually pitch them on what matters versus pitching on things that don't.

Lenny (01:13:31):
Love that. Do you have a favorite life motto that you often come back to share with friends, find useful either in work or in life?

Will Larson (01:13:40):
No mottos, but I can think of two things I thought about a lot. At Uber is something I talk to people a lot because it was a challenging time for much of it. It was there's no way around, just through.And that was like, "Hey, we're not going to dodge around this. We're going to gut through it and we're going to get to the other side and then we're going to be there." What I think about a lot more now is, will anyone remember what we decided in six months? Because I think people stress out about a lot of decisions, but I increasingly believe most decisions people stress out about just aren't that important.

(01:14:11):
So I'm like, "Will anyone care in six months what we did here?" And the answer is no. Just do something reasonable and let's move on to the next more important thing.

Lenny (01:14:17):
I love that. You've done a lot of writing. Is there a piece that you've written that you feel like is underappreciated that no one really totally got and hasn't spread and you're like, "Ah, I'm so proud of that one"?

Will Larson (01:14:30):
Maybe the piece I'm most proud of from last year was Hard To Work With. So Hard To Work With is basically I see a lot of people who are incredibly talented, but they try to hold their peers to a high standard and then they're viewed as combative or difficult to work with. And this one comes from a core struggle of my early career where I kept trying. I thought I was holding people accountable and people were just like, "You suck to work with."

(01:14:58):
And I was like, "But I'm just trying to have a high standard. Isn't that what we want?" And talk about honest values. Every company is like, "We have high standards," and you're like, "Well, let's do it." And then they're like, "We don't have high standards here. You suck." So that one is one that really is so transformational to me, and I think it really hits some people hard because I think a lot of people really go their entire career without figuring this one out.

(01:15:20):
And they're some of the most talented, hardest working people you'll ever work with and can't quite land this one idea that's holding them back. And they care so much and they are often despised because they care so much. I think this is one that I hope more people will read over times and there's a really important lesson for me in there.

Lenny (01:15:42):
Well, we will link to it in the show notes and help more people discover it. Two last questions. Where can folks find you online if they want to reach out and maybe follow up on questions? And how can listeners be useful to you?

Will Larson (01:15:51):
So find me online, lethain.com, lethain.com. All my writing, my books, everything links linked there. And the biggest thing that I'm thinking about right now is just strategy. So really curious for folks who are thinking about strategy, who think they've done product, business, or engineering strategy well. Would love to hear from folks what they're thinking about, what's actually worked and maybe what are the lies that have not turned out to work that they thought might work earlier in their journey.

Lenny (01:16:19):
Amazing. Will, thank you so much for being here.

Will Larson (01:16:23):
Thank you so much. This is really fantastic.

Lenny (01:16:25):
Same for me. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

