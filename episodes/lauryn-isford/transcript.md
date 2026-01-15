---
guest: Lauryn Isford
title: Mastering onboarding | Lauryn Isford (Head of Growth at Airtable)
youtube_url: https://www.youtube.com/watch?v=dLku0AiGPVA
video_id: dLku0AiGPVA
description: 'Lauryn Isford is a product growth leader and practitioner, who most
  recently led Growth at Airtable, and is about to start something new 🤫.  In today’s
  episode, we get into the many tactics...

  '
duration_seconds: 3861.0
duration: '1:04:21'
view_count: 18254
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- onboarding
- churn
- metrics
- kpis
- roadmap
- prioritization
- a/b testing
- experimentation
- analytics
- funnel
- conversion
---

# Mastering onboarding | Lauryn Isford (Head of Growth at Airtable)

## Transcript

Lauryn Isford (00:00:00):
An activation rate that falls in a lower percentage range, maybe for most companies five to 15%, is better than one that falls in a higher percentage range because it means that there's likely much higher correlation with long-term retention and you're really working hard to get most of your users to reach a state that they're not reaching today.

Lenny (00:00:24):
Welcome to Lenny's Podcast where I interview world-class product leaders and growth experts to help you get better at the craft of building and growing products. Today my guest is Lauryn Isford. Lauryn was most recently head of growth at Airtable. Before that, she was a product growth lead at Facebook, working on user growth, internet.org, and growth of Facebook at India. Before that, interestingly, she led growth for Blue Bottle's e-commerce business. In our conversation, we dive deep into Lauryn's favorite topic, onboarding, why it's one of the biggest and most undervalued growth levers, what she's learned about optimizing onboarding flow through her work redoing Airtable's onboarding flow, what she's seen work and common pitfalls around onboarding, plus a ton of advice around figuring out your activation metric. I could talk all day with Lauryn about growth, but we had to cut this off to keep this to a reasonable length. Enjoy my conversation with Lauryn Isford after a short word from our wonderful sponsors.

(00:01:19):
This episode is brought to you by public.com, who want to tell you about their new treasury accounts which earn a 4.8% yield on your cash. That is higher than a high yield savings account while still being backed by the full faith and credit of the US government. Treasure yields are at a 15-year high, but buying US Treasuries is super complicated if you go to a bank or navigate an ancient government website, or at least that was the case. Now you can move your cash into US Treasuries with the flexibility of a bank account, you can access your cash whenever you want, even before your Treasury bills hit maturity. There are no hold periods, no settlement days, just a safe place to park your cash and earn a reliable yield. Public will automatically reinvest your Treasury bills at maturity so you don't have to do anything to continue growing your yield, and you can manage your treasuries alongside stocks, ETFs, crypto, and any alternative assets. Do all your investing in one place and earn 4.8%, a higher yield than a high yield savings account only with a Treasury account at public.com/lenny.

(00:02:24):
Today's episode is brought to you by Miro, an online visual whiteboard that's designed specifically for teams like yours and mine. I have a quick request, head on over to my board at miro.com/lenny and let me know which guest you'd love for me to have on in 2023, and while you're on the Miro board, feel free to play around with the tool. It's a great shared space to work closely with your colleagues to capture ideas, get feedback, and iterate quickly and easily on anything you're working on. For example, in Miro, you can build out your product strategy by brainstorming with sticky notes, comments, live reactions, voting tool, even an estimation app to scope out your team sprints. Your whole distributed team can come together around a wireframe and draw ideas with a pen tool or even put mocks right into the Miro board. And with one of Miro's ready-made template, you can go from discovery and research to product roadmap to customer journey flows, final mocks, you get the picture. Head on over to miro.com/lenny to leave your suggestions. That's M-I-R-O.com/lenny.

(00:03:27):
Lauryn, welcome to the podcast.

Lauryn Isford (00:03:28):
Thank you. I'm so excited to be here.

Lenny (00:03:31):
We've chatted a bunch over Slacks, like all these different Slacks we're in and Twitter and emails, but we've never actually chatted real time, and so I have a million questions that I want to ask you. So, thank you again for being here.

Lauryn Isford (00:03:42):
We have never chatted real time, so everybody's getting the first conversation and I'm really looking forward to it.

Lenny (00:03:48):
I know that you have this pretty spicy contrarian take on experimentation and that I think you believe people run experiments too often and maybe not everything should be an experiment. Can you talk about that?

Lauryn Isford (00:04:00):
Yes. So, experimentation is a really big part, growth culture, growth hacking culture, PLG culture, growth marketing culture, any kind of growth, at least in my sphere, and sometimes teams can be really, really dependent on experimentation when trying to grow a business. A great example of this would be consumer growth at scale. Think your classic big social company. I worked at one of them. I am a former employee of Meta back when it was called Facebook. When you're at scale trying to grow a social app, experimenting can feel second nature. It can feel like a necessary step in your product development process that you want to drive more signups or you want to drive better activation with new customers. So, you change some buttons, change a design, and A/B test it, and then see if numbers go up or down, and then make your ship decision based on it.

(00:04:56):
I find that there's generally two reasons why a grow team wants to experiment, and one of them is to understand more precisely the metric impact of what they're building and what they're putting in front of customers, and the other is risk mitigation where you're making so many big dramatic changes that there's some risk that while this could be really great for the business, it could also be really bad and it would be good to understand that before everybody's experiencing that in production. So, with that framework in mind, sometimes you don't need to experiment. Sometimes if the business, let's say activation, right, activation rates go up 6% versus 7%, that precision actually doesn't help all that much beyond being able to say in your performance review, "Hey, I increased activation by 7%." So, it also is expensive to have folks on the ground, be it engineers, analysts, product managers, spending time understanding the results of an experiment that could otherwise be spent on road mapping, on foundational analysis, on shipping things. So, experiments can be expensive.

(00:06:09):
So, with all that said, generally my advice is to experiment when you need to and to primarily see it as a risk mitigation tactic when you're making dramatic changes and to let the product development process do more work. So, spend more time with customers, be more rigorous in understanding precisely what problem you're solving, get mocks in front of people and see how they react, and hopefully have more conviction than you otherwise would when you ship something that it's okay if every customer sees it tomorrow and that the experiment doesn't actually matter as much.

