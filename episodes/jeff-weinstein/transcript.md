---
guest: Jeff Weinstein
title: 'Building product at Stripe: craft, metrics, and customer obsession | Jeff
  Weinstein (Product lead)'
youtube_url: https://www.youtube.com/watch?v=qbZQjprTnrU
video_id: qbZQjprTnrU
description: Jeff Weinstein is a product lead at Stripe, where he helped grow their
  payment APIs to hundreds of billions in volume and transformed the way founders
  start companies into a few simple clicks...
duration_seconds: 9300.0
duration: '2:35:00'
view_count: 45501
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- onboarding
- metrics
- okrs
- roadmap
- prioritization
- user research
- iteration
- data-driven
- analytics
- funnel
- revenue
- culture
- management
---

# Building product at Stripe: craft, metrics, and customer obsession | Jeff Weinstein (Product lead)

## Transcript

Lenny Rachitsky (00:00:00):
Watching you operate on Twitter, you're just breaking this wall between the PM and the customer.

Jeff Weinstein (00:00:04):
The moment the customer felt compelled enough to go out of their way to talk about some problem, that's a unbelievable gift. I will leave a meeting to just get one message back to them. If you're text message friendly with five or 10 of those, you are going to have so much direct signal that is infectious.

Lenny Rachitsky (00:00:22):
Many people told me I need to ask you about picking metrics.

Jeff Weinstein (00:00:24):
Well, what was the value that we're trying to produce for the customer and can we measure it from their perspective? And okay, how do you know you have product market fit? Charts that showcase things are going up into the right on one hand and then tweets on the other.

Lenny Rachitsky (00:00:36):
You started at Stripe something called study groups.

Jeff Weinstein (00:00:39):
We show up four to eight people total pretend to be some company with some outcome problem. Rule one is you do not work at Stripe and rule two is we're not here to solve any problems. This is just about practicing empathy for the customer.

Lenny Rachitsky (00:00:57):
Today my guest is Jeff Weinstein. Over the course of his six plus years at Stripe, Jeff was the product lead for Stripe's payment infrastructure teams. We helped scale Stripe payments to hundreds of billions of dollars in volume a year. He also led PMs and Teams on a number of zero to one bets at Stripe, and most recently took on the scaling of Stripe Atlas, which as of the day this podcast launches allows you to incorporate a new company in a single day, including handling 83B elections, incorporation documents, getting your EIN, share purchases, and all the things that used to take weeks or months before a company could begin operating. At this point, one in six new Delaware corporations are started on Stripe Atlas, which blows my mind. This episode ended up being the longest in my podcast history because I wanted to basically do an archeology of an incredibly effective and admired product leader.

(00:01:49):
We spent the entire conversation digging deep into the many skills that Jeff has built that enable him to consistently build successful and beloved products. We get into his go-go- go plus optimism, long-term compounding philosophy of building products, how to think about and operationalize product craft and quality. He shares a popular program that he started at Stripe called Stripe Study Groups that I think you should steal. We also talk about how to effectively talk to customers, how to know if you have product market fit for your new product, how to pick great metrics for your team, what he's learned about getting shit done at a big company. Also, advice that he's gotten from the founders of Stripe and so much more. This episode is for anyone who's looking to level up their product building chops in every way. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you Jeff Weinstein. Jeff, thank you so much for being here and welcome to the podcast.

Jeff Weinstein (00:02:50):
Thank you Lenny of Lenny's Podcast. I knew what to expect, but it's fun to see the first name and the podcast all line up. I really appreciate you asking.

Lenny Rachitsky (00:02:59):
So I wanted to start with a quote that I found from you that I think gives a little perspective into how you think and how you approach the world. So here's the quote. "Very frequently I would do poorly on tests in school and then the professor would say very reasonably, 'Hey, I think you should bump down a level to the previous semester's pace,'" and you said, "I actually know that, that's why I'm in this class. I want to be in the class that I'm potentially the worst at." This isn't how most people think. This isn't how most people operate. Usually people want to get good grades, they want to be at the top of their class. Clearly you have a different approach and a different mindset. Where did this come from for you and how did this shape the way you think about product and the work that you do?

Jeff Weinstein (00:03:37):
Some of it was just the fact that I wasn't particularly good at the class and had to rationalize it for myself in some form. So in retrospect that sounds highfalutin, but at the time I just wasn't particularly good at the classes I was in. But I think it comes from growing up. I went to a pretty hippy-dippy K through 12 school in Baltimore, Maryland where we were really asked to think about why we were in school and to pick any of the courses that were of interest to us outside of AP programs or grades or any particular requirements. You really got to choose your own path. And I recall one particular class in high school, which was somewhat a science class, but it was called the History of Science, and we actually walked through and studied all of the, at the time, best understood ways the world worked in science, but then later were turned out to be wrong, right?

(00:04:40):
In the 1500s we believed X, Y, and Z. In the 1600s we believed A, B and C. just very confidently. In 1500s we thought something and then the 1600s we thought something very different. And so this class was quite impactful on me where we spent an entire year studying things that are not true. It was fascinating. That particular teacher employed another trick on us during that class, which was it took the tuition fee of our school and divided it by the number of hours and wrote the cost on a ticket and then handed us in the beginning of the year. Tickets for every single one of the classes and he would stand at the door and you would have to give him a ticket at the end of the class that he thought it was worth it. And just like that practice of deep intellectual understanding of how people evaluated something at the time and choosing for yourself to spend the time on it by just the physical act of handing that ticket to the teacher.

(00:05:44):
That really clicked for me. And so when I got to college and it was a real college university, people are coming from often quite more rigorous backgrounds of things that were true. I was a bit unprepared and I remember actually taking a microeconomics class that was quite advanced and had a close friend and we studied exactly the same information. We sat and looked at the same cheat sheets, we practiced the same quizzes, we read the same books, and he got the top grade in the class and I got the bottom and that's from where that quote came from where the professor said, I think you should bump, potentially bump down. I was like, "I already know that stuff. I'm interested in this topic. I'm going to try to improve, but look just because I'm significantly worse than the other kids in the class that has little to do with if I should leave." And he was particularly cool with it.

Lenny Rachitsky (00:06:32):
This episode is brought to you by Pendo, the only all-in-one product experience platform for any type of application, tired of bouncing around multiple tools to uncover what's really happening inside your product? With all the tools you need in one simple to use platform, Pendo makes it easy to answer critical questions about how users are engaging with your product and then turn those insights into action. Also, you can get your users to do what you actually want them to do. First, Pendo is built around product analytics, seeing what your users are actually doing in your apps so that you can optimize their experience. Next, Pendo lets you deploy in-app guides that lead users through the actions that matter most.

(00:07:12):
Then Pendo integrates user feedback so that you can capture and analyze what people actually want. And the new thing in Pendo, session replays, a very cool way to visualize user sessions. I'm not surprised at all that over 10,000 companies use it today. Visit Pendo.io/Lenny to create your free Pendo account today and start building better experiences across every corner of your product. PS: you want to take your product-led know-How a step further, check out Pendo's lineup of free certification courses led by talk product experts and designed to help you grow and advance in your career. Learn more and experience the power of the Pendo platform today at Pendo.io/Lenny.

(00:07:56):
Today's episode is brought to you by Cycle. The AI-powered feedback platform for product teams. Is your customer feedback, a tangled mess of Slack threads, survey responses and overflowing inboxes? Wish that you could know what your customers really need? Cycle unifies all of your customer interactions from support chats to user research, gong calls and app store reviews into one neat collaborative space. Cycle's AI then extracts actionable insights on autopilot. Cycle will learn what you're building so that it can label incoming feedback automatically. That means you'll get a full voice-of-customer report without manually triaging feedback. Then simply you Cycle Ask to dig deeper into any topic and generate custom AI-generated summaries across your entire feedback repository. What makes Cycle different is the way that it lets you close feedback loops in each release. Feedback is not used just as a way to prioritize what to build, but also as a tool that creates trust with all stakeholders. Sign up for a free cycle trial today at cycle.app/Lenny and put your feedback on autopilot. That's C-Y-C-L-E.app/Lenny.

(00:09:07):
It's really interesting that you went to this liberal artsy hippy dippy school as you described, which a lot of people bash on. Why spend all this college money and time on a liberal artsy education and you ended up being really successful in a very technical, highly analytical data-driven company, and it's interesting that that experience still helped you succeed in this other path.

Jeff Weinstein (00:09:27):
It did take a change though because I started in... English was my selected major in school, but then I kept playing with computers and I kept liking math and I looked at the roles of the backgrounds of the people who were running the types of companies I loved. At the time Facebook was getting super phenomenally successful. Apple was already on their up and up again and everyone who was leading those places had technical backgrounds and I liked computers a lot, so I added computer science as an engineering degree midway through school. So I had to take the real science classes with the pre-med kids and the rest of it, and I did similarly poorly, but I did end up with a computer science degree and a liberal arts degree. So it was a journey, but I had to make a pretty big switch in the middle to get on that path.

Lenny Rachitsky (00:10:16):
I asked you if there was one thing that you'd love to get across in this podcast. I asked you what would it be and here's what you said. Here's the first item on this list that you sent me, "Go, go, go ASAP plus optimistic comma, long-term compounding approach." Can you just talk about what you mean by that?

Jeff Weinstein (00:10:36):
Yeah, there's two things going on here. So I see the world as immediately we have just such opportunity to take action in front of us. We can be optimistic and go, go, go as soon as possible. I think that a lot of life is you get as much furniture as you've room in the house. We will do the work the night before it's due, so let's just make it due tomorrow. Can we turn tomorrow into today? So just optimistically seeing if we can just inject energy to go, go, go has produced surprising results and I think it ignites in other people that same interest and then it feeds off each other. And that's I think really in my bones from growing up. And then I added over time, had to learn this longer term, compounding, more strategic mindset where some of the things we want to accomplish, be it at my startups in the past or at Stripe, they can't be solved in an afternoon.

(00:11:41):
They're going to require layers of infrastructure and services and applications and UI and partnerships that really look like that iceberg drawing you see where you just see the top, but then there's the whole thing underneath and I've had to learn over time to pair my instinct of like, "Let's get it done today, let's move forward, let's see what we can get done. Let's make some mistakes, let's try it out." With, "Where are we going? What needs to be true over time? Where can we always invest? What will we never regret spending time in?" We'll never regret spending time making the latency of our payments APIs at Stripe faster. We'll never regret making it more reliable to send 83B election mails to the IRS. Like we'll never regret those things. So let's just always compound those capabilities over time. Then the trick is how do you mix this go, go, go attitude with a long-term compounding? That's something I still struggle with, but I try to purposely balance it more than I used to.

Lenny Rachitsky (00:12:44):
It's such a good way of summarizing just how to be successful in a lot of things. Go, go, go ASAP, stay optimistic. Focus on long-term compounding growth. Is there an example of that in action? I know we're going to talk about Atlas a bunch, but I guess is there an example of that working for you or a product you worked on?

Jeff Weinstein (00:13:03):
I work at Stripe, which is a infrastructure company. We build things that help businesses do online commerce in various forms, and I've had a few roles at Stripe. I'm in our beautiful office here in South San Francisco, one of which was the product person that helped us decide how we were going to go global and how we were going to offer multiple ways for people to pay. It turns out there's more than just credit cards in the world. There's small hundreds of ways that people will naturally want to pay for things online and as a business you're going to, of course, just want to accept whatever it is people want to pay with. And for the first seven or eight years of Stripe, well prior to my being here, the incremental country ads and the incremental new payment methods was relatively flat over time and that was surprising to all of us who worked here because the world wanted it and we had a lot of people working on it and we were working very hard, but it wasn't producing returns in the way that we wanted.

(00:14:11):
And so actually the optimistic as soon as possible go-go attitude was not working. No matter how much energy we poured into building Thailand payment methods or UK bank transfers or an in-person payment system in Latin America, we just couldn't rack up points and get it done. So we had to step back and say, "Well, what is the world going to look like in 10 years? What was going to need to be true and how can we start to go there now?" Which meant going a lot slower, building internal platforms, sending people around the world to start to build these payment methods, uproot their lives, pay for their apartments, get them on airplanes, start using these payment methods actually in the world. And so it really our line flat line for a while and we're like, "Okay, is this strategy working? Is it not working?" But then over time we start to see it switch to nonlinear again and go from whatever it was, 10 payment methods at the time.

(00:15:03):
And now Stripe accepts over 100. So we got to 50 really quickly and then skyrocketed to 100. And I remember there being a meeting where we said, "Well, maybe we should just lock everyone in the basement and see if we can get from 10 to 50." That would be the intensity startup go attitude. But we looked at the individual components of what it meant to get this done and how long we wanted this to be true for and we had to go a lot slower. That was a very formative decision where you had to mix the go, go, go with the long-term compounding.

Lenny Rachitsky (00:15:39):
Awesome. Okay, so let's start to delve deeper into some of the specific seals that I hear you're incredible at and that I've seen you be incredible at on Twitter and LinkedIn and things like that. So the first is craft, craft and quality. I'm told by many people that you have a very strong obsession with craft and user experience and quality and even more so I'm told that you teach people at Stripe how to be obsessed with craft and quality and user experience in a very systematic way. I feel like this is something a lot of people are starting to realize is really important and or are trying to get better at, either personally or at their company. So first of all, let me just ask why is this so important to you? Why do you think craft and experience and quality is so important? Why do you put so much emphasis on it yourself?

Jeff Weinstein (00:16:25):
I think I'm really working backwards from failures in the past and avoiding them. And so maybe just a quick story. I started a company several years ago based on just a personal pet peeve of mine, which was I was a SQL analyst. Many you listening might have written SQL in the past, maybe the robots write the SQL for you now, but you still need to write SQL yourself. And every single time I wrote a SQL query, I wanted to run the same subsequent analysis. I wanted great version control, I wanted all the cool stuff that GitHub had for code but for writing data code. And so my friends and I built a little Python tool which basically let you run our style queries. It lets you draw charts and pivot tables quickly and sharing all this modern SaaS application stuff. But applied to SQL a few years ago and we turned that into a company.

