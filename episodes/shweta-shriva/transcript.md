---
guest: Shweta Shriva
title: Product lessons from Waymo | Shweta Shrivastava (Waymo, Amazon, Cisco)
youtube_url: https://www.youtube.com/watch?v=VtNmAjNF3Tc
video_id: VtNmAjNF3Tc
description: 'Shweta Shrivastava is a Senior Product Leader at Waymo, an autonomous
  driving technology company backed by Alphabet. Prior to joining Waymo, she was the
  CPO of Nauto, where she also worked...

  '
duration_seconds: 2536.0
duration: '42:16'
view_count: 5227
channel: Lenny's Podcast
keywords:
- growth
- metrics
- kpis
- prioritization
- mvp
- analytics
- funnel
- hiring
- culture
- management
- strategy
- vision
- mission
- market
- design
---

# Product lessons from Waymo | Shweta Shrivastava (Waymo, Amazon, Cisco)

## Transcript

Shweta Shrivastava (00:00):
Are you proactively trying to challenge your own assumptions is extremely important, right? As a big enough product manager as well as a seasoned product leader, if you're not doing enough of that, then I think you might not be listening. If there's no conflict, if there's no contention, then something is missing.
Lenny (00:20):
Welcome to Lenny's podcast where I interview world-class product leaders and growth experts to learn from their hard one experiences building and growing today's most successful products. Today, my guest is Shweta Shrivastava. Shweta is senior director of product management at Waymo, which if you're not familiar with Waymo, they're building self-driving cars that already live on the streets in San Francisco, LA and Phoenix. I actually got to take a ride in one ahead of this chat and you'll hear all about that in this episode.
(00:48):
Before joining Waymo, was chief product officer at Nauto and AI started focusing on driver automation safety. Before that, she was head of product management at Amazon Web Services for their database and analytics services, and before that she was at Cisco. In our conversation, we delve into what it's like to work as a PM at Waymo and how it's both different and similar to software only products.
(01:09):
We talk about their KPIs and goals at Waymo, including how they track progress towards a future of self-driving cars, how they build subtle cues and behaviors into the cars to create trust for the rider and also for other cars on the road. Plus Shweta's biggest lessons about building products and teams across the many companies she's worked at. I can't wait for the future of every car being self-driving, and it was super fun to learn about what goes into making this all happen. With that, I bring you Shweta Shrivastava after a short word from our sponsors.
(01:40):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate your growth. Thousands of fast-growing companies like Gusto, Com, Quora and Modern Treasury Trust Vanta to help build, scale, manage and demonstrate their security and compliance programs and get ready for audits in weeks, not months. By offering the most in-demand security and privacy frameworks such as SOC 2, ISO 27001, GDPR, HIPAA, and many more.
(02:07):
Vanta helps companies obtain the reports they need to accelerate growth, build efficient compliance processes, mitigate risks to their businesses, and build trust with external stakeholders. Over 5,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2 and these other frameworks. For a limited time, Lenny's podcast listeners get $1,000 off Vanta. Go to vanta.com/lenny. That's V-A-N-T-A.com/lenny to learn more and to claim your discounts. Get started today.
(02:38):
This episode is brought to you by public.com. We want to tell you about their new treasury accounts, which earn a 4.8% yield on your cash. That is higher than a high yield savings account while still being backed by the full faith and credit of the US government. Treasury yields are at a 15-year-high, but buying US Treasuries is super complicated. If you go to a bank or navigate an ancient government website, or at least that was the case. Now you can move your cash into US Treasuries with the flexibility of a bank account.
(03:09):
You can access your cash whenever you want, even before your treasury bills hit maturity. There are no hold periods, no settlement days, just a safe place to park your cash and earn a reliable yield. Public will automatically reinvest your treasury bills at maturity so you don't have to do anything to continue growing your yield. And you can manage your treasuries alongside stocks, ETFs, crypto, and any alternative assets. Do all your investing in one place and earn 4.8% a higher yield than a high yield savings account only with a treasury count at public.com/lenny.
(03:47):
Shweta, welcome to the podcast.
Shweta Shrivastava (03:49):
Thank you. Great to be here.
Lenny (03:52):
It's great to have you. I thought we'd start with just a little bit about what it is you do at Waymo today. What are you and your team's responsible for at Waymo?
Shweta Shrivastava (04:02):
Yes, my team's responsible for three key areas, I would say. One is building a big part of the software that actually runs on board the fully autonomous vehicle and that determines the actual behavior and trajectory of the vehicle. Secondly, building the simulation tools and technologies that are required to validate the performance of the system. And then, a third one of the teams focused on commercially scaling our ride-hailing business, which is one of our key go-to market applications for the technology we're building.
Lenny (04:34):
So as you know, I arranged a ride for me in a Waymo in San Francisco. It was actually a really rainy day and it was quite mind blowing. I've never been in a self-driving car that had no driver sitting in the front. I have a Tesla and I turn on self-driving sometimes, but I've never experienced just sitting in the back and this thing just raises you around. Also, just like a memory hat is the app to call the Waymo, it feels like Google Maps except instead of just telling you how to get to a place like a car shows up and just takes you there and then you could change course as you're driving and it's crazy how quickly it became normal.
(05:08):
I'm just like, all right, we're just riding around San Francisco in this self-driving car and just sitting in the back and telling you where to go. And so anyway, I'm going to ask you a bunch of questions around this, but I guess thank you for arranging that ride. It was quite special.
Shweta Shrivastava (05:21):
No, I'm glad that you were able to do that on a rainy day. So that's a special bonus because, again, the technology has been performing very well, which has been very heartening for us to see.
Lenny (05:30):
A few questions along these lines, one thing that I noticed that was really cool is we're trying to turn into a lane and there's cars coming in that lane just continuing to move and the car just kind of subtly was inching its way out, communicating through this interesting body language thing of just like, can someone let me in? And it's interesting, there's no eye contact involved and it's just like this, I don't know, gesture that you all have to develop.
(05:54):
And so, I guess, the question here is just like what have you all learned? And I don't know if you even work on that piece of it, but just, I'm curious how you think about creating this body language of the car communication system to help people understand what it's trying to do.
Shweta Shrivastava (06:07):
We're using a lot of human driving data to train our deep models. So it's important to make sure that the behavior of the car doesn't seem robotic, it can feel quite unnatural. And from the get-go, we focused on building a fully autonomous system. So it's important to have that familiarity, that trust, building with the riders where they're not daunted by technology, they don't feel like they're sitting in our walk. It has to feel very human-like, but in a good way. Making it safer than human driving, but then not making it feel unnatural.
(06:40):
And so we have deep learned models that can understand what the other road users' intent is. So, stuff like which way the pedestrian is looking or what is their body orientation because that could tell you which way they're headed. The road signs or the gestures, somebody is trying to stop the vehicle. The system can understand all those signals.
(07:04):
So because we're using deep learn models trained on human driving, but again sort of in a good way. We discard the bad human driving data. We can mimic human driving behavior in a good way and that's why you saw the behavior that you saw yesterday. Now, one thing to note is we can't also just completely rely on explicit gestures and signs because a lot of driving has also social norms. If you're in a pretty clear section in San Francisco, maybe it's okay for pedestrians to cross even when they don't have a walk sign.
(07:43):
Another city, another intersection might have a different social norm when it comes to pedestrians crossing the four-way stop sign or the crosswalk or what have you. And so, the car also has to learn about those social norms and be able to react to it. So, like I said, we don't realize how sophisticated, how interactive and how social driving really is. And with our artificial intelligence capabilities, we have been able to incorporate a lot of that into our system behavior.
Lenny (08:14):
So before Waymo, you worked at non self-driving software companies, you worked at Amazon, Cisco, a few other companies. I'm curious what you've found to be the biggest difference working in a company like Waymo versus a traditional software company.
Shweta Shrivastava (08:29):
As I said earlier, it's a highly complex, technically complex, system that we have built and we're improving. And if I may say, it's the most game changing product that anybody would ever work on.
Lenny (08:43):
I don't know, Amazon's pretty cool, but I totally get you.
Shweta Shrivastava (08:46):
I worked at Amazon, I'm a fan. And they have been pretty transformational with AWS and on the eCommerce side. But a fully autonomous driving system, it's also a very, very hard problem. So it's transformational from that perspective too. I would say that the PMC has to be able to go technically indeed, compared to what they would do in other software products. They have to be able to get into the details as much as needed. They have to be okay with uncertainty and ambiguity.
(09:24):
Again, I think, that is part and parcel of any product management role, but it's even more so here. This is a long game and so you have to have the tenacity to play the long game and be continuously improving the product and make this thing a broad reality and future. So, those are some of the attributes. I would also say that there is some level of self selection here. You have to be driven by the mission to make the roads safer. We have about 1.35 million debts that happen every year across the world from traffic accidents and most of that is attributable to driving errors and driver distraction.
(10:04):
I've been guilty of checking my text messages while driving. I've seen other drivers do that. But a fully autonomous technology, you don't have that risk. That's the risk we're trying to minimize. So they have to be driven by that mission. One other thing is that the concept of MVP, which is so widely popular in the SaaS product management world or product management world, in general, has a whole new meaning here at Waymo when you work in a product like this because safety is on top of mind for all of us and can't really cut corners on safety.
(10:42):
The MVP bar itself for safety is extremely high for us. So, the core product management philosophy also, getting an MVP out there and then iterating with the real world deployment. It applies, but it's just a different bar on that MVP.
Lenny (11:03):
Touching again on safety and human behavior, I was thinking a little bit as we're chatting about, say of Tesla, which has self-driving car, self-driving capabilities and intellectually I know it's probably going to drive a lot better than I am, but I still feel like I need to disengage it occasionally when I'm on a curvy road. I'm just like, I don't know about this, I don't want to leave room for error if there's something that weird that happens.
(11:30):
And I imagine someone designing product for that weird behavior where I should probably trust it because it's probably a lot better driver than I am, but I don't know, I feel like I can do a better job. Is there anything you've learned about, I don't know, human behavior or how to design software for these sorts of experiences that maybe surprised you or thought was really interesting or that was really important?
Shweta Shrivastava (11:51):
Since you mentioned Tesla, I just want to clarify that it's a different system that we are building, which is for Waymo, we started by solving the problem of fully autonomous driving without a human driver at the wheel from the get-go. It's not a driver assist or aid system which relies on the human driver taking over when there's a complex situation. So I think that expectation is built into that kind of a product and so the human folks who are using that product will also have that mindset that, hey, I should be ready to take over when the situation demands because we've built the system from the get-go to work in a fully autonomous mode without a human driver intervention at the wheel.
(12:38):
We had to integrate this into our design philosophy from the very beginning that this has to feel credible, predictable and the writers have to be able to trust the system. So that has been sort of the core of the design philosophy. And so, what happens is, and I heard this from you as well, which resonated with me and I've heard this from a lot of our writers, that for the first five minutes of the ride it's, wow, is this thing really happening.
(13:10):
But then it starts to feel very natural and as if this is how it was always meant to be. After the first five minutes, this is like uneventful. That's exactly how it's supposed to feel, but it's not a happenstance that it feels that way. The naturalness, the smoothness and still adhering to safety at all times are things that are designed into the system. And then we make sure that the rider has visibility into what's happening. If they're not wearing the seatbelt, the rider support would call them. So then they know, okay, there's a human that they can reach out to if they have an issue. They can look at the monitor in the car to understand what the car is seeing. So I think all these little things help develop that trust in the system.
Lenny (13:57):
On that same note, what's one thing that your teams have built that creates a lot of trust or maybe it was a surprisingly important element in creating trust in the experience in terms of the product, especially in, I don't know, either the app or in car experience.
Shweta Shrivastava (14:14):
I don't know if I can point to one thing. Again, this is such a holistic experience that I think it has to be a bunch of small things to make it feel natural, transparent and trustworthy to the writers. And I can give you one example that I don't think I've mentioned in the discussion so far. So, again, because the system is designed to be cautious and defensive but still making adequate progress in the absence of traffic, it will never go above the speed limit. It doesn't go above the speed limit. It sticks or adheres to the speed limit or something that a lot of our riders actually appreciate about the system.
(14:55):
Now, it turns out that adhering to the speed limit even without traffic sometimes is not the best thing. You have to go below the speed limit and we realize that for driving in the slopes or the gradients, in clients in San Francisco, there are many of those. The human brain is trained to, or the human drivers are sort of in subconsciously, they slow down when they go downhill in those slopes. The autonomous vehicle doesn't necessarily have to do that if it's safe and if it's staying below the speed limit.
(15:31):
But we learned that this is a more natural driving experience and this is what our riders would also expect in terms of the experience. So that's something that we then modify the behavior on.
Lenny (15:45):
That makes sense. I would want it to slow down. On the other hand, if I feel like I could trust that, I wish there was a button to just crazy mode, just go for it. Kind of digging a little bit into the product team's way of working, what are KPIs that you all use to track progress? I don't know, either amongst some of the teams you lead or also just broadly progress on self-driving technology. How do you know you're making progress? Is it just miles driven as something else?
Shweta Shrivastava (16:12):
There are tons of these metrics that we analyze on a daily basis, weekly basis depending upon what the metric is. But if I were to categorize them in two broad categories, that'd be the commercial and operational metrics and the system behavior metrics. So, one important thing to note here is that we're in a proof of concept or a pilot phase anymore. This is the service that we are offering to riders. Paid service in Phoenix and also it's open to public in San Francisco, so it's an actual service.
(16:46):
And so, we're tracking the commercial metrics in terms of the trips per week, the daily or weekly active users and all the funnel metrics that you can think of. Also, the operational metrics, the cost, right? Well, how much is the thing costing us to operate? So that's, I would say, all the stuff on the commercial scaling side. And then on the driver performance, the vehicle driver as the technology name as I alluded to earlier, the driver performance metrics, they span across safety, the compliance to the road rules, our ability to make adequate progress as in not get unduly stopped or stranded in dense traffic situations as an example.
Lenny (17:32):
What are just specific metrics there? Anything you could share just like what is the actual goal in one of those teams?
Shweta Shrivastava (17:38):
The goal here is to be able to drive safer than humans. Now, we don't really have one standard human driving benchmark, safety benchmark, that everybody uses, but we do gather enough of that data. We have access to enough of that data to form an opinion on or a metric on or benchmark on what does human driving look like, how many collisions, as an example, a human driver would have every a hundred thousand mile. And then we want to make sure that our performance is better than that.
(18:19):
So that's simplifying, right? And several things go into both calculating the benchmark as well as our performance against that benchmark. But that at the core of it, that's what we're trying to do. So that's on the safety side and then I would say on the stops and strands, which is trying to, which goes in the different direction. Hey, you can be very safe if you're not moving at all. That's not what we're building. We need to make sure that the riders get to their destination on time. So it has to be appropriately assertive and be making the right progress.
(18:53):
And, so again, how much did the vehicle slow down unduly, right? Or, in how many instances in a given week did it have to rely on a rescue help? Those are the situations that we want to avoid. And then, how much did we slow down the traffic for other users? So we again do extensive benchmarking and look at the priors, et cetera, and really understand would an adequate performance be there and measure our own against that.
Lenny (19:28):
Awesome. Today's episode is brought to you by Elements. I just recently discovered this stuff actually from another podcast and it is such sweet, salty goodness. Element is a tasty electrolyte drink mix with a science-backed electrolyte ratio. And unlike most electrolyte drinks, there's no sugar coloring, artificial ingredients, gluten or any other BS. Getting enough electrolytes helps prevent and eliminate headaches, muscle cramps, fatigue, sleeplessness and other common symptoms of electrolyte deficiency.
(19:57):
Element is the exclusive hydration partner to team US USA Weightlifting and many other Olympic athletes. Also, dozens of NBA and NFL teams and players rely on Element to stay hydrated along with Navy SEAL teams, FBI sniper teams and the Marines. You can try Element totally risk-free. If you don't like it, you can share it with a salty friend and they'll give you your money back, no questions asked. To give it a shot, go to drinklmnt.com/lenny and you'll get a free sample pack with any purchase, which includes one packet of every flavor.
(20:27):
My favorite is watermelon salt. You won't find this offer publicly available, so you have to head to drinklmnt.com/lenny to take advantage of this offer. Stay salty.
(20:38):
I'm guessing you're not going to have an answer to when do we think we'll have fully self-driving level five autonomy. So let me ask you a different approach to that question of just what's most in the way of us getting to full self-driving where we don't have to do anything ever? Is it like miles driven? Is it like tech breakthroughs that still have to happen? Is it regulation and just cities being like, okay, it's fine. What's the biggest blocker at this point or bottleneck?
Shweta Shrivastava (21:01):
So let me share my opinion on the L5.
Lenny (21:01):
Cool.
Shweta Shrivastava (21:06):
So L for those who might not be very familiar with this term, L2, L3 is still very much driver assist. It gets to some level of autonomy but then it relies on the human driver at the wheel to be able to take over complex situations. L4 fully autonomous without a human driver at the wheel and no expectation of a human driver at the wheel. That's what we've been focusing on. L5 would be in any kind of road completely unstructured, off-roading in that kind of an environment, be able to drive without any map, without any priors, what have you.
(21:44):
And we believe that by offering the kind of service that we are offering in Phoenix and in San Francisco through the rest of this year and other cities in future is it helps realize that the dream of the fully autonomous driving, in a big way, without having to go to L5. So I think that the technology is already there. L5, I'm not sure, maybe that becomes more niche, et cetera. It solves very specific use cases.
(22:16):
In terms of the blocker, I would say, the technology is there, but it still needs improvements. Especially we were not able to drive in snow yet. Something that we have to tackle in future.
Lenny (22:25):
I could barely drive in slow.
Shweta Shrivastava (22:28):
Yeah. And I don't like to drive in snow. Even I, I avoid snowy days. But that is something that we still have to build as a capability in driving fully in snow now. So that's great.
Lenny (22:39):
Makes sense. Clearly, there's a lot of little things, a lot of big things and it's a really interesting point about we don't need L5, L4 is great for most people. Maybe a last question along this track and then I want to pivot to a different area. So Waymo's been this long-term investment for Alphabet and many PMs often try to create buy-in and keep buy-in for large investment and large project. I know this is a different scale of investment than what most PMs work through. But is there anything you've learned about keeping leaders bought in and excited and continuing to invest in a project for years and years? Specifically just like tactics that keep people excited and bought into a long-term investment?
Shweta Shrivastava (23:21):
Yeah. So first of all, we are fortunate that we have the backing from Alphabet and other investors. And the autonomous vehicle industry is interesting and I think the last year has been interesting with more consolidation happening. So I think the name of the game here is to show progress, show meaningful progress and meaningful progress, not just in terms of technology but in terms of commercial deployments. That is the rubber meets the road, if you will, phase off of the product.
(23:54):
And the results have to speak for themselves, for our investors to have the confidence in us. So notwithstanding what's happening to other AB companies in the industry, it's about what we are doing. And then look at the progress that we've been making and where we are headed. And the fact that we've been accelerating our milestones and going through our own expectations, I think, these are very positive signals to our investors as well.
(24:23):
Another startup as well, t's not about you have to do what's the right thing for the business. Your focus is on creating value for the customers, creating value for the riders. You have to build a business that makes sense and the investors see that too. Or we're not going to do something unnatural or something that doesn't align with the business goals in order to gain any short term brownie points with investors. I think it doesn't work that way and the investors will see through that too.
(24:52):
Definitely Alphabet has been our backer for forever. So, it's really about focusing on building the right business and doing the right thing for the users.
Lenny (25:03):
I think that's a great takeaway that if you're finding that there's a buy-in and continued support for what you're building, focus on momentum and showing success. It's pretty simple if you think about it. And it's hard to cut something that's just showing success. And so, even at the scale of Waymo, it's a great lesson. So that makes sense.
Shweta Shrivastava (25:03):
Absolutely.
Lenny (25:24):
We talked a bit about other companies you've worked at and so I want to kind of zoom out a little bit. And I just want to ask, you worked at Amazon, Cisco, Waymo now, startup you mentioned. What are just some of the biggest lessons you've learned about building successful teams and successful products?
Shweta Shrivastava (25:40):
In terms of the product, whether you're working for a big company or a startup, the core product management tenant is still the same, which is, you have to work backwards from the customer problem or the user problem. Building a technology for the sake of it doesn't really go that far, so you really have to focus on the, what are you building, who are you building it for and what problem are you solving?
(26:05):
And this applies in any context. And Amazon has this great process where the PMs have to write a press release for the finished product even before they start building the product. That's the first thing that they have to do is to write that press release like the product is about to launch today. What are you telling the users about that product? Really forces them to think about the value proposition more thoroughly.
(26:33):
And I know many other companies are starting to look at that practice as well, but I find it very effective.
Lenny (26:39):
Do you do that at Waymo or do you folks do that? Is there kind of a system there or?
Shweta Shrivastava (26:43):
The explicit PR FAQ process that Amazon follows is, I think, Waymo has its own version of it. But it is about sort of focusing on the customer problem. Now, Waymo is also a very different kind of product. It's highly integrated. And different types of product management flavors, if you will. Some are more technically focused and technically deep, some are more commercially focused. So they all adapt. They have their versions of working backwards from the customer problem. But that still remains the core tenant in my mind.
(27:13):
The other big lesson, at least working in some of the large companies that I have had is it's also very important to know what you're not building. And this one is not only in big companies, I would say even in startups, it's extremely important to know what you're not building because you could very easily get swayed by customer X telling you to do this, customer y telling you to do that. And a product that tries to be all things to all people usually doesn't end up going anywhere.
(27:42):
So that focus, that prioritization and being crisp about what you're building and what you're not building is very important. And then, in the context of the large companies, what I was going to say was, I think, is the classic innovator's dilemma. The large companies tend to be the market share leaders in their focus areas. And so, the product team and the product leaders can get very incremental in their product strategy and then lo and behold, you see an upstart that comes and disrupts them.
(28:16):
And so, I have definitely learned the lesson that you need to disrupt yourself before somebody else does because it's going to happen. It's inevitable. And large companies that are constantly challenging themselves and disrupting their own models or their own product capabilities to bring those, even something more transformational for the customers, are the ones that really succeed. And I think this is where the product leaders have to bring in that mindset of, hey, are we getting too complacent or it's time to just.
Lenny (28:46):
That's such a good reminder. Is there an example of you doing that or something you worked on where you got the company to commit to something that maybe could have been a threat from a disruptor or maybe even just seen that happening at a company? Just like is there a specific project or investment that comes to mind?
Shweta Shrivastava (29:02):
[NEW_PARAGRAPH]At Amazon, I was the first PM and then I drove the team around it for a no-code application development platform called Honey Code. So that was a brand new service. Amazon had never delved in that space before. It was more infrastructure focused and this was first of its kind service that the team worked on. And this has played out many times in my career, and so I am a big believer in disrupting yourself before somebody else does it.
Lenny (29:33):
What do you think is the most underrated PM skill that you suggest people, maybe especially early in their career, that they should focus on maybe that they're probably not thinking about?
Shweta Shrivastava (29:42):
I think the listening and empathy are the top ones. These are very important because I think when folks think about product management, they think about the influencing without authority and prioritization and being able to write with PR, et cetera, all those things are sort of more top of mind. The listening and empathy, I wouldn't say that they are underrated, I think is there's now a lot more recognition that these are sort of core skills if you want to be able to influence a lot without authority.
But I think it's easier said than done. You really have to come in with that growth mindset, with that beginner's mindset, be able to absorb and just learn and listen and don't jump in with ideas necessarily, right? Take the time to formulate that opinion to really learn and understand the customer and the market and really be true to that tenant of working backwards from the customer problem, not just say because it's become such a platitude now in the product world.
Lenny (30:42):
Yeah, there's a book. There's a whole book called Working Backwards now.
Shweta Shrivastava (30:46):
Yes. That is the one thing that I would say that somebody who's starting out as a product manager really try to follow that principle. And then listening and empathy is going to go a long way in terms of being able to do that.
Lenny (31:00):
On listening and empathy, what do you think helped you most develop those two skills?
Shweta Shrivastava (31:06):
So I think for me, part of it was just doing this over and over again in different environments, in different product launches that I have led in different types of companies that I've worked with. In startup as well as big company, the dynamic is different. And, again, the team that you're working with in different companies have a different culture. So, when you're working with let's say an engineering leader, being able to understand what are his or her constraints? Where is he or she coming from? What does impact look like to that person? And then understanding where you're aligned, where you're not aligned are things that you have to develop and start paying a lot more attention to as you rise in your career or go up the ladder.
[NEW_PARAGRAPH]And I think a lot of that for me came by just being in different kind of situations and different kind of environments.
Lenny (32:08):
Yeah. That's what I often say also, a lot of this just comes from doing it again and again and again. There's not going to take a course and then just I'm a great listener, I'm done.
Shweta Shrivastava (32:18):
Yeah, no, it doesn't.
Lenny (32:19)
Yeah, which is not easy to ... It'd be nice if there's a book you read and then you become a great listener and a great empathizer.
Shweta Shrivastava (32:24):
Well, I think one take or one that I could share is just challenging your own assumptions. So, I think listening with an open mind but then are you proactively trying to challenge your own assumptions is extremely important. As a big enough product manager as well as a seasoned product leader, if you're not doing enough of that, then I think you might not be listening well, right? Or you might not be picking on the cues. If there's no conflict, if there's no contention, then something is missing.
Lenny (33:03):
It's not often you're going to be always right.
Shweta Shrivastava (33:04):
Yeah.
Lenny (33:05):
Maybe one more question along these lines. You've been promoted many times, now you're in a place where you promote people and I'm curious for someone that maybe wants to get promoted or struggling to get promoted, what would you say are probably the reasons they aren't? Or what do you think people should focus on if they want to just get a promotion and many promotions in their career?
Shweta Shrivastava (33:28):
I'm going to say something that might sound a little cheeky, but I think the way to get promoted is to not want it too badly. It is about you have to focus on the impact. It's about having an impact and then doing what is right for the business. So not sort of optimizing things for your promotion, which look, we are all ambitious human beings. And there's nothing wrong with wanting a promotion, just to be clear, and there's nothing wrong with being ambitious, but then focus on the impact.
(34:03):
Are you working on the right things that will have the right outcome for the business? Because if you are and if you are giving it to your 100%, that will be visible. And making your ambitions known to your manager, to your leader, is a good thing that you should. And so, when the right opportunity comes, at least your leader or manager is aware that, hey, this person wanted to work on something more challenging, so maybe I put her on that project.