Lenny (00:06:44):
It's so interesting hearing that from a head of growth person. Working at Airbnb for a long time, and you talked about this, there's so much value put into the amount your experiment moves the metric is so important to, like you said, your performance review, your team's status, your team's ability to show they were successful. People look at like, you drove this metric 14%, which oftentimes you add up from experiments you've ran. How do you work in a culture like that, or is it just in that culture you may as well run experiments because that's the only way you get credit for the work you do, or is there a way to just be like, "Wow, that is how we measure it, but it's still maybe not worth running everything as an experiment"? How do you kind of find that balance?

Lauryn Isford (00:07:29):
It feels to me like that is the default culture, especially as growth teams become organizations and as those organizations grow with companies into growth stage public company territory and beyond. However, I do think you can build a different culture, and the only way to escape the trap of experimenting everything is to have a very intentional culture about doing right by customers and doing the right thing for the business. A growth team or a growth org exists in service of improving the business and delivering results for the business, and whether or not you measure those precisely in an A/B test, you still shipped them or you didn't.

(00:08:09):
So, the rigor around your process was either there or it wasn't. This means though that there have to be other ways to motivate, reward, retain, and develop really good talent. So, a culture around the impact you had on customers as measured by qualitative feedback or as measured by deals that were closed or deals that weren't lost, or other kinds of indicators that you did the right thing for customers is important and there shouldn't be, especially in engineering within the world of growth, a culture around having to point to numbers to demonstrate your impact because if there is, then the team will biased experiments all the time, and that's not necessarily the right thing for the business. It's a very expensive cost.

Lenny (00:08:50):
Wow. It's so wild hearing this from, again, a head of growth, someone that's so analytical like you. Is there an example of something you launched that maybe most people would've run an experiment and you decided not to for one of these reasons?

Lauryn Isford (00:09:01):
There is a feature, a product really, that Airtable offers called Airtable Forms. It's possible you've used it. I'm not sure if you have, but-

Lenny (00:09:10):
No, I don't think so, but I will go check it out.

Lauryn Isford (00:09:12):
You can check it out. There are some new features I'm about to tell you about, so maybe that will entice you.

Lenny (00:09:16):
There we go. Scoops.

Lauryn Isford (00:09:18):
So, Airtable Forms is much like other forms products. You can create a form and then send it to anybody to submit. The people who submit your form don't need to be a user of Airtable.

Lenny (00:09:30):
Oh yeah, I have used that. Okay. It's just like the turn an Airtable into a form. Yes, I've used it. Okay.

Lauryn Isford (00:09:35):
Exactly. So, something we noticed is that there was a gap in feature parity for Airtable Forms where the submitter could not request a copy of their submission. So, I might send my T-shirt size to Lenny for a form around ordering swag for the company and then I might want to remember which T-shirt size that I ordered and get a copy of that in my email. We created that feature which as a result was gated on creating an account with Airtable, and we just turned it on and wanted to see what would happen because we knew from rigor of a wonderful product team doing robust customer analysis and also doing the data work that this is something that people wanted, that it was a feature that would bring value to customers, and that even if it didn't move certain metrics like a signup percentage, even if it might affect the mix shift of activation rate from folks who signed up, it would be net good for customers who were using forms and who were submitting them.

(00:10:35):
So, we did roll that one out without an A/B test. It did have a big enough impact on our signup metrics that we saw at top line and didn't need the A/B test to see what was happening. And we also were able to use attribution to make some analysis possible after we rolled it out so we could learn from what was happening to the base afterward.

Lenny (00:10:53):
Fascinating. That's a really good example, and I imagine that helps a lot when the head of growth is encouraging the team not to run as an experiment versus a PM on a subteam, like, "Nah, we don't need to run this as an experiment," because in that case you're already acknowledging that team, "You did a great job, look at this metric. Clearly this one moved. Clearly customers want it." So, to your point, basically this kind of stuff has to come top down probably for it to work well.

Lauryn Isford (00:11:15):
I think it does, and it also cannot be an excuse for rigor around building well and being precise in what customers need, but overall, if you can be a results-oriented organization that just wants to do the right thing and move with urgency, then in my opinion, that's the way that you can have the most impact.

Lenny (00:11:33):
Cool. Okay. I didn't expect to spend that much time on that question, but there's so much there. That was really interesting. What I want to spend the bulk of our time on is onboarding. Something that I found myself, and I think you agree with a lot of this but I'll confirm, is that I've done a lot of research into the growth stories of the most successful startups, and what I find, one, is that retention ends up being the thing you got to crack. If you can't crack retention, nothing else matters. And then, two, more interestingly, onboarding ends up being one of the biggest levers to increasing retention which basically A then B equal C, onboarding ends up being one of the biggest areas of opportunity for growth teams both early on and late stage. And so, I guess the first question, would you agree with that general sentiment that onboarding is this huge opportunity and often undervalued?

Lauryn Isford (00:12:22):
Yes, I definitely agree. It depends of course on the shape of business. Not every business should prioritize onboarding first, but if you have some sort of self-serve element of your product, if someone can give your product a try, maybe you have a playground or a sandbox demo, if there's a premium element to your pricing scheme, if you maybe offer things totally for free and don't even have monetization yet, onboarding is that first really important choke point that from which downstream of onboarding so many important metrics and results flow for the business, from converting someone to a paid customer to closing a deal to growing, how many people in an organization are using your product. So, all of that really comes back to onboarding and if you can get that right, lots of good things will follow.

Lenny (00:13:13):
Okay, great. I'm glad we agreed. I already know this, but you spent a lot of time on Airtable's onboarding flow.

Lauryn Isford (00:13:20):
Yes.

Lenny (00:13:21):
And so, I'm curious just to learn about what did you do over the time that you spent optimizing Airtable's onboarding experience, what kind of impact did you see through the work that you did there, and then just any big kind of general takeaways that either you think people should know or that you'll take with you to future opportunities around optimizing an onboarding experience?

Lauryn Isford (00:13:43):
We could talk about onboarding all day. This is one of my favorite things to chat about recently. So, we did have a wonderful activation team rebuild Airtable's onboarding flow over the past 12 to 18 months. This included many projects, including several big ones. So, what you've probably experienced if you signed up for Airtable recently or what you might experience if you create a new account soon is we've built an immersive wizard that we called Guided Onboarding that helped guide you through setting up your first workflow on Airtable, and in doing that reduced the cognitive load of getting started, helped you make more progress faster, and created scaffolding that more than 90% of customers would benefit from to be able to get up and running on a product that's pretty complicated. That was the first piece.