(00:17:29):
We got some progress, but then there was this moment one day where we had maybe a couple 100 customers and we had an error where we basically by accidentally shut down the service and it was bricked for 10 or 20 minutes. And at the time we were hustling in our little dinky office to get the application back online. And we really were proud of ourselves about how reasonably quickly we did and people went back to using it. It wasn't a super long outage and we didn't lose any data. We were just high-fiving each other. And we went about our day and about a year later I realized that that was a...

(00:18:11):
I missed a huge moment that I should have pounced on, which is that during those 20 minutes, our customers weren't furious. They weren't emailing us like crazy, they weren't texting us, they weren't trying to find us on Google Maps and knock on our door and say, "Hey, I need this thing back online immediately." We heard a couple comments from them, it was little murmurs. And I didn't realize at the time that was the signal that we did not have product market fit. And I ended up wasting many more years on that project. And wasting is a big word. We built amazing software, people liked it, we were able to sell the company.

(00:18:55):
It helped many of us learn how to really build software. But I'm really trying to avoid that situation again. And I think craft is a dessert that you get after the meal of does your thing solve a real problem in the world and are people clamoring, needing it badly? And that's really my obsession is in finding problems in which people will pause their entire day to solve. They will leap through the computer to be like, "Oh my God, I have that problem. Do you have a solution?"

(00:19:32):
And if you focus on that style of product development and we can get into just how do you listen for that and then turn that into product. Later, you might get the opportunity to really provide craft and beauty and touches and moments and delight. But certainly there is no amount of craft, there is no amount of beauty, there's no amount delight or touches you can add to a thing that will solve the problem we had at our startup, which is that people didn't really need this. And that's the biggest error is picking something in which people don't really need it. And then going through these practices of trying to make it great when maybe it shouldn't exist in the first place.

Lenny Rachitsky (00:20:16):
I think a lot of people see all these tweets and messages about just obsessed with the craft of what you're building and you can easily lose sight of... Nobody even cares about what you're building. It could be the most incredible experience ever designed, but if it's not something anyone ever wants, it doesn't really matter.

Jeff Weinstein (00:20:34):
People don't really get out of bed for their second problem. They get out of bed for their first problem. And you have to carefully listen and not pitch your customer or your prospective customer as you're trying to figure this out. And I think this advice, not even advice just style applies to small companies, big companies, anyone which is people don't want to be pitched. I'm sometimes on a UXR call with a very well-meaning person or a founder who has a new product that they want advice on or they want to find customers. And the first thing that they start talking about when we get on the call is, "Hi, I'm the CEO of X, Y, and Z company. We do one, two, and three. I want to show you a demo." It's like, "Hold up, I'm a customer. I have..." What a wasted opportunity you've just done here.

(00:21:34):
I have so many problems, you're guessing ahead of time, what is my top problem and now that you've anchored and limited to the pitch you're going to miss, you very likely going to miss the burning problem that they have on the top of their mind. And it's not the customer's job to interrupt you and say, "Hey, could you stop your pitch? I want to tell you about my top problem." And you can see this down the stream, which then companies who launch things, put craft, have a great launch, raise money are then later gone. And it's because they built something that wasn't solving a burning need. And I think you can stem it all the way back to they were just pitching rather than sitting in silence and just waiting for their customer to just open their heart out about what's the most burning thing.

(00:22:28):
And sometimes I'll prompt our customers, I'll say, "Hey, do you mind just opening up your email? What's in there?" Or, "If you weren't talking to me right now, what would you be working on?" Or, "Hey, last week, what grinds your gears? What are you not looking forward to?" Or magic wand, "What do you wish you could just have off your plate immediately? Forget Stripe, forget about thing, work on just in your whole life. What is it that you do not want to be doing?" Or, "A massive opportunity you wish was just one door away?" And it's a little awkward because they don't know why you're asking that kind of question, but then you just sit there in silence. And for the most part, if you have amazing customers who are smart and ambitious and are trying to build their own business, they're going to want to offload their hardest thing to somebody else.

(00:23:17):
If you've earned trust along the way, and certainly not pitching is a great way of earning trust. You're just listening. We've learned a lot at Stripe from that. And that's where you can start to find adjacencies, right? "Well, hey, I don't know if Stripe could really help me with this, but wouldn't it be cool if we could identify if the person signing up on our site wasn't fraudulent or is who they say they are or isn't a bot, or are they really a dog on the internet?" And we're like, "We keep this as the major complaint from all of our customers, but we're not an identity company." It's like, "Well, I guess now we are because all of our customers who are trying to build their business all have this problem." And so via silence, you can just create your roadmap pretty quickly and drop a lot of the long UXR, long survey, long build cycle approach.

Lenny Rachitsky (00:24:15):
So I love where we're going with this. This is where I was going to actually talk about next is just your ability to talk to customers and user research. It feels very unique, watching you operate on Twitter, you're just sharing your email constantly, getting on calls with people constantly. There's this, you're breaking this wall between... That a lot of people imagine there is between the PM and the lead of a team and the customer. You're not relying easy research. You're not waiting for someone else to do this work for you. Talk about just why and how you do this. I think there's so much to learn from just how you operate in finding opportunities, picking problems to solve by talking to customers.

Jeff Weinstein (00:24:53):
It's where the business comes from is customers. It is not a long shot hypothesis about why to talk to them. It's like if they love your stuff, they will tell their friends and pay fair prices for the product. We're so fortunate through the internet that people announced themselves as being interested in a topic. Sometimes they're interested in it by posting on Reddit a long thread or a screenshot of a customer service interaction that bugged them or hopeful that from their dorm room in country X, someone else in the world has solved the same problem. And the internet has given us all this absolutely magical forum that you can just yell out the window and then billions of people could actually listen to what you said out the window. Now, that's not all the time true for all people in all situations, but dramatically more true now than ever before in human history.

(00:26:05):
And so the fact that people wouldn't be listening to their customers and really jumping through the computer to talk to them surprises me. It's like I always sometimes think, "Do they have some other strategy? Are they so confident in what they're building that they don't need to hear directly from the people who will be using it?" And I think some of it is my own fear that I'm going to make the same mistake I've made in the past, which is build something that people like they're using but isn't solving a burning enough problem such that they're going to stop their day, they're going to tell their friends, we're going to be able to sustain the company economically over a long period of time. And that really just comes from hearing people's most burning problems and then just jumping through the computer and talking to them takes a little bit of nervous gumption, like walking up to a person at a bar or cocktail party and saying, "Hi, my name is Jeff."

(00:27:08):
It can be a little awkward, but then you get it. It's a rush once it starts to work. And once you get the iterative loop that they're excited to talk to you, they have problems, they see you as a trusted, not salesy, not pitching, not narrow-minded to just my product and my position, but I'm here to hear about all of your problems and see where we can help. Not promising we can help solve everything, but let's listen. That is infectious, both between the customers and internally. And so I'm able to bring more people into that practice. At Stripe, I'm able to quickly grab an engineer and hop on a call. I can forward a message over to a Slack group. And they know that because the customer's speaking directly, it somewhat trumps everything that's happening during the day. We could go to our meeting where we're going to guess what the customer wants or we could talk to them directly.

(00:28:08):
And you have to use a little bit of art to decide which customers you want to listen the closest to. But even at Stripe's scale, where we're dealing with many millions of businesses and many hundreds of millions of consumers on the other end of those businesses, you can pattern match relatively quickly. What are the styles of customers that represent where the world is going, the most ambitious, the most technical, the fastest growing, the most detailed. And you don't need 10,000 of those people to talk to. If you're text message friendly with five or 10 of those, you are going to have so much direct signal about where to go that you forget how you did it in the past.

Lenny Rachitsky (00:28:57):
I love these. So I'd love to learn more about these tactics that you've found helpful. So you've shared this idea of silence, talking to someone and just being silent, and I forget the phrase you used, but just like ideas emerge, like your whole road map can emerge from that silence. So let me share a few of the things you shared so far and I'm curious what else. Two is tweeting just like, "Hey, I'm looking to improve Atlas right now. What bugs do you have? Here's my email address." You talked about text messaging, just like, "Hey, can I get your number? And I'll just text you when I have questions." If there's anything else to add to these, that'd be awesome. And then what else have you found? Just ways to actually get to a customer and find opportunities that are important.

Jeff Weinstein (00:29:34):
Speed is an important one, which is just reducing the time between the moment the customer felt compelled enough to go out of their way to talk about some problem. They're busy, there are snacks to eat, they have families, they have other things to do. There's a lot going on in the world, a lot. Your dumb product, it's amazing that they would spend any of their time discussing it at all. I mean, most of the time if you don't like something, you just move along. You just apathetically, silently move forward in the world. And so the fact that someone took their finite time to succinctly with curiosity, communicate to the world or you about your product, that's a unbelievable gift.

(00:30:27):
That should be P-zero alert level intensity. And so I will leave a meeting, I will change what I'm doing to just get one message back to them. Even if it's, "Hey, I got this. I'm about to go to dinner. Can I hit you up tomorrow?" They're like, "Oh yeah, thank you. Awesome. I can't even believe you responded." That puts us in the camp of on the right trajectory where they're going to feel that they have a almost secret portal between this big brand of a company and another human who's just actually curious...

Jeff Weinstein (00:31:03):
... brand of a company and another human who's just actually curious what's going on, that's night and day. And it's also, fun fact, tip, when people are really hot on an issue and it could blow up on social or they're going to start becoming a detractor, we make mistakes, we have SLA breaches, we have errors, you're going to want to get on that stuff fast. And in those situations, my bar for how we will respond to those folks is not to just solve the problem, but it is to turn them into a promoter, and most of the time we're able to, even if there was a pretty relevant issue.

(00:31:40):
I remember one time at Atlas, we had this bug in which for a handful of our legal docs, they were handing out let's say, 25 shares rather than 25% of the shares. We dropped the percentage sign, and thankfully a founder noticed this in the docs and tweeted about it. My heart paused and I was like, "Oh no, this could be a really serious issue." And we were able to fix it and regenerate the documents relatively quickly for everyone that was impacted. And I was thinking to myself, "Wow, we really let this person down. We have one job to do, which is to get their company right and we didn't."

(00:32:20):
And that person was incredibly gracious about the situation and said, "Anytime you want me to just read your docs, I'd be happy to. I have a law degree. I care about this topic. I want to brainstorm with you about ways that Atlas could do more document creations." I was like, "Wow, I can't believe I was in this sort of defense position, and now we've gained a friend in the world who can be eyes and ears and brainstorm with us." And the team maintains a really close relationship with that person as they do with many, many founders who use Atlas.

(00:32:53):
And so, just again, we're so quick to put the outside world in this other camp where we need to touch it with kid gloves and treat it as a big blob and a cohort and a statistic, when it is a human with a problem who likes snacks, who is busy, and it's fun to do and it turns out to be an incredibly easy, fast way to figure out what to build.

Lenny Rachitsky (00:33:20):
There's a bunch of stuff I want to follow up here. One is, people may be hearing this and like, "Oh my God, I'd be overwhelmed with feedback and people to fix problems for and bugs and texting of people." They're just like, "There's so many people that potentially I'd have to be interacting with." How do you try to narrow that down? I know Atlas is a very highly adopted product. There's a ton of people, there's probably bugs, often people sending you feedback. How do you pick the people to zero in on?

Jeff Weinstein (00:33:47):
I think there are two parts to this. One, what a problem to have. Of all the problems in the world, "I'm overwhelmed by customer interest," is on the top list of problems I want to have. I think most entrepreneurs would purchase that problem as a state. And so, if you're in it, I think, take a deep breath and look at the sunrise or sunset and just enjoy the fact that you've built something that is meaningful enough that people would spend their time. Again, there are amazing snacks that they could be spending the time on otherwise, so that's a huge deal. And then two, you need the art. There's an art and science to picking where to go deep. I will happily respond to folks with, "I really appreciate that. Do you mind sending me a screenshot or a video?" And some of them don't. Okay, that's fine.

(00:34:45):
You kind of get a sense of quickly looking at how they wrote about it or just pattern matching how detailed they were, or how much they seem that they want to engage and kind of balance it that way. Otherwise, you can tell folks, "This is really awesome. Do you mind sending me an email with three to five bullet points about the details of how you got to this issue?" And that's not a 30-minute meeting. You don't need to blow up your whole life to get on the phone with them. It's not a huge homework assignment to them, but it's enough structure that it will self-select those who want to go deep, and then from there, you really do owe it to them to follow up if they're going to be that detailed. And at that point, you really have made a product friend for life and you'll kind of continuously go back to them. So you have to kind of tune it.

(00:35:48):
I also will bound some of these efforts, so I'll just completely make up one day a program. So, "Hi, Stripe's doing a bug-finder program." I made that up as I was driving to work one morning, tweeted it, was curious if anyone would send anything. "We'll be taking videos for the next three days to go super deep." And people are like, "Oh my goodness, I would love to be part of the Stripe bug-finder program. May I apply?" I'm like, "Oh, it's very selective. But yes, of course for you." It's just giving people permission through a program, even if it is deeply arbitrary, I find helps with bounding it, and then later I can follow up with the world, "Hey, we ran our first program, we got 65 videos," which we did. "We found dozens of issues," which we did. It was an incredibly valuable use of our time and it really came from just a single tweet.

Lenny Rachitsky (00:36:53):
Something I saw you mention somewhere is that you only pay attention to feedback from people that are paying customers and ignore everything else. Can you talk about that?

Jeff Weinstein (00:37:00):
People who build things for people tend to be empathetic and interested and curious folks who have friends, and then those friends want to use your stuff because they know you and they like you and they'll have good feedback. But you need to figure out, is that actually your customer, or is that your friend trying it? Who is actually your target customer exactly? Not a company or a segment, not digital natives that are X big. I'm talking about Sarah in this department, who has these tabs open and just faced this problem and needs to solve it by 4:00 PM. That level of specificity. If that's your customer, and I'm talking mostly about B2B, which is where I spend a lot of my time as the social network, B2C stuff I have less intuition on, they're very willing to exchange money for solving their problems, incredibly so. Oftentimes, if you listen with enough silence, they might even say, "I'll pay you money to solve, blah." If you sit there long enough in silence.

