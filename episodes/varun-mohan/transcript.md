---
guest: Varun Mohan
title: 'Building a magical AI code editor used by over 1m developers in 4 months:
  Inside Windsurf'
youtube_url: https://www.youtube.com/watch?v=5Z0RCxDZdrE
video_id: 5Z0RCxDZdrE
description: Varun Mohan is the co-founder and CEO of Windsurf (formerly Codeium),
  an AI-powered development environment (IDE) that has been used by over 1 million
  developers.
duration_seconds: 4446.0
duration: '1:14:06'
view_count: 63559
channel: Lenny's Podcast
keywords:
- growth
- okrs
- roadmap
- prioritization
- revenue
- hiring
- culture
- management
- strategy
- vision
- mission
- differentiation
- market
- persona
- design
---

# Building a magical AI code editor used by over 1m developers in 4 months: Inside Windsurf

## Transcript

Varun Mohan (00:00:00):
A lot of the bets we're making inside the company are for things that are not three, four weeks away. We should be cannibalizing the existing state of our product every six to 12 months. Every six to 12 months, it should make our existing product look silly. It should almost make the form factor of existing product look dumb.

Lenny Rachitsky (00:00:13):
How do you know when it's time to hire someone?

Varun Mohan (00:00:16):
I want the company to almost be like this dehydrated entity. Every hire is like a little bit of water, and we only go back and hire someone when we're back to being dehydrated.

Lenny Rachitsky (00:00:24):
Any other there skills you think people should be investing more in with the rise of AI building more and more of our products?

Varun Mohan (00:00:29):
The engineers are now able to produce more technology. The ROI of building technology has actually gone up. This actually means you hire more. The best thing to do is just get your hands dirty with all of these products. You could be a force multiplier to your organization in ways in which they never even anticipated.

Lenny Rachitsky (00:00:47):
Today my guest is Varun Mohan. Varun is the co-founder and CEO of Windsurf, which has quickly become one of people's favorite AI coding tools, and is basically the main competitor to Cursor with over 1 million users four months in. In our conversation, Varun shares what makes Windsurf unique, why they decided to invest heavily in enterprise sales very early in their history, why agency is going to be the most important skill for engineers and product builders to build, also the story of how they started out as a GPU infrastructure company and realized there was a much bigger opportunity up the stack and the two pivots that got them to where they're today.

(00:01:20):
He also gives a live demo, advice for being successful at Windsurf, and so much more. There's so much to learn about where things are heading for engineers and product builders in general in this conversation. And I'm really excited to bring it to you.

(00:01:32):
Thank you to everyone on LinkedIn and Twitter and my newsletter community for suggesting great questions to dig into with Varun. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you get a year free of Perplexity Pro, Notion Plus, Linear, Granola, and Superhuman. Check it out at lennysnewsletter.com. With that, I bring you Varun Mohan.

(00:01:59):
This episode is brought to you by Brex, the financial stack used by one in every three US venture-backed startups. Brex knows that nearly 40% of startups fail because they run out of cash. So they built a banking experience that focuses on helping founders get more from every dollar. It's a stark difference from traditional banking options that leave a startup's cash sitting idle while chipping away at it with fees. To help founders protect cash and extend runway, Brex combined the best things about checking, treasury, and FDIC insurance in one powerhouse account. You can send and receive money worldwide at lightning speed. You can get 20X the standard FDIC protection through program banks. And you can earn industry-leading yield from your first dollar while still being able to access your funds anytime. To learn more, check out Brex at brex.com/banking-solutions. That's B-R-E-X, .com/banking-solutions.

(00:02:57):
This episode is brought to you by Productboard, the leading product management platform for the enterprise. For over 10 years, Productboard has helped customer-centric organizations like Zoom, Salesforce, and Autodesk build the right products faster. And as an end-end platform, Productboard seamlessly supports all stages of the product development lifecycle, from gathering customer insights to planning a roadmap, to aligning stakeholders, to earning customer buy-in, all with a single source of truth. And now, product leaders can get even more visibility into customer needs with Productboard Pulse, a new voice of customer solution. Built-in intelligence helps you analyze trends across all of your feedback and then dive deeper by asking AI your follow-up questions. See how Productboard can help your team deliver higher-impact products that solve real customer needs and advance your business goals. For special offer and free 15-day trial visit productboard.com/lenny. That's Productboard.com/L-E-N-N-Y.

(00:04:00):
Varun, thank you so much for being here and welcome to the podcast.

Varun Mohan (00:04:03):
Buddy, thanks for having me. A long time listener.

Lenny Rachitsky (00:04:05):
Oh, I really appreciate that. I'm so excited to have you here. I feel like just you guys have become this overnight success, which is definitely not an overnight success, but I feel like I've been hearing about Windsurf more and more as people's favorite AI tool. And I just don't think people know the story behind Windsurf, behind Codeium, the company that you built. So I thought it'd be good to maybe just start there and have you just briefly share the history of Codeium and how Windsurf emerged out of Codeium.

Varun Mohan (00:04:31):
Yeah. So the company was actually started close to four years ago. As you know, AI coding was not a thing four years ago. ChatGPT was not out four years ago. At the time, we actually started out building GPU virtualization and compiler software. Before this, I worked in autonomous vehicles. My co-founder, who I had known since middle school, worked on AR/VR at Meta. And for us, we believe deep learning would touch many, many industries. It wouldn't just touch autonomous vehicles. It would touch financial services, defense, healthcare. And we believe these applications were hard to build, these deep learning applications. So we made it possible for you to effectively run these complex applications on computers without GPUs, and we would handle all the complexity of being able to actually run the workload on the GPUs for you. And we were able to optimize these workloads a ton.

(00:05:20):
And in the middle of 2022 rolled around and we had a couple million in revenue and we were managing upwards of 10,000 sort of GPUs. We had eight people. At the time, we were free cash flow positive. But I think what we felt was once these generative models started to get very good, we sort of felt a lot of what we built was not as valuable. And this was a very, very hard moment for us at the company. We were only eight people at the time, but we felt, "Hey, would people be training these very bespoke sentiment classifier models anymore that were very, very custom models? Or would they just ask GPT-N, is this a positive or a negative sentiment?" Probably it's going to be the latter, right? And in a world in which everyone was going to run generative AI models, why would an infrastructure company be a differentiator? Because everyone is going to run the same kind of infrastructure down the line.

(00:06:06):
So instead what we decided to do was we believe generative AI was almost going to be like the next internet. And in that case, what we should go out and do is build the next great apps like Google, like Amazon. And we vertically integrated and actually took our infrastructure, our inference infrastructure to go out and build Codeium at the time. And at that time, we were early adopters of GitHub Copilot and we thought the coding space was going to get tremendously disrupted in the next coming years. So we actually took our infrastructure, we ran our own models in massive scale. We even trained our own models.

(00:06:35):
In the very beginning it was very, very simple. It was purely an autocomplete model, which basically means that as the user was typing, we'd complete the next one or two or three or four lines of code. But we provided the product entirely for free in all the IDEs that developers coded. That meant to VSCode, JetBrains, Eclipse, Visual Studio, Vim, Emacs. And the reason why we were able to build it for free was because of our infrastructure background. We were able to optimize these workloads a ton.

(00:07:04):
I guess very quickly after that, some large businesses also wanted to work with us. And we built out this enterprise motion to work with these large companies like Dell, JPMorgan Chase. And for them the bigger thing wasn't just, "Hey, could we autocomplete code or could we chat with the code base?" It was, "Could you offer us a secure offering that was also personalized to all the private data inside the company?" So we took our infrastructure and made it so that we invested a ton in making sure that we deeply understood these large companies code bases. And that's what we were working on until six months ago.

(00:07:33):
It's not that we've stopped working on that, but basically what we realized six months ago was we were getting limited by the IDEs that we were already working in. So VSCode, which is a very popular IDE, had a ceiling for the AI capabilities, we could showcase our users. And because of that, we decided to go out and fork VSCode and build our own IDE with some of these new agentic capabilities. And over time in the last couple of years, the model capabilities have also been growing exponentially year over year. And that's sort of where we are right now. I skipped a lot of pieces there, but that's what we're landed.

Lenny Rachitsky (00:08:05):
There's so many interesting threads there. One is just, there's always this question of just where value will accrue in AI. And it's so interesting, you guys started almost at the bottom layer of infrastructure GPUs and then you went to what people call a GPT wrapper, not actually. So I guess any just lessons there, just thoughts on just where you think value will end up in this world of AI and the stack of AI tools?