(00:14:39):
We also then introduced some personalization to use case on top of that. So, instead of helping you build something generic, having you build something that's relevant to you. And then we also worked on ongoing education. So, once you're in a workflow, once you've built something, how do we help you level it up to go from beginner to intermediate to advanced? One funny anecdote about this is that we actually called that project The Mole, M-O-L-E, because the design pattern in product looks like a mole. It pops up from the bottom of the screen and gives you tips as you're exploring. So, those are some of the biggest changes we made. We did retire a bunch of our tooltips which were a big part of onboarding for a really long time. So, happy to chat more about that, and then also did a bunch of more incremental optimizations as well. In general, tried to take a portfolio approach to what we did.

Lenny (00:15:36):
Cool. Okay. A few questions real quick.

Lauryn Isford (00:15:38):
Yeah.

Lenny (00:15:38):
What were the three buckets real quick? So personalization, ongoing education, what was the first one?

Lauryn Isford (00:15:38):
The first one was guided onboarding.

Lenny (00:15:38):
Guided onboarding.

Lauryn Isford (00:15:38):
Exactly.

Lenny (00:15:46):
What was the impact of this work, just to give people a sense of the kind of impact you can have on conversion and then whatever other metrics you looked at there?

Lauryn Isford (00:15:53):
We were working on activation for a few years before I arrived at Airtable. There was already an awesome activation team, hard at work. Overall, the investments we made in onboarding over about a six to eight month period that included the wizard, The Mole with ongoing education, and also some personalization together drove a 20% lift in activation rate for Airtable.

Lenny (00:16:20):
Wow. That sounds quite impactful, especially at a company at that scale.

Lauryn Isford (00:16:24):
It's awesome. I would say celebrate any clear statistical significant improvement in activation rate. It's a big victory, and credit goes to the team that really spent many, many hours with customers and designing precisely to build something that could have that big of an impact. I think it speaks to the importance of really understanding what a user needs to be onboarded well, which is not the same as what your business wants the user to be onboarded to. So, delineating those and building carefully is really what made it successful.

Lenny (00:16:57):
Which of these three buckets would you say had the biggest impact? Because I want to kind of get a couple levels deeper to get to what exactly did you do that worked really well.

Lauryn Isford (00:17:05):
I would say that the guided onboarding wizard which is the immersive wizard that helps you figure out how to get started was the most impactful thing we did.

Lenny (00:17:14):
And it's interesting that you had tooltips and this feels like a tooltip-y thing. What is it conceptually? What's the simple way to think about the onboarding wizard versus a bunch of tooltips telling you like, "Hey, Lauryn, click here, next go here, and then check this thing out"?

Lauryn Isford (00:17:26):
Totally. Imagine being in a step-by-step guide where you are asked question, for example, pick which kind of project you're working on, pick what kinds of things you'd like to track for this project, and then as you select from beautiful, easy-to-click buttons that require very little work on your part, something is visualized for you on the right half of the screen. So, you can see your workflow visually come to light as you do the work on the left half of the screen, and all of this is done for you in a very guided and instructive way.

Lenny (00:17:59):
Are there any generalized learnings from that experience of just how to do a great onboarding experience? It sounds like probably avoid tooltips, instead just kind of ask questions and show them progress as they're going through it in kind of like an immersive experience versus here's the product, check out all the cool features.

Lauryn Isford (00:18:18):
I think there is something to be said for reducing reliance on tooltips, but I'm not sure I would go so far as to say the tooltip is dead, as much as I maybe would like to because there are too many of them out there. The reason for this is that I do believe Airtable's customers had a very specific need which was that the effort required to build basic scaffolding was too much and they needed more support, guardrails, bumpers to help them through that, and this kind of guided or immersive wizard was the best mechanism we could come up with to reduce that effort required and to make them feel more supported in their journey. I'm not sure that this pattern is one that works for every product. I think it's one that works well for a complicated product, where figuring out where to go next and how to get started is actually very challenging or has a high cognitive load.

(00:19:14):
So, I would keep that in mind, but in this case, it did work really well for us. I have seen some other products in the wild adopt similar patterns which gives me confidence that it is transferrable beyond Airtable and that there's probably something to it. That's definitely a big learning. I think one other big learning for us was that we had to meet users where they are. We have some awesome advanced features of really cool stuff you can do with Airtable, automations being a great example. However, users don't necessarily need to get that started on day one. They don't need to learn about the advanced stuff when they haven't even looked at a workflow before. So, we really worked hard to prioritize what the user actually needed and to consider what was necessary education versus what could be ongoing education and building it up.

Lenny (00:20:06):
Can you talk a bit more about what that was? What did you actually do to understand the type of user, and then what did you change for them? Because we actually did something like this at Airbnb, and it was a tiny bit successful for host onboarding but it wasn't anything big. And so, I'm curious what it is you specifically did. Did you ask them a few questions and then grouped them in a group and then changed the way the rest of the flow went, or, yeah, what'd you do there?

Lauryn Isford (00:20:31):
Good question. So, at the very, very beginning, we sort of said new users broadly need help. Who are they? What do we know about them? How can we help them? We spoke to a bunch of customers and also watched them get started and looked for patterns in behavior and also clusters. So, someone who is familiar with databases, somewhat technical and prefers to and has experience in building things might have a different need from onboarding than someone who is exploring a tool that was recommended to them for a project minute. With that in mind, there were some clear segments of personas or buckets of users that we could split out to give different experiences. Now that said, when we rolled out the guided onboarding wizard, it was actually just one generic onboarding that was one-size-fits-all, and while escape patches are great, we felt like we could solve, as I think I referenced earlier, more than 90% of use cases or users needs with one generic onboarding to start and then we could personalize from there.

(00:21:34):
When we started to personalize, generally we found bucketing customers by their learning style and their building style was more effective than more classic segmentation, like do you work in marketing, do you work in product management, do you work in operation. The reason for this is that there are many different types of building or workflows that are possible in Airtable. Some are sophisticated for use at work, some are simple for use at work, some are somewhere in between and are for a hobby use case or a consulting use case. Knowing how someone would go about building was more effective than what do you actually want to see on the other side.

