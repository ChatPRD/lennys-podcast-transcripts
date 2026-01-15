---
guest: Tomer Cohen 2.0
title: Why AI is disrupting traditional product management | Tomer Cohen (LinkedIn
  CPO)
youtube_url: https://www.youtube.com/watch?v=R-zCfLQD_84
video_id: R-zCfLQD_84
description: Tomer Cohen is the longtime chief product officer at LinkedIn, where
  he’s pioneering the Full Stack Builder program, a radical new approach to product
  development that fully embraces what...
duration_seconds: 4052.0
duration: '1:07:32'
view_count: 23051
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- okrs
- kpis
- user research
- mvp
- iteration
- experimentation
- funnel
- team building
- culture
- management
- vision
- mission
- positioning
---

# Why AI is disrupting traditional product management | Tomer Cohen (LinkedIn CPO)

## Transcript

Tomer Cohen (00:00:00):
When we look at the skills required to do your job, by 2030, it will change by 70%. So whether or not you're looking to change your job, your job is changing. In order to stay competitive, you actually have to go back to some first principles, go back to the drawing board and reimagine what it means to be building.

Lenny Rachitsky (00:00:15):
You're experimenting with a very different way of building product at LinkedIn that fully embraces what AI unlocks.

Tomer Cohen (00:00:24):
We call it the full stack builder model. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and which team they're on. It's really fluid interaction between human and machine.

Lenny Rachitsky (00:00:37):
This feels like this could be a model for how a lot of companies operate and how product ends up being built in the future.

Tomer Cohen (00:00:42):
Change management here is going to be a critical part, but it's not enough to give them the tools. You have to build the incentives programs, the motivation, the examples to how you do it. I see a lot of companies roll out their agents and just expecting companies to adopt. It doesn't work this way.

Lenny Rachitsky (00:00:56):
There's always been this question, is AI going to just make people that are not amazing, more amazing, or is it going to make amazing people even more amazing?

Tomer Cohen (00:01:01):
Top talent has this tendency of continuously trying to get better at their craft. The key trait that I'm emphasizing for builders is...

Lenny Rachitsky (00:01:11):
Today, my guest is Tomer Cohen, longtime chief product officer at LinkedIn, who is piloting a new way of building that I think will become a model for how companies operate in the future. It's called the Full Stack Builder Program, and essentially the idea is to enable anyone, no matter their function, to take products from idea to launch. They've scrapped their APM program and replaced it with an associate full stack builder program. They've introduced a new career path with the title Full Stack Builder that anyone from any function can become. And as you'll hear in the conversation, they've built a bunch of internal tools and agents and processes to basically build a human plus AI product team that can move really fast, adjust to change quickly, and do a lot more with a lot less. If you're looking for inspiration for how to rethink how your team operates and to lean into what AI is unlocking for teams and companies, this episode is for you.

(00:02:06):
A huge thank you to Shira Gasarch for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. And if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including a year free of Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, [inaudible 00:02:29], Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin and Stripe Atlas. Head on over to lennysnewsletter.com and click product pass. With that, I bring you Tomer Cohen after a short word from our sponsors.

(00:02:42):
My podcast guests and I love talking about craft and taste and agency and product market fit. You know what we don't love talking about? SOC 2. That's where Vanta comes in. Vanta helps companies of all sizes get compliant fast and stay that way with industry-leading AI, automation, and continuous monitoring. Whether you're a startup tackling your first SOC 2 or ISO 27001 or an enterprise managing vendor risk, Vanta's trust management platform makes it quicker, easier, and more scalable. Vanta also helps you complete security questionnaires up to five times faster so that you can win bigger deals sooner. The result? According to a recent IDC study, Vanta customers slashed over $500,000 a year and are three times more productive. Establishing trust isn't optional. Vanta makes it automatic. Get $1,000 off at vanta.com/lenny.

(00:03:36):
This episode is brought to you by Figma, makers of Figma Make. When I was a PM at Airbnb, I still remember when Figma came out and how much it improved how we operated as a team. Suddenly, I could involve my whole team in the design process, give feedback on design concepts really quickly, and it just made the whole product development process so much more fun.

(00:03:56):
But Figma never felt like it was for me. It was great for giving feedback and designs, but as a builder, I wanted to make stuff. That's why Figma built Figma Make. With just a few prompts, you can make any idea or design into a fully functional prototype or app that anyone can iterate on and validate with customers. Figma Make is a different kind of vibe coding tool. Because it's all in Figma, you can use your team's existing design building blocks, making it easy to create outputs that look good and feel real and are connected to how your team builds. Stop spending so much time telling people about your product vision, and instead show it to them. Make code-backed prototypes and apps fast with Figma Make. Check it out at figma.com/lenny.

(00:04:42):
Tomer, thank you so much for being here and welcome to the podcast.

Tomer Cohen (00:04:45):
Thank you. It's great to be back.

Lenny Rachitsky (00:04:47):
It's great to have you back. I'm really excited to be chatting because you're experimenting with a very different way of building product at LinkedIn that fully embraces what AI unlocks, kind of leans into what is now possible, and to me, this feels like this could be a model for how a lot of companies operate and how product ends up being built in the future. There's a lot of product leaders that are talking about AI, what they can do. It feels like you're actually doing this in a really, really radical way, and so I'm excited to learn from you to hear about this for listeners to understand what you're seeing, what you've learned. Let me start with just why did you decide this was necessary? Why are you rethinking all of these things about how product has been built for a long time? AKA, why do people need to pay attention to what we're about to be talking about?

Tomer Cohen (00:05:34):
It really starts with kind of the basics. For me, technology has always been about empowerment. It's not about what it does for us. It's about what enables us to do. And now we have this amazing opportunity in my mind to make it about meritocracy, and I think it's an opportunity, but it's also a necessity right now, and I want to put this in context where we're entering this phase where the time constant of change is far greater than the time constant of response. Basically means that change is happening faster than we're able to respond to it. Now, LinkedIn has this unique view of the world of work. So we actually have some pretty, in my mind, mind-blowing stats to put this in perspective. When we look at the skills required to do your job, by 2030, which is literally four years from now, sounds a long time, but four years from now, it will change by 70%.

(00:06:25):
So whether or not you're looking to change your job, your job is changing. The only question is, do you keep it? And then we look at organizationally, the fastest growing jobs right now, the most in demand jobs in the market are growing by north of 70% from last year's fastest growing job. So there's a new kind of iteration of what you need as an organization to thrive. And then you apply that to building products and you realize that in order to stay competitive, you actually have to go back to some first principles, go back to the drawing board and reimagine what it means to be building. And what I love about this is when you think about the role of a builder, which the builder is at the heart of company, the goal is actually quite simple. The builder takes an ADN, she brings it to life. That's really the process, right?

(00:07:11):
And we all build those, let's call them best practices. You research the problem really well, you spec it out, you design it, you code it, you launch it, and you iterate. That's basically it. But what happens at many at scale companies, LinkedIn included and many other companies, over time that process became very complex very quickly. So what happened? We took every step and we expanded it to a lot of sub-steps. Researching, the problem became looking at for us 10 to 15 sources of information, obviously talking to customers about doing data pools, looking at feedback tickets in multiple sources, social media, interactions with customers. We probably have 10 to 15 sources of information we go for before we feel like we have research department really, really well.