(00:38:17):
And so, you could listen to your friendly friend who you got to play with your beta version and they'll say they liked it and they will click around. But that is extremely different from Sarah, who has the actual problem and is willing to pay. And it is so tempting to go down the first path with the friend group that I sort of needed a rule, which was like, "Okay, rather than..." I was like, "Well, don't pay attention to that quite as much. Really pay attention to, who is your target customer and are you in a fast iteration cycle for them and are they telling their friends?"

(00:38:51):
But that wasn't enough, because people are so drawn, myself included, drawn to the friendliness that I just set a rule, which is, "We discount all of that feedback from our friends to zero." That is not of interest to us. We don't even write it down. It's just not part of what we're talking about at all. We are only interested in Sarah, our target customer, and can we get her to solve whatever the problem is as quickly as possible, as jangly as possible and go from there?

(00:39:26):
And then the paying part is a forcing function because again, even with Sarah, because you're paying attention to her and solving her problem a bit, she'll say, "Of course, oh, this is great. I want feature X, Y and Z. Can it do one, two, and three?" Naturally, she would say that. But if you said, "And by the way, this thing is $10,000. We'll happily refund your money 100% the second you don't like it," she might say, "Whoa, whoa, wait a second. Yeah, I like this thing, but not $10, 000. For $10,000, it would need to solve X." And you're like, "Oh, there it is." That was actually what the thing that was of value, and we were all kind of dancing around this. It's useful, we're on the right track, and because I've fallen down that path myself so many times, I just set a rule.

Lenny Rachitsky (00:40:25):
This is great. I was actually going to ask. This technique of using silence, to help people actually practice it, you just shared this quote of, "For you to pay $10,000 it would've to do X." That's a really cool line to use. Is there any other advice there of just how to practice this idea of creating silence to help a potential customer share what they actually need?

Jeff Weinstein (00:40:45):
I encourage people to take an improv training class or two, just to get people out of their skin a bit. By the way, this advice applies to big companies also, not just small ones. And we have issues, and I hear other larger companies have issues where a big company will say, "Hey, we're an enterprise and we're going to pay you this big contract. All you need to do is build features one, two, three, four, five, six, seven, eight, nine, and go through security steps, A, B, C, D, E, F, G." And this siren song of the big three-year contract of your first enterprise buyer, even when you're already big, you can go from Fortune 1000 to Fortune 500 to Fortune 10 to Fortune 1. There's always more. There are so many stories of the rug being pulled in the middle and they never actually use it and the contract never lands.

(00:41:38):
Same in partnerships. And so, I would say the same thing, which is, "If we're super serious about this, send us $1 million. Wire us $1 million. We'll happily wire it back anytime you need it, but let's actually put some stake in the ground about the value." And I find that in the cases in which they're like, "Whoa, wait a second, no, absolutely not. We can't commit here." That's really a good signal because you're about to spend a huge amount of time building something that might not ever be used, and that's the majority case I hear. Or you might get the opposite, which is, "Sounds great. Let's make sure our teams are trained on it faster. How can we get you to our office to explain it? We need it to really work with this system we haven't talked about yet. And now that we're paying, we want it even faster."

(00:42:32):
And so, I find that it puts a fork in the road towards faster success or avoiding the non-success case. And even at Stripe scale, I've heard our founders somewhat push this methodology on us, where one from the outside might think, "Well, it's a 8,000 person company. Surely they have just regular ways of building things for larger customers, and we too need these style of commitments if we're going to go off roadmap."

Lenny Rachitsky (00:43:04):
So a big lesson you're sharing here is essentially, make sure people are ready to pay for something that they're asking for. That is the ultimate sign that they-

Jeff Weinstein (00:43:13):
And by the way, ready to pay is different than paying. Significantly different, significantly different. I've also thought of, "Well, as long as they're ready to pay and they said they would pay and they look at the contract, we should feel good." That is not the same as paying. Paying is an independent group of people saying, "My problem is burning enough that I'm willing to exchange something I have that has value for the promise of what you're going to do." And now it's a real commitment. That is extremely different than ready to. So I will often be on the phone or video, whatever with a founder and I will have them practice charging me. I'll just say, "Hey, I'm just a friend. I'm trying to help you out. It's a little bit self-serving because I work at Stripe and I want to get feedback on our products."

(00:44:09):
I'll say, "Feel free to sign up for any invoicing or payment service. I don't really care which one. You're welcome to choose Stripe if it's easy enough for you, I'd love to hear your two cents, and send me an invoice or a payment link for $1 right now, right now. That way, when it comes time to actually charge your first customer, it won't be your first time. It won't feel weird. You'll have already done this, you already have a dollar in your account, you already have your logo on the top right of the invoice. It'll feel great." And I probably could go through my email inbox and just see $1 receipts to random people because I'm just so convinced that the difference between paying and willing, ready, I thought they would pay is night and day different.

Lenny Rachitsky (00:44:57):
Yeah, there's this term, willingness to pay that I feel like it should change, as you're saying, to just cross that willingness to even just-

Jeff Weinstein (00:45:05):
Paying.

Lenny Rachitsky (00:45:06):
Paying, exactly.

Jeff Weinstein (00:45:07):
Yeah. And we can refund the money. There's no issue at all. Just other tricks on how to get people going is, ask them about their regular life as a human, "What did you do yesterday?" And they'll be like, "Oh, at work?" I'm like, "Or not. Whatever." And people, they'll start to spill, they'll just start to spill and eventually they'll get to their biggest problem pretty quickly.

Lenny Rachitsky (00:45:33):
Let's talk about metrics, going in a different direction. Many people told me I need to ask you about picking metrics and the importance of metrics and how you think about metrics. So let me just maybe start with a question of, just why do you think picking the right metric and why are metrics so important in building successful products?

Jeff Weinstein (00:45:52):
I somewhat walk around with the belief that the product manager's responsibility is to produce product market fit. And okay, how do you know you have product market fit? Charts that showcase things are going up into the right on one hand, and then tweets on the other. So metrics like quantitative and qualitative, and I really see them as deep siblings and equals, you really need both. It's not oh, OKRs versus something. There are some things you want the texture of the person on video showing how complicated a thing was. And then also, we're trying to make an economically viable system that we can run at large scale and you can't keep all that stuff in your head and need to measure it. And so, I think metrics at their best are a numerical representation of the value we're providing for the customer.

(00:46:59):
One could measure anything. You can just start counting events and log lines. We've made it incredibly cheap to count stuff. And so, now we have this big privilege of choosing what to measure. And I really just try to map it all the way back to, "Well, what was actually the value that we're trying to produce for the customer and can we measure it from their perspective?" Whereas I think it's natural, both because when you work inside of a company, you're just thinking internally, but also the way that the metrics are collected inside your application to be more internal-oriented. How many people logged in? Okay, that's a fine measure, but how many people accomplished what they were trying to do after they logged in, is not just necessarily sitting there as a single event in your database. You have to think about it a bit. Another reason why I spend a lot of time crafting a small number of these metrics is, they force trade-offs and decisions.

(00:47:56):
So we could all sit around all day and say, "Hey, I heard all these customer problems, we should build X, Y, and Z." And another person could absolutely reasonably say, "Well, I heard from these customers, we should build one, two and three." And they're all true. We could have a lot of success in both, but the majority case is that we don't build either and we sit around and argue and bicker and we go slowly. "What are we going to do to naturally, organically every day, orient a larger group of people in the right direction and see if our tactics are generating progress over time for a customer from their perspective?" And metrics on the left and a series of tweets on the right is a pretty great combo.

(00:48:42):
Here's an example. A couple years ago I had been working in our payments group at Stripe for a bit, and then I started working on some of our banking and incorporation services. In Atlas, when I started working on it, it had had some success. It had already existed for four or five years prior to me spending time on it. But when I started to look at the support tickets, people were pretty unhappy frequently. They had a DocuSign stuck in their email box. They needed a co-founder's address, but they didn't know their co-founder's address. They couldn't log into the dashboard to figure out their 83(b) manual filing instructions. And we saw this basically in the first week of spending time on Atlas. I was just like, "Just show me all the support tickets. Are they happy support tickets? People writing in being like, 'Oh, I love this service, it's absolutely fantastic. Can you just do A, B, C more for me?' Or are they sad support tickets?" And they're like, "Oh my God, they're all sad support tickets."

(00:49:45):
And so, we're just asking ourselves, "Well, why would someone recommend Atlas to a friend?" I was like, "Well, it would have to accomplish A, B and C activities for them. It would have to get their company, it would have to handle getting their tax ID from the IRS. It'd have to handle all the downstream administrivia." But surely, if they had a bunch of support tickets at the end, they're not going to go tell their friends to use this thing. We could measure all of the intermediate parts, we could measure the success rate and the frequency of incorporation services and we do all those things, but if you looked at the support tickets, there's just no way if you had a support ticket, you would recommend it to a friend. And so, we suggested this metric to ourselves, companies that have no support tickets through the incorporation service.

(00:50:36):
The whole process, from the moment you start the application open, actually the first page load at the very beginning, all the way through the process waiting for the government, waiting for the IRS, and we give you two more weeks to write into support. We give an extra buffer two weeks. And if you get through that whole thing with no support tickets, that's a yes. If you have any number of support tickets, that's a no. And we just looked at the percentage of founders that were going through the service with zero support tickets, which is very different than looking at an average, right? You could have the average as 0.3, but that doesn't necessarily mean that they're getting to 0.2 is going to cause them to tell their friends more. And we looked, and only 15% of founders were getting through Atlas with zero support tickets through that metric.

(00:51:31):
And I just thought, "Okay, well let's just drive that number way up, and let's look at the support tickets aside what people are needing and we'll bake it into the product, and presumably it'll fix it. People will like that more and then tell their friends." And over about 18 months, we took that number from 15% to 85. We basically just flipped it. And you can look at the market share plotted on the same timeframe and it's the same shape. And I think you have to find a measure by which it speaks directly to what the customer wanted, and that if you accidentally leaked your dashboard to them, your customer would be ecstatic to learn that that's what you were measuring the whole time. If we were to showcase the internal Atlas metrics, which we often just screenshot and publish, I think they'd be pretty happy to hear that we were spending all of our time making sure that none of them had support tickets.

(00:52:33):
And it was incredibly encouraging and motivating to the engineers on the team because we could just assign them a topic. "Hey, look at all these support tickets. Why don't you come up with the product spec, the scope, the solution? Oh, want to learn more? Just reply to the support ticket email, figure out what they need." And so, we kind of turned all of the engineers on the team into PMs to go and one issue at a time, figure out what needed to change and build products for it. And that's where we pushed forward on 83(b) elections, automating it, sending in the mail for folks. We built our own signing service.

(00:53:17):
We turned everything into a click. We did just did sort of the obvious things we saw in the tickets, but as the PM, I was able to just sort of, not on autopilot, but really sit back and have content full conversations with engineers who were bringing solutions and ideas for product, rather than one person going through all of the potential ideas, scoping them and assigning them. And because it was based in what people were saying and wanted, it was very motivating for everyone on the team. So somewhat long answer, but figuring out something in which every day we can wake up and look at the same metric and with some confidence know what to do, is so much better than, "Let's figure out what to do each month, and starting from scratch."

Lenny Rachitsky (00:54:08):
I think this is amazing and important advice, just the power of a single metric that everyone on the team can understand, rally around and use to prioritize the work they're doing. I've seen exactly the same sort of impact. Funny enough, Airbnb, one of the teams actually had a metric sort of like this, basically reducing the people contacting Airbnb with support issues. But what ended up happening is, their team started just making it harder to contact support because they're like, "Maybe they don't need to contact support about all these trivial issues, so maybe let's encourage them to figure it out themselves." Is there anything you've learned about to try to avoid these kind of second order effects that are of perverse incentives of a metric?

Jeff Weinstein (00:54:47):
We look at multiple metrics, but we will optimize around one and you have to use your own judgment to look at some of these countermeasures and pick them. We would also, that would sort of be our overarching metric for a year, but then we would pick specific tactical metrics about how we would accomplish it. So just an example that both is how we solved a problem, but also it's just a style of metric that was useful to us. Of course, some of these support tickets included things like, "I'm waiting to hear back from Atlas about, if they're going to approve my application because Stripe is required for very good reasons to evaluate certain business types, or sanctions, lists and the worldwide products." So there is some, should be incredibly quick, but there is a bit of a review process, and of course if you were not hearing back from us, you would be upset because you're trying to make your company immediately, "This is ridiculous. Let's get back to us quickly."

(00:55:59):
And so, we knew that one of the reasons that people were writing to support was like, "Hey, what's up with my review? What's going on?" And we knew that our tactic was just to drive up how quickly we got to a final decision on folks and to reduce the number of overturned rejections, where someone writes back in saying, "Hi, come on, I'm totally just making something reasonable. What's up? Why did you reject me?" And so, we would pick these overarching single metric, which was the companies with zero support tickets, but then we would have a specific KR that was owned by an engineer, which is the tactic that we're going to do. And so, we would not allow ourselves the perverse tactics to sort of just casually exist. We would choose which tactics we're going to do and then set a metric for it.

(00:56:49):
And the other reason I love this metric is, it's a cohort metric by which you're trying to drive something up into the left. Sometimes people will get excited about a chart that goes up into the right, it's kind of a meme, "Oh, that's going up to the right." I'm really excited about charts that go up into the left. So you have to figure out some optimization that you're trying to maximize. And so, in this particular case of this risk review, we would look at, "Hey, for the cohort of customers that started last month, how quickly did we get them to their final risk review by number of days since they submitted?" And so, you want a chart that looks a lot like, "Here we go, right up to the top." Because you want 100% of your customers to get their final decision as quickly as possible.

(00:57:44):
Wouldn't you know it, when we looked at the chart, it was doing this. And so, each month we would just make it a little better, a little better, a little up and to the left, up and to the left, up and to the left. And now basically 100-ish percent of people get their risk review within an hour, from a long tail taking a long time. And so, we would constrain the tactic through a metric and then watch it through an optimization function. And then when we got to a point where we were happy with the target, we could put down the tactic. That's another really useful thing about metrics, you can decide when to stop a tactic because you get to some level of success that you're comfortable with and you can always choose to pick it back up later.