Varun Mohan (00:08:28):
Maybe I can start by just saying one thing about startups that I think are really true, it's very unlikely the first thing that you believe you should go work on is going to be the right thing, which is a very hard thing to kind of wrangle with being a startup founder, right? You need to kind of be irrationally optimistic that what you're going to do is going to be differentially important. Because otherwise, why would you go out and do what you're doing? And if it's obvious, then a bigger company would've already done it, right?

(00:08:56):
But then you also need to be really, really realistic because most ideas that are, I guess, non-conventional are usually bad ideas, right? So it's this weird tightrope you need to kind of balance on top of where you're pushing for a future that you believe is true, but all the while you're getting new information. You need to kill the beliefs that you had. And if I were to start with the infrastructure piece, we first went in with the assumption that model architectures were going to be really, really heterogeneous.

(00:09:27):
Working from an autonomous vehicle background, there were many different types of model architectures out there. There were convolutional neural networks, graph neural networks, recurrent neural networks, LSTMs, sort of lighter neural nets with frustrum point networks. And there were maybe tens of architectures we were dealing with. And at that point we were like, the complexity of this is so high that it's very clear if someone offloaded the complexity, there would be a lot of value.

(00:09:50):
Fast-forward to the middle of 2023, everything looks like it's going to be a transformer. So now our hypotheses are just wrong. So at this point then, most of the value is probably not going to accrue at purely the, at least this is our belief, at the infrastructure layer. It's going to accrue somewhere else. Where is the layer that you can actually differentiate on? And we believe the application layer is a very, very deep layer to go out and differentiate on, right? What are the number of ways we can build better user experiences and better workflows for developers? We think there's effectively no ceiling on that, on how much better we can make the lives of developers basically.

Lenny Rachitsky (00:10:22):
You touched on the second thread that I thought was really interesting here, is just how you guys pivoted from ideas that were working. You were making money, people loved it. You said you had millions of dollars of ARR revenue. And then you're just like, "No, we're going to completely change the business."

(00:10:36):
So the question there is, just like, what have you learned about knowing what to follow? And one thing I heard there that was really interesting is just once your assumptions change about that you built your idea on, it's time to think this idea and maybe try something else.

Varun Mohan (00:10:48):
I think the way we sort of think about this is even when we're working right now, we just accept that we're going to get a lot of things wrong. We're just going to get a lot of things wrong. Obviously that's a very big moment because that was a bet the company moment in the sense that we basically said, told our investors, "Hey, we're making money on this." We had already raised 28 million of capital and we were just like, "Hey, we're just going to pivot entirely from this." And we did that overnight. This wasn't this thing where we just said, "Hey, maybe a quarter, one or two quarters." Because one of the things we knew that's very important for startups is focus.

(00:11:20):
If you're trying to do another thing that you think is big and you're focused on something that you don't believe is valuable, you're guaranteed going to fail at the thing you think is going to be big. So that's a very obvious thing there. But I think once you go in with the assumption that a lot of your hypotheses are going to be wrong, but you will do the most concentrated work possible to go out and validate these hypotheses and you won't be in love with your ideas.

(00:11:41):
I think ideas, it's awesome when you have a great idea, but you should never be too in love with your ideas. And you have an organization that is very truth-seeking. I think a lot of people at the company have had their ideas tested over and over again. Even just building Windsurf. That is not a complete company pivot, but that's a big decision that we made at the company. You kind of need to make some bets. And sometimes you're wrong and sometimes you're right. But if you have an organization that comes out and you feel like morale is not going to be low if you made the wrong decision, that's the best, right? That means you have optionality for the rest of time.

(00:12:14):
And Lenny, one thing that I try to tell the company about this is, this year the total amount of engineering output we'll have is much larger than the engineering output we've had since the beginning of the company's creation 'till now. So that almost means every year is a new lease on life for us, right? It's almost a new way for us to test out an entirely new set of hypotheses. And maybe we were wrong about our original hypotheses in the first place. What makes us more smart than everyone else to be right more times than that?

Lenny Rachitsky (00:12:46):
That's so empowering. It makes me think about... Uri Levine was on the podcast, co-founder of Waze, and he has this phrase that he wears on his shirt. His book is called this Fall in Love with the Problem, Not the Solution. And that feels like that's exactly what you're describing.

(00:12:59):
Okay, so let's talk about Windsurf. What's the simplest way for people to understand what is Windsurf?

Varun Mohan (00:13:04):
Yeah. So Windsurf is an IDE, right? It's an application to go out and build software and build applications. The crazy thing is a lot of people who use the product don't even probably know what an IDE is, which is crazy. And we'll get into that in a second.

(00:13:22):
But why did we go out and build Windsurf and what is Windsurf maybe? Why couldn't we have just done this on top of conventional IDEs like Visual Studio Code? So maybe just to get into this a little bit, as we saw that AI was getting more and more powerful, the way people go out and build technology, we thought the interface for that was going to change remarkably. It was not going to be a conventional pure text editor where the user is writing a handful of lines of code or most of the code and the IDE provides maybe some basic feedback on what the user is doing right or wrong. And the basic feedback could be, "Hey, there's a bug in your software or compiler error in your software." It could do much more, right? It could actually go out and modify large chunks of code.

(00:14:04):
One of the key pieces that we recognized was, with this new paradigm with AI, AI was probably going to write well over 90% of the software, in which case the role of a developer and what they're doing in the IDE is maybe reviewing code. Maybe it's actually a little bit different than what it is in the past. And we'll see this very soon with Windsurf. Maybe when you're using the product, actually a good chunk of the user's time is that you're reviewing what the AI is outputting. So we needed to build custom-review flows into the IDE to actually make it so that it was easier to actually go out and do that, right? Because the developer is not spending all their time writing code.

(00:14:38):
And this is the fundamental premise on why we built the product. We thought we were going to get limited a ton if we had very, very basic UI out there. And I'll give you even a simple example here. We have this auto-complete product that completes a handful of lines of code. Now we've actually launched this offering called Windsurf Tab that basically shows you refactors as well. And these refactors are almost inline refactors. And we were able to build a custom UI for that in Windsurf.

(00:15:03):
But in VSCode, because of the access to the APIs, we needed to dynamically generate images right alongside the user's cursor because we just didn't have access to the capabilities to showcase and edit properly. And what we realized is immediately by porting over to Windsurf, our acceptance rate tripled. Same ML models, it just tripled. So what that, I guess, gave us confidence in is yeah, you could argue technology is very important. And I think technology is very important. But if our users are getting very little value from the technology we're sort of building, you need to really clarify, "Maybe we do need to build a new surface and interface." And that's what Windsurf is.

Lenny Rachitsky (00:15:39):
So the big bet you took there just to make this super clear, is you were initially working within existing IDEs that everyone was familiar with. And then it was like, "This isn't going to get us where we need to go. We're going to try to convince people to switch to something completely new because it's going to be so much better. It's our own IDE."

(00:15:56):
I think maybe people may not recognize just how risky that is, convincing engineers to use something completely new. That's a huge deal.

Varun Mohan (00:16:02):
Yeah, no, of course. And one of the key pieces, maybe Lenny, that would be important to share is a lot of our developers do use Visual Studio Code. But there are lots of people that write in languages like Java, sort of C++ and so on and so forth, and they might use the JetBrains family of IDEs that like IntelliJ. And for us, we are actually still committed to building on those platforms, right? We just felt though that one of the dominant IDEs, which was Visual Studio Code, was limiting the sort of user interface that we could give to our actual customers.

Lenny Rachitsky (00:16:35):
What is the current state of traction for Windsurf? You hear all these crazy numbers about all the competitors in your space. What can you share there for folks just to know?

Varun Mohan (00:16:43):
Yeah, so maybe a handful. We launched the product a bit over four months ago. And in that period of time, over a million developers have tried the product. And obviously we have many hundreds of thousands of monthly active users right now.

Lenny Rachitsky (00:16:54):
I love how these days like, "oh, a million. Oh, no big deal." It's just the numbers are absurd these days. We're just getting used to just 100 million ARR here, million users in four months there. It's just like, "Oh, of course. How could you not have that?" But that's absurd. It's just like an insane time right now.

(00:17:12):
You touched on something that I wanted to get to later, but I may as well bring it up now, the question of just how engineering will change in the future. You throw out the stat that 90% of code is going to be written by AI in the future. Dario from Anthropic recently said the same thing. You guys have a really interesting glimpse into just how things will look in the future.

(00:17:31):
So I guess the question is just, how do you think coding specifically will look in the next few years, how different will it be from today?

