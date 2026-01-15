---
guest: Nabeel S. Qureshi
title: How Palantir built the ultimate founder factory | Nabeel S. Qureshi (founder,
  writer, ex-Palantir)
youtube_url: https://www.youtube.com/watch?v=xQkSenlJvwA
video_id: xQkSenlJvwA
description: '*Nabeel Qureshi* is an entrepreneur, writer, researcher, and visiting
  scholar of AI policy at the Mercatus Center (alongside Tyler Cowen). Previously,
  he spent nearly eight years at Palantir,...

  '
duration_seconds: 5849.0
duration: '1:37:29'
view_count: 23065
channel: Lenny's Podcast
keywords:
- retention
- metrics
- roadmap
- iteration
- analytics
- revenue
- hiring
- culture
- management
- vision
- mission
- competition
- market
- persona
- design
---

# How Palantir built the ultimate founder factory | Nabeel S. Qureshi (founder, writer, ex-Palantir)

## Transcript

Lenny Rachitsky (00:00:00):
30% of PMs that leave Palantir start a company. Just give us a picture of what the people are like.

Nabeel S. Qureshi (00:00:05):
I feel like they screened really hard for a few traits in particular. One is like very independent-minded people who weren't afraid to push back. Two is people with broader intellectual interests.

Lenny Rachitsky (00:00:15):
What's the difference between, say, a PM at Palantir versus a traditional PM?

Nabeel S. Qureshi (00:00:18):
They were extremely careful about only making people PMs who had first proven themselves out as forward deployed engineers. You basically could not become a PM any other way. There's two types of engineer at Palantir. So, there's one that works on the core product and they're a traditional software engineer. There was a different type of engineer which you sent into the field. You would spend maybe Monday to Thursday and you would actually go into the building where the customer worked and you would work alongside them. You would literally get a desk there and so, that engineer became known as a forward deployed engineer.

Lenny Rachitsky (00:00:51):
What's something that you believe that most other people don't?

Nabeel S. Qureshi (00:00:54):
I think this is a somewhat contrarian view within tech.

Lenny Rachitsky (00:00:58):
Today, my guest is Nabeel Qureshi. Nabeel is a founder, a writer, a researcher, and an engineer. He was recently a visiting scholar researching AI policy at the Mercatus Center alongside Tyler Cowen. At one point, he worked with the National Institute of Health and major clinical centers to create the largest medical data set in the world. He worked at the Bank of England for a bit. He was founding member and VP of Business Development at GoCardless, one of Europe's biggest financial technology unicorns.

(00:01:23):
And most related to the topic of this conversation, Nabeel spent almost eight years at Palantir as a forward deployed engineer working on public health projects with US federal agencies, including public health services during the COVID-19 response and applied AI in drug discovery. Whether you are a fan of Palantir or hate everything that they do, they are an important and fast-growing company that is pumping out incredible product leaders, as you'll hear more than any other company in the world. So, it is worth studying and understanding.

(00:01:52):
I've never heard an in-depth conversation digging into how they operate, build product, hire, and were able to scale from a primarily services business to a software business. So, I am very excited to bring you this inside look. In our conversation, we go deep into what the heck does Palantir even do, why getting good at managing lots of data is an underappreciated secret to their success, a look at the unique forward deployed engineer role that they innovated, and what other companies can borrow from their insights here. Also, how they hire and how they build amazing product leaders, plus a ton of advice on talking to customers, building products, and starting companies.

(00:02:26):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a bunch of amazing products for free for a year, including Superhuman, Notion, Linear, Perplexity, Granola and more. Check it out at lennysnewsletter.com and click Bundle.

(00:02:44):
With that, I bring you Nabeel Qureshi.

(00:02:47):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point, your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow and Loom.

(00:03:19):
WorkOS also recently acquired Warrant, the fine-grained authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases.

(00:03:42):
If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM or user management, you should consider WorkOS. It's a drop-in replacement for auth zero and supports up to one million monthly active users for free. Check it out at WorkOS.com to learn more. That's WorkOS.com.

(00:04:05):
This episode is brought to you by Attio, the AI native CRM. Attio is built to scale with your business from day one. Connect your email and calendar and Attio instantly builds a CRM that matches your business model with all of your company's contacts and interactions enriched with actionable insights. Sync in your product usage, billing info, or any other data sources and Attio's flexible data model will handle it all without any rigid templates or workarounds.

(00:04:33):
With Attio, AI isn't just a feature, it's the foundation. You can do things like instantly prospect and route leads with research agents, get real-time insights from AI using customer conversations, and build powerful AI automations for your most complex workflows. Industry leaders like Flatfile, Replicate and Modal are already experiencing what's next for CRM. Go to attio.com/lenny to get 15% off your first year. That's attio.com/lenny.

(00:05:08):
Nabeel, thank you so much for being here. Welcome to the podcast.

Nabeel S. Qureshi (00:05:12):
Thanks, Lenny. Glad to be here.

Lenny Rachitsky (00:05:14):
In our chat today, I want to zero in on a post that you recently wrote where you shared your reflections on your time at Palantir. You spent something, maybe just under eight years there. The reason I'm really interested in Palantir is I've been doing a bunch of research recently looking into which companies hire the best product managers and create the best product managers, and Palantir just keeps coming up over and over in the work that I'm doing.

(00:05:37):
So, I'll share a few stats real quick. I looked at which companies produce the most founders, especially out of their PM team, and Palantir is, by far, number one. 30% of PMs that leave Palantir start a company. And number two is 18% and that's Intercom. So, that stat, I looked at which companies PMs that leave get immediately promoted in their next role, Palantir is number one of all companies in the world.

(00:06:02):
I looked at which companies' PMs become the first PM at another startup that they join, Palantir is number two in the world. And then I looked at which companies alumni PMs become heads of Product down later in their career, Palantir is number three in the world. Also, just the company is doing extremely well. It's worth, I think, something like $200 billion these days. So, there's a lot to learn from Palantir.

(00:06:27):
I actually want to start a question that I imagine every employee at Palantir constantly gets that, and I still don't think people totally have an answer in their head. What does Palantir do?

Nabeel S. Qureshi (00:06:38):
That's a great question. You started off with an easy one, Lenny. So, Palantir is, the way I describe it, is they achieve outcomes for their customers very tactically. The way they do that tends to be through a data platform. So, they have what I consider to be the world's best data platform, and I can go into what that means in a second. And then there's a couple of different versions of this. So, there's one that's optimized for intelligence and defense use cases that one is called Gotham. And then there's one that's more optimized for commercial use cases and that one's called Foundry.

(00:07:12):
And that's the classic explanation of what they do. So, they sell a data platform. They typically work with very large customers is the other thing. So, it's going to be Fortune 50. It's going to be governments around the world. It's going to be those kinds of customers. So, that's the capsule answer, but there's lots to unpack in there.

Lenny Rachitsky (00:07:32):
Awesome. Okay, and we're going to touch on a lot of this stuff, including the data piece. I want to start with talking about just the people and the culture of Palantir. You shared a bunch of really funny stories of what it's like to come to work and even interview at Palantir. There's a story you shared where because maybe the co-founder, you're walking by and he's chewing ice, and that's some benefits to cognition. Just give us a picture of what the people are like, especially early days Palantir and the culture and how unique it might seem.

Nabeel S. Qureshi (00:07:58):
Yeah, it's definitely, it's an add-a-one company. I don't know how else you would start this company if you were not somebody like Peter Thiel. And so far as, it seems like there was a point at which they owned a silly fraction of the office space in Palo Alto. So, you'd walk around Palo Alto and there would just be Palantir hoodies, Palantir buildings everywhere and so on.

(00:08:21):
And so, I feel like what happened at some point is they raised a lot of money and they resorted to all these really interesting ways of just getting top talent out of places like Stanford and other top schools and just people who knew the founders who tended to be very interesting intellectual people. And I feel like they screened really hard for a few traits in particular. So, I would say one is very independent-minded people, people who weren't afraid to push back, who questioned the frame of everything and thought for themselves and had strong convictions.

(00:08:55):
Two is just people with broader intellectual interests. Karp just released a new book and he's quoting Habermas and all these European intellectuals and just things you don't typically see a tech CEO do. And so, I think there's that intellectual strand in the company. And then yeah, I think three is just people who are very intensely competitive. There's a sort of win at all costs mentality to the company. And so, I think those were the set of traits that were this gravity while in California at a certain time. And so, you just had a lot of really fascinating people joining the company at that time.

(00:09:33):
The way they screened for this was interesting too. So, for the longest time, they had... Everyone does this now, I think, but at the time, it was a little bit rarer, is a founder had to interview you in order for you to receive an offer. And so, a founder, it could have been Alex Karp, it could have been Stephen Cohen. Earlier on, it might have been somebody like Joe Lonsdale, but it was always one of these people.

(00:09:54):
And the interviews were pretty strange. With Stephen, it would be, you'd be chatting about philosophy for an hour and a half and it would very much just be like he would pick a topic out of thin air. It was impossible to prepare for, and then he would just go very, very deep and try and test the limits of your understanding. But it would really just be a fun conversation and then if you pass the vibe check, you'd be in. And so, there was that strong selection mechanism.

(00:10:20):
There was also the question of, I think it might have been Thiel who mentioned this, but he thinks that a lot of the best recruiters in the world or the companies that attract talent, they put out this distinctive bad signal and it has to turn some people off. That's the key of a good, bad signal. So, I think in the present day, OpenAI and Anthropic, they're both sucking up some of the best talent that you and I know. And I think one way they do do that, and they are sincere in this, but they do really attract people who are almost messianic about the potential of artificial super intelligence and who really believe this is the only thing that matters and it is going to be the biggest thing in the world.

(00:10:56):
I think Palantir's version of that was that they were quite focused on things like preserving the West. There was a slogan of Save the Shire, right? So, they were talking about military and defense and intelligence and the importance of that well before everybody else. And bear in mind, this was during the era when it was social, mobile, local apps. You had, social media was on the rise. You had, the hot companies were Facebook and Pinterest and things like that. And so, this was, at the time, a very strange thing.

(00:11:26):
And so, I think to be drawn to that, you had to look at the other options and say, "Well, this is fine, but what am I really doing in life?" Whereas you had this other place that was like, "Hey, come solve the hardest, messiest problems in the world with us." And I think just at that time, that really drew some really good people.