Lenny Rachitsky (00:58:23):
So there's some really cool lessons here of just how to pick a good metric. Just to kind of maybe summarize what I'm hearing is, you kind of worked backwards from essentially NPS, like, "Why aren't people recommending Atlas?" You found, "Okay, well people that are complaining and having issues with support and running into problems, most likely are going to be detractors, not going to want to recommend Atlas, so let's have those really ambitious goals. Eventually nobody has a support ticket/let's just track how many people have zero issues." And then you identify, "Okay, what's driving a lot of these support tickets? It looks like this risk timeline till they get to this certain milestone, let's make that our goal for the next quarter or whatever, and let's focus there and then make an impact." And then I imagine move on to other levers within this bucket of zero context.

Jeff Weinstein (00:59:08):
You have to pick the right metric for your audience in... I wouldn't wouldn't fully export that metric to everyone. That was not a terrible one to export, but in the founders choosing where to get started mindset, again, this isn't just deeply spending time listening to your customers. They all ask their friends, "Hey, how did you start your company?" They want to talk to an older sibling of sorts about how it went. And so, we decided that our go-to-market strategy would be to delight our current customers such that they would tell their friends. And other businesses, that's always somewhat useful, but you can also reach people with billboards and Google ads and other types of upsells. That's very difficult in the moment that someone is starting a company that's sort of a National Geographic, can you get the picture of the bird at exactly the right time?

(01:00:10):
How are you even supposed to go find people who are about to start companies? Thankfully, they have this practice of just asking their friends. And so, if their friends loved it, they're going to just recommend it. And that has the metric and the tactic and the go-to-market all lined up, rather than sometimes in cases you might hear someone say, "Well, let's make the product quality better." Well, we all make the product quality better, but why? Why is this actually going to move what our customers want, and the business board? And when you can line them all up, it can be quite beautiful, especially when you can see it month-over-month for a long period of time. One other metric I think that I would export to anybody, is if you are unsure what to measure, we have this, I don't know if we stole it from somebody else or if we came up with internally, whatever, is just users having a bad day, where we will just emit a log line anytime we think that a user bumped into a problem.

(01:01:14):
So maybe they hit a 404, or maybe their payout was one day after the ETA, or they had more than 10 payment declines, you can kind of brainstorm again or just listen to customers, what would cause you to personally have a bad day, and then just emit an event when that occurs. And then you could just make a stacked bar chart of all the bad day reasons and the frequency by which they're happening, and it's eye-opening to see those frequencies. And it's kind of a metric I hadn't thought about until Stripe's scale, in which you just don't know what's happening until you emit the log line and count it. The frequencies could be...

Jeff Weinstein (01:02:03):
... emit the log line and count it. The frequencies could be kind of mind-blowing. And I think for almost any scale business, if you are bored one day and you're not sure what to measure, just make a user having a bad day chart, emit a log line and count it as a bar chart and then anybody else can add their own bar chart on top of it. And so, it's become a way for teams to scale their understanding of users through metrics by just saying, "Hey, look, anytime anybody has an idea about why a customer is having a bad day, just emit a log line, put it on this chart, and then we can choose over time which bad day reasons we want to burn down and hopefully just eradicate them, not just minimize them.

(01:02:41):
But it gave us kind of a background noise counting system for where there are problems and anytime there's an incident or some customer issue, the first thing I think is, "Ooh, I wonder if we have a bad day reason for this." And if we do, I actually feel okay. I'm like, "Oh yeah, it is a bad day for this customer." I wish I didn't have it, but at least we're aware and we can evaluate it against other bad days that we want to burn down. What does sometimes a little bit grind my gears or gives us an opportunity is like when we didn't know about that bad day. And it's a surprise to us too, that is for me is immediate action. It's like, okay, cool. We have to figure out a way to count this bad day. We got to get it on the chart. That way we can make an informed decision about when to invest improving it.

Lenny Rachitsky (01:03:35):
And I love this idea. I haven't heard this before. So the idea is just make a list of what happens to a potential customer that would cause them to have a bad day. What are some examples for Striper Atlas that you guys have?

Jeff Weinstein (01:03:45):
Are you a Stripe customer, Lenny?

Lenny Rachitsky (01:03:47):
I am with my newsletters. The payments go through Stripe. I check my dashboard every day.

Jeff Weinstein (01:03:52):
Cool. So what would be a bad day for you?

Lenny Rachitsky (01:03:53):
Oh, I see some silence happening here. It not loading. The numbers taking a long time to show up. Something being completely off in there, not being able to log in. The silence is good. I just want to keep going.

Jeff Weinstein (01:04:19):
The question is how much to the audience is how much of the silence will we edit out before it goes live? But this is what I'm talking about, right, is I could guess them, right? And as you were saying those, I know the URL of those charts. I know the login one because I feel that too. So I play with Stripe all the time and then you get a two FA too frequently and come on, I had the same cookie. I was just here yesterday. So we count all that stuff and try to make it better over time. But I'm so excited when someone brings me a new bad day I hadn't thought about yet because that's like product cabinet.

Lenny Rachitsky (01:05:00):
I love it. And your advice here is this doesn't necessarily have to be your goal or metric. It's just watching this thing that could lead to a lot of interesting ways of operating.

Jeff Weinstein (01:05:10):
A couple other just like quick metrics things because it's a bit of a... I don't know, some people like cycling or something. I guess, I like metrics. People get a really nice bike. I want a really great metric. Picking metric titles that make you feel something. So we could have called that measure of companies, number of companies that do not send a support ticket over X period and Y period with min... You sometimes see these charts where the metric itself named itself. This is just companies with zero support, that's it. And the brevity and the focus and the customer mindset built into the chart name can become currency inside the company. It's like, oh, I'm working on making this chart go up and it feels good to just say the name out loud rather than some complicated underscores and mins and maxes and the database field name is still in the chart title.

(01:06:26):
These are aesthetic choices, but I think make dramatic differences in the cultural willingness for people to buy in and get excited about it and reduce the need of a product person to just remind everyone every day why they're doing it. It's like the metric is motivating us because it's a motivating thing to talk about. And then lastly on metrics is there's just good hygiene that people should bring to their measures. Percentages shouldn't have 41 significant digits if only two of the digits are relevant. You should keep all the measures of your dashboard on the same X-axis. These are just stylistic things that increase the frequency that people want to just wake up every day and open the dashboard and look at it. And that is so powerful if your whole team is looking at the same set of information that has the heartbeat of the customer every single day.

(01:07:26):
In fact, we can measure at Stripe the usage of our dashboards by team, and so we can see which teams are themselves looking at their own metrics and that is an incredibly useful predictor of how on the same page they are and how customer obsessed they are. So I just think it's not an area that's sort of behind the scenes, bean counting reliability is the machine hot. You can make metrics that mean something to the customer and you would be proud if they were to be screenshot and put on the internet and be like, "Wow, I feel like that company is taking their promise to me seriously. And I can see myself on those metrics as a customer." That's where we're really shooting for.

Lenny Rachitsky (01:08:18):
So [inaudible 01:08:19] back what you just said there, which I think is a subtle point potentially, is just making the dashboard look nice, like the hygiene of the naming conventions and the decimal points and the chart. In your experience, you find that really powerful and important.

Jeff Weinstein (01:08:34):
A couple of years ago, Stripe did internal work to make an internal metrics kind of dashboard system. And we have a special place called Go Metrics. Many people use a go/service where you can just quickly go to a URL. And again, I have to sometimes do a rule rather than a policy. My rule is if it's not on Go Metrics, I'm not going to look at it. So if people can send me one-off queries or charts or screenshots or presentations or emails of charts and data, but that is in the wind, we can't interrogate the query metrics are almost always wrong. For many weeks, we didn't quite get the definition correctly. You have to live in the metric for quite a while before you really believe in it. And so, if you're always looking at some one-off version, it's just very difficult for it to rise up to the level of importance that is a thing we should trust to help us decide what to do. That's an incredibly high bar. And so, I just find you have to look at it frequently enough.

(01:09:46):
And if you're going to look at it frequently enough, it means it needs to be in a discoverable place. You almost go through a couple stages of grief about it because we'll kind of put a metric up in a place and everyone initially is like, "Wow, this is great. I was so excited to finally see this." And then a couple of days later, "I don't quite understand it. What does it actually mean? I saw this other metric from this other angle that kind of makes it feel counterintuitive that it's like this." And then you kind of look into it, "Wait a second, we've been counting it wrong the whole time. Oh, no." And then you look at it the third week and it's a completely different version and then you hope that we forget about it and maybe we'll go onto something else and nope, we're not going to forget about it. Week four comes around, you're like, "Wait a second. Okay, this is..." Then the team meeting starts, "Hey, just a reminder, let's just bring up the metric again, not a screenshot of it. Go to the URL."

(01:10:39):
And just that level of frequency and specificity and ritual around it is what brings it into the decision-making culture. And again, we treat it the exact same as we do tweets. It's the quantitative and qualitative right next to each other. And because you're putting that amount of attention to it, you can't have a 1,000 metrics. We just don't physically have time the day to bring that level of care and understanding to so many things. So then it forces you to know so many things you could care about down to a small number of things that you really must care about. And again, that practice goes back to do you really understand what your customer wants? And so, for all these tactics, it's about finding out what your customer wants and then different versions of how do we sort of know it's true over time and our tactics improving?

Lenny Rachitsky (01:11:32):
It sounds so simple when you describe it that way. This episode is brought to you by Anvil. Their document SDK helps product teams build and launch software for documents fast. Companies like Carta and Vouch Insurance use Anvil to accelerate the development of their document workflows. Getting to market fast is a top priority for product teams. And the last thing that you or your developers want is to build document workflows from scratch. It's time-consuming, expensive and distracts from core work. You could stitch together multiple tools and manage those integrations. Or you can use an all-in-one document SDK. Most product managers will tell you paperwork sucks. Anvil's document SDK helps teams get to market fast, incorporate your brand style and give you back time to focus on your company's core differentiated features.

(01:12:24):
For your users, paperwork often starts with an AI powered web form styled and embedded in your application. From there, you can route data to your backend systems and to the correct fields in your PDFs via API. Complete the process with a white labeled e-signature. The best part about Anvil is the level of customization their SDK provides. Non-technical folks love Anvil's Dragon Drop Builder and developers love their flexible APIs and easy to understand documentation. Build documents software fast with Anvil, that's useanvil.com/lenny to learn more or start a free trial. That's useanvil.com/lenny. Kind along these same lines, there's something that I've learned you started at Stripe to help people obsess with user experience and get quality to where it needs to be and move a lot of these metrics, something called Study Groups. Talk about what that is. I'm very curious.

Jeff Weinstein (01:13:19):
Okay, let's imagine we understand our customer, we've understand their burning problem. We've built a solution that's in their hands, they're using, it's hopefully better than their alternatives and they're starting to use it and we have some real traction. You could still measure the success, you could still look at the tweets and then, of course, you go to pick it up yourself and you're like, "Wait a second, this thing is horrible. How did it get so bad?" Anyone who's built a product that has gone over the horizon of it's actually in production and being used for a year or more as you go to iterate on it, especially when you're in a larger company and there's multiple teams and multiple products going on, there's just some entropy in the world that causes these things to go bad. I actually have a hard time naturally explaining it.

(01:14:13):
You kind of think to yourself, well, it's code. It just must be running the same every day. But somehow you do enough things in a row. And what was once a smooth end-to-end flow for accomplishing a test or a customer is all of a sudden some Byzantine complicated broken mall where all the doors are busted and you have to know exactly the way to get through the dashboard to solve your problem. "Wait a second, I thought this was great just a second ago." And many of us have experienced that. Now, okay, what are we going to do about it? Well, one is it is really difficult to take time during the day to allow yourself to even know that this is true. Because if you're working on one particular team, you're going to have some next thing you're shipping, you're going to have your customers, you're going to be doing great product work.

(01:15:14):
Meanwhile, your current thing kind of starts to rot in the world and decrease all the trust you've earned to build what you're building now. It is actually difficult to decide, well, what hours during the week am I going to block off from my future progress to see it from the customer's perspective today? And there are various techniques to try to incentivize or to structure a group of people to do that. Stripe has a thing called friction logs as well, which is a single individual will pretend to be a customer and go through a product experience end-to-end and write it down. And that has been quite successful at Stripe for very motivated people who can block off the time and have the wide enough context to do a complicated thing end-to-end and have the time to write it up and the position the company to send it out as a critique potentially to not just your own team but in a whole organization.

(01:16:31):
So that's actually a pretty high bar to crossover. So I was kind of brainstorming what could we do to make this more fun and have the frequency which we're looking at our own products dramatically increase? And we kind of iterated few through ideas. And I landed on this thing called Study Group, which is basically a random group of people inside the company. They might not work on any particular team. They might not all be PMs, just like literally anyone who wants to sign up, a support person, a sales person, someone who's on our events team, an engineer and our infrastructure stack. Anybody can sign up for a Study Group. We show up maybe four to eight people total. We pretend to be some company with some outcome problem. Maybe we want to accept money in person at an upcoming farmer's market, or we want to run a multi-country global business where we have software that another business would use to run their business. If it was something quite complicated.

(01:17:38):
We could pick any motivating goal. And there are two rules to Study Group rule one is you do no longer work at Stripe. You do not work at Stripe, not pretend, don't work at Stripe, not try to forget you do not work at Stripe, you've never worked at Stripe. You work at... And we make up a name of the company, Dolphin Aquarium Industries, and we will pick a CEO of the company from the group amongst us. And okay, Jenny is the CEO. "Hey, Jenny, what do you want to do today?" "Well, I want to sell in-person tickets to the Dolphin Aquarium." It's like, "Cool, where would just start?" So we actually embody the customer. We will not break character, it's a little bit of the improv thing and as the kind of maestro of Study Group, I will firmly but kindly, if I hear you use any internal Stripe knowledge, which is natural to do, because, well, you worked on a team and you know where that button really is.