Varun Mohan (00:17:39):
I think when we think about what is an engineer actually doing, it probably falls into three buckets, right? What should I solve for? How should I solve it? And then solving it. I guess everyone who's working in this space is probably increasingly convinced that solving it, which is just the pure, "I know how I'm going to do it" and just going and doing it. AI is going to handle vast majority, if not all of it. In fact, it probably actually, with some of the work that we've done in terms of deeply understanding code bases, how should I solve it is also going to get closer and closer to getting done. If you deeply understand the environment inside an organization, if you deeply understand the code base, how you should solve it, given best practices when the company also gets solved.

(00:18:19):
So I think what engineering kind of goes to is actually what you wanted engineers to do in the first place, which is, what are the most important business problems that we do need to solve? What are the most important capabilities that we need our application, our product to have? And actually going and prioritizing those and actually going and making the right technical decisions to go out and doing it. And I think that's where engineering is probably heading towards.

(00:18:40):
Now, does that mean that no one needs a CS degree? I think that's maybe a little bit overplayed a little bit just because maybe here's my argument for that. A lot of developers nowadays that build full stack applications, at least until a handful of years ago, they probably went to college and took an operating system course. And in theory, they're not really playing around with the operating system, like the kernel scheduler very frequently. But do those principles help them in understanding why their applications are slow? Do they help them in understanding why some design decisions are better than the other? Yeah, that makes them a much better engineer than another engineer. And I think that idea and the understanding of what's going on at the bottom will make a good engineer even better. But also at the same time, it empowers a bunch of people that never understood all of those things, how to actually build as well, which is another remarkable sort of thing that fell out through this whole process.

Lenny Rachitsky (00:19:33):
I don't know if you have kids, but just say you had kids or you had niece or nephew going into college, let's say, would you suggest they do do computer science or would you suggest you're not going to have a good time if that's the career you choose right now?

Varun Mohan (00:19:47):
Yeah. Maybe I think back a little bit. So I went to MIT. A lot of us at the company went to MIT together on the engineering team. I think when I think about what we learned the most for engineering or computer science, it was not exactly like how do you write code. That is almost a given that you can write code after going to college. It's more like the principles of how you think about a problem and how you break it down and how you solve it in an interesting way.

(00:20:15):
So an example of a class that I really enjoyed was our distributed systems class. And there, you're kind of reading through literature and understanding how some design decisions were kind of made. And I think it's more like a problem solving kind of course and a major. It's a major of how you solve problems given some constraints of how computers today function, right? Like, here's the speed at which memory sort of operates. Here's the speed at which... Here's how much computation you can do in one cycle or one second. And based on that, you can make some trade-offs and solve a problem.

(00:20:45):
So I don't know if I would say that you shouldn't go get a computer science degree. I think computer science is almost synonymous with problem solving. In that case, I think it's pretty valuable. Is everything you learn in your computer science degree useful? I'd say a lot of things that I learned in my computer science degree are not useful. I'll give you an example. I took a parallel computing class in Julia. I don't think Julia is a very popular programming language anymore. Am I very sad that I took the class? No. The principles of parallel computing are still very useful, I would say, today.

Lenny Rachitsky (00:21:12):
So what I'm hearing is, skills that you still want to build, whether it's computer science or maybe some version of computer science, is kind of building the mental model of how computers and systems work.

Varun Mohan (00:21:12):
That's right.

Lenny Rachitsky (00:21:23):
Parallel processing, memory, hard drives, internet, things like that. And then there's just problem solving skills, being able to solve interesting problems. Is there any other skills you think people should be investing more in with the rise of AI building more and more of our products?

Varun Mohan (00:21:37):
I think one of the things that's maybe a little bit undervalued is this kind of agency piece. And I think about this a lot, which is, you have a lot of people that could go through college and go through school and they're basically told exactly what to do on a P-set. They're given these very, very, I would say, well-defined paths that they need to take. I think maybe in society and just school, we don't prioritize how do you make sure you get people with real agency that want to build something, right? Their goal is not just to maybe graduate from college and then get a job at a big tech company where they're told exactly what to do or where to put the pixel for this one website. I think that's maybe a skill set that is undervalued just right now, probably in the last maybe 10 years or so. And I think that's going to be really, really important.

(00:22:27):
For a startup, obviously these are skills that we just look for. We look for people that are really high agency because we just recognize that by default, if we don't innovate and do crazy things, we're going to die. The company is just going to die. So we just look for this, right? But I would say for most software engineering jobs, that's probably not the case. Just think about big company X and what they're hiring for on the average software engineering interview. It probably doesn't look like that.

Lenny Rachitsky (00:22:52):
I love how you phrased that. If we don't do crazy things and innovate, we're going to die. That would be a great title for this podcast episode. And I think, I know, it's 100% true. There's just a lot of crazy things happening and a lot of innovation happening. And if you can't keep up, you'll die.

(00:23:07):
So let's talk about hiring. You have a really interesting approach to hiring. There's a few questions I have here. One is just how do you... I know you try to stay really lean. That's a common theme across all the AI startups these days. How do you know when it's time to hire someone?

Varun Mohan (00:23:22):
I love the idea of being a lean company, but I don't idolize it in the way that, "Hey, it is a dream to be a 10% or 20% company that's making 50, 100, 200 million in revenue." That's not, I think, what we idolize inside the company.

(00:23:36):
I think what we idolize is, be the smallest company we can be to satisfy our ambitions. That's what the goal is. And maybe, Lenny, the way I would sort of put that out there is, if I told you, "Hey, I'm going to build an autonomous vehicle," and I said our team is 10 people, you should rightfully say, "Hey Varun, you're not serious. And you'd be right. I'm not serious at that point. So I think the answer is, what is the minimum number of people to go out and build the crazy ambition project that you have?

(00:24:04):
And I think the project we are trying to go out and do, which is completely transform the way software gets built, we've mentioned this [inaudible 00:24:11] the company, our goal is to reduce the time it takes to build apps and technology by 99%, right? It is a tremendously sort of ambitious goal. And it's not possible for us to be a 10, 20, 30, 40 person engineering team in the long term and actually satisfy that goal. We think there's a very, very high ceiling. So that's maybe the first key piece there. It's like, if we can crack actually being a fairly sizable company but still operate as if we're a startup, that's the dream. That's the dream.

(00:24:40):
In terms of hiring philosophy, the way we sort of think about things is, we only hire for a role if we're actually underwater for that function. So let's say we're going out and building inference technology. Unless we're underwater there, we will not go out and hire someone to go out and work for that. And the reason for that is, I actually think this is a feature. When you hire for a role and you already have enough people there, you get a lot of weird politics that ultimately ends up happening. And it's not because people are bad people. I think most people are really well-intentioned. But what happens when you have people that join a company and in reality you didn't really need them? They will go out and manufacture some other thing that they should go work on. They will go out and figure out something else to work on. And realistically, it's not that important, but they will go out and try to convince the rest of the organization that it is important.

(00:25:30):
I just think as a startup, we don't have the bandwidth to go out and deal with that, right? For me, I would like to see everyone just almost be raising their hands up being like, "I'm dying. We need one more person." And that's when we go out and hire someone. And one of the analogies I like to give is, I want the company to almost be this dehydrated entity and every hire is like a little bit of water. And we only go back and hire someone when we're back to being dehydrated.

Lenny Rachitsky (00:25:57):
I love this metaphor so much. And it sounds painful. It sounds painful that you need to be underwater and raising your hand, "I'm about to die and dehydrated." But I also know that it's a really exciting way to work. It sounds hard, but if you're in it, it's just like... I guess talk about just that side of it because I think it could sound like, "This is terrible. I don't want to work this way."

Varun Mohan (00:26:19):
You know what I actually think, Lenny? It's really good for a handful of reasons, which is that a lot of the... We respect and trust the people that work at the company. So this forces ruthless prioritization. You have a team that's going out and doing something. They will never ask to work on something that's not important. In fact, if there are two things that they're working on, they're just going to just tell me, "Hey, there are two things on my plate. I just don't have the ability to do two. I can only do one." And they will pick the one that's most important.

(00:26:45):
And this actually goes back to one thing that I think is true about startups and just companies in general. You don't win by doing 10 things well. You win by doing one thing really well and maybe you fail nine things. This is the thing that I've told the company, "This is very different than school," right? In school you optimize for your total GPA. But for companies, I just need to get an A+ on the one class that matters. And then I can get an F in all the other classes. And an F in all the other classes doesn't mean just doing illegal things. That basically means you just deprioritize things that don't matter. That actually forces this organizational prioritization that is just really, really good.

(00:27:22):
And Douglas and I, Douglas being my co-founder, we can tell the company, "These are the two things that are the most important." But if we go out and tell these are the two things that are the most important to the company and then we put the company has 20% more people than necessary, what's going to ultimately happen? It's almost a forcing function for ruthless prioritization to have fewer people or people that are just underwater internally at the company.