(00:07:58):
Think about reviews for product. There is design reviews, privacy reviews, security reviews. I can go on and on and on. And each one of those substeps actually has a valid reason to exist. But when you add a whole thing together, you're like, "Oh my God. This is why it takes, to build a small feature, multiple teams, multiple code bases, multiple sprints just to get it out to launch," and not talk about iterating, which is actually where you seek success. You never see success in the launch itself. So really the work itself is not complex, but the process we made very complex. And when I was digging in, I found it doesn't end there because somebody has to do all those substeps, so what happened is you actually move from process complexity to organizational complexity as well.

(00:08:41):
And then you actually led to microspecialization. All those subsets are doing by somebody specific. So from one builder, we have multiple functions. Obviously we have engineering, product and design, and you can start questioning those lines. At least I am internally. And from there, we have a lot of subspecialties. It happens in every one of those functions, but imagine design. We have interaction design, animation design, content design, research. There's so many aspects to that. So they're all valid, but they all have people, and that entire process basically means a lot of... It's basically bloating. It's complexity. And then without noticing, you end up with this massively complex... We actually have this diagram that basically shows the process complexity, organizational complexity together.

(00:09:26):
And usually people are mind blown because they're working on one thing very specific, but when you zoom out, you have this overwhelming experience you're kind of thinking about. And now we have this real opportunity to collapse the stack backup, go back to craftsmanship, rethink the product development lifecycle, which is where the full stack builder model comes to life.

Lenny Rachitsky (00:09:47):
Wow. Okay. And there's so much here. We're going to be showing the visuals as you talk to help people see what you're explaining here. And all of this is very rational. If you have 15 sources of information, why not pull from it? Why miss out on that stuff? And what you're describing here is as you get more power and more specialized... It all makes sense rationally, but when you start to step back and look at this like, holy shit, it takes six months to launch one feature. I want to ask about the stat you shared. I think this is an incredibly powerful stat and you have very unique data here to tell you this sort of stuff. So you said that something like 70% of the skills that people will need in the future are going to change.

Tomer Cohen (00:10:28):
To do their current job.

Lenny Rachitsky (00:10:29):
To do their current job. And what is this looking at? Is this just based on historical data or how do you find that?

Tomer Cohen (00:10:36):
Yeah. To be fair, there was always a change, right? So it was never about just keep the skills you have today, but we've never seen such a dramatic part of your role today. So whether you are a marketer right now or a seller, a recruiter, an engineer. Engineering is where a lot of the investment is going in right now in terms of agents. Those jobs will change dramatically. I remember I said my role, my life as an engineer and even then it's changed materially after 10 years, and then the change we're seeing right now, just thinking about in four years, what did it take to actually engineer really, really well would be dramatically different, or to build software, to build an artifact of some sort. But it's true for almost every function. It's not equal. Some job like nurses will see less impact, but some jobs will see 90%, 95% impact.

Lenny Rachitsky (00:11:28):
There's also a stat that I don't think you mentioned here that I saw on the post when you first talked about this program is that 70% of today's fastest growing jobs were not even on the list of jobs a year ago.

Tomer Cohen (00:11:39):
Yeah. No, so this is the fastest growing job on the list were not there a year ago, and then many of them don't even exist a decade or two ago. There's actually some pretty amazing stats across the board.

Lenny Rachitsky (00:11:52):
Okay. So let's talk about this program that you built. Tell us the name and then tell us the gist of what it is today and the vision of where you want it to be.

Tomer Cohen (00:12:03):
Yeah. So we call it the full stack builder model. And the goal, always start with the goal. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and specifically which team they're on. And the idea ultimately is to be able for that builder is to develop experiences end to end, to combine skills and expertise across what was traditionally distinct domains to bring it all together. And it's not a sequence of steps. It's really a fluid interaction between human and machine. That's how the way I see it. And then when you look back at that product development life cycle from the idea, the insight all the way to launch, the key trait that I'm emphasizing for builders is where I want them to spend their time is where I think great builders should shine in.

(00:12:54):
So the idea of vision. Coming up with a compelling sense about the future. Empathy, super critical, right? Having a profound understanding of an unmet need. Communication is critical. And we see this a lot in job descriptions right now for almost every role, but ability for you to align and rally others around an idea. Creativity, which for me is about coming up with possibilities beyond the obvious. For example, I don't think AI yet is great at creativity. I think it's kind of, in many ways, brings back the things you might not know about, but it's not the kind of next level creativity, which I think still humans are much better at.

(00:13:33):
And then ultimately what I think is the most important trait for a builder is judgment. Some people call it test making, but it's making high quality decisions in what is complex ambiguous situations. Everything else, I'm working really hard to automate. Really, really hard. And then when you think about the outcome, it's not just about having more shots at the goal, which I think people go like, "Oh, the iteration speed is going to be very high." Yes, but what you're really doing to an organization of at scale organizations is they're a lot more nimble, a lot more adaptive, a lot more resilient. They can navigate the future. They can actually match the pace of change to the pace of response.

(00:14:13):
And an analogy I have in mind is kind of Navy SEALs. You come to training, they're all kind of learning, they're cross-trained, across multiple areas. What they specialize in is the mission and they operate in small pods and they're very nimble and you can assemble them very quickly. And I think that's going to be the organization that will win in the future.

Lenny Rachitsky (00:14:33):
Okay. So the simple idea, if you're just to boil it down to a sentence, the idea here is there's a builder who goes through the entire product development process essentially on their own. They have an idea, they research, they do data, they prototype design ship. That's kind of like the vision of where this goes?

Tomer Cohen (00:14:50):
Yes, but it doesn't have to be on their own. It's not like... I still believe in teams.

Lenny Rachitsky (00:14:51):
Got it. So smaller teams.

Tomer Cohen (00:14:55):
Just smaller teams. Smaller teams and much more focused on the problem, the mission, per say, versus... Actually, one of the things we've done as an example, we started to do the idea of pods. We're no longer large teams. We assemble a team, ideally a full stack builders coming together and it's less about can I have an engineer design PM working together and trying to combine this trio looking at folks who can flex across and then they tackle something for a quarter or so and then we reassemble those two different pods. That's one example of an manifestation we're doing right now and seeing actually some great success in both in terms of velocity, but also in terms of that focus and nimbleness of that team.

Lenny Rachitsky (00:15:37):
And it feels like the goal here, what you're trying to adjust and that broke as teams bloated as speed and adaptability and flexibility, because going back to your original point that change is happening so much more quickly now that companies that have been building in this traditional way just can't compete.

Tomer Cohen (00:15:56):
Yeah. It's not that you have to break the model. I think the model is broken. It's just this pace of change is helping us realize it.

Lenny Rachitsky (00:16:03):
Okay. So then going back to the things that these builders still do versus what you want to automate. So the list you shared is they're responsible for the vision, empathy, communication, creativity, and judgment.

Tomer Cohen (00:16:16):
Yes. Yeah. And I would put a lot of the focus on the latter. I think if you ask me at the end of the day, what's the kind of most important trait? I would say it's that judgment, test making ability.

