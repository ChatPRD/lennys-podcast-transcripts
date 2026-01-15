---
guest: Sri Batchu
title: Lessons from scaling Ramp | Sri Batchu (Ramp, Instacart, Opendoor)
youtube_url: https://www.youtube.com/watch?v=RcYCU5UAZOk
video_id: RcYCU5UAZOk
description: 'Sri Batchu currently leads growth at Ramp, the fastest-growing SaaS
  business (and fintech business) in history. Previously, he led growth strategy and
  operations at Instacart and was one of...

  '
duration_seconds: 4638.0
duration: '1:17:18'
view_count: 8355
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- churn
- metrics
- roadmap
- prioritization
- mvp
- a/b testing
- experimentation
- analytics
- funnel
- conversion
- monetization
---

# Lessons from scaling Ramp | Sri Batchu (Ramp, Instacart, Opendoor)

## Transcript

Sri Batchu (00:00:00):
I do think there's actually a general path that most B2B companies take and should take. My view is you start off with founder-led sales, the early team needs to know how to actually sell. Then you hire your first couple of salespeople, then you start some very low cost targeted marketing efforts. So whether it's content, community, small scale events, and then PR, after all of that is when you start paid and brand effort and then SEO probably start around the same time that you start paid marketing efforts. The reason for the progression the way I've described it is the channels get more expensive as you go farther along and they get more effective as you understand more about your customers.

Lenny (00:00:43):
Welcome to Lenny's Podcast where I interview world-class product leaders and growth experts to learn from their hard one experiences building and growing today's most successful products. Today my guest is Sri Batchu. Sri was VP of Ops at Opendoor, then head of growth at Instacart, and currently he's the head of growth at Ramp, which as you'll hear at the top of the episode, is the fastest growing SaaS business and the fastest growing FinTech business in history. They hit a hundred million dollar yearly run rate in two years, which is absurd, and in the last year grew 4X during a period where most companies barely grew at all. I recently did a newsletter post on how Ramp builds product with their VP of product, Geoff Charles. And in this episode, we zeroed in on Ramp's approach to growth. We chat about what Ramp did in the early days to kickstart growth, how they mostly grow these days, how their growth team is structured, their prioritization framework plus their north star metrics.

Lenny (00:01:37):
Also, how they operationalize velocity, which is at the core of their team culture. Ramp is a really special company that is clearly on an incredible journey and I am really excited to share this glimpse into how they operate. Enjoy this episode with Sri Batchu after a short word from our sponsors. This episode is brought to you by Attio, a new type of CRM that's powerful, flexible, and built around your data. Traditional CRMs were built for a different era with totally different speed, scale, and data demands. Attio is different. It allows you to quickly build a CRM that matches your unique workflows and data structures. Within minutes of connecting your email and calendar, you'll have a CRM that's already set up complete with customer profiles and automatic data enrichment. You'll also have realtime dynamic reporting at your fingertips. No more slow deployments, outdated user experiences or tedious manual data input.

Lenny (00:02:32):
With Attio, you can build and adapt your CRM on the fly, no matter your business model or company stage. Attio is the CRM for fast-growing startups. Get started today and get 15% off your first year at attio.com/lenny. That's A-T-T-I-O.com/lenny. This episode is brought to you by Coda. You've heard me talk about how Coda is the doc that brings it all together and how can help your team run smoother and be more efficient. I know this firsthand because Coda does that for me. I use Coda every day to wrangle my newsletter content calendar, my interview notes for podcasts, and to coordinate my sponsors.

Lenny (00:03:11):
More recently, I actually wrote a whole post on how Coda's product team operates and within that post they shared a dozen templates that they use internally to run their product team, including managing the roadmap, their OKR process, getting internal feedback, and essentially their whole product development process is done within Coda. If your team's work is spread out across different documents and spreadsheets and a stack of workflow tools, that's why you need Coda.

Lenny (00:03:36):
Coda puts data in one centralized location regardless of format, eliminating roadblocks that can slow your team down. Coda allows your team to operate on the same information and collaborate in one place. Take advantage of this special limited time offer just for startups. Plan up today at coda.io/lenny and get a thousand dollars startup credit on your first statement. That's C-O-D-A.io/lenny to sign up and get a startup credit of $1,000. Coda.io/lenny.

Lenny (00:04:10):
Sri, welcome to the podcast.

Sri Batchu (00:04:12):
Thank you, Lenny. Thanks for having me. I'm a huge fan and I've been following the podcast and the newsletter. So excited to be on here.

Lenny (00:04:18):
Really appreciate that. So let's talk about Ramp. So Ramp where you lead growth is apparently one of the fastest growing products in history. I believe it's the fastest growing SaaS product and business and also the fastest growing FinTech business. So first of all, is that generally true and correct?

Sri Batchu (00:04:38):
Yeah, I mean I'm sure you know of Packy and he's done a great analysis where he shared this work and compared us to a bunch of other companies and when he released this a year ago, we were the fastest growing company to a hundred million dollars of annualized revenue at the time. I don't know if there's been others since, but certainly not in the FinTech category as far as I know.

Lenny (00:04:58):
Okay. So you said the fastest growing to a hundred million. I think it took two years to get to a hundred million and run rate, right?

Sri Batchu (00:05:03):
Exactly.

Lenny (00:05:03):
That's insane because rarely is there all of this money sitting around for a company to just come in and accumulate and grab from people and provide that amount of value. So that's an insane stat. Maybe another question along these lines, is there any other just stats you could share, but just the scale of Ramp or just the speed that Ramp has grown?

Sri Batchu (00:05:23):
We publicly disclosed that last year we grew Forex on top of that, very sizable based from the year prior and Okta actually released some recent stats on fastest growing software companies among SMB and mid-market and Ramp was by far the fastest growing despite the fact that a bunch of others on the list were materially smaller. The company's still very lean for the amount of growth. We're under 500 people roughly today at that scale and that's definitely have a much higher revenue per employee than some of our other competitors and others in the space. And yeah, I mean we've got a very thoughtful and smart finance team that I've worked with actually closely our old head of strategic finance at Instacart and they set ambitious goals for us on growth and I'm happy to say we've consistently beat those ambitious goals over the last 16 months or 18 months since I've joined.

Lenny (00:06:16):
Which is especially challenging in this environment. So it's extra meaningful. Okay, so here's the big question I want to start off with. I know you weren't there at the beginning of Ramp's journey, but from what you know, what do you think the team did early on to seed this level of growth and success other than just building an awesome product that people really love? And if that's the answer, that's fine, but usually that's part of it. I'm curious just like is there some clever unique tactics that they used to help create that incredible growth from the beginning?

Sri Batchu (00:06:49):
I think you're certainly right on the product side. Obviously you've recently written about Ramp's product engine with Geoff and that there's been incredible product market fit because of the product team that deeply understood the customer experience and I think that's certainly helped initial word of mouth. One thing that I did want to point out that Ramp did that was interesting is obviously Eric and Karim, the co-founders of Ramp, were previous founders of another company that they had a successful exit on.

Sri Batchu (00:07:15):
So they had a strong reputation as founders and came in with the right set of experience to build Ramp and one of the things that they did is what I call cap table as a growth strategy where they did a great job of getting a large number of early stage founders and other influential operators and advisors onto the cap table at the company. And many of our initial customers were these companies that were on the cap table or the founders were on the cap table for. And Ramp today is actually not majority startups or tech companies anymore. The vast majority of our customers are mid-market and enterprise. That's where our revenue comes from. But there's a lot of love among the tech founder community because of the early days, both the product quality as well as all of these investors that Ramp got.

Lenny (00:08:08):
Wow. I have not heard of this strategy before and I didn't know this was actually a big part of the initial story. So is there examples of folks that they had on their cap table that are examples of folks that helped them grow initially like this?