Lenny Rachitsky (00:27:46):
Everyone listening that works at a big company knows exactly what you mean when you described when there's just too many people, they will all find work to do and they will all be pitching ideas. They all want to show impact, they want to do well in their performance reviews. That's just the nature of too many people at a company. And so I think this all really resonates.

(00:28:04):
To even getting even deeper on just what it looks like when someone's underwater to tell you it's time to hire, is it just someone coming to you, "Varun, I need someone on this team. This is just not possible"? What does that look like even more practically?

Varun Mohan (00:28:16):
Yeah, I think it's basically along those lines. It's that, "Hey, there's some pressure to get something done in a short period of time." By the way, one of the things that we do believe though for software, if you want to do great things, it's not possible to just say, "Hey, I want to get it done in one month" if it is like... Because you have to think about it from this perspective. If a software project could get built in two to three weeks, what does that really mean about the true complexity and differentiation of what you built? It's probably not very high, unless you believe you are way smarter than everyone else. But I think that's hubris, right? I think we actually have a very exceptional engineering team. But also at the same time, I don't think our engineering team is so exceptional that we can do things in three weeks that the rest of the world can't do in six to nine months. That's kind of stupid to believe that.

(00:28:57):
So I think basically it comes down to that person coming out and being like, "Hey, look, I don't have enough time to do X." Us having a conversation to be like, "Okay, what can you do then?" And if the answer is, "I can only do less than that," then maybe we make a decision actually, "Oh wow, that's great. Maybe we actually should deprioritize Y." Because this is actually also another thing that's very hard even for people like me and my co-founder. It's that we also want to do a lot of things. There's an urge to do a lot of things. But if we are forced to make a decision constantly on like, "We cannot do X," it's very clarifying. It's very clarifying because our engineering interview process is also extremely low acceptance rate. So it's not very easy for us to very quickly spin up people and have them join the company really, really quickly either.

(00:29:43):
So I think it's clarifying for everyone. It's clarifying for the person that wants more people. We can just tell them, "Hey look, we don't believe you should be doing this other thing." And it's also clarifying for us because we can also get on the same page with them. And sometimes we just kind of agree, "Hey..." Our teams are very flexible that, "Hey, actually we do need to get something done." And one of the things that we've kind of tried to make sure is true on our engineering team is, people's value to the company does not have anything to do with the size of their team. There are projects inside the company, there are directly responsible individuals for these projects inside the company. And if we feel like one project is very important, then people can move from one project to the next.

(00:30:21):
There's no notion of someone owning people at the company. That is a very bad and gnarly idea. In fact, the person that is the most valuable at the company is the person that can do the most crazy sort of project out there with as few people as possible. And that's what you should be rewarding internally.

Lenny Rachitsky (00:30:35):
How many people do you have at coding at this point?

Varun Mohan (00:30:37):
So we have close to 160 people and the engineering team is over 50 people right now.

Lenny Rachitsky (00:30:42):
Awesome. Oh, what's the other bigger functions? So [inaudible 00:30:46]-

Varun Mohan (00:30:46):
We have go-to-market. We have a... Yeah.

Lenny Rachitsky (00:30:48):
Oh, right. Okay. I want to talk about that, the sales learning that you guys had. Okay. But let's close out this hiring conversation. So we talked about what you look for... To tell you it's the time to hire, what do you look for in the people that you interview and hire?

Varun Mohan (00:31:01):
One of the key pieces that we look for, we have a very high technical bar. So assuming that they actually meet the technical bar, I think we sort of look for people that are really, really passionate about the mission of what we're actually trying to solve and people that are willing to work very hard. I think one of the things that we don't try to do is convince people, "Hey look, we are a very chill company and it's great to work here." I think, no, this is a very exciting space. It's very competitive. You should expect us to lose if the people at the company are not kind of... They're not working very hard. And I think one of the biggest dog whistles I hear is, when I ask people how hard are you willing to work, some people actually ultimately say, "Hey, I work very smart." And I basically ask them a question, "If we have many smart people at our company that also work hard, what's the differentiator going to be? Are you just going to pull them down?"

(00:31:48):
Because I think one of the things that's true about companies is it's like this massive group project. And I think the thing about a person that is not pulling their weight that's bad. It's not the productivity, right? At some point when the company becomes many hundreds of engineers, I'm not going to be thinking about the one engineer that's not pulling their weight. It's the team of people they work with that are almost basically saying, "Is this the bar internally at the company? Is this the expectation?" And I guess, Lenny, if I told you you have a team of five people and the four other people you're working with just don't care, how much are you going to feel like you should care?

Lenny Rachitsky (00:32:21):
Not too much.

Varun Mohan (00:32:22):
Exactly. So for us, I think that's what we more care about. We have a culture where it's very collaborative. It's not an individual sport, but people feel like they can rely on other people to get complex sort of tasks done.

Lenny Rachitsky (00:32:35):
So the question you asked there just basically is, how hard are you willing to work? How hard do you want to work? And I know some people, there's this whole group of folks that are just like work-life balance, "How dare you ask me to work crazy hours?" And I love just the filter upfront of, "If you work here, you will work really hard. You'll work a lot of hours. It's a crazy space to be in. And we will win by working smart and also really hard."

Varun Mohan (00:33:02):
Yeah.

Lenny Rachitsky (00:33:03):
You said at some point earlier that your engineering pass rate, as you said, it was like 0.6% of candidates, something like that.

Varun Mohan (00:33:10):
Yeah, it's probably post or take home. It's probably that actually. So the take home itself filters probably another 10, 15X on top of that.

Lenny Rachitsky (00:33:19):
Here's a question that I've been hearing more and more, is just, how do you do interviews these days with tools like Windsurf out there that solve all your problems?

Varun Mohan (00:33:25):
We are okay with people using the tools because I think one of the worst things is like, if someone comes here and doesn't like using these tools, we believe there are massive productivity improvements. We do bring people into the company on site so we can actually see how they think through problems on a whiteboard and all these other pieces. So we do want to see how they think on their feet and hopefully they're not just taking what we're saying, putting it in a voice translator and sticking it into ChatGPT and getting the answer out.

(00:33:51):
So there is a way to do this. My viewpoint on this is the tools are really, really important, but I do think we still look for some problem solving ability. If the only way you can solve a hard problem is put it into ChatGPT, I think that's a concern to us.

Lenny Rachitsky (00:34:07):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast. It's where I put my community resources, it's how I manage my workflows.

(00:34:22):
Here's how Coda can help you. Imagine starting a project at work and your vision is clear, you know exactly who's doing what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs to documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all in one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab.

(00:34:54):
Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's C-O-D-A, .io/lenny to get started for free and get six months of the team plan. coda.io/lenny.

(00:35:24):
Okay. Let's talk about this go-to-market sales experience that you guys had. So you started obviously like most people, started building without sales team. And then you realized, from what I hear, that that was a huge miss and a big opportunity to talk about there because that's really unique, I think, that you guys have a large sales team and go-to-market team.

Varun Mohan (00:35:40):
Yeah, we actually made this decision pretty early in the company's history, I would say. We hired our VP of sales over a year ago actually. And the go-to-market team is now over 80 people inside the company. So it's a pretty sizable function inside the company.

(00:35:55):
Yeah. Maybe a little bit of a backstory here. So when we started the company, actually we had a handful of angels that actually were operators, go-to-market operators. So an example of one was Carlos Delatorre who used to be the CRO of MongoDB. And I think for us, we never viewed enterprise sales and sales as a very negative thing. I think this is a interesting thing that technical founders sometimes don't really like. They think sales is a very negative part of the process. Everything should be product-led growth. I think it's not that black and white. I think enterprise sales is really valuable. But maybe when we were a GPU virtualization company and we were an infrastructure company, the reason why we never hired a salesperson is, I didn't know how to scale the function. I was the one who was selling the product.

(00:36:37):
So ultimately speaking, if it was hard for me to sell the product incrementally, I didn't know how we could make that into a process that we could then go and scale. I didn't know how we could take the revenue of the business from a couple million to hundreds of millions and let alone even tenths. So if I didn't know how to do that, how could I go out and hire someone and make them scale it out?

(00:36:58):
On the other hand, for Codeium, very quickly, a lot of large enterprises reached out to us. And from that alone in the middle of 2023, we started, I guess, me and a handful of other folks at the company started selling the product and we were doing tens of pilots concurrently with large enterprises and we were very quickly able to understand that there was a large enterprise motion that needed to be built in this space. So by the end of 2023, we actually hired our VP of sales. And very quickly after that, scaled our sales team. Yeah, I mean look, if you want to sell to the Fortune 500, it is very hard to do that purely by swiping a credit card.