Lenny Rachitsky (00:16:27):
And then in terms of what you're automating, what are some of the areas you've seen a lot of success in actually automating and where do you think this goes?

Tomer Cohen (00:16:35):
Yeah. So I think just to kind of break it to pieces, and I think this is... If you were a startup right now, in many ways you can start this way. There's no legacy code, there's no legacy structure you run. And in fact, a lot of the startups I talked to that are built AI natively, they're just working at full stack builders. That's the way they start. If you're at a company at a scale of ours and many others in the market, you're like, this is almost like a new production function and mindset that you have to do. And there's really three components that we're working on. One is platform. The second one is the tools and the agents. And lastly is the culture.

(00:17:17):
The platform one, this is the kind of level of investment you have to do before, before this actually starts, you start to see all the benefits accrue. But the platform for us as an example is rearchitecting all of our core platforms so AI can reason over it. So we're building kind of this composable UI components with server side that we actually build. We're basically building for AI to be ready to bring it in. So you can't just go and bring a third party tool and have it work on the LinkedIn stack. In fact, that's one of our biggest learnings. It never works. Never works. You have to bring it in and customize a lot of it, working almost in alpha mode with those companies to make it work internally.

Lenny Rachitsky (00:17:59):
So this is essentially re-architecting your code base to work more efficiently with AI. Is that one way to think about it?

Tomer Cohen (00:18:04):
Yes. And in many ways, working with those companies to adjust something in their stack to work with our stack as well.

Lenny Rachitsky (00:18:12):
When you say those companies, meaning the development agents like Cursors and [inaudible 00:18:16] and such?

Tomer Cohen (00:18:16):
Yes. Or Figma on design. Or you can think about design systems is another example of that. But you have to have that back and forth because they're not... In many ways, we haven't seen anybody be able to work off the shelf immediately on our code-based design systems and unique context we have.

Lenny Rachitsky (00:18:34):
Just to follow that thread briefly, so there's Figma. That's interesting. So basically the way Figma exports and keeps your design system, that has to change to work better with AI is what I'm hearing.

Tomer Cohen (00:18:41):
They first need to know how to work with our design systems, which is something, in many ways a lot of those companies are working on. Same with coding. It doesn't work that you just bring it in and it just reasons over your code base really well. We tried. We are building that layer that basically allows it to do so, whether it's Copilot or Cursor, Windsurf and so on.

Lenny Rachitsky (00:19:02):
Got it. Okay. Oh yeah, Copilot. Microsoft. I get it. I get it. Okay. Okay. So that's the platform. So that's an investment that you guys have to make to make AI effective at building and doing all these things.

Tomer Cohen (00:19:17):
And then you have tools. So tools is where you really build the agents. I mentioned I want to automate everything outside of those five trades that we talked about, and then we're building the tools for that. And then for that, actually very similarly, I can't just bring a tool from the outside and work. So I'll give you an example. One of our biggest things is building a trust agent. Trust is really important for us at LinkedIn. There's a lot of unique vectors which trust plays at LinkedIn doesn't place it anywhere else. So we need to bring all of that know how and context and information base into that agent. So we ended up building our own trust agent at LinkedIn.

Lenny Rachitsky (00:19:53):
And so what is this trust agent doing? Telling you when you're maybe exposing information that you shouldn't be?

Tomer Cohen (00:19:58):
So when you build a spec, you build an idea, you walk through the trust agent and it'll basically tell you what are your vulnerabilities, what harm vectors potentially you're introducing or will be introduced as a result of that. And I had our head of trust build it. So the head of craft for every area is building their own agent. As an example, we have one of our features for job seekers is called Open to Work. If you're looking for a job, you can put an open to work.

Lenny Rachitsky (00:20:24):
Yeah, a little green loading thing on the circle.

Tomer Cohen (00:20:25):
Exactly. And actually it's a great signal. I've seen some great success from it. People are helping each other. The community really thrives around helping each other. But at the same time, it introduces a trust vector for bad actors because they're open to work. People who are looking for a job are potentially more vulnerable to scams than other folks. So being able to think about how do we prevent all of those ahead of time. So we walked that spec from a couple of years ago through the trust agent. Not only was it able to find all the stuff we initiated at the beginning, but all the holes that we did not catch until later. So that's a great example of something that actually worked really well.

(00:21:03):
That's one. The other one is a growth agent, as an example. Again, LinkedIn has a very unique... Actually, we have an incredible growth team, growth process. We've kind of funneled all of our unique loops, our funnels, our tests of the past, everything into this growth agent, and now you can basically rock your respect for it, your idea for it. And it would not just allow you to do it better. It would actually critique how good is your idea. This is something you cannot bring off the shelf. It's very unique to LinkedIn. So we had to invest dramatically in it. And one team which is using it right now, which is almost... I wasn't thinking about it at the beginning, but our UXR team, our UER team, the user research team is usually using that growth agent to understand out of all the things that are basically surfacing for members, which one has the biggest growth opportunity to have the biggest impact? That was not in the cards when we thought about that idea, but teams are basically funneling those ideas into this one.

(00:22:05):
An example is our research agent. So research agent basically is trained on the personas of our members. You can think about a small business owner, a job seeker and so on. And it's using not just world knowledge, it's using all the research we've done in the past, all the support tickets coming in. So it's pretty good at understanding that persona at LinkedIn. So one examples we had is a team came out with a spec. They weren't aware we had the research agent yet. I asked the research agent for a small business owner, wanted to think about the marketing spec we had, and it critiqued it extremely well. Actually, in many ways shifted the direction of the team to focus on other integrations tools we can focus on, but it's very hard to have that visibility all to all that corpus of knowledge inside of the company.

(00:22:56):
That's another example. We have an analyst agent trained on all how you basically can query the entire LinkedIn graph, which is enormous. And instead of relying on your SQL queries or data science teams, you can use the analyst agent. All of those I would say are, I would call them still MVP+. The goal for us in the next couple of months to basically roll them out externally. Externally, I mean, internally at LinkedIn.

Lenny Rachitsky (00:23:20):
Not as new product lines.

Tomer Cohen (00:23:22):
Exactly.

Lenny Rachitsky (00:23:22):
Okay. So many questions. One is just how are you building this? Is there a platform you're using? What does it take to build an agent at LinkedIn? Is it all internal tools or is there third party use?

Tomer Cohen (00:23:31):
It's a great call. So I think we've been experimenting with a lot of tools. And I would say for a lot of those kind of knowledge corpus agents, we're using everything from Copilot Enterprise to ChatGPT Enterprise. By far though, the most important part was basically our own customization of it. That's been where we saw the biggest gains. Even building the orchestrator across those because you want the agents to start following to each other, the trust agent should work with the growth agent and go do a back and forth versus doing what more sequentially. So we've done a lot of work internally to make it happen. This is why I think it does require that level of investment.

(00:24:09):
And then in some cases, let's talk about the design agent that we're working with. We're working with multiple companies to try and understand which product works best for us. And interestingly enough, and this is another learning, different teams gravitate to different products. So that's something we'll have to resolve and think about how we do this really well, because ultimately we were trying to simplify the process as much as possible, but that was a big learning for us and which tools we use and how we basically integrate them in.