Lenny Rachitsky (00:11:43):
We're going to talk about the reasons people don't necessarily like Palantir and the moral question of what they do, but when people look at a company that is like... I guess OpenAI, to your point, is a good example where they're just so turned off by maybe their approach. What you're missing is that's potentially intentional because it actually draws in the people they really want.

(00:12:03):
It makes me think about, I was involved in creating the core values at Airbnb and something that we learned at going through that process is, when you define the values for your company, it's really important to clarify who this is not for, exactly as you described, which feels unnatural. Like, "Oh, we want to be inclusive, we don't want to make people feel like they don't belong." But the whole idea is to be clear on here's who will thrive here and here's who's aligned with our mission. And what I'm hearing is Palantir and these companies take it to the extreme.

Nabeel S. Qureshi (00:12:30):
A hundred percent, yeah. On my team at Palantir, one process that we followed, I could talk about this more if it's interesting, is when you started a new project, you basically had to organize what they called a murder board for it. I think this is originally an army type. So, the idea is, basically, you write up a two-page plan for the project. You invite three or four smart folks who don't know anything about the project and their job is just to tear apart your plan.

(00:12:56):
And so, you have to write, here's the vision for this, here are the goals, here are the tactics over the next three months. And one section was principles that you're following for this project. And I remember giving this advice a lot was just like when people joined, they would write principles such as move fast and I would always be, "Everyone likes to move fast." It is not a good principle actually because nobody can really disagree with this reasonably. You need something that actually a lot of people are going to go, "Why are you taking this principle? This seems wrong to me." So, you need something that people can disagree with.

Lenny Rachitsky (00:13:29):
I want to come back to the beginning of what you described of what they look for, what Palantir looks for in people. You talked about independent-minded, a lot of interests, broad interests, and competitive. First of all, I think a lot of people hearing that, especially the last part, be like, "I don't want to work there." Why does this work? Because this isn't naturally what you would think of as how you build the most amazing, productive team.

Nabeel S. Qureshi (00:13:52):
I think it just draws people who want to win. I think that's what was really important. The other piece of it, I think, is that there's actually, and this was much truer 10 years ago, is there was a lot of talent that was a little bit outside of the tech ecosystem but could easily have been very successful within it. So, people who got out of the military or one of the intelligence agencies and they were doing, let's say, an MBA somewhere to transition into the corporate world. And I think, typically, they would have taken a position at a classic Fortune 500 corporation. And actually, Palantir managed to get a bunch of that talent. And at the time, that was very undervalued.

(00:14:32):
The people who succeed the most in the Marines or the Special Forces or whatever it is, tend to be pretty smart people. They tend to have accomplished very difficult goals in very hostile environments. And it turns out that when you're starting a somewhat chaotic tech company, that's actually a very useful skill to have. Again, I think more companies are doing this now, so Scale AI and et cetera. But at the time, that was a very differentiated talent pool.

(00:14:57):
And so, I think having those values as opposed to maybe the values that were more in fashion then, so talking about how inclusive you are, or the sushi that you serve at lunch, or whatever it is, it just drew a very different crowd. And I think the game that was being played there was, one, it's mission alignment. You're doing a defense company, that's the kind of person you want to attract. But I think there's also, two, which is just what is the talent that maybe is a little bit undervalued now and how do you actually draw those people to you? And I think that game is always shifting.

Lenny Rachitsky (00:15:31):
This is definitely starting to explain why so many Palantir alumni go on to start companies and become leaders at other companies. These are leaders that you're hiring. So, it feels like a lot of it is just the talent you hire are people that are naturally leaders.

Nabeel S. Qureshi (00:15:45):
I think you're right, and we can get more into it, but I think there was also a very concrete set of ways where that place was a training ground for founders. I even think it turned a lot of people who might not have become founders into good founders because of the way it works. So, I think there was a selection effect there, but there is also some training effect too, but it's unique to the way the company works.

Lenny Rachitsky (00:16:08):
And is that along the lines of the forward deployed engineer stuff or is that something else?

Nabeel S. Qureshi (00:16:11):
It is that, yes.

Lenny Rachitsky (00:16:12):
Okay, cool. We're going to get to that. I love it. Okay, amazing. Before we do that, one last thing is something I've seen is that you guys at Palantir don't really have titles. Everyone's the same level and just generic titles for everyone. Talk about that. Why do you think that was important? Why was that useful?

Nabeel S. Qureshi (00:16:29):
I don't know this for sure, but I do know that Thiel writes about this in Zero to One and his take is just that as soon as we have these title, you have a thing that people are competing for and then you get these very unproductive conflicts. You get people optimizing to game the system. You get Goodhart's law everywhere. So, it's like you have a metric and then people basically manage to the metrics.

(00:16:50):
I don't want to pick on any one company, but if you take Google, for example, there's a lot of interesting posts by people who left Google and they cite this as a reason why they got a little bit disgruntled, is that there's a way to get promoted. Rather than, let's say, improving an existing product, what you do is you start a completely new product and that has your name attached to it. And then when it comes to promotion season, you could say, "Hey, I did this new thing." And then boom, you have a new Google product, but it's maybe confusing to the end user.

(00:17:15):
So, I think they wanted to avoid all these kinds of dynamics. And so, the way that they did that was they said, "Well, titles are not going to be this memetic totem that everybody competes for. Instead, everyone is just going to have the same slightly meaningless title, which is forward deployed engineer." And the only people who did have titles were the CEO and then there were six directors and that was it. And now, I think it's a little bit more nuanced. There are different teams. There are some people with titles, but honestly, it was almost like...

(00:17:45):
We used to joke about it. It's like people would leave the company and then you'd see them update their LinkedIn and they would be like, "Oh yeah, I was totally the SVP of XYZ." And it's like, "No, you weren't. You're just..." But then it's like I totally understand it too because when you leave the company, you have to make your experience legible to the next person. And so, guess what? Things like SVP actually do matter.

(00:18:08):
And so, yeah, I think they wanted to avoid this intel competition. There are downsides to doing this. So, maybe the competition isn't as explicit around a specific title, but instead, what it becomes about is there's a particular exact or something and you want to gain that favor. And so, it becomes more about who can get in the inner circle of this person or whatever. And there were those dynamics too.

(00:18:32):
I actually am a big fan of this philosophy though, the no titles one. I think what it did do is that it basically said if you are in, let's say you're in a role of you're leading a very important project, which could happen, what it said was... This is always fluid. So, you are in this role because you're very good and so, it's a meritocratic thing. But if you start performing well, it's actually very easy to shift that because there is no explicit " I am the GM of this project title." And so, you always had to earn your place in the company. You always had to earn the right to work on what you were working on, and I think that was a good side effect.

Lenny Rachitsky (00:19:12):
Let's start talking about forward deployed engineers. What is a forward deployed engineer?

Nabeel S. Qureshi (00:19:17):
So, the way this originated was, basically, you can think of it as there's two types of engineer at Palantir. So, there's one that works on the core products. So, they don't necessarily leave the building in Palo Alto or New York or the offices. They're very much working on the core products and they're a traditional software engineer.

(00:19:35):
Because of the way the company works where you had these very large engagements with these large entities, there was a different type of engineer which you sent into the field. So, what that meant was you would spend maybe Monday to Thursday and you would actually go into the building where the customer worked and you would work alongside them. You would literally get a desk there. And so, that engineer became known as a forward deployed engineer.

(00:19:55):
So, within the company, that function is known as business development or BD. And then PD is product development. So, it's where the product is made. And so, within BD, you had forward deployed engineers. There are actually two types. So, there is one that it's a more technical software engineer. So, you have to pass a software engineering interview and prove your chops there and you would typically have a CS degree, but there was actually a type of forward deployed engineer that didn't have that. So, you would still get a technical interview, but it would be less about, do you know the specifics of this C++ algorithm? And it would be more about just like can you reason about data? We didn't have that division originally, but it turns out that there's a lot of people who are technical adjacent, shall we say, who you really need in the room when you're working with these large organizations or these large companies, because translating what you're doing into language that would resonate with an executive or being able to navigate the social dynamics in a room, all these are very valuable skills. And so, the hiring criteria there were a little different. It was a bit more about, are you savvy as a human? But all of that was given the title of forward deployed engineer, and it's just an engineer who works with customers.

Lenny Rachitsky (00:21:10):
Okay, so just to make this crystal clear for people, a lot of people hear this idea of Palantir having forward deployed engineers. A few other companies have done this. It's pretty radical. So, as you described, you basically have a desk at a company. So, you worked with Airbus and we'll talk about that. So, let's just make it real. So, you have a desk and a computer and login access and all these things at Airbus. You go to their office four times a week. You're sitting there with their employees working side by side, building a product for them, versus what most people do where "they just talk to customers," where they do an interview once in a while, they do a Zoom, they share mocks, things like that. This is like that on steroids. Is that roughly the way to think about it?

Nabeel S. Qureshi (00:21:51):
It is, yeah. And so, we would really be there a lot of the time. And so, the side effect of that was, one, you learn to live and breathe the customer's problems and you learn to speak their language. And eventually, they saw you as one of them and so, you develop these really close bonds with the customers. So, at Airbus, I would be at the factory where the planes were produced, or I'd be sitting next to people diagnosing issues with aircraft or whatever it was. Similarly, later on, I worked with the NIH, which was part of the US government, and I actually had a badge there and I would work with civil servants and biologists and clinicians and people who were working there.

(00:22:31):
And so, it's this pretty radical thing as you suggest. I think the key thing there from a business point of view is the average deal that Palantir had was very large in the many, many millions of dollars, which means that you could pay for this as part of the thing that the customer got. And then it was priced according to the value that the customer got.

(00:22:51):
So, as a simple example, if you're Airbus and let's say that you have an issue with one of your planes and you need to fix it, and fixing that is worth a $100 million or something to you, that's how it would be priced. It would not be priced as, "Hey, you're buying data infrastructure and it's similar to Snowflake or Databricks or one of these other providers. It's much more anchored to, here is the outcome.

(00:23:15):
But then the job of the forward deployed engineer is not just to deploy software. It is not just to sell software. It is to actually solve the problem. And so, you would have to be there. You would have to meet the key stakeholders who are actually in charge of reporting to the CEO about the specific issue. You would have to become their friend. You would have to gain their trust. And you would have to, in some cases, create new software such that it could actually solve the novel problem that was in front of you.

(00:23:41):
So, I would have friends who worked with one of our energy company customers and they would have to learn the ins and outs of how oil wells work. And then out of that, it turns out that having streaming data is actually very valuable for this use case. And so, boom, suddenly, there's a product that can handle streaming data that becomes part of the core platform. But that would be the motion, is you learn about the problem. You figure out what software would best address it. You build that software. You use it to accomplish the goal. And then eventually, that gets folded into the broader product suite.