Sri Batchu (00:08:20):
One example that I can think of is Eight Sleep founder, he's been very close to the Ramp team, same with the Pod founder and then a bunch of VC firms that are investors in the company are also customers of the company.

Lenny (00:08:32):
Do you know if the strategy there was VCs who connect them to small companies that would use Ramp or is it directly founders of companies that would immediately use Ramp?

Sri Batchu (00:08:43):
Yeah, I'll say it was more founders and executives of customers that can use Ramp. Certainly we have a fantastic group of very sophisticated investors who have made introductions to Ramp as well and that helped. But I will say that is not as big of a channel as one might expect because companies have their own decision making frameworks for selecting a product like Ramp and the investor opinion and recommendation matters, but turns out it doesn't matter maybe as much as another customer who's actually used the product that they know or are actually experiencing the product.

Lenny (00:09:17):
Amazing, awesome tactic. I've not heard of that before. In terms of growth, how much of growth of early Ramp was new customers versus expansion within existing customers? Because what's cool about credit card is people spend more, you make more money because you're taking a piece of that. So roughly how much of the growth insanity over the first couple of years was from expansion within existing customers?

Sri Batchu (00:09:39):
Obviously many of our early customers have grown quite a bit and our whole strategy is to save companies time and money so they can redeploy that in other ways for their own growth or other objectives. And we obviously are growing our product suite as well like BillPay, Flex, et cetera, where our customers can spend more money on Ramp and get more value out of Ramp. Having said all of that, what's interesting is that the vast majority of our growth back then and even to this day is via new customer acquisition. It's just we are adding so many more customers that the growth of our customers while strong and important part of our growth lever is not nearly as material as you might think.

Lenny (00:10:21):
Okay, awesome. So that's a good segue to the next question I had, which is if you're going to create a pie chart of how Ramp grows and ideally if you could even share early on and then now, how does that pie chart look? What are the slices of that pie and then what are the rough percentages of where growth comes from for Ramp?

Sri Batchu (00:10:37):
Rather than going into the specifics, one thing I'll say about the growth system today is if you were to look at what percentage of our business comes from outbound sales, paid marketing, field, and then a bunch of other channels and then you compare it against industry benchmarks, I think the secret sauce of Ramp is not that we've found a channel that's unique and that we've over-invested or under-invested. I don't think our distribution would be not that far off from looking at other companies at our size and stage.

Sri Batchu (00:11:10):
I think what we've done differently is we've really focused on making all of those investments very much driven by technology and data. And so one example that I'll give you is that our sales teams are actually incredibly efficient by any metric that we look at and we obviously benchmark them. And the reason for that is because we actually have a growth engineering team that's dedicated to supporting that efficiency but including adjusting third party data and using AI to automate much of their workflow, et cetera. And we've been doing this well before AI has become the buzzword for a lot of folks, but this is something we've had this team for almost two years now that that's been working on sales automation and data to just make our sales teams more efficient. That's just one example, but we've got similar types of mandates for every channel that we invest in and thinking about how do we inform this better customer and prospect data and how do we automate and technologize it so that we can build that competitive mode for each channel.

Lenny (00:12:13):
I'd love to learn more about this growth eng team that works with sales. How is that structured maybe as the first question and then just what are their goals? How do you measure their progress and success?

Sri Batchu (00:12:24):
A lot of companies do it differently. I think what works really well with Ramp is that we have the same shared goal, which is the pipeline driven and the payback period of the channel. It's unique to Ramp where the engineers feel ownership of the quota. They're not owning product metrics or what have you, they're obviously of course interim and input metrics that are important, but they really do feel accountable for the pipeline driven and the efficiency driven by that team. And I think that naturally allows them bottom up to come with the right projects that they think will have maximal impact on efficiency and top line.

Lenny (00:13:04):
So what are the sorts of things they do for a sales team? Is it like they help them prioritize leads or is it they help craft their messaging? Which parts are maybe most important?

Sri Batchu (00:13:15):
All of the above, helping find the right prospects, sending them the right messaging as well as prioritizing responses and drafting potential responses for the team as well.

Lenny (00:13:26):
Fascinating. How much impact have you seen that has on sales?

Sri Batchu (00:13:30):
It's incredibly helpful to our sales team and it's one of our most efficient channels as I've mentioned. So I think that there is something unique about our ability to bring technology to every channel.

Lenny (00:13:41):
Super interesting. Maybe on that topic, can you just talk about how your growth team is structured at Ramp? What are the kind of sub-teams and how do you think about?

Sri Batchu (00:13:50):
We've got an organization today that might evolve and if we get to that topic we can talk about it, but historically the way we've been organized is we've got channel based teams that are deploying spend in a given channel. So we've got a paid marketing team, a lifecycle CRM team, we've got a field marketing team, et cetera. And then we've got a product engineering team that is supporting growth and sales and helping each of these channels be more effective that's dedicated to growth. And then separate from that, we've got a small kind of what I call an innovation or skunk work type of team that works on cross-channel. Just things that don't neatly fit into a box that we think could be cool or fun to try to just do more experimentation that is cross-channel, cross-team.

Lenny (00:14:37):
Definitely sounds like the most fun team. What are some of the things they've done or work on in the skunk works team?

Sri Batchu (00:14:42):
They've done testing of new channels that don't necessarily fit into very... And that includes new online platforms. They've done some interesting stuff on TikTok and Reddit and other places, things like that. They've focused on referrals and how to make that a more delightful experience for the customers, first party events, things like that. Things that are often smaller scale and if they work we can invest more and make them larger scale later.

Lenny (00:15:16):
I love it. So the teams roughly is there's a paid growth team that just works on paid growth optimization, lifecycle CRM team basically it's like emails I imagine is a big part of that.

Sri Batchu (00:15:26):
Yeah, exactly.

Lenny (00:15:27):
Then there's a field sales support team and then there's the sales team, kind of eng sales team that you talked about and then I also imagine there's like a self-serve.

Sri Batchu (00:15:37):
Yeah, exactly. There's a self-serve activation eng team as well. And then of course there's SEO and website and bound lead channel management team.

Lenny (00:15:47):
And then this awesome skunk works team. I love it. Okay, so shifting a little bit, something that comes across often and consistently with Ramp, and this came across very clearly in the post that I did on how Ramp builds product with Geoff is velocity and how important velocity is at Ramp. There's this awesome quote that I'll read here from Keith Rabois who I think led many of the rounds of Ramp. He started Founders Fund, famous investor. He said that, "Ramp's product velocity is absolutely unprecedented in my 21 years working with technology businesses." So here's my question to you. Can you just talk about what that actually looks like and feels like working inside Ramp with this intense velocity?

Sri Batchu (00:16:30):
Yeah, it is a great question and Keith is amazing and then probably one of the smartest investors that I've ever had a good fortune of working with both here as well as at Opendoor, and I'll say he's absolutely right about that. And what you see internally is what I'll say is razor-sharp focus on reducing cycle time and bias to action and how do we reduce cycle time. I think it's basically the core of it culturally to me is getting people to think about smaller units of time for decision making. It seems obvious but I think you really have to reinforce it culturally. So one thing that Eric, our CEO, does, which I don't know if you've heard externally, is we have days.ramp.com where we can see how many days it's been since the founding of Ramp internally and it's day 1,529 at Ramp. He has that number of days at every board meeting, at every all hands.

Sri Batchu (00:17:28):
It's just to remind people that we don't work in years, quarters, weeks, we work in days. Each day matters and so never put out something tomorrow that you know can get done today. And that bias to action really permeates not just in the product teams but everywhere. So our growth team, which as I've just described, is extremely cross-functional, a lot of marketing folks and other expertise on the team, but we work a lot like a product team, we work on two-week sprints, we cross-prioritize across these teams and we work all together rather than in separate silos within the growth team.

