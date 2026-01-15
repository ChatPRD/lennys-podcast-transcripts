---
guest: Nan Yu
title: Linear’s secret to building beloved B2B products | Nan Yu (Head of Product)
youtube_url: https://www.youtube.com/watch?v=nTr21kgCFF4
video_id: nTr21kgCFF4
description: Nan Yu is the head of product at Linear, one of the most beloved and
  fastest-growing B2B SaaS products out there today, and the gold standard for high-performing
  tech teams. In our conversation,...
duration_seconds: 4868.0
duration: '1:21:08'
view_count: 39440
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- okrs
- roadmap
- mvp
- iteration
- analytics
- pricing
- hiring
- management
- strategy
- market
- persona
- design
- ux
---

# Linear’s secret to building beloved B2B products | Nan Yu (Head of Product)

## Transcript

Lenny Rachitsky (00:00:00):
I think you see in the team at Linear that a lot of people don't see, which is that there's not actually a trade-off between speed and quality.

Nan Yu (00:00:06):
People talk about this as if there were a trade-off because when they think about speed, the thing they over-index on is rushing or being sloppy. What they should be indexing on is being really competent. If you look at people who are at the pinnacle of their craft, you can basically tell how good the output is going to be of their work product by how fast they're going.

Lenny Rachitsky (00:00:26):
What does speed look like when you say it can be done quickly and high quality?

Nan Yu (00:00:30):
What it really looks like is you have some rough time budget for how long you think something's going to take. By the time 10% of it has passed, after week one, you have something that works that tests some kind of key hypothesis internally.

Lenny Rachitsky (00:00:42):
I imagine a criticism you all get. Over time, you'll probably become a bloated piece of software as well.

Nan Yu (00:00:47):
When we examine this problem, we look at, "Well, what feature requests can we debate and what kind of feature requests do we absolutely have to say no to?" The stuff that we absolutely have to say no to is the exact kind of thing that leads to this bloatedness that makes ICs hate their lives.

Lenny Rachitsky (00:01:02):
Something that your head of sales shared with me is how impressed he is with the way you ask questions on customer calls and just keep digging and digging until you get to something.

Nan Yu (00:01:10):
My goal is to feel bad in the same way that customers feel bad.

Lenny Rachitsky (00:01:17):
Today, my guest is Nan Yu. Nan is Head of Product at Linear, which is one of the most beloved, most beautifully designed, and also the fastest growing B2B SaaS product out there today. You rarely see the kind of love that people have for Linear for any enterprise B2B SaaS product. So, there is a lot that we can learn from how Linear operates and how they build product. In my conversation with Nan, he shares a system that he uses for being creative and coming up with non-obvious solutions to customer problems, why it's a red flag to him when PMs tell him there's a trade-off between speed and quality, how he talks to customers in order to figure out the emotion that they want to avoid and then figure out the solution to avoiding that emotion, plus some killer advice on how to land a job, including how he landed his job at Linear and his previous role at Mode, and so much more.

(00:02:06):
If you have a desire to build a company or a product that's as beloved as Linear, this episode will give you a ton of tactics and ways to change how you and your team operate. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes, and it helps the podcast tremendously. With that, I bring you Nan Yu.

(00:02:30):
This episode is brought to you by Sinch, the Customer Communications Cloud. Here's the thing about digital customer communications. Whether you're sending marketing campaigns, verification codes or account alerts, you need them to reach users reliably. That's where Sinch comes in. Over 150,000 businesses, including 8 of the top 10 largest tech companies globally use Sinch's API to build messaging, email, and calling into their products, and there's something big happening in messaging that product teams to know about, Rich Communication Services, or RCS. Think of RCS as SMS 2.0. Instead of getting texts from a random number, your users will see your verified company name and logo without needing to download anything new. It's a more secure and branded experience. Plus you get features like interactive carousels and suggested replies, and here's why this matters. US carriers are starting to adopt RCS. Sinch is already helping major brands send RCS messages around the world, and they're helping Lenny's Podcast listeners get registered first before the rush hits the US market.

(00:03:33):
Learn more and get started at sinch.com/lenny. That's S-I-N-C-H.com/lenny. This episode is brought to you by Paragon, the integration infrastructure for B2B SaaS companies. Is AI on your 2025 product roadmap? Whether you need to enable RAG with your users' external data like Google Drive files, Gong transcripts or Jira tickets, or build AI agents that can automate work across your users' other tools. Integrations are the foundation, but building all these integrations in-house will cost you years of engineering, time you don't have given the fast pace of AI. That's where Paragon's all-in-one integration platform comes in. Build scalable workflows to ingest all of your users' external data into your RAG pipelines and leverage ActionKit, their latest product, to instantly give your AI agents access to over 100 integrations and thousands of third party actions with a single API call. Leading AI companies like AI21, You.com, 11x, and coffee.ai are already shipping new integrations seven times faster with Paragon, keeping their engineers focused on core product development. Ready to accelerate your AI roadmap this year? Visit useparagon.com/lenny to get a free MVP of your next product integration.

(00:04:56):
Nan, thank you so much for being here and welcome to the podcast.

Nan Yu (00:04:59):
Thanks for having me. I'm a long-time listener and reader, so it's really a treat to be here.

Lenny Rachitsky (00:05:05):
I want to share something with you to kick off that I haven't shared with you yet, that I haven't shared with anyone. These results might have come out by the time this podcast comes out, but I'm running a survey right now that I'm calling, "What's in your stack?" Where all my subscribers are asked, "What tools do you use most day to day? What tools do you love most? What tools do you hate?" And one of the questions asked was, what tool do you wish you could switch to if your IT department allowed you to? The number one answer by far is people want to switch from Jira to Linear.

Nan Yu (00:05:38):
Wow. I mean, hopefully, that means we're doing a good job.

Lenny Rachitsky (00:05:41):
I think that's exactly what that means. I'll read a couple quotes to give you a sense of what people are saying about Linear. I doubt these are surprising to you, but this gives people a sense of why you're here and why I'm excited to extract as much wisdom as I can from you. So, a couple quotes here. "Linear is a joy to use as I interact with my engineering teams, and I find inspiration in its design." "Linear is simple to use, yet powerful." "Linear's design is obviously an industry benchmark, but moreover, the performance and speed is a massive productivity boost."

Nan Yu (00:06:12):
I mean, it's really good to hear that because in a lot of ways, that's what we're trying to do. If you think about the entire impetus behind why Linear was started, it's because Karri was sitting at Coinbase and Airbnb and these places and just watching everyone around him struggle using the tools that they had available and always incumbent tools and just seeing that it made people hate their day-to-day a little bit, and we all got into technology and design and engineering, all this kind of stuff because it was fun. All of us started off building stupid MySpace pages and all of these side projects when we were young, and it started off as this fun thing that we do, and we're like, "Wow, we get to do this for a career," and then to have all of this kind of stuff put these big speed bumps into our day-to-day workflow, it just was really sad. So, that's why we started Linear. This really bust through all of that.

Lenny Rachitsky (00:07:11):
What I love about Linear, I feel like it's an inspirational business because many people want to, "I'm going to build just a much better version of something," and often that doesn't actually work out. Often nobody cares enough. There's all these barriers and reasons. People don't switch to something that's better, and Linear is an amazing example of building an excellent product and actually succeeding, and there's a lot more to it maybe than just building an awesome product. So, that's what I'm excited to dig into and understand how you all operate, and I guess just based on these results, to me, this is the ultimate sign of product market fit. People being sad they can't use a product in B2B enterprise software especially, so let's get into it.

(00:07:52):
First question I want to get into is something that I think you see and the team at Linear sees that a lot of people don't see, which is that there's not actually a trade-off between speed and quality. I think a lot of people think this is just an innate fact and something I've heard you talk about is that's not actually true. I actually saw Patrick Collison tweet this exact point that I'll read after you... I want to hear your thoughts, but talk about what you've learned about how there's maybe not actually this trade-off between speed and quality.

Nan Yu (00:08:20):
People talk about this as if there were a trade-off almost in a naive way because when they think about speed, the thing they over index on is rushing or being sloppy, and what they should be indexing on is being really competent or being like an expert. So, if you look at people who are at the pinnacle of their craft, it could be anything. It could be like a chef or a programmer or someone building houses or something. You can basically tell how good the output is going to be of their work product by how fast they're going. If they're going really fast, and they're obviously not being sloppy and then leaving a mess all over the place, it's like, "Yeah. Well, they got there because this is just second nature to them," and they're able to go at a really rapid pace and try stuff. And when we're building software, that's such a big component of how good the product is on the other side of it, which is like, "How many iterations were you able to do?" So, the only way you're going to get a bunch of iterations done and try different things and really feel out these different variations is by just going very fast.

Lenny Rachitsky (00:09:25):
In terms of speed, is the speed there moving quickly on each of iterations? Like what does speed look like when you say, "It can be done quickly and high quality"? What does speed look like?