(00:24:13):
And so, you can start to see why this would be a good forge for founders. And this was actually part of my thesis going in and joining, was I said, "Well, say, I got five reps of this," which I got more than that. But say, you got five reps of doing this in five disparate contexts, you actually become very good at this cycle of, okay, go into the building, gain the trust of the person, meet the people that are going to become your users, talk to them about their problems, make sure you're building something that actually solves them, and it's just a boondoggle.

(00:24:43):
Get really fast feedback and iteration loops. So, every week, you would have a cadence where it's like Monday, you go in. You do your meetings. Monday night, you build something. Tuesday, you show it to somebody. Tuesday, you get the feedback. Tuesday night, you iterate on it. Wednesday, you show it to somebody. Wednesday night, you iterate on it. So, you get four of these, five of these cycles every single week.

Nabeel S. Qureshi (00:25:00):
It already got it. So you get four of these, five of these cycles every single week, and you're moving incredibly fast. So 6 weeks in, you've suddenly gotten to, wow, this is really valuable, and somebody's willing to pay you whatever, $20 million for it, and boom. I think this is why you get so many founders coming out of this same process.

Lenny Rachitsky (00:25:20):
It's becoming very clear why so many founders emerged out of Ballinger. Okay. So an important element of this as you described, is that the idea here is build this as a one- off solution to solve a real problem at say Airbus or some government organization. And then the idea as you create something out of that, that then Ballinger can sell to other companies. What's extra cool about that is they pay you to solve this problem for them and then that is funding this other product that Ballinger can now sell to everyone. What a cool business.

(00:25:51):
However, early days Ballinger, everyone thought it was just this services business or just consultants building software for companies like Airbus, there's no way they can make this a platform that works for a lot of people. Clearly, that's what's happening and it worked out. This is like the holy grail. Solve one customer's problem and then sell it to everyone else. Every SaaS business basically would love to do this. What do you think allowed them to actually achieve this and be good at this? What are some principles that worked?

Nabeel S. Qureshi (00:26:22):
Yeah. That's a great question and it's true. I think that from when I joined until maybe until IPO and a little bit after, I was told, "Hey, isn't this basically a sparkling extension? Isn't it a consulting business lopping as a product company?" And eventually it became undeniable. One, because I always laugh when people are like, "What does Palantir do?" It's like you can go onto YouTube and just search Palantir demo and you'll get plenty of demos of how the software looks. Not many people know about this, but you can go and sign up with a credit card right now and start using it.

Lenny Rachitsky (00:26:22):
I can have a Palantir account?

Nabeel S. Qureshi (00:26:22):
You actually can. Yeah.

Lenny Rachitsky (00:26:22):
I did not know that. That's cool.

Nabeel S. Qureshi (00:26:57):
Yeah. I think it's called AIP now. So it's not actually that mystical and there is a product, and if you look at the margins, they show that. So they have 80% plus margins, which is not really what you would get if you were actually a consulting company. It would be closer to 20 or 30%. So then your question was, well, how did they actually achieve this? I think there was just incredible talent in the product development organization, really top tier, incredible talent. And it took some really, really smart people to take the set of internal tools that we were using at the time to create value of customers and then go, what is the unified version of this? Would this look like if this were a product? And out of that process that I saw came Foundry assume there was a similar process with Gotham a while back. But basically it's like, the motion was that you would go in and early on you were basically armed with Jupyter Notebooks and some data integration stuff, but it was very primitive and you had to create value that way.

(00:28:03):
But we kept building tooling that was useful for forward deployed engineers. So we were our own first customers and at some point there was this concept of, "Wait, what if we take our internal tools and we let our customers use them?" And I remember at the time, this is a really radical idea. And then Shyam Sankar, I think he's the CTO, maybe he's the president now, he just mandated like, "Okay. Every customer deployment you have to have a customer using this within three months or whatever." So it was horrible at the time because these had been built for these nerdy Silicon Valley engineers, and so they weren't particularly usable. They would crash all the time. You'd have to debug spark errors or whatever it was. But basically that process brought a lot more rigor to our thinking about the product.

(00:28:52):
And out of that kind of, I would say three or four year process came the Foundry product. And then there was a lot of focus around things like performance and reliability and so on. That was all really painful. So yeah, I think the answer was just talent. And then there was this recognition that we do. We do know things that most people do not know about how data works in large organizations. That was the other thing. We discovered a lot of "secrets" in this process of living with customers for so long.

(00:29:25):
The basic one was just data integration is massively painful inside organizations. This is very hard to understand unless you've worked in a large organization, but it's actually impossible to even now to get access to a lot of your own internal data that you need to do your job. So you'll hear stories of people being like, "I'm trying to calculate our sales this quarter, and I had to wait six weeks for some other analytics team to get me this deliverable." So just knowing problems like that and being able to focus our product efforts around those problems, meant that we were able to build something generalizable there.

Lenny Rachitsky (00:30:00):
Okay. There's a lot here. First of all, you talk about Gotham and Foundry. I know that we'll link to videos of people checking these out, but just what's the simplest way to understand what these two products do?

Nabeel S. Qureshi (00:30:10):
So Gotham is optimized for military and defense use cases and intel as well. I would say they both have some things in common. So they both have, I would describe this almost as a pyramid where the bottom layer is data ingestion, the middle layer is data mapping, and then the top layer is anything that's user facing. So any UI component. And then if you think of Foundry for a second, there's different tools that allow you to ingest data to it. There's different tools that allow you to easily build data pipelines and clean up data, which everybody has to do. And then there's a bunch of tooling that allows you to build compelling UIs on top, do point and click analytics, do notebook style workflows, however technical you are. So that's, I mean, when it's a platform, it's a suite of things that has a common data backing but contains a bunch of different applications.So I think that is somewhat true of Gotham as well. But when you log in, you see this unified interface.

(00:31:08):
So what is the actual difference then? I would say with Gotham, you're looking much more at workflows like that involve maps, for example. So when you're doing a military operation, a lot of the time you are going to be looking at a map and you are going to be monitoring the movement of troops or tanks or whatever it is. Another big difference is the idea of graph-based analysis. So Gotham, one of the use cases was finding combing through networks of terrorists and basically finding the bad guys. So being able to do queries that are graph-based was important. So it's like, "Who is everybody that Lenny called in the last week?" Imagine all the nodes fanning out from there. And then it's like, "Okay. Well, this one looks interesting. Let's zoom in on that. What is this person's location?"

(00:31:56):
So it's this very graph-based way of thinking that also applies to things like fraud. So Gotham has been deployed against fraud, but if you look at Foundry, it doesn't actually emphasize that component so much because it turns out, let's say you're a B2B SaaS company, you're probably not doing that much graph-based analysis. You're doing things that look a lot more like classic SQL queries, tables, that kind of stuff. So Foundry is a lot more traditional in that way.

Lenny Rachitsky (00:32:20):
That was an amazing explanation. For the first time, I am starting to understand what these products do. Basically, it's just sucks in a bunch of data, cleans it up so you can actually trust it and then helps you interact with it in various use cases, maps, graphs, tables.

Nabeel S. Qureshi (00:32:36):
Yes.

Lenny Rachitsky (00:32:36):
Okay. Amazing. The example you gave of what you worked on at Airbus, you described it as basically a sauna for making planes. Is that right?

Nabeel S. Qureshi (00:32:44):
Yes.

Lenny Rachitsky (00:32:45):
So how much of that does becomes a part of this core product versus stays this one-off thing? Is it elements, that's a cool innovation, let's put that into Foundry. How does that work?

Nabeel S. Qureshi (00:32:55):
This was a really interesting story actually. So the initial problem that we came into with Airbus was that they had a new aircraft called the A350 beautiful aircraft. By the way, if you get to, I think if you fly New York to Singapore, it's often in that A350. Really nice. So it was a relatively new aircraft at the time, and their mandate to us was, "Okay. We need to ramp up production of this really fast," much faster than we've ever done it before. So it's like the numbers are very approximate, but it's like, "Okay. We're producing 4 this month, we need to do 8 the next month, 16 the month after, and so forth, and you are going to help us do it." So this goes back to what I was saying earlier is the mandate wasn't like, "Hey, we need to upgrade our data infrastructure. We thought you guys would be met the list of requirements." It was much more just like, "Please help us accomplish this mission. This is the big thing."

(00:33:42):
So we went in, scoped out the problem. There were a bunch of different things that we could build that helped accelerate this, but one of the basic problems that we figured out was that without getting too much into the weeds, the way the factory would work, is that there's a bunch of stations and you can think of the plane as literally moving between each station and then each station would do a certain set of work on it. So initially, it's literally a big fuselage and the fuselage is sitting there and then people are doing a bunch of work orders against it. They need parts in order to do that work. And then at some point they say, "Okay. This is ready to move to Station 31, and the plane is physically moved to the next station and then Station 31 does its next thing."

(00:34:23):
So in order for the next station to do its work properly, they need to know, one, what work was done at the previous station and what work is remaining? Two is just like, if you think about this problem, not all work is going to get done on time. So things carry over to the next team, and the next team then has to... So when I'm describing this problem to you can start to visualize, okay, maybe I need some Gantt chart to this, and I need the ability to click in and say, "Okay. What did Station 30 do and what work orders remained undone?" And then it's like, "Okay. For those work orders, what parts do I need and where in the factory might they be?" So this was very, very hard to do as it is. A lot of it was just relying on people going and having conversations with other people on the factory floor, and coming from tech where it's maybe not as complicated as building aircraft, that is a phenomenally complicated process, but it is easy to see, okay, you can actually improve this problem with software.

(00:35:20):
All that data was stored in SAP and SAP is like established software. It's good at what it does, but it's not the most user-friendly necessarily, especially if you're not an expert in how it stores data. The table names are very hard to understand and read. So one of the things we figured out was just if you can pull in these tables that may as well be written in completely alien language, the table name would just be like S3, F1_Z or something like that. And you'd have to know, okay, this is the table where the part ID is stored or something.

(00:35:51):
If you could pull in those tables and join them in the right ways, and then just map them to human concepts that humans can understand, so things like a part a work order, an aircraft, et cetera, and basically build a hierarchy or mapping between them, then what you can do is, a user can just log in and say, "Okay. Aircraft 79, where is that? Okay. It's at Station 31. All right. These are the work orders, et cetera." So you've translated it into a more human-legible thing.