Lenny Rachitsky (00:24:39):
Got it. So you might have an amazing Figma agent, but some teams want to use a different design tool.

Tomer Cohen (00:24:44):
Yeah. So we've kind of experimented with Figma and Subframe and Magic Patterns and so on, and we saw people gravitating depending on the function, their level of visibility, their know how of the tool before, they're gravitating to different tools. And ultimately, I don't want to have eight design agents in the company, so we have to converge into at least a few. And I think it's similar across many areas because the appeal of those, a lot of those agents are trying to solve similar end goal, but they're doing it very differently. And what you'll see that ultimately, I don't think there's going to be a winner takes all because the starting point of the customer or the user will dictate a lot how simple they are for that use case.

Lenny Rachitsky (00:25:28):
Super interesting. The other interesting takeaway here is you're designing very specific agents that are one job to be done. Is that a very intentional decision? Did you try an agent that just is super intelligent on all these things?

Tomer Cohen (00:25:41):
Ultimately, they will do an orchestrator. We're going to really orchestrator across, but we did want to be able to rate and grade those agents really well on how they're doing. And I think there is a level of expertise. Now, we're kind of building this in a way where we'll be able to mask a lot of those. You might not know that there's a trust agent. You might have, we call this internally the product jammer agent that basically does your product jam, which is a process we do internally. You might just use the product jam engine, and that product jam agent will work with all the other agents. But now we're starting with that building blocks until we build the orchestrating layer across.

Lenny Rachitsky (00:26:20):
Another interesting takeaway from what you've been sharing is that so much of the work has gone into the beginning of the product development process, just like helping you craft the right requirements, clarify trust, and then here's product jam and here's the research we've done. And I imagine it's because coding has already been accelerated with all these IEE tools. Talk about just why that's maybe where most of the investment's gone and where you've seen the most impact so far.

Tomer Cohen (00:26:43):
Well, 100% our coding investment has gone, started a while back, and those are fall into place. We have our coding agent. In fact, we've kind of staged it into two parts of it. There is the idea to design part, and then let's call it the code to launch part. The code to launch part has gotten a lot of attention and we're making some big inroads there. Everything from the coding agent to what we call the maintenance agent when you have a failed build, it will do it for you. In fact, I think we're close to 50% of all those builds being done by the maintenance agent and a QA agent.

Lenny Rachitsky (00:27:19):
Wow. So this is when a break builds instead of engineers hopping on the issues that an agent fix.

Tomer Cohen (00:27:24):
You can still go and finish your coffee before you have to go and redo the build again.

Lenny Rachitsky (00:27:27):
Extremely cool.

Tomer Cohen (00:27:28):
But we haven't had much investment until we kind of launched this program in the idea to design area. And that's a material part of work. It's also where the quality a lot of the work comes from, at least before you start to go into the coding phase. The idea is to empower everybody. So if you're an engineer, you can basically use all those tools at the front of the process and be able to be a full stack builder.

Lenny Rachitsky (00:27:51):
How long did it take to get this kind of in place for you to actually form your first team to build these, the initial agents and some of this backend, redo the code base sort of thing?

Tomer Cohen (00:27:59):
I announced this internally end of last year, we really kind of started working, but it was more setting up the teams and the processes internally. We had our first MVPs of those agents I think like four to five months after it was really trained, I would say. But really the work itself has been kind of couple of months of dedicated work. A lot of it has been getting all the corpus of data together, cleaning it up. And that's actually a good learning as well. It's not great to just give it access to your drive and say, "Reason all over this knowledge base." It actually does a very poor job understanding importance of the past and putting weights on stuff. You actually want to think about specifically what the context when do you want to give it to and what's the knowledge base that you want to have it focused on. So even cleaning up, let's call them gold examples or golden examples to learn from, has been one of the biggest learnings. Just reasoning over your entire knowledge base did not work.

Lenny Rachitsky (00:28:54):
Yeah, that makes sense. There may be just like a researcher with a strong opinion about something that you disagree with and it wouldn't know. It's like, oh, of course, this is data, this is fact.

Tomer Cohen (00:29:03):
Exactly. And then it doesn't always understand ties to original specs to success. You have to actually build... This is a really interesting way. When you think about how you bring those tools in, you can't just bring them in. You have to know what you feed them with. And what you feed them with is not just access. I see a lot to just focus on the connectivity and integration and it reminds me of the... This is almost like, this is actually more than 10 years ago when I was co-rebuilding the team, co-rebuilding the feed at LinkedIn and we started from scratch and I had to literally sit down and filter through examples of what is a good professional post on LinkedIn and what is not. And this was like weeks of work getting up that golden sample of examples, but it wasn't... The most important part was feeding at the right data, not all the data.

(00:29:57):
So it requires work. This is where I would say for many companies who are thinking about this phase, and I do a lot of sessions today with CPOs and COs on this process. You have to put this initial work to get the gains after. When I think about it, I think there's a takeaway there in generally with AI, even if you're learning it for the first time and so on, whether it's Cursor or whether it's design, if it's Figma or other tools or Lovable, you should be ready to invest those hours before you start seeing yourself pick up in velocity and quality, which will come up, but you have to invest that time.

Lenny Rachitsky (00:30:35):
This episode is brought to you by Miro. Every day, new headlines are scaring us about all the ways that AI is coming for our jobs, creating a lot of anxiety and fear. But a recent survey for Miro tells a different story. 76% of people believe that AI can benefit their role, but over 50% of people struggle to know when to use it. Enter Miro's innovation workspace, an intelligent platform that brings people and AI together in a shared space to get great work done. Miro has been empowering teams to transform bold ideas into the next big thing for over a decade. Today, they're at the forefront of bringing products to market even faster by unleashing the combined power of AI and human potential. Guests of this podcast often share Miro templates. I use it all the time to brainstorm ideas with my team. Teams especially can work with Miro AI to turn to unstructured data like sticky notes or screenshots into usable diagrams, product briefs, data tables, and prototypes in minutes. You don't have to be an AI master or to toggle yet another tool. The work you're already doing in Miro's Canvas is the prompt. Help your teams get great work done with Miro. Check it out at miro.com/lenny. That's M-I-R-O.com/lenny.

(00:31:46):
What's the current state of the pilot? How large is it? How many teams are doing it? What kind of stuff have you shipped? Just give us a sense of today's world.

Tomer Cohen (00:31:54):
Yeah. I wouldn't say we are yet at a very high sample rate where it's kind of a high percentage of the organization, but we have a substantial part of the organization already using it to provide a lot of the feedback. We're seeing a lot of great examples. So the way I think about the benefits is a function of experimentation volume multiplied by quality. How good are those experiments divided by the time it takes to actually pull them out, like idea to launch. So on saving times, we're seeing, whether it's PMs, designers, engineers, saving hours of work a week right now, whether it's the analyst agent we talked about or the prototyping really quickly or the product jamming experience has been a big part of that. On the quality side, we're seeing insights discussions just be much, much better. And by the way, quality and time, sometimes they help each other because it's high quality, you don't have to spend as much time on something.