Lenny (00:18:08):
So I pulled up the site you just mentioned, days.ramp.com, and not only is it days since launch, which is 1,529 when I'm looking at it, there's a many decimal points that are counting up. 1,529.43453142. Oh my god. Okay. Is that a new addition, the decimal points?

Sri Batchu (00:18:29):
No, I think that's always been there. It's just amping it up, how much time is passing. It could be stressful at times, but I think that the mitigating factor is that it's been able, as you know, A players want to work with A players attract A players and retain A players, and Ramp has done a really great job of hiring people that are fantastic that can work in this environment well and are motivated by the success and the winning from this sort of culture.

Lenny (00:18:58):
Yeah, I was actually talking to Eric about it for another piece I'm working on and he was showing me some early board decks in every deck as you said has day 544 of Ramp. So it's very real what you're talking about. Is there anything else that just as someone that came into Ramp from other traditional companies that also move really fast, Instacart and Opendoor, that is just like holy moly, this is velocity? You talked about a few things but is there anything just like holy shit?

Sri Batchu (00:19:26):
You can see the cycle time thing in terms of responsiveness from everybody at Ramp and I think typically what you tend to see is as companies get bigger, they evolve off of Slack to email and everything just moves a little bit slower and there's process and then there's obviously a lot of good parts of that but Ramp, what I noticed when I joined and true to this day is how quickly people will respond on Slack and jump on things and even if they don't complete it, there's very clear action item on who the owner will be and what the deadline will be even if it's not. And that to me was always very impressive just about... And I think it's one of those things we build in public, so everything is very visible so you can see how this is working across teams and I'm glad that we've been able to maintain that culture even as we've gotten much bigger.

Lenny (00:20:21):
There's two effects of that I imagine. One is how do you stay in the flow and get work done if you're just expected to constantly respond? How does that actually work?

Sri Batchu (00:20:31):
I don't think the expectation is necessarily that one constantly responds, but it is something that I have seen people are good at. And so I think one of the things that, again, not like a novel productivity tool, but something that Ramp does do is just trying to think about focus time and response times and using calendar blocking to really effectively manage your time that way. And then doing calendar audits of yourself as well as of your team to say, okay, what are your highest priorities for this week, this day, this month? And how does your calendar reflect your priorities? Because in many ways you ship your calendar and so thinking about how are you spending your time and then blocking your time accordingly.

Lenny (00:21:15):
And is this mostly a cultural just this is how we operate or is there a principles or sorts of processes that are set up to help people do those sorts of things?

Sri Batchu (00:21:24):
Yeah, it's cultural in terms of how we operate, but we also have templates. Our people team has a template on how to do a calendar audit properly and things like that. So we've tried to create some learning materials as well for folks that are new to get into the flow of way of working.

Lenny (00:21:45):
Awesome. Okay, so then the other elephant in the room with talking about working really fast and hard and responding really quickly is work-life balance and burnout and things like that. One thing I'll say is I believe in working really hard and working long hours as a important ingredient to success. I know there's been a bit of a backlash against that and just like, no, you shouldn't work really hard, you can be successful without doing that. I don't think that's true. So with that said, I guess what have you learned and what do you think Ramp has learned about how to find that balance and not just-

Sri Batchu (00:22:17):
Yeah. I completely agree with you. I do think, especially earlier in your career, hard work is so important both for learning but also impact and it's a tough balance that a lot of successful companies struggle with. I think my biggest learnings is it's, A, some of it is like self-selection, right? You're hiring people that are excited about doing this work and this way of working, but at least I tend to find the people that I've worked with that are highly successful, ours are not the problem. It's really autonomy, flexibility, and mission alignment and the general happiness they get from their work. And so that's what I try to focus on, which is not the hours that someone's put in, but quality of the work and the impact. And I think a big part of the push to having great results and working hard is really being grateful and appreciating the team when they do push themselves and celebrating wins.

Sri Batchu (00:23:23):
And I think we could always be doing a better job, but I think we've historically done a great job at that, at celebrating wins big and small. And I think part of the culture of building in public and open internally helps with that. So people are always sharing their wins. And then it's a very one funny stat that I don't know if other companies track is we track engagement during all hands on the Zoom to see what percentage people participate. And it's usually close to a hundred percent, like people are talking, the entire company is talking on the Zoom chat because they're excited about the wins that their friends and colleagues are shipping and the things that we're talking about in the audience.

Lenny (00:24:05):
How do you actually track engagement? Someone sitting there watching who's in the chat?

Sri Batchu (00:24:08):
No, it must be some tool our IT team can do it. It can say what percentage of participants chatted or something like that.

Lenny (00:24:15):
I see. So it's not like who's looking at the screen, it's like who's talking in the chat?

Sri Batchu (00:24:18):
Yeah, exactly. Or reacting in the chat, et cetera.

Lenny (00:24:21):
That's awesome. And it's not like you must engage, it's more just like are we delivering the content.

Sri Batchu (00:24:26):
No. And by the way, this is probably the first time I'm sharing this. I don't think brand employees necessarily know this. I don't think we've actually shared this. I just heard it from our IT person recently and I thought that was a fun stat.

Lenny (00:24:38):
I love that because it's more just like are we providing value to people or are they actually excited and interested in this sort of thing? I was going to add onto your point about how working hard and working long hours can be seen as this like, "Oh, this sucks. I wish I was at home watching Netflix," but I find that the most fulfilling parts of my career or where I was just working insanely hard for a long time, as long as that work was meaningful, exactly like you said, it was something that mattered and came out and shipped and people were excited about it and if it wasn't like, "Oh, that was a waste of my life." So that super resonates.

Sri Batchu (00:25:09):
Yeah.

Lenny (00:25:10):
I want to come back to growth for a moment. I had a couple more questions I wanted to ask here. You talked about some of these teams that you have around ways you're driving growth. Is there an area you think you're going to be investing more in over time or that you feel is working better? I know there's trade secrets here that you don't want to share necessarily, but just anything that you feel is people are maybe under-appreciating or under-investing in that you think you might invest in more?

Sri Batchu (00:25:34):
What I'll say on that front is, look, we, like everybody else, are always focused on driving more efficiency in our growth engine. There are some channels that, and we have a diversified portfolio of bets, right? One thing that's interesting about the world of growth today is I think historically people that used to run growth were folks that had a marketing or a product background. And what you're seeing these days I think are more folks like me who actually come from an investor and analytics background to lead growth teams because growth has become more and more about a diversified portfolio of bets at a reasonable ROI and building a system that's designed around experimentation and data-oriented.

Sri Batchu (00:26:22):
So the reason I say all of that is our goal is to over time, of course, make all of our channels more efficient, but also allocate more to channels that are more efficient as long as they're scalable. And so the more that we can push customer awareness via owned and earned media, the better for us. And so we've got a few different strategies on that front, but we're also working on making our other channels more efficient by the day.

Lenny (00:26:54):
So mysterious, but I appreciate you sharing what you can. The point about the portfolio of bets is interesting because if you think about it, most companies initially grow from one. You talked about growth engines, that's the same term I use. Usually there's just one thing that helps you grow initially like SEO or word of mouth or maybe paid. And then eventually every single company basically ends up doing all the growth channels and then has a team dedicated to just keep optimizing SEO, keep optimizing referrals. So I think that's a very typical path. And then it's exactly said, how do we make each of these as efficient as possible?

Sri Batchu (00:27:28):
Yeah.

Lenny (00:27:29):
Maybe as another last question around Ramp's growth. Is there any other just really surprising, interesting, really effective tactics that helped Ramp grow over time?