(00:36:16):
So the thing we built, I slightly flippantly described it as Asana. It's a little different. But basically that's what it did, was it gave you a unified view of, okay, this is what's going on inside the factory. This is the work that needs to be done on this particular plane. And then me today going to my job at Station 31, what work orders do I need to fulfill and where are the parts that I need to do that? So did this directly become a part of Foundry? Not exactly, because the way that other companies work is not going to be using this same set of concepts, but the overall idea of taking a bunch of tables, and then mapping them to human understandable concepts was a very powerful one.

(00:36:58):
So this actually resulted in a big piece of Foundry now, which they call Ontology. You've probably heard this term as you've seen... If you see Palantir presentations, they always talk about Ontology. This is what they actually mean by that, is it is a set of concepts that is understandable to you as a human and you are not having to go and dig around and do. You're just able to say, "Where is the aircraft now and where is it going next?" So the ontology became a huge piece of Foundry. It was directly informed by the learnings that we had from building that application inside that factory. And I would say it's still a very big differentiator today. I don't think too many other companies ship this kind of stuff yet.

Lenny Rachitsky (00:37:41):
Wow. I love how excited you still are about this. I could see it being so fulfilling to solve this big problem. I saw a stat that I think, 4X their productivity. What was the number there?

Nabeel S. Qureshi (00:37:52):
Yeah. I don't recall the exact stat, but we did ramp up production, I think at least 4X that 1 year, which I mean obviously, they did this and we just helped with it. But that CEO said that we played a critical part.

Lenny Rachitsky (00:38:05):
Also, you moved to France, I think for this. That was how forward deployed you were. You lived in France for how long?

Nabeel S. Qureshi (00:38:09):
Yeah. I lived in France for about a year and a half. The way they built their planes is they manufacture different components around Europe. So they build the tail in Spain and the fuselage in part of the UK and Germany and so forth. So they basically ship everything to France to be assembled at the end, which you can imagine this is a very messy process. So I was mostly in France, but there would be weeks where I'd have to fly between all these countries just to figure out where things were.

Lenny Rachitsky (00:38:39):
In your post you wrote about how just the life of forward deployed engineers is pretty crazy. You just get a call sometimes like, "Hey, you're flying to this random country tomorrow. Get ready." Is that just life as a forward deployed engineer?

Nabeel S. Qureshi (00:38:50):
It is. Yeah. The company had a very, I would say, aggressive attitude towards travel in the sense of when you join, you were basically told, "Look, you have to be okay with travel. Are you okay with that?" And the attitude, which again I think is a very founder friendly one is you need to be willing to just jump on a plane that night if that's the best thing to do for this customer and if it's going to get us to where it needs to be to win. So there were many times when it would be like, "I need to take this cross continental flight tomorrow for this particular thing because it will be useful."

(00:39:26):
So I think that's one of the takeaways for me was just being in person is so valuable when you are working with some external party, just going there for a few days and spending time with them, maybe going out for dinner. You build so much more trust than if you're trying to close a customer over Zoom or do an engagement over Zoom. It's just the vibe is completely different. So yeah, getting on a plane was a really cool part of our job for a very long time. This obviously changed around 2020 because COVID happened, the company IPO, and so there needed to be a bit more internal controls around this. But I would say pre-2020, this was a very big part of the culture.

Lenny Rachitsky (00:40:03):
I'm excited to have Andrew Luo joining us today. Andrew is CEO of OneSchema, one of our longtime podcast sponsors. Welcome, Andrew.

Andrew Luo (00:40:11):
Thanks for having me, Lenny. Great to be here.

Lenny Rachitsky (00:40:13):
So what is new with OneSchema? I know that you work with some of my favorite companies like Ramp and Vanta and Watershed. I heard you guys launched a new data intake product that automates the hours of manual work that teams spent importing and mapping and integrating CSV and Excel files?

Andrew Luo (00:40:28):
Yes. So we just launched the 2.0 of OneSchema FileFeeds. We have rebuilt it from the ground up with AI. We saw so many customers coming to us with teams of data engineers that struggled with the manual work required to clean messy spreadsheets. FileFeeds 2.0 allows non-technical teams to automate the process of transforming CSV and Excel files with just a simple prompt. We support all of the trickiest file integrations, SFTP, S3, and even email.

Lenny Rachitsky (00:40:55):
I can tell you that if my team had to build integrations like this, how nice would it be to take this off our roadmap and instead use something like OneSchema?

Andrew Luo (00:41:03):
Absolutely, Lenny. We've heard so many horror stories of outages from even just a single bad record in transactions, employee files, purchase orders, you name it. Debugging these issues is often finding a needle in a haystack. OneSchema stops any bad data from entering your system and automatically validates your files, generating error reports with the exact issues in all bad files.

Lenny Rachitsky (00:41:24):
I know that importing incorrect data can cause all kinds of pain for your customers and quickly lose their trust. Andrew, thank you so much for joining me. If you want to learn more, head on over to oneschema.co. That's oneschema.co.

(00:41:37):
There's a lot of founders listening to this and a question that I'm thinking and they're probably thinking, and there's two questions here. One is how hardcore to go potentially with their own forward deployed operation. And then two is just how and a company I know is actually doing this, how far to go with one company's problem and invest in just like we are going to nail solving this one customer's problem with the hope that this is something we can abstract and sell as a big platform. So let me start there. And you're building a company, any I guess insights or advice on just how far to go down this road of we'll solve customer one's problem and we bet that this is going to be a big opportunity for a lot of other companies?

Nabeel S. Qureshi (00:42:20):
So I would say on the forward deployed piece, my friend Barry McCardel, the CEO of Hex, the analytics company, he wrote a really good post about this actually, and his take was just like, "You probably don't need forward deployed engineers." It's very specific. But I think basically the thing there is you have to be willing to be quite almost wasteful. You have to be willing to invest a lot in finding the thing. And for that you just need a certain ticket size. So you need each customer's revenue to be probably in the billions of dollars. If it's below that, you're probably not looking at a traditional forward deployed engineer motion. It's something a little bit different.

(00:42:59):
So I think one thesis that a lot of people left Palantir with and started companies around was there's a lot of customers that Palantir won't serve because maybe they're too small a ticket size. So actually you could go and do something like Palantir for those companies, but instead of charging them $5 million, you're charging them 250K. So in a scenario like that, you might still have forward deployed engineers, but they're not going to France and spending five days a week in a factory. It's more like you'll have one person and they're looking after five different customer accounts. It's more of that ratio in order to make the numbers work. So I think a lot of the principles can be abstracted from that experience, but it is a really specific sales motion that depends on a specific way of doing business.

(00:43:49):
I think to your other question, yeah, I think it's obviously something that is very hard to give a general answer to. My main thing here is just that you can definitely tell when you are just doing consulting and when you are closer to building a product. And I think the error that people make more often than not is they are actually too stuck on their own product vision. That's the mistake I've seen a little bit more actually than the other way around. If you go to an enterprise customer, and let's say you think you're doing analytics software and it turns out they don't actually care about internal analytics this much, they actually have this other massive burning problem and they don't have a good solution to it yet. I think a lot of people are unwilling to go and pivot to the big problem because they're like, "Well, we're analytics software and so maybe this customer is a fit for our thing," and maybe that's the right call. In some scenarios, that is the right call. You should go find a different customer where your thing resonates more.

(00:44:48):
In other scenarios, it's actually the right call to pivot and just put everything on that big problem instead and then go and find other customers for that thing. There's no hard and fast rule. I remember reading a really interesting post by, I think it was David Hsu from Retool who had this exact thing. I think he worked at Palantir for a while too. He said that they had the Retool product and it wasn't getting any traction at all. And then he tried an outbound email campaign where he literally just changed the subject line to build internal tools easily. And then suddenly they started getting all these replies from CTOs who were just like, "Yeah. This is actually a huge pain point for me."

(00:45:28):
But the exact same solution, they were previously framing it as, I think it was supercharged Excel or something like that, and nobody was biting. So they just changed the way they framed it and found a different set of buyers and succeeded that way. So yeah, no hard and fast rule, but I think it's always you need to have this matrix of options in your mind and be very deliberate about which one you are going with and why.

Lenny Rachitsky (00:45:53):
I think your piece of advice is really important there. Usually in your experience, you're saying people index too far too? Like now, what they're asking me to do is not what I think they need or what customers will need. You're saying it's actually more likely they're right, and that's maybe where you should be focusing more versus this abstract vision and original idea you had?

Nabeel S. Qureshi (00:46:14):
I think so, yeah. I think it's very hard to not be anchored to your own experience and your conceptions as a problem. And one thing I've seen in really strong founders is they're able to drop a bunch of those assumptions and almost treat a new opportunity as a completely blank slate. And then just figure out how to reshape things so that you're taking advantage of that, and that's how you don't get stuck at a local maximum.

Lenny Rachitsky (00:46:37):
Your other piece of advice is also really great. So people hear this and they're like, "We don't afford an engineer to sit at one customer prospects office and build stuff for them." But your point is you can have one for five different customers. They're not there full time. They bounce around, but they're... It's almost like sales engineering, just like what you call it sparkling sales where they help make it successful. I know Looker is a famous example. They think they called them forward deployed engineers. Do you know any other companies by the way, that some version of forward deployed engineers?

Nabeel S. Qureshi (00:47:07):
There's a lot. I mean, I know that the AR-Labs are hiring forward deployed engineers now, they're building forward deployed engineering teams and they could make it work, but I think there's going to be key differences. I don't see Anthropic going into an enterprise customer and building some entirely from scratch solution for them. It's going to be something that leverages the Anthropic set of products. So there's a lot of companies that have this label now, but I think what's really confusing about, it's just that it means a few different things. There's another post by Ted Mabrey who's I think the head of commercial at Palantir, and that's a very good one too, to point with those too.

Lenny Rachitsky (00:47:46):
So say someone was, "I want to try this sort of thing in my company," what would be a few bullet points if things they should get right? You're describing the spectrum of what people describe as forward deployed engineers, if they were to try to do this, what do you think they need to most do correctly for it to be successful?

Nabeel S. Qureshi (00:48:04):
The key things that made our model work well, one, they were actually real engineers who could build product themselves. That's a very big difference. I think a lot of the time companies will say, "This person's a forward deployed engineer," but actually they're mostly there to be more of a solutions architect, or they're not necessarily building anything to know, but they're just listening and trying to find a way of deploying the existing product. They're not empowered to do new product. So the really radical thing Palantir said was, "No. Go in and if you need a completely new product to do this, you can go ahead and build it." And I think that's really the key difference.