Nan Yu (00:09:36):
Speed... What it really looks like is you have some rough time budget for how long you think something's going to take, and by the time 10% of it has passed, you have a workable solution. It's not like, "Oh, at the halfway point, we have something that is maybe a candidate that we can play around with." It's like, no, no, no. After week one you have something that works that tests some kind of key hypothesis internally so that you can feel like is this thing actually panning out the way we expect it to or did we have some crazy incorrect assumption? And you don't want to wait until you're 80% done to be able to make that kind of judgment because then it's just too late. Then you're pushing deadlines out, and you're making your marketing team very sad.

Lenny Rachitsky (00:10:18):
Amazing. Okay, so the way you think is, "We're going to spend a month on this feature. Let's get something workable. We can start testing with potential users even internally in the first few days, essentially in the first week"?

Nan Yu (00:10:30):
Yes. Yeah.

Lenny Rachitsky (00:10:32):
Yeah. I guess how can you do that? Because most teams can't do that. Most teams need to research, design, build. "Okay, cool. We have something," and once a month later, what allows you to do that?

Nan Yu (00:10:43):
Yeah, I mean, there's a lot of components of it. I think having really good talent really helps. Having engineers who don't get blocked by every single little design choice, they're happy to just make something workable. Even if they don't feel comfortable with that particular solution, they'll just bust through it and make something happen there. Part of it is intent. We don't have any expectation that the first version of it is going to be great. That is not in the cards. Look, the first version of it is our best guess in the general direction of what we want to actually ship in the end, and sometimes it works out. Sometimes, it's like, "Wow, this first version was pretty good. Let's make some minor adjustments, and we're good to go," but there's no expectation there. So, no one feels like they have to be a perfectionist and get everything, like all sanded down and really in tip-top shape. It just has to work and get the job done and validate or invalidate our major assumptions.

Lenny Rachitsky (00:11:38):
I'll read this quote from Patrick Collison. He tweeted this today as I was preparing for this interview, and he's the CEO and founder of Stripe, if you're not familiar. His tweet is, "I increasingly believe that 'good, cheap, fast -- choose two' maxim is devious misinformation spread by the slow. In my experience, slow and expensive usually go together."

Nan Yu (00:11:57):
Yeah, exactly. I mean, use the contractor kind of example. Like If someone's making modifications to their house, and it's taking forever, one, you're in a hotel and also the bills are adding up.

Lenny Rachitsky (00:12:09):
The other example you used when we were chatting about this earlier is chess players. I'm thinking of Magnus Carlsen, watching him. I think he was number one in speed chess in addition to just regular chess and what a microcosm of this point.

Nan Yu (00:12:22):
Yeah, I think that's the case and Magnus and Hikaru and all those guys who are at the top of their game, they can go unbelievably fast. In fact, that's the usual... I mean, I don't want to get too out of my depth with chess, but the usual way you try to make the game fair is you give them much, much less time than someone who's not quite as strong of a player, and they'll still win a lot of time, too.

Lenny Rachitsky (00:12:43):
So, maybe just to close out this point and give someone something concrete they can do with this information, say they want to start moving faster while not cutting quality, what do you think they can do? What's one thing they can start trying to work on and improving in the way they operate?

Nan Yu (00:12:58):
I think it's really that sort of attitude and point of view question to understand and take the almost controlled risk that the first version of this is not going to be perfect. So, it actually makes it a lot cheaper in many ways. It means you don't need a pixel perfect design. It means you don't need to make sure that all of the little UI bugs and stuff like that are solved because none of that really matters. What matters is you have working software that you can interact with, and you can see if it feels good. Does it actually solve the core problem that is facing our users? You can take it back to users. You can even let them into an early beta or something like that and get real validation there and to really focus on getting the smallest, shippable element, like not shippable in the sense of, "I can actually put on the production," but in the sense of like, "I can start learning from here."

Lenny Rachitsky (00:13:50):
Just a question I imagine is in everyone's mind is what do you do with this first very ugly V1... not ugly, not fully ready, first version. Is this something you're using internally to see if it's something? Is it something you have beta design partners with?

Nan Yu (00:14:04):
We have a gradually increasing sort of circle of users that use every single feature. So, by the time it hits GA, by the time it gets released, it's been used by a lot of different users up to that point. So, the first circle is just internal users. We use Linear every single day to write software and do our own work, so we have that kind of advantage and then once we feel like it's good enough, we'll put it into some beta customer group, and again, as early as we can in the process. We have to make sure that we don't end up corrupting people's data, and it doesn't look hideous and that kind of stuff, but as long as it reaches that level of quality, we can release it to early access customers who can give us good feedback and also just try to solve their problems with it. If no one engages with it, if no one's using it, then that's a good signal that we didn't really hit the mark, and then we have a couple of different beta audiences that we grow and then the ultimate release obviously is for GA where everyone gets it.

Lenny Rachitsky (00:14:59):
That's an amazing answer. Okay, so secret number one to Linear success, I'm going to take some notes here, is get new feature, product ideas out to people as early as possible, say, in the first 10% of the amount of time you've allotted, and then release it increasingly to more and more people to get feedback. I think the implication here is just most wasted time is on building things nobody actually ends up wanting or using. So, the sooner you at least get directional sense of are you heading in a good direction, the faster it all go?

Nan Yu (00:15:30):
Yeah, totally.

Lenny Rachitsky (00:15:31):
I imagine a criticism you all get. People are like, "Yes, Linear is so great, so beautiful, so much better than what's been out there for decades," but over time you'll probably become a bloated piece of software as well. That's just the fate of enterprise software. You have to check all these checkboxes. IT teams need all these features. So, there's always this like, "Oh, yeah, sure, you guys can operate this way for now. You have an amazing product for now, but it'll get ugly and bloated." How do you think about avoiding that? I know it's something you spent a lot of time thinking about. Maybe give us a glimpse into some of the conversations you have internally when there's these feature requests like, "Oh, I need single sign-on with this thing and this button here." How do you think about what to add, what not to add, and how to add these features to not make it bloated?

Nan Yu (00:16:14):
This question actually comes to us a lot from candidates that are interviewing with us. When you go like, "Hey, do you have any questions for us?" This is the question that we're going to get. So, we hear it quite a lot, and it's very sensible for them to ask it because they see history being littered with the corpses of startups trying to compete in this space and not making it, and I think when we examine this problem, we look at, "Well, what kind of feature requests can we debate and what kind of feature requests do we absolutely have to say no to?" And the stuff that we absolutely have to say no to is also the exact kind of thing that leads to this bloatedness that makes ICs hate their lives, and it's very specific. It's customization features requested by middle managers in order to make reporting a little bit easier at the cost of making IC workflows worse.

(00:17:16):
It's like if it fits that description, we're just saying, "No." There's no debate because we've already thought about it and this is the thing that we can't take a single step down this path. So, I think that's honestly one of the core promises of Linear is that we will not make this particular trade-off. So, when you see people saying like, "Wow, Linear is so much faster. It's so much easier to use and it makes my work so much more enjoyable." This is the reason because we have not taken a single step in this direction. It's very easy for a PM to say yes to this kind of request because often they're talking with buyers. Any kind of B2B type of space, they're talking with whoever the gatekeeper is and sales is putting pressure on them, and they're saying like, "Hey, we really want this one feature. It's going to make our reporting nicer." 

(00:18:02):
So, the director's going to be really excited by this, and we'll definitely make a buying decision based off of this, and we have to convince them that this is a false trade-off. The whole premise is wrong because the moment you start going down this path, and you make the IC user experience worse, they're just going to disengage. No one has to do this. If I'm an engineer, I get paid to write code. My performance review is based on my code contribution. It's not based on like, "Did I fill in all the tickets right?" So, I'm just not going to do that part, or I'm going to do it very sporadically, and then I'm going to just focus on my actual job. 

(00:18:38):
And then all your reporting is wrong because all the data is wrong, and it's sparse, and you get situations where people will... They'll say like, "Well, here's a dropdown field that someone put in here that's required." There's nine choices. I don't know what any of them meet, so I'm just going to pick one at random. I'm still going to pick the first one. Also, I'm going to pray that my boss is not actually using this data to do any kind of reporting and that has consequence because the data can't possibly be correct. So, I think for us, it's a very easy decision when it comes to that particular category of feature request.

Lenny Rachitsky (00:19:12):
I love how simple and clear that is. Basically, you all have a policy. We'll prioritize ICs over middle managers. Especially, like I love that it's around reporting. Almost always it sounds like, "I want to track what's happening."

Nan Yu (00:19:23):
Yeah, exactly. It's always, "I want to track what's happening." Well, what do you want to track? Well, I want to track which version of the product this thing's tied to based on some field information. It's like, okay, how is the person working on this supposed to even know that information? Well, it takes like a five-minute scavenger hunt every single time. It's like, "I don't think they're going to do that, man."

Lenny Rachitsky (00:19:43):
What I imagine happens, and I think why this is hard for most companies is there's an implication that you're turning down deals. You're not adding that one feature that will close a massive million-dollar sale, very difficult to do. I imagine it helps a lot that... I imagine the COO is very bought into this and there's this, "We will win long-term holding the line on this." Is that right?