Sri Batchu (00:27:41):
I think one thing that's been interesting is Ramp's ability to leverage PR as a growth machine. And as you've seen, we've got a fantastic PR and comms team and we get a lot of deserved good press through that. And one thing that's been interesting is our fundraising also as a growth strategy not obviously explicitly we've got very clear goals for our fundraising, but what we have seen is anytime that we've been fundraising and we've been using that as an effective way of creating a market moment, it's driven actually a non-trivial amount of top funnel for us.

Lenny (00:28:22):
People always talk about PR being like, people over overinvest in PR, they think PR is going to be this magical growth lever, but it actually works sometimes and in my opinion, you have to have something really interesting for it to work and obviously you guys do, the company's growing like crazy, which is innately an interesting story. The founders are really important and rarely is funding like an event anymore for most companies. So I mean this says a lot that people care about your funding.

Sri Batchu (00:28:51):
What you say it is exactly right is you have to be thoughtful about your PR moments. Everybody wants to announce things about themselves that's not necessarily interesting for the press or for an audience. And so thinking about how do you compile enough value to the general audience. So our fundraising announcements usually also have some additional color on something unique about the business that we share to provide more value to readers.

Lenny (00:29:20):
And then there's also newsletter people like me and Packy you mentioned who wrote about Ramp because it's also just so interesting. What's your sense of that versus traditional PR? There's this, I don't know, big debate of just traditional media's no longer relevant. All these other people will go through newsletters and podcasts and things like that. What's your sense there?

Sri Batchu (00:29:38):
It's what are the audiences that you get with each of these tactics. And so we do both obviously get some earned coverage in these newsletters and other tactics and we pay for some and we advertise in other cases. And what we tend to find is these are great reach, but they tend to work very well for actually hiring. It improves Ramp's reputation as a company for recruiting and hiring, which helps and they help with certain audience of customers, which is typically tech founders and folks close to the tech ecosystem. But as I mentioned, the vast majority of the world is not startups and the majority of Ramp's customers are no longer tech and startups. And so as we're thinking about ways to grow. I think channels like these are one piece of the equation, but I think traditional PR will remain another really important piece because they just target a different audience.

Lenny (00:30:38):
As you're talking, I'm watching the days count up on the days that Ramp page still and stressing me out. I feel like keeping you from doing work to keep growing Ramp, but let's keep going. I'm going to close this tab. You talked about growth engines. I'm curious what you've learned about building a growth engine in a company. And another way to put it is just a repeatable scalable growth process, whether it's at Ramp or Opendoor, Instacart,

Sri Batchu (00:31:03):
People talk a lot about what should the right design of the team be or profiles of people on the team, et cetera. And I'm happy to talk about what are the right profiles of people. I think that's an important conversation. But I think design of the team, people often... I think it's a red herring about team structure and team design and what's the right one, et cetera. I think most of that is irrelevant. What actually matters is culture and rituals and cadences rather than the team itself.

Sri Batchu (00:31:35):
And so what a great growth engine and a great growth team is one that where you set the culture, set very simple north star metrics, usually one, at most two. And you've created a culture of defining hypotheses that are data driven and a culture where that can be executed quickly and have an MVP mentality for product and non-product projects where people can fail and learn quickly and iterate quickly. So I think that part of it is more important than the specific people or their functions in many ways to me, especially when you're starting to build a growth engine. It's like can you build a set of people that can generate new ideas and evaluate them effectively and move quickly is really what you're trying to design for.

Lenny (00:32:29):
Let's unpack some of this because this is great. So in terms of north star metrics, what are some examples in your experience of good north star metrics? Revenue is obviously a very common one, but often it is too high level. Do you have a sense of what a good north star metric is?

Sri Batchu (00:32:43):
I like having two. One is something around volume and growth and you want that to be, A, very motivating and intuitive for people to understand and also, B, something that the growth teams can directly impact, right? Revenue is, for better or worse, more important to the company, but also much farther down the line of whether or not the growth team can impact that. And so at Instacart, for example, our north star metric for growth was monthly active orders. And that's what we all rallied around and looked at every day, how are now doing? And then obviously we had a large growth in consumer engineering team at Instacart, 300 plus people. And so there are people working on every single corner of the app and outside of the app on acquisition to drive growth. And it's like some of the stuff is minutia, right? It's making the checkout flow slightly better or faster or something like that.

Sri Batchu (00:33:42):
So that's a good example. It's like, okay, well, so we're going to goal that team on MAO, how are they going to move monthly active orders by making the checkout flow slightly better? Maybe they can have an impact or maybe not. And so one of the things that we did is the actual local team has their own metric that they can directly influence. You want to actually hold people accountable for things that they can influence. And then we created via the finance and data team, a translation layer for every team's metric into MAO.

Sri Batchu (00:34:13):
It would be like if you got one extra weekly order because of your checkout flow from the same customer, it would have point X impact on the company's MAO and then you would just roll up all project plans as well as project impact back into this singular MAO metric. And the other benefit of doing something like that is that it also helps you cross-prioritize much easier. Should we add more engineering to this team? Should we add more budget to that team? It's like, okay, well what's the MAO map? Where is there a more MAO per dollar or per engineer being built? And it just really helped us unify and move together.

Lenny (00:34:52):
I have questions about this. This is great. By the way, why is it monthly active orders versus just monthly orders? How can you be an inactive order?

Sri Batchu (00:35:00):
Sorry, orderer.

Lenny (00:35:02):
Oh, okay.

Sri Batchu (00:35:03):
So monthly active users basically is what it is, but we call them orders because users can just log in and not order, right.

Lenny (00:35:08):
Got it.

Sri Batchu (00:35:09):
You're actually ordering on the platform.

Lenny (00:35:11):
Yeah, I think there was this backlash against users at Facebook. I think it's monthly active people and so I get it. Okay, understood. Interesting. So you find that instead of sub-teams having a different metric that we just know is good. That's one of the variables in the formula of monthly active orders. You actually have a translation that converts that specific metric moving to the north star metric.

Sri Batchu (00:35:36):
The team on their day-to-day for their sprints, whatever are looking at their own metric. But for the purpose of planning and resource allocation and reporting, we would use the translation layers to actually just look at everything on a MAO basis.

Lenny (00:35:49):
Knowing those sorts of formulas are often not perfect, how much weight do you put into that formula specifically?

Sri Batchu (00:35:56):
Yeah. And I think in general the planning process is not perfect. You can have a financial plan in Excel and the reality can diverge quite a bit. The only thing you can be certain of is that you're not going to accomplish exactly the plan. So we did a couple of things to that. One is setting a culture of we know this isn't perfect, this is like 70/30, 80/20, it's to guide. So we wouldn't use the translation factor to make a marginal decision if something is five or 10% off.

Sri Batchu (00:36:29):
Those are done based on judgment because at the end of the day, regardless of what metric framework you use, marginal decisions are marginal for a reason. They're really hard things to decide. And so the framework helped with just reducing the cognitive overload of decision making to only those that are marginal. So the ones that are obvious that are going to have big impact becomes clear even if the measurement framework isn't perfect. And so that's what we use. And the other thing that we just had as cadence is we would actually update all of the translations every six months for the new planning cycle based on new information that we knew on how moving X impacts MAO.

Lenny (00:37:10):
Just to make it even more real, what are some examples of those lower level metrics? Is it increased conversion of sign up by X percent?

Sri Batchu (00:37:17):
Any number of things. It would be actually load time of the app on open. There's a team that's trying to make that faster or more efficient because we know that that impacts whether or not the person actually ends up ordering if it takes five seconds to load versus two seconds to load. And so the full customer experience were all segregated into different teams that were optimizing just like how long does it take to open, number of searches that a user does on the app. We know the people... And number of items that are put into cart, like amount of time from cart to check out, things like that we literally just map out any user's journey throughout the app and have separate engineering teams that are focused on that.