(00:48:44):
The other stuff I've already mentioned, the value of being in person, and I think building close personal bonds with your customers. I do think the better founders do this anyway. They're on texting terms with their buyers, they become friends with them outside of work, and they see them as humans who they're trying to help. I think this is very motivating, gaining a really deep understanding of the business that your customers are in and knowing how those dynamics work. So a simple example might be, say hospitals in America. It's very counterintuitive to think of a hospital as a business. People think of it as it's a place where you get healthcare, but actually if you view it the way a COO or CMO views it, it's going to look very, very different too.

(00:49:34):
As a very simple example, sorry, this is a little bit dark, but how restaurants want to turn over tables as fast as possible in order to maximize for the day? Hospitals actually want to do the same with patients. They would like to treat you and then get you out of a bed so they can free up the bed to get a new person in there. So that's not super intuitive, unless you think hard about how the revenue for that hospital works. But then once you think about it, you're like, "This has a bunch of problems associated with it." And you start to go into really interesting...

Nabeel S. Qureshi (00:50:00):
... problems associated with it, and you start to go in really interesting directions.

Lenny Rachitsky (00:50:05):
There's just like the words and memes, and take you a long way working and understanding it.

Nabeel S. Qureshi (00:50:05):
Yes.

Lenny Rachitsky (00:50:10):
Okay, so essentially the things you want to get right, make sure it's in person, make sure the person is technical, make sure they have a deep understanding of the business and the problems they're having. The technical piece is interesting with AI tools these days, making everyone technical in some sense. You could argue this is going to become more common, people can just open up Cursor, Windsurf and just start adding features.

Nabeel S. Qureshi (00:50:30):
I think this is a really interesting thesis you've just hit on, and I expect to see a lot more startups that take advantage of that insight.

Lenny Rachitsky (00:50:38):
Basically it makes forward deploying engineers cheaper.

Nabeel S. Qureshi (00:50:40):
Exactly.

Lenny Rachitsky (00:50:42):
What is the current state of forward deploying engineers at Palantir? How much has it changed over the past few years? If you join now, is this still something you can do?

Nabeel S. Qureshi (00:50:49):
Yeah, of course. I should obviously emphasize that one, I left the company in 2023, and so this is just my personal view, I don't speak for them. I think that if you think about it, one of the metrics that the company had to measure its own success was essentially revenue per engineer, and so the more "product leverage" you had, the higher that number was. So if you had to throw a lot of people at every marginal problem, then you weren't doing so well at that because you're basically building a new thing every single time, and you are in effect a consulting business. If on the other hand, every time you encounter a new customer, the product turns out to be relevant to them, then great, and so this product leverage metric was actually a very unique thing and kind of a North Star for the company for the whole time I was there.

(00:51:37):
If you reason that out, what that means is that in the early stage of the company, you will have a customer and then you might have five to 10 engineers working at that customer. And so over time you want that ratio to change. So you want it to be each customer, because the product is so powerful, maybe AI coding's gotten a lot better, each customer you only need two people, and then maybe you actually get to a point where you can have one person looking after multiple customers. And I think that's how the job has changed, is now it's a little bit more about you have multiple customers, maybe you're spending less deep time with each individual one of them, but it's a lot clearer what problem you're solving across multiple customers and you have more of a kind of defined offering.

(00:52:21):
And so I do think that has been a bit of a change, but the company remains a very interesting and dynamic place to be. In some sense the story's only starting, because one lens through which you can view this company is they spent 20 years basically building the mother of all data foundations for every important institution in the world, and I guess what's very valuable now that AI models are out is proprietary data that isn't public. Suddenly you have access to that and you are in a very privileged position to help your customers deploy AI in a way that makes them successful, and that solves real business problems. That is essentially the bull thesis for this company and why it's probably going to 100X again. And so it's still a really interesting time to join but I do think the nature of the ratio of people to a customer, for example, is one big difference now.

Lenny Rachitsky (00:53:16):
Not investment advice, but it might 100X. I totally understand why that might happen. So let's talk about the data piece, you said that this was one of the secrets of Palantir's success, this early insight into the power of ingesting data, cleaning data, being able to analyze and work with it. What a marketing share there, just what they figured out about why this is so valuable, why it's so hard and how they achieved it?

Nabeel S. Qureshi (00:53:40):
I think it's just very obvious as soon as you step into a corporation and spend a couple of days there really, is you're like, all right, let's suppose your job is to increase sales, so the first thing you want to do is get a clear picture of what's going on. All right, so let me go and query the sales database. Oh wait, where's the sales database? I can't get access to this. Okay, I need to file an access ticket. All right, now I have to wait one week. And so everywhere we went, this was the big pain point, was we have to wait six to eight weeks just to get data access, and then when you do get data access, it's not like the data's in an easily queryable format, you actually really have to know what you're doing in order to get the right metrics out, and so on and so forth.

(00:54:21):
And so it turned out like, okay, it's this iceberg analogy where the actual analysis is actually just the tip of the iceberg, it's kind of the last five or 10%, and the 95% before that is, I am gaining access to the data, I am cleaning the data, I'm joining the data, I'm normalizing it, putting it all in the same format. And so once we spotted that, then it's like, okay, there's actually a lot of product to be built there just to make that process easier. People don't think of Palantir as this place where innovative new product and UX ideas come out, but I actually think it's been one of the most generative companies for that specifically in the last 20 years, it's just that most of that didn't see the light of day and so people don't know. But if you look at the product primitives that they developed in order to make the things I just mentioned a lot easier, they're actually really valuable and interesting and could probably form the basis of independent companies themselves.

(00:55:21):
And so, yeah, it just took every single step of that process became much, much easier once there was a software solution around it. So if you talk about data ingestion, there's essentially a universal data adapter that's part of Foundry. It can read anything, so JDBC, S3 buckets, whatever you want. It allows us to look into the data, maybe preview the first 20 rows, and then it allows you when you're ready to set up a schedule and just pull it in on some cadence. That process alone for an engineer used to take a long time, especially pre-Vibe coding, and managing all those cron jobs and doing this analytics, VM somewhere inside the customer's tenant was a huge pain.

(00:56:04):
And so you productize that piece, then it's like, okay, once you have the data, it's like how do you actually join it? What if you're non-technical? Is there a way for a non-technical user to be able to join tables and see what the result is? And so there's all these very fascinating business problems that, because I think the access was very difficult to get, and people hadn't really solved before, and so there was a lot of white space to do some product innovation. So now I would say Foundry's definitely the best data platform in the world just because it has all these different applications within it that solve these discrete parts. And it came out of this, years of painful experience, watching people have to clean data and join it and figure out what this table name meant and so on and so forth.

Lenny Rachitsky (00:56:50):
You shared in your post this kind of evocative story of some people's jobs is just to gate keep the data. They're there to give you access to this very valuable data within the organization, and how hard it is to get. That was a lot of this work, is just breaking through those political battles of like, "Okay, we need this data for the good of the company and took a lot of work." I guess anything there you want to add?

Nabeel S. Qureshi (00:57:12):
It is, yeah. It's a huge pain, and there are good reasons for it. It's not like folks are malicious here. If you're IT or if you're an InfoSec type person, then your goal is to prevent data breaches and to make sure that sensitive information doesn't spread too wide. And so what's the easiest way to do that? It's to lock the data down, basically be a gatekeeper for access. I think where it got a little bit more interesting was where your skills are valuable and depend on you being the gatekeeper. So what I mean by that is let's say I'm the only guy who understands the way the sales calculation pipeline works and I write the SQL for it. All the requests from business SMEs come to me, I have a big queue of them, it takes me weeks to get through this queue. I have a great job, I have great job security, and people depend on me.

(00:58:05):
And so now along comes this company and they're like, "Hey, actually we want to make sales data available to everyone and we want to make it point and click." Suddenly you're like, "Hey, hang on, what am I going to do?" And so that's where I think there was a lot of difficulty and I always say people are like, what accounts as competitors? I don't think it's the ones that you would think of necessarily. Palantir's biggest competitor is a company rolling its own solution, and so the biggest difference would just be a CIO saying, "I'm going to build my own data infrastructure, I'm going to own it, it's going to be on top of one of the hyperscalers, and we're all just going to do our own analytics ourselves." And what we came along with, which was quite disruptive to this model, was saying, "No, actually all your data is going to get ingested into this one platform and everybody in your company is going to use it." The trade-off is it's going to be really, really easy for everyone to do things. But as you can imagine, some people weren't a huge fan of that model.

Lenny Rachitsky (00:59:01):
It feels like Glean is the biggest competitor to Palantir after I hear this, do you know about that company?

Nabeel S. Qureshi (00:59:06):
I do, yeah, Glean looks amazing from the outside. So many differences there, I can totally see why you would say this, but-

Lenny Rachitsky (00:59:15):
Clearly a different use case but it feels like the reason they've been successful is they figured out a lot of this data ingestion, permissions, search stuff. I never thought of it that way.

Nabeel S. Qureshi (00:59:24):
Yeah.

Lenny Rachitsky (00:59:24):
Interesting. Okay, I want to talk about hiring, you talked a bit about this. You're starting a company again, what are some of the key lessons you've learned from your time at Palantir when you are hiring people for your company? I don't know if you're actually hiring people yet, maybe when you may start hiring.

Nabeel S. Qureshi (00:59:42):
Yeah, we have six people at the moment, so a really reasonably small team. I think with hiring, it's funny, man, there's so much hiring advice online and you read it and you're like, "Yeah, this is super obvious." And then when you live it, you're suddenly like, "Aah, this is why people say this." So a few simple examples are I think the thing that is really hard to find is somebody who really, really has a lot about doing the thing and will go that kind of extra 20%. I think when you hire out, especially not to pick on them, but I think if you hired a [inaudible 01:00:17] right, it's like people want a 400K a year job, they would like to work a certain number of hours, they would like to ship some code and then go home, that's basically the model that you get accustomed to even if you don't intend to when you work at a big company.

(01:00:31):
And so if you hire out of that for a really small startup, it can be really challenging because a lot of your success as a startup depends on each individual person being like, "No, I'm really going to, I'm work this evening if that's what it takes to get this thing working, and I'm not just going to check my boxes, I'm actually going to look towards what is the real outcome that this business is trying to achieve." And everything I'm saying feels kind of obvious, but when you actually feel that difference between somebody who's just checking the boxes and somebody who's kind of an animal in this way, they'll actually go and pursue and accomplish the end outcome, that difference is very, very big and it matters so much for your first 20 people. And there's no science to finding these people. It's not like you can just put somebody who cares about outcomes in your JD and then suddenly you'll get all these people applying.