Nan Yu (00:20:05):
So, it is, but I also think that there's not as much pressure as you would expect to do these kinds of things. There are basic scaling things, like we had to make SAML and SCIM and that kind of stuff. It's like, "Yeah, sure, we're going to do those sorts of, like keep the lights on type of work," but when it comes to work that's related to the actual business logic of the app's value proposition, what buyers care about is, is this going to make their team more effective? That's the reason that they're making this buying decision in the first place is that they're like, "Well, the current situation we're in... " And especially with large companies, right? The current situation we're in is a mess, and if we can convince them that these types of things are actually the reason that it's a mess, then we can really navigate them out of wanting them in the first place.

Lenny Rachitsky (00:20:57):
Got it. So, there's an element of you think you need this, but it turns out you'll be more successful and get everything you want, not getting this?

Nan Yu (00:21:04):
Yeah, and the thing is, it's not everything you want, right? Because people come with a laundry list, and it's like laundry list. Here's 10 things I want. You're like, "Do you want all of those 10 things equally?" They're like, "No, actually I don't." The first three are the things that really matter to us. If we solve the first three, then the other stuff, we can negotiate on. So, our job is to solve the first three-way better than anybody else that if they got through the first three through some kind of visual programming, customization type of thing, that it's never going to get to the quality level and the depth that we're able to offer by offering those as native features.

Lenny Rachitsky (00:21:37):
It's interesting thinking back to that survey I shared where the tool people want to switch to if IT allowed them was Linear, and on the one hand you could argue, "Well, okay, IT is not letting them use Linear for all these reasons.  On the other hand, you guys are growing really quickly within enterprise, like you're a new business. You started, I think, mid-market startups, and now you're working way up. So, I think it's not fair to say it's not going to work in enterprise. It's clearly working really well. I don't know if there's any stats you can share anything of that, but it seems to be going well, expanding up market.

Nan Yu (00:22:11):
Yeah, I mean, growth has been good. Growth in enterprise has been leading the other segments because I think this year, especially we reached a tipping point where I think with software, so much of the buying decision is based on almost like a brand thing, like is this for us? A lot of times people pick "enterprise software." It's like, "Why? You know everyone doesn't want this," and they're like, "Yeah, but it's for us." 

Lenny Rachitsky (00:22:36):
You won't get fired for buying Microsoft or whatever.

Nan Yu (00:22:39):
Yeah, exactly, and I think that we're starting to have enough brand penetration amongst enterprises where people can have that feeling, right? They're like, "Hey, Linear is for us. Who are we? Well, we are a large company that wants to act like a startup." It's like, "Who doesn't want that? Who doesn't want to go fast?"

Lenny Rachitsky (00:22:58):
Yeah. I had Jeffrey Moore on the podcast, and this is exactly what crossing the chasm looks like. He talked about basically you need someone that's across the chasm like a later adopter that isn't the person that's, "I love new stuff, and I'm an early adopter kind of evangelist." You need someone that's like traditional old school, takes their time to start to adopt it for you to be like, "Oh, okay. Now, maybe I should really take it seriously."

Nan Yu (00:23:21):
I also think that with this particular category of tool, and with a lot of other B2B software, not... Like no means not now, right? Not right now because it doesn't fit our budget. It doesn't fit our change management situation. "Oh, we have this exec that's really wedded to this other tool," but those things change, right? So, we keep in contact with them. They're in our CRM where we make sure we follow up, and we've had a lot of these where we've been said no to, like two years ago, and now we have some new features, and then go like, "Oh, yeah, it seems like you're ready for our scale," or whatever.

Lenny Rachitsky (00:23:59):
You mentioned that when you have these debates and questions that come out, you have features that a big company wants. There's this category of, "We know we will not build things for middle managers that want reporting and custom stuff just to track what's happening," versus something an IC wants to be more productive and successful, Linear. Give us a little sense of some of the more complicated debates that aren't necessarily in that bucket.

Nan Yu (00:24:22):
I think the complicated debates are often when we do add a new native feature, do we extend an existing feature and make it more powerful or do we add a new sort of service? And a big part of that is trying to figure out exactly who's going to use it, what are the actual real life use cases that we know about? Like that I know that Bob from Company X has this workflow and this is how it would work for him. Here are the different variations where it would work. So, tying it all the way back to real people is-

Lenny Rachitsky (00:24:52):
Like a specific person?

Nan Yu (00:24:53):
Yeah, specific person. Yeah. Yeah, exactly. Not a hypothetical person. Not one that you made up like Alice, Bob, or whatever. It's like, "No, here's the first name, last name. Here's their email. You can ask them," and I think that being able to tie it all the way back to reality in that way is a big part of how we really think about and discuss these things.

Lenny Rachitsky (00:25:13):
This connects the way I think about my newsletter is I always try to answer the question a very specific, like a person actually asked, not a general sense of something people may be interested in, and that very specific question, like it implies there's a need. Like not implies, it proves there's at least one person who needs this thing versus you have this idea of somebody that may want this thing. 

Nan Yu (00:25:36):
Yeah. I think a trap that a lot of times PMs will fall into is they'll make something, and they'll make some choices in it because maybe it's beautiful or it's elegant, but they don't go the step of like, "Is reality also beautiful and elegant?" Because reality is ugly sometimes, and if you have a beautiful and elegant solution that doesn't match with reality, it doesn't really matter. People can look at it, and they can ooh and ah, but if they don't use it to get their work done, it's never going to have long-term staying power.

Lenny Rachitsky (00:26:01):
Do you have a heuristic of how often you need to hear something for you to... could be just convinced, this is worth investing in? People may hear this, "Oh, one Bob. Bob wants this featured." That doesn't make sense. It's just one guy. How do you know when it's like, "Okay, we should really invest in this"?

Nan Yu (00:26:17):
Part of it is you hear something, and you're like, "Gosh, that actually is... " Not only is that true. It means that the way we thought about this was a little bit wrong, and I call this process... I don't know if it's the right way to describe it. I call it a kneeling where you have a thing, and it's not quite the right shape, and you put it out into the wild. So, this happens way in the first bit of the life of a particular feature. You release a thing, and then you start getting feedback about it, about hey, it doesn't quite fit reality, and then you ask yourself like, "Did we test that aspect of it? Did we actually match that part to reality?" And if you didn't, then it's like that's the part where you don't actually need that many pieces of feedback against it. It's not really a volume thing. It's like, "Did we think about this right or wrong?" That's one sort of category.

(00:27:01):
Another category is just you're getting a request for maybe a very big feature or a feature set from a lot of different people, but then you dig in, and you try to say like, "Okay. Well, tell me about how you're trying to use this," and there's 100 different use cases. So, you have choices here. You can either build the big feature that covers all the long tail of use cases or you can try to see if there's really concentrated pools of use cases for this that really make a lot of sense to adopt as a first order type of feature. So, I think those are the two sort of strategies that we employ the most. It's like, "Did we think about this wrong? And now we're just learning something about how it matches reality or for this big general feature that people are asking for, are there actually more specific use cases that we should be solving, and we should be solving really, really well?"

Lenny Rachitsky (00:27:52):
A thread that's coming through so far across a lot of these examples is getting to the specific person using the thing and making them happy and making sure the ask is going to solve their actual problem. In the case of looking at the IC versus the middle manager, in this case, it's like, "Let's talk to the person actually asking for this thing," not, "There's like 100 people generally asking for this thing and let's build what we think is a general solution."

Nan Yu (00:28:18):
Yeah. I'll give you an example of all of these things, which we just launched a feature called Customer Requests, and basically what this does, it adds a new concept of Linear, which is a customer. For B2B companies, this is very relevant, and the reason we did this is because we kept getting this request for fully customized fields, and we would be like, "Well, what is it that you want with your custom fields?" Because the problem is you add 100 custom fields and all your ICs start hating it. So, we don't want to go down that path, but what is it actually you're trying to do? And 40% of them were because, "Well, I have a customer," like Walmart or whatever, right? Like, "Walmart asked for this feature, and it's really important. I need everyone to know that Walmart needs this. I need to track it. I need to see how have we report... " 

(00:29:09):
We can report on what have we done for Walmart over the past year so that when my CSM has a one-on-one conversation with a rep, they can have some kind of evidence that we've been doing stuff for them, like all this kind of stuff. We're like, "Okay. Cool." That sounds like a very useful and powerful thing you want to do. How do you expect people to tag these things? Well, manually, because that's how we did it in our spreadsheets. It's like, "Okay, instead of that, we're going to hook up with your customer support tools. We're going to hook up with your CRNs. We're going to automatically bring in feedback from these companies. We're going to analyze the emails where they're from, and then if someone requests a feature that gets escalated into engineering, it'll just be tagged with whoever asked for it. You don't have to do anything, but you will know, and you can still report on this stuff, but there's nothing about this that makes ICs lives harder.

(00:29:54):
In fact, it makes them feel more confident because when they're building the thing, they actually understand who's asking for it and exactly what the email said. So, when they're doing the design or the details, they can actually see the real-life use cases that are present and solve for those directly.