Lenny (00:38:04):
And there's essentially some kind of regression analysis that tells you here's load times impact on MAOs.

Sri Batchu (00:38:10):
Exactly. And the other thing that we did is just so we would've these translation factors, but we could also just see what the cumulative impact of all of the work is that Facebook did this too, which is just long-term holdouts for each surface area. So the checkout experience team that I've been talking about a lot for some reason would have their own holdout. And so we could see what the cumulative impact of monthly active orders on the people that got last half's experience versus this half's experience on the holdout. And that would make it very clear. So regression is one way to do it. And then basically effective A/B test, but was a small holdout.

Lenny (00:38:46):
Is there a holdout for the performance team where someone just has a really slow version of Instacart?

Sri Batchu (00:38:51):
I wonder actually, but there's holdout for almost everything. There's a holdout for ads, for example. So there are some lucky Instacart users out there that are not getting ads and they've never gotten ads because they've always been part of Instacart's advertising holding.

Lenny (00:39:08):
That'll be a great revenue boost whenever they want to kill that holdout.

Sri Batchu (00:39:13):
Can you imagine was a conversation internally on should there be a permanent holdout? Should it be last year's experience? How should we think about, especially because it's such a important driver of modernization?

Lenny (00:39:24):
This episode is brought to you by Eppo. Eppo's a next generation A/B testing platform built by Airbnb alums for modern growth teams. Companies like DraftKings, Zapier, ClickUp, Twitch, and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth team stack. This leads to waste of time building internal tools or trying to run your own experiments through a clunky marketing tool.

Lenny (00:39:51):
When I was at Airbnb, one of the things that I loved most about working there was our experimentation platform where I was able to slice and dice data by device types, country, user stage. Eppo does all that and more delivering results quickly, avoiding knowing prolonged analytic cycles and helping you easily get to the root cause of any issue you discover. EPO lets you go beyond basic clickthrough metrics and instead use your north star metrics like activation, retention, subscription and payments. Eppo supports, test on the front end, on the backend, email marketing, even machine learning claims. Check out Eppo at getE-P-P-O.com. That's geteppo.com and 10X your experiment velocity.

Lenny (00:40:31):
Maybe just one last question along this specific thread is this framework of having everything translated into a north star metric something you bring to every place you work now? And is this just something you recommend? For example, does Ramp approach things this way as well?

Sri Batchu (00:40:44):
I think it depends on the size of the company. I think this actually becomes much more important as companies get bigger because there's more teams to prioritize and more resources to cross-allocate. And having a common currency makes that a lot easier. And so we do something similar at Ramp as well where we have translation factors for all of the various things that the teams are doing that translate back to the north star for Ramp.

Lenny (00:41:07):
Cool. And then are you up for sharing the Ramp's north star metric or do you want to keep that part?

Sri Batchu (00:41:12):
Yeah, I mean I can tell you what we used to do in the recent past we're evolving some things and in the recent past it was for the growth team, the north star was dollars of SQL pipeline. So anything anybody did, we would try to estimate the impact into what would be the dollars of sales qualified lead pipeline generated for Ramp. So if the website team wanted to change language on the card's landing page, their direct impact would be conversion rate of email submission or something like that would be what they would be optimizing for. And then we would have, okay, what does two bips of conversion rate mean for dollars of SQL pipeline? A lot or not a lot? And depending on that, it's like, "All right, don't waste your time doing that project. Let's do something else instead." So that just helps us score and prioritize efforts.

Lenny (00:42:03):
Here's a fun story. I actually tried to sign up for Ramp when I was starting this newsletter and business and it didn't let me because I had a Gmail-

Sri Batchu (00:42:09):
For Gmail, yeah.

Lenny (00:42:13):
So I moved on and that would've been such a huge revenue opportunity. I'm just joking.

Sri Batchu (00:42:18):
I know, I know. And I'm glad you brought that up because we are obviously aware of it and we are working on something for users that have put in a personal email address. in terms of how to reengage that.

Lenny (00:42:30):
You're about to 5X growth because I had no other domain at that point. Now I have Lenny's newsletter and stuff, so it's like, "Shit, I'm stuck."

Sri Batchu (00:42:39):
By the way, for anybody else that has that problem, they can just reach out to me, we'll figure it out. The reason we don't allow personal emails is because it's just typically very low in tech users that are coming to the website that are putting in personal emails.

Lenny (00:42:51):
Makes sense. I totally get it. I was not offended. I just like, all right. I had no way around it. That's the problem. So I like that you guys are adding some path around it and you're saying email you or reach out to you.

Sri Batchu (00:43:02):
You can find me on Twitter or email me. I'm just as sribatchu@ramp.

Lenny (00:43:06):
All right. You're going to have the most sales leads of any person at Ramp when this comes up. Okay. One other thing I wanted to touch on is success metrics. You talked about one of the keys to success and this repeatable growth engine is clear success metrics. Is there any just learnings and tips you have for people when they're thinking about success metrics?

Sri Batchu (00:43:26):
Finding the right success metric, there usually should be two. There should be one on volume and another one on efficiency. And we can talk about what are good efficiency metrics and what are good volume metrics. On volume, I think the right success metric has a couple things that are important. One is there's a clear linkage to value creation for the business. So if I move this metric that will drive revenue and which will drive equity value for the business or whatever it is that this particular. Metrics and for Facebook it was MAU, for Instacart, it was effectively monthly active orders, and it's something that we know is important that will really drive the value for the business, but it needs to have the other component of it, which is it's very intuitive for all of the people working internally to the company.

Sri Batchu (00:44:17):
And it's also clear, if they're working on some minutiae, how that can impact and actually move the main metric. So it's usually you have to find something that's somewhere in between, not too far, too lag, towards revenue and value creation, but also not something that's actually translatable to the efforts of various teams.

Lenny (00:44:39):
Is there an example of a good success metric that just comes to mind to make this a little bit concrete for people?

Sri Batchu (00:44:44):
It just depends on what goal at any given time is. Sometimes you're trying to drive more users, sometimes you're trying to drive more engagement and you can reorient the company on what you're trying to do as the north star for growth during that period of time. So users, obviously we've talked about as a good one. For engagement, I've often found what really helps is, and you've done actually really good benchmarking at some point, the escape velocity metric for growth for a company, I think.

Sri Batchu (00:45:15):
I don't think you phrased it that way, but that's [inaudible 00:45:18] for a given user, which is what does it take for somebody to become an engaged and active user or customer of a platform? And at Facebook, it was 10 friends the first seven days. At Instacart, it was three orders in the first month. And at Ramp, for our activation, I mean it's very specific to Ramp, but we've got four events that the customer needs to do in the first 30 days. And if they do that, they have a high likelihood of being activated and successful. So our activation team focuses on that.

Lenny (00:45:49):
The framework you just described reminds me Gibson Biddle has this really simple framework of gem where you can basically prioritize one of three things, growth, engagement, or monetization. And his advice is always just all of them are great, just make sure you're all aligned on which one matters most at the time.

Sri Batchu (00:46:06):
Yeah. And it is very similar to, we used to have this at Opendoor, and I think DoorDash also uses a similar framework, which is speed, quality, and cost. All three are important, but it's very hard to optimize all three at the same time. So you need to have a particular prioritization. And I think growth teams can also use that as, okay, I think the way I about the growth team's journey is step one is build a system that can move fast and then work on improving the quality and then work on optimization of cost after. So you pick which phase you're on because you can't do all three at the same time, whether it's growth, engagement, monetization, or just the other way of framing on it.

Lenny (00:46:49):
Speaking of metrics, I have this note here that you're a big fan of payback period for measuring investment ROI versus CAC. Can you talk about why that is?