(01:01:18):
So then it's like, okay, well how do you screen for that and how do you find those types of people? And so that's where it gets really interesting. I think that's where the mission alignment comes in, and so you do have to find people who, for what you are doing, have this extra maybe private reason to care about it a little bit more than the average person. So I think for Palantir, they did hire a lot of vets, for example, or maybe people who were a little bit more patriotic or pro-America than the average tech employee, and those people had an extra reason to Palantir and an extra reason to try that little bit harder. And so what I'm doing is a little bit more in the kind of medical and health space, and so I think people who have themselves had experiences with this system have maybe had relatives go through difficult experiences with things like cancer or whatever it is. They're just that extra bit motivated to really care about the thing you're trying to do and then work that little bit harder, and so I think aggressively filtering early on to things like mission fit, how much have you cared about stuff in the past, and what's an example.

(01:02:29):
You ask questions like, what's the hardest you've ever worked to get something done and why? And that does differentiate a lot of people, a lot of people don't actually have a great answer to that. So I would say that's been a really big learning, is it's less about testing for the right skills, yes, that's important, two it's much more about just who has that extra 20%.

Lenny Rachitsky (01:02:47):
That is really interesting, everything you've shared is essentially around motivation, and drive, and passion, and kind of just commitment to working on this intently, and it's almost like a second thought of just like, oh, also they're really smart and skilled at stuff. It feels like that's just table stakes and this is actually what makes the difference in your experience.

Nabeel S. Qureshi (01:03:08):
Yeah, I totally agree, and I think it's different for every business. So I think if you're in a space like B2B SaaS where maybe it's a little harder to tell the story of like, oh, this is so mission-critical, whatever, there are other ways of getting at this thing. So for example, I know a lot of people, again, it's a little played out now, but I know a lot of people who for sales teams, they will explicitly go for people who were professional athletes or played sports in college, and it's like, okay, what does that test for? It's like you are very, very disciplined, you're very, very goals and numbers oriented and you're willing to just work really, really hard. And so there's all these kind of lateral ways of getting at these qualities that I think you just have to be intentional about as a founder. As a personal example, I'm a runner and so I actually love meeting fellow runners and I kind of joke like, "Oh, maybe I'll go higher from run clubs or something like that."

(01:03:57):
But it's just same with I play a lot of chess, I love meeting chess players. I'm not necessarily saying that's the right kind of hire for me, but I think having this thing of here are some traits that seem uncorrelated, but which actually give you good signal to this person's personality, those are actually really important. The last thing I'll say just as a funny illustration of that concept is I think Max Levchin tells the story of somebody interviewing at PayPal early on and he passed all the skill interviews and then it just got to the final round and he said something about liking to shoot hoops, like he liked to play basketball, and they were like instant reject. The vibe here was like if you're not a mega Linux nerd, hardcore computer person, then we don't want you here, even if you actually passed all the tests just because you like to shoot hoops. Now whether that was the right call or the wrong call, don't know, but that's an example of what I'm talking about.

Lenny Rachitsky (01:04:54):
I think that's a great echo back. People hearing this may be like, "What the hell? How dare they do that?" But this is exactly what you said at the beginning of our conversation, that like an approach to building a generational business is to be very clear about who this is not for, and that's okay, it's your company, not everyone needs to work there. And it's almost saving them time because they might realize this isn't for me, this isn't the people I want to be around necessarily. So I think it's important to see that side of it, is it's your business, it's important to be clear about who is a good fit for the company and who's not. Speaking of that, let's talk about product management for a bit. I know Palantir PMs are not traditional product managers. I imagine people have the title, Product Manager at Palantir, okay, so if so, as far as you understand what's the difference between say a PM at Palantir versus a traditional PM say at a FANG company?

Nabeel S. Qureshi (01:05:51):
Palantir was, as far as I remember, quite anti-PM for a while and eventually we did need them because we just got more serious about product testing.

Lenny Rachitsky (01:05:57):
Classic story, classic story.

Nabeel S. Qureshi (01:05:59):
A classic story.

Lenny Rachitsky (01:06:00):
In many companies,

Nabeel S. Qureshi (01:06:01):
The big difference or one big difference I noticed was that they were extremely careful about only making people PMs who had first proven themselves out as forward deploying engineers. You basically could not become a PM any other way. So as an example, when I mentioned earlier the thing that we built for the plane factory, the person who was managing that deployment, she later became the PM for ontology, and it was just because she'd kind of proven her method in the field. And the reason for that's pretty simple, it's going to be someone who understand how customers work and has that customer empathy, and it's going to be someone who has this drive to get things done because that's what BD selected for. I think the failure mode that they were very, very averse to in traditional PMs was this kind of Google Docs syndrome of like, okay, I'm going to write my product requirement documents, and I'm going to manage it in this very sort of sane, rational way I think, so the company was really rigorous about that.

(01:07:04):
And so basically PMs were almost always internal promotions and they always came from BD. I am not aware of a single case where we took somebody who was a PM at a place like Google, which produces many excellent PMs and hired them successfully into Palantir, it's just a very different vibe. So I think that was one thing. This is maybe more of a classic PM trait, but you just had to be either an engineer yourself or extremely good at working with engineers, and the ones I saw who succeeded the most were just best friends with their engineering team. And the team would always just be like one, it was called the group pm and then it would be a lot of very, very good engineers. And basically the success or failure mode was just do the engineers and trust you? I mentioned before Palantir how is very almost disagreeable personalities, and so if you didn't gain the trust of engineering team pretty fast, you didn't last very long.

Lenny Rachitsky (01:07:58):
I think we've cracked the question of why are Palantir PM's so successful? First of all, the hiring bar is just basically hiring for leaders in a lot of different ways, to this, I don't know, forge for founders where they're working with a company solving a real problem, building a real product that makes money, and then those are the people that become the PMs at Palantir and then they go on to leave and that's why 30% of them end up starting companies, I'm surprised it's not higher, or become first PMs at other companies or heads of product.

Nabeel S. Qureshi (01:08:29):
Yeah, absolutely, it's crazy. I was part of a pretty small team within Palantir, I think it was 20 to 25 people when I joined, and I think at least six of them now are either unicorn or just pre-unicorn founders from that group of 25 people, which is actually a crazy ratio. And then a bunch more have become founders recently at an earlier stage, so yeah, there's all these little pockets of excellence and it's been really interesting to see. I think the other thing that's driving that a little bit is when you leave, it's just such an interesting company to work at that I think the retention numbers were actually very high for that company. People would often stay a lot longer than maybe the average Valley tenure. And so when you left, it was really this decision of just something very specific is pulling you and you want to kind of play the next level of the game, and so it was very unusual for someone to leave and then join maybe a more traditional tech company. It's sort of like you're either going to go become a founder or why would you leave when there's so many interesting different things to work on? And I know that sounds a little culty, but that's what everyone thinks.

Lenny Rachitsky (01:09:35):
I could totally see that. A lot of people that left Airbnb have never found something more meaningful, it's just hard, especially if you're early. There's a stat that I didn't share that I think is really interesting, and when you look at YC founders and where they've come from, I think you maybe shared in your post that there's more YC ex-Palantir founders than there are ex-Google founders in spite of Google being something like 50 times bigger sample size.

Nabeel S. Qureshi (01:10:00):
Yeah, yeah.

Lenny Rachitsky (01:10:02):
Let's talk about the moral question of Palantir. A lot of people probably seeing the title of this episode, hearing this, will not be excited about Palantir being highlighted and promoted, a lot of people kind of disagree with what Palantir's doing. Builds products that kill people in some ways, they work with governments they don't agree with. I know you wrote a really insightful way of how you approach this question when you decided to work at Palantir and how you see people tackle with this, can you just talk about the framework that you landed on and how you thought about this yourself?

Nabeel S. Qureshi (01:10:34):
Yeah, it's a really interesting topic, it's definitely very nuanced. I think what I was trying to say in that post was a couple of things. One was that there was a lot of upside there. So I worked on the US Covid response, I have friends who worked on Operation Warp Speed, and these are all things that I think saved a lot of lives, and I was pretty focused while I was working at NIH on cancer research. And so to me, these were just obviously good things and you couldn't do them anywhere else, and so that was alone a reason to stay. The question I had in that post was, well, okay, there are definitely going to be other pieces of this that people object to. So during the 2016 to 2020 era, it became a pretty common thing to go into work in New York and you'd have people protesting outside your office or doing all kinds of things. And so there was this question of, well, is this okay? And I think the point I was trying to make was it's rare that disengagement is the correct answer, and I think it's more recognized now, but especially then it went a bit too far.

(01:11:41):
So the famous example here is Google kind of disengaging with a Pentagon AI project just because some people felt that working with the Pentagon was itself morally bad. I think that's a way to sort of the left of what the median American would say, I think the median American would say it's fine to work on defense stuff within reason and assuming you're doing largely good things, and so there was just this kind of almost arbitrage there at some point of just hang on, it's not like working on defense is inherently evil, it's actually a pretty interesting thing. And then there's this question of, well, would you rather be in the room and making this better or not? And so I'm struggling with how much I can share here, but as a simple example, if you're doing even a workflow, which I think many people would not be super comfortable with, let's say you're targeting somebody for some kind of strike. If you compare the way it's done now to maybe the way it was done in 2010, it's going to be a lot more targeted, it's going to be a lot more accurate, and so you've actually improved that process and reduced the chance of error. Maybe you should feel good about that, right? Now, that is a bullet many people are not willing to bite.

(01:12:52):
I didn't work on the defense side of the company myself, but I think you have to be okay with these kinds of grade zones and actually actively thinking about what you are doing. And that doesn't mean that it's always the right thing to do to work in a defense company. Maybe we go into a very dark future and we start being the bad guys in some ways, and then it's probably not a great idea to work at a defense company. So it's a shifting landscape but I kind of felt pretty strongly that a lot of people in tech just didn't want to think about this at all.

(01:13:29):
So you have engineers now who are working on optimizing short form videos for higher engagement, and you sort of want to say to them like, "Hey, are you thinking about what this is doing to the brains of young children?" Or "Have you seen an 11-year-old kind of scrolling something for five hours and do you think this is a good thing?" And I think people don't want to think about this stuff too much. I'm not saying I know the answer, but there was almost this refusal to look at what tech was doing from a political lens for a very long time. It was just like, "Hey, let us play with our toys, let us sit in our little park, and don't bother us, and we're just going to build cool stuff and launch it."