(00:22:19):
This means that something like a template which can give you an example of how to build a use case for project management can be helpful for inspiration but might not actually be the best way to teach you how to use a product like Airtable, when instead, we could learn that you're someone who needs more familiarity with databases to be able to get to the next level, or who might need a more visual learning experience instead of a more data-forward learning experience. So, we tried to segment the experience that way and found that that yielded better results on activation than some of the more traditional segments.

Lenny (00:22:52):
And how did you decide which segment that a user was in? Was it a question you asked them right at the beginning?

Lauryn Isford (00:22:57):
We had a really awesome research team that would do some surveys and conversations with customers away from our production experience and away from individual projects. So, we had a really robust read going in to the project of who these different personas were, different building types, different learning types. That said, we do also ask folks when they sign up some questions and depending on who you are or what we might think we know about you or want to know about you, we might ask you different questions and that's in service of helping you get started.

(00:23:27):
I had some big ideas for how we might bring this to life even further that might come to life in the future, such as if somebody's there to just help out, if they're may be a teammate rather than a builder, if they're just there to work with someone else because Lenny invited Lauryn to work on her table because he needed Lauryn to do something or update a sprint, whatever. Lauryn needs really different onboarding than Lenny. So, actually getting that data in the flow is really useful because then we can route customers to a fully different experience. It's amazing how much low-hanging fruit there is to personalize and segment that onboarding experience in so many products that are out there. You just need to be really detail-oriented and precise on who you're working with.

Lenny (00:24:11):
You talked about this experience as activation, and so just digging a little bit further into that idea. One of the important kind of metrics, milestones you got to figure out when you're working on onboarding is what is an activated user, what's the activation milestone, what's the activation metric. I know you have some strong opinions and some really interesting insights into activation milestones based on your experience at Airtable. Can you chat a bit about that and just share what Airtable's activation metric ended up being?

Lauryn Isford (00:24:37):
Yes. So, overall, every growth team needs a north star metric. It's so important to have singular focus on what the business results are that you are working to drive in your team. On our activation team, which as I mentioned focused on onboarding, though in theory there could be other ways that you want to focus on driving activation, we had one north star metric which was what we called our team activation metric. So, this representative, a team of people were activated on Airtable's product and using it in a way that suggested they would be long-term retained. For us, that was week four, multi-user, meaning in the fourth week, more than one person on that team is active and contributing to a workflow on Airtable.

(00:25:23):
This metric is something that our wonderful analytics team determined to be highly correlated with long-term retention. It's also a metric that holds a relatively high bar, so it requires a number of things to be true, that something of substance has been built, that people persist and continue to collaborate, that they're collaborating on a weekly cadence, and also holds a relatively high bar on exactly how they're contributing, meaning that the sum total of this is somewhat hard to achieve which means that we have a hard job and also a high bar as an activation team to achieve that for as many customers as possible.

(00:25:58):
In general, I think an activation rate that falls in a lower percentage range, maybe for most companies five to 15%, is better than one that falls in a higher percentage range because it means that there's likely much higher correlation with long-term retention and you're really working hard to get most of your users to reach a state that they're not reaching today.

Lenny (00:26:22):
I really like that heuristic. So, the idea there is when you're picking an activation metric, you want it to be in the single digits potentially because you're saying that's more likely to be correlated with retention because retention's probably pretty low long term. Is that kind of the rough idea?

Lauryn Isford (00:26:38):
That's a rough idea. Of course, the metric should be correlated with retention no matter what, but if 40% of your customers are still active at week four maybe with a metric that would be week four active rate, then only a fraction of those are still going to be active in month 12, in month 18, and month 24, and I would much prefer to pick a more specific, more precise metric that maybe only 5% of users reach, but know that those 5% of users will be with us for the long haul, and if we could get that 5% even to 6% or 7%, it would have huge downstream effects on long-term metrics for the business. So, that's why I would opt for a more specific metric.

Lenny (00:27:22):
Okay. So, this activation metric, week four multi-user active is a really interesting metric. Can you talk a bit about how you actually operationalize this and put this to work on your team to help people understand what to work on and make sure they're moving the right sorts of numbers?

Lauryn Isford (00:27:39):
Totally. So, one of the first things that we did when me and my team started to revisit week four multi-user active right before we started to rebuild onboarding is break that metric down into all of its component. So, if you really think about what goes into that number, how many teams sign up as a team versus as an individual, how many of them make it to week four, how many of them have more than two people invited versus more than two people who've ever been active, versus more than two people who were active in the fourth week, maybe they have one person active in the fourth week, and then what does active mean, and what are the different kinds of behaviors that constitute contribution or being active. Doing that really detailed work on the metric helped us understand what levers we could pull to have a really big impact on activation overall.

(00:28:34):
Additionally, we actually started using more metrics. So, we didn't just use our activation rate metric week four multi-user active to make all of our decisions. We introduced a few more, and one of them with purely a retention metric for an individual. Are you week two retained? Are you week four retained? The other was what we called Build with a capital B, and this was roughly a sophistication score. So, for someone who's building something, have they reached sort of intermediate levels of use of Airtable? The reason why we added these metrics is we were building new mechanisms for onboarding that were helping users build more effectively and find more value in Airtable, but sometimes those treatments helped users become more sophisticated but didn't help them invite more teammates, or sometimes those new mechanisms made someone more interested in giving us a shot for a few more weeks, but what they built was actually not any more impressive than if they had done it on their own.

(00:29:38):
So, this group of metrics actually really set us free. It gave us those constraints where we could actually measure success in a few different ways and think about activation as being more complicated than just a single metric and celebrate anything we could do to help on a couple of dimensions. So, I know it's a little unconventional to have a few metrics that you work with, but we did find that that was really helpful when we were making big changes.

Lenny (00:30:04):
That is actually really interesting. So, it makes it feel like the core activation metric you talked about was more of an output metric and you kind of realized here's the things we could actually be moving directly. Is that roughly how you thought about it?

Lauryn Isford (00:30:15):
Exactly. It also helped us grapple with some of the tensions we felt which I know a lot of teams working on activation and onboarding feel, which is picking one metric doesn't paint the whole picture of what you're trying to achieve when you help a user onboard to your product and when you educate them about what's possible. So, in having sophistication and retention and an element of team use all as part of the fabric of how we talked about activation, it made us much more well-rounded as a team.