(00:32:52):
So we are seeing that applied in. And the volume, I wouldn't say we had a rate where I'm seeing a high percentage organization doing it yet, but this will come once we... We haven't GA'd this internally. That will come in the next couple of months once we have all the stuff in place. But we're seeing designers and PMs picking up bugs directly from Jira tickets, pushing them in, something we haven't seen before, and there's just an appetite for everybody to just join. So in fact, the biggest thing right now is everybody wants access. Everybody wants access to the tools to be able to do it together, and we just want to make sure it's good enough to make sure the whole organization can do it really well.

Lenny Rachitsky (00:33:32):
So how is it that you're piling it? Is it some number of people have access to these agents and they just work the way they've worked with access to these tools? Or is there a team dedicated, this is the way you work now and this is it, and we'll see what happens.

Tomer Cohen (00:33:47):
So that's a great call. So basically we have a team building. It's the core team building the FSB track across all of R&D, FSB, full stack builder. And then there are pockets and pods of teams using it. So basically we are looking at specific areas that we're basically giving it to. The condition there is they give feedback. As a response for that, they make the tool better, so it's not just access. We want people who will use it. So one of your early adopters would be the ones who help [inaudible 00:34:15] up the product really well. So we're doing this in a pod model right now.

Lenny Rachitsky (00:34:19):
So it's like a pod within a larger team, like a designer, PM, engineer kind of group within... Is there an example? You have a part of LinkedIn that's trying this out?

Tomer Cohen (00:34:27):
Yeah. So if I think about some of our teams, whether it's... Actually, we just launched Semantic People Search and the Semantic Job Search as well. That team was using part of those tools to actually help build it. So that team actually, this was PMs building their own dashboards with those tools without waiting for design resources to come in. Then we have a design team who is now... This started really from the manager rolling this out. And in many ways, what I tell this team is, "Don't wait for the official GA. Start doing it. Start leaning in." We're seeing designers of that team starting to push PRs, which never happened before. And now other teams, they want to do this as well. So it's starting with this kind of grassroots experience. I would say the places have been very formal. I would say the beginning has been the top.

(00:35:22):
The product executive teams, basically we move from functional leaders, design, PM, BD, and so on to product areas leaders, and they basically rock across the stack and they also go for a 360 with all of those functions to see if they're really able to do a full stack building experience. Then we're also launching at the junior side a new program called the Associate Product Builder Program, where basically we used to have our APM program, which this is about it's ending this year. And then starting January, we're going to start having our APB program and they're going to come into LinkedIn. We're going to teach them how to code, design and PM at LinkedIn. They're going to go through a pretty rigorous training process, and then they're going to join those pods, and gradually we're going to grow that program to be a material part of LinkedIn as well.

Lenny Rachitsky (00:36:14):
Wow. So this might be the future of the APM program is this full stack builder APM-ish program.

Tomer Cohen (00:36:21):
In many ways, we've built some pretty amazing... I'm really excited for that group. I wish I could join it. But we build amazing training for them. And in many ways, we're going to use that training to think about how we roll it across the organization. We're kind of using the lens of you have great technical skills, but you're not an engineer at a company yet, or you have great design taste, but you haven't designed at scale in company yet, and we're going to teach you how to do it at LinkedIn, but the training we're going to use a lot to extend across the company as well.

Lenny Rachitsky (00:36:51):
Okay. So you have these programs, these pilots and these pods, and you said what you're looking at to see if this is something you roll out is experiment velocity times quality times time.

Tomer Cohen (00:37:01):
Divided by time.

Lenny Rachitsky (00:37:02):
Divided by time. Okay.

Tomer Cohen (00:37:03):
Yeah.

Lenny Rachitsky (00:37:04):
Got it. And I guess I know it's early, but just you said you're seeing that it's saving teams a few hours a week at this point, something like that?

Tomer Cohen (00:37:11):
Yeah. And I think the feedback has been the most important part. Right? The way to think about this is just like you build a product. So we're building this product internally and you want to experiment with some kind of early adopters who will give you feedback, and the feedback has been amazing. In fact, our top talent are the ones who are using this the most at LinkedIn. And the feedback from them has been incredible in terms because they're also willing to spend the time and give the feedback as well. And the response from them has been incredible in terms of like the quality of their output, the time they're spending on this to get the value back, their desire to be part of this and actually scale this and make this even better. So that's where a lot of the excitement has been from how they're using it and the quality we've seen there. I would say in six months or so, we'll be able to see a lot more of the organization use it and you'll start seeing those top line numbers will build as well.

Lenny Rachitsky (00:38:12):
That is a really interesting insight that the top performers are finding the most success, because there's always been this question, is AI going to just make people that are not amazing, more amazing, or is it going to make amazing people even more amazing? And it sounds like it's likely the latter.

Tomer Cohen (00:38:24):
Yes. And in many ways, it's surprising, it's not surprising. I've seen this also when we were... It's surprising because you want everybody else to be part of this and lean in. I think top talent has this tendency of continuously trying to get better at their craft and this innate need to be at the cutting edge of how you build, and I think we're seeing this here as well. This is why I had this phrase I say with the team that if we build all those tools, will they use it? And I know right now the answer is no. It's not enough to give them the tools to use it. You have to build the incentives programs, the motivation, the examples to how you do it. They need to see other people being successful as well.

(00:39:11):
And I've seen this also when we're shifting LinkedIn from a desktop company into a mobile company. It was a very similar process. It's very hard. Change management here is going to be a critical part. I think I see a lot of companies roll out their agents and just expecting companies to adopt. It doesn't work this way. Some will adopt. That tends to be your cutting edge 5% of talent that just wants new tools and they have a bias for change. But the vast majority needs to work for change management in how they do it, and that requires being a lot more thoughtful about the cultural aspect of it, which is by far from me the biggest and most important thing to do.

Lenny Rachitsky (00:39:48):
Yeah. I want to spend time there. And it makes a lot of sense why people don't spend time here because they have so much to do. They got to ship things. Their days are already busy. You have to now carve out time to learn this new tool that'll not pay off for a while. So I get why people are like, "Okay, okay, I'll get there. I'll use it someday," but they don't. This idea of culture, when I saw you share this initially, this is the third piece of making this successful. So there's the platform of getting the code base ready for people for AI to work with. Then there's the tool, like the agents you've talked about, and then there's the culture. Is there more there that you can share of just what has actually worked in helping get people on board? One thing I heard is creating a little bit of FOMO of like, okay, only a few people can use this and you have to sign up to get access. What's worked in getting people to get on board?

Tomer Cohen (00:40:39):
Yeah. I think this is where I emphasize to people that getting everything done, the platforms, the tools is not going to be sufficient. It's a prerequisite for this to work, but not sufficient for this to work because it really requires you to invest a lot in the cultural aspects of how do you get people to lean into this one. And this one might feel slow at first, but I've seen this before with our transformation of thinking from desktop to mobile. And once it picks up, it actually maintains very high velocity. One, people are really incentivized by how you define expectations for them. So to think about what is the expectation of somebody in the role, whatever-

Lenny Rachitsky (00:41:21):
So like changing performance review sort of things.