(01:14:08):
And 2025, we're in a very, very different state of the world, tech is involved in politics now, and politics basically came to tech. There's this famous image of Mark Zuckerberg, he's sitting in Congress and he kind of looks very pale, and he's like, "Why have they dragged me in here again?" But I think tech went through this journey of, oh, we're suddenly becoming important now, oh, we're really, really important now, oh, we better stop playing this game of politics. And so I think what I'm saying now is a lot more consensus than it was 10 years ago, but at the time, the feeling was just like, "Look what we are doing is political, so you better engage with that."

Lenny Rachitsky (01:14:44):
I think when this became really real for a lot of people is with the Ukraine War, the government's running out of certain vehicles and ammunition, we're just not able to produce it, and then we're like, "Oh, thank God for a company like Anduril and all these other tech companies that are actually ahead and keeping us ahead." I think the only reason the US is ahead of that...

Lenny Rachitsky (01:15:00):
And keeping us ahead. I think the only reason the US is ahead of China and the space race is because SpaceX just is one company that just has been doing this for a long time. So I think a lot of people have kind of realized, okay, maybe we need these things.

Nabeel S. Qureshi (01:15:13):
Right. And I would make this argument as well, it's like people are like, well, how can you feel good about working in defense? And it's like, well, you're not going to feel great if China invades Taiwan, actually, you're not going to. I think you are probably also not going to like that outcome. So we do just live in this world where you do need to build up deterrents to these things and they better be good. So to me, it didn't feel that difficult of a question. I think when you zoom into particular things, they can be very difficult questions and there have been a bunch of those in the last couple of years. But yeah, again, disengagement isn't the answer.

Lenny Rachitsky (01:15:46):
Yeah. And again, it's not for everyone. I think that's an important kind of theme through this conversation is some companies ... like, to build ... sometimes to build a generational, really successful company, you need to turn some people off because that's what brings in the best talent oftentimes.

(01:16:03):
Okay. Just a few more questions. Kind of like stepping back a little bit. You're building a company again. What are a few core pieces of advice that you're bringing to your new startup that will inform how you build this company, from your experience at Palantir? We talked about a lot of stuff. Is there anything, I don't know if there are three things that you think are like, "I'm definitely going to do these things this way because it worked really well at Palantir."

Nabeel S. Qureshi (01:16:27):
One thing is probably just really fast iteration cycles. So placing a lot of bets and then being really rigorous about just going through that cycle very soon. I have this [inaudible 01:16:40]principles, and one of the things on there is basically saying EOP successes goes up the more bets you make, and it's sort of a function of how many bets you make and the probability of success of those individual bets, right? And so one easy way to almost guarantee that you'll hit something is just to make a lot of bets and then just kind of cycle through them very quickly. Now, obviously this is difficult, often this question of, well, is this bet actually failing or are we quitting too soon, kind of thing. But that's kind of one principle I take, is just test this thing very early. You know, like the classic "why feed, why see" thing is just when you take something to a customer, ask them to pay you a lot of money and [inaudible 01:17:22] then find a new problem. Don't wait three weeks, which is what every founding team typically does because you don't have that kind of time.

(01:17:29):
I do think the importance of just having a really tight, distinctive internal culture and building a strong feeling of trust within a team is really important. And kind of like you mentioned with Airbnb, and people definitely felt this at Palantir, there was this feeling of like, well, you worked here, you must be good. I trust you, and all of that. And I think it's so important to create that and you kind of know that feeling. That's what ... like, people ask me, should I go work at place X or should I just go be a founder straightaway? I don't know the answer for everyone, but I will say one of the benefits of working at a place like that is you just have all these internal benchmarks now for, okay, this is what this should feel like, and if it doesn't feel like that, we're off. And I can't imagine not having those benchmarks and just kind of having to figure it all out.

(01:18:21):
So yeah, I think that thing, too, is just distinctive, internal, strong team culture. And then I think for me, think three is just working with a really messy part of the real world. So I kind of joked when I left, like, I am excited to just do pure software. I'm excited to, I don't know, I want to build an ID or something and just not have a support email even and all of that. But it turned out, look, my comparative advantage in a lot of ways was the networks I'd built and the experience I'd had in engaging with the messy parts of the world. And they do need technology a lot, right?

(01:19:00):
There's this horrifying thought I have sometimes of just like, maybe we'll get ATI in the next two years and the healthcare sector will still be broken and it will still be impossible to afford rent in New York City and build houses and all these things. And that may well become true. And so I think it's important to engage with those parts of the world too, even though they're really, really challenging. And I think the really nice thing about LLMs is that actually, there's so many workflows now that are accessible to you as a tech founder and people are somehow more open to working with tech companies than they ever were before. Selling into the sectors of the economy in 2015, incredibly hard. I think now post the ChatGPT moment, people are willing to give chances to small startups that they weren't willing to do previously. As you mentioned earlier, the cost of doing things like forward-deployed engineering has fallen by maybe five to 10 x now at least. And so there's a lot of new possibilities and I'm excited to engage with the best.

Lenny Rachitsky (01:20:01):
Wow, that is some alpha right there that you're finding, that some of these very large organizations are more open to working with startups, because classically, investors don't want to invest in companies that are going after healthcare companies and governments and things like that. So it is really interesting actually to hear.

(01:20:17):
I'm going to mirror back the tips you just shared, and there's actually a secondary tip that I think is the more interesting piece. So the first thing you're taking away is iterate quickly, but I love your tip of ask for lots of money quickly, early, to see if it's an actual idea that people will pay lots of money for. And if not, move on. I love that.

(01:20:35):
The other is build a very distinct culture, but the piece you share there that I love even more is this idea of knowing what a high bar looks like, knowing what awesome A plus people look like, and you need to work at a company like Palantir to actually see that. So the advice there I feel is just work at a company that is amazing, first, with the best talent, to understand what that should look like, plus you build a network of those folks. So I think that's really interesting.

(01:21:03):
And then the other pieces of advice you're pulling away is work on really hard, messy problems because that's where the biggest opportunities are, and it's sounding like this is the easiest time to actually do that. Amazing.

(01:21:13):
Okay. I'm going to take us to a recurring theme on this podcast called AI Corner. And what we do in AI Corner is we share some way that .. and this is you sharing ... some way that you've found AI to be useful in your day- to-day, either in life or in work. Is there any way you found some tool ... some AI tool useful that you can share?

Nabeel S. Qureshi (01:21:38):
Oh my gosh, there are so many. I'll give you a few examples. So I use Wispr Flow quite a bit. So this is the talk to your keyboard and it will transcribe for you app. Very good. It's just great when you are iterating very quickly with an LLM and sometimes you have to do these paragraph-long prompts and it's just easier to speak into them. So Wispr Flow, I like.

Lenny Rachitsky (01:22:01):
Just to double down on that, you press a button and you start talking-

Nabeel S. Qureshi (01:22:05):
Yeah.

Lenny Rachitsky (01:22:05):
And it's writing out what you're saying. Cool. And there have been these products for a long time, Dragon Dictate and all these guys. Is the difference now these are just very, very good now at actually transcribing what you're saying?

Nabeel S. Qureshi (01:22:18):
I think that's right. Yeah, they use a really good model and so it rarely makes mistakes even when I think it's quite challenging. And then, yeah, the UX I think they just nailed. So that's really good one.

(01:22:27):
I love Claude Code for developing. Even though I have my complaints about it, there's something just very addictive about just telling it what to do. And it's basically something that you run within the terminal of your computer, and so you just type Claude, it opens up the Claude interface. It's very cute, it's very beautifully designed, and you just tell it what to do. And it actually operates on the file system directly. So if you're like, "Hey, create a bunch of these files," that'll just do it and you don't need to go and muck around inside Finder yourself. And then it'll do these really complicated pull requests and it'll basically execute them quite well. So to me, this is a very exciting kind of preview of AI agents.

Lenny Rachitsky (01:23:03):
That's what I was going to ask. So this is essentially an AI agent engineer. I didn't know that's what Claude Code did. Very cool.

Nabeel S. Qureshi (01:23:10):
Yeah. It's sort of a guided agent, but yeah, it is really sweet. And then yeah, I'm just enjoying ... you know, every week there's a new, wonderful new thing to play with. Last seven days, I've been testing Gemini Pro 2.5. Excellent model. I don't love Google's UX sometimes, but I was playing with that. And I use LLMs every day for all kinds of things. The other day I was doing taxes and I needed to classify a bunch of transactions based on some metadata, and so I just wrote a script up really quickly and it did that. So.

Lenny Rachitsky (01:23:43):
I love just the smile on your face as you're describing all these AI tools. I think a lot of people are just like, holy shit, I'm just overwhelmed with all the things I need to be paying attention to. All these things I'm hearing, all these tools I got to try. And I love just this vibe of just like, this is incredible and so fun. We need more of that.

(01:24:01):
Okay. I'm going to take us to another recurring segment on the podcast. You're going to get a double whammy. Contrarian Corner. So here's the question. What's something that you believe that most other people don't?

Nabeel S. Qureshi (01:24:12):
I think going to college is great. I think this is a somewhat contrarian view within tech, maybe not in the broader economy, but I often see people saying just like, oh, if you can just drop out when you're 18 and just start working, why would you go to college? And I think this is completely wrong, but maybe it's good advice for 5% of the population who probably would've been to your fellows anyway. But college is one of the few times when you can just make really, really deep friendships. You are in typically a nice campus. If you're in North America, you get to spend all of your time just thinking and writing papers and reading books and hanging out with your friends.

(01:24:49):
And it's actually very precious and it's very hard to find that kind of time after you turn 21 because you got to pay your rent, you've got to work, you've got to do all this stuff. Let's say you make a bunch of money, you take a career break, it's still ... all your friends are working and you always feel like there's a ticking time or on top of your head or something.

(01:25:09):
So just taking those three or four years at the very beginning and going really deep on lots of different intellectual topics and being able to try different things and discover more about yourself. I'm a big college fan. I can't comment on the ROI or whatever. I personally think the ROI is great, even though the fees are kind of high in the U.S., but that's probably my kind of contrarian within tech view is don't drop out of college unless you have a really good reason.

Lenny Rachitsky (01:25:35):
It's so funny that that is contrarian and it does sound contrarian. I had a great time in college here. Here. Okay. Is there anything else, Nabeel, that you wanted to share or leave listeners with before we get to our very exciting lightning round?