Lenny (00:30:46):
That connects a bit to, so we worked on this post together about how to choose an activation metric and you shared part of this story for that post, and there's a little bit of a debate amongst folks that contributed their opinion on how to decide an activation metric, where it's a debate between is it okay to have a workspace activation metric where it's like how many boards somebody creates, how many Airtables somebody has created versus a user action, like user has created 10 tables or user using it two times a week. I think you're on the side of workspace is maybe a more interesting metric for a collaboration tool, and it's interesting that you end up with both in the end which I think is kind of where folks landed. You probably look at how's the company using this tool and then per user, are they using it consistently. So, I guess the question is just what's your take on user specific activation metric versus workspace level activation metric?

Lauryn Isford (00:31:39):
I really like this question. I agree it is a great debate. I'm not sure there's a clear answer because it does depend on your product. In the case of Airtable, which is a product that has seat-based pricing and generally horizontal adoption, it totally makes sense to have a workspace activation measure because you want to understand in an account, in an organization how many folks are actually using a product and finding value. That can be different for tools that might look like Airtable but have different mechanisms for growth or different pricing or different vertical personas that tend to adopt it. So, I do think there is some variance. I do have a reaction to share with you that's a little spicy-

Lenny (00:32:19):
Please.

Lauryn Isford (00:32:20):
... is that it's important that growth teams are agile and this means that north stars, key metrics, focus metrics will change, and if you're working on the same metric forever, there's probably some inefficiency in actually chasing the biggest impact for the business. So, I would be open-minded about if a workspace or team or account activation metric is always the right thing to focus on. Team activation looks really healthy because your growth team did some really amazing work on it, maybe user retention is the right place to focus next year. Maybe it's more about conversion. Maybe it's more about some other signal for long-term retention, and I would be open to being dynamic and changing that metric over time. Stability in metric is great, it helps with momentum, it helps with building expertise, but sometimes we overfocus on picking the perfect north star metric and by the time you feel like you've found the perfect one, it's actually time to move on to something different and work on a different opportunity.

Lenny (00:33:24):
This episode is brought to you by Eppo. Eppo is a next generation A/B testing platform built by Airbnb alums for modern growth teams. Companies like Netlify, Contentful, and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern grow team stack. This leads to wasted time building internal tools or trying to run your experiments through a clunky marketing tool. When I was at Airbnb, one of the things that I loved about our experimentation platform was being able to easily slice results by device, by country, and by user stage. Eppo does all that and more, delivering results quickly, avoiding annoying prolonged analytics cycles, and helping you easily get to the root cause of any issue you discover. Eppo lets you go beyond basic click-through metrics and then set you to north star metrics, like activation, retention, subscriptions, and payments, and Eppo supports test on the front end, the back end, email marketing, and even machine learning clients. Check out Eppo at geteppo.com, get E-P-P-O.com and 10x your experiment velocity.

(00:34:34):
Is there an example of that that comes to mind when you talk about being a little stuck on a metric? Is that something you went through at Airtable or anywhere else you worked?

Lauryn Isford (00:34:43):
I've gone through it plenty of times. We actually at the organizational level on the Airtable growth award changed our north star metric a couple times which is a big deal that manifests for several teams. Roughly the arc of that change for us was shifting from being a growth org focused on revenue to a growth organization focused on user growth and customer growth. This for us was a really important moment where we decided that it was most essential in our work to grow the business to bring millions more people onto the platform, using the product and finding value in the product, because we were taking a decade's long view that they could always become monetized or converted customers later, and there wasn't really a rush. We felt that focusing on revenue led us to make some decisions that were a bit more short-term oriented than would be ideal.

(00:35:39):
There's also a dynamic here where in the world of enterprise SaaS, the world of B2B SaaS, there's a new theme called product-led sales that's very hot right now, and this means that often in a PLG company there's some ideal end goal of handing off certain customers to have a sales conversation or to close an enterprise contract. In that case, you might actually prefer to delay revenue for months or quarters or years to manifest it later, and when that's the case, your growth team should be fully aligned in lockstep with sales and with go-to-market team and focusing on user growth is actually the right call. So, that's an example of a big pivot that we made, and in doing that, we felt more strategic clarity and were able to move faster.

Lenny (00:36:25):
That is an awesome story. How long did that process take and any advice for folks that might be going through a similar journey of maybe we should rethink our north star metric not and not be revenue? Any advice there?

Lauryn Isford (00:36:36):
In general, I would say having stability in north star metric for at least six months feels like table stakes to me and that's for the reasons that I cited before, for building momentum, for building domain expertise, and also for compounding impact in areas where you see success, where you notice growth flywheels that you can optimize. However, if you're reaching a point where that north star metric feels like it's old news, maybe you're outgrowing it, maybe you want to work on different things, I think that's great. Be open-minded about changing it up. I would generally try to start with the mechanics of the business and what you think you might be able to drive in terms of metric impact with the resources you have on your growth team. That can look different for every growth team because some of them have marketing, some are more product and engineering, some are kind of a mix of both or even something different than that.

(00:37:27):
So, I would start with what impact do we think we could have? Where do we think the biggest opportunity is to chase? You can literally draw a funnel on a whiteboard and map it out and brainstorm together, do some analysis on the side, and when you see what opportunity feels like the most important thing to chase, try to build a north star metric that reflects the output of that work, rather than drives all of your decision-making from the beginning. A north star metric should really be a measure of what you plan to do, the strategy you plan to deliver is delivering results for the business on the other side, rather than the other way around.

Lenny (00:38:05):
So, you mentioned trials and freemium at one point and I want to spend a little time on this, and I know you also have some strong opinions about this kind of debate. Another debate people have, there's always debates in growth, between offering a trial or offering a freemium product, self-serve, and I think your perspective is you should do both, and I think maybe you call it a reverse trial because I was doing some research. So, I guess is that true?, Is that how you see the world, and then just generally, why do you believe that that is the right approach?

Lauryn Isford (00:38:31):
What is it about all these growth people with their strong opinion?

Lenny (00:38:34):
Right?

Lauryn Isford (00:38:35):
I guess I have so many of them. You're educating me on my own perspectives today. Freemium and free trials. So, to get on the same page with definitions for all of our wonderful listeners, a free trial is when you can use the product for free for a limited time and then your only option beyond that limited time is to pay for use of the product. Freemium would be when there are multiple options for how to use the product and one of those options is an infinitely free version of the product. So, you can use Airtable for free forever or you can pay some amount and have access to premium features.