Tomer Cohen (00:41:23):
Very much so. So everything from how you hire to calibration and evaluation. And one thing I want to see there early is this kind of AI agency and fluency. Like I mentioned, the tools are there. The question is, would you use them? Because the tools will be good enough, but not great at the beginning. That's the classic thing of every good MVP tool. They're good enough, but they're not great. And then you kind of want to build that agency to make the tool better. We're in this kind of notion of we're going to make this better for LinkedIn together. Two is piloting success inside of your organization. That's the pod model where you're showing that not only this could work, it's actually having success. So we have even our partnerships team, our BD team, being able to go instead of relying on waiting for an engineer to help build the developer portal and build the connectors there.

(00:42:17):
Literally one of our head of partnerships just went and did it himself. Didn't even delegate to his team. And their goal is to say like, "Hey, I can do it. You can do it as well." Those examples are really, really powerful. I talked about the associate product builder program where we are going to be very focused on training. I think that will send a really strong message across the organization. People will see this talent and what they can do, and I think that will create that movement. But celebrating wins in all hands, highlighting people and showing those examples. One example we've seen recently, people really looked at it in a surprise lens, but then it kind of, I think, really opened up a lens for them. We had somebody in our user research team. We had an opening for a PM on the growth team, and that role was open for a while, and she said that, "I think I can do it."

(00:43:11):
And she used all these tools. This is a user researcher becoming a growth PM, not usually the career path you see, but she was excited about the area. She used all those tools, and she's now a growth PM on the team. And really, you can start thinking about her more as a full stack builder ultimately. But seeing those openings and then highlighting those two people, actually people who are doing this have been a great example of it. And then just making sure that those tools are accessible. People can provide feedback, you share a lot, has been an incredible part of this. It's not enough to be top-down directive that this is how we want to work. People want to feel like there are success stories. They feel like it's worth their time. It feels it's a movement they want to be part of, and then ultimately they can see successes in how they do it.

Lenny Rachitsky (00:44:02):
I love this kind of comparison to the shift to mobile. We all went through that and there's all these stories of companies requiring you to show mobile mocks. That's the only way we're going to operate. Now everything you have to ship has to be on mobile, and it's interesting how similar this is to them, to that experience. And so a few things you just shared here just to kind of summarize some of the things that have worked for you. Showing wins, celebrating wins, showing people what other folks are doing with AI tools, creating a program that people enroll into and make it a little bit exclusive. This performance review piece is really interesting because that really will change people's behaviors. Here's how we get promoted. Have you actually already made that change to the PM? I guess it's every track, I imagine, not just product management. Have you already made that change or is it kind of like a work in progress?

Tomer Cohen (00:44:45):
So there was two aspects to it. Once I moved my team, my directs, we did 360 for them. So their 360 was, if you came from PM, you had the designers on your team rate you. And so that had its own, and then we shared those with them, and that had its own kind of motivation. But then we broadly took it across. So when we hire right now, we look for those. And then this upcoming cycle, we do a bi-annual. That's going to be part of the performance evaluation piece and we announce it to everybody. And for what, it's where people are excited to show. And they're excited to know how they're going to be... It's always about, like, "I want to know how I'm being rated or evaluated." So just being able to show those examples has been a big part of it.

(00:45:31):
The other thing I would say, it takes time for this program and its formality to roll out across the entire organization, and I was intentionally not trying to be quick at rolling this out to everybody because I think that just dilutes the value of it really quickly because it's not about... I could care less about your title. I care about how you work. So calling you a full stack builder is not what I'm looking for. Changing your mindset to a full stack mindset is what I'm looking for. You're thinking you can do the whole thing. You're looking at those tools and looking at how to do it.

(00:46:07):
So one of the things I've said is if you're looking for a formal reorg or declaration to start building differently, you're waiting too long. Look, my biggest thing is here's a permission for me to just not wait and just go. So whether or not you have the right tools or not, go build the tool, use a tool from the outside, bring it in, show those examples. In many ways, prove that you are a full stack builder in mindset before anything else come to mind. And that just naturally will happen, and that's also where we've seen some of our best talent just goes and leans a lot into.

Lenny Rachitsky (00:46:41):
I love that. I was going to actually mention that quote. Someone you shared, you work with told me exactly that quote you just shared, so I'm glad you brought it up of just if you're waiting for a reorg, you're not thinking about it the right way. How do you encourage people to actually play with these tools on their own? Are you just like, "Go take a few days to play with AI?" Is it just try it? Or is there anything formal you've seen of just getting people to more try this on their own without joining this program?

Tomer Cohen (00:47:05):
A lot of the tools we've made, we've been sharing them regularly. A few of my all hands have been all about how to use those tools. But then at the same time, we're kind of inviting, have you found a new tool that works really well for you? Share it, show it. Again, it could be Slack, could be Messages, Teams and so on, how you do it. But the idea is really to start getting that investment in how things work. Actually, I think in general, you can feel overwhelmed by tools right now, by recipes and how to do things like what's your prompt and what's my prompt. But really it's finding something that kind of works really well, that can gravitate around and really invest in that's been those areas. But I think we've had this invitation to go and explore and go and bring in stuff that you think are great. And in many ways, bring others along on the journey. It's one good way to make the influence much bigger than a few folks who are doing really well with this.

Lenny Rachitsky (00:48:00):
Are there any surprises on the negative side that have come out of this, of PRD is just feeling like AI driven, people slowing down unexpectedly? Is there anything that surprised you of just like, "Okay, this is actually not great"?

Tomer Cohen (00:48:12):
Yeah, we mentioned a few of them. I was hoping for some tools to work off the shelf really well. It was never the case because we had to invest quite a lot.

Lenny Rachitsky (00:48:21):
Never the case.

Tomer Cohen (00:48:21):
Never the case. We had to invest quite a lot. And again, part of it is we just have a lot of legacy information and code based and knowledge and designs and so on. So a lot of the companies we work with are seeing this as a great growth opportunity for them as well to invest, but I do think it's a big area of investment as well. We talked about not just giving access to all of your context which we started with, and we were like, "Oh, here's access to all the drive, all information," failed miserably and hallucinates like crazy." People gravitating towards different tools, like our goal was to converge on tools, but that was pretty hard.

(00:48:58):
And then I think in terms of quality, we've just seen better quality, but I think it's because, again, where we are in the stage is still the early adopters and they're doing a few iterations in terms of how to do it. But I would say the tooling adoption is hard. And then I think for some people, this is important for me to kind of state, some people do not want to be full-stack builders, and that's completely okay. Some people see themselves in specialization, and I think specialization has a place and a role. So I didn't want the message to be across the organization I expect everybody to be a full-stack builder. I do not. I think there are system builders that empower full-stack builders, and then you have people who are specialized. But I don't think we need as many specialized people as we did in the past.

Lenny Rachitsky (00:49:46):
I didn't actually realize this until just now. So is this their title now instead of product manager engineer, they're full stack builder?

Tomer Cohen (00:49:52):
We have a full stack builder title formally inside the organization, and we are gradually putting people in that bucket.

Lenny Rachitsky (00:49:59):
So there's a whole career ladder that's forming. There's a whole... Okay. That's a bigger deal than I even thought. So where are you finding these folks mostly coming from, like product, engineering, design? I imagine it's a mix, but just is there a most common trend?

Tomer Cohen (00:50:13):
It's a mix. People listening, I would just think about just go over your org and imagine who can do it, who can right now flex across those functions, whether it is engineering, design, product, even BD, and what you'll find is there's already quite a few that can flex across.