Sri Batchu (00:47:02):
Yeah. CAC obviously gets thrown around a lot and a lot of people are like, "Okay, you have to be reducing your CAC, CAC, CAC, CAC." There's a fundamental flaw to it which obviously is that you're focusing on cost and not the value derived. And so when you focus on CAC and reducing CAC, what tends to happen is you actually might be doing something very damaging where you're succeeding in reducing CAC, but you're actually bringing in customers that are less valuable because those are the ones that you're able to attract with a lower CAC. And so reframing it away from CAC towards LTV is helpful and that's better. So thinking about for better customers that are bigger, we want to spend more. So you might think, okay, well, LTV to CAC might be a better way of looking at that. I think the challenge with LTV to CAC especially for a lot of, even Ramp, it's only four years old, is it's really hard to predict LTV.

Sri Batchu (00:47:57):
It's like a DCF, it's extremely assumption laden and it's hard to know what the final value will be. And especially if you think your churn is low and your LTV is very high, you might end up spending a lot of money because you're like, "Oh, my LTV to CAC is great." And then a year or two into the business, you realize actually your churn is higher than you thought. Your initial customers aren't representative of your long-term retention and all of a sudden you've destroyed a lot of value by looking at LTV to CAC, which is why I'm a big, big fan of payback period and actually being really thoughtful about that using contribution margin, not revenue or gross margin, like how long of contribution margin from this customer does it take to payback their cost? And setting this obviously is typically a mandate from the executive and board level on what is the payback period that we're comfortable with, and then just orienting everybody towards driving that blended payback period down as much as possible.

Lenny (00:48:56):
For folks that aren't familiar with the concept of payback period or contribution margin, could you just briefly describe what those mean for listeners?

Sri Batchu (00:49:01):
Yeah, so contribution margin is basically the profit that you make on a given customer after you take into account all of the variable costs. So including the cost of production as well as any other variable costs to serve that customer. So that might include support and other things that scale with your revenue. And then payback period is literally just how many months of that profit would it take to pay for? Let's say it costs you $5,000 to acquire this customer and your estimated profit per month on the customer is 500. That is a 10-month payback period. So as I say that, I'm sure you've heard, you still have to make assumptions for payback period, but at least they're more based in recency and you can evaluate them more quickly.

Lenny (00:49:49):
Awesome. Thank you for doing that. Just a couple more questions around growth specifically. So there's a lot of ways to grow through the history of a company. You can invest in SEO, you can invest in paid and sales and referrals and influencer marketing, brand marketing, billboards, all these things. Do you have an opinion on how to sequence these sorts of bets for a company, especially in B2B?

Sri Batchu (00:50:10):
Of course, a lot depends on who your customers are, what your unique value propositions are and how competitive the space that you're in. But I do think there's actually a general path that most B2B companies take and should take frankly, which is my view is you start off with founder-led sales, like the early team needs to know how to actually sell, then you hire your first couple of salespeople, then you start some very low cost targeted marketing efforts. So whether it's like content, community, small scale events, and then PR. After all of that is when you start paid and brand efforts. And then SEO probably start around the same time that you start paid marketing efforts.

Sri Batchu (00:50:56):
The reason for the progression the way I've described it is the channels get more expensive as you go farther along and they get more effective as you understand more about your customers and they're more scalable as well as you go farther along the list that I've described. And so that's the intention behind sequencing in that way. SEO is a bit unique. The reason I recommend it later rather than earlier, even though it's not necessarily that expensive, is just take some time to build. And without domain authority or backlinking or any media presence, you can end up just flailing with SEO, creating content and not getting any actual traction for a long time. So there's usually a good inflection point for your company to double down on SEO efforts. And it's somewhat a little bit later than some of the other times.

Lenny (00:51:43):
This touches on a great line that you have around experimentation where you talk about how you don't want to just fail fast with an experiment. You want to fail conclusively, if that's the word. Is that right? And then can you talk about that?

Sri Batchu (00:51:57):
Yeah, I talk a lot about that with my teams both here and other places, which is we celebrate failure. Growth experiments in my history are typically 30%-ish success rate. So the vast majority of things that you try don't work. And so you want to create a culture where people aren't afraid to take risks and aren't afraid to fail. And for me, failure is not that you didn't drive revenue, failure is not learning. So it's really important that you learn when you fail. And so we celebrate failure as long as you're learning and you can only learn if you've designed the right test and you failed conclusively because otherwise, I think many of us have been in situations where there's intuition that something might work and it doesn't work, and then you end up doing it over and over for years because every time a new executive or somebody else has the same idea, you try it again and it's because you haven't been able to design the test to fail conclusively, and it's hard to do.

Sri Batchu (00:53:00):
But at the end of the day, there's only two ways to make an experiment successful. Either you have a very large M or have a very significant treatment, which is what you're doing in the experiment itself. And in B2B, you don't usually have the luxury of large M, which you do in consumer. Facebook can get stats taken in two hours. A B2B company could take two years to get the same number of touch points. And so to counteract that, I recommend people just trying to maximize the treatment effect, which is if you have a hypothesis that you're testing, just throw all of the possible tactics and resources that you think would move that needle because you can always cost rationalize later if it works.

Sri Batchu (00:53:49):
And so just maximize the treatment effect. And if with all of that it didn't work, then you can say, "Hey, we're not going to try this again because we literally did try everything that we could to test this hypothesis." And if it doesn't work in the best version and it's expensive as it is, this is not worth spending more time on. But if it does work, great, then you do another version of the test with half the tactics or whichever tactics you think work better or worse and you optimize over time.

Lenny (00:54:17):
Is there an example you could share when you did that?

Sri Batchu (00:54:19):
I mean, account based marketing is something that is very common in enterprise software where you've selected certain customers that you think are high priority and you're saying, "I want to touch them in as many nuanced ways possible to see if that drives conversion." And this is something I've seen tried many times where people do it, but they do it halfway where they're like, "Okay, tried these three things. Conversion of the control group wasn't higher. And so we think this is not going to work."

Sri Batchu (00:55:00):
And then a new go-to market executive comes and they have to do it again. They have to do it again. They have to do it again. It's a very common one wherever this happens. And so when we did it at Ramp, we did exactly what I just described, which is let's really be thoughtful about the experiment design, both in terms of maximizing the number of people as well as maximizing the number of ways and types of ways that we're effectively touching these target customers to show the value one way or the other.

Lenny (00:55:31):
So what it sounds like is the hypothesis isn't like this email will have a big impact on conversion. It's like this strategy of coming after customers is what we're testing.

Sri Batchu (00:55:43):
That's the example there. And I think for example, this kind of framework is more important for cross-functional, larger scale, bigger tests rather than an email modification. But we could even use it on a micro example, like an email modification where you are like, okay, I think this particular email is underperforming because it's not talking to this part of the customer's pain point or journey or what have you. And the simplest test would be, okay, let me make some tweaks to the text and edit that, and that could be the end of that test.

Sri Batchu (00:56:24):
And if that doesn't work, you're like, "Oh, maybe those weren't the right text edits. Let me do a different text edits or whatever." And that's fine, that's low cost. It's not the end of the world for you to be wrong there. But an alternative that you could do is like, oh, what are all of the things that I could change about this email in the same test? Is it the trigger of the email? Is it the text content of the email? Is it additional personalization? Is it the design of the email? Trying to think of what are all of the various levers that you think could be wrong and put them all together to test your hypothesis of this touchpoint is wrong and how do I improve that.

Lenny (00:57:02):
Well, obviously the downside of that is if it doesn't work, you don't know if it's like, oh, maybe it was this thing could have worked in the subject-

Sri Batchu (00:57:08):
Yeah. So there's always trade-offs on this. But what you're hoping is you've done a complete refresh where you did all the things that you thought were intuitive that should work. And if it doesn't work, then you're like, "Okay, maybe my hypothesis is wrong." But you're right. There's always going to be a challenge if maybe the execution is wrong and I did too many things potentially in that case.