But you have to be focused on really creating the right impact for the company and not optimizing for yourself to get promoted. If you try to maneuver that too much, it becomes visible and it's not a positive signal to the organization when they can see that that's what you're trying to do. And it also distracts you from the things that you need to be focusing on. So, I would say, improve your skillset as a product manager. Make sure that you're made your vision known that you want to work on challenging high visibility projects or products that really test or stretch your skills and then be really dedicated to that cause and work on what has the business impact for the company, do the right things.
Lenny (35:15):
I really like that advice. I 100% agree with all of that. I have a couple final Waymo questions and then we're going to get to our very exciting lightning round. Just for folks that maybe want to try out Waymo, so maybe just like where's it live now? When do you think it'll roll out to new cities? And then, how do people try it and use it if they live in one of those cities? If that's possible.
Shweta Shrivastava (35:37):
We are already in the Phoenix metro area and in San Francisco. So in those cities you can just go and download the app and you can use the service. We have done initial fully autonomous testing in LA. And we're going to be expanding in LA through the rest of the year, so stay tuned for more development on that front. And then, we do have a list of cities that we're going to be rolling out in the coming years, but unfortunately, I can't share that list just as yet.
Lenny (36:04):
And if someone lives in one of those cities, is there a way they could try to get on a wait list or try to use this stuff or is it closed doors right now?
Shweta Shrivastava (36:11):
So it is open doors in San Francisco and Phoenix.
Lenny (36:15):
Got it. So you just sign up and you get on the waitlist and then you might get off?
Shweta Shrivastava (36:17):
In Phoenix, I don't even think that there is a wait list.
Lenny (36:20):
Oh wow.
Shweta Shrivastava (36:21):
On the waitlist.
Lenny (36:22):
I got to move to Phoenix. That's cool.
Shweta Shrivastava (36:24):
Or just wait, just yeah, a little while in San Francisco. But yeah, Phoenix is great. So, if you want to move there, that's totally fine.
Lenny (36:33):
No, I'm going to start packing tonight. Just joking. Anything else you want to touch on before we get to our very exciting lightning round?
Shweta Shrivastava (36:40):
No, I think we talked about a bunch of things. It's been a great conversation so far.
Lenny (36:45):
It's not over yet. We've reached our very exciting lightning round. I have six questions for you. Are you ready?
Shweta Shrivastava (36:51):
Bring it on.
Lenny (36:52):
Okay, here we go. What are two or three books that you've recommended most to other people?
Shweta Shrivastava (36:58):
Crossing The Chasm by Geoffrey Moore and Clayton Christensen's Innovator's Dilemma are still sort of the two classics in product management that I have quoted a lot and I have recommended to many folks.
Lenny (37:12):
Awesome. I've got both in my little bookshelf behind me.
Shweta Shrivastava (37:14):
Yeah, me too.
Lenny (37:15):
What's a favorite recent movie or TV show that you've really enjoyed?
Shweta Shrivastava (37:19):
I have an eight-year-old daughter, so my viewing choices are very much influenced by what she watches. But let's see, I did enjoy the Top Gun, the new Top Gun movie, Top Gun Maverick quite a bit. We watched it in the theater and visuals were just fantastic. I think it was also inspiring to see what Tom Cruise was able to do and it's quite a feat that he pulled off at this age. It was very inspirational.
Lenny (37:49):
Fully agree. Favorite interview question that you like to ask people?
Shweta Shrivastava (37:53):
Especially at the senior levels, I always ask them, when was one time that you failed and what did you learn from it? I've seen that folks who has either say that they've never failed or they're trying a success story as a failure story are usually, they're disingenuous or have not had the depth of experience. So I ask that question and I'm looking for some real solid examples there.
Lenny (38:21):
Awesome. What's a favorite recent product that you've discovered that you love?
Shweta Shrivastava (38:27):
I wouldn't say that I recently discovered it. It's on my wishlist to buy very soon. I'm all for sustainable mobility, so I am shopping for a foldable ebike so I can do more mountain biking without doing mountain biking. That's the sustainable part for me, I guess.
Lenny (38:47):
Is there a specific model or brand that you are most excited about?
Shweta Shrivastava (38:50):
I would take recommendations from you, but I'm still shopping. I think electric, there are a couple.
Lenny (38:57):
All right. Folks who have recommendations, leave suggestions in the comments.
Shweta Shrivastava (39:01):
Please do.
Lenny (39:01):
And what's something relatively minor you've changed in your team's product development process that you've found has had a tremendous impact?
Shweta Shrivastava (39:09):
I wouldn't say that this is a product development process, although, in different parts of phase of my career, I have definitely instituted different types of processes and tools that have helped improve the product development. But I would give you an interesting one that I use a lot in my prior company and then I use a different form of it here in Waymo is what I used to call as the rule of seven. If there have been seven emails in an email thread and you still haven't resolved the issue, just call the person or get in a room huddle, resolve it live.
(39:43):
But the long email exchanges that don't converge and go anywhere I feel are a waste of time for many people. So I'm like, you've got to a limit. Waymo is a bigger company, so the limit's more like 10, but if you haven't resolved something within an X number of emails, please just get on a call, get in a room and get it resolved.
Lenny (40:04):
I love that. And the idea is it's seven if it's like you and that person going back and forth seven times?
Shweta Shrivastava (40:09):
Yeah. Or all of people are just going back and forth. And then adding more people and then everybody chime in, but where is this thing really headed?
Lenny (40:21):
I love that. Final question. If anyone gets to ride in a Waymo, what's a pro tip for them to have an awesome experience?
Shweta Shrivastava (40:29):
Bring your favorite playlist, sit back and enjoy the ride.
Lenny (40:33):
Great. When I was on my right, I turned on some jazz and it was raining outside. It was real cozy.
Shweta Shrivastava (40:39):
But did you actually do it on the ... So, so there's a feature, if you have a Google, you have to download the Google Assistant, but you can actually play your playlist list in the car.
Lenny (40:49):
That's cool. No, I chose a station that was in there just like jazz music.
Shweta Shrivastava (40:52):
Okay. Yeah.
Lenny (40:39):
Yeah. Okay. This is great. All right. Hopefully I get another ride someday.
Shweta Shrivastava (40:56):
Yes, you should.
Lenny (40:57):
Shweta, this was amazing. I am going to start packing my bags for Phoenix. I'm going to sell my car. Everything's going to change
Shweta Shrivastava (41:04):
Exactly what we wish for.
Lenny (41:07):
There's your KPI. Thank you again for being here. Two final questions, where can folks find you online if they want to learn more, reach out, ask you maybe some questions, maybe apply to join Waymo if you're hiring, and how can listeners be useful to you?
Shweta Shrivastava (41:20):
You can find me on LinkedIn. And then if you are interested in opportunities at Waymo, go to Waymo career web page. You should see all the open positions. It's okay for you to reach out to me on LinkedIn as well for product management roles. How can listeners be useful to me? I would say, hey, sign up for the ride in Phoenix or San Francisco and LA when we open up, give us feedback.
Lenny (41:43):
Awesome. Shweta, thank you again for being here.
Shweta Shrivastava (41:47):
Thank you. It was great to have this conversation.
Lenny (41:50):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