(00:39:14):
So, with all that in mind, personally I'm in the camp of offering a reverse trial. Funky name, but what that means is offer a trial but also offer freemium. Do both. The reason why I like this is you get an opportunity when somebody shows up and says, "Hey, I'm going to give your product a try today," to show them everything that's possible. Onboarding is a huge component of that. Help somebody get started, have those aha moments and experience initial value, but also this is your moment to showcase everything that can be done with your really cool product, and you have some limited number of days, maybe seven days, 14 days, 30 days, to showcase all of the cool things that your company is building for your customers. That is the beauty of a free trial. It's not just that someone can try your product without paying. It's that they can try even more of the product, all of the premium, amazing advanced offerings that could be possible if they decide they want to settle on a premium plan.

(00:40:17):
When you are deciding if this is something you want to do, I would actually take a big step back from looking at competitive pricing pages and getting into the details and reading blogs and just think about what your philosophy is as a business on monetizing customers. The reason for this is generally the reason to offer a free plan or a free trial but really a free plan, the freemium type of pricing model is if you value letting millions, tens of millions of customers give your product a try, even if they never pay you a dollar. That shows to me prioritization and value of user grab, brand awareness, and exposure of your product more than just revenue. And if that's the case, a freemium pricing structure can be really great for your product, and it give you the space to see if your product can become that household name that everybody is familiar with and can give a try and get some early value and even experience some aha moments.

(00:41:24):
On top of that, you can offer a free trial to show what's possible with premium value and then that really can just be focused space for you to say, "Hey, look what's possible if you pay us $5 a month, $10 a month," and you might even get some extra conversion out of that and some more paid customers. So, in general, that's how I think about it. I like the reverse trial because user growth is important and if you're in a long game where you're trying to grow a business for a decade or more, ideally you're trying to get millions of people onto your product and you can always have that monetization conversation later, but you only get a couple moments where you can say, "Hey, pull out your credit card or let's get on the phone and talk about an enterprise contract," with a customer before you lose trust or lose patience. And so, that focus on helping them discover value and build loyalty to you is much more important.

Lenny (00:42:13):
I really like this concept, a super cool name too. I'm also thinking back to some of the SaaS tools I've used that have had this where I go straight into the pro plan and then I'm like, "Oh, I don't want to lose all these features," and then I actually end up buying it. So, when I'm hearing this, it sounds to me like it's a better version of the freemium approach. I imagine there's still many SaaS tools that are very enterprise-y, take handholding, maybe this goes away. I know Elena Verna who's been on the podcast is just a huge proponent of everyone will be product-led, self-serve eventually, but until that day they're still like, I don't know, I think of Retool I think is very hands-on, handhold-y, front I think is like that. There's all these tools that people don't get really quickly.

(00:42:57):
And so, I guess do you still think there's a need for some of these tools that need sales and customer success involvement to stick with just trial at least for now, or do you think they should all kind of find a way to get to self-serve and a reverse trial?

Lauryn Isford (00:43:12):
I do really agree with what Elena said. I really look forward to the day when self-serve and freemium are possible for every product, but I also recognize that that can be really expensive to build and implement and is not for everyone. So, that's cool too. There are other options. In general, I think freemium and also free trials tend to be most effective when there's something that the person who signed up can actually do on their own without being handheld. It doesn't have to be full functionality. It can be exploring a sandbox or a demo or something they can poke around in and experience value, see that aha moment. That's great. That's a moment where you can give value to that person who's chosen to spend time with your product. If that's not possible, there are different ways to be creative that don't require having premium pricing. You can think about how to use concepts related to PLG and related to top of funnel adoption in different ways.

(00:44:16):
So, maybe you can create custom landing pages or experiences that help showcase value without a full signup or free plan or free trial experience. Maybe you give folks the ability to sign up and while they've sort of signed up as an interested customer, they're not fully experiencing things, they might not even have the option to pay for something yet, but they can learn. There's some resources. There's some education for them to experience. Or, maybe you can think about top of funnel adoption or traffic as being most helpful for extension within customers you already. So, if you've signed contracts with a couple really large Fortune 500 companies and somebody wants to join and signs up on your website from the same email domain, then you can provide an experience for them that might feel like it helps them learn the mechanics that's actually only available to folks who are part of organizations that already have contracts with you.

(00:45:19):
It's a different way of thinking about PLG and not necessarily something you would offer for free, they're already an enterprise customer, but some of those concepts can still have a lot of value and help you grow the footprint of an account in an organization, and those are definitely awesome things to try if you can't offer something self-serve.

Lenny (00:45:36):
So, what I'm hearing is find ways to make things some component of it self-serve so that you don't need to necessarily talk to someone immediately. They can start to understand some element of it on maybe an interactive planning page or some very simple part of the product.

Lauryn Isford (00:45:50):
Exactly. I think the key is to figure out what it would be like for someone to experience value when there's no human sitting next to them, and that value doesn't have to be full functionality of the product.

Lenny (00:46:02):
Awesome. Coming back to onboarding, and this is my last onboarding question, I have another topic I wanted to touch on. Do you have any just general pieces of advice, either probably this will work if you're working on onboarding/things that probably won't work and are common traps that people fall into when they're trying to optimize onboarding activation flows in general?

Lauryn Isford (00:46:26):
I do see a very common trap that I would love to caution against, which is that employees of a company build onboarding for customers, but they build what they think customers want rather than what customers actually want, and that manifests in an onboarding experience that's not very helpful. So, there are two patterns that I typically see. One is naming features. So, imagine you're using Airtable for the first time and you see a tooltip and it says, "This is automations," and it explains what automations is to you. That's not that useful for a user who doesn't really know what's going on yet because they aren't sure if automations are relevant to them, if they're suited to their use case, what exactly the word automation entails. We've named a feature, but it's really sort of an announcement of something awesome that Airtable built, rather than an application that can help educate the user on how they'll receive more value from that feature. Try not to name features. It can be very tempting in practice, even though it sounds easy in theory.

Lenny (00:47:32):
Before you move on, what have you learned about how to actually name things in such a way people understand? Is there some you do there?

Lauryn Isford (00:47:39):
Ooh, naming things in a way people understand.

Lenny (00:47:41):
Versus the feature name, like you just said.