Lenny (00:57:29):
How does that go with the velocity culture? Is it just do those things real fast even though it's not like micro optimize, it's like go bigger but do them fast?

Sri Batchu (00:57:39):
Yeah. Yeah. So that's why I think it's important to frame where this matters. And so I think I'm less worried about failing conclusively for things that you can fail really, really fast and just redo, right? Things like website conversion, email, et cetera. I'm more worried about that for things that take a while to plan and cost money, et cetera.

Lenny (00:58:05):
Got it. Okay. Great. Maybe one last question around growth specifically. What are some of your favorite tools for the growth team, either internally, whatever you can share, or externally that just allow you to operate efficiently and effectively?

Sri Batchu (00:58:19):
A couple of things that we've used, I mean, one simple thing is for sprint planning, actually, we use Airtable because the planning process and the scoring is so much more analytical and the translation layer. So we've got a template on how we do our sprint planning and how we translate the various impact metrics into the common currency, which I enjoy, but I don't see it has to be Airtable. It's just some form of organization that works well for that. In terms of a very tactical growth tool that we've enjoyed recently is we used this company called Mutiny, which is also around customer, which is a tool for website copy, personalization. So they hook up with our third party data sources that we pay for, and based on what we know about the customer as they're landing on our page, we can personalize, copy, and design based on that. And that's had material impact and allowed us to scale website experimentation.

Lenny (00:59:18):
Amazing. And then are there internal tools you've built to help with experimentation or I don't know, sharing data, dashboard? I don't know, is there anything else that's just like, wow, this really helps us move fast?

Sri Batchu (00:59:27):
Eric, our CEO, has publicly talked about this. I think we as a company are very thoughtful about what we build in-house versus what we buy externally. I think a lot of engineering teams are often excited about building things in-house where there's off the shelf products that could basically work externally. And Ramp has historically been good at not falling into that trap. And we use third party tools for a lot of our growth and experimentation for things that are not proprietary, strategic, et cetera, obviously. Some of the automation stuff that we've talked about, we've built all of that in-house in terms of prospecting, lead scoring, and how we talk to our customers. But for the most part, we use external tools. Instacart and Opendoor were not like that. We built our own internal experiment tracking systems, A/B testing frameworks and all of that in-house.

Lenny (01:00:25):
That's what I would've guessed about Ramp that it's with speed, you got to not build stuff you don't have to build. So that makes a lot of sense. Okay. Maybe one last topic to talk about. I want to talk about hiring. You have some really interesting approaches to how to think about hiring. One is I think you have a really interesting strategy for how to find the best companies and also the best people at each of those companies to go after if you're hiring for specific role. Can you talk about how you think about that?

Sri Batchu (01:00:51):
Gokul on Twitter has talked about some of those, which is there's two ways to go about hiring great people. One way is basically a very thoughtful and tactical network search where let's say you're hiring for a head of SEO, you go ask your network of who is the best SEO person you know, get introduction to each of those folks, and then ask them who the best person that they know is. And you have a mapping of where are the best SEO teams and why. If you can't get one of those people, 20, 30 people on your target list, you go down the list of, okay, what is the next best person? And you typically want to limit it to companies that are one to two stages of growth after you. So you want somebody that has seen your stage of growth and beyond at a company that has a reputation for craft and the field that you're looking for. So that's a very classic way of doing that, and I think that works really well for people and companies that are really well-connected.

Sri Batchu (01:01:56):
So there's another approach that I've actually used successfully is much more kind of data driven and external and not as network based, which is you can often look up data. [inaudible 01:02:14] is a lot of it is somewhat public, right? So you can look up information on which companies might be doing well. So for example, I'll just pick like if you're looking for great email marketing folks like CRM marketing lead or something like that, you can actually look up on similar web, what percentage of traffic shows up via email to companies websites. So you've got your target list of companies that are one or two stage beyond you that you respect as general companies. And you can go and see, okay, which ones of these are actually really effective at driving web traffic or app traffic or app downloads via their email. And then go try to source from those teams and companies. And I think people under-utilize that even though it's very intuitive, it's just not something that occurs to people to do.

Lenny (01:03:03):
I love that. I've not heard that tip right there. The first piece, Google definitely recommends this, and I think the core part of that is the core theme here is find the companies that are the best at the thing you're trying to hire for, and then figure out who at the company is the best once you start talking to people. I love it. Another strong opinion that I think you have is around paying people and how much to pay the best. Can you talk about that?

Sri Batchu (01:03:30):
Yeah, I think there's a lot of conversation around compensation is very much focused on equality and narrowing the gap and bands for compensation. And I think personally, I know it's a bit of a spicy take maybe, but I think it's the exact opposite direction of the conversation that companies should be having about compensation, which is I strongly, strongly believe that small teams of successful people can drive a lot more impact than larger teams of mediocre people.

Sri Batchu (01:04:05):
And so I strongly believe you have to design a system where you're able to reward 10X operators with 10X the comp. You certainly see that at the executive level. So if you look at the same executive at different companies at similar stages, the comp can be widely different based for a variety of reasons. But one of them is the perception of performance and potential by the management team. And I think people need to be thinking about how to do that across more levels, which is if you can do that, and if you do that well, I think you're able to differentially hire and retain the best talent. And that'll be a great competitive advantage for companies that can do that well.

Lenny (01:04:48):
And do you think about this within a team pay the best people the most, or is it more only hire these 10X people and then pay everyone the most?

Sri Batchu (01:04:58):
People think of the talent density of your company as dependent on hiring. And that's obviously true. It's an important part of the ecosystem and the first part, but it's equally dependent on retention and performance management. A lot of companies can be good at hiring, but hiring has pretty high rate of false positive. Interview is the worst, best way to hire somebody. And then there's lots of ways you can make the interviewing process better, make it more interactive, make it more effective, but at the end of the day, you still don't know about someone until you really work closely with the new team, with the new mandate at your company.

Sri Batchu (01:05:40):
So I think it's not about necessarily hiring [inaudible 01:05:44] operators, obviously you're looking for that, but it's also about investing in people that are doing really well and accelerating their growth and rewards based on impact once they're there and as well as managing out people directly that didn't work out. And I typically think it's almost never when I've had to part ways with people is because someone's a bad actor. It's almost always that it just wasn't the right fit for whatever reason, for their skillset, for their life goals or whatever it may be. And it just wasn't a fit for that role. And I think a lot of companies are hesitant to make those changes, and I think that's how they bring their talent bar down, frankly.

Lenny (01:06:28):
Absolutely agree. Sri, is there anything else that you wanted to touch on before we get to our very exciting lightning round?

Sri Batchu (01:06:35):
I don't know how many people will use this. I'm still surprised when new folks come to me and it's like I need to write, by the way, a document of how do you work with me? Because I know it's a lot of people have been talking about, I think [inaudible 01:06:51] Johnson's talked about it too, but I say that my love languages are spreadsheets and frameworks. And one very simple one that I've always liked that sometimes people surprised to hear, but it's most consultants know is what we call MECE, mutually exclusive, collectively exhausted set of things. So whenever you're trying to attack a problem and trying to brainstorm solutions or what have you, I really like to remind the teams to think about MECE because when you think about that and evaluate your set of solutions with that framework in mind, I think you tend to find that you've catch more potential solutions and also you'll feel comfortable that you've been comprehensive in your solution development. So anyway, just a little thing for people that are earlier in their careers to not forget.

Lenny (01:07:46):
So let's make it a little bigger than a little thing. So MECE, mutually exclusive, collectively exhaustive. Is there an example of what that may look like and or visualize for people to think about what this means in practice?