Lenny Rachitsky (00:50:34):
Interesting. Are there any functions you think are especially successful at this? Not to play any favorites, but I don't know. Are you finding like, okay? Or you could also not highlight any specific.

Tomer Cohen (00:50:45):
No, I think it's a mental model of how you do it. I think if I were to play what's the hardest craft to potentially learn, I think design has a lot more work to get the design agents to be really, really good. So I think designers have a little bit of a leg up in terms of others learning their craft than the vice versa. But I honestly think it's a mindset. I've seen designers code, I've seen PMs kind of design and do well. And this is why I think when you kind of step back and you think about people in your organization and who can flex, I think you'll see them show up in many areas. And what I think you'll find there is they have the agency, they're leaning into new things, they have the fluency, like they're already building new experiences and they have that growth mindset that they just want to get better, so it doesn't matter what they learn at school or what label somebody put in them when they join the company.

Lenny Rachitsky (00:51:44):
What I love about a lot of this is it's the easiest time to transition between different product roles than it's ever been. Design's moving to PM, and sure, or just moving to this new role, it makes it so much easier to, like you said, that researcher became a growth PM.

Tomer Cohen (00:51:58):
And this is probably my biggest advice slash motivation I give to the team because what I tell them is ultimately... By the way, this is for me as well. I think about it the same way. The incentives for you are so aligned with your organization of what we're asking for, right? Because we need you to change. We want to be a more agile, adaptive, resilient organization that can deal with the pace of change, but you want as well for your own career. You want to be at the cutting edge of how you build. So the incentives are really aligned between what you need for your own career and what the organization needs you to do. So there's that permission to go and do it for me is ideally kind of a tailwind in what they want to do more than anything else.

Lenny Rachitsky (00:52:46):
Maybe a last question for people that are inspired and like, "Okay, this is what we need to be doing," any just tips for someone starting down this road to be successful at trying something like this at their company?

Tomer Cohen (00:52:58):
I would say I would start with the notion of how do you want to bring this just structure. I would think about the platform you need to build, the tools you want to bring, and then I would spend a lot of time on the culture. Platform and tools I think would be, again, a prerequisite, but not sufficient, and the cultural aspect is really important. I would think a lot about how you bring people along. So for one of the learnings we had that probably able to do it differently right now, if I were to redo this program was, for a while I was working very closely with my core team on it, the core kind of full stack building team that were in charge of building all this material, but the organization was always asking questions. "What's going on? Who is doing it? What are the tools?" And in retrospect, we could have done a lot more in the flow to just show them and get them to already use early tools or be aware of it versus doing a small team on the side.

(00:53:49):
So it's okay to start with a small team. I think it's really important. But at the same time, just making sure there's visibility across the whole thing is really powerful. Being patient and being willing to invest. I always give this example of, we always give this example of like, "Oh, look at this startup. They built this in a week." Yes, you can build lifestyle in a week right now if you start from scratch. It's actually not hard. But when you are trying to transform a large organization, you want to have this impatient about the goal and you have to have a high ambition, but being very thoughtful and patient about how you bring it to life and the key things you have to invest in. If you don't invest in your platform, I just don't see how this could be a successful outcome. If you don't invest in customizing the tools for you, then you're just going to get vanilla generic agents from the outside.

(00:54:39):
So being aware of the investment and making sure you actually allocate resource to it, this is kind of the classic, be willing to invest upfront so you can reap the benefit after, versus saying, "Hey, why am I not seeing us moving into 2X the productivity in a week?" That's not going to be this way. You can see it with some people, but starting to collect those examples and starting to really think about the transformation is really key.

Lenny Rachitsky (00:55:05):
This is so incredibly cool. I know that a lot of CPOs and heads of product and all kinds of leaders are reaching out to you trying to figure out what you've learned how to do this. So I love that we went deep on all these things. Just final question, is there anything else that we haven't shared that you think might be helpful for listeners to hear or maybe just to double down on before we get to our very exciting lightning round?

Tomer Cohen (00:55:26):
Whether you're in an organization, you're waiting for your leader to roll this out or you're a leader trying to roll this out, I would not wait. The first thing I've done, which I thought in retrospect was very hopeful is I did announce this upfront we are going to this mode. We're starting in pockets, we're starting in pods, we're building the tools, but this is the mountain we're going to go after, and in many ways, we're going to make it great. I also announced that this is not just an end state, it's a kind of continuous progress. There's no state we're going to get to as much as continuously just trying to be better. And in many ways, to compete, you just want to be better than others in how you build because the version of building will completely just transform itself every few years or so.

(00:56:13):
So do not wait. Really focus on the progress you're making, over communicate with your team, not just the vision, but also the progress you're making, almost like holding yourself responsible. If you're a leader, give yourself KPIs you share with your own teams or OKRs. And if you're inside of the organization, and I would say whether or not or not your CPO or your CEO is announcing this type of program, go do it or join an organization that does it so you can be at the cutting edge of how you build in the future.

Lenny Rachitsky (00:56:43):
Tomer, with that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Tomer Cohen (00:56:48):
I'm ready.

Lenny Rachitsky (00:56:49):
First question, what are two or three books you find yourself recommending most to other people?

Tomer Cohen (00:56:54):
I love to give trios of books that I really like. So my current trio is, they're very diverse in topics, so apologies if it's not falling all into tech. But the first one is called Why Nations Fail. It's a book I read a decade ago even more and the authors of it just won the Nobel Prize last year. And it basically talks about why does some nations succeed and some fail? And it's not the usual explanations we go for, which is, oh, it's culture, it's natural resources, it's the kind of religion. A lot of those tends to be the kind of immediate excuses people have. It kind of falls into two camps. Are there extractive or inclusive institutions? Can people participate broadly and opportunities shared or there are institutions that basically are supposed to be attracting from many and give to some.

(00:57:48):
So it's just an incredible way to just think about how you build a nation. And for us at LinkedIn, we think a lot about the idea of opportunities, so how you build a product as well. And it's just a good way to move away from easy explanations into what really makes a country really successful as well. Second book, it's called Outlive. It's really about the idea, it's kind of like the author, Peter Attia talks about the idea of medicine 3.0, which is really the notion of building personalized medicine, which I think in the world of AI will become incredible in the future. But it's all those, let's call those categories that you should think about for your life so you can just optimize your health as much as possible and goes for everything through fitness to diet to the biggest health factors you should think about. But it's a great long book. Then lastly-

Lenny Rachitsky (00:58:41):
The one in my bookshelf behind me.

Tomer Cohen (00:58:42):
There you go.

Lenny Rachitsky (00:58:43):
It's up top. You can't actually see it, I think.

Tomer Cohen (00:58:47):
And then lastly, it's a book that also came out many years ago, but it's called The Beginning of Infinity, which I really like, by Deutsche. It wasn't an easy read for me, but I love the idea. In fact, especially in products, I love the idea of cause and effect, like really finding great explanations for why things happen and then building on top of that your next iterations. And this book really pushes on the idea of explanations that only once we have a clear understanding of what things happens, then we can have breakthroughs on top of that. But until we get to a point of clear scientific breakthroughs, we are not going to make significant progress. But when you do that, it's really almost like infinite progress you can make on top of that.