Lenny Rachitsky (00:30:09):
As I'm hearing this, it's like, "Okay, obviously, this seems like an obvious solution. Of course, 40% of people telling me they have customers." In reality, most of the time, if you hear from a bunch of your customers, "Hey, I need this custom field," and sometimes you hear one thing, sometimes you hear another. Most of the time you're going to build this custom field. Something that your head of sales shared with me is how impressed he is with the way you ask questions on customer calls and just keep digging and digging until you get to something that is an insight for you, and then you start to try to solve the problem for them and think about what the product might be, and I think this is such an important and underappreciated skill for PMs. Is there any advice you could share of just how you approach this, how you ask questions, how you think about these customer calls to get to, "Okay, now, I see what we need to build versus let's just build what they're asking for"?

Nan Yu (00:30:59):
It's funny because I think from the outside, I'm on these sales calls and then the AE or someone's watching me ask these questions, and I think often they're like, "What are you doing? You're just asking questions from angles that I don't even know what your goal is here," and my goal is to feel bad in the same way that customers feel bad. They come to us with a request, "Hey, we want X," and it's like there's something motivating it and you can do the normal analytical thing and be like, "Ask five whys," and try to figure out like, "Well, what are your goals?" "And as a persona X, I want to achieve this outcome." You can do it that way, but you might miss the reason that they actually feel bad for not having this thing like, "I can't accomplish this goal. So what?" "So, I'm not going to get promoted at work."

(00:31:44):
Okay, great. I understand the severity of your problem at this point. What is the actual emotional valence that is motivating whatever you're telling me? And it takes a little while to get there. You can ask people directly like, "How do you feel?" And they're not necessarily going to tell you, but if you have a long enough and deep enough conversation with them, you start to level with them, and you're starting to see stuff from their perspective, and the more you see it from their perspective and the more they know that, the more they're willing to open up to you and tell you like, "Okay, honestly, I had this thing happen where I marked the ship date of this project as December 30th because it's a Q4 project, and I wanted to put it at the very end, and then my marketing team lost their mind because they're like, 'We can't ship something on December 30th. Everyone's on vacation,'" and you're like... And then they're like, "Yeah, this has made me feel really bad." 

(00:32:36):
So, I don't ever want to put dates on things ever again. So, like, "Okay, cool. We can help you deal with that. If that's what you're feeling, then I can start building stuff to make sure that you never have to have that bad feeling again."

Lenny Rachitsky (00:32:50):
People talk about empathy like, "You need to have empathy as a PM. You need to build empathy the best product leaders, have empathy in this." I think it's such a succinct and powerful way of describing what empathy actually looks like as a product leader, which is I want to feel as bad as they feel in hearing the story they tell, and it sounds like the way you do that is you keep asking questions to understand the moment they felt bad about something. In this case, the deadline.

Nan Yu (00:33:17):
And if you ask somebody in that last story, like what kind of issue do you have? You're like, "Oh, marketing and I would just never align on anything." It's like that doesn't really tell you what's going on. What it tells you is you had this terrible moment of communication that it's all miscommunicated, and you're like, "It's just going to keep happening over and over again." So, the thing that we did specifically to solve this was on projects in Linear, you can just specify a target date at whatever level of granularity you want. You can say it's a December project. You can say it's a Q4 project. You can say it's a second half of 2024 project. Like whatever you're happy promising, you can just put it on there and that way you never feel like you have to give this sense of false precision so that it ends up with a whole bunch of miscommunication down the line.

Lenny Rachitsky (00:34:04):
I could see why people love Linear is it just makes them feel less bad less often. There's a lot of connection here. I know this idea of emotions and feeling bad is a core part of how you think about building product, looking for moments. People feel bad. Is there anything more you could share there to share how you think about this idea of emotional hooks, emotional moments, and how you decide what to build?

Nan Yu (00:34:27):
So, to set the background of this, I've worked in very, very competitive industries. I worked at Everlane, which was a direct-to-consumer clothing brand. I worked in Mode, which is like BI tools and there's so many BI tools out there, and then obviously, Linear. We're project management. There's a lot of project management tools, and I think the more competitive your industry is, the more the low-hanging goal-oriented stuff is already picked because every PM from every one of these companies has been asking like, "Well, what's your goal? What is your job to be done," and all this kind of stuff. So, you have to look at things from an angle that other people might not have seen and for me, and for us, it's the angle of where are the emotional hooks that you're experiencing as you go through your work day, as you use our product, as you use competitors' products?

(00:35:21):
I think it's probably underexplored because... I don't know. I feel like PMs and engineers, we're like very thinky people. We avoid the touchy-feely stuff. So, I think that's the opportunity. You can see where are you feeling bad throughout your day where you don't even know? You might think, "I hate Mondays." "Why do you hate Mondays?" "Well, on Mondays, I have to go out and gather a whole bunch of stuff to write this report that it's really annoying." "Oh, so if I gave you a button that made the report, would that help?" It's like, "Oh, yeah, then I might not hate Monday so much." So, I think Paul Graham has a word for this. He calls it schlep blindness, right? It's like I'm schlepping through life, and I'm just completely blind to it, and it's true. You have to have an outsider come in and see what the rhythm of your feelings are throughout the day, throughout the week, and you note the spots where you could really use a lot of improvement.

Lenny Rachitsky (00:36:14):
Is there an example? I've shared a couple, but just where you've noticed this in someone using maybe a competitor or even Linear that you solved. I know you gave an example of the dates. I guess is there anything else?

Nan Yu (00:36:26):
A big feature that people love about Linear is we have this thing called Triage Management, and what it does is it systemizes this thing where if I put an issue into a different team, if I'm asking them to do something or I'm reporting a bug to them, it sticks in a special zone where it'll notify the right people. They're on a rotation and people will be able to respond to it in an organized manner, and I think this kind of automation, this feature, it came out of two different fields people were having. One, people were trying to implement this stuff by hand, and it was just a lot of touches, and they were doing it, but they felt like, "Oh, I'm totally underwater." "Why are you under water?" "Well, I have to throw all these tickets around and route them correctly and stuff like that," and they didn't see this as an opportunity to have a tool specialize in managing their triage queue. 

(00:37:23):
Because they were managing by hand.... They were on top of it, but it just felt really bad because they just had to spend so much attention doing this and then there's the folks who didn't do that. The feeling was just like, "Well, it's totally out of control. People are just throwing tickets over the wall, and I don't know what to do with them. I don't know where they are. They end up in all these holes and then the people on the other side are like, "I throw tickets over the wall. I have no idea what happens to them. I have no expectation that people are ever going to respond to them." So, there's all of these bad feelings that people are having. They all have the same root cause, which is like there wasn't a very automated organized way to deal with your triage queue.

Lenny Rachitsky (00:37:54):
Marketers, I know that you love TLDRs. So, let me get right to the point. Wix Studio gives you everything you need to cater to any client at any scale, all in one place. Here's how your workflow could look. Scale content with dynamic pages and reusable assets effortlessly. Fast-track projects with built-in marketing integrations like Meta, CAPI, Zapier, Google Ads, and more. A-B test landing pages in days, not weeks with intuitive design tools. Connect to tracking and analytics tools like Google Analytics and Semrush, and capture key business events without the hassle of manual setup. Manage all your client's social media and communications from a unified dashboard, then create schedule and post content across all their channels. If you're on content-rich sites, Wix Studio's no-code CMS lets you build and manage without touching the design. And when you're ready for more, Wix Studio grows with you. Add your own code, create custom integrations with Wix-made APIs, or leverage robust native business solutions. Drive real client growth with Wix Studio. Go to wixstudio.com.

(00:38:55):
I'm going to try to summarize some of the secrets of Linear's success so far. So, the first is get something out as quickly as possible, say, in the first 10% of the time that you have to build this thing and get it out to internal users and then maybe a growing list of beta users and people that are aware of they're using early stuff. Two is prioritize the IC and the user, basically, versus the buyer or the middle manager that wants reporting and all these custom features. So, it's basically focused on the user, which I think you hear a lot, but I love this very specific example. Three is when you hear asks for features and requests, get to the specific person using the thing, not just general, "Okay, cool. I've heard it 100 times." Find the person that actually needs this thing and understand what's going on, and then four is look for people feeling bad in a moment working in the product. Is there anything else that I'm missing that's important or any nuance you want to add?

Nan Yu (00:39:54):
The part where you said, like focus on the user, I think it's maybe a little bit more subtle than that. There's a nuance which is find where the incentives are really misaligned amongst your user base. There's a middle manager that wants really detailed reporting and there's a IC who just really doesn't want to go through all those extra steps, and the incentives for what they want are just very... They're just very misaligned, and you have to find those situations and be pretty judicious about how you make those trade-offs and where you can really find win-win outcomes there.

Lenny Rachitsky (00:40:30):
That's a really important nuance. Something else that's come through a couple of times as you've been talking is also something Patrick Collison tweeted once that has stuck with me, which is this idea of having a mental model in your head of the user. So, the way he described it and the way you've described it is oftentimes people are like, "Cool. We're going to figure out what to build. We're going to do a bunch of research, talk to users. That'll inform what we build, and we build it, versus what you've been saying and what he said is you do a bunch of research, look at data, talk to people. That informs your mental model of what the customer needs in their life, and then that informs what you build. So, that anytime you do more research, talk to customers, it's informing your view of the person, and then you're like, "Oh, this was different from what I imagined," or, "Oh wow. This is exactly what we've been thinking and let's build that." Anything along those lines that you might want to share?