(01:18:41):
And the docs link goes a little bit to the wrong place, but if you click the other link, you'll get to it. If I can see you use any internal Stripe knowledge, I'll just pause and say, "Hey, let's redo the sentence or redo what we did with no Stripe knowledge. As a reminder, you don't work at Stripe." And it takes us a couple of times, but people really get into it and all of a sudden we'll start making up characters and the CEO will be like, "Oh, Tim, you're our designer. Where are we going to get the color palette?" All of a sudden there's a person who's not a designer in real life is now all of a sudden having to practice the empathy to be in a customer's position. And because we're going to be doing it for an hour, hour and a half at a time, you actually start to believe that you don't work at Stripe and you work at Dolphin Aquarium Industries and you start to really feel it.

(01:19:34):
So that's rule one. You don't work at Stripe. And rule two is we're not here to solve any problems. We're not here to critique, we're not here to solution or suggest, we're not here to file bugs. All of those things is recorded. We can do that later, whatever. This is just about practicing empathy for the customer and going through the product. And we have done more than 25 of these at Stripe thus far in just this year, last few months of 2024, more than 250 people have participated in the Study Group. And it is deeply eyeopening for those involved. The responses are sort of business emotional, not super emotional, but just, "Wow, I can't believe how hard it was to accomplish X, Y and Z. I thought we were amazing at blah." It's like, "Well, we actually are still pretty good, but we need to get back towards amazing" or Wow, "I didn't even know that internally people wouldn't know that our products did 1, 2, and 3."

(01:20:45):
And this has become so internally popular that teams have adopted for themselves. And so, we've kind of franchised Study Group internally already where different teams will run it. But I think we're going to continue it because I think a little bit is coming out of the pandemic. People just want more group activities. I think some of it is the slowness by which we do it. We're not rushing through it. Which another reason I appreciate your podcast as well is let's really get into the details and not be rushed for time. You forget that you have a meeting at the end kind of amount of time. No one is to blame or defensive because it's not your product at all. It's a random group of people. We don't even introduce ourselves about what team we worked on. We're just all here as participants to embody the customer. And then I think lastly, a reason why it's worked, and these are many of these just been actually super surprising to me.

(01:21:39):
I wouldn't have been able to prick ahead of time, is it's just fun. People want to make up the name of the company. They're excited about what Dolphin Industries would sell. A person who's not a CTO in real life gets to pretend to be a CTO and there's little theatrics to it, but it has been different enough from our other approaches for a company like Stripe, which is already pretty focused on this topic, that we think that there's enough legs here that we're going to keep it and kind invest in groups pretending to be the customer and going through it painstakingly slowly rather than only demos or only writing, which has other benefits, but misses the participation of a larger group and more fresh eyes. So it's been fun and we named it Study Group. I guess, I named it Study Group because I wasn't sure it would be initially. So I just came up with something that sounded cutesy, but gave me enough leeway that we could kind of adjust it over time. And this is where we've landed.

Lenny Rachitsky (01:22:56):
It's fascinating that there's so much theatrics and ceremony necessary for a product team and a company to find out these things about their product. You would think people are like, "Oh, we know how onboarding looks. We know all these things," but basically what you're saying is you don't, and you need to do these sorts of things in order to really know what your product is like these days.

Jeff Weinstein (01:23:20):
The customer does not live in our walls. They aren't. They're not here. They don't know our lingo. And it is just so natural for our internal mindset and lingo to flow into the application over time. And you need some counterbalance to get there. And I think it has to be an unnatural counterbalance. It used to frustrate me actually more like, "Wow, why aren't we doing this?" Well, we're actually doing great work to move something forward and we have our local optimizations. It'd be difficult to get to this level of specialization that multi-product companies are trying to do without that level of focus on a per team basis, but then you need something unnatural to help us bring it back.

(01:24:12):
And so, I'm constantly looking for non-punitive fun ways objectively to get more perspectives from the outside in. If it's breaking the fourth wall to get on the phone on Twitter, if it's looking at a metric of users having a bad day, which is just like counting what's happening, you can't argue with that. Or a random group of people just kind of scratching their head trying to find a button, those are truths in the world that we're trying to make sure are inputs to all of our teams. And if you don't have those inputs, I can totally naturally see where the entropy of the world leads you to have Frankenstein bad products, even when all the individual parts are well oiled and run by great people. So you need something unnatural.

Lenny Rachitsky (01:25:06):
There's an interesting trend and thread through our talk so far broadly, there's just an obsession with making something great and awesome. And then a layer below is just an obsession with the user experience being as great as possible. And for a lot of PMs, there's not a direct line between make the experience as amazing as possible to growth and revenue and success and things like that. And it feels like for you and for Stripe broadly, there's this innate implication. If we're making the experience better and better and better, we will grow. You're nodding your head a little sideways a little bit, so I'd love to hear just your thoughts on just this obsession with experience and user issues. But we also have to go to the business. What are the metrics are moving?

Jeff Weinstein (01:25:51):
If someone else has a strategy for moving revenue that isn't getting it from customers, I want to know about it because it's so hard to get it from customers. If there's some faster path, please tweet me and tell me about it because this is very hard, a lot of work to do. So if there's something else, I want it on the table, but I often find it's part of the product experience. So maybe it's internal sales tools. We can do a Study Group about our internal sales tools process and our deal desk and our margin structure. We can do a friction log on our third party vendor process or a migration service or the way an ecosystem partner helps deploy our services into a big enterprise. Nothing is sort of off limits from product. In fact, I was chatting with a friend who runs the company and they were small company on the verge of product market fit starting to feel, customers starting to pull and they're like, "Oh, but our self-service funnel, it's so leaky and we have all this support coming through self-service."

(01:27:03):
First of all, congratulations, unbelievable that they're going through your product, even attempting self-service and contacting you. The majority case would be no one tries or they try and fail and don't contact you. So again, what a problem to have. And two, they wanted to minimize the support. In that particular case, it's like, "Well, what's actually in those support tickets? What's in those sales? Those are really sales contacts." They're like, "Oh, they want to learn more about how they get started." They want to know the expertise about... This is a particular company, it's a healthcare related company. They wanted to know the healthcare choices available. They wanted to know how to migrate from some old system they had to it.

(01:27:41):
I was like, "That's the product. The thing you're talking about is the product." Turn those moments during your self-serve process into not self-serve and make the product experience be let's get you on the phone. And now when they get on the phone, they know the first name of the person they're talking to because they have it from the onboarding forum and all of a sudden it feels like you are still in the product, but it's not software. Now it's a person, but it's a person backed by internal software, which knows as much as they can about the customer and what they want. And I was really inspired by Fidelity, which is a big financial institution where many people listening might have switched jobs and had to move their 401(k) or something like this from job A to job B. Maybe in some universe it'll be three clicks, but not today or certainly not when I tried a couple of years ago. You got a call and go on a phone tree and all the shenanigans, and then I got on the line with someone from Fidelity. They're like, "Hi, Jeff. They knew about the old company. They confirmed my address." They said, "By the way, this is not a digital process yet. We're going to FedEx you an envelope and inside it is going to be the thing for you to sign. Here's going to be exactly where to sign. Here's a picture we're going to sign. We've put another envelope inside that envelope ready to go. And so, you just take the papers from envelope one, sign them where it says and put them in envelope two and put it back to the [inaudible 01:29:16]."

(01:29:15):
It's like, "Wow, that is product." That is a product experience where I think some people would say, "Oh look, the product experience has to only be in software." So I feel when people think, oh, product quality and craft has some limit towards business value, there's some asymptote that you have to be like, well, kind of product plate time quality is over. We need to talk about business. It's like, let's figure out exactly what is causing the business to happen and make a product, even if it doesn't look naturally the same as our SaaS, software, browser, mobile, whatever versions. I think we can see the entire experience as it. And from there, I include the sales process, I include the support process, I include tools that help with compliance and everything else. And again, if people have a way to make all those things bad and lead to great increasing revenue over time in sustainable ways, I want to know about that because that sounds so much easier than the version that we're trying.

Lenny Rachitsky (01:30:23):
I love that and clearly it's worked for Stripe. Just one last question. I want to talk about Atlas and dive into just like what is Atlas and how is it doing and things like that. I know there's some new stuff coming that you're going to share, but one last question about Study Groups. How do you decide what product you're going to pick to do a Study Group on? And then what is the expectation with the result? I imagine there's a PM sitting around like, "Oh my God, I just got this 10 page report on all the problems."

Jeff Weinstein (01:30:48):
So initially, I just made up a list of stuff that I thought would be fun to Study Group to kind of kick it off. And now, because it has a bit of an internal brand and it's exciting, and people who have gone to a Study Group say nice things about Study Group there, they actually proactively say, "Hey, we should Study Group blah," or "We're launching something next week. We should Study Group it before it goes out the door." Or now I actually just have a huge backlog of things to Study Group based on what people want. And now we're again franchising it. So we're going to have Study Group captains and people run their own Study Groups, and so we can really scale this behavior. But we did our first Study Group of an internal tool recently. And so, that I think is going to catch on just anything at all can be Study Group. It just takes about an hour and a couple of people and you open up the Zoom and that's it.

(01:31:37):
And then for expectation wise, look, it is so tempting to put more regulation on something. Okay, well, everything coming out of this program needs to be scored and rubricked and have SLAs. That is extremely reasonable. As some of these next steps, we do notice things that are of serious issues and we have some formal processes inside of Stripe for elevating bugs to certain priority levels that get tagged and have SLAs for teams to acknowledge and review. And so we kind of funnel the outputs of a Study Group into our already existing formal processes rather than having some new special thing that's going to bother a particular team. I will say though that it is difficult to watch one of these Study Groups and if you are the team involved in some piece of it and not want to act on it, because seeing your fellow teammates struggle to use your thing in some way is more motivating than the customer because you can kind of always say to the customer, " Well, they didn't really know," or "They have some special setup."

Jeff Weinstein (01:33:03):
Well, they didn't really know or they have some special setup. You probably shouldn't say those things, but you can kind of rationalize it, whereas a group of people incentivized to have actually accomplished it, who got together to do so painstakingly slowly not being able to do so if that's not what excites you as a product person to want to solve, this thing's not for you. But then again, you have your own organization system, you have your own things you need to ship and study group doesn't have a mandate that comes from it. We have our own. It's more of a cultural piece of information that is very high signal and then people tend to use that high signal for good prioritization. I will say though, that we have added the SLAs to certain bug levels that begin to match a bit of our incident process.

(01:34:01):
So in an incident strike, like in many companies, pencils down, fix the problem, severity levels, non-negotiable Slack rooms happen, war rooms, all that stuff. You don't want to do that with every single bug, but we have a rubric of craft related tags for our bug system. And if it is a sort of a P0 bug, which is not an incident, right, it doesn't mean to put down your pencils. You do need to acknowledge it at Stripe within seven days. And even if it doesn't mean to fix it, it's like a person looks at it and says, "Hey, we're going to do it or not do it." That's a still pretty strong bar for a non-incident related craft issue.

Lenny Rachitsky (01:34:45):
It feels just at Stripe, there's this cultural focus on we want to make the product great, we want to make the experience as great as possible. A lot of companies, it's just teams. We have this goal. We're not going to do anything that isn't driving this metric and goal that we have. And I think for teams like that, it's hard to hear just like, oh, someone's going to send you all of these problems that you experience. There's the negative version where the founders goes through the product like a CO of a larger company, just, oh my God, look at all these problems. You need to fix these immediately. And a lot of times it's completely distracting from the things they need to do, the goals they're trying to drive, things that really, really matter that the CO may not be thinking about. And it feels like you're trying to find this balance of here's problems that exist. You don't need to fix them. You probably should. Here's the most important stuff. But also there's often you find a correlation between make the experience better, you're going to do better.

Jeff Weinstein (01:35:37):
There's a huge amount of trust here involved in your colleagues, which is we want to provide teams great information and the best teams welcome that information. It doesn't mean that it comes with a auteur opinion from the outside world that says you must do X. We have a rubric on some of the craft related bugs, but again, we let the teams relabel them. And so maybe it's actually not a P0 from their eyes and that's the trust we put in the teams. I think that the failure mode is when you don't look. And so we need unnatural, safe, fun lore that gets us out of our chair and into the customer's mindset. Best is if it's you and you're your own customer, okay. Second best would be sitting right next to the customer in the outside world and then like, okay, fine, I'll take a third best, which is pantomime the customer and enforcing you don't use any internal knowledge. If you have practices in those three categories, I'm comfortable with the failure modes.

Lenny Rachitsky (01:36:56):
I love that. This is definitely going to be the longest episode I've ever done, which is exactly what I expected and I'm happy that we're doing this.

Jeff Weinstein (01:37:04):
Everyone go 1.75X or something.

Lenny Rachitsky (01:37:07):
I like when people are like, oh, this episode is really good. I had to slow down to 1.75 or something. How are you even listening at that speed? No, it's 1.0 speed. That's what this episode needs to be. There's two more areas I want to spend some time on. One is Atlas. We've talked a lot about on the surface of Atlas. I want to help people understand what the hell it is and the stuff that's happening there. And two, I want to talk about getting stuff done at a big company, something that you've done at Stripe and I hear you have a lot of good advice on. So first of all, what is Atlas? We've talked a bit about it. What's the best way to understand what Atlas is and who it's for?

Jeff Weinstein (01:37:42):
In 2016, a bunch of Stripes were traveling the world, Stripes is what we call teammates here, and they're just hearing stories from entrepreneurs around the world. And you would hear this unbelievable story from incredible entrepreneurs who have a laptop, which is that they'd have to fly to the United States on an airplane to make a US company in order to get access to use financial system, to raise money from US or global investors, often to take USD or to charge US customers. And you could have sat around and said, huh, is that illegal? They don't live in the US. Can they have a US company? Absolutely. The US loves this. It is incredibly encouraged for people from around the world to make a US company and many people do.

(01:38:38):
Now, why did it require an airplane, right? And so you start to hear that kind of thing at a coffee shop amongst someone with a laptop who has access to the whole internet. And that is a burning problem. Right. That is not a tier three issue. I am not able to run my business without getting on an airplane should be sending alerts off in your whole psyche that you have discovered something important. And so I wasn't at Stripe at the time, but I'm very thankful that, I was running my own startup at the time. I was very thankful that the people at Stripe decided to try to tackle that problem. And so Atlas is a way to start a company in a few clicks, and we think that's an incredibly big deal because while there are smart humans across the whole planet, the opportunity that they have is not uniform. But it's a little strange because it's all the same MacBooks and it's a little strange because it's all the same IP addresses and we all have plenty of bandwidth and smarts.