Nabeel S. Qureshi (01:25:48):
No, I think it's a really exciting time in the world. I think AI can be exhausting, but it does really just open up the possibility of building a better world in all these ways. And so I think just reassess what you're doing every couple of months and make sure that it's aligned with where I think AI is going and make sure that you are working on something that you feel has very high potential if it succeeds. And I think that's more important than ever now just because the amount of leverage we have with technology is at the highest point in history.

Lenny Rachitsky (01:26:22):
Let me double click on that real quick. So for people that want to do what you're describing, what helps you understand where AI is heading and just kind of align with it, are there places of information and news you find useful? Is it just play with it kind of thing? What would you recommend?

Nabeel S. Qureshi (01:26:39):
This is the big question. I use X a lot to keep on top of AI, so I would just recommend finding a good Twitter list and maybe following people off of that. There's some good newsletters. I really like Latent Space, I know his X handle, it's Swyx, S-W-Y-X. I can't remember his actual name, but that one is very good and it's pretty technical. I would recommend trying to stick to the more technical newsletters if possible. I think there's a lot of philosophy about AI or AI policy type stuff, and I think that's good if that's your area, but it's an area where it's very easy to have a lot of takes on it. You're not necessarily learning a lot by reading those.

(01:27:16):
But I think it's just important to know what's going on and make sure you are revisiting your own workflows as often as possible. And just making sure that the people who went here are going to be the kind of hybrid cyborgs who fuse with the AIs. This actually played out in chess, if I can take a slight detour, is the chess players who succeeded the most in the mid 2010s especially were the ones who were really early adopters of neural network based chess engines. So when DeepMind did that thing, there was very quickly an open source version of it called Leela, and you find basically the very top players like Magnus Carlson, Fabiano, they were the ones who kind of mind melded the most with Leela and learned how it played and then kind of started copying its moves.

(01:28:06):
And so I think just becoming a cyborg to the extent that you can. And then I think there's this barbell thing of, it's also important to just leave everything at go touch grass just for your own mental sanity.

Lenny Rachitsky (01:28:18):
Excellent advice. And with that, Nabeel, we've reached our very exciting lightning round. Are you ready?

Nabeel S. Qureshi (01:28:24):
Yes.

Lenny Rachitsky (01:28:25):
Here we go. What are two or three books that you find yourself recommending most to other people?

Nabeel S. Qureshi (01:28:29):
The first one that comes to mind is Impro by Keith Johnstone. This is actually ... I wrote about it in that essay. It's one of the books that [inaudible 01:28:36] used to send to people. I just think it's a really interesting book. So nominally speaking, it's about improvisational theater, which I believe this guy was a pioneer of. He was a British guy, Keith Johnstone, active between the '60s and the 80s I think. And Impro is just this really interesting book about creativity and how social behavior works and basically just what he taught his improv students. It's a very weird book. It's full of these unbelievably strange ideas. There's a lot of very tactical things he tells you to do in the first chapter, for example, just to break out of your own mental frameworks, really just wild stuff.

(01:29:16):
He'll tell you to walk backwards while counting down from a hundred and think about some problem that you're struggling with and there's all these kind of odd things. But the number of ideas per page I've found on that book is extremely high. The concepts about how social interaction works and how things like status and so on play into your social behavior are super important. And they made every kind of fully deployed engineer read that for the simple reason that I think it just helps you kind of read people better and interact with them better and become more conscious of how you are coming across and just modulate that.

Lenny Rachitsky (01:29:51):
What is the title again?

Nabeel S. Qureshi (01:29:52):
Impro.

Lenny Rachitsky (01:29:53):
Impro. Okay, cool. We'll link into it in the show notes.

Nabeel S. Qureshi (01:29:56):
Yeah, so Impro is number one. I think just to go a little more highbrow, maybe Shakespeare's history plays, there's a set of them called the Henriad, so like Henry IV, Henry V, Henry VI. I find most people don't read these, so they'll read Hamlet or Macbeth or whatever, but the Henry one is absolutely incredible. You don't have to be interested in British monarchy or British history in order to enjoy them. They're actually some of the most interesting and insightful books I've read about power and how power works and politics and what the sacrifices that you might have to make if you want to be a successful king in that case. But it transfers over.

(01:30:35):
I think it is worth thinking really hard about, I think especially in a world where everything is kind of organized around these prominent figures and personalities now. When you think about the current administration, you think Trump, Elon, or when you think about AI, you think of Sam Dario, right? And so I think it's important to understand, how do you think about these personalities and yeah, the kind of game that they're playing. And Henry is actually ... the Henriad is an incredible kind of set of books around that.

(01:31:05):
They're also easy to read, which sounds hilarious when I say it, but you can read a Shakespeare play in a day. They're sort of ... I don't know, they're like 50 pages long. It's not that bad. You have to get used to the language. Yes. But I would recommend that for sure. I guess you asked for two to three. I love High Output Management by Andy Grove. I just think that's a great business book, and people tend to read summaries of it on the internet more than they actually read the book. But the actual book has a lot of really interesting stories and explanations about ... I think the most powerful thing about that book is actually how Andy Grove thinks, and less any of the specific tactics there. And I think you don't get that unless you read how he came up with all these things.

Lenny Rachitsky (01:31:48):
Your first two books were extremely out there versus what other people have recommended, and the third book was the most recommended book on this podcast. So I love that spectrum that we just went on. Perfect. Okay, next question. Do you have a favorite recent movie or TV show that you've just really enjoyed?

Nabeel S. Qureshi (01:32:04):
The last movie I really loved was a Decision to Leave. It's a Korean movie. It's by the Director of Old Boy, which maybe some people have heard of. It's a great movie. I think it was released a couple years ago and the basic premise is, there's a detective who is investigating a woman who's accused of killing her husband, and he gradually starts falling for her, which starts to affect his judgment in all these ways. Just a really fascinating kind of psychological thriller with a sort of romantic element to it. Visually, very beautiful. Yeah, I think a lot of the most interesting movies nowadays come from abroad actually. So East Asia, South Asia, places like that. TV, I don't watch so much yet. It's been a while.

Lenny Rachitsky (01:32:47):
Totally understandable for a founder. Okay, next question. Do you have a favorite product that you've recently discovered that you just really love? It could be an app, it could be something physical, it could be a water bottle.

Nabeel S. Qureshi (01:32:58):
I don't have a good answer to that one. I guess I don't buy enough stuff.

Lenny Rachitsky (01:33:01):
Fully acceptable. There's no wrong answers in the lightning round. Moving on, do you have a favorite life motto that you often find useful in work or in life that you come back to, that you share with friends or family?

Nabeel S. Qureshi (01:33:15):
So there's this architect called Christopher Alexander who wrote these beautiful books that are about beauty and kind of more than architecture. And he was a teacher at UC, Berkeley, and he got really frustrated with the students because he just felt like they were always turning in kind of average work. And so he would always tell them every week, imagine there's a gothic cathedral in France called Charge. And he would say, you have to aim for Charge. You have to make something that is better than that. That should be your goal, not to just turn in something that's what you feel is good enough. You actually have to try and be better than the very, very best that ever did it. And I find myself just repeating this a lot to myself. It's just aim for that, really try and do that. Otherwise, it's very easy to anchor on something right in the middle. And you do this unconsciously all the time.

Lenny Rachitsky (01:34:09):
So is that the motto, just aim for Charge?

Nabeel S. Qureshi (01:34:12):
Yeah, yeah, yeah.

Lenny Rachitsky (01:34:13):
I love that. Most people have no idea what that would be, but with the context is quite powerful. Final question, what's a classic novel that `you think would be most valuable for product builders?

Nabeel S. Qureshi (01:34:27):
My favorite novel is Anna Karenina, and I would recommend that everyone read Erica.

Lenny Rachitsky (01:34:32):
I'm reading that right now. I've never read it before.

Nabeel S. Qureshi (01:34:35):
No way. And yeah, so it's by Leo Tolstoy. It's this epic 19th century Russian novel that follows a set of characters across society. And I think it's just extraordinary because what's amazing about him is he's just able to imagine himself into the brain of anybody. And so even ... he will briefly just go into the consciousness of, I don't know, the servant who's bringing the meal to the table or something like that. And he'll just tell you a page of what they were thinking, and then he'll just flip back into his main character's head. And I think that is the most impressive demonstration of this kind of skill I've ever seen.

(01:35:12):
And I think, to connect it to your question, this is what you have to do if you're going to be really good at product, is you have to really think yourself into the other person's head, and you have to be really seeing it the way that they do. And it's so hard, especially as a founder or product person, not to just get stuck on your own way of seeing the problem, right? You wrote up this doc, you made these marks. You're like, this is going to be great. And then you take it to somebody, they don't care that much. You really have to exercise your empathy and understand why they see it that way and what they actually care about.

Lenny Rachitsky (01:35:43):
What a beautiful way to bring it all together. Let me also add, while I'm reading the book, something ... a tip here is, people talk about having Chat GPT voice mode, just kind of sitting there next to you. I found that extremely helpful with this book where I just ask what the hell does this thing mean? There's all these Russian dances and balls and etiquette. You just ask and you're like, I'm reading Anna Karenina, what does this mean? And it just tells you.

Nabeel S. Qureshi (01:36:04):
Yes.

Lenny Rachitsky (01:36:04):
So there's another cool tip for AI. Okay. With that, Nabeel, this was incredible. Two final questions in case people want to look you up. Where can they find you online and how can listeners be useful to you?

Nabeel S. Qureshi (01:36:16):
Find me online, my website is nabeelqu.co and my X handle is Nabeel QU, I'm probably most active on that, but yeah, my website has all the links and a bunch of essays and interesting stuff. How can you help me? I would say send me an email. My email is on my website. Introduce yourself, say hi. I love meeting people. I don't always have time for coffees nowadays or things like that, but I genuinely do get a lot of energy from just receiving emails from interesting people, so please do reach out.

Lenny Rachitsky (01:36:48):
Awesome. Definitely check out Nabeel's Principles. Is that the name of that post?

Nabeel S. Qureshi (01:36:53):
Yeah.

Lenny Rachitsky (01:36:53):
Great. Okay. That's one to start with, and then also there's the Palantir Post that we just talked through. Okay. Nabeel, thank you so much for being here.

Nabeel S. Qureshi (01:37:00):
Thank you. Appreciate it, Lenny.

Lenny Rachitsky (01:37:02):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