Nan Yu (00:41:19):
Yeah, I mean, I can tell you a little bit about how we manage our backlog, which I think actually ties directly into this. At any given moment, we have probably 20 or 30 opportunities that we could possibly explore, just product opportunities, like problems to solve, areas to improve for our users, but they're not ready yet. We don't have enough conviction around how we might approach it. So, we just accumulate understanding of this stuff and periodically, we accumulate some more stuff, and then we reevaluate, "Okay, what is our current understanding of how we might best approach this thing?" And I think something that people struggle with is that they might have this model in their head. Like a PM might have this model in their head about how a user behaves, but it's just very hard to share that with someone else. You have to telepathically throw it into their brain, which is hard. So, what we try to do is identify areas that we might attack with a product, but also keep an up-to-date analysis of each of those areas so that everyone can engage with it and also contribute.

Lenny Rachitsky (00:42:22):
Is there an example of something that's sitting in your roadmap? I don't know if you could share these sort of things that's just sitting in the backlog of just like, "We're not quite ready to tackle this yet, but here's something we're inkling on."

Nan Yu (00:42:31):
Yeah, sure. Capacity planning is a thing that's been sitting in our backlog, and it's something that we see managers struggle with all the time, which is like I have a limited amount of personnel and resources, and I need to deploy them in such a way where we can theoretically accomplish our roadmap, but also we don't get blocked by some bottleneck that we don't end up blocking all of the projects because this one engineer is stuck on some info thing, and that's a thing people struggle with all the time. All the solutions out there are bad. The best solution is a very, very custom spreadsheet that someone would make, and it's a lot of upkeep. So, we have some ideas about how we might automate this, how we might use existing data within Linear to really help out with this problem, but I don't think we've quite cracked it yet. 

(00:43:18):
I think there's some nuances that we have to really explore a little bit further. So, we're continuously developing this, and as we hear from hear from users that are struggling with this problem, we will get on a call with them and sit down with them and talk through it.

Lenny Rachitsky (00:43:31):
And the idea there is keep informing this mental model, keep informing what this could be until you get to a place of like, "Okay. Cool. I think we figured out what will really solve this problem in an elegant way"?

Nan Yu (00:43:42):
Yeah, and I want to really stress a nuance here, which is it's not that we want to solve the entire problem. The entire problem is quite big, but there's something that's really right for Linear to do that would help people have a good starting point for them to reason about it. So, I think a lot of building conviction around stuff is not even like do we have a workable solution? It's like how much of the problem should we actually take on? Because if we take on too much of the problem, then we'll end up overpromising and not being able to deliver on it.

Lenny Rachitsky (00:44:13):
I think what's also useful here is you all keep your team very small intentionally and being constrained keeps you from taking on these things too early because you don't have the engineers to build their designers.

Nan Yu (00:44:24):
Yeah, that's true. I actually hadn't really put that part together, but I think some of the reason we've done it this way is because we don't have the bandwidth to action everything. So, we have this backlog that we maintain to make sure that when we do take it on, we're pretty set up for success.

Lenny Rachitsky (00:44:41):
Yeah, it's interesting. I think a lot of companies are starting to realize that they can build better products and move faster with fewer teams. I want to move in a different direction and talk a bit about how you actually think about building new products. Something that I've heard from you is that you have a systemized way of being creative, which I think is a dream for a lot of people's. It's like how do I be more creative? How do I think of new innovative concepts? You have a really interesting process for how you do this. Can you talk about it?

Nan Yu (00:45:09):
Yeah, totally. I think when people talk about being creative, a lot of times what they have a problem with is extrapolating. They can see the stuff that's right in front of them, but what about two or three steps down the line? And then it's just like, "Well, there's just so much possibility. I don't know what direction to go." So, the way that we try to do it is we ask a question which is like, "Okay, how extreme can you take it? You're designing a product. You're trying to come up with a solution. What's the most outrageous version of this along some trait?" I don't know if you guys did this at Airbnb, but I think Brian Chesky talks about like, "What's the 11-star experience?" Is that a thing you guys did?

Lenny Rachitsky (00:45:51):
It was a thing he talked about. Yeah, there's always a push of what's the 10X version of some idea.

Nan Yu (00:45:57):
When you think in that way, when you're saying like, "Hey, what's the 11-star experience?" What you're really asking is like, "Hey, what's the most luxurious version of this hotel stay? Or what's the most unforgettable kind of experience we can give people?" And you throw away things, I don't know, like cost. You throw away things like practicality because that's not what's interesting. What's interesting is I want to actually explore the possibility space, and I think this is really important to do because the goal is to get you to see beyond your defaults. We have all of these constraints that we're operating under that we psychically have in the back of our heads that we just don't even realize we have them. So, just break past all of them, and then you can really see what your options are because we talk about product decisions. It's like, "Oh, yeah, you have these choices. What are you going to decide?" There's all this decision-making kind of theory.

(00:46:52):
But the biggest risk is you didn't see the right choice to begin with. You have these three choices and none of them were right. It's this fourth one that was over in this corner, but you didn't look in that corner, so you never found it. So, I think the whole goal of this is to try to expand the search space of what you're trying to do.

Lenny Rachitsky (00:47:09):
So, what you're saying is people often don't think out of the box enough by not thinking too radically enough. So, the choices they're deciding between are just meh options and there's this process of breaking out of that, and I think you could hear this and be like, "Yeah, sure." I could spend 10 minutes being like, "Oh, hey, what's the craziest [inaudible 00:47:35]- "

Nan Yu (00:47:34):
Yeah.

Lenny Rachitsky (00:47:35):
But you're saying that actually is what you do and that actually works really well?

Nan Yu (00:47:39):
Yeah, and you actually build it. You can think of a very extreme version of a product and you can say, "Hey, let's actually... " For the first version, we talked about, like the first version, you know it's not really the right answer. Sometimes, you know it's so hard because you know this is the most extreme version of the answer. So, let's build that as fast as we can and see how it feels, and then we're going to learn so much about what the right actual answer is because we have seen this area of the product space and really felt it.

Lenny Rachitsky (00:48:05):
Awesome. Let's talk about an example of this because this feels awesome.

Nan Yu (00:48:09):
Yeah, I can talk to an example. Actually, is it okay if I demo something?

Lenny Rachitsky (00:48:13):
Absolutely. Let's do it. Show and tell.

Nan Yu (00:48:15):
Yeah, let me do that right now.

Lenny Rachitsky (00:48:16):
Here we go. We're going to share screen.

Nan Yu (00:48:18):
All right. So, this is just like a demo space instead of Linear. So, the feature where we did this that I remember very clearly, because it was recent, is we built this feature to save drafts for your issues. So, Linear, as hard as an issue tracker, if I make a new issue and let's say I'm trying to report a bug or something, so it's like I make a bug report, then I might start thinking through like, "Okay, what are the repro steps?" And then I start typing them, and this happens all the time. When you're at work, you're doing this and someone distracts you. If someone pings you on Slack or you have to go to a meeting or something like that, you're like, "I got to put this away for a second. I'll come back to it later." Note to self, figure out the actual repro steps and do it.

(00:48:56):
So, what can you do? Well, you want to save it as a draft. So, we're like, "Okay, this is the problem," and the first version of this, we're like, "What do we want to do? Linear is about being fast." So, we don't want to get in your way. We want to say like, "What is the fastest draft saving experience possible?" So, if you save it as draft, you can save it as draft. If you decide to not... you want to throw it away, you don't want it, just hit the X button, and it'll just throw it away. We're not going to interrupt you with a popup that says like, "Do you want to save your changes," or any of that kind of stuff. We'll just absolutely get out of your way fast as possible. So, we're like, "What's the risk here?" Well, it might feel really unsafe.

(00:49:31):
If you close this, and we don't ask you if you want to save change, you might feel like, "Oh, I just lost my changes on accident." We knew that going in. We built this anyway, and it felt super unsafe. It turns out that sort of inkling that we had was true, and we really felt exactly how unsafe it was. So, then we were like, "Okay, well, what's the safest thing we could possibly do?" The safest thing is just auto save everything. So, you start a new issue, and then you start typing some stuff, and it's just like auto saving as soon as you type a single character and that did feel quite safe. So, cool, but it also ended up leaving behind a whole bunch of like a paper trail of things you change your mind about. You've probably had this happen in document tools where you have a whole bunch of things in your space called like Untitled Document or New Document and stuff like that. It's just like-

Lenny Rachitsky (00:50:24):
So many untitled folders.

Nan Yu (00:50:25):
Yeah, so many untitled folders because the moment you say new folder, it starts saving it, and then you don't actually mean for that to happen. So, we had those two sorts of variations that we built, and we fell through and where we ended up was a balance between those two. So, what happens is if I'm creating a new issue, like I am here, and I close it out, it'll interrupt me, like we have to interrupt you, otherwise it feels too unsafe. So, I can save the draft, I can go to my drafts, and then if I'm in this draft I've already made, and I go in there, and I start to say, "Okay, I'm going to keep working on it," but then I get interrupted again, then I'm just going to auto-save it for you. There's no point. I'm not going to ask you again.