Lenny Rachitsky (00:37:35):
Let's talk about Cursor. I don't want to spend too much time with competitors, but that's what everyone's always thinking about when they think of you guys. You guys are kind of the leading players, I think, in the space also. There's Copilot, but that's different.

(00:37:46):
So what's the simplest way to understand how you guys are different from Cursor and also just how you think you win in the space long-term?

Varun Mohan (00:37:53):
So I think maybe a handful of things that I could share. So on the product side, I think we've invested a lot in making sure code-based understanding for very large code bases is really high quality. And that's just because of where we started. We worked with some of the worlds are just companies like Dell, JPMorgan Chase. Companies like Dell have singular code bases that are over 100 million lines of code. So being able to understand that really, really quickly to make large scale changes is something that we've spent a lot of time doing. And that requires us actually building our own models that can consume large chunks of their code base in parallel across thousands of GPUs and almost rank them to be able to find out what the most important snippets of code are for any question that are asked about the code base. So we've gone out and built large distributed systems based on our infrastructure background to go ahead and do that. That's maybe one.

Lenny Rachitsky (00:38:38):
Let me actually follow that thread because I think people may underestimate just how big of a deal that is. So when we talk about, we had the founders of Bolt and Lovable on the podcast, so those products, they build something from scratch, they built, they write the code for you. So that versus just loading, say, Windsurf on your million line code base, say, at Airbnb or Uber. Like, understanding what the hell you have and how it works and where to go change things without breaking it is insanely hard. And so what I'm hearing is that's kind of a big differentiator as you guys started there actually. And then Windsurf is now building up that advantage.

Varun Mohan (00:39:15):
That's right. Yeah. So that's a big thing that we spent a lot of time on, which is just understanding what the code base is doing. And actually one of the other things is, what are all the user interactions with respect to the code base? And happy to show that also in a bit here.

Lenny Rachitsky (00:39:31):
Awesome.

Varun Mohan (00:39:31):
The second key piece probably is we're not only tied to Windsurf actually. This is probably a weird statement given even we are talking about Windsurf, which is that actually we're pretty focused on supporting IDEs like JetBrains. JetBrains or IntelliJ has over 70 to 80% of all Java developers coding in JetBrains based IDEs, right? The reason why we don't feel as big a need to almost build a competing product to JetBrains is JetBrains is actually a very sort of extensible product in a way that VSCode is not. VSCode is not very extensible.

(00:40:05):
So I think for us, our goal here is not only just to satisfy a subset of users that can actually switch onto our IDE, but we want to give this agentic sort of experience to every sort of developer out there. And if that means there are Java developers that write in JetBrains, that's fine. We work with a lot of large enterprises that have 10 plus thousand developers where over 50% of the developers are on JetBrains. It's a very large product. And by the way, that company itself is a privately held company that makes many hundreds of millions of dollars a year. So it's a very, very large company. So for us, that's another key piece. We actually want to meet developers sort of where they are. And if they use a different platform, we'll work on that too.

(00:40:42):
The third key piece, and this probably sounds another key piece for enterprises, is we work in a lot of very secure environments. We have FedRAMP compliance, which means we can sell to very large government entities. We have a hybrid mode of actually using the product, which means that all the code that lives that is indexed, it actually lives on the tenant of the user, right? Code is one of the most important pieces of IP for the company. So I think just if you were to look at it from a big company perspective, there are many reasons why over the years of just building an enterprise product, we've handled a lot of complexities that large companies want to see. But that's part of it is because of the history of how we got here in the first place.

Lenny Rachitsky (00:41:21):
Okay, Varun, enough teasing. Let's do a live demo of Windsurf so folks can see what it's like. And then I'm just going to ask you a bunch of questions as we're going through it. So I'll let you pull up a little shared screen where you have Windsurf pulled up.

Varun Mohan (00:41:33):
Great. So some context, this is a very basic React project. There's nothing in it right now. So if you were to open any sort of file, it's the default React app project. I have this basic image here. You can pass Windsurf images of what you'd like the project to look like, of what I would like an Airbnb for dog's website to kind of look like.

Lenny Rachitsky (00:41:55):
Beautiful. Beautiful mock-up by the way. I love that this is like all you need.

Varun Mohan (00:41:59):
This is all you need. This is all you need. So basically what we're going to do is we're going to say, "Hey..." One of the cool parts about Windsurf is it can actually work in an existing project already. So I can basically say, "Hey, change this React app to show an Airbnb for dog's website based on this image and preview it."

(00:42:25):
So now it'll just go out and start executing code, reading through the repository. Obviously, it doesn't know what the current code base actually looks like. And it'll go out and analyze the code base to actually find out the set of changes necessary. So we'll go out and wait and see what it's going to do. But while we're doing that, let's continue the conversation.

Lenny Rachitsky (00:42:45):
Awesome. Okay, so first of all, so you open up Windsurf. You had a boilerplate React project ready to go. And Windsurf had never really seen this code before. You ask it to do stuff on your code base, which is just like, "Change this to Airbnb for dogs using this design." Amazing.

Varun Mohan (00:43:03):
That's right. That's exactly right.

Lenny Rachitsky (00:43:04):
Yeah. Okay, cool. So we'll let it run and we'll talk. Let me ask you this question that I've been asking everyone that comes on that is building a product that helps engineers build products and product managers build products and designers.

(00:43:15):
Say you could sit next to every single new user that opens up Windsurf and whisper a couple tips in their ear to help them be successful with the product. What would be a couple tips you'd share?

Varun Mohan (00:43:25):
Tip number one is just be a little bit patient and both patient and explicit. When you ask the application to go out and make some changes, it could actually go out and make many irrelevant changes. One of the things that I think prevents this the most is just be really, really explicit or as explicit as possible. And one of the things I ask people to do is in the beginning, start by making smaller changes. If there's a very large directory, don't go out and make it refactor the entire directory because then if it's wrong, it's going to basically it destroy 20 files.

(00:44:00):
And I think from there, one of the key pieces I think that comes from the users that use the product is they sort of learn what the hills and valleys of the product are. The analogy I like to give are kind of similar to autocomplete. When you use a product like autocomplete, you would think a product that is suggesting things but only getting accepted 30% of the time would be really, really annoying. But the reason why it's not very annoying is actually because you've actually learned that, hey, 70% of the time, I don't need to accept this. And the times that I do, I know to get value from it. And you also know beforehand if a sort of command that you write is very complex, you just expect, "Hey, the autocomplete is not going to work for it." So I think it's almost like a, understand what the hills and valleys of the product are.

(00:44:45):
The crazy thing is, every three months that kind of gets changed and reevaluated. It almost becomes the case that it becomes materially better than it was in the past. So I think maybe patience and being explicit are maybe the two important key pieces I would tell users.

Lenny Rachitsky (00:45:00):
And I think something that was kind of between the lines there is get a gut feeling of what the model is capable of, like how specific to be versus how abstract it can be. And there's kind of this gut feeling you start to build over time.

Varun Mohan (00:45:12):
That's right. Yeah. And with that, it feels like we have an actual preview. Guess what? We have a nice-

Lenny Rachitsky (00:45:20):
Cute dogs.

Varun Mohan (00:45:21):
A nice dog app. And one of the cool parts is that we've also done beyond just modifying code is actually being able to point to different pieces. And I guess I could just kind of say... I could point to different elements and say, "Hey, make the background..." This is not great design, but I could basically say, if I took this element, "Make this background red and just take a particular element and just change it and make it red." And it should go out and be able to go out and do this.

(00:45:52):
The preview aspect of the product of being able to showcase the app while it's getting built helps in that, now actually you can live entirely in app world. You don't even maybe even need to look at the code. Granted this looks hideous, but in some ways if I wanted to, I could go out and do that, right?

Lenny Rachitsky (00:46:09):
This is what happens when there's no more designers. Like, [inaudible 00:46:11].

Varun Mohan (00:46:11):
Yeah. When there's no more designers. Sure. Maybe the answer is like, when you ask me what should people be doing, they should study great taste. Having great taste. Because I think taste is also a very, very hard, right?

(00:46:22):
But maybe the other key piece, Lenny, that I wanted to showcase here is obviously you could keep going here. I could take different components and kind of change them. We have a lot of plans here that are beyond just point and click changing components. But one of the cool pieces is the AI. There's an AI review flow as well, which is kind of like what I was saying. The goal of AI has now changed a lot in that it is now modifying large chunks of code for you. And the job of a developer now is to actually review a lot of the code that the AI has generated. And granted right now during this podcast, I'm not going to review all the code that's getting generated.