(01:39:49):
And so what can we do to dramatically lower the barrier to great people solving problems? And we've found over and over again that increasing the ease and simplicity and decreasing the cost and complexity tends to lead to just more of that thing. And we have a fundamental belief that there should be more startups and they're not finite. And that belief comes from both just a core hope because there are so many problems in the world that don't seem to be being solved fast enough by our current institutions and larger companies that we think will actually, we need entrepreneurial energy to tackle them. And then it's also comes from experience of seeing it happened. Instacart signed up for Stripe with a Gmail address and then Covid happened and they delivered critical food to everyone when people were reasonably not allowed to go to the grocery store easily.

(01:40:53):
So you just don't know what the next Gmail address is going to do. And so in Atlas, we radically try to simplify the process of getting a company started and that mission has taken us to just solve more of the problem over time. And so over the last few years, for those who have either used Atlas or have started a company or maybe follow along on Twitter a bit, you might've seen just a progression of complexity that used to exist being automated. And so a big one that we did about a year ago was this 83(b) election, which is this absolutely Byzantine silliness system by which you have 30 calendar days to send a one-page document to the IRS that could radically change the economics of how you are incentivized as a founder. And this is not one of these greedy loophole. The IRS in the 1980s made this IRS rule in order to spur more entrepreneurship.

(01:42:07):
They want this. And the only issue is they made it extremely difficult to accomplish. You have to send a snail mail in to an IRS address in a particular format, in a particular way with no verification that it happened at all. And if you do it 31 calendar days, there's no redo. Okay. Now again, if you're a product person, you hear the founders terrified all day long about this same issue, just alarm bells in your head whole time. And so I had experienced it for myself as a founder several times, and I also just heard story after story and I just put on my to-do list for the team, we are going to solve this 83(b) election thing. And there are very good reasons not to do it because it comes with potential huge liability. Don't want to screw it up, it's snail mail.

(01:42:54):
You're really going to monetize this. It's a competitive advantage to do it. You can kind of argue yourself not to do it in a million ways. But again, back to the mission of just taking all of this complexity and turning into a single click. It was obvious to us and we got started on it. Infrastructurally, we've been automating these steps and when this podcast airs, I guess today, it will be true that when you go to start a company on Atlas, it will just be a single click.

(01:43:26):
You go to type in your friend's names, what the name of the company will be, it'll tell you if it's available automatically or not. You can split the company up 50, 50 or whatever you want to do, fill out a few things and you click go and then like a burrito coming to you, like a pizza tracker, we will just handle all of the downstream activities that used to be, hey, remember to come back in and purchase your shares. Why am I purchasing my shares? I'm just getting started. Why am I writing a check for $10 and putting into a bank account that I can't even open yet? And then I have to wait for that to be done to get the 83(b) [inaudible 01:44:09]. All of those steps are now just handled in the background so that we can get you ready for business in a day or two.

(01:44:17):
And so this is our vision. So you can quit your job on a Sunday night, get the Sunday scaries, I'm done with this thing, and on Monday morning fill out this form and the next day be able to run a billion-dollar business because we will have automatically handled getting you access to banking systems, to payment systems, to handling all the equity paperwork, filing your 83(b) election where you can just shift from having worrying about the company starting process to just building and shipping.

(01:44:52):
And you'll just get kind updates in the background. Cool, the IRS is giving you a tax ID. Cool, your 83(b) election is filed. Cool, all the founders have their equity and you're ready to go on the cap table. And we've done this by deeply integrating with the governments and deeply integrating with banking partners where we can get you access to the financial system before the IRS and the other governments come back with their sort of official yeses because we take care of the problem in the background by which we're faxing, phone calling, filling out forms on your behalf. And so we just want to take all that complexity and just erase it so that you get the same thing the YC group gets when they start, that checklist that they go through. We just have the robot do exactly the same thing.

(01:45:45):
And so in some ways it is a really big deal in a big ship because it completely automates the company starting process. But in other ways it's an incredibly incremental step that it's taken us three years to get to where we had to systematically automate the internal steps, each one and now we've done the work to wrap it all up into one button. And you can just watch how your company's doing in the dashboard.

Lenny Rachitsky (01:46:16):
Well, first of all, congrats Jeff and the Atlas team on shipping this. I know this is a big milestone and it's been a long time coming.

Jeff Weinstein (01:46:21):
Yeah, Atlas was actually a little reasonable before we decided to do all this work. It's like why do this next step of completely automating it when it was actually fairly straightforward before. Atlas has above 80 NPS, which is quite high. Apple is in the low 60s, AirPods is 75. I love my AirPods. So Atlas in the 80s with almost 50% response rate is quite high. And so we still chose to do another year of work to automate all of this work behind the scenes because we see that companies are charging their customers sooner when they go through this automated process versus waiting. And it's a little strange. You just started your company. Well, what does it really matter to wait an extra seven days or 20 days before you can really get going on business? Those are really fragile days which you're building. And to some of our conversation earlier, that amazing feeling of getting your first customer and being in it with them and money actually exchanging hands and getting that relationship.

(01:47:34):
If we can slide that forward in the world by a couple of days or weeks, which we're seeing, like half the time it takes to get to your first customer, just shave a whole week off of your company and you can kind of see GDP being born sooner. And went my whole life knowing that okay, GDP is not finite and it can grow, but I've never really seen it and now I've actually seen it grow faster, sooner. And I think anything we could do to just move that forward is going to inspire and lower the bar for more people to be an entrepreneur because they'll see how satisfying that can be.

(01:48:21):
And another stat, which really was interesting to me recently is that we have seen since doing much of this automation work, that more solo founders are using Atlas than ever before. And I think it's because you can just do a lot more on the internet as a founder with no-code tools and everything else and get going. Very cool to see that bringing the best of the internet and making it available worldwide can be correlated with more people becoming entrepreneurs. And I think we should just keep doing that.

Lenny Rachitsky (01:48:55):
It's incredibly inspiring and I think this is going to be a huge deal. It's hard to think about how many, what sorts of changes in tech could transform how many companies are started and how many companies not just started but actually happen because to your point, you may start and they're like, nah, nevermind a few days later if it's still stuck in some queue.

Jeff Weinstein (01:49:13):
Totally. And then you don't know where these things are going to go. We have the sort of cohort of 2024 startups in Atlas got to $50 million in revenue twice as quickly as the cohort in 2023. And so we kind of also think sometimes, oh, it was the pandemic that pushed everything online. Those are our best years. It's like we're seeing the earliest cohort charts of new startups just cracking up into the right. And that's very exciting because you also hear sometimes, well the funding market is down and valuations and this and that and the other. That is much more of a point in time capital analysis and much less business, like just how businesses are working day to day. It's really in the revenue that is representative of their futures and that looks amazingly bright.

(01:50:05):
And then of course these companies go off to do pretty wild things. Companies that have started through Atlas, there's been 55,000 of them to date are doing $5 billion a year in revenue. I think it actually resets their expectations of what other tools will be in the future. It's like, well, if it was so easy for me to get my company started, well why is it so hard to do banking? Well, thankfully there are some great services for it, but I think if we can push people towards expectations higher, then they will want to make their companies better and we'll just all benefit from that.

Lenny Rachitsky (01:50:38):
How much of this is based on you guys sending faxes and sending mail yourself, like I don't know how much you can talk about the behind the scenes, but is there a lot of, through this ops element to automating some of this?

Jeff Weinstein (01:50:51):
Atlas is in total 10 people, which is I think a relatively small group for the role that it plays in the wider startup ecosystem. And we just don't pick up work we can't automate because we know that we need the leverage. And so we're not going to put ourselves in situations in which we have to compete to be the best. We're going to put ourselves in situations where we can automate it and be the only, and that's a different mindset. So in terms of why we picked up 83(b) election as a topic, when we made that decision, we made a commitment that we're going to do this forever. We're going to do this forever. This is a piece of infrastructure for the rest of the internet. That is a very high bar to set as the thing you're going to do.

(01:51:50):
And so we're happy to take our time. This is part, versus like go-go-go versus the long-term compounding. Go-go-go was when we assigned one engineer, hey, it's your job today to send one piece of paper to the office with this third party mail service. Why? Doesn't matter. Today, just send a single piece of paper to the office and an incredible engineer, and she went on to lead all of 83(b) election work. She sent it. And the proof of just receiving the piece of paper at the office that we had just sent yesterday is incredible proof. Right. We're like, well look. I mean, the 83(b) election is just sending this piece of paper to the IRS, like we just did it. Right.

(01:52:37):
That go-go-go as soon as possible was extremely useful because it's just like, look, this exists. We can do it. Come on. On the long-term compounding part, we were extremely serious about how we picked our third party vendors, and backup vendors, and what promises, and SLAs, and reporting systems, and alerts, and playbooks, and backup processes, like it's in a very intense amount of internal structure we use. But again, we have to look at where the value is. The value is in making sure it happens. Does it need to be us sending the mail? Does it need to be us talking to government? Not necessarily. And we have chosen to work with third parties and many backup third parties as well because one, there's expertise in the world of physically printing and sending mail that the 10 of us are not going to today become experts in. And two, I think it also causes us to build better software in that we now need to evaluate if something's actually working because it's happening externally.

(01:53:39):
Whereas when you build it yourself, again, you have this natural feeling, well, we built it. It must be working. Oh, later we'll add alerts. Later when there problems, we'll figure out playbooks. Well look, when it's a third party building it, you're like, wait a second. What happens if they screw up? Like cool, we better figure that out. We better OCR all the results. We better do all these check sums, we better... And it would be awesome if we could always treat our internal work that way, but because it was external, it forced us to be more rigid where we needed to be rigid and create interfaces and kind of commitments. And again, we work with a bunch of great third parties and back up third parties to execute this. And each year we write a document called Should We Do This Ourselves? And we look at the other nine of us around the room and go, of course we shouldn't. Let's go on to something else. So again, we're just really stitching it together, but ensuring that it happens.

Lenny Rachitsky (01:54:31):
Awesome. Okay. I was imagining fax machines just,-

Jeff Weinstein (01:54:34):
There are fax machines occurring. There are fax machines occurring,-

Lenny Rachitsky (01:54:37):
Not in the Stripe [inaudible 01:54:38].

Jeff Weinstein (01:54:38):
And there are phone calls being made and there are robots waiting on phones on hold as well.

Lenny Rachitsky (01:54:44):
Oh, amazing.

Jeff Weinstein (01:54:45):
There's quite a lot going on.

Lenny Rachitsky (01:54:47):
AI is here. I saw a stat that one in six new Delaware corporations are now started on Stripe Atlas. That's absurd.

Jeff Weinstein (01:54:54):
Yep. I'm very excited to tell you when it's one in five, but it is not today.

Lenny Rachitsky (01:54:59):
Okay, sounds like we're close.

Jeff Weinstein (01:55:01):
We're on our way.

Lenny Rachitsky (01:55:02):
Sounds like we're close. The other stat I have here is that the fastest growing cities for startups. Here's what I have, I don't know if you know this, but Boulder, Shenzhen, and Las Vegas.

Jeff Weinstein (01:55:13):
They're everywhere. One of the, it's like stat we kind of came up with a little bit last year that I'm just personally deeply obsessed with is founding teams in which the co-founders are in multiple countries. So we kind of nickname this. Again, it's like giving things a good title, headlines. Cross-Border Founders. Wow. More than 20% of multi-founder teams have at least one founder from another country. That is astounding to me, that the internet could bring people together like that. And I think that's going to provide more perspectives, more solutions will be local and global. Just all perspectives are great. And again, I think the Atlas team itself represents this. We were very intentional of how we built the Atlas team. It's majority women and we have more diversity to hire, but we're just very intentional to make it a team that had diverse perspectives. You've been on teams that don't have diverse perspectives of any type. They are so much worse. There's no real science necessary here. We just enforce that. We had the opportunity to build this team that way.

(01:56:36):
And it was really important to me that it represented a world we wanted things to look like and to represent. And it just had to be very intentional about it because I've made mistakes in my career previously where my startup was all men when we sold to box one of them. And on each hire it was harder and harder and harder to hire someone of a different background. Just naturally folks didn't want to join that type of team. And that was the last time I've ever going to make that mistake, which is that early the candidate poll must match where you want the team to go. It's not a down funnel problem, it is an up funnel problem. And where you have to just make sure that for each role you're comfortable with the distribution of people and backgrounds in your candidate pool and go from there. And I think that is one of the reasons why that 10 person group is so effective, is it has just a lot of diversity and perspective.

Lenny Rachitsky (01:57:38):
Another skill Jeff Weinstein is incredible at that I wasn't even aware of. We're going to add them to the list and I actually saw a photo of the team and I noticed that. And so great work. Is there anything else on Atlas that you wanted to share before I get into how you actually made Atlas happen at a company like Stripe that has a billion things to do?

Jeff Weinstein (01:57:55):
We just want to hear about what's hard for you. If you look back in your emails and if you started a company recently, you're starting a company right now, the whole world is counting on you to pick a customer, solve their problem 10 times better than their alternative, get it to them, charge for it, become economically viable and build a great business that provides great services. We are not counting on you to become experts at this silliness of administratively running your company. Imagine life without Google Docs where you'd have to hire an IT person to run your IT back end on employee three. You'd have an IT person or imagine the world without AWS for EC2 or S3 or any of these cloud services and you're racking computers yourself.

(01:58:46):
You're just absolutely not going to try as many things. We just see the company structure, the structure, bringing people together to be like that, and we want to automate more and more and more of it and turn it into software. So we're looking for the next things to work on. We have a couple ideas, but we expect to turn more of groups of people working together, that administration into software. And I think it's just going to unlock huge amount more people choosing to do it.