(00:51:06):
I'm always going to auto save it because I'm not going to create a new object. I'm just making modifications in place. So, we made this very specific choice of on a brand new issue, we will interrupt you, and then on an existing draft that you're messing around with, we're just going to auto save everything and someone doing a analysis. If they did a detailed teardown of these decisions, they might say like, "Wow, they made very specific choices here," but the path to get there is to do something totally extreme in one direction and then totally extreme in another direction and then find where they really meet up.

Lenny Rachitsky (00:51:39):
Such a good example, the way that you described it is you went like here's the safest route. Here's the fastest version. Where did you come up with these list of options? And for folks that are trying to do this for their company, are these like... Because these are Linear principles, we're going to be very fast. Is this the way you think most companies should operate these sorts of attributes? Do you think it's specific to what makes their product different? How do you think about that?

Nan Yu (00:52:04):
I think for a lot of companies, you have to ask, "What is the promise that your product or your business is making people?" It might be you always have a car available if you need it, and if you do that, then maybe we're going to have to implement search pricing to make that happen. It's always going to be available. So, here's the trade-off that we have to make. It's a very extreme point of view to do that. Or you might say the price is always predictable, but sometimes you can't have a car in the first place. Those are all choices that you get to make, and you have to sort decide, like where in that spectrum does it make sense based on the promise of your company?

Lenny Rachitsky (00:52:40):
A lot of people talk about this idea of working backwards. Brian Chesky in Airbnb has a big concept of working backwards from the ideal. Let's design the best possible scenario and work backwards. I love that this is even more tactical, which is just pick the extreme version of very specific attributes. Probably not that ideal, but it'll give us insight into a version of the ideal and an element that works well and then what doesn't. Yeah, exactly. I did this a lot actually at Airbnb, just like testing the extreme. So, it super resonates, this idea, and when you say test, so was it like you build it and play with it? Do you roll it out to some of these circles of users or is it often just internal, and then you learn and then iterate?

Nan Yu (00:53:23):
Yeah, we rolled out some of these versions to people.

Lenny Rachitsky (00:53:25):
Oh, wow. Okay.

Nan Yu (00:53:27):
So, the super-fast version that was unsafe, that only went interna, and everyone felt it was too unsafe, but then we thought, "Okay, let's go to the super-safe version," and then we rolled that out and everyone started having a whole bunch of... Like how many drafts are people making? I'm like, "This is too many." The people are leaving behind this crazy paper trail. Okay, we got to figure out some difference here.

Lenny Rachitsky (00:53:46):
Awesome. So, this very much connects to your first point of get things out really quick, and in this case, it's like extreme versions. You're probably not going to work long term, but it will teach you.

Nan Yu (00:53:56):
Yeah, exactly.

Lenny Rachitsky (00:53:58):
Amazing. Okay, and seeing it in action, I'm like, "Okay, obviously, this is the solution," and that's how the way this should feel, and to your point, it was not an obvious solution when you started thinking about it.

Nan Yu (00:54:08):
Yeah. I mean, the best solutions are always obvious in hindsight, and it's just like you have to develop a process internally that to eventually find your way there.

Lenny Rachitsky (00:54:16):
Something else that you've mentioned when we were chatting that connects to some of the things we've been talking about is you have this perspective that B2B software isn't just solving people's problems, it's also teaching them how to work, and it's this accumulation of information. Can you talk about that? Because I thought that was really fascinating.

Nan Yu (00:54:38):
If you think about how a lot of B2B software gets created, it's because there was some person in the middle of some giant company who implemented some kind of process, and they're like, "Wow, this process is really working for us. Maybe we should make it easier," and they build a little tool internally and then all of their colleagues can now press on buttons and good things happen, and then they turn that process and that tool. They spin it off into a startup, and they make a startup. This process repeats thousands of times. So, when you adopt that tool, you're not just adopting the actual software, you're adopting the idea that this is a practice that you ought to be doing in the first place. So, if you're a marketing person, and you adopt some marketing software, you're not just saying, "Okay, now, I can write emails and send them to people."

(00:55:24):
There's all sorts of process around that. You're organizing stuff into campaigns. You're measuring click-through rates. You're calculating cost of acquisition and all that stuff probably comes equipped with a tool because those are the right practices to do when you're doing this sort of marketing exercise. And whether you knew about it before or you learned it from the tool, like as a buyer for this kind of product, what I'm doing is I'm saying like, "Hey, I'm going to bring in this baseline level of marketing competency into my organization, that this is the worst we can do is whatever the tool defaults are."

Lenny Rachitsky (00:55:58):
Interesting. So, you're basically buying into a way of working when you're adopting a piece of software, not just have this problem I need solved.

Nan Yu (00:56:06):
Yeah, exactly, and I think the most salient example of this is if you've ever seen like a company adopt an ERP product, it's the most painful thing you can imagine. It's doing deep surgery. They have to redo all of their internal processes and the way they manage inventory and all this kind of stuff, but they're willing to do it because they know that this is a battle-tested way of making sure that you're actually doing good management of resources. So, they're like, "We're growing up now. It's time for us to adopt these best practices. In order to do that, we have to adopt this tool, and we will conform to whatever the tool is best is to do."

Lenny Rachitsky (00:56:44):
This connects to a couple things I know about Linear, one is what you've shared of just avoiding these customizations requests from people. Do you have a very opinionated way of here's how you should operate in order to build a great functioning product, org, and company in general? I'm just connecting threads here. One is like we're going to avoid letting people customize too much because we know they'll have a bad time, and then two is just this idea of we are opinionated about the way you should work in Linear, and it's like you have a Linear method, I think it's called, of just like here's how product team should operate based on everything we've seen be successful.

Nan Yu (00:57:19):
Yeah. Yeah. It's definitely connected in a way, and I think sometimes when people talk about... You mentioned like being opinionated, and I think sometimes when people talk about being opinionated, it can feel like they're almost saying like, "Hey, this is arbitrary," like your opinion and my opinion, they're just too opinions, man. Neither is right or wrong. What we try to do is find where there's actual consensus amongst a lot of different high performing teams, and then we can take those practices and say like, "Okay, for a team that isn't already practicing this, can we give them a button so that they can start practicing this?"

(00:57:56):
When we see companies doing a really good job of managing their triage queue, but it's very manual, we're like, "Okay, can we automate this? And then for this other company that really needs it that they don't know this is what they need, can we just give them a button to activate this?" And now they have the practice within their org, too.

Lenny Rachitsky (00:58:10):
So, I think the takeaway here is when you choose a tool, recognize it's going to change the way you operate and be thoughtful about is this the way we want to work versus just we just have a problem we want solved?

Nan Yu (00:58:21):
Yeah, exactly.

Lenny Rachitsky (00:58:22):
I want to come back to something, a thread that's come up a couple of times in our chat is the way you collaborate internally. It feels like there's a pretty unique way. You said you were on all the sales calls. Is there anything that you can share about how you collaborate internally, how the different functions collaborate that may be unlike how other companies operate that might be helpful for them to learn from?

Nan Yu (00:58:44):
Yes. Something that's worked really, really well for us is we think of product management as partially like a go-to-market discipline in the same way that sales and marketing are, right? When you talk to people and like, "Hey, tell me how product management works in your company," they'll probably say something about like, "Well, there's engineering product and design. They work in this triad, and here's how they interact and collaborate," and we all understand why that's useful, why that's helpful, but this other form of collaboration between product management, sales and marketing, I think it's something that's probably really underexamined and often I feel like in organizations, you actually see some antagonism between product and sales and marketing, and I think that's a shame because when we come together, the way we think about the way that we think about selling is a matter of like... especially because we sell to very expert practitioners, and they have a very sensitive BS detector.

(00:59:51):
So, a big part of what we try to do is we try to help our marketing team pick exactly the right word and the right phrasing to make us sound native to the language that our customers speak and also-

Lenny Rachitsky (01:00:04):
You're talking about engineers is my sense, right?

Nan Yu (01:00:07):
Yeah. Engineers is a big one, but even product managers, right?

Lenny Rachitsky (01:00:08):
Mm-hmm.

Nan Yu (01:00:10):
Like product managers know when... They know what the job is like. So, when you come in, you say the wrong words, people give you stink eye.

Lenny Rachitsky (01:00:17):
Don't call them project managers.

Nan Yu (01:00:19):
Yeah, exactly, for example. So, I think that's a big part of what we have to do. So, on our PM team, we actually have a full-time product marketer, and her job is to... Tactically, it's like all the change logs come from her, all the release notes, and also she's always crafting the language for whatever upcoming release that we're building and working directly with the teams and trying to figure out how to talk about it, and then once we go out and build the campaigns, build assets and things like that, that's where a lot of the language is coming from. It's coming from the work that she's doing and then with sales, they're validating all that message in the field. They're saying the words to customers directly and telling you if it's sticking or not, and then you can have a really good feedback cycle between those three disciplines.

Lenny Rachitsky (01:01:05):
What I've seen you refer to this way of working as is a double triangle, which is I think a complement to the PM, engineer, designer. Talk about that and give us a visual of what that looks like.