(00:46:57):
But let's say I want to go out and modify some of this code. And this is where if you're an actual developer that actually wants to go modify, maybe I don't like my variable name being called title. I want it to be called Title String instead, like this. And if I wanted to go out and make that change and change to go out and say Title String and that's what I'm going to do, I'm just going to tell the AI to continue.

(00:47:18):
The cool part about this is Windsurf not only knows about what the agent has done. It also knows everything that the user has done. Our goal here is to have this almost flow-like state where everything the user has done, the AI also knows. And it is able to predict the intent. And as you can see, it said, "I noticed that the interface property title was changed to Title String." And then it now has gone out and modified all the locations within the app from title to Title String. And now it no longer says that.

(00:47:45):
So this is where even if I'm writing software and I want to go and make point changes, the AI can go out and quickly make these changes on the user's path. Imagine doing a refactor or a migration and you just change one part of the code. You can just tell the AI to continue the rest. And because it deeply understands the code base, it should go out and find all the corresponding places to go out and make the change. And obviously now when I reload my app, there's no bug in the app. It still loads properly. I could obviously tell it to do even cooler things like make the app retro. I don't know what that means, but I guess I could do that. And it should go out and make the change correspondingly for me.

(00:48:23):
But yeah, that's maybe the high level parts there where the AI is not only able to operate entirely in app space but also on the code space of the users going out and modifying code and to bridge the gap between the two. So it should add leverage not only non-developers that are just purely building apps, but also developers that are just hands-on keyboard too.

Lenny Rachitsky (00:48:44):
Amazing. By the way, if you're not on YouTube, you can't see, but you can just select any element of the page and then reference that in your ask of, "Here's what I want changed." I didn't know that was a feature. And that is extremely cool.

(00:48:57):
So interestingly, so having just looked at Lovable and Bolt and Replit and apps like that, it's basically doing all the things those apps do. Oh, wow. There's the retro version. That's good. I like that it built on your red and made it really nice actually.

Varun Mohan (00:49:11):
Actually the red looks way better now.

Lenny Rachitsky (00:49:12):
Yeah, a little green button. This is great. Okay.

Varun Mohan (00:49:14):
Cool.

Lenny Rachitsky (00:49:16):
So I don't think people realize this, but apps like Windsurf, that it could actually do a lot of agentic work for you where you just tell it, "Here. I want you to do this" versus it's auto completing code for you.

(00:49:25):
The big difference is you need to start it with some code base so you have this kind of boilerplate React project. Is there a reason you guys aren't taking that step and just doing that automatically for you? Is it because you're targeting engineers and they don't need that or is there other reasons?

Varun Mohan (00:49:39):
Lenny, the interesting thing is the base app that you saw for this was also generated by Windsurf. The reason why we sort of didn't generate it is installing all the dependencies takes like three or four minutes. And for the demo, I didn't want to wait. But totally, actually most of the users of the product, probably zero-to-one build these apps.

(00:49:57):
And if I can say one interesting thing is, when we launched Windsurf, actually we tasked everyone at our company to go out and build an app with Windsurf. That included our go-to market team and our sales team. There was a crazy stat that I think people would find surprising, but we've saved over half a million dollars of SaaS products we were going to buy because our go-to-market team has now built apps instead of buying them. Our head of partnerships, instead of buying a partner portal product, has actually built its own partner portal. He had never built software in the past. We've actually come up with ways inside the company to deploy these apps easily in a secure way. And we're actually now building very, very custom software for our company to operate more efficiently, which is, I would not have expected this probably six months ago.

Lenny Rachitsky (00:50:44):
That is incredibly interesting. You don't need to name company names, but I guess what's a space you're least bullish on that you think is going to have the most problem here with people building their own version of these sorts of products?

Varun Mohan (00:50:56):
I think maybe my viewpoint are these very, very verticalized niche products I think are going to get... They're going to get competed down a ton. And I think sales products are an example of one of these things. And maybe this is a... I don't want to be very negative, but it's very hard inside a company like ours to task our best engineers to build a best in class sales product. There's not enough interest to do that. Or to build a best in class legal software product or finance software product. It's very, very hard for us to. And actually that's a very big moat for these companies that built these products that they were able to come out, have an opinionated stance on how to do this, hire good enough engineers to go out and build the software. Our company is unwilling to do that. So previously, we would go out and buy the technology because there would be no alternative.

(00:51:48):
But now one of the crazy things is that the domain specialists now have access to build the tools that they ultimately wanted, which is actually crazy. If you think about why were these software companies able to exist these vertical software companies, the reason is because they had many features. The kitchen sink of features worked for a lot of companies, but each individual company only wanted 10% of the features. But the problem is, each individual company was not capable of maintaining a piece of software or building the custom piece of software for 10% of the features, but that has now changed entirely. Now they can.

Lenny Rachitsky (00:52:22):
Yeah. There's always been a story of like, "Why would I spend any time building my own software if I could just..." But now it's like five minutes of time.

Varun Mohan (00:52:29):
Five minutes and maybe even more custom to your system. How many times have you bought a software and you're almost like, "Why is there no integration to X? And I actually use X." How annoying is that? That actually makes the software less useful to you.

Lenny Rachitsky (00:52:43):
So I think what's cool is when you go back, if someone zooms back to the beginning of when you started the demo, it's basically a PM talking to an engineer, "Hey, build me a Airbnb for dogs. Here's a stupid mock that I made with some boxes." That's almost like a bad PM talking to an engineer and it just actually works. That's what's insane about this. And so that's why this example you're sharing of go-to-market folks, building their own things, it's like they don't need to know anything about product building. It's just describe it in some ridiculous way and draw a couple boxes of what you want it to look like and it makes something for you.

Varun Mohan (00:53:20):
Which shows that agency is what matters. If you have a product manager that has an idea, there's no reason for why that idea cannot be more well fleshed out. How many times do you have a product manager that just continualize ideas, but it just feels like they are extremely unsure on how to execute on it? They just want to say things for sake of saying things? But for the people that have ideas and a lot of, I guess, agency, they can go out and prove out what they want without any sort of external resources.

Lenny Rachitsky (00:53:47):
I think even more acutely for product folks listening to this, it's the salesperson coming to you being like, "Hey, I want this thing. It's going to help me with my sales team." And you're like, "I don't have a million things to build. I don't have time for this." And so that problem goes away, which I think will make a lot of product leaders really happy.

(00:54:04):
The model that this is sitting on, is it Sonnet?

Varun Mohan (00:54:08):
Yeah. So just to break down how it ultimately works, we have a model that does planning. And I would say right now Sonnet is a really, really good planning model. I think OpenAI's GPT-4o is also good. But the crazy thing is what we try to do is we try to make the Anthropic based model or Sonnet model try to do as much of the high level planning as possible. And then what we try to do internally is run all the models necessary to do high quality retrieval for the agent. As you could see, the agent needed to understand what the rest of the code base ultimately did. We actually make sure we run models to actually chunk up the entire code base and understand the code base so that obviously it would not be a good idea if we had a 100 million line code base to send that entire code base to Anthropic.

(00:54:49):
First of all, you couldn't do that. That's over 1.5 billion tokens of code. So obviously that would be three or four orders of my actually larger than the largest context lens right now.

(00:54:58):
But you also wouldn't want to do that from a cost and latency standpoint too. So that's one. And the second piece that you saw was the model is able to very quickly make edits to the software as well. We have custom models that we built that are post trained on top of popular open source models that can make these edits really, really quickly to the code base. And the reason why you would want to do that is it's A, faster, and B, also that model can actually have more of the code base in context too. So it can be better at applying changes than even Anthropics model too.

(00:55:28):
So I think the way we like to think about it is, our only goal is how do we build the best product possible? How do we build the best product possible and how do we make the ceiling as high as possible? And we will go out and build models and train models wherever necessary. But if we're not going to be good at a task and we think the open source is better or Anthropic's better, we'll go and just use the open source or Anthropic.

Lenny Rachitsky (00:55:47):
And so the models you guys are building, those are built on open source models that people are releasing?

Varun Mohan (00:55:51):
Yeah. Interestingly, the one that does retrieval is actually completely pre-trained in-house that actually does that. But yeah, for a lot of different pieces, it's based on open source. Interestingly for the one that does the edits and auto-complete, that is also in-house. As you're typing, we actually do some auto-complete related stuff. I'm happy to show that, but I think a lot of users are familiar with that capability. So I think the way we like to look at it is like, what could we be best at and we will go out and trade. But if we're not going to be best at it, we should not just, for the sake of ego, go out and trade something.