Lenny Rachitsky (01:59:16):
Interesting. I'm so curious what that ends up being. If you really think about what you're doing here, if you believe that entrepreneurship and innovation and technology make the world better, you're creating such an unlock to allow more of that. And like I said, I think it's hard to imagine and think of other examples that could be as transformative and impactful as just making this process.

Jeff Weinstein (01:59:35):
It's funny because I go back to again, I also hear from founders, entrepreneurs like, oh, I can't think of an idea. Like, ah, I need a startup idea. And yet everything in the world is broken. And I also recall my first startup early 2010, 2012 ish, I joined a friend's company. That was started at the same time that the Stripe founders started Stripe. And that is, I think about that a lot because with the same information, knowing how hard it was to accept online payments, I chose to work on something else where they didn't. They worked on making it easy in seven lines of code to accept payments online, which turned out to be really useful.

(02:00:29):
So I really encourage people to be very sensitive to the problems that they see and just not let any little hiccup go unnoticed. And I think Atlas is really a manifestation of that, which is, let's actually look at every single thing. You went from hobby to economically successful operation and which of any moment along the way you shouldn't have had to do. And we think those things are a fair game to play with in any topic. I think that there are many more gigantic businesses, important things to be solved sitting in plain sight. I can't see them always, but when you hear, if you sit in enough silence and you hear the same people complain about problems, you too might find something as big as online payments are hard, which was sitting right in front of all of us.

Lenny Rachitsky (02:01:24):
And I think it's important to note, it doesn't necessarily have to be a venture-backed, venture scale company. Right. There are many, most businesses in the world are non venture-backed, venture scale billion-dollar companies. You can build a profitable company.

Jeff Weinstein (02:01:36):
It's kind of funny. We've all put this badge of honor of giving away a lot of your company. People really love owning a lot of their company and being successful. So you just got to pick the right capital structure for your business.

Lenny Rachitsky (02:01:57):
And again, the amount of money that has been generated of the companies that started through Atlas, you said $5 billion, basically that's the GDP of Atlas. That Atlas is,-

Jeff Weinstein (02:02:07):
And that's like revenue per year and that's growing,-

Lenny Rachitsky (02:02:09):
Per year.

Jeff Weinstein (02:02:10):
Yeah.

Lenny Rachitsky (02:02:10):
Yeah. And obviously a lot of it would've happened anyway, but still it accelerated. It's probably growing faster. A lot of it probably never would've happened otherwise. Yeah.

Jeff Weinstein (02:02:19):
We ran a survey a little bit ago, we need to rerun this, where we just asked people would they have started their business without Atlas. And about 20% of people said they wouldn't have or wouldn't had then. And again, these things are fragile. Right. And it's not all Google employees leaving their job to the build something. It's people from every possible background, every possible role, every possible job, every possible age group who see problems and can solve it. So it's dramatically more fragile than people think.

Lenny Rachitsky (02:02:56):
Well, great work, Jeff, and team Atlas and Stripe in general.

Jeff Weinstein (02:03:00):
Fun.

Lenny Rachitsky (02:03:01):
Let's talk about one last thing. There's so many more things I still want to talk about. Maybe we'll have a,-

Jeff Weinstein (02:03:06):
We can go quick. Yeah, we can [inaudible 02:03:08].

Lenny Rachitsky (02:03:08):
Make it 2X speed. So Atlas is basically a zero to one product. I know you didn't start initially, it was there, but you took it from, I don't know, maybe you took it from 0.5 or something to one in 100 now, and a lot of people struggle with starting things like this within larger companies. Like Stripe's a large company, right? It's like a very innovative, well run company, but it's also a large company. And clearly you made shit happen, you and your team. What kind of things have you learned? Actually, let me read a quote. Here's a quote that kind of describes you being good at this from one of your former colleagues who will go unnamed. "Jeff is really good at cutting through the BS. You hear so much about frameworks and all this complicated stuff that people talk about, NPM circles, one of the most straightforward, obvious things probably right. I get so annoyed after calls with Jeff sometimes because I know he's right about something. I banged my head against the wall for months." And so talk about just what you've done, what you've learned about getting stuff done.

Lenny Rachitsky (02:04:03):
Talk about what you've done, what you've learned about getting stuff done at a large company. What do you need to do?

Jeff Weinstein (02:04:07):
Not having things be your idea I think is really powerful. I just talked to 50 customers who all yelled the same thing. Here they are in varieties of quotes and forms and the rest of it, and you put some three bullet points of strategy around why it's important, it's going to help you win more market share, and the rest of it and how you can do it well. Cool. What else could we want to do? Maybe somebody has something where 51 people have the same burning thing, but the majority failure mode is we do nothing. That's the majority failure mode. So one, aligning people with deep customer stories story boarding some solution visually with a Sharpie and not a pencil, not Figma initially, not high or low fidelity. I can never remember which one is the detailed one, but Sharpie. What is the unconstrained perfect solution to this burning problem?

(02:05:18):
That's Pixar-style storyboard. You don't need to be a designer. You can just draw stick figures on a piece of paper or whimsical or whatever you want to do. And with those things, if you're not asking for the sun and the moon on headcount and team size to make some forward progress, who could stop you? Let's get some first version working. It was very motivating to get that single piece of paper in the mail, which was blank, to kick us off on the 83(b) election. Again, by the time this podcast airs, we'll have crossed 10,000 83(b) elections filed, and we will have done them all 100.00% on time. With the burning use case, why customers are going to need it, why we can do it cheaply, effectively, safely over a long period of time, and here's the way to get tangible, forward progress quickly against the stick figure vision, but with something in the browser or one version of it. Let's just get one thing working one time.

(02:06:31):
I find proof of existence to be an incredibly powerful proof, rather than proof by theory or proof by debate. It's like, "Look, we did it one time. Hey, I'm holding the piece of paper." Pretty motivating. If we just printed out the right information, we'd be done. You're like, "Okay, actually there's a lot to do other than just that," but it really pushed us forward. Cutting through a little bit of the red tape is about momentum and making each step not such a big deal and asking for less permission. Then of course, once you have a little bit of that under your belt, you're going to naturally be trusted with taking more of those kinds of bets.

(02:07:24):
Paired with some of the things we talked about earlier of everyone's looking at the same place about the metrics, everyone can watch the success. We don't need to do big, internal updates with long-winded PowerPoint presentations and scrambles the night before. You can just go to the metrics page and see how we're doing. That brings so much trust to the group that people start going from, "Why do we have this Atlas thing that doesn't really produce so much money. It's charging companies when they don't have money. We're a big payments business. How do you even compare these things?" To "Wow, look at the progress that they're making against the mission, and look at its impact on the curves." And you start to root for it more.

(02:08:16):
I think that's how we got it there. I will say one other thing, which is that making something economically viable is extremely important. I am probably the fourth person to run Atlas, and it's quite a pantheon of people prior to me, including the founder of Mozi, which is a compliance startup, Watershed, which is this amazing climate reporting tool, also led Atlas, Patrick McKenzie, patio11, for many folks who [inaudible 02:08:46]

Lenny Rachitsky (02:08:46):
Wow, what an alumni group, this collection.

Jeff Weinstein (02:08:48):
We owe ourselves a dinner. We owe ourselves a dinner. Quite a group. And now we have a new person. I technically no longer lead Atlas, so we've hired up a whole team, which is really exciting. And Hayley Halvarsson, who's joined us about a year or two ago, she leads Atlas now and you can find her on Twitter. She's fantastic. We swap jobs over a course of a year, just one month at a time, the roles. And so she worked for me, then I worked for her, and she's gone off to hire some amazing people to run Atlas. So it's really quite a privilege to have these people lead it over time.

(02:09:22):
But it was really important for us to communicate why we were going to run this in an economically viable way, and I think that applies to all products and all businesses. It's like, "Look, if you're a customer acquisition-style product, showcase why this is the best customer acquisition for the dollar for the company. If you are a margin-generating, moat-creating, ecosystem-growing portion of the business, then your metrics have to show it." So you can't just have half the story of just the product quality and the tweets. You have to have the economics. Who else is going to put this much energy into this style of product and that gives us confidence that we should invest it in the long term? Because alternatives can come and go, and I super encourage there to be more Atlas alternatives. That'd be great for founders, but I think over the long term, it'll be difficult to do so because of the business model.

Lenny Rachitsky (02:10:19):
There actually was an alternative at one point, AngelList, and then they're like, "No, Stripe is killing it. Let's just send everyone to Atlas."

Jeff Weinstein (02:10:26):
I had worked on Stripe payments for a while, and I had just started on Atlas, and I think that same month AngelList announced that they were doing incorporation and banking and cap table all together, which was exactly what I wanted to do. I was like, "Oh shoot, did I sign up for the wrong thing? AngelList is such a smart group of people, so customer-oriented, great brand, I love many of the people that work there, they work with some of the best legal minds, and they have the RUV setup. There's so much awesomeness here." I was like, " Should we really compete? What should we do here?" And we thought about it more and more like, "Look, in the very long term, this company-starting process is going to become a efficiency cost problem, and there's so much long tail complexity with dealing with multiple financial institutions, multiple government processes, all of this legal complexity, and it's difficult to charge a lot of money for it because it's hard to charge people money when they haven't even started the business yet."

(02:11:36):
We looked at it and said, "Look, we're going to keep this long-term, compounding approach because we think that this is where it's going to go." And it was a zero interest rate environment at the time. AngelList built a phenomenal product. I looked at it with nothing but admiration and happiness, but it also smarted and hurt. We kept building, kept building, kept building, and I got a phone call one night, on my wife's birthday before we sat down for dinner, and it was Dan at AngelList, I hope he'd be comfortable telling the story, who I love. Incredible product mind and he led product over AngelList for startups. He said, "We're going to get out of incorporation. This is not going to be our focus going forward. Do you want the business?"

(02:12:28):
That was like a year and a half after they had really gone out, or maybe two years after they'd gone out, or something like this. I was like, "Wow." We had kept such an open relationship with them. We had paired with them on legal constructs. We had discussed 83(b) election openly. A lot of people were like, "I can't believe you're talking to the competitor." Look, we all share the same mission here. Yes, we're competing, but are we really all better off from treating each other at arm's distance? We had a shared Slack channel. We discussed when the Delaware was slow on incorporation. One time is because they were playing softball and they had an afternoon off. That's a real story, and we've discussed it. AngelList was incredible in how they evaluated it. We're evaluating different partners, but because of our working relationship and the quality of your product, and they saw we were going with 83(b) election and the intensity of that, they just put up a webpage that said to get started with AngelList, if you need a company, go right over to Atlas.

(02:13:36):
That was a really amazing moment because I respected them so much and I looked up to them so much that they would mutually beneficially choose to do that. And everybody was excited and happy, and customers are happy, and it's been an incredible relationship since, in which you can start on AngelList, go through Atlas, and then all of your information is automatically populated into AngelList automatically. We've since rolled that out with several other partners, Mercury, Carta, others, but AngelList really led the way there, and we maintain a great relationship with the team. It took a while, but it really reproved to me that they're not competitors. It's alternatives, and if you care about your customer, you care about their alternatives, and if you care about the mission, you need to all work together. Look, there's some friendly competition, of course. We all want to win, but in the long term, I think all parties are significantly better off.

Lenny Rachitsky (02:14:31):
Wow, that is an awesome story. I don't know if you've shared that anywhere else. There's so many lessons there that I could spin off on and... Not worrying about competition, staying heads down, just solving customer problems, staying close to your competition, not being afraid to talk to them, sharing advice with each other, just building the best possible product. I don't know, there's a ton there that's super interesting.

Jeff Weinstein (02:14:52):
I couldn't really draw it up any better, and I think the world is better off with more specialization, and it's a pain in the butt to do these incorporations. I think you want more specialization and more partnership, and I think a lot of companies are starting to do that now.

Lenny Rachitsky (02:15:12):
Let me go back to the lessons you shared on how to build something new at a big company, then we can wrap up. I took a bunch of notes here, and these are awesome and they actually resonate a lot with Mihika, who came on the podcast, who's at Figma, been the person building a lot of zero-to-one stuff. So it's nice that there's these trends that are coming up again and again.

(02:15:32):
One tip is storyboard the ideal. With a Sharpie, draw out, "Here's this exciting vision of what this could be if we were to pull it off without constraints." Unconstrained, powerful vision. Two is solve a burning use case. Make it clear this is a huge problem for a lot of people. There's probably stories you share there. Show tangible forward progress like, "Look at this, we made this progress, we made this progress. Sent ourselves a piece of blank paper. Look at this, it's a huge milestone." And have momentum, and Mihika talked about this. Keep the fire alive. Keep the fire alive, show momentum. We're making progress. This metrics moving up into the right. Then there's a milestone... Felt like you had an early milestone of like, "Look, we made progress," and then also, have the business case, basically. "Look how much we could make and look what this could be if we were to succeed." Anything you'd add there? Anything you'd correct?

Jeff Weinstein (02:16:22):
Bringing the earliest customers into the room with your team as soon as humanly possible. We would just invite a founder to the team meeting. We would pipe all their feedback into a Slack channel automatically. We have all the NPS scores going to a channel, and anytime it's not a 10 for 10, we follow up directly. Constant engagement with a customer creates the momentum where it doesn't need to be the product person or some other leader saying, "We need to do this. Follow me." It's, "Oh my gosh, the world needs this. Let's figure out how to do it even faster."

(02:17:06):
And a tip that the team has tried, and this is well since I've been involved day-to-day, is literally inviting customers in to design the product, which I'd actually never heard of. "Hey, we're thinking about what happens after incorporation now and what can we do to help founders after they've set up their company? What would be magical there?" We just invite founders in, into a Whimsical, a piece of software I love. It's a really easy learning curve to create visual diagrams. And rather than doing a UXR about it, we just say, "What would you hope this dashboard would have?" And they'd grab a thing, and they start typing, and they start drawing what they want their dashboard to be. Why were we guessing beforehand? I now scratch my head. I'm several years into a decade-plus building things and I was like, "I doing this by myself. Why didn't I just assign it to the people who are going to use it in the first place?"