Nan Yu (01:01:18):
Yeah, I think PMs, like product managers, we often have a tough time trying to explain like, "What is your job?" It's a little bit of everything. I think the job that I do that we see it as is you're taking the building side of the organization and the selling side of the organization and bringing it together. You're taking all of the commercial motivations and goals of the company and making sure that what you build actually solves for those goals, and you're tempering that with what's possible and where the opportunities are to actually build stuff. So, to me, it's the PM in the middle, and then you have engineering, product design, and then sales, marketing, product management on the other side.

Lenny Rachitsky (01:02:03):
PM is always in the middle-

Nan Yu (01:02:05):
Indeed.

Lenny Rachitsky (01:02:06):
... but I think that's true from the perspective of PM, and I love this visual of just the PM is connecting the builders to the sellers, and you're involved in both worlds. This connects very directly to Brian Chesky's whole thing about how PMs should be doing marketing. So, the way they changed it, every PM is also PMM, and there's no more... They're product marketers now. That's their title and that's like the extreme version of what you're describing. 

Nan Yu (01:02:33):
Yeah. Yeah, and I think Apple's been doing that way for forever, too.

Lenny Rachitsky (01:02:37):
Got it. So, the advice here is if you're a PM at a B2B business, lean into the sales and marketing side of it, lean into the go-to-market.

Nan Yu (01:02:45):
Yeah, and in fact, if you're leaving something on the table in terms of the kind of impact that you are having at your job, that's probably the thing that you're leaving on the table. You're probably already doing a good job of collaborating with engineering and design. It's probably the sort of sell side that there's an opportunity for you to have more impact.

Lenny Rachitsky (01:03:05):
Just to make it even more concrete for PMs that are like, "Okay, I want to do this. I want to do what Linear's doing. I'm going to get more salesy." What does it look like when someone is more is in this double triangle working more closely with sales? You talked about being on sales calls. What else there can you share of just like, "Here, try these things"?

Nan Yu (01:03:20):
I think originate the message that you send to your audience. There's a lot of things that marketing does, which you are never going to necessarily touch. There's always demand gen and figuring out channel strategy and all this kind of stuff, like sure. That's a peer marketing concern, but actually picking the words and where the emphasis is, like you should understand the customer at a pretty deep level, probably deeper than any other group at the company because of the kinds of requirements gathering, discovery that you're doing. So, you're going to know the native language that your customers speak a lot better and help your marketing team originate those words.

Lenny Rachitsky (01:03:58):
Got it. So, basically be really involved in the product marketing, the writing, the emails, the headlines, the website?

Nan Yu (01:04:06):
Yeah, yeah, exactly. I know the word product marketing is also so overloaded. They do so many different things, but it's that sort of content creation piece that you really have an opportunity to contributes to.

Lenny Rachitsky (01:04:16):
Yeah, I love how concrete that is. It's like don't think about this concept, product marketing. Just think about the words that your potential customers and customers see. Okay, final area I want to spend a lot of time on is totally different. It's around getting a job. 

Nan Yu (01:04:31):
Oh, yeah. Okay.

Lenny Rachitsky (01:04:32):
You have a pretty unique approach to finding a gig. I heard from the founder of Mode about the very unique way you approached getting a job there. I imagine Linear is a similar boat. What advice can you share with folks that are looking for a job, maybe struggling, that work for you when you were looking for your next gig?

Nan Yu (01:04:51):
Project management is a unique role. Because we do just about everything, you don't really get pigeonholed into being compared along a single dimension with everyone else, and everyone who's hiring PMs, just like when they're hiring execs, they're hoping that they bring them on to solve some burning problem that they have. So, it's your job when you're in the interview process to figure out what that burning problem is. So, put on your discovery hat and go figure out what is the actual job to be done of the hiring manager when they're bringing on a new PM onto their team? And if you can do that and then make a good case that you are the person to solve that problem, then hiring you becomes a binary choice between do I hire the solution to my problem or do I hire someone else?

(01:05:48):
And I think what ends up happening a lot is when you're in a interview process, you're just trying to put your best foot forward, trying to say that you're great at everything. You have very few weaknesses. Maybe you tried too hard, like whatever, but everyone's going to say that. So, you're just one of end people, and you want to make yourself a little bit of just you versus the field. You're the solution to a problem and then everyone else is like a roll of the dice. 

Lenny Rachitsky (01:06:15):
So, the way you're describing it is the company has a job to be done, say it's drive growth of some feature. In this case, it's like for Linear, just build a killer or successful B2B product. I don't know. That's a broad one. Usually, you're not interviewing for head of product role, so that's maybe too broad. So, it's like what is this PM role's job to be done at the company and then help convince them you are the best person to do that job and solve this problem for them.

Nan Yu (01:06:42):
Yeah, and a lot of times when you take that approach, it'll feel like you already work there, and the way that I did this, like I got advice from a friend. He said like, "I was interviewing for this job at Mode that you referenced." I'm like, "How should I approach it?" He's like, "Just act like you already worked there. What would you do?" And then it's like, "Okay, I could do that." So, then when you're in this interview process and someone's asking you questions. He goes, "Do you have any questions for me?" You can ask them like, "What are your OKRs this quarter? How can someone help you achieve those?" You can be that specific about it, and they're like, "Oh, yeah, sure. I can tell you about the exact thing that I'm doing this quarter, and then you'll have some level of intelligence about what people are actually trying to solve because I think often we just get stuck in these very high level general types of questions like, "What's the company goals sand all that kind of stuff, and it's like, no, you can get really specific. If you were collaborating with that person in your job, what would you say to them?

Lenny Rachitsky (01:07:39):
I love how actionable this advice is. There's obviously an element of this takes work and time. A lot of people are interviewing at a lot of companies, trying to find a job, is part of your advice. Pick the ones you're most excited about and invest a lot of time in this way of interviewing.

Nan Yu (01:07:58):
You can invest a lot in the ones where you know that you're going to be able to over deliver on. If you understand what they're actually trying to solve, then you know where you're going to have both the highest chance of success of getting hired, but also doing a really great job on the other end of it.

Lenny Rachitsky (01:08:13):
And you talk about how you're like pretending you have the job, pretending you actually have this job as part of the interview process. Oftentimes, as an outsider, you don't have enough information to have a really good thought on what the solution is, and maybe part of it is going to be so wrong because you're like, "I don't actually know. I don't have the data." Do you actually try to reach out to the engineers and designers on the team to try to understand things? How far do you go to try to solve these problems and show them what you can do?

Nan Yu (01:08:37):
Yeah, I mean, you're in the interview loop. These are people that you're going to be working closely with. So, start there. Do your discovery questions, and if there's an area that you think you want to dig, you can ask. There's no harm asking, "Hey, can you put me in touch with an engineering manager who's working on the same problem?" And if no one else is asking, again, you're going to have an extra piece of feedback from that eng manager. So, yeah, like this guy asks really good questions, and it seems like they're really with it. No one else is going to have that piece of feedback. So, during the debrief process.

Lenny Rachitsky (01:09:08):
And just asking that question alone will show them how deeply you're thinking about this already?

Nan Yu (01:09:14):
Yeah.

Lenny Rachitsky (01:09:15):
Amazing. Nan, is there anything else that we have not covered that you want to touch on or share or you think might be helpful to listeners before we get to a very exciting lightning round?

Nan Yu (01:09:30):
I have a very specific point of view on deadlines. I don't know if that's [inaudible 01:09:34] you care.

Lenny Rachitsky (01:09:34):
Let's do it. Fire away.

Nan Yu (01:09:38):
I think what often happens is people get depressed about deadlines. It's like, "Hey, here's the ship date," and then you never make it. I don't know if you've had this feeling before.

Lenny Rachitsky (01:09:47):
Absolutely, with some deadlines.

Nan Yu (01:09:49):
You were an engineer before too, right? So, it's just like engineers is basically like, "Oh, yeah. Yeah, deadlines, they're complete fabrications," and the only way to make deadlines real is to take them so seriously that they are basically like a P0 problem, and everything else has to not matter in comparison to the deadline because that's the only way you're going to be able to signal to the team and also to all the stakeholders that you're actually taking it seriously. So, my feeling on deadlines is don't have too many of them, and when you do, it's a P0. So, the engineer is working on it. They don't get to work on anything else.

(01:10:28):
It's like, "Oh, I need them for this," like nope. Nope. You're not pulling them off of anything. We're doing this. As a PM, your job is to just cut as much scope as possible to make it possible to hit that deadline. Like what are the things actually blocking us from doing it? Because what you want to do is at the moment where you have to make the go, no-go call on whether to ship, you want to be able to actually have a product that you can say yes to. It might not have all the features you had wanted or whatever, and you can say no. You can make that choice, but you want to set yourself up to be in a position where you can actually say yes or no to something, because what often happens is like we want this thing. Well, it's not even close to being done yet, so there's no possible way we can say yes. I can't ship it. It's half broken. It's like, "No, no, no. You want to get to a point where it works. It might not be the product that you want, but it is an actual real product that you can conceivably ship."