Lenny Rachitsky (00:56:23):
This may be getting too technical, but just, is there anything interesting around what you train on?

Varun Mohan (00:56:27):
Yeah, so one of the interesting things that we have from our users, and this is where we try to think like, "Why would we be any better?" is that, actually every hour, we get probably tens of millions of pieces of feedback from our users. We get a lot of feedback on what they like and what they don't like. For something like autocomplete, we get a lot of preference data, a lot of preference data. And the preference data is weird. It doesn't look like data that you find on the internet. It's like data as the user is typing. Imagine you're typing some code in a code base, the code's going to be incomplete as you're typing it, right? It's not going to be in a full-fledged form. It's not like it is on GitHub. But we have a lot of data that looks like this.

(00:57:06):
So we are uniquely well-positioned to actually build a good model that can complete code even when it's in an incomplete state when the models that are out there, the frontier models have consumed very little code that looks like this. So for that case we're like, "Hey, we can go out and do a much better job potentially." And we'll go out and train models on all the preference data we have.

(00:57:25):
The same is kind of true on retrieval, right? There's a way to find out, are we retrieving the right data? Did the user accept the code change after that? Was the retrieval actually a good retrieval a signal that we can get? So basically the way we like to look at it is, if something is just purely code planning, there's not a great reason why we would be the best at that. I can't come up with a coherent argument for that. But for something that looks more along the lines of, "Hey, here's an intermediate code base that is very gnarly and here are some changes that need to get made" and we know the evolution of the code or we've seen the evolution of code across millions of users, we feel like we can do a great job of that.

Lenny Rachitsky (00:58:03):
I think what's interesting about this is another differentiator/moat for companies that end up winning in this space, is you just have more and more of that data than other companies if you're ahead.

Varun Mohan (00:58:14):
Yeah. This is sort of why maybe at a high level we like the zero-to-one app building product space. I think it's really... It's a good product space. But ultimately I think it needs to boil down to you understanding the code, because otherwise, you're living at too high a plane where it's not clear why you would be able to be the best at that compared to everyone else. It's not really clear.

Lenny Rachitsky (00:58:35):
As a company, you mean?

Varun Mohan (00:58:36):
As a company.

Lenny Rachitsky (00:58:36):
Versus as a user.

Varun Mohan (00:58:37):
It feels like it might get competitive in a way that it's not clear where you would continue to differentiate over and over with time.

Lenny Rachitsky (00:58:45):
I see. Because if they're just sitting on top of Sonnet and just doing what every other Sonnet wrapper is doing, there's not a lot of differentiation or moat.

Varun Mohan (00:58:54):
It depends on how you do it. But maybe if I was to say this, if the inputs you're consuming are just web elements, extremely high level web elements, then the interface might be high level enough that it's hard to maybe get better than maybe what the frontier models are doing just across the board. You are just better off just plugging in Sonnet for everything.

Lenny Rachitsky (00:59:14):
Got it. Awesome. One thing I wanted to come back to that I wrote down that I think is really important for people to understand, you talked about how with Windsurf it's not necessarily... There's a boilerplate code base that you want to start with because it's actually... Because it's not an abstracted zero-to-one app builder. It's an actual IDE you're coding in. And you talked about how has to install dependencies, which is kind this painful thing. And the reason it has to do that is because running locally on your machine versus in the cloud, like, say, Lovable and Replit and all these guys, although I think Bolt runs in your browser in this really cool way.

(00:59:47):
So that's an important distinction. This is like you're running this locally in your machine and has all the libraries you need to actually run it.

Varun Mohan (00:59:54):
No, I think that's important. I think we believe a lot of people sort of build software in what are called code spaces and things in a remote machine. I just think it's that a lot of developers like building locally for what you said. Like if you're doing things that are more than just full stack applications, you might have dependencies on your machine that are just system dependencies that are just gnarly to install. Let's imagine you're building a GPU-based application and the Nvidia drivers, they're necessary. You just want to give people the flexibility to build where they can build. And I think the IDE and building locally has been a thing that people have done for decades, so probably it's not going to go away in the next couple of years.

Lenny Rachitsky (01:00:29):
I love that your sales folks now are running local host servers.

Varun Mohan (01:00:34):
Well, with the browser previews, it's easier, right? You kind of just open it up on the side.

Lenny Rachitsky (01:00:37):
Yeah. Yeah. Oh my god. Okay. I have a few more questions just about how you think and operate at Codeium. So you guys are kind of at the forefront of how product teams are going to operate. You're seeing the future every day. And so I'm curious if there's ways you guys have structured your teams, engineers, product design that might be different from how other companies are doing it or have tried stuff that has worked really well or tried stuff that's a huge disaster?

Varun Mohan (01:01:02):
One interesting decision that we kind of have for core engineering is that we don't have pure product managers for the core engineering side of the company. And by the way, that's purely because we build for developers and our product is built by developers. So I think the intuition from our own developers is hopefully valuable. If not, we might be hiring the wrong type of people. So I think our developers are, in some sense, flexing to be more product conventional product managers.

(01:01:32):
Now on the other hand, if we were building something that looked more like Uber or the persona was very different and we didn't ourselves understand it, I think the organization wouldn't look the way it looks.

(01:01:42):
For the enterprise side of the company, because we do work with a lot of large enterprises where the requirements are not something that our engineers would automatically understand, I don't think our engineers wake up and they're like, "We need FedRAMP." This is probably something that a lot of customers come to us with and tell us. We have people that flex in this product strategy role that understand what the customer wants and understands the technical capabilities that we have to best build a product that would help them at scale.

(01:02:12):
So I think we have an interesting organization in this regard, but mostly I would say because we are a developer-based product, I would say that's true.

(01:02:21):
And then also kind of like what you said for the engineering team itself, the team structure is, it's fairly flat. We try to go with two pizza teams, teams that are fairly small just because I think the problem is when a team gets too big, the person leading the team is no longer able to get in the weeds of the technology itself. And I think in a space that's moving this quickly, I think it's dangerous to have leaders that don't understand the technology deeply and are not building. It's very, very dangerous because there's too much armchair quarterbacking. And so I think that's maybe one other decision we made.

(01:02:56):
And then teams are very, very flexible. So if we decide something is a new priority, we're very quick to change the way a team looks. And it's very centrally planned in this regard.

Lenny Rachitsky (01:03:08):
The two pizza team concept, I saw a tweet long ago where someone from India, was like, there's always talk about two pizza teams, but pizzas in India are much smaller. And so the teams end up being smaller and they're like, "Why can't we build as much of these teams in the US?"

Varun Mohan (01:03:22):
Oh man.

Lenny Rachitsky (01:03:23):
Okay. So how many PMs do you have? So you said you have 150 employees, something like that?

Varun Mohan (01:03:28):
Yeah. So in terms of the product strategy function, we have three people in that role right now.

Lenny Rachitsky (01:03:34):
I see. So it's like product... They're in their titles is product strategy, not necessarily product management?

Varun Mohan (01:03:41):
That's right.

Lenny Rachitsky (01:03:41):
Interesting. And then 50 engineers, you said 80-ish sales folks?

Varun Mohan (01:03:45):
Yes, that's right. And then obviously we have functions like recruiting parts of G&A, like finance. We have marketing at the company. So some other functions internally as well.

Lenny Rachitsky (01:03:56):
It's interesting. And this is something that you hear all the time with companies like Dario for example, from Anthropic talking about how 90% of code is going to be written by AI. But all at the same time, all you guys are hiring engineers like crazy.

Varun Mohan (01:04:08):
Yeah. Is that contradictory?

Lenny Rachitsky (01:04:10):
It's that contradictory, will there be an inflection point of like, "All right. Now we don't need them anymore."

Varun Mohan (01:04:15):
I think it really comes down to, do you get incremental value by adding more engineers internally? I'm going to take... First of all, maybe just to set the record straight, if AI is writing over 90% of the code, that doesn't mean engineers are 10X as productive. Engineers spend more time than just writing code. The review code, test code, debug code, design code, deploy code, right? Navigate code. There's probably a lot of different things that engineers do. There's this one famous law in parallel computing, it's called Amdahl's Law. I don't know if you've heard about it. But it basically says if you have a graph of tasks and you have this critical path and you take any one task and parallelize it a ton, which is make it almost take zero amount of time, there's still a limit of the amount of how much faster it made the whole process go.

(01:04:56):
So maybe put simply, let's say you have 100 units of time and only 30 units of time is being spent writing software and I took the 30 and made it three, I only took the 100 and made it 73. It's only a 27% improvement in the grand scheme of things.