Sri Batchu (01:08:00):
Yeah. I mean, I'll give it really dumb example, but that will make the point hopefully. It's like, okay, our profitability or our revenue growth has slowed down is the problem that you're trying to solve. And so okay, you start with, okay, what does this mean? You've got revenue per user has gone down, or customer has gone down, or number of customers have slowed down. Okay, that's step one of the MECE framework. Then it's like, okay, where does the revenue come from? What are all the various products that revenue could be coming from? Has it changed on any one of them? And then customers, why have customers gone down? Is it new customer acquisition? Is it activation of customers that have signed up? Is it retention? And just breaking that problem. So at each layer you've collectively exhausted all of the possible ways that this problem could have arrived. And just having that framework whenever you approach every problem will prevent you from missing something important. And also just more generally give you an others' confidence that you're being comprehensive in your solution development.

Lenny (01:09:11):
Got it. So one way to think about this in this specific case is just make a formula of all of the variables that play into the question you're trying to answer.

Sri Batchu (01:09:19):
Yeah, exactly.

Lenny (01:09:20):
Awesome. Well, Sri, with that, we've reached our very exciting lightning round. Are you ready?

Sri Batchu (01:09:26):
Yeah, let's do it.

Lenny (01:09:28):
What are two or three books that you've recommended most to other people?

Sri Batchu (01:09:32):
I tend to find most business books can be decks, but one that I really like actually is Never Split The Difference by Chris Voss. It's a negotiation book, find it super helpful for negotiation, but also for a lot of business decision making generally, to be honest, and life. And then I'm a big fan of sci-fi short stories, so anything by Ted Chiang or Ken Liu, I highly recommend.

Lenny (01:09:57):
I love those both. On the first one I'm actually in the process of listening to it on audio and every time I'm in a place where I can negotiate something, I never remember anything that I've learned. Is there one thing that you've taken away from that book that stuck with you of like I use this?

Sri Batchu (01:10:11):
I think that the core of the book really is about listening behind the problem of negotiation and what is the person really asking for. So his example of if you're always trying to split things evenly, you'll end up with one brown shoe, one black shoe, where neither of you are happy. And so rather than thinking about BATNA and ZOPA and all the other business school frameworks on negotiation, I think focus on deep down what does this other person want and how can I change the conversation about that rather than the thing that we're arguing over.

Lenny (01:10:47):
Awesome. Great. Next question. What's a favorite recent movie or TV show?

Sri Batchu (01:10:51):
I mean, obviously it won the Oscar, but I really enjoyed Everything Everywhere All at Once. I thought it was such a wonderful story and really I think it's one of those... It's funny. The movie can also be, I think, everything because there are just so many different reads that you can get about that. It's about family, it's about immigration, it's about love. There's a lot of really interesting themes explored via one movie.

Lenny (01:11:19):
What's a favorite interview question you like to ask?

Sri Batchu (01:11:21):
I was going to say, oh, I like to ask other people.

Lenny (01:11:24):
You like to ask. What did you think I was going to ask?

Sri Batchu (01:11:26):
Oh, I thought what was my favorite interview question that you've asked or others have asked?

Lenny (01:11:30):
Oh, I got to clarify this. Both are acceptable answers.

Sri Batchu (01:11:37):
I was going to cheat on that one and say the one that you asked me right before, because I'm a big fan of actually movies and TV shows and people rarely ask about that interviews like this, but favorite interview that I'd like to ask candidates actually is what's something that you're really bad at but you still do and why?

Lenny (01:11:58):
What do you look for in their answer when you ask them?

Sri Batchu (01:12:01):
Yeah, a lot of people actually struggle with that question and can't answer anything that they do that they're bad at, which is a little bit of a yellow flag, which means that they're only used to doing things that they're successful at and they haven't cultivated interests that are not correlated to their own success at doing something. And they haven't taken the time to do that. And folks like that are going to run at the first sign of trouble and be like, "Oh, I'm not successful at this, so I'm going to move on." And what I really want to see is people that show examples of things that they're not successful at that they do for other motivations and goals and interests. And so if you can tell me a compelling story like that, it's usually a winning answer so to speak.

Lenny (01:12:43):
What is a favorite product or two that you've recently discovered that you love?

Sri Batchu (01:12:46):
Carrie mentioned Eight Sleep once in this call. I love my Eight Sleep. I'm a big fan and they're Ramp customers as well. And so that's been a great pandemic purchase. So I guess maybe not as recent. And then maybe another one is Fellow coffee, their kettles I think just designed so beautifully. I don't drink coffee, I drink tea, but I use my Fellow kettle for tea, and I think it's just a delightful product to use.

Lenny (01:13:15):
I got a Fellow kettle from my tea also, and I found that the flow of the water was too slow and it's just standing here pouring this pour over.

Sri Batchu (01:13:24):
Yeah. Yeah. So they do have a non-pour over kettle, which is what I have, which makes it easier.

Lenny (01:13:29):
Okay. My mistake. Next question. What is something relatively minor you've changed in your product development process that you found to have a big impact on your ability to execute?

Sri Batchu (01:13:42):
Yeah, I mean, I don't know if this is minor or not, but one of the things that on the growth side, we used to have separate sprint planning for the product team, for the marketing teams, and each team had their own planning cycles. And one of the things that we did is we brought them all together into one. So the lifecycle marketers joined the product activation team sprint cycles, and so their projects and work are very tightly aligned and work in the same pace and system as the rest of the product team. And that's had tremendous impact in our ability to work together.

Lenny (01:14:19):
Final question, Ramp is all about helping people save money. I'm curious if you have any tips on just saving money.

Sri Batchu (01:14:26):
I mean, it seems obvious, and I think I feel like negotiation's already been the theme of this lightning round, but everything is negotiable when it comes to contracts. People think contracts are standardized for software and usually not. People are trying to sell you something they're trying to grow too. They have their quotas to meet, they have their goals to hit. So I mean, Ramp obviously has a service for this if you wanted to scale these Ramps, but you can do this on your own. Always try to negotiate, be mindful of quarter ends for salespeople. And so if you can push something out till near the end of the quarter, you can ask for, "Hey, I'll sign it by the end of the month if you give me a 10% discount," will often work. So there's tips like that you can do, but remember that you can always negotiate.

Sri Batchu (01:15:10):
And then the second one is, I would say is just hire slower. I'm a big believer in, and Geoff talks about this too in your other interview, hiring based on slope rather than intercept, I think will work well for you and only hiring when people and teams are really stretched. I think this will serve you well both on cost and on impact. There'll be plenty of scope for the people that you hire, and as I said, I'm a big believer in small teams accomplishing more like Ramp being like a fraction of the size of some of our competitors with similar orders of revenue.

Lenny (01:15:47):
Sure. We've covered velocity, growth, hiring. So many topics, everything I was hoping we touch on. Two final questions, where can folks find you if they want to reach out and learn more and how can listeners be useful to you?

Sri Batchu (01:15:59):
Yeah, I'm a big fan of the fun place of the cesspool of Twitter, so I have a public Twitter account that you can DM me. My DMs are open, it's just my name's sri_batchu. And in terms of listeners can be useful, honestly, I think I really enjoy meeting like-minded folks, and as I may have mentioned in other places, Ramp is growing incredibly well and we're constantly looking to hire and we're still hiring. So if you know best in class growth in marketing folks that they can recommend that we hire at Ramp, I'd love to hear.

Lenny (01:16:40):
And I think the URL is ramp.com/careers. I just pulled it up.

Sri Batchu (01:16:43):
Yep, that's it. Thank you.

Lenny (01:16:47):
All right, Sri, well thank you again so much for being here and for sharing so much.

Sri Batchu (01:16:49):
Yeah, of course. Thank you.

Lenny (01:16:52):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

