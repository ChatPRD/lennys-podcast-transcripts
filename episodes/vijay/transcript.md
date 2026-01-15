---
guest: Vijay
title: An inside look at Mixpanel’s product journey | Vijay Iyengar
youtube_url: https://www.youtube.com/watch?v=t-2oXtZrlEc
video_id: t-2oXtZrlEc
description: 'Vijay Iyengar is Head of Product at Mixpanel, and similar to myself,
  came from an engineering background before transitioning to product. In today’s
  episode, he explains how Mixpanel has...

  '
duration_seconds: 2811.0
duration: '46:51'
view_count: 8119
channel: Lenny's Podcast
keywords:
- growth
- retention
- onboarding
- churn
- metrics
- okrs
- roadmap
- prioritization
- analytics
- funnel
- pricing
- revenue
- hiring
- culture
- leadership
---

# An inside look at Mixpanel’s product journey | Vijay Iyengar

## Transcript

Vijay Iyengar (00:00):
The issue for us at the time was that we took people away from the investment in our core product to go do those other things. We moved people, right? And so the trap there is that you leave yourself right for disruption in your core because someone else can out invests you in that core. And so if you are the leader in some core product, our takeaway here is you should continue to out invests everyone else in that core and then invest the profits that come out of that core into the next venture. Invest profits and not people, or venture capital, which is maybe net present value of profits or something to that effect. But don't take people away from the core to go to these other things because then you end up distracted.
Lenny (00:40):
Welcome to Lenny's Podcast where I interview world class product leaders and growth experts to help you get better at the craft of building and growing products. Today my guest is Vijay Iyengar. Vijay is currently head of product at Mixpanel. He actually has a very similar career trajectory to myself where he started as an eng intern at Amazon. Then he was an engineer for a while at Uber, then he became an eng manager at Mixpanel. But then he shifted from an ENG manager to director of product, and now head of product at Mixpanel. You don't often see people moving from an leadership role straight to director of product, so it was really interesting to hear what he took from his eng experience and brought into his approach to product leadership. But we spent the bulk of our time talking about what he's learned from the journey that Mixpanel has been on, where they started with a simple product, then scaled to a number of different products, solving many problems for customers, and then made the hard decision to scale back to just a single core focused analytics product.
(01:33):
We talk about why they made that choice, what they learned about when it makes sense to expand a new product and when you probably shouldn't, and how they approach that organizationally. We also talk about how Mixpanel builds product, how they think about products philosophy, how they prioritize, and also what you're probably doing wrong in how you set up your analytics for your own product. With that, I bring you Vijay Iyengar after a short word from our wonderful sponsors.
(01:56):
This episode is brought to you by Pando, the always on employee performance platform. How much do you love the performance review process? Yeah, it's time consuming subjective bias, and there's rarely any transparency. With the rapid shift to distributed work, it's a struggle to create the structure and transparency that you want to help your employees have the highest impact and growth in their careers. Pando is disrupting the old paradigm of performance management, including a continuous employee-centric approach so employees stay engaged, see their progression in real time, and know exactly when and how they can level up. With Pando, managers can leverage competency-based frameworks to effectively coach and develop their teams and align on consistent growth standards, resulting in higher quality feedback and higher performing teams. Visit pando.com/lenny for more info and get a special discount when you sign up and reference this podcast. That's pando.com/lenny.
(02:54):
This episode is brought to you by Notion. If you haven't heard of Notion, where have you been? I use Notion to coordinate this very podcast, including my content calendar, my sponsors, and prepping guests for launch of each episode. Notion is an all-in-one team collaboration tool that combines note-taking, document sharing, wikis, project management, and much more into one space that's simple, powerful and beautifully designed. And not only does it allow you to be more efficient in your work life, but you can easily transition to using it in your personal life, which is another feature that truly sets Notion apart. The other day, I started a home project and immediately opened up notion to help me organize it all. Learn more and get started for free at notion.com/lennyspod. Take the first step towards an organized happy team today, again at notion.com/lennyspod. Vijay, welcome to the podcast.
Vijay Iyengar (03:52):
Thank you, Lenny. Great to be here. Huge fan of the pod, and so glad I can contribute.
Lenny (03:57):
I definitely want to talk about Mixpanel's journey both as a product team and a product. But before we get there, as an engineer, you were in a longtime engineer and then you became a product leader, is there anything you had to unlearn as an engineer in the way you thought about leadership and product and business?
Vijay Iyengar (04:13):
One of the things after you've been in engineering for a while is that develop this tendency to immediately respond with no to new ideas. And I think from the engineering perspective, this is because you spend a lot of your time building and maintaining ideas that maybe are half thought out or didn't really go anywhere, and you just feel like the full brunt of the maintenance cost of that. And so you build up the scar tissue and this immune response to say no to new ideas, and it's a hard no, like no, we're definitely not going to do it. And I think I had to unlearn that moving into product because you get a lot of ideas coming from a lot more places in the organization, and ideas are fragile in their agency and it's a hard no can really kill a whole direction that you could potentially go.
(04:55):
They could be very high reach and high impact. So, one thing that I've found is the best way to get to a no, if you ultimately need to get there, is to try to make it work. Start trying to make yes work and document how you've tried to make yes work. And do that earnestly, not as an exercise of just an alternative that you're considering. Try to do it sincerely and get to know after trying to make yes work. And so that's one thing I've been trying to just apply my engineer problem solving brain to do that instead of thinking about how it might not work and saying no.
Lenny (05:25):
Is that something that you recommend engineers work on looking back? I know as a PM, it's like, oh, I love when engineers say yes. This is awesome. I'm going to actually help everyone learn to say yes. But as an engineer, obviously that's a challenge often. What do you recommend to folks that are engineers currently that maybe want to improve on this or shift in how they think about saying yes, saying no when they're asked about something new?
Vijay Iyengar (05:48):
I think some of the best engineers that I've worked with actually already do this, but [inaudible 00:05:53] they're able to balance both in their head. So, ultimately this balancing act, you just want on-call, you were woken up three times at 3:00 AM due to various bad ideas, and the next morning you wake up and then stand up, it's like, "Hey, can we do this new thing?" You kind of have to have that empathy and do that. So yeah, I think the exercise is just take 10 minutes to consider the idea and just sincerely consider how might we make it work. And if at the end of those 10 minutes, it's like futile and there's no path, it's fine to say no. And it's a good instinct to say no, actually in a lot of cases. But yeah, I would recommend that to engineers. I think it would've been better in my career, for sure, if I had learned that sooner.
Lenny (06:26):
I want to spend some time on the Mixpanel product journey. It's been an interesting rollercoaster. I think the company's been around for how many years? Since 2010? 2009?
Vijay Iyengar (06:34):
20009, yeah.
Lenny (06:35):
So, I know it started as kind of a very simple product analytics product back in the day. And then as you do with ambitious companies, you look for more problems to solve. You look for more problems to solve from your customers. So as I understand it, you guys added a lot more products to the suite of Mixpanel products. And then I know that there are some challenges with scaling that, and maybe the products didn't stick as much as you're hoping. And what I understand is recently, you moved back to just the single core analytics product. And so I'd love to just hear that journey of what that process was like, what you learned as a product leader and as a company about scaling, expanding, trying to solve a lot of problems, and then coming back to one core straightforward problem.
Vijay Iyengar (07:15):
Mixpanel started in 2009 as provide product analytics to EPD teams. And I think early on, it saw a lot of success because it built this in-house database called Arb, which stands for arbitrary segmentation. And that was necessary because events data, which is the fuel for product analytics, is few orders of magnitude larger than most other types of data that people collect, and so you need a specialized approach to deal with it. And so that I think spurred the first wave of explosive growth, because product analytics was a really burning problem at the time. People were shipping mobile apps like crazy and they needed a solution that could scale, and that was kind of a durable mode for Mixpanel for a while. And I think because we had this SDK that was installed in so many apps and we had this really scalable event collection and analytic interface, it was just natural to expand into a few adjacencies that would leverage those same technologies.
(08:04):
So, the first one was messaging, being able to send targeted messages to users, which is something that's fairly natural, you might want to do, especially if you have an SDK already installed. Yeah. The other aspect that we've added into was data infrastructure and trying to be the single source of truth of data in companies. And what ended up happening was that by 2018, we had this big churn problem. We had something like 40% churn, revenue churn, our core product. And when we dug into, it wasn't that people were churning because they didn't need product analytics anymore. They had the need. They were just churning to competition because we were just not up to the market in terms of the features we had in our core. And when we dug into why that was, it was just that we had a 50% engineering team that was building products across three domains, product analytics, messaging, and data engineering stuff.
(08:52):
Our engineering team was just spread too thin to address all of those core gaps in functionality. And so we made a really hard call at the time. We said the hard no to those two other categories and decided to focus our entire engineering team on closing the gap on product analytics and innovating there. And from a process standpoint, how we operationalize this was we threw away all our planning and all the execution and that we work that we'd planned to do so far, and we did something very simple. We took all the churn reasons that our customer success and sales teams had been painstakingly collecting for years, grouped them by category, which was roughly product features we needed to build, sorted descending by ARR, took the top 10 things and made that our roadmap, just give every engineer direct access to customers and give them a bucket to go work on, which I think goes against about a million product best practices out there of just doing that.
(09:41):
But I think given the context at the time, we needed to optimize for speed, and speed comes when you have extreme clarity on what you want to do and focus. And so we really just optimize for speed in that time. And so in that first year we moved really quickly and we shipped something like a hundred features in that year and closed a lot of gaps. Again, these are all vanity metrics. Measuring number of features doesn't mean anything.
Lenny (10:04):
And what year was this by the way?
Vijay Iyengar (10:06):
This is 2018 to 2019.
Lenny (10:09):
Got it.
Vijay Iyengar (10:09):
Yeah. So, we moved really fast shipping all these features and instantly saw the improvements to win rate and to retention. But one of the cracks that started to emerge was we neglected the holistic design of our product at the time, right? And if you're shipping features that quick leads, you don't have time to stop and think, where does this go, and how does this fit into our overall system architecture? And what started to happen was that we were hitting diminishing returns with some of these features. And not considering the holistic design and consistency meant the reach of every feature was low. You had to rebuild it for every part of the product that we were in. And so at the time we made... We spun up the second stream that was very design led. And I think this was also coincided around the time we adopted Figma, and it's a really broad design at seat at the table of the company, and we just set up this goal to make design one of our key differentiators.
(10:53):
So, this design driven initiative was really about how can we think about the system architecture of our product? What are the key building blocks of Mixpanel? Where do they need to fit? How few of them can we have, which is a really important step? And then how will users discover them and how do they relate to each other? But I think this realization was born out of the fact that so many great products win or lose based on their architecture. I think Notion, for example, that pages in blocks architecture is so strong, and you can hang so many features off of those core building blocks in a way that has such high impact on region and discovery of those features.
(11:26):
So anyway, we did that in parallel with the.... And continued that grind on core jabs. And so the end result of that phase, which is from 2018 to maybe late 2021, 2022, was our retention went from about 60% to 90%, and our NPS went from 16 to 50. So I think, yeah, there's a lot in there to unpack, but refocusing on the core really helped us achieve those results.
Lenny (11:52):
Got it. Yeah. I have a lot of questions about this. So interesting. So, that phase that you went through where you sorted things by potential ARR, was that the phase of expanding to multiple products or that was post we're going to focus on analytics and go all in there?
Vijay Iyengar (12:06):
Oh, that was post focusing on analytics.
Lenny (12:08):
Okay.
Vijay Iyengar (12:08):
Yeah. Yeah.
Lenny (12:09):
And you're saying that you had a stream of just builds all the features that were lacking that are causing customers to churn, and in parallel, there was a track of let's build this product, such that it all connects and works together well and it's really well thought through long term?
Vijay Iyengar (12:24):
The first thing, I might have made it seem like it was just the buckets were features. We did take the step of turning them into problems and being clear, exposing engineers directly to the customers that had those problems and then invent a solution to solve them. So I mean, loosely there were features involved, but a lot of them were kind of core problems we needed to solve.
Lenny (12:40):
That first approach is so interesting. It's kind of like, yes, we will make more money if we focus on these features. To your point, it ends up being just a bunch of features and products that kind of maybe don't synergize. Looking back, was that a good idea to approach it that way, at least for a while?
Vijay Iyengar (12:54):
It highly depends on your context. In a very competitive context where there are just table stakes features that customers need and that it's been validated by the market, you need to optimize for speed more so than anything else. But it is an approach that outlives it's usefulness pretty fast, and we've put that approach behind us relatively quickly after that phase. And I would actually say that design driven phase was the next phase, where it was, okay, we're not bleeding on the table stakes anymore, but we want to make a holistic product that has high reach, high impact on the features and is actually usable. And so that was I think a follow-on phase that's necessary. Obviously, depending on your particular circumstances and competitive dynamics, you can sequence them differently, but I think it was the right call to just... Sort of the on-call thing again where when you're in trouble, you got to get out of trouble. You can't mow your lawn while your house is on fire. You kind of put out the fire and then deal with everything else.
Lenny (13:47):
Yeah.
Vijay Iyengar (13:47):
So, that's kind of the approach we took.
Lenny (13:49):
What's an example of a feature or product that you launched within that first track? And then what's an example of something that came out of the designer led approach, if anything comes to mind?
Vijay Iyengar (14:00):
I think out of the first track, oh man, there's so many that were just core. We didn't have a good cohorts product at the time, just being able to create behavioral cohorts users and create them from any report that we built, right? And I think that, I mean it's just table stakes and analytics to be able to do that. So, that was one of the first things we built, and it was fairly obvious. There's a lot of other things in more advanced types of funnel analytics and a flows and visualization that was really interactive. I think on the design-led phase, the biggest thing I think was visualization consistency and making our charts interactive in a consistent way across our entire product. And so there's two things that enabled. One was that every time we added a new visualization or a new enhancement to a visualization or how something is sorted in one report, it just instantly applied everywhere.
(14:46):
So, just the reach was multiplied for everything we added. And the other thing is it just made the product more accessible, let us add dark mode. So, it made our visualizations really stunning and really easy to see what the takeaways were. And then every new visualization we added inherited all those benefits.
Lenny (14:59):
I'm trying to think about being at a company that goes through this phase of, "Hey, we're just going to build a bunch of stuff that we know we need." And it feels like hearing it, it's like, "Oh yeah, and then we're just going to make it all look great and connect and work well." I imagine that wasn't planned, and I imagine that wasn't easy to get people to maybe slow down on just building more products and features or push it in a direction where it's all going to make sense. Can you talk at all about what that process was, how hard it was to shift from we're just going to knock through all this checklist of things to let's just bigger, let's slow down, let's spend a lot of time designing?
Vijay Iyengar (15:35):
It was definitely more messy internally than I described it. One of the key junctures was when we had this really talented design team and we were putting them on these very tactical projects that was, frankly, that was very engineering led, right? And design would often come in at the end and be asked like, "Hey, can you just make this look nice and put some pixels on it?" And it's just such a waste of your design team to have them do that. But at the same time, the pace was so high that they didn't have time to come up for air and do anything else. And so there's actually this moment where I was an engineering manager at part of this.
(16:05):
And had a meeting with our BM and our head of design at the time, and we said, "Hey, we can actually do the next three months of projects about any design," which was a kind of controversial thing to say, "but we're doing this so that you can take three months with a set of designers and go think about the system architecture of the product, and we'll wait for that to be done before we do any architectural things that might impact the architecture." And I think that gave designers a bit of breathing room to go do that, just separating them for a bit from the tactical fire. Because what was happening instead was we would get towards the end of the project, bring design in, and they would use each project as an opportunity to squeeze in like, oh, and we can simplify here. And that's just a classic way to blow up scope at the end of the project because there wasn't a dedicated space for design led projects.
(16:48):
And I think that that was kind of a key friction point that we ultimately had to decouple for a bit, and then regroup and say, "Okay, now we'll look what's our strategy," and just take on projects purely for the sake of improving consistency, reach depth of our UX.
Lenny (17:02):
Also, looking back, the process you went through adding a bunch of products to solve more customer problems, something every founder and product team thinks about, when should we add new product lines? When should we expand beyond the core? I'm curious what you take away as a lesson and what you'd advise other founders and companies when it comes to when is the time to expand and think about a new product and a third product and a fourth product?
Vijay Iyengar (17:28):
I don't know if there's a hard and fast rule here. I can just maybe say what made sense and didn't make sense in our context. The issue for us at the time was that we took people away from the investment in our core product to go do those other things. We moved people, right? And so the trap there is that you leave yourself ripe for disruption in your core because someone else can out invest you in that core. And so if you, you're the leader in some core product, our takeaway here is you should continue to out invest everyone else in that core, and then invest the profits that come out of that core into the next venture. Invest profits and not people, or venture capital, which is maybe net present value of profits or something to that effect. But don't take people away from the core to go to these other things because then you end up distracted.
(18:10):
And the other aspect of that is that those secondary products we took on were in categories of their own. And it's really tempting and you'll often get dragged into accidentally entering another category, and then you'll end up building these bolt-on products that are the best in their category, right? And the adjacent categories for analytics are CDPs or message targeting or feature flagging or something, but there's not that many people that need the sixth best CDP or the eighth best feature flagging or the 10th best message targeting tool. And it ends up being, in aggregate will contribute five to 10% to your revenue, won't seriously accelerate your growth rate, and then takes engineers away from the core product. And so those were the circumstances that we were.
(18:50):
And I think if you're seeing churn to your competitor on your core product and you're not best in class on any of the other ones, then maybe it's time to reevaluate. And then the last thing I'll say there is that it's also 10x more painful than you think to cut mild successes than anything else, and just organizationally painful. And there's teams that have whole roadmaps, and it's a really painful experience, so you have to think really hard before you kick those off.
Lenny (19:18):
That is really, really insightful advice, makes me think about if you bundle good enough solutions, there needs to be kind of this anchored tenant that I will not give this thing up and I'll use the third best version of something else, if you have it. But if you're not that valuable and important, you're not going to convince people to use something because they're competing against the best in every category.
Vijay Iyengar (19:39):
Exactly. Yeah.
Lenny (19:40):
That is really interesting. I've been doing this kind of series on how different companies approach building product and I have a few questions I'd love to ask around the product development process and Mixpanel.
Vijay Iyengar (19:50):
Sure.
Lenny (19:51):
The first is just like, how do you plan? How do you plan? I know it evolves, but just how do you plan currently? How long are your planning cycles? How far ahead do you plan in detail? Do you use OKRs? Maybe let's start there, those three kind of sub-questions.
Vijay Iyengar (20:04):
We have these unsolved problems and analytics that we're going after. For us that’s like, people always want more power, more simplicity, better data trust, faster onboarding, better collaboration, better price performance. And so we largely organize our teams around those problems and those missions. One quick aside there is that some of those problems have attention with each other. Power and simplicity, there's a trade off there, right? And we want one team to own both, so that they're kind of forced to confront that tension and beat that trade off. And so that's kind of how we think about generally our product team, is these cross-functional EPD teams, each of which that's focused on solving these long-lived paired problems for customers [inaudible 00:20:41] our core analysis team focused on that power, simplicity, trade off problem. In terms of planning, the way it works is that we plan on a six month time horizon. And I can talk about our most recent planning cycle actually, because we're just completing it.
Lenny (20:53):
Yeah, let's do it.
Vijay Iyengar (20:54):
Yeah, basically it started out with this strategy memo that our leadership team wrote that basically just conveys this is where we want to go as a company in the next year, and here's how the product team can contribute most of that and just established these key pillars. We shared that with the teams, and they took that and also combined that with all the quantitative and qualitative context they're constantly consuming about the problem they're working on and our customers, and ideated and developed the series of bets for the next six months, which I think are some extent similar to OKRs, where ABET... The anatomy of ABET is that it's problem we want to solve, our hypothesis on the solution, and then some plan to win, some plan to actually get there and a way to measure that you got there.
(21:32):
And I think one of the unique things that we did relative to other companies that do planning is... I think it usually is sort of this W process of there's the strategy memo, and then teams generate bets and there's a review, and then they go back and I iterate and then they finalize. And we kind of collapsed the middle part of the W where myself and our head of design actually spend time with each of the teams actually ideating on the bets and participating in the solution discovery process, going into the jam sessions and adding fig must keys ourselves with ideas and thoughts on things, which we did because we aren't a huge product team, and we are not going to do 50 things and a half. We're going to do maybe 10 to 12 things.
(22:12):
And so that's enough that we don't... We can do something that doesn't scale if that enables high bandwidth communication between us and the teams. And it ends up being more messy and unstructured ABET in that phase because we're in there contributing ideas as well. But by the end of it, I think the team leaves feeling both more competent in their bets because there's more thought that's gone into it, and then more aligned top to bottom line why we made certain decisions. And so I think that that's one thing that's different. And then we conclude that process with the roadshow where we presented the rest of the company, and then get their feedback as well.
Lenny (22:41):
How long is this process generally?
Vijay Iyengar (22:43):
The teams did pre-work for a couple of weeks, like two weeks in December, and then we did a two week sort of sprint on solutioning and ideation in January, the first two weeks of January.
Lenny (22:53):
Awesome. And what's the end result of planning for each team? Did they deliver a document with, here's our strategy, here's the big bets, here's a roadmap? Is there a template you pass around? How do you get to a thing that people share and present and comment on?
Vijay Iyengar (23:10):
Yeah, I think there's basically three artifacts that are kind of linked to each other. So, the first is we use Notion, and so we have a database in notion called bets, which is where each page in the database is [inaudible 00:23:22]. And that has a template, yeah. So, it's kind of roughly what I described with a few more sections of what problem we're solving? What's the evidence of demand? What's the region impact of this problem? How do we know we're successful? And then what's the key driving hypothesis behind the solution? And then a rough line. And then that's tied with a presentation that's kind of like a tight summary of that that has one slide per bet, and then is also tied with more of an execution focused, how do we sequence and staff this thing and eliminate dependencies, which the engineering team contributes to. So, I think those are the three artifacts that are linked together.
Lenny (23:54):
This episode is brought to you by lemon.io. You achieved product market fit, you're able to activate, engage and retain your customers, but you don't have the engineers that you need to move as fast as you want to because it's hard to find great engineers quickly, especially if you're trying to protect your burden rate. Meet lemon.io. Lemon.io will quickly match you with skilled senior developers where all vetted results oriented and ready to help you grow, and all that At competitive rates. Startups choose lemon.io because they offer only handpicked developers with three or more years of experience in strong proven portfolios. Only 1% of candidates to apply get in, so you can be sure that they offer you only high quality talent. And if something ever goes wrong, lemon.io offers you a swift replacement so that you're kind of hiring with a warranty. To learn more, just go to lemon.io/lenny and find your perfect developer or tech team in 48 hours or less.
(24:51):
And if you start the process now, you can claim a special discount exclusively for Lenny's Podcast listeners, 15% off your first four weeks of working with your new software developer. Grow faster With an extra pair of hands, visit lemon.io/lenny.
(25:08):
I know you have some insights on prioritization and some strong opinions on how to prioritize. Can you talk a bit about that and how you advise your product teams to prioritize?
Vijay Iyengar (25:17):
One really common framework in prioritization is RICE, reach, impact, confidence, effort. And I think it's simple and fairly robust, which is generally good qualities of a framework. But one of the traps with RICE that we observed is that the C and E, the confidence and effort tends to cause you to prematurely deprioritize potentially high reach, high impact bets, really innovative things. And we encountered this on one of our teams early last year were we just RICE'd everything, all the ideas, and a lot of the high reach, high impact things ended up at the bottom because confidence and effort were just so murky for them, as they should be typically for high reach, high impact ideas.
(25:55):
And so one exercise that we push our teams on is just ignore the C and E for a little longer than it's comfortable, and just sit with those high reach, high impact ideas with engineers and designers in the room committed to actually trying to solve them. Give it a fair shot. And you'll often find if you spend a week on that set of ideas, you can get pretty far in understanding the confidence and the effort. You can probably find a higher confident lower effort way to do them. Then add the C and E back in, and then RICE as usual. And the goal is to end up with a reasonable mix of innovative bets, incremental bets, and then ones that are technical debt or product debt that you need to address.
Lenny (26:31):
I usually just cut out the C myself. I find that it's not that powerful. Do you do this in a Google Sheet? Do you use this in Notion? How do you actually recommend teams do this prioritization, or just eyeball it?
Vijay Iyengar (26:43):
I'm not super opinionated on the exact tools that teams use. I think this is a team local exercise typically, but most teams use Notion and just simple tables or databases in Notion-
Lenny (26:51):
Sweet.
Vijay Iyengar (26:52):
... work fine for this. I think the other thing on prioritization that's always tricky is estimation. And every engineer will value you estimates are all lies, and if you say it'll take eight weeks, it'll take eight months. But I think the core problem with estimation is you're asked to estimate things before what the thing is, and it's just a strange output to be expected to produce. And one approach that I found really interesting is from this book called Shape Up by Basecamp, which this idea of appetite overestimates, where instead of making the estimate an output of planning, you make the time box or an appetite the input, and you say, "We want to solve X problem and we're willing to invest six weeks solving that problem."
(27:31):
The obvious question there is how do you pick that time window? It just seems arbitrary. And so the base camp people suggest just pick six weeks for everything, and they're really austere about if you can't scope hammer something down to six weeks, you're doing it wrong, which I think is... It can work and has a lot of benefits if you creates a rhythm in your company, but one approach I found that works better is pick a reasonable sounding appetite and just explore the two to three options around it. Pick six weeks, and then say, "What would we do differently if we only had four weeks or eight weeks?" And you'll kind of naturally find the efficient frontier of cost and impact, and then align on that. And the important thing is that you check in after that time period and say, "Is there any new information that's just we should continue? Did we uncover the biggest risks, and are we just on the long tail of things?" And actually be honest with yourself about that. I think that's important regardless of what framework you use.
Lenny (28:23):
I really like that. So, is that how you actually operate, you create a time box, we have four weeks for this project, whatever we get done, we ship whatever we don't, we push out?
Vijay Iyengar (28:30):
We operated that way in engineering, particularly on the infrastructure side, because we have this series of projects that would just take forever, and the longer it takes, the longer it's going to take. And so we've done that exercise quite a bit. I'd say more on the more engineering heavy projects than others, but we're starting to adopt it more in the product side as well. The main exercise we've taken on the product side is more the consider, what would you do differently with different time boxes approach?
Lenny (28:56):
Just a thought exercise.
Vijay Iyengar (28:58):
Yeah, it's a good thought exercise. Then it just forces everyone to truly score the requirements. Critical, nice to have, is nice, but really if in two weeks, you're going to get pulled off to do something completely different, what would be a complete solution that addresses the core problem. And it forces you to peel the meat of the problem in first, as opposed to just doing the things that are surrounding it.
Lenny (29:17):
That's cool. I really like that. I've done that myself. I'm curious if anyone ever does the shape up process for real or it's just like we will ship anything that is ready within six weeks and not actually have specific deadlines or kind of concrete goals of products they need to ship in specific ways.
Vijay Iyengar (29:32):
Yeah. Well, I think the shape up process, if you run it all the way. They do... Their idea is that you can actually predict on a six week time horizon. So, you can just hammer down scope to something that is complete. It needs to be complete. It can't be milestone one that's like a half baked thing in six weeks, which I think that rigor... The rigor they applied to that across the board, you need to do it all the way. You can't adopt the process halfway. I think the is the challenge. Otherwise you end up with people shipping milestone one and then moving on, which is not the complete product.
Lenny (30:01):
Makes sense. A couple more questions around how you build product. You mentioned that you have a unique approach to keeping product teams close to customers. And I'm curious what you've learned there, what you found to be helpful and just kind of keeping product teams close to your customers.
Vijay Iyengar (30:15):
I think this is one thing that is something we invested in pretty early on at Mixpanel. Actually around that time, in 2018, when we refocused on our core product, one of our sales engineers, Aaron, built this automation where he piped all these customer gaps that we got that were reported by our customer success and sales teams, piped that into Slack and just a feed. And what this created was this culture where all engineers and designers could consume that raw feed of direct points of customer with no gatekeeper, no process to access it, no pre-aggregation, right? And I think this scale's pretty far. At a product team of our scale and with our reach of customers, we don't get so much feedback that someone couldn't read it in 20 minutes every day. And for four or five years in engineering, every day I would read all the gaps that we got, and many engineers would do that.
(31:04):
And one of the rituals that it's enabled is we'll find that engineers will go into that channel and react with a message with an email emoji, which means I'm going to email this customer and find out more, right? And they'll just email the customer and say, "Hey, I'm the engineer that built this feature. I saw you said this specific thing. Can you tell me more? I'd love to understand." They ask the five why's, and then they improve the product on their own. And I think that culture is just so important, and it just empowers all engineers and designers to think a PM a little bit, which I think takes a little bit of a load off on the PM to be the gatekeeper of all that information.
(31:39):
And then over time, we've evolved it quite a bit as our data stack stack's involved. So, we now not just take customer requests, but we take things that are posted on Twitter and NPS survey feedback and win loss notes from our competitive deals and pipe them both into Slack and into Notion so that we can both get the realtime feed, and then we can sort and aggregate and tag things accordingly. But the key artifact of this is that it's all open. There's no gatekeeper behind that process.
Lenny (32:04):
That sounds both amazing and wild. Do you still allow engineers just to email customers and ask them questions about this stuff, or is that harder to do it as you've grown?
Vijay Iyengar (32:12):
Oh no, we still allow that. Yeah.
Lenny (32:14):
Wow, that's awesome.
Vijay Iyengar (32:15):
One nice thing about the stack actually, the data stack, is that... So, basically all these feeds information land in our data warehouse, which is BigQuery. And from there, they're pushed out via a reverse CTL tool we use called Census to Slack and Notion that make the note code. But one of the benefits of that is that we can enrich all of these feeds with who's the account? What's their ARR? Who's the CSM? And all that other contact information. So, it's usually not an engineer's blindly reaching out to a customer without letting a CSM know if it's a million dollar account or something. The idea is just trust them with that context, and they can tag the right people and make the right call on that.
Lenny (32:50):
I'm so curious how that gets prioritized and how PMs are looped into all that, but we don't have to get too deep in that. That's a really cool process. I haven't seen that before. Our engineers were just emailing customers, digging into questions and problems.
Vijay Iyengar (33:01):
The trap of course is what you just called out is you can't be reacting to everything all the time. And certainly if you ship a redesign, the first two weeks of that, there's going to be a bunch of feedback that's like, I hate this. Go back. And I think that's sort of an organizational muscle you have to build, balance the reaction, and that's just a thing we've had to practice doing, but I think the trade offs are worth it.
Lenny (33:20):
Awesome. One last question along these lines, can you just talk about the tools you use, the SaaS products you use to run your product team for collaboration, communication, notes, docs. You mentioned Notion as an example.
Vijay Iyengar (33:31):
I think our stack is actually fairly standard these days. So, we have Slack, Zoom for communication, Notion for docs and any long form writing, and it's a [inaudible 00:33:42] database, and Figma and FigJam for design and whiteboarding. I think what's actually more interesting is our data stack and the productivity we get out of that. I briefly touched on this, where basically all of our data gets EPL'd out of all the systems we have, lands in BigQuery, gets joined and modeled, and then pushed out via census to all the other tools in our stack. And I think that's been a huge productivity unlock because you can build internal tools with very little code. If you can write SQL, you can build an internal tool basically, and that pushes information to the teams that need it. And so that, I think, just has unlocked a lot of these types of things like automating qualitative signals with no code in a reliable way.
(34:22):
And then if someone like, "Oh, can I get ARR on this?" Yeah, sure it takes two seconds to do that. So, I think that data stack has been a huge productivity unlock for us.
Lenny (34:29):
Awesome. Have you guys shared that anywhere online, just to show kind of the stack you guys have built?
Vijay Iyengar (34:33):
We have a couple blog posts that talks about our stack for... We use this both for our PLG infrastructure and our product, let sales, defining a PQL and alerting a new user who fits that criteria, but then we also use it for internal tools. We have a few blog posts on that topic.
Lenny (34:48):
Sweet. We'll follow up and include some of that in the show notes.
Vijay Iyengar (34:51):
Yeah, definitely.
Lenny (34:53):
Final line of questioning, you're one of the smartest people in the world on product analytics heading product for Mixpanel. I'm curious what you think most people get wrong when they're setting up product analytics for their site, their product, their company.
Vijay Iyengar (35:08):
It's maybe a bit of a hot take because I think so many people-
Lenny (35:11):
There we go.
Vijay Iyengar (35:12):
Yeah, so many people still do this, but I think the biggest mistake is setting up analytics using client side SDKs, client side tracking. So, web and mobile SDKs, putting a mixpanel.track or segment.track in your web app or your mobile apps. And reason it's a hot take is that for many people that's product analytics and SDK tracking are synonymous. They're like, "All right, Mixpanel means SDK, I have to put an SDK in my web and mobile app. But that's a mistake because it... We've just seen time and time again, it leads to poor data quality and difficulty to maintain that data. So, the problem on web is, just due to app blockers and other unreliable things, in the JavaScript world, you end up dropping 20 to 30% of your events, and so it just doesn't match your internal databases.
(35:55):
And then on mobile there's two problems. The first is that you have to reinvent tracking for both iOS and Android because it's two different languages and two different platforms, generally speaking. And so you end up with many duplicate events that semantically mean the same thing, but are just different because of the two platforms, and you might have two teams owning that. And the second issue, which is I think even worse, is that you are kind of beholden to clients updating their mobile app to get to the latest version that has your latest tracking. So if you want to add new tracking, it'll only apply to people at the latest version and beyond. Whereas yet all of your old tracking, whether it's broken or you made a mistake, is still out there in the wild, and so you're constantly getting events that are old and broken.
(36:32):
And so what we recommend instead, and that we've seen a lot more customers adopt recently is just track events from your servers instead of your clients. And that has three benefits. One, it's instantly cross platform. Web and mobile and TV and whatever other platform, they're all going to go through your servers, so you instantly get a hundred percent reach. The second is it's in an environment you control. So if you want to update tracking, you can update it and updates for a hundred percent of users. And then the third thing is that... And this is I think maybe unintuitive, but it's true, is that engineers have been tracking events from servers forever. It's called logs, right? And events are just logs where they user ID in them. And so they don't need to deal with learning a new SDK and dealing with all of that. They just have to track logs that have some structure and a user ID in them. They're tracking events.
(37:18):
And so if it's easier for the developer, it'll get done in a higher quality way. So, I think the really simple advice there is just start tracking events from your servers instead of from your clients. And if you need to supplement it later on with context that's only on the client, you can add that on later, but server side should be the default.
Lenny (37:34):
Maybe a last question is just what's changed most and how companies work with analytics in the past few years? And then just where do you think things are going in the space of analytics?
Vijay Iyengar (37:43):
Yeah, so I think one huge trend is the rise of the data warehouse. So these are Snowflake, BigQuery, Redshift, and they're really scalable and they speak this SQL standard, which has led to this explosion of tools that have emerged around them and make it really easy and cheap to load data into the data warehouse, and then also easy to push data out of the data warehouse by tools that can just do that. And this has a few implications. So, the first is that the data warehouse becomes the center of gravity for all data in your company. Whether it's product marketing and sales data, they all land there. And I think that's really valuable today in this product led growth world, and a lot of incus filled my bad. But from a data standpoint, that means all these teams need to be operating off of the same version of the truth, and that version of the truth is sitting in the warehouse, and it just needs to be joined correctly.
(38:33):
The second thing in terms of where things are going is the events, a time series of users at this action at this time, are the universal data model for analytics. And the reason for that is every action, every interaction a customer has, whether it's with your sales team, like a gong call, or with your marketing team, they clicked on that or viewed marketing article or their product, which is more well known, those are all events. They can all be modeled as events. And it's super granular, super intuitive as a way to understand what people are doing. And it's really powerful, because oftentimes you want to ask questions about sequences of events, right? Which user has spent this much time on my pricing page and then looked at three developer docs? That's probably a user I want to reach out to. So many things can be modeled off of that.
(39:17):
And so I think data warehouse is becoming the loading dock for all this data, which can be very easily modeled this events, but it's not a very great analytical tool for events because SQL is optimized for rows and tables and joints, and not events and sequences of events and segmentations of events. And so one of the things that we're spending a lot of time thinking about is how do we get that really rich, trusted, comprehensive dataset from the data warehouse into a tool that's optimized from the UI down to the data model for events, because that unlocks really fast intuitive exploration of data on dataset that people already have in trust? So, that's, I think, one of the big trends we're excited about and what we see as the future.
Lenny (39:56):
Interesting. And you think Mixpanel is in a good place to help people do that? Is that how see this, there's something that companies like yours will help people solve, or is this something everyone's going to have to figure out for themselves, or there's like a whole new class of startups launching to help them make the mess out of data warehouses?
Vijay Iyengar (40:11):
No, there's always a new class of startups joining in the analytics space. It's never dull moment. Yeah, I think this is something that we are looking to solve, because I mean, analytics only as good as the data. And if people are already collecting great data in the warehouse, I mean we integrate with the warehouse really well, then we get access to that good data. Increasingly, what we've been seeing is that companies like in the reverse ETL phase, like Census and Hightouch are effectively reinventing the CDP reinventing, data movement tool like segment on top of the data warehouse. And so really our strategy there is just tightening our integration with those tools. And we've seen just huge growth and people using their data warehouse as the source for events, not adding SDK tracking anywhere, and just saying, "I already have events sitting here. I trust all of them. They're from all parts of my business. Why can't I do analytics on my support tickets and my gong calls just as easily as I can do it about my user behavior." And so I think that's something we're seeing and we're investing in.
Lenny (41:04):
Awesome. Anything else you'd like to share before we get to our very exciting lightning round?
Vijay Iyengar (41:09):
Yeah, we opened talking about the transition from engineering to product, and I think one of the things that's just been really fruitful in my career, both on the engineering side and product side, is just adopting that product mindset and getting closer to customers, consuming the raw feed of customer context, taking every opportunity to talk to them. And I'm really excited to see things like this podcast and your newsletter and other forums for engineers to also develop that product mindset then and get closer to customers, because I think long term, that just means better products and services at lower and lower prices, which is just innovation. So, I'm really excited to see more of that in the world.
Lenny (41:45):
Here, here. With that, we've reached our very, very exciting lightning round. I've got six quick questions for you. I'm just going to go through them pretty fast. Whatever comes to mind, just share, and we'll see how it all goes. Sound good?
Vijay Iyengar (41:57):
Sure. Let's do it.
Lenny (41:58):
Okay. What are couple books that you recommend most to other people?
Vijay Iyengar (42:02):
On the business book standpoint, there's this book called The Goal by Eliyahu Goldratt. And it's kind of an old book, but I like it because it's sort of written in this fast-paced thriller model. It's like a fiction book, but it's about this idea of the theory of constraints, finding constraints in a system and how you can remove them to improve productivity. So, I found it's just a fun read, and also really insightful non-technical books that I recommend to folks, particularly those that live in SF, which is Cool Gray City of Love by Gary Kamiya, who is a longtime SF president. And it just goes into the history and the communities, and even the geography of San Francisco, and I've just discovered so many little pockets in the city from reading that book, so it's something I recommend to people who live in San Francisco.
Lenny (42:46):
What's a favorite other podcast that you enjoy other than this podcast?
Vijay Iyengar (42:50):
I'll do non-tech one for this. So, I'm a huge fan of the show The West Wing, and so there's this podcast called The West Wing Weekly that goes into each episode of the West Wing and brings in actors from the show, as well as folks from government to talk about each episode, and it's just a delight to listen to if you love The West Wing.
Lenny (43:06):
Wait, so they go back to the old show, The West Wing and talk about old episodes with politicians?
Vijay Iyengar (43:11):
Yeah.
Lenny (43:12):
That's cool.
Vijay Iyengar (43:12):
Yeah.
Lenny (43:13):
Wow.
Vijay Iyengar (43:14):
Exactly. So, the show's over. The podcast is over.
Lenny (43:18):
Oh, okay.
Vijay Iyengar (43:18):
You have all seven seasons, but I think it started in 2016 or 2015 or something.
Lenny (43:22):
Got it. So cool. Favorite recent movie or TV show that you've really enjoyed?
Vijay Iyengar (43:27):
Pretty mainstream TV tastes. So, I really enjoyed We Crushed and Severance. Those are two good shows I really enjoyed last year.
Lenny (43:35):
Awesome. Favorite interview question that you like to ask people that you're interviewing?
Vijay Iyengar (43:39):
I'm a big fan of open-ended questions, and so one of the questions I ask in the behavioral interview at the start is, walk me through the story of you from college to now, or high school to now, if they're a more junior candidate. And couple interesting things here, interesting to see where people spend most of their time talking and where they don't, and also how they describe the other people on that journey. And do they use a standard framework to describe everyone, or do they go into each person uniquely? So, just tons of follow up questions from that.
Lenny (44:09):
Final question is, who else in the industry do you most respect as a thought leader?
Vijay Iyengar (44:14):
Got a lot of inspiration from Gibson Biddle and his product strategy medium thing. And in particular, there's a piece on proxy metrics and the shape of metrics you should use, which I found is a really... The way he frames it is a really elegant way to measure, reach and impact at the same time of your metrics. And then also a big fan of Shishir from Coda, specifically his essays liaison on [inaudible 00:44:37] questions, framing problems, and the one on marginal churn contribution. It's really interesting.
Lenny (44:42):
Amazing. Both guests of this podcast and people I love. Great choices. Vijay, this was awesome. Thank you so much for joining me. Two final questions. Where can folks find you online if they want to reach out, learn more about what you're up to? And then how can listeners be useful to you?
Vijay Iyengar (44:57):
I'm on Twitter and LinkedIn. I think my handles will be in the show notes. Not super active there, but I definitely check DMs and would love to connect on either of those. And then how can listeners be useful to me? Yeah, I mean, ultimately at Mixpanel, we're building a product for product teams. So, two things. If you haven't used Mixpanel in the last four years, we've changed a lot, as I've described on the pod, so check it out, and happy to take any feedback to help us improve the product.
Lenny (45:23):
Awesome, Vijay, thank you so much.
Vijay Iyengar (45:26):
Thanks, Lenny. It's been great.
Lenny (45:29):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