Lenny Rachitsky (01:11:19):
So, you said that don't have too many deadlines, but when you do, make sure you... Everyone understands these are actual deadlines. When do you decide it's worth having a deadline? Is it like a marketing launch sort of thing? What's worthy of a deadline in your experience?

Nan Yu (01:11:32):
Yeah, it's usually having to do with some kind of external marketing type of exercise that you're try to hit.

Lenny Rachitsky (01:11:39):
Got it.

Nan Yu (01:11:39):
And I think that that's the other thing that I think. As builders, we can often look at launch dates and stuff like that. It's like, "Oh, who cares if it's a little bit later or we skip this change log," or whatever it is, and I think that that's really a... I don't know. It makes me go crazy when I hear people say that in all honesty. With marketing and communication with customers, you basically have a limited amount of opportunities to do so. A year is 365 days. There are 12 months. Each of those months has about four weeks. There's some rhythm where you get to have 50-ish weeks to say something to your audience once a week, or you get to have 12 months to say something really big or four quarters to say something huge. If you miss one of those opportunities, you don't get it back again. You can't time travel back and say like, "Okay, actually, let's redo first quarter and say this message that we wish we could have gotten into the field."

Lenny Rachitsky (01:12:35):
That is such a powerful point. I could see the sales marketing, go-to-market element of your job coming out there. I imagine everyone that's in that field's like, "Yes, this is exactly right." Maybe just the last question along this line. So, I love this idea of taking deadlines very seriously when you commit to a deadline. At the same time, as you pointed out, it creates a lot of stress knowing there's a deadline we have to hit. So, one lever you've mentioned is cutting scope. Another is just people spending more time estimating to have more accurate deadlines. You invest in that. How do you think about just for an engineering team to come into a deadline, how much to spend on de-risking and estimating versus just, "Let's just do our best and then we'll cut and adjust"?

Nan Yu (01:13:18):
This might be my hot take, but we do almost no estimating in order to hit deadlines. What we do is we ship as early as we can. The thing we talked about earlier where if by the time that 10% of the time has elapsed, you have a working thing, you can now spend the rest of the time deciding whether or not you want to do another iteration or you want to polish that thing and get it to be a shippable state. So, you're setting up your future self to be able to make that decision. So, none of this is... You can't go into this at the very last moment and say like, "Okay, now, we have to take the deadline seriously." You have to do it from the beginning and commit to the process of going very fast, iterating early, and then putting yourself in a position where you can say yes or no to a product.

Lenny Rachitsky (01:14:03):
So interesting and so different from the way most companies operate. Nan, this was everything I was hoping it'd be. I think this is going to help a lot of people build much better product, which would be good for the world if more products are like Linear. With that, we reached our very exciting lightning round. Are you ready?

Nan Yu (01:14:20):
Yeah, let's do it.

Lenny Rachitsky (01:14:20):
Okay, let's do it. Okay, first question. What are two or three books that you have recommended most to other people?

Nan Yu (01:14:29):
I think the one book that I recommend the most is The Design of Everyday Things by Don Norman. I read it originally in college for an HCI class I was taking, and I think of everything I've ever read, it's the thing that caused me to see the world from the perspective of everything you interact with as a product. Every pencil that you use, every door that you open is a product that somebody designed.

Lenny Rachitsky (01:14:55):
And is that the big takeaway from that book? Because it comes up a lot, and it's such an old book. So, I guess for someone that hasn't read or maybe doesn't have time to read, it is the big takeaway for you. Someone designed everything and there's a reason things aren't great, and they can be improved.

Nan Yu (01:15:10):
Yeah. I mean, I saw this the other day. I was at a café in my neighborhood, and I saw a kid rip a handle off a door, like of the café. He pulled it so hard, it came right off because it was a push door, but it had a handle that looked like you could pull it, and that's one of the canonical examples of the book because [inaudible 01:15:25] are just mysteries. Yeah.

Lenny Rachitsky (01:15:28):
Awesome. Next question. Do you have a favorite recent movie or TV show you've really enjoyed?

Nan Yu (01:15:33):
I watched The Diplomat on Netflix. I think it was terrific. It's really fun, easy watch. It has some West Wing vibes if you were into that back in the day.

Lenny Rachitsky (01:15:44):
Yeah, have you seen the second season?

Nan Yu (01:15:46):
Yeah, I finished the second season. Yeah.

Lenny Rachitsky (01:15:48):
I wasn't as excited about the second season, just to put that out there. The first season was really good and then just went off a little like, "Okay. I guess it's cool," but stuff like that.

Nan Yu (01:15:55):
Yeah, it got a little like spy thrillery, I think.

Lenny Rachitsky (01:16:00):
Okay, cool, but still really good and on Netflix. Okay, cool. Do you have a favorite product you recently discovered that you really like?

Nan Yu (01:16:06):
I didn't discover it, but I discovered a version of it that was really interesting. There's a pen. Actually, I have one on my desk. It's called the Sakura Micron. I don't know if you use these. It's like a felt tip pen. It's really great. It was originally invented in Japan for artists to draw comic books and stuff, and you can use it for anything. I use it for journaling or whatever, but I was on Amazon. I was trying to buy more, and I found a package that said like, "Bible Study Kit." I was like, "Why is this labeled Bible Study Kit?" And it was literally just the pen in four different colors, and it was because the thing doesn't bleed through pages. So, if you have a Bible, which they often have these really flimsy newsprint pages. It's not going to bleed through.

(01:16:51):
And it's just really interesting to me that someone marketed a normal package of these pens as a Bible study kit and for people who were looking for that keyword, and it was official, too. It was not something hacked together. It was actually an official packaging of this.

Lenny Rachitsky (01:17:04):
Amazing. What a unique pen choice. Two more questions. Do you have a favorite life motto that you often come back to and find useful in work or in life?

Nan Yu (01:17:15):
The correct amount is too much minus one, and I think this ties into the try the extreme version of it of a thing where... I don't know, like a stupid example, like how much pizza do you want to eat? It's like, well, five slices was too many. I feel bad. Then four was probably the right number, and then if you want to find the right number, sometimes you just have to really shoot for the edge and then find out what's too much, and then you'll find out exactly what the right amount is.

Lenny Rachitsky (01:17:41):
I love how tactical that is, makes me think about Elon Musk's thing about cutting things. Like one of his formulas for just getting stuff done, one of them is just cut stuff before trying to optimize it and automate it, and his advice is if you don't bring back 10% of things, you cut, you're not cutting enough.

Nan Yu (01:17:59):
Yeah, exactly. 

Lenny Rachitsky (01:18:01):
Final question. You worked at Everlane for a number of years, and you shared the rough idea of a story around a shirt, maybe a bestseller that they have now, and how you helped create a bestselling women's shirt. Can you share that story?

Nan Yu (01:18:19):
Yeah. So, I mean, to be clear, I witnessed the creation. I don't think I had a direct hand in it, but yeah. So, I saw this advertisement the other day on Instagram for... It's called the Women's Box-Cut Tee, and it's a wide and short for women, and I looked, and it had 20 colors of it, and it sells super well, and I remember when we created this thing, and it was because there was a batch of defective men's t-shirts. They all came in an inch and a half too short. So, we couldn't sell them. You would have your belly button sticking out. No one wants to wear of that. So, what we did was like, well, we have to salvage the inventory because we were a very small company, and we had to make cash flow, and we couldn't just damage it out.

(01:19:06):
So, the design team and the marketing team came together, and they said, "Okay. Here's what we're going to do. We're going to cut another two inches off of this and make it really cropped and market it towards women as like a cropped boxed-tee silhouette, and we did that. We're like, "Okay, hopefully, we can salvage this inventory and not have to take a write-down." It sold out in a week, and we're like, "Oh, okay. I guess we just made a hit product," and it's one of these things where it's very hard to know what this was. Was this a marketing thing? Was this a design thing? I don't know, but you just come together, and you find the right product market fit in the weirdest way.

Lenny Rachitsky (01:19:43):
I love that it's still going.

Nan Yu (01:19:43):
Yeah, it's still going. Originally, it was just white. Now, there's like 20 colors.

Lenny Rachitsky (01:19:48):
Oh, man. I love how many industries you have worked in: fashion, data analytics, project management. I don't know what's next. There's more, I imagine. Nan, this was incredible. I really appreciate making time for this. Like I said, I think we're going to have helped a lot of people build better products. Two final questions, where can folks find you online if they want to reach out and learn more? And how can listeners be useful to you?

Nan Yu (01:20:08):
Yeah, I'm on X/Twitter as the thenanyu. It's T-H-E and then my name, and if they have any feedback about Linear, we're very happy to take it, especially for people who use it in their day-to-day. We really want to hear from users.

Lenny Rachitsky (01:20:26):
What's the best way for them to share that? Is it tweet at you? Is it go to the website? What do you recommend?

Nan Yu (01:20:31):
Oh, yeah. You can tweet at us. You can DM me on Twitter. My DMs are open, so it's all good.

Lenny Rachitsky (01:20:36):
Amazing. Nan, thank you so much for being here. 

Nan Yu (01:20:39):
Yeah, of course. Thanks, Lenny.

Lenny Rachitsky (01:20:40):
Bye, everyone.

(01:20:43):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