Lauryn Isford (00:47:43):
So, instead of that, I think what would be more useful, given the constraints of using a tooltip that's pushing someone to try an automation would be to explain how the automation is relevant to them, or even better, to enable a one-touch turn-on of the automation feature or set up an automation to complete your workflow where we actually do some of the work and if you click into here, we will show you what value is possible and help you get it to the finish line. So, really focusing on that contextual application or helping to drive towards an outcome, rather than just educating on a name.

Lenny (00:48:23):
And there's an element of smart defaulting, just like starting to do it for them versus do you want this or not.

Lauryn Isford (00:48:29):
Exactly. There's also an element here of segmentation or personalization where you should be sensible about if everybody needs to know what an automation is or if there are only certain folks who actually need to learn about it and others might not need to know.

Lenny (00:48:42):
Awesome. All right. Back to your other suggestions.

Lauryn Isford (00:48:46):
Oh yes, there is one other suggestion which is if you're working on a SaaS product, especially a freemium product, there's probably some pricing and packaging scheme that explains which features are available for free, which features are not, how many you get, and sort of maps out usage of the product, both for free users if you offer a free plan, and then for premium users if you offer premium plans. I find sometimes teams working on onboarding will map onboarding to that pricing or packaging. So, for example, maybe automations, to use the same example of the same feature, is something that's generally premium, that if somebody uses automations they're more likely to be a paying customer. It can be tempting then for an onboarding team to try to push automations to people when they're getting started because of course, we'd prefer if customers use premium features because then they might be more likely to become premium customers, but that is not in the best interest of educating a user on how to get started.

(00:49:44):
So, I do think it's very important to be careful that you are rooted in the customer need and rooted in helping that customer achieve maximum value, rather than sitting in the priors of what your packaging scheme might suggest or what might be in the best interest of the company.

Lenny (00:50:02):
As a growth leader, how do you operationalize that? Is it set some drag metrics? Is it just philosophically, let's make sure we're optimizing the right metric? What's worked to actually avoid that problem?

Lauryn Isford (00:50:15):
I think north star metrics help because a team can be singularly focused on the most important result for their roadmap and their charter. However, guardrail metrics are equally important. So, an onboarding team that builds amazing onboarding that causes a 10% drop in revenue would need some sort of guardrails to make sure that they knew that that might not be the right trade for the business, and importantly, should have the rigor and passion to go deep and understand what caused that drop in revenue and figure out what it was about that onboarding that ultimately caused a guardrail metric to suffer. So, with that in mind, I think guardrail metrics can be very useful and are important to choose wisely. I love working with strong analytics partners on a growth team because rigor and education around how to think about guardrail metrics is something that we should always be thinking about, whether you are a data analyst in functional specialty or a PM or an engineer or a designer.

(00:51:19):
So, that's how I kind of like to think about it. I do think guardrail metrics help and then just being well reasoned and thinking about what's best for the business and speaking about your work as being what's best for the business and the customer overall, rather than being too narrow in your own swim lanes of what you work on.

Lenny (00:51:35):
Great advice. I want to shift to a different topic and this will be much shorter. You have this really cool framework for thinking about the PLG funnel, product-led growth, and interestingly kind of trickles down to the team you build, metrics you choose, and things like that. So, can you just briefly talk about just this framework that you use to think about PLG growth in the PLG funnel?

Lauryn Isford (00:51:55):
When I think about how to grow with PLG in a business that has some element of PLG, self-server, freemium, I usually start with a funnel that roughly maps to the same scaffolding, regardless of business. Whether I've worked on the business, whether I'm supporting the business as an advisor, I love starting with this framework. The first step is join, the second is evaluate, the third is upgrade, and the fourth is expand. This funnel represents the journey of a customer in a PLG product as they advance and develop in their lifetime of using the product. It starts with becoming a part of the account that's using the product or signing up, and you might join because you found Airtable on Twitter or you might join because Lenny invited you to use Airtable. So, there are different ways that you can join that product in the first place.

(00:52:55):
Then importantly, you evaluate if it's right for you, and that word choice of evaluate is deliberately not onboard or activate because it's about what the user needs to see that they are going to get the value that they want in using your product and in building a habit around it. Next is upgrade. Ideally, someone has gone from beginner to intermediate or even advanced in their ongoing education and in getting to know your product over some amount of time and they see premium value and raise their hand and say, "I will convert to it." Now if you offer self-serve premium plans, that's awesome. They can do it with a credit card right in the product. Sometimes this means raising their hand to talk to sales and that's great too, but they upgrade to some sort of premium experience or to more value than what they have when they got started.

(00:53:43):
And finally expand, and vertical says this can be nuanced but with more horizontal tools. Ideally, a few folks, maybe one, maybe a few are using a tool in an organization and then many more adopt it over time, and that expansion drives net dollar retention, it drives brand awareness, it drives more usage in more pockets of the company, it is awesome for renewal rates if you're working with enterprise contracts, and ultimately then also brings new referrals into the product that loop all the way back to the beginning at join.

Lenny (00:54:19):
I love it. And what's cool is upgrade and expansion kind of bake in retention. You're not going to upgrade, you're not going to expand if you're not retained. Can you talk a little bit about how you use this framework? Do you bucket? Do you have these four teams on your growth team that focus on each of these stages? Is it more of a conceptual framework? Do you come up with KPIs for each of these steps? How do you actually operationalize this concept?

Lauryn Isford (00:54:40):
I think this framework is a step to abstract to represent exactly how you should structure your teams or to be represented with four metrics, for KPIs. However, it's a really good conceptual way of grounding your team or your organization in the mechanics of how machine that is the business you work on run. From there, it can become much easier to communicate with each other on where you see opportunity on specific pockets of the product that might be impactful. So, for example, you might be working on a strategy related to landing pages and be able to name that that's going to help drive joins in new organization, and that's a really awesome way to communicate why you might invest there versus investing in something related to onboarding that would help with evaluate.

(00:55:32):
So, I love this framework because it helps everyone communicate clearly and also you can derive from it more specifically what are the opportunities that are relevant to us with this framework in mind, and then revisit it over time to gut check if you feel like maybe what you're investing in now is a bit outdated and needs a refresh, or if there are other pockets of the business that need more attention that you might be able to work.

Lenny (00:55:58):
Can you talk a bit about how you structured the growth team potentially based on this framework and just generally how you thought about building the growth team at Airtable?