(02:18:01):
Now look, that doesn't always work because not all of your customers are going to be product designers at heart, but more of them than you think, and I think it's giving your customers write access, and not just read access, to your company is incredibly powerful. I think I had not quite seen it so directly where you just actually designed what they want, but I saw a diagram of something we're working on right now. I was like, "Wow, we haven't even had design look at it." They're like, "No, actually the customer drew it." Great. Why were we guessing?

Lenny Rachitsky (02:18:35):
I think you have an unfair advantage where your customers are founders and oftentimes have product skills and design skills, but I love that [inaudible 02:18:43].

Jeff Weinstein (02:18:43):
It's true, but I will really push, because you don't need a hundred of them and you'll find somebody somewhere who knows. You just got to sit in a little more silence. They'll raise their hand.

Lenny Rachitsky (02:18:55):
There's a quote you shared somewhere that relates to what you just said that your dad once said, "You can screw up a sentence if it begins with 'The customer.'"

Jeff Weinstein (02:19:03):
That's true. Yeah, my dad runs an IT business in Baltimore to help other businesses with their computer systems. Growing up, I would literally, physically clean the keyboards of his employees and dust the mice. But yeah, he's very, very customer-oriented, where I get a lot of it from, and my mom's a painter, so I think there's some combination of talents or interests there. He would take it one step further, and he sometimes physically bring a chair over in a meeting and say, "The customer is sitting here," and you'd have to pretend. Then he would fake talk to the invisible customer. "Based on what you've seen today at the meeting..." I saw him do this one time. "Based on what you've seen today at the meeting, are you more likely to pay your bill or less likely to pay your bill based on what you witnessed?"

(02:19:55):
That's a little intense on the pantomime, but I think the point gets across that... Again, because it's so natural to think internal, if you begin the sentence physically with "The customer" then start your sentence, you just have a much better shot at it.

Lenny Rachitsky (02:20:09):
That's an amazing story. Very a study group-ish, like an early prototype. Jeff, we've covered so much ground. I have two hours more worth of questions, but we need to-

Jeff Weinstein (02:20:21):
Let's lock.

Lenny Rachitsky (02:20:22):
We need to cut it off, I think. Is there anything else you wanted to share or leave listeners with before we get to a very exciting lightning round?

Jeff Weinstein (02:20:31):
Really excited about whatever you're building out there, thinking of building. My email address is incredibly easy to find. My Twitter handle is incredibly easy to find. Do not hesitate to send me cold emails. My love language is Loom videos of bugs, but feel free to send anything you have off the top of your head. I respond to good cold emails. Don't hesitate.

Lenny Rachitsky (02:20:51):
What's the email, real quick, for people?

Jeff Weinstein (02:20:53):
If finding my email address is your issue? It can't possibly be, but it is my first initial and last name at basically everything in the world, though my handle on Twitter is jeff_weinstein, but gosh, if you can't find my email address then you got a bigger problem.

Lenny Rachitsky (02:21:07):
Okay, we'll link to it in the show notes, as well. With that, we've reached our very exciting lightning round. Are you ready? Here we go. What are two or three books you've recommended most to other people?

Jeff Weinstein (02:21:20):
I know a lot of people on this podcast recommend high-output management, but it should be swap the Bible out for it at all the hotels in the world, in the little drawer. Put it everywhere. You can't go wrong, though. It is an incredible clarity of how to spend your time as a leader, a manager of other people, a very high bar for how evaluating your work as the sum everyone around you. That was very clarifying to me that it's not an individual effort, it is the sum of everything I'm involved in is how to measure it. So that's definitely up there. A nice pair to that book, as a amuse-bouche afterwards, is Orbiting the Giant Hairball: A Corporate Fool's Guide to Surviving with Grace, I think, is the full exact title by Gordon MacKenzie, which is the story of a illustrator at Hallmark, the greeting card company, and it turns out to be a, again, bureaucratic, slow-moving organization that, over time, added rules and policies and rules and policies and quelled creativity and innovation, which is surprising at a greeting card company, but it existed. So this is his incredibly well-drawn book, as you'd imagine, with beautiful illustrations about how he orbited the hairball of the organization to inspire others, keep himself engaged, and to bring creativity and excitement and trying to pull people off the hairball as he orbited it. So I think it's a fun afternoon read with beautiful illustrations about how to stay sane at big companies and where to be a little goofy and take the advantage and gravity of the hairball, but not be succumbed by it and to be able to orbit it.

(02:23:22):
Those two are really fun. I will say one other one I like... Because we haven't talked about strategy here, there's been more getting stuff done and some other tactical things, but 7 Powers, and I know you had the author recently on, which was awesome. I won't explain the book, you just watch the podcast of it, but it walks through many of the business powers and moats a company can have. I ran into the author...

Lenny Rachitsky (02:23:55):
Hamilton Helmer.

Jeff Weinstein (02:23:56):
Hamilton Helmer, yes, thank you.

Lenny Rachitsky (02:23:57):
What a cool name.

Jeff Weinstein (02:23:58):
Very cool name. Alliterative. At the Box lunchroom one time, where I worked at Box, they acquired one of our companies, and I was like, "Any luck finding the eighth power?" He was like, "I'm looking, I'm looking," as he ran off with his sandwich. One other funny, somewhat embarrassing moment about that book is when I was applying to work at Stripe, I was in some email conversation with our CEO, Patrick Collison, who is quite well-read and enjoys books, and I was trying to showcase, " I like books a little bit," though not at any level of him. And I had mentioned I just finished reading 7 Powers, and I recommended it to him, but it joke's on me because he's quoted in the foreword that I had skipped. So he was very kind to let me know that he had read it and he is quoted in it, so I was like, "Oh shoot, maybe I won't get the job." But I got through that part, at least. So those books have spoken to me. Do you have a favorite power, by the way, Lenny? Do you have a favorite power?

Lenny Rachitsky (02:24:57):
His favorite power is counter-positioning. I also like that power a lot because I think it's the one you can that really changes everything about how you build your company, so that's the one that always stands out to me. How about you?

Jeff Weinstein (02:25:07):
I like counter-positioning also, and Atlas with going cheap and that audience is counter-positioning, but I really enjoy process, the process power, because it is very difficult to, as an organization, get good at anything, and if you could do that over a long period of time in a sustainable way, you have a power.

Lenny Rachitsky (02:25:26):
This is the nerdiest chat I've ever had. Which is your favorite 7th Power? I love it. But on that power, I asked him about it. He makes a really strong point there, that rarely is it actually a power for people. They think the way we execute is going to be our advantage and rarely is it actually a power. Usually people can copy it, but when you nail it...

Jeff Weinstein (02:25:47):
That's even better, because then if your competition thinks they have it-

Lenny Rachitsky (02:25:50):
Yeah, exactly.

Jeff Weinstein (02:25:51):
They won't invest than the other one. So I like it even more, for that reason.

Lenny Rachitsky (02:25:54):
I love it. But I was going to say with Patrick Collison being quoted in the book, not only was he wrote part of the forward or was quoted, he basically credited 7 Powers of helping build Stripe. No big deal.

Jeff Weinstein (02:26:07):
Totally.

Lenny Rachitsky (02:26:08):
This lightning around is going great. This is a very microcosm of our whole chat so far. Second question, do you have a favorite recent movie or TV show?

Jeff Weinstein (02:26:17):
How To with John Wilson. It's on HBO. For those who haven't seen it, not really giving away anything because it's just wild when you watch it. You can't give it away. This videographer has found footage where he's just walking through Manhattan, and other parts of the country, but mostly New York, with a camera for 10 years, just filming intensely weird things. And if you've spent any time in New York, there's plenty to film. Then has put together this narrative afterwards about certain topics like how to make risotto or how to take out the trash or how to...

(02:26:53):
It's a way of seeing life through the eyes of these vignettes, diving down and really understanding people, and he does it through this incredibly dry humor of stitching together this video footage to tell a different narrative. And I think some of it is that we used to live in New York, and I love living in California, but I miss that frequency of strangeness, and you can see that through that TV show. Fantastic.

(02:27:26):
Movie? I recently watched The Quiet Girl, which is a film about a young Irish girl who is from a dysfunctional home and has this opportunity to live with a family friend who have more opportunity for her, more empathetic to her, and it showcases, again, how fragile things are. It's a very intense film, but there's something beautiful in how much opportunity was in front of this young girl. It is a tearjerker, but a great one.

Lenny Rachitsky (02:28:05):
Do you have a favorite product you have recently discovered that you love?

Jeff Weinstein (02:28:11):
I love my computer. I'm fast at my computer. Being fast at my computer helps me just go from intention to just out in the world. I've fallen back in love with Raycast, which is an automation tool for those who have watched the journey of Spotlight and Quicksilver and Alfred and all these automator services. Raycast seems to have cracked the nut on automation, nerd complexity, but also UI ease and some nice touches and loads quickly, does the basics. It's fully programmable, extensible, just a huge fan of Raycast. And then I think for product people, if you don't have CleanShot installed for screenshots, you're behind the curve. Being able to take a screenshot and blur particular things or point at stuff or have arrows and lines and have that be second nature, fast, instantaneous is so useful to be able to communicate what you're seeing. When I get a new laptop, it's Raycast first and CleanShot second.

Lenny Rachitsky (02:29:10):
Wow, I am going to download CleanShot immediately.

Jeff Weinstein (02:29:13):
Yes, it's extremely-

Lenny Rachitsky (02:29:15):
I've not heard of it. I've been using Skitch as my blurrings.

Jeff Weinstein (02:29:18):
As much as I appreciate the Skitch folks, CleanShot is an incredible piece of software.

Lenny Rachitsky (02:29:22):
Amazing. I'm going to do that. All right, two more questions. Do you have a favorite life motto that you often come back to, share with friends or family, find useful in work or in life?

Jeff Weinstein (02:29:30):
I don't even realize I say "Go Go Go" a lot, but I do. I actually say it and write it so people I hear that they'll later say, "Go Go Go" back to me. I'm like, "Huh? Don't I say that sometimes?" "Yes, you say it a lot." So apparently, "Go Go Go" is one of them. I also-

Lenny Rachitsky (02:29:45):
I love that.

Jeff Weinstein (02:29:46):
Say, "Let's make some mistakes," when we're brainstorming something or sitting at a sushi restaurant and talk sushi guy or gal, to showcase, "Let's be creative. Do whatever you want. No pretense. I'm not evaluating anything. Let's make some mistakes." It's just a weird thing.

Lenny Rachitsky (02:30:08):
They're so good. I'm going to use that for my podcast guests. "Let's just make some mistakes. Don't worry about it."

Jeff Weinstein (02:30:14):
At that point, everyone's like, "What? Okay, fine. Sure. Cool."

Lenny Rachitsky (02:30:17):
I like the combo of those two, "Go go go, let's just make some mistakes while we're going."

Jeff Weinstein (02:30:21):
You have to use it in certain circumstances and not for the five nines of reliability on our API, but it does have its place.

Lenny Rachitsky (02:30:29):
Final question. You worked with Patrick Collison and John Collison for many years. I'm curious what the most useful feedback or advice you have heard from them or learned from them?

Jeff Weinstein (02:30:40):
On my first month working here, which I guess is six, seven years ago now, they had put me in charge of our payments infrastructure services. That's all the backend systems that communicate with the financial system and all the internal APIs where we build the external APIs and products on top of, so quite a lot of stuff. I knew nothing about finance. I knew nothing about the scale that we're talking about. They entrusted me, somewhat insanely, with that responsibility. On the first month we had our quarterly business review where... The normal quarterly process, and I was like, "Okay, cool. I'll do the next one. I'll write the next one." I've been here one month. They're like, "No, you write it. It'll be even better that you write it." It's like, oh my God. It's forcing me to have to, in the fourth week, have that catalyst to understand the whole business and with the permission, because I was going to have to write this doc about how we're doing. The company had been in existence for seven years before I got here. It was already at some reasonable scale.

(02:31:54):
It was an intense operation, and I remember writing the first draft and sending it to him because it was... I didn't want to send... He had pushed me to do it a bit, and I figured I'd give him an early draft and he wrote back, "This doesn't sound like you yet." The willingness to entrust a new person to provide their own perspective and bring it into a very formalized document like that was an impressive... That really spoke to me, and I rewrote it completely, and I made it sound like me, and I've tried to make things sound like me since.

(02:32:29):
John's is more of a gut punch, I'll say. I reported to John, the co-founder. Maybe nine months into reporting to him, I would run around with a clipboard. I was a little bit manic of getting a lot done. A lot going on at Stripe at the time. We'd have a one-hour one-on-one, I'd be listing all of the things that we had accomplished and the problems we have and where we need escalation help and where we're stuck and all this that and the other. Lots of stuff. I had checklists and physical paper, flipping it over a little bit frantically. And he said, "You are one of the best people I've ever worked with at solving problems three through 100, but I need you stuck on problems one and two."

(02:33:22):
Oh man, that hurt. I was like, "Oh, shoot." I am productive on the non-hardest problems and I was trying to mask, not on purpose mask, but who wants to be stuck on something so hard when there's so much else to do? From then on, I would show up to him with problems one and two and not talk about problems three through 100. Even if we were working on them, we would just not talk about them and we would get stuck on problems one and two. That was phenomenal advice, which I was like, "Oh, shoot, I'm going to be fired." But it was really a deeply impactful sentence.

Lenny Rachitsky (02:34:03):
Wow, what a powerful, great, helpful... That's great advice [inaudible 02:34:10] right there.

Jeff Weinstein (02:34:10):
He really looked my soul and-

Lenny Rachitsky (02:34:12):
Yeah, I love this.

Jeff Weinstein (02:34:13):
Like a street fighter style or something.

Lenny Rachitsky (02:34:16):
But to your point, very impactful and helpful.

Jeff Weinstein (02:34:18):
Yeah.

Lenny Rachitsky (02:34:20):
Jeff, we did it. The archeology is complete.

Jeff Weinstein (02:34:23):
I appreciate the time, Lenny. It was fun. I don't do too many of these, so I'm curious to people's feedback and really appreciate the questions.

Lenny Rachitsky (02:34:30):
Amazing. Jeff, thank you so much for being here.

Jeff Weinstein (02:34:33):
Appreciate it, Lenny.

Lenny Rachitsky (02:34:34):
Bye everyone.

(02:34:37):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.