Lenny Rachitsky (00:59:33):
Naval's always talking about that last book. I think I bought it and it was just hard reading this.

Tomer Cohen (00:59:39):
It's not an easy read, at least for me. It wasn't an easy read, but it's a very powerful read.

Lenny Rachitsky (00:59:41):
Awesome. Is there a favorite recent movie or TV show you really enjoyed?

Tomer Cohen (00:59:46):
Can I do a podcast?

Lenny Rachitsky (00:59:48):
Absolutely.

Tomer Cohen (00:59:50):
So there's a podcast in, it's in Hebrew, it's called One Song, and it takes a song that generally is ideally popular and then goes really deep on the origin and the history of the song, and I love it. I love music and just dissects songs so well. It does a great job also in bringing to life the story behind it. So for me, it just goes back to you thought the song was about something, but then it goes really deep into the actors behind the song, and sometimes it's the words chosen or it's how the lyrics match the music itself, and I just really enjoy that one.

Lenny Rachitsky (01:00:30):
There's a podcast called Song Exploder, I believe, that is a similar concept that's not in Hebrew, in English, that I'll point people to if you love that one.

Tomer Cohen (01:00:39):
That's awesome.

Lenny Rachitsky (01:00:40):
Is there a product you've recently discovered that you really love? Could be an app, could be some clothing, could be a kitchen gadget, type gadget.

Tomer Cohen (01:00:48):
Can it can be a product I want to have, which I think is actually really easy to do?

Lenny Rachitsky (01:00:53):
I love that. This is a product thinking 101 and just the vision of what you want to see.

Tomer Cohen (01:00:58):
So in my car right now, there's Alexa built-in, which is great because the kids can ask for songs all day long and it's a whole show inside of the car. But one of my favorite things to do when this has been doing it for well over two years is I go in and I go into voice mode.

Lenny Rachitsky (01:01:17):
ChatGPT.

Tomer Cohen (01:01:18):
Yeah, ChatGPT, and then just have a conversation, and that's just friction. I would love to have on my steering wheel a button that invokes my AI friend that can sit next to me in the passenger seat, and I just think that would be such a... I actually think it would [inaudible 01:01:36] rides for people. Just that movement, that's just like elimination of friction will transform the experience for me.

Lenny Rachitsky (01:01:43):
On that note, I recently discovered Teslas actually do this now. If you hold the right wheel, Grok appears and you could talk to Grok. So it's here. The AI has arrived. Yeah. I just did it by accident and then it's, "Okay, cool."

Tomer Cohen (01:02:01):
Great. So for me, if anybody from Rivian is listening, please bring this in the car.

Lenny Rachitsky (01:02:06):
Rivian's falling behind. Yeah. And you have to use Grok. It'd be cool if you could switch to different AIs because it has a personality. Just give me information. I don't need you to laugh and give me jokes.

Tomer Cohen (01:02:20):
Did you need to spend some time with it before or did it have any memory from... Did you bring any memory into it?

Lenny Rachitsky (01:02:27):
There's a logged out version and then you could just log in and it connects to your account. Yeah, it's extremely cool. No one's talking about it. It's crazy because I don't know if they launched it fully, but it just appeared.

Tomer Cohen (01:02:38):
Do you talk in the car a lot to it?

Lenny Rachitsky (01:02:41):
I don't use it that much, to be honest, but I should. My wife just doesn't love Grok. I think the brand of Grok is a specific brand. And so she's like, "Don't talk to Grok in here with me."

Tomer Cohen (01:02:52):
I love voice mode, so I use it all the time.

Lenny Rachitsky (01:02:55):
Yeah, I love voice mode too. It just interrupts too often. That's the issue there, right? It's just it stops.

Tomer Cohen (01:02:59):
By the way, you can set it up. You can basically say like, "Hey, just let me finish."

Lenny Rachitsky (01:03:03):
I now know that. I'm learning so much. Okay. Two more questions. Do you have a life motto that you often find useful in work or in life?

Tomer Cohen (01:03:11):
I think last time I talked about it, I most associated here with, I might be wrong, but I'm not confused, although I don't say it as much anymore. But I think the one I love, growth mindset is a second religions for us at home. And one thing I love about, there's a phrase there that is becoming is better than being, which I think ties into the FSB mode a little bit, which is you're always in progress mode, iteration mode. It's not about reaching a state. It's about the journey, the process. That's what you should fall in love with. It's about continuously growing and evolving without the negativity of it or there's no sense of FOMO there. It's just this continuous thing. If I look back a year from now and I look back, how much did I grow? How much do I know? What skills to do that again? Where are I becoming better? Do I feel like Tomer version 2026 versus 2025? What's the delta there? And I kind of love that as a way of thinking.

Lenny Rachitsky (01:04:13):
A great segue to our final question. By the time this episode comes out, it won't be a secret that you're leaving LinkedIn after 14 years. Legendary run. You joined way before the acquisition, you helped them integrate. Just like the way LinkedIn was perceived 14 years ago is so radically different from the way it is today. It's actually really fun and interesting to be there versus how people for a long time felt about LinkedIn. So I guess the question just how you feeling and what's next? I imagine you're going to get a lot of calls from a lot of people, but what are you planning?

Tomer Cohen (01:04:48):
Yeah, so I feel proud. It's been an incredible ride at LinkedIn. The way I've got to know about LinkedIn deeply the very first time was when I moved to the Valley and I went to a lecture at Stanford about social networks in 2008 and Reid was there and he talked about the power of being a professional communities online, and I was very nerdy about it and thought it was incredible vision, had no plans to join and actually started my own company after. But as luck would have it, found myself joining a few years after and just thought the mission was incredible. So in many ways it aligned with my purpose and just was an incredible ride to be here.

(01:05:32):
And I also feel very grateful. I shared this with the company recently. I was starting to take learnings from my experiences here. A lot of it was from tough situations. We had a lot of tough situations at LinkedIn and hard calls and late nights, but you learn so much from those and I'm just incredibly grateful. And I'm excited. I'm excited. I have a bias for change. I have a bias for kind of positioning myself in a place where I can learn the most and learn a lot. And it's an incredible time to build, so I'm just excited to be thinking of new problem sets and new areas where I can go deep on and invest the next decade in.

Lenny Rachitsky (01:06:13):
I think it's going to take a long time for you to not feel like you're working on LinkedIn and to forget about all the things that you have been worrying about for so many years.

Tomer Cohen (01:06:20):
After you build something for such a long time, and I think you and I talked about it at one point, that I think one of the best traits for a builder is to become very passionate with what they're building. Really care. Not about the job. It's really care about the product. When you feel the pain when somebody complains and you kind of have this continuous discontent, and it's like for me, it's the notion of raising a baby. So yeah, it's hard. It will be hard. I will always think of LinkedIn as one of the babies I helped grow.

Lenny Rachitsky (01:06:53):
Well, I'm excited to have you back someday when you figure out what you want to do next and or start whatever you're doing. I love that this was an excuse to get to know you. Tomer, thank you so much for being here.

Tomer Cohen (01:07:03):
It was great to be here. Thanks, Lenny.

Lenny Rachitsky (01:07:04):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