(01:05:09):
So I think look, we are definitely seeing over 30, maybe close to 40% productivity improvements. But I think for the vision that we're solving for, even if I were to say the company in the long tail had 200 engineers, it'd probably be too low still at that point. So the question is, how much more productivity do you get per person? Actually, maybe just to even say one of those thing for some of these large companies, let's say you took the CIO of a company like JPMorgan Chase, right? Her budget on software every year is $17 billion and there's over 50,000 engineers inside the company and you told her, "Hey, each of these engineers are now able to produce more technology." That's effectively what you've done, right? The right calculus that JPMorgan Chase or any of these companies will make is the ROI of building technology has actually gone up. So the opportunity cost of not investing more into technology has gone up, which means that you should just invest even more. And maybe in the short term you have even more engineers, right?

(01:06:08):
Now, that's not true across the board. There are some companies that are happy with the amount of technology they're building and there's a ceiling on the amount of technology they want to build. But for companies that actually have a very high technology ceiling, this doesn't mean you stop. This actually means you hire more.

Lenny Rachitsky (01:06:22):
This is a great bull case for engineers. I feel like the canary in the coal mine for the engineering profession is when companies like yours slow down on hiring engineers.

Varun Mohan (01:06:30):
Yep.

Lenny Rachitsky (01:06:31):
That's not happening.

Varun Mohan (01:06:32):
[inaudible 01:06:32]. It seems like Anthropic is also hiring a lot to get it done.

Lenny Rachitsky (01:06:35):
Yeah. Everyone is. So I think that's really promising. I think if you're in college still, makes sense to get into engineering at this point.

(01:06:40):
Okay. Let me ask you this question as kind of a final question maybe. What's maybe the most counterintuitive thing you've learned about building AI products, building Windsurf and just being in a space?

Varun Mohan (01:06:54):
I think one of the weird things is online, everyone is very excited about the short-term wins that we are making, right? Like what we're putting out maybe weekly. We do these waves every couple of weeks. But actually a lot of the bets we're making inside the company are for things that are not three, four weeks, maybe three, six months, nine months away. That's what we're working on internally. Because I think this is kind of, Lenny, what I was mentioning to you before. One of the goals that I tell everyone at our company is we should be cannibalizing the existing state of our product every six to 12 months. Every six to 12 months, it should make our existing product look silly. It should almost make the form factor of our existing product look dumb.

(01:07:31):
So there's this weird tension where you want to have a product in market and you want to incrementally iterate and listen to users and keep making it better and better. But I would say we were the first identical IDE product out there. That's what we landed with. And I think the value of that is going to depreciate very quickly unless we continue to re-prove ourselves. And we will need to re-prove ourselves in ways in which our users are not even asking. So there's this tension here, where incremental feels very safe, right? Add this one more button. Users say, "Hey, I would like to be able to have this drop down to do X." But that is not the reason why we're going to win. That's almost table sticks. Yeah, we'll decide to do some of these. We might not decide to do a lot of these things. But it's these longer term efforts inside the company that almost disrupt the existing product that are ultimately the reason why we're going to succeed.

(01:08:21):
It's this weird tension that you need to have in your head of, you can't also not listen to your users at all because they're the reason you exist.

Lenny Rachitsky (01:08:29):
This reminds me of a recent podcast guest. We had Gara from captions on the podcast and he told us that he has two roadmaps. They have two roadmaps at the company. They have the real roadmap, like the typical roadmap based on feature requests and user feedback and data and things like that. And then they have the secret roadmap, which is completely not informed by users or data/ it's just them making bets on where they think the world is going.

Varun Mohan (01:08:52):
That's right.

Lenny Rachitsky (01:08:52):
And I love that he calls it the secret roadmap just to make it very mysterious and-

Varun Mohan (01:08:56):
That's smarts. That's very smart.

Lenny Rachitsky (01:08:57):
Okay. I have one more question. I apologize. What's one thing that you wish he had known before starting Codeium?

Varun Mohan (01:09:04):
Honestly, I wish I had... Maybe humility is the wrong term, but this idea of just being okay with being wrong faster. I always think about things on when we make decisions. Me and my co-founder, we always talk about it. We're almost like, "Hey, I wish we had made the decision to do this a couple months earlier." We always talk about this. And the weird thing is outside looking and everyone's like, "Wow, actually the decision was made at the right time." But in my head I'm always banging my head being like, "What if we had made it a couple months earlier?" I think part of that is I waxed poetically about like, "Oh, you need to be irrationally optimistic and uncompromisingly realistic." But it's very hard to do this in practice because you drink your own Kool-Aid too. Because if you're not drinking your own, you won't get up out of bed. The answer is already solved. It's not actually any of these startups. The answer is Microsoft is going to be the winner in any software category. Isn't that the answer? Just because of distribution, resources and capital, they're going to commoditize every space.

(01:10:06):
So I think in some ways this amount of just understanding that, hey, re-evaluate your hypotheses and get into an uncomfortable space way more frequently is something I need to remind myself even to this day. And probably something that I didn't know coming in and starting the company. We started the company at peak zero time. At that time, probably everything seemed like it was going to moon. And there was probably a lot of irrational confidence, I would say, that we shouldn't have had.

Lenny Rachitsky (01:10:36):
Varun, we covered so much ground. What an incredible conversation. I learned so much just sitting here listening and asking you questions. Is there anything else that you wanted to share I leave listeners with, any last piece of nuggets or wisdom before I let you go?

Varun Mohan (01:10:51):
To be honest, I could give predictions about the space. Probably most of them are going to be wrong. I think the best thing to do is just get your hands dirty with all of these products. And I think one of the most obvious things that's going to happen is, in the next year, there will be a tremendous amount of alpha for anyone that is able to take maximum advantage of these tools. Just imagine how many of your coworkers just don't even know the existence of these tools, don't know what they can do and how much less productive they will be. And I would just say get your hands as dirty as possible, as quickly as possible.

Lenny Rachitsky (01:11:24):
And when you say get your hands dirty, basically it's like download Windsurf, start coding. Ask it to build things for you.

Varun Mohan (01:11:29):
Yeah, build apps. Build apps. Start using it for maybe even making mocks, modifying your existing code base. There's probably ways in which you could be a force multiplier to your organization and ways in which they never even anticipated, right? Imagine if you were a product manager that could actually very quickly make edits to the code base and just start pushing changes yourself. You probably get a tremendous amount of respect from your own engineering peers. You could probably get way more done because of that. I feel like there's no sort of ceiling at that point.

Lenny Rachitsky (01:12:00):
I think this is such an underestimated point you're making here. There's apps that can build things from scratch and then there's apps like this that can edit your existing code base if you're a PM at... What's the largest company you work with, people-wise?

Varun Mohan (01:12:15):
Publicly, let's just say JPMorgan Chase.

Lenny Rachitsky (01:12:16):
Okay.

Varun Mohan (01:12:19):
They have over 50,000 developers.

Lenny Rachitsky (01:12:20):
Okay. So you could be a PM at JPMorgan Chase and be like, "I have a problem I need to solve. I want to move this metric. I want to change the step in the signup flow." You just open up Windsurf and tell it to do the thing you want. And then can you push straight to GitHub and do a-

Varun Mohan (01:12:37):
Yeah. Actually, you could do that too.

Lenny Rachitsky (01:12:39):
... merge [inaudible 01:12:39]-

Varun Mohan (01:12:39):
Yeah.

Lenny Rachitsky (01:12:39):
Okay. PR?

Varun Mohan (01:12:40):
Yeah, it could make a PR for you.

Lenny Rachitsky (01:12:41):
Oh, my God. This is insane. Folks, future is out of control. Okay. Man, that was such an important point at the end there because I think people may not realize this. They see all these other apps, they're like, "Oh, [inaudible 01:12:51], prototypes," but this is legitimately something a PM can actually do work with.

Varun Mohan (01:12:55):
Yeah. When you think about the people, at least that, I don't know, Lenny, who you respect the most, they're the people that somehow, despite their title, their level of agency and just output just all the way down to the weeds to the highest level strategy is just perfection, right? They know when to go all the way down. And I think sometimes you see people that talk about roles and they irrationally feel like, "Oh, because I'm this role, I'm not allowed to touch this." Well now everything's open season, right? And I think this is an opportunity to almost go all the way down to the weeds and all the way up to the top and just be effective on every level.

Lenny Rachitsky (01:13:29):
Unbelievable. All right. Well with that, we'll leave folks. Varun, thank you so much for being here.

Varun Mohan (01:13:35):
Awesome. Thanks a lot, Lenny.

Lenny Rachitsky (01:13:36):
What an incredible conversation. Thanks, Varun. Bye everyone.

(01:13:42):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