Lauryn Isford (00:56:06):
We had what I think is a pretty relevant set of teams. If you're thinking about building out a few in your own product or organization that focuses on sort of a PLG shape of business, we had one team working on acquisition and they were really responsible for the join. So, they mapped actually really well to this funnel. One team working on activation and they mapped pretty closely to evaluate. It wasn't a full representation of what's possible in evaluate. We were pretty focused on the self-serve business and that was different than, for example, helping an enterprise customer evaluate the right offering for them, but that activation team was most closely tied to that second step in the funnel.

(00:56:50):
And then we had a monetization team that worked on monetization and pricing and they mapped really closely to the upgrade part of the funnel. They did touch some other things as well. So, they worked on churn prevention and downgrades. They worked on some billing related projects, but in general, they were most thematically aligned with that upgrade step of the funnel. One area that is more emerging that's interesting is expand. So, when we got started on Airtable growth, we didn't have a team dedicated to that expand piece and it became increasingly interesting to us over time as we started to notice that larger companies were using the product. This meant that there was a bigger opportunity than there had been before to really help drive expansion and get more folks using the product in those accounts. That's an area that emerged later. That's a really good example of revisiting your priors and being resilient or agile in your org structure because it wasn't something we set out to work on initially, but it became a really clear opportunity later.

Lenny (00:57:53):
You mentioned that Airtable is thinking a little bit more about B2B growth versus just kind of B2C where I think it's been historically. Can you talk about that and just how you're thinking about that?

Lauryn Isford (00:58:04):
B2B growth is an emerging space for growth practitioners and hobbyists like me because the playbook hasn't been written the same way that B2C growth or consumer social growth has been. It's a new space, and there are quite a few companies that are really excited about exploring B2B growth and how to apply the DNA and the mechanics of a growth organization to more of that B2B motion or to working with more upmarket customers or enterprise customers. So, it's very top of mind for me. It's a active conversation in the growth community, especially in San Francisco. Overall, I'm really excited to see what we can do by applying this approach to growing businesses, to new types of businesses. It will require some differences in execution model. So, in B2C or in consumer social as two examples, you can experiment at large volumes or you can make changes that impact thousands or millions of people pretty easily.

(00:59:15):
In B2B growth, generally you're working with a much smaller set of customers and also the risk profile can be very different because smaller numbers of customers that represent larger percentages of your company's total revenue must be treated with absolute care, as opposed to a world where you might have millions of folks coming through your product every day and small changes might not have as big of an impact. In an enterprise organization, it's important to be very careful and rigorous and to prioritize that customer's needs all the time. This means that rigor, that customer conversations, that beta testing, that live prototypes and demos are significantly more important and that face time with the customer is significantly more important than it is in B2C growth. So, we'll see what happens. I'm really excited to see more folks who have given growth a try in B2C or in consumer spaces try applying it to B2B because it will become increasingly common in the industry.

Lenny (01:00:19):
Well, with that, we have reached our very exciting lightning round. I've got six questions for you. I'll go through it pretty fast. Are you ready?

Lauryn Isford (01:00:27):
I'm ready.

Lenny (01:00:28):
All right. First question, what are two or three books that you recommend most to other people?

Lauryn Isford (01:00:34):
Ride of a Lifetime by Bob Iger. I give this to new reports on my team. Great book to read when you're thinking about your leadership style, and Rocket Men, really fun story. I love a good story about ambition and achieving awesome things.

Lenny (01:00:50):
What's a favorite other podcast, other than the one you're currently on?

Lauryn Isford (01:00:54):
I like Fifth & Mission which is a local San Francisco podcast on local politics.

Lenny (01:01:01):
Favorite recent movie or TV show that you have watched that you've really enjoyed?

Lauryn Isford (01:01:05):
I really like the White Lotus Season 2. White Lotus was very fun to watch. I also, on the movie front, I'm in a habit of watching Best Picture nominees every year and last year there were a couple movies I really enjoyed, one of them was Belfast.

Lenny (01:01:22):
Oh man, that was an intense movie. I watched that recently. And also, if we should turn this into a drinking game, every time someone mentions White Lotus, we drink. It's an amazing show, but it's definitely comes up often. So interesting.

Lauryn Isford (01:01:35):
Comes up too much.

Lenny (01:01:37):
It deserves to come up often. I love it.

Lauryn Isford (01:01:39):
That's true.

Lenny (01:01:41):
It's great, but that'd be okay. We're going to do a drinking game from now on and I'll have a shot here. Love White Lotus. Favorite interview question that you like to ask people?

Lauryn Isford (01:01:50):
Tell me about a time that you delivered something that was impactful.

Lenny (01:01:58):
What do you look for in an answer when you ask that question? What's your kind of a good sign and what's maybe a bad sign?

Lauryn Isford (01:02:02):
I'm looking for someone to help me understand how they define impact and what it means to them. I think a good answer for growth practitioner is intrinsic motivation about having an impact on the business.

Lenny (01:02:19):
Hear, hear. What are five SaaS products that you use day to day, and you can't say Airtable?

Lauryn Isford (01:02:25):
Figma, Miro, Slack, Gmail, and my fifth one, I need to think about it.

Lenny (01:02:36):
It's because I cut out Airtable. I got you.

Lauryn Isford (01:02:39):
I know, I always say Airtable. Airtable's definitely number five.

Lenny (01:02:42):
Okay. Probably number one. Okay, final question. Speaking of Airtable, what's the coolest use of Airtable you've seen?

Lauryn Isford (01:02:48):
There was a great embedded view, which is the internal term for when you put Airtable on your website in an embedded way so people can check out cool stuff, related to finding COVID vaccine when they came out, which was really awesome. I also appreciated that a similar use of Airtable has become quite popular this year in support of facilitating folks who've been laid off to help them find new opportunities.

Lenny (01:03:15):
Lauryn, this was amazing. I learned a ton. We got through everything I was hoping to get through which I did not expect. Two final questions, where can folks find you online if they want to reach out and learn more and to reach out to you, and then two, how can listeners be useful to you?

Lauryn Isford (01:03:28):
You all can find me on Twitter. I'm @laurynisford. I love hearing about how folks with all different kinds of cool products are thinking about growth. In general, I find all of us are better at growing businesses when we study the awesome wins and learnings of others. So, please, my DMs are open. Send me cool things you're working on. I'd love to learn about it.

Lenny (01:03:51):
Amazing. Lauryn, thank you. Let's go drive some growth.

Lauryn Isford (01:03:54):
All right.

Lenny (01:03:57):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

