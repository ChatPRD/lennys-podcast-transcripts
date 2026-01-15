---
guest: Gaurav Misra
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
- acquisition
- onboarding
- metrics
- okrs
- roadmap
- prioritization
- user research
- mvp
- funnel
- monetization
- subscription
- revenue
- hiring
- team building
---

# Mastering onboarding | Lauryn Isford (Head of Growth at Airtable)

## Transcript

Gaurav Misra (00:00:00):
There's rarely a time like this where so much is possible. Even like five, seven years ago, it's so hard to start a company. Everything feels like it's done, someone else is working on it. Suddenly, it's a time, right now, which I've never even experienced, where everything you try just works.

Lenny Rachitsky (00:00:14):
With people constantly hearing about all the things happening. Is there any tools or processes or approaches you've figured out to help stay focused?

Gaurav Misra (00:00:21):
Our engineering goal is every engineer should ship a marketable product every week.

Lenny Rachitsky (00:00:27):
I love just how wild that sounds. How do you maintain quality and make it all cohesive?

Gaurav Misra (00:00:31):
I actually think as a startup your job is to take on technical debt because that is how you operate faster than a bigger company. Bigger companies don't take contact technical debt, they pay it usually right away, or they're paying back technical debt from the days when they were a startup.

Lenny Rachitsky (00:00:45):
Is there anything else that in how you operate and the way you build product that you think is really unique and interesting?

Gaurav Misra (00:00:50):
We have what we think of as the public roadmap. This is basically what people have asked us for. There's all these surface areas where we receive user feedback, but these are all features that every competitor knows about. If a user is asking us for it, they're asking everybody for it.

(00:01:04):
It's not going to be a game changer in terms of winning against your competition. So we have a second roadmap which we think of as a secret roadmap.

Lenny Rachitsky (00:01:15):
Today my guest is Gaurav Misra. Gaurav was an early employee at Snap where he led the design engineering team, which he explains in the conversation. He's also an engineer at Microsoft and a couple other companies. Most recently, he's the co-founder and CEO of Captions, one of the most successful and cutting-edge consumer AI products, which lets you generate and edit talking videos with AI. They have over 10 million users and have raised over a hundred million dollars.

(00:01:39):
In our conversation, we essentially do an archeology of how a modern AI oriented startup operates, including how every single engineer at their company ships a marketable product or feature every single week. Why they have a secret roadmap, in addition to a regular roadmap. We also get in-depth about how Snap as a product team operated. What he's learned about what it takes to build a successful consumer and social app, why they had no PMs and how designers ran the show, which may or may not have been a great idea. And also what happens in a world where AI video is so good that you have no idea if it's real or not. This episode is for anyone that is building a product on top of AI. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app. And also, I just launched an insane deal for subscribers of my newsletter. Every yearly subscriber now gets a year free of Notion, Perplexity, Superhuman, Linear and Granola. Learn more at lennysnewsletter.com. With that, I bring you Gaurav Misra.

(00:02:39):
This episode is brought to you by Brex, the financial stack used by one in every three US venture-backed startups. Brex knows the nearly 40% of startups fail because they run out of cash, so they built a banking experience that focuses on helping founders get more from every dollar. It's a stark difference from traditional banking options that leave a startup's cash sitting idle while chipping away at it with fees. To help founders protect cash and extend runway, Brex combined the best things about checking treasury and FDIC insurance in one powerhouse account. You can send and receive money worldwide at lightning speed. You can get 20x the standard FDIC protection through program banks and you can earn industry-leading yield from your first dollar while still being able to access your funds anytime. To learn more, check out Brex at brex.com/banking-solutions. That's brex.com/banking-solutions.

(00:03:36):
This episode is brought to you by Paragon. The integration infrastructure for B2B SaaS companies is AI on your 2025 product roadmap. Whether you need to enable RAG with your user's external data like Google Drive files, Gong transcripts, or Jira tickets, or build AI agents that can automate work across your user's other tools, integrations are the foundation. But building all these integrations in-house will cost you years of engineering, time you don't have given the fast pace of AI. That's where Paragon's all-in-one integration platform comes in. Build scalable workflows to ingest all of your user's external data into your RAG pipelines. And leverage, ActionKit, their latest product to instantly give your AI agents access to over 100 integrations and thousands of third-party actions with a single API call.

(00:04:24):
Leading AI companies like AI21, you.com, 11X, and Copy.ai are already shipping new integrations seven times faster with Paragon keeping their engineers focused on core product development. Ready to accelerate your AI roadmap this year, visit useparagon.com/lenny to get a free MVP of your next product integration.

(00:04:50):
Gaurav, thank you so much for being here and welcome to the podcast.

Gaurav Misra (00:04:53):
Thank you. Thanks for having me. Excited.

Lenny Rachitsky (00:04:55):
I very rarely have early stage founders on the podcast, but I wanted to chat with you because you're at the center of so much of what is top of mind for a lot of builders these days, AI and video, and just consumer and social apps.

(00:05:11):
Also going viral and finding new marketing channels. So I think there's a lot that people can learn from the way you approach product, the way you've built product and the way you just think about where things are going. So again, thank you for being here.

Gaurav Misra (00:05:26):
Appreciate it. Honestly, it's an exciting time. I got to say like there's rarely a time like this where so much is possible. In normal times, if you think about even five, seven years ago, it's so hard to start a company. It's so hard to come up with an idea. It's just like everything feels like it's done, someone else is working on it. Or it's like, oh it's been tried three times and failed three times. And suddenly, it's a time, right now, which I've never even experienced honestly in my career, where everything you try just works.

(00:05:56):
There's so many possibilities. There's not enough people in the world to work on them. Honestly. There's more things that can be done than there's people available to do them. It is just such a rare thing. And honestly, it's not going to last forever. We are going to catch up to this, but just feels lucky to be part of that movement. It's awesome.

Lenny Rachitsky (00:06:17):
When you said everything is working, I think what's an important distinction there is the building of the tool works. The tech is now there to build all these things that have not been possible before. The thing that is increasingly, difficult, and I want to get your take on this, is getting anyone to pay attention and stick with your thing because it's so easy to build stuff and everything is just awesome and interesting. It's harder to get people to pay attention and stick with your product.

(00:06:42):
So I guess is there anything there, you've learned that you've built a number of successful products. We'll talk about Snap and what you're doing now, about just, I don't know, what you need to think about these days to get anyone to pay attention and then stick around.

Gaurav Misra (00:06:54):
Yeah, I mean honestly it's a great point and I think there is a lot of hype obviously, and part of it, that's what's driving a lot of this growth for a lot of companies. And I think from a user acquisition/marketing perspective, in a world five or seven years ago, if you were making something novel and you went to users and it was like, "Oh, we got something better." People are going to be like, "Well, whatever. Everybody says they got something better. I don't care." But today, and this is not probably the way you should do it, but you can go and just say, "We've rethought this thing with AI." And a bunch of people will just be like, "Well, how?" Or "Maybe I should check this out."

(00:07:33):
They'll just try it. Obviously, you have to deliver on the promises. If you don't deliver, people will come in, they'll play around a bunch and then just leave. But if you can truly deliver on the promises, there's great opportunities to require users at scale. So I think that's slightly different. And I don't know how long that lasts, but it is definitely a different time from that perspective. I do think also at the core of building products is solving problems. I think a lot of people sort of get caught up in this, well, it's cool and people will come for the cool right now. People will come in and be like, "Well, let me check it out. It's cool."

(00:08:11):
But at the end of the day, if you're just building a playground and people play around in the playground and then they leave after playing around, it's not a business. So I think that is still key. You have to be solving real problems.

Lenny Rachitsky (00:08:25):
As we were talking, I'm thinking about every day there's something that would maybe a few years ago be news for a year. Holy shit, this is now possible. Now it's like every day something like that happens and then we're like, all right, so what I think about is like, we'll have AGI one of these days or super intelligence and everyone's going to be, "Oh, amazing." And then, "Okay, what's for dinner?"

Gaurav Misra (00:08:46):
Isn't that already happening? Think about, in a way, I self-reflect on this sometimes if like, you've seen Iron Man and stuff, they have the J.A.R.V.I.S thing and you've seen Interstellar and they have the TARS machine. They're talking back and forth with these things like bouncing ideas. That is science fiction. That's literally science fiction. Okay, it's not perfect, but it exists in a way that nobody could have imagined. That's science fiction has become reality and I feel like nobody cares.

(00:09:18):
In a way, you would've expected the world to be turned upside down, but it feels like almost in a way so slow and people are like, yes, adoption is happening, but I feel like it's almost a shocking development in a way.

Lenny Rachitsky (00:09:31):
It feels like you guys have done a good job staying top of mind and continuing to get people excited because to your point, there's so much happening. How do you get people to continue to be like, "Oh, okay, wow, what their building is actually is interesting and continues to be interesting."

(00:09:45):
Anything you've learned about just what it takes to stay top of mind and continue to pull people back and get people re-excited over and over?

Gaurav Misra (00:09:51):
Hundred percent. I mean, I think honestly it just comes down to not just AI for the sake of AI or AI for the sake of excitement or hype or novelty or whatever that is, it's actually effective AI like AI that solves real problems, practical problems. And the fundamentals haven't changed. In a way, there's three steps to building products. You identify a user problem, you apply some technology to solve that problem, but then finally you have some mechanism to find people who have that problem. If you can do all three of those things, then in any environment you can create great products. But I think right now what's different is so much is changing on the technology side that you can create products that could not have been created before and solve problems that could not have been solved before. And that's creating the opportunity.

(00:10:45):
And for us, especially in the video space, it's truly endless. We've just begun, our goal specifically for video is not to build professional tools. We're not building for professionals at all. We're building for the person who could not have created video before. They didn't have the tools, the skills, the means to be able to create video and now they can because they're able to jump over that skill gap or that time gap. Maybe they're business owners, they don't have time, they want results, and honestly a lot to solve there just tons.

Lenny Rachitsky (00:11:20):
Solve people's problems. Easier said than done, but it's a good reminder. In the end that's all that matters. Something that I always think about with people in your shoes is just how do you not get overwhelmed and how do you know what to pay attention to? How do you stay focused?

(00:11:36):
Any tips there for folks that are just reading every day, a new announcement, and then just like I just, how do I? What do I do? There's too much.

Gaurav Misra (00:11:44):
It is the new problem of product development in a way. There's too many possible paths you can go down. There's too many ideas, there's too many things you could do. And I mean obviously, prioritization is always an important skill set and has always been, but it's become an even more important skill set right now because you have to figure out what not to pay attention to. Our general framework for it is to look for user demand, and actually the easiest way to check for user demand is to just see what has virality.

(00:12:10):
Usually, what has virality and what people want to share and talk about, there's something at the core of it that actually is interesting. Now, it may not always be interesting in a way that's like maybe it's a one-time use case. Maybe it's not something that people would do repeatedly. Maybe it's not something you could build like a subscription business off of, but oftentimes there's some things, some core element of it that has resonated with people. And if you can identify that core and then mold it into fitting into your business, it's actually a great way to identify what actually works. And we have these tools right now. We don't have to build anything. You can just kind talk about it and people will share it, share the idea.

(00:12:49):
And you can measure how well the product might be received even before you built anything. So it's a great tool we use for prioritization. We spend a lot of time on social media. Obviously, our app is often used for social media, so a lot of our employees will spend a lot of time on social media. We look at what the trends are, what's happening, and based on that we can get a pretty good read of what might resonate well with people.

Lenny Rachitsky (00:13:15):
So as a leader of a company with people constantly hearing about all the things happening, is there any tools or processes or approaches you've figured out to help people continue, stay focused, not get excited about every shiny new object and actually ship things? I

Gaurav Misra (00:13:30):
I mean honestly, it's all about incrementality in a way. I think we do aim to ship every week. Our engineering goal is every engineer should ship a marketable product every week. And so what's a marketable product is a product that you can show to users and the user might subscribe or pay for the app just for that or come to the app essentially just for that. And that's why table stakes features, let's say we're talking about word processor or something. If you had auto format or just table stakes stuff like justify alignment or something, no one's going to come to your word processor for justify alignment. You can market that because it's obvious, of course it exists, but if you did something unique that nobody else has done, you can go and show that to people and people will come to your app just for that.

(00:14:22):
And even if your app doesn't have a lot of the obvious stuff, maybe it doesn't have justify alignment, people will jump over that just to use these new tools and new abilities that you might be building and marketing. So we try to do every engineer one marketable feature per week, and a lot of that stuff may not work, but a lot of it does work and we can figure out obviously, where to put in more effort, things that start to work, we double down on those things, build more. People often complain because think about it, in one week where we're shipping, it's not complete, it's MVP, truly.

(00:14:57):
And we slice the hell out of it. We take the design and we cut, cut, cut until we can really say that it's going to be useless if we cut anymore. We get that out and people come in. And if things are going well, people will use it despite all the problems that it might have, and now people will complain and we'll have a list of problems and we know what to do next. That's a starting point essentially. As long as we're shipping one a week, we get a ton of volume of features and products and directions we're releasing, cut a lot of that. What remains expand from there. So it works really well, and it keeps people focused.

Lenny Rachitsky (00:15:37):
I love the simplicity of that. I love just how wild that sounds for a lot of companies I imagine. Every engineer ships a marketable feature or product every week.

Gaurav Misra (00:15:46):
Yes.

Lenny Rachitsky (00:15:48):
There's some people listening to this and are just completely stressed out by this idea and there's some people listening who are like, this is exactly how I want to work. This is how every company should build.

Gaurav Misra (00:15:56):
Yep.

Lenny Rachitsky (00:15:58):
How do you maintain quality and make it all cohesive? I imagine that's the big trade-off. Just, any tricks there for folks that want to maybe start operating this way.

Gaurav Misra (00:16:06):
Quality is not something you compromise on most of the time. I think yes, there's strategic compromises in quality, but most of the time what you want to do is have a bar for quality where people should come in and if they're using the feature, it should work, right? Of course. And the way to cut down on time, and I think this is a mistake people make a lot of the time, is when time is being pressured downward, a lot of times engineers, PMS, designers, they will cut on quality rather than cutting on scope. And actually you can cut on scope. It's actually, the method that we use is we look at every element that's going to take any time to build and we just say, what if we remove this? Is the product still useful?

(00:16:48):
And we keep repeating that until we remove whatever's left and we say it's going to be useless at this point. And that becomes the one-week project, right? It actually really works. It narrows down to the core of what you're really trying to ask. So for example, let's say we wanted to build something to add an image on your video or something like that, and this is a really basic idea. I just made it up right now. And you might imagine a design in which you import your image from your camera roll, but before it lands in your video you might want to remove the background. You might want to change the hue and saturation or something like that. And you might expect a designer to design all of those features and you let it design, but you really quickly realize that you can cut all of that stuff.

(00:17:38):
You can cut the background or you can cut the hue saturation. All you really need is pick. And then there might be a picker. We need a picker with a library, with a lot of different type. What if you want to pull from the cloud? What if you want to pull from the drive or something like that? Cut all of that, right? And essentially come down to the core, which is just native picker from the camera, lens, straight in the video, no UI. And that is already, that should be useful. If that's not useful, then anything else built on top of that is also useless. So that's how we might go about it.

Lenny Rachitsky (00:18:12):
That last sentence is so key to this. It's the core idea of ship small iterative features before you invest a lot in something to figure out is there anything there, is this worth spending weeks on?

Gaurav Misra (00:18:24):
Totally. And I think the coolest part of this method is the first thing that the users will come in, they'll use the thing, they'll import images and the first thing they'll complain about is what bothers them the most? Is it human saturation? Is it background removal? Is it picking from the cloud? You'll just get the most complaints about that thing.

(00:18:43):
People will be like, and people will be honest about it or they'll be like, "This sucks. It doesn't even have background removal. What kind of image thing is this?" And you have to take that feedback and just next week you can ship in a single week all the things that the user's complaining about.

Lenny Rachitsky (00:18:59):
And then they're like, wow, this team is shipping like crazy.

Gaurav Misra (00:18:59):
Yes. Exactly.

Lenny Rachitsky (00:19:01):
Solve all my problems. So responsive. This connects a common sign of product market fit, which is when people are complaining about the thing that means they actually care enough to complain and that's a really good sign if they're complaining about something.

Gaurav Misra (00:19:13):
It's very true, very true. If nobody complains, it's almost red flag.

Lenny Rachitsky (00:19:18):
A lot of this is turning into an archeology of a modern product team and startup. So I want to keep digging. This is not where I was planning to go, but this is awesome. I love that this approach of every engineer shipping something every week that's marketable connects directly to where I started this conversation, which is how do you stay above the noise?

(00:19:36):
And part of the answer is just ship stuff constantly, and just continue to impress people. Like, "Here's a new amazing video feature." "Look at this thing."

Gaurav Misra (00:19:43):
Exactly. Yep. I think it's definitely key, right? And there's enough area and enough scope for that to happen. I think truly in normal times it may not be possible to create that much roadmap that quickly, but I think because there's so much innovation underlying all this, there is that scope available. The roadmap almost seems unlimited, just truly.

Lenny Rachitsky (00:20:07):
Okay. The other question I imagine people would be wondering is how do you work on longer-term projects that take many weeks? There's also infrastructure, I guess, back-end stuff. So maybe answer those questions.

(00:20:17):
How do you think about long-term stuff and then how do you deal with back-end stuff that isn't a feature that anyone would care for?

Gaurav Misra (00:20:22):
Yep. Usually, we'll dedicate time to that separately. For example, usually Q4 for us is infrastructure quarter. We just go and build all the infrastructure. Q4 is generally, we've already delivered a ton of products and stuff. We're feeling pretty good about the rest of the year. Things are winding down. Obviously, holidays and stuff coming up. And so we spend all that time paying the technical debt.

(00:20:48):
I actually think there's a unique thing to think here about technical debt in general. And as a startup, your job is to take on technical debt because that is how you operate faster than a bigger company. Bigger companies don't take on technical debt, they pay it usually right away. Or they're paying back technical debt from the days when they were a startup, and they took on a lot of it. I mean Snaps, I used to work at Snap and there was a lot of examples of that over there, and I'm sure it happens at every other company.

(00:21:19):
And we think about it as like, well, is this a problem we need to solve today or is this a problem that the 50th engineer or the hundredth engineer or the 500th engineer can solve? And if it is a problem that a future engineer can solve, we should use that future engineer now. Essentially, that's what we're doing. And we're saying we're going to push this to somebody in the future. And by the way, if the company fails, that engineer will never be hired and all this won't matter anyways. So it's like financial debt in many ways. Financial debt is taken on to create leverage. It can be a good thing like if you're buying a house, you take on debt and you can buy something probably more than you can afford without taking on debt.

(00:22:04):
And it's the same thing. You can create products that you wouldn't be able to build with a small team that you have by taking on strategic technical debt. It's very positive actually.

Lenny Rachitsky (00:22:13):
Wow, this is such a cool idea. And where my mind goes is that future engineer may be an AI agent engineer.

Gaurav Misra (00:22:19):
Exactly, yeah.

Lenny Rachitsky (00:22:21):
Just solving problems, just on technical debt in you.

Gaurav Misra (00:22:24):
Exactly. Some engineer in the future Five-hundred engineer many years from now will get a promotion because they solve this big problem that those really bad early engineers created.

Lenny Rachitsky (00:22:36):
So obviously, there's a line to this. There's only so much debt you can take on before you become a big problem.

(00:22:43):
Is there any thoughts on just that balance of just how much is too much and how if it's enough for a net feature engineer or just-

Gaurav Misra (00:22:50):
Yeah, I mean I think generally the rule of thumb is every piece of debt that you take on you have to pay interest on. So if there is debt that you've taken on, there's 1% or 2% of your time that is going to be taken away every day in maintaining bugs and issues and restarts and crashes and things that are happening with that. Because you did it the fast way, something's going to go wrong with it. Every day. 1% of your time will be taken away. If you take on enough debt, you'll be paying 80 or 90% interest and you'll not have any time to do anything new. You'll just be paying interest. That's all.

(00:23:23):
And that's when you get into the mode of like, oh, we're just keeping the lights on. We don't have any engineers to do anything. We're just keeping the lights on. That's the failure case for a startup. So in a way, you have a technical debt runway. Once you run out, once you've taken on too much debt. And if you haven't delivered value in that time, enough value to hire the engineers to pay the interest or just pay off the debt, you'll get in trouble.

Lenny Rachitsky (00:23:46):
I love that. That's such a nice heuristic of how to think about when to invest in something. I don't want to go down this too far, but just a thought I have is ... because sometimes there's big technical decisions you got to make that impact the way everything builds or is built in the future. I imagine those you spend more time on and take really seriously.

Gaurav Misra (00:24:02):
Definitely. Yeah, I mean I think as long as it's possible for wherever it's like a two-way door, you can do whatever you want. I mean this is a classic methodology. If it's A one-way door, it's worth thinking about and sort of doing correctly at least as much as the one-way door would matter to you in the future.

Lenny Rachitsky (00:24:22):
How much do your engineers use Cursor and tools like that to build? How much is AI helping your team move?

Gaurav Misra (00:24:28):
A hundred percent, yeah. I mean everybody's using it. It's super helpful. I mean even I'm using it honestly. Yeah, it's a huge multiplier for the team, no doubt.

Lenny Rachitsky (00:24:40):
And is a Cursor specifically. Is there anything else that you guys found useful?

Gaurav Misra (00:24:43):
Yeah, we are using Cursor. Yep. We've tried all the different tools. We were using Devin as well, which is another, you know? That's more advanced, I guess. It's solving bugs for you.

Lenny Rachitsky (00:24:52):
Yeah, Devin's basically, I think it's 500 bucks a month and it's like an AI engineer that you just chat within Slack.

Gaurav Misra (00:24:58):
Exactly, yeah. In a way, these are the types of things that us as a startup can do that bigger companies can't just, you know, they can't just pull in Devin. They have to get 30 lawyers in the room first before that happens.

Lenny Rachitsky (00:25:11):
And they're all called Devin, these are like agents. Everyone's going to have hundreds of Devins working at their company.

Gaurav Misra (00:25:15):
Exactly. You can have multiple Devins. I actually heard you can have a manager of Devins who's managing Devins.

Lenny Rachitsky (00:25:21):
I love that managers are all getting layered, like unlayered and then they're going to have AI managers. That's the ultimate bait and switch.

Gaurav Misra (00:25:30):
Yep.

Lenny Rachitsky (00:25:32):
Okay. Is there anything else that in how you operate and build the way you build product or set up the way you build product that you think is really unique and interesting that other people might be able to learn from?

Gaurav Misra (00:25:42):
Our process is a bit interesting in that way. We have a design team, we have a PM team. We're very early on those teams right now. And obviously, we have engineering. And we have all the different surface areas. So iOS, Android, web. There's backend team, machine learning team, research team. So generally, when we're developing products, we may start off with a PM first approach where we're finding some sort of overall issue that we want to take on some new area or pillar we want to take on and then creating sort of product specs from there.

(00:26:17):
But a lot of times we'll also start the opposite way. We'll first design something without even having any idea of what or why we're doing it, but we'll design a bunch of different things and then we'll sit down with the PMs and look at the designs and just go over one and the next and the next until we find interesting things and ideas that pop out of that.

(00:26:36):
And a lot of times that leads to us discovering things that we wouldn't have discovered if we were just too focused on the metrics and the numbers and things like that. So it's almost reversing the process a little bit and starting with design first, but it can often result in finding unique ideas basically. I also think that we have a unique setup in how we create our roadmap. So normally you have a single roadmap and we actually divide a roadmap into two different roadmaps. So we have what we think of as the public roadmap. This is basically what people have asked us for. So there's all these surface areas where we receive user feedback and we look at all that feedback and people will ask for features. They'll ask for, I want background removal, I want to undo and redo, I want to upload longer videos, whatever it is, a bunch of different features.

(00:27:26):
And we'll just make a list of that. And just like anything else, we'll prioritize it and we'll look at how many people it affects and what the possible markets are and just get it done basically one at a time.

(00:27:37):
But these are all features that every competitor knows about. These are public. If a user's asking us for it, they're asking everybody for it. And every team has essentially more or less the same list and everybody's prioritizing it. And yeah, sure you can win a little by extra nicely prioritizing it or winning a little in prioritization or execution or something, but it's not going to be a game changer in terms of winning against your competition. So we have a second roadmap which we think of as a secret roadmap. So this is a roadmap that nobody asked for anything on this like literally, nobody has ever asked for it.

(00:28:13):
And if a user were shown something on it, they might be like, "I don't need this. I don't know what this is." But given our unique vantage point, our unique understanding of the problem set, the user space and the technology, we've come up with some special ideas that we think will completely revolutionize how something is used where we can truly change the behavior of the user. I think that's what at is at the core of. It's like people are doing things one way if we're able to show them another way. And once they try it, they never go back. That's what a product is, that's success. And those are the types of ideas that we put on the secret roadmap. These are things we never talk about publicly, never tell anybody about, and we announce them and just give them to users and see the effects.

(00:29:00):
A lot of this we come up with through brainstorming. So we do actually do quarterly brainstorming, company-wide, everybody's included like everybody from. It's not just a product team thing, it's like engineering, recruiting, everybody's included in. And we all come up with marketing, obviously, everybody comes up with ideas, we vote on the ideas, rank the ideas, and then the product team takes over from there and thinks about like feasibility and technology and what the different things could be. So this is a way where we can take all that noise that people are getting, everybody's browsing social media, seeing all these different things that are blowing up, these models and advancements and we can get all that information together and provide a unique internal roadmap where how are we going to approach and create value out of all of these different advances that are happening.

(00:29:49):
So that's our general methodology. And a lot of times the biggest wins will come from the secret roadmap. That's the game-changing stuff. It's not going to be the user requests usually that are going to do that.

Lenny Rachitsky (00:30:02):
I love just how calling it the secret roadmap makes it extra interesting. [inaudible 00:30:07]

Gaurav Misra (00:30:06):
Exactly, yeah. It's a secret.

Lenny Rachitsky (00:30:09):
It's a secret. I'm not even going to ask you what's on that secret roadmap. You can't tell me.

(00:30:15):
What's an example of feature that came out of that secret roadmap that's been a big deal for you guys?

Gaurav Misra (00:30:18):
Tons. I mean, I'll give you an example from a long time ago. One of the first AI features we added after the app initially took off was this feature called eye contact. So this was a feature where if you're recording something, oftentimes people who are new to recording a video might read from a script or a teleprompter or something like that and they might have that off-screen. So it looks like you're reading and it's not great from the perspective of the video itself or the viewer of the video. So we had this feature where it basically shifts your eyes to look at the camera.

(00:30:52):
And we were actually the first company to build this. We worked with Nvidia on this. It's actually really interesting because when we originally reached out to Nvidia about this. They were not sure why we needed this. And they actually gave it to us pretty openly and were excited about some sort of partnership of how can we get this technology into something that could be useful.

(00:31:19):
But we saw this creator use case which was unique, and it was one of the ideas that came out of the brainstorm and we threw it on there, we launched it. It was a huge success. I mean, I'll be honest, the video, the ad that we made, a social media post that demonstrates this was so viral, it was made in basically every language around the world. It still till today gets millions of views. We find reposts and reposts of that thing that other people have created that get millions and millions and millions of views because people are like, "Wow, this is a great idea."

(00:31:59):
And now it's been copied the hell out of, I think it's available basically on every app you can imagine. For good reason of course. But that's one of the ideas that came out of it.

Lenny Rachitsky (00:32:10):
You talked about how you come up with these secret roadmap ideas. I'm just intrigued by this. I'm going to spend a little more time here.

(00:32:14):
Does your team ever work with an AI LLM to help brainstorm? I imagine that's where things will go, where you're actually jamming. The AI agent is brainstorming along with you.

Gaurav Misra (00:32:25):
Honestly, I would like for it to go there. It hasn't gone there yet. We haven't done that exactly, because the problem is context. And I think just the context of understanding the user, the use case, it's so abstract. Even right now, I feel like I understand our users obviously, but I can't exactly verbalize why that is or how that is, a little bit abstract. And I spend a lot of time with RPMs and designers imparting anything that I understand and I've learned over the many years I've been working on this, how do I impart this to them? But then it's a challenge because I can't even verbalize it myself. And so it's an extra hard challenge to figure out how do I put this context? How do I make it available to an LLM when I can't even put it into words exactly. And honestly, this is probably my own feeling but, and I need to work on this, but there is something to it.

(00:33:26):
I do remember at Snap for example, I think one of the most unique things about Snap and the CEO Evan Spiegel was that he had an unmatched understanding of the user. I think years and years and years of the company's existence past, almost a decade. And nobody understood the user like he did. He would come up with ideas that everybody would disagree with and we would launch them and there would be hits, just hits after hits. And nobody would understand why. Everyone would line up and be like, "Great." Round of applause for everyone, but no one knew why.

(00:34:07):
A great example of that is a lot of this was figured out in retrospect too. I think there was a point at which Snap declared that they're a camera company and a lot of people laugh at them and said, "Camera. What are we making digital cameras or something?" Or, "Why is it a camera company?"

(00:34:22):
But I think at the core of it was this idea that Snapchat opens to the camera and that was actually the differentiator. That actually that small decision was holding the entire company against all competition because when the moment passes where your friend is doing something funny and you need to capture it, you're not going to open Instagram or anything else because it doesn't open to the camera. You're going to open Snapchat because you can capture it right away. And Instagram can never copy that because all their metrics are going to go down as soon as they do that. So that is a fundamental understanding. And I figured this out much later, actually, but it's such a powerful idea.

Lenny Rachitsky (00:35:08):
I'm glad you talked about Snap. That's where I definitely wanted to go. This is where I was going to start. So I'm glad we circled back to your experience at Snap. So the reason I am interested in this is if you think about social networks like Snap is basically the last social network to have launched and stuck around other than TikTok, which I don't think is a social network. I think it's just this content platform. I don't think you're really interacting with people really. And that was 2011 when it launched. So it's been like 15 years since the last social network launch that has worked.

(00:35:40):
And I think it's interesting also because there's rarely been a lot of insight into just how Snap operates. You were there really early. You're a big deal at Snap. You built a lot of really important features. So I wanted to spend a little time here, and it feels like a lot of things you learn from Snap you're bringing to your company now. So let me just ask, I think you may have answered this, but I'm curious if there's something else here just broadly maybe other than Ev's brain, what do you think was core to Snap being a successful consumer social product?

Gaurav Misra (00:36:12):
There were a couple of different things that went well. I do think for a company like Snapchat or Social Network, the core product market fit can be extremely strong. Essentially, the reason that people are downloading it, the way that it's spreading, the way that it's distributing, the way that it's inviting friends or sending Snaps or whatever it is, that product market fit can be so strong sometimes that it can be hard to actually build something because you actually can't tell if what you're building is what's responsible for growing the thing or if it's actually hurting it and it's growing despite what you're doing basically.

(00:36:53):
And I think because of that, it actually sometimes teaches people the wrong things. It teaches people that the contrarian thing that they were doing was right when it was actually just wrong and the company just grew despite it. And I think some of the things that Snap did well and it needed to do really was to continue innovating, right?

(00:37:17):
Because for a company like Snap, it has a ton of competition. Social networks are monopolies by nature and there's a lot of reasons for Facebook or any other social network to stop the growth of Snapchat. And they tried, they tried really, really hard. And the way that Snap was avoiding that was by innovating. I think the core of it was the setup that they had, which was very unique. I've never seen anything like it. I've worked at a bunch of different companies, but obviously there's a CEO and the CEO was very product-led, his designer himself, but he surrounded himself with the design team. That was sort of the central team in the company. And the design team was like 10, 12 people. Basically, pretty small, even at 5, 6,000 employees it was that small still.

Lenny Rachitsky (00:38:02):
Oh wow. At 6 or 6,000 employees. The design team was, you said how many, five or six people?

Gaurav Misra (00:38:07):
10, 12 people.

Lenny Rachitsky (00:38:08):
10, 12. And to add to that, there's no PMs really for a long time. That was before.

Gaurav Misra (00:38:12):
For a long time, yeah.

Lenny Rachitsky (00:38:14):
Big difference.

Gaurav Misra (00:38:14):
Initially, there were no PMs at all. PMs were introduced with monetization. Once monetization was a big sort of element, that's where PMs came in. Today, I think there's a ton of, or there's an adequate number of PMs across the company, but there was a long period of time, especially when the innovation was happening, when there were a much, much smaller number of PMs and it was very designer led. But at the same time, I think that's slightly misleading in the way that these weren't your sort of average designers.

(00:38:43):
These were designers who were actually PMs as well. That's what the secret sauce was. They were able to not just design but also do the PM part which is a big responsibility. It's a lot of work, especially for that many employees, but it gave the CEO a way to have granular control over what exactly was being launched in which part of the app at all times.

(00:39:05):
Because he could meet with a set of 10 or 12 people and know every change that was happening that was user impacting. A lot of changes were being worked on that were infrastructure and types of things that keep going on in the back end where you're improving ranking and whatever that might be, performance and things like that. And those were not usually his concern. He was concerned with what UI are we adding where? And if you needed to add UI to the app, you needed it designed. And if there's no designers in the company, except for a handful who talk directly to the CEO, you create a very granular control over what's being launched in the company. So everything needed to be approved by Evan. If you hadn't approved it, it's not going out. So the design team actually held a lot of power in that.

Lenny Rachitsky (00:39:50):
This is awesome. So what I'm hearing partly is, I don't know if this is true, but it feels true that to make a consumer app that is successful and breaks through, you almost need a singular mind that continues to stay in the weeds on everything. And the way Evan did that is very close to the design team who basically ran product.

Gaurav Misra (00:40:10):
That's very true. Yeah, it's very true. And he was able to keep the context of the entire app in his head at the same time. He knew the interdependencies and what we're doing and why we're doing it. And so that gave him just very granular control over the company's product roadmap.

Lenny Rachitsky (00:40:26):
It makes me think about Brian Chesky and Airbnb is a consumer product, it's not a social network, but I wonder if that's just an interesting insight just for consumer products. They will generally do better if there's one person with a really ... the right sort of combination of experiences, insights, and just they continue to run and own every detail.

Gaurav Misra (00:40:46):
Definitely. And also the ability to bring about change, the ability to truly energize an entire organization to do something that's not just incremental but fundamental.

(00:40:58):
<< Founder mode >>

Lenny Rachitsky (00:41:00):
Exactly.

Gaurav Misra (00:41:01):
Founder mode. That's what we're getting to, basically.

Lenny Rachitsky (00:41:04):
Yeah, ever heard of it. Okay. And then you said that these designers, so I know it's famous that Snap had no PMs for a long time. Designers were PMs. This point you made about the designers where PME is really important. I think a lot of people look at this, they're like, "Amazing. We're just going to hire just designers. We don't need all these PMs. Slow everything down. Just tell us what not to build." Can you just talk about the level of these designers? What allowed them to be as successful as they were without any PMs?

Gaurav Misra (00:41:32):
Yeah, I mean I think what was expected from the designers now was not just the ability to design, the skill set of designing, which all of them were IC designers by the way. And there were no reports, so they weren't allowed to have reports actually. And so they were designing everything themselves, but they also had to have the leadership skills to go figure out the roadmap, write all the documents, work with the different teams, figure out shipping schedules and just know everything, not just the technical and the engineering part, but the UX and the UI and the product needs and why are we doing this.

(00:42:15):
The roadmap, there's just a ton to keep in mind. And that means that it was a job that was just highly ... it was very high workload. No doubt, very high workload. These people work really hard and they were paid highly too. For what it's worth, they were paid way higher than you would expect designers or PMs or engineers to be paid with quarterly bonuses and all kinds of things.

Lenny Rachitsky (00:42:43):
That's interesting. And it reminds, people always say, "Why do you need PMs?" There's like someone has to do the work that a PM does. They're not sitting around doing nothing. And it's important to note the person that will take on the PME work, they have to be good at it and enjoy it. And a lot of designers don't want to be doing writing docs and organizing stakeholders and getting alignment and ...

Gaurav Misra (00:43:03):
100%, 100%. That's why it was so hard to find those people who were able to do two things. I actually think there's an insight in there is innovation between when you're merging craft right between two different functions. And I do think there's something special about one person doing two different functions or at least being able to do. And I think a lot of unique insight and innovation can come from that.

(00:43:31):
I actually think on my personal side, I eventually joined the design team. I started at Snap on the engineering team. I eventually joined the design team over the last two years that I was at Snap. And a big part of what I did there was create this function called design engineering. And that was actually a different combination. It wasn't the designer PM. It was the designer engineer. The person who can think of the UX design it and also build it and launch it, all of those things.

(00:44:03):
And we saw both the ability to take designers and teach them engineering and take engineers and teach them design as part of that. Obviously, the reason that we created that function was very different. It was actually to continue innovating as the company got bigger. One of the problems that we identified was that as the company got bigger and bigger and there's like 500 engineers, 1,000 engineers, 2,000 engineers, 3,000, suddenly it just becomes very difficult to do everything.

(00:44:32):
Everything is a six-month project or a one-year project. Every product is a massive investment of 500 engineers and a lot of time. And so you really have to pick your bets. If you get it wrong, if you are innovating and trying to create new products and you spend 500 engineers for a year and it doesn't work, it's a big problem. You're going to be in trouble, especially if we're coming like Snap where everybody was copying what they're doing so they had to constantly innovate, create new stuff and push the bounds.

(00:44:59):
I think Evan's philosophy was always he didn't fight the things that were getting copied, right? Stories got copied pretty much straight up. A lot of things that Snap created got copied, but he was more of the mindset of like, "Let's expand the pie, do something new and push the boundaries." We'll keep innovating basically. And so to do that with that scale of a company becomes really hard. And so we had this idea of let's create a small team where we can go and pretest a lot of these ideas because we had a lot of ideas and we can't go and build all of these things. So the idea was create a small team of these design engineers, people who are able to do the entire product design engineering process in their head and can put together early versions of the product, which we would actually bake into the Snapchat app itself.

(00:45:46):
And we were able to even test, for example, run a test in Australia, see how it's performing. Run a test in a couple of high schools, just a couple of high schools, see how people behave. And that way we already have data on how this might perform in a real world environment, but we haven't built it to production level. It's a prototype, essentially. It's how a startup might build something.

(00:46:08):
The same idea of what we're doing at our company now, build fast, get it out there, get feedback, understand whether it works or not, and then work with the engineering team to build it at a scale. Once we understand the product and the dynamics, then it makes sense to put on 500 engineers for six months to build it.

(00:46:25):
So that was a big part of it. I think the nice thing that came out of it that was completely unexpected but actually transformational for me in a way was obviously in big organizations, alignment is a big issue. How do you get everybody on the same page? And a big part of a PM's job is actually to create alignment and it can be a lot of work because you go talk to all these stakeholders and get them on the same page.

(00:46:48):
But one of the insights that we had, which was unique was as the company gets bigger, you can actually create alignment by causing internal virality. If there's enough people in the company, it actually starts acting like a consumer base might. If you share something interesting with someone, they will share it with somebody else because they think it's interesting and you can actually create virality inside a company.

(00:47:16):
So one thing that we would do is we would create these prototype products. We would just go into an area, redo a bunch of stuff, create these prototype products that didn't exist in Snapchat normally, and then we would just share the build and it would explode. It would just go viral inside the company. Day after day we would hear from engineers, then managers, then VPs, then eventually from Evan being like, "Oh my God, everyone's talking about this. Why am I the last one to hear about it?"

(00:47:47):
So it would create instant alignment across the company of this is exciting, this is something that we want to get behind. And everyone would be asking, "When are we doing this? When is this happening? I see someone's already working on it." So it was a great way to do that. And once we really understood that the product actually had good dynamics and we had tested it, it was a great way to get it out in front of everybody and create this idea of, "Hey, we're all working on this. This is the future."

Lenny Rachitsky (00:48:17):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast. It's where I put my community resources. It's how I manage my workflows. Here's how Coda can help you.

(00:48:35):
Imagine starting a project at work and your vision is clear. You know exactly who's doing what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs to documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all in one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab.

(00:49:04):
Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's coda.io/lenny to get started for free and get six months of the team plan. coda.io/lenny.

(00:49:34):
Another thread I want to follow up on is prototyping. It feels like that is where a lot of PM work is going is getting straight to a prototype versus design or versus PRDs. And it feels like that's something that you did and worked super well. Basically, it's a team to prototype ideas that in theory now you can just build really quickly with AI. So I think that's really interesting, seeing where the feature's going, just ...

Gaurav Misra (00:50:00):
100%. Getting things in people's hands, trying it out. Oftentimes, unless you truly try it out, in design, it can, in theory, look good with all the perfect conditions, but when you actually use it, you realize it's actually not that useful, for example. Or when you give it to users. And some of this is intuition, honestly, just like anything else, but there's nothing like getting something in the hands of users at the end of the day.

Lenny Rachitsky (00:50:23):
I love how many of these things you brought over to your current company, and I'm trying to think about, one is this idea of just constantly innovating feels like that's informed and tell me what I'm missing, but that feels like that's informed. The ship market will feature every single week. This idea of getting design, starting almost with design versus PM a lot of times. I'm curious why you don't even go straight to prototype in those cases. Is it just the tools aren't there yet or?

Gaurav Misra (00:50:47):
I mean, I think our shipping process is fast enough that within a week we can get it out anyways. So that way we just get user feedback, which is even better.

Lenny Rachitsky (00:50:55):
And then the other really interesting thing, I'm trying to visualize that triangle of a product team, the triad of PM, engineer, design. Feels like you guys at Snap took the corners, not the corners, the line of that triangle. And you have design engineers. You have design PMs. I imagine engineers were PME already. They're very product oriented PMs. Did you have a function called design PMs? Probably not.

Gaurav Misra (00:51:20):
I mean honestly, it's interesting.

Lenny Rachitsky (00:51:21):
Sorry, engineer PMs.

Gaurav Misra (00:51:23):
Yeah, engineer PMs should be a thing, I feel like, or every engineer should strive to understand the product, right?

Lenny Rachitsky (00:51:29):
Yeah. A lot of companies operate that way. Like Stripe, I think they had hundreds of engineers before they hired the first PM because I think the engineers were doing what they did at Snap to do the PM work. So it feels like at your company you don't operate that way. It feels like you have PMs, engineers, designers. Talk about why you decided not to approach things that way.

Gaurav Misra (00:51:48):
I do think PM is a very valuable function. I think it may be actually, and maybe I'll get roasted for this, but I think at the end of the day, not hiring PMs at Snap might've been one of those decisions where it actually succeeded despite that and because someone needs to do that work. If you don't have enough people to do it, then nobody truly owns it and then it doesn't really happen. Or if it doesn't happen, no one's responsible, which is not the right structure you want in an organization. So I think though, that being said, there was something unique to be said about what if a designer had the PM mindset.

(00:52:29):
It's actually the same idea as what if an engineer had the PM mindset and then you get even crazier. What if the PM had a design and engineering mindset? I think all we're talking about is everybody truly understanding all the functions that they're working with. Having a fundamental, broad understanding of the functions they're working with.

(00:52:48):
At Captions, we're actually going even one step further than that. Why shouldn't the PM understand marketing? I think that's actually the biggest opportunity for PMs to understand is how do we actually find the users who have this problem? I think that's a big part of solving the problem. I have a unique take on this in terms of I actually think PMs should own all the way to marketing in a way. And the reason is that if you think about marketing, it's expanding the surface area of the product, right? It's like search marketing is just placing a button to your product in Google.

(00:53:28):
Facebook ads is just placing a button to your app in Facebook. It's almost like you work at Facebook. You work at Facebook, you have a button in the app somewhere, you make a specific thing and people show up. The funnel begins there and you have all the metrics all the way from the beginning, all the way from when the user tapped on the button in Facebook and then they went down all the steps and then they landed on some onboarding screen and they did the thing, they used the application.

(00:53:56):
That's where the journey begins. And all of that is, in a way, it's a product. It's the same skillset. Understanding users from that point on is I think that's fundamental. How do we not do that today? We should be. So that's how we think about stuff. But I think the core idea is that every function should understand every other function deeply as much as possible and maybe even to the level where they can operate in that function. And that just increases the likelihood that all decisions being made in the company at the micro level will be optimized for all possible parts of the funnel that different people are essentially looking after. That's something we think about quite a bit.

Lenny Rachitsky (00:54:44):
I completely agree with that take. It's interesting that at Airbnb, Brian was famous for changing the titles of all product managers to product marketing manager for exactly this point because he's like-

Gaurav Misra (00:54:56):
Makes sense.

Lenny Rachitsky (00:54:57):
... you should be doing the marketing, you shouldn't just be building the thing. And to me, I've always assumed as a PM, your job is for this thing to grow and to get adopted and be loved.

Gaurav Misra (00:55:07):
Of course.

Lenny Rachitsky (00:55:07):
So it's interesting people don't already think of it that way.

Gaurav Misra (00:55:10):
I agree.

Lenny Rachitsky (00:55:11):
But obviously, it's hard to learn the skills of being awesome and paid growth and SEO and product marketing, messaging, positioning, but I completely agree. That's such an important element of building a product. You're not just building a thing, hope it works. Goodbye. So I love that that's how you think about it. And so I guess when you hire PMs, it sounds like you look for marketing instinct and some experiences.

Gaurav Misra (00:55:31):
100%. And at least the ability and instinct to be able to learn it.

Lenny Rachitsky (00:55:38):
Yeah. Okay, so I'm going to share one other thing that I thought as you were talking that I think is really interesting and it comes up a bunch on this podcast and this connects back to Ev and what we can learn from his success. So Patrick Olson once tweeted this tweet that has really stuck with me, which is it was around user research and the way he described it is user research isn't go to user research that informs what you build and then you build that. It's instead you do user research, it informs the mental model you have as a leader, a product builder of what your customers need and what pains they have, and you adjust that model in your head and then that's how you decide what to build. And it feels like Ev is very much that. His head was learning what people need, teens in particular, and it just worked.

Gaurav Misra (00:56:28):
Yeah, I think it's very spot on. I would say though Snap didn't like user research as a function for the longest time. I think there was one user researcher in the company until, again, 5,000 employees, the post IPO basically. But I think the people that were making a lot of the product decisions and the CEO himself, of course, were very steeped in how the user behaves and how they operate. They understood that.

(00:56:56):
I do think Snap also had a unique way of thinking about how to determine if a product is within scope or out of scope of what their mission was. And I think a lot of companies use the cyber framework and we try to as well, but essentially, the idea at the core was that they want to enable private sharing in a safe way. So I think that makes it clear that certain things just are out of scope for Snap.

(00:57:28):
It's actually one of the reasons why Snap wasn't the company to discover "short form video," TikTok style stuff because it was just against the nature of the company to even try something. It was against the mission of the company. Public sharing means possibly bullying and bad behaviors, which is exactly what Snap was trying to avoid. We don't want those behaviors to develop on the app. So for example, on Instagram stories, you can share somebody else's stories to your followers. I can take your story and share it to my followers. You can't do that on Snap.

(00:58:02):
And there was a discussion about should we do this? No, because it can enable bullying. Essentially, you're not consenting to your thing being shared to my followers and that's essentially bad. So a lot of it was done based on this type of pillar-based thinking of this is our mission, this is what we're trying to do, does it fit within or is it outside? If it's outside, we don't do it no matter what the cost of it is, no matter how exciting it is.

(00:58:30):
And even on Spotlight, the big challenge was like how do you take something like that and put that inside the Snap mission? So that was something we worked on quite a bit. Yeah, I mean I think there's tons of stories about earlier versions. I mean Snap almost had essentially what is TikTok earlier than TikTok existed and it died out because it didn't align with the mission essentially, but happy to get into it.

Lenny Rachitsky (00:58:56):
Yeah, that actually would be really interesting, because interesting that these things are important. It's important to have these clear values in the mission of the company and to not focus on things that are outside that. And then you hear these stories of they had TikTok potentially. So yeah, whatever you can share there, that'd be awesome.

Gaurav Misra (00:59:12):
Yeah, I mean, I don't know if you remember this, but there was this product called Our Stories, and essentially it was MyStory, but it was a public story. And it started off with this idea of campus stories where you can post to your campus and other people can see it. And that actually started creating a lot of virality because essentially people would post. There was viral moments truly where people would post stuff like, "Oh, I think two people fell in love on it or something like that." Those types of things really went viral and it had really good engagement.

(00:59:47):
But at the end of the day, the problem was that we were against algorithmic essentially ranking of those types of things. So there was a curation team that was looking through every single one so that there's no negative behaviors happening essentially on the app. That was just not scalable. Even though it had really high engagement and was doing well, it just wasn't feasible to have a person looking at every single thing posted to determine whether it's appropriate or not.

(01:00:15):
It ended up dying out, but it looked like what was an early version of TikTok before it had launched. So I think in a way though it was a good thing because I think Snap does have a mission and I think it is solving a problem. I do think there is a bifurcation of social media at this point. There is what you traditionally think of as social networking where you share things with your friends. And by the way, remember the days where that used to be the way that apps would go viral. You would share things with your friends and then they would share with their friends and everybody was worried about friend sharing and how do you send to a friend and can I text message my friend or whatever.

(01:00:59):
That time is over. Virality now happens through a completely different mechanism. It happens through essentially algorithms that are deciding whether your piece of content is worth showing to an arbitrary number of people, and this is the new age of social media. It's TikTok, it's YouTube Shorts and Instagram Reels and so on. And I think actually it's changing the fundamental nature of how people interact, fundamental nature of how things go viral. And I actually think from a regulatory perspective, we should be thinking these as differently.

(01:01:37):
On one side, you have something where you're deciding who sees something and then on the other side, you have something where the company is deciding which means that it's semi curated, right? It's actually the company's voice. So yeah, I don't know, should Section 230 apply to that? I have no idea. Or maybe not. Maybe we're thinking about this the wrong way, so it should be interesting.

Lenny Rachitsky (01:02:03):
Wow. All right. Well, I'm out of my depth on the legality decision, so I'm going to not follow that thread, but I imagine there's something really interesting there actually. So you've been talking about just how much things are changing and I just wanted to follow that thread and specifically, you guys are at the cutting edge of what is possible with AI video.

Gaurav Misra (01:02:25):
Yes.

Lenny Rachitsky (01:02:25):
It feels like we're approaching and maybe we're there. This world where you have no idea if it's real or AI. I'm curious, first of all, just how far you think we are from that and second of all, the implications on the world where you can just generate any video you want.

Gaurav Misra (01:02:40):
It's fundamental. At the end of the day, a time where video images, audio can't be trusted actually hasn't existed for a while. If you think about ... I mean there was a world in the 1800s where there was no video or audio or images and everything was proven by he said, she said for the most part. And it's possible that if everything can be generated and anything can be created and it looks just as real as if it were real and there's no way to tell, then we might actually return to that world where there's no way to prove anything besides physical evidence or he said, she said.

(01:03:20):
And I think that's scary, but also possibly opens a bunch of new opportunity for someone to figure out how to solve this problem. I think it's going to be a big problem. I do think today, we are almost there in terms of creating absolutely photorealistic video. I mean the very recent models, a very cutting edge is just about ... It feels like a few centimeters away from achieving it, but I do think to fully get there to the point where it cannot be differentiated at all, it's still a couple of years away.

(01:03:52):
I also think that it is use case driven in a way. I think thinking about Captions for a second, we take a unique view on what type of video we want to focus on. Video generation and text to video generation. If you look at it today, it's all silent video. There's no audio and it's often what you think of as stop video or B-roll, right? You can actually make a movie with B-roll. And a lot of a movie or a TV show or a social media post or an ad actually is dialogue or monologue. That's actually what it is is people talking to each other, to the camera, interacting. That's actually what makes true story.

(01:04:35):
B-roll is supportive elements that are showing up to set the scene or something like maybe before the scene opens, you see a few shots of New York City or LA or something, and then you jump into the room and now two people are talking. So our goal is to solve the talking video problem. How do we create video where people are delivering dialogue or monologue or things like that? And that's what we focus on purely. And there actually isn't a lot of work happening in that area today and it's not a solved problem. We're getting there, we're getting closer and closer, but today's models actually bifurcate a little bit.

(01:05:15):
So there's a set of companies today that are able to create these types of what we're talking about is avatar videos. They're using this technology called neural rendering. It's actually not a technology that's affected by the transformer and diffusion model revolution or the large model revolution, essentially. This is a technology that existed separately and it doesn't have anything to do with the AI growth happening right now. It just happens to produce semi-realistic outputs, but it actually stops at some point because it's not clear how it becomes generalizable in every situation.

(01:05:55):
It has to be trained on people individually. So you might ingest a little bit of video of you and then you can generate you. And so it's a different technology and a different outcome, essentially. And a bunch of companies using this type of model, a bunch of companies are doing general text to video with no audio today. These are large generative models and they have the capability to do more, but that frontier just hasn't been reached yet. I think there's no doubt in anybody's mind on the research side that it is 100% solvable. It's just like somebody has to go do it and we haven't gotten there yet. Nobody has had the time to go and do that yet. So that's where we're at, essentially.

(01:06:35):
We're working purely on large generative models for talking videos. So that's our core focus. I do think though, from a safety perspective, we have a unique framework or how we think about it. So generally videos divide into two categories. So for us, we think on one side of what is documentation, so this is the type of video that it could be a personal video where you're taking a video with your friends and you're hanging out, you're at a restaurant. It's documenting what happened. You had fun, whatever it was, it's for your memories. And there's a non-personal version of this which is like, oh, it's like a reporter documenting a crime or something that happened or whatever it is and who was involved, where was it? Maybe it was a natural disaster or something, and this is for history. We want to see what happened.

(01:07:27):
And there's actually no benefit to AI-generated video in any of this. Actually, all of this, it's just negative. It's all negative. If we are generating fake versions of reality to fool people, there's just nothing good about that. And we want to stay away from that, essentially. We want to design products and build products that make it difficult to use for that particular use case, for anything that falls within that. And on the other side, you have what we think of as storytelling.

(01:07:56):
Now this could be ads, it could be social media posts, it could be TV, movies. All of these things are storytelling. They're designed for entertainment, they're designed for fun. And nobody believes if you watch a Geico commercial, you're not thinking that the gecko is real selling insurance somewhere out there. You know that this is fabricated and it's for entertainment. And same with reality TV even, right? It's called reality TV. It's definitely not reality and social media, ads, all this stuff falls in the category.

(01:08:28):
And if we can enable more people to tell stories and entertain other people and get their message out there, that is pure positive. This is where we want to focus. And a lot of our effort in the product and design process goes into how do we design products and build products that specifically make it really hard to use on one side and really easy to use on the other side. And that's the real challenge.

Lenny Rachitsky (01:08:53):
That's really helpful. Something that I'm really curious about as you're chatting is ByteDance just released a really amazing model. I was actually just looking at it where you put a photo in, I think, and it just creates a video of this person talking in all these different ways. Where does that fall amongst the buckets you just described?

Gaurav Misra (01:09:09):
I think that falls exactly in the area that we're in, which is talking people and that's what they're going after as well there. So that's actually one of the first examples of a large model that a larger company has released where it's able to do these dialogue or monologue videos. And I mean you yourself, you've seen it, so I'm not going to describe it too much, but as you know, it's highly expressive. It doesn't look like an avatar video. It looks like ...

Lenny Rachitsky (01:09:37):
Yeah, it's wild.

Gaurav Misra (01:09:38):
And that's because of the technology that's used is fundamentally different. It's just like this is using a true large diffusion model is what they use. Whereas most companies that are working on avatar technology are actually using something pretty basic in comparison.

Lenny Rachitsky (01:09:53):
How long has it been since that Will Smith spaghetti video? Just to give us a reference of how fast things are moving?

Gaurav Misra (01:09:58):
Oh my god, it's been so fast, right?

Lenny Rachitsky (01:09:59):
I think it's a year.

Gaurav Misra (01:09:59):
Amazing.

Lenny Rachitsky (01:09:59):
Or is it like two years?

Gaurav Misra (01:10:03):
I think it's probably about a year and a half, two years. Right?

Lenny Rachitsky (01:10:04):
Wow. We'll link to that video and then you could tell basically that video is the state of the art of AI video one to two years ago. And then we'll link to this other Omni something. I forget what it's called. I'm just showing what it's like today.

(01:10:18):
Geez, Louise. Okay, final question and this is around something that I know you have a really interesting insight on, which is that you see marketing using AI video basically as the final frontier of how people will experience AI is marketing, is seeing it in marketing channels. Talk about why you think that's the case and just what that looks like.

Gaurav Misra (01:10:42):
It comes back to what we were talking about before where the reality is that no matter how interesting, advanced and amazing a technology is, science fiction has become reality. We were talking about this. What was literally science fiction on TV is real now and most people still don't even know about it, to be honest.

(01:11:01):
My parents live in India and they are the only ones in the neighborhood that know about ChatGPT and they write these amazing notes to the community just with all these words. And people are just like, "How did you get so good at writing?" And they're not telling anybody, but there's still a ton of people who don't even know that these advancements have happened. And so adaption is actually much slower, even for the most exciting things. Of course, in tech circles, everybody's talking about it, but the reality is it takes a while to get out there.

(01:11:33):
And I think for companies that are going to succeed, they're going to have to figure out how to market these products so that they can be the ones to reach all these people that have the problems that they're now able to solve. And we think about that every day. So on that note, as a consumer product, we spend a bunch of time and money on marketing our products, and we often use performance channels and all kinds of things, but about a year ago, we would run AI video in ads and things like that, and we would get all these comments of people being like, "Oh my God, this is so fake. Don't show me this."

(01:12:08):
And around that time, the technology got just about good enough that suddenly, those comments stopped happening and suddenly, you could get performance that was even better than actually recording with a person because you could just try more things. You could just generate 30, 40 possibilities and one of them would win and it would win more than the one creative you can get from a person. And more interestingly, when you think about localization, you're going to go do that in every language. Once you discover winning creative, now you have to go localize that in every market and rebuild it from scratch.

(01:12:51):
It's just a ton. And oftentimes it doesn't perform as well because it's been rethought essentially. But we found that just translating it with AI was able to get performance almost as good as the original, in the original language. So this is going to fly to the entire market. I think wherever there's dollars to be made, saved, it is inevitable. It will be consumed and it will very quickly be a lot of social media.

(01:13:21):
I mean, you could imagine a social network of the future where, and this is dystopian by the way, so watch out. You could imagine a social network of the future where all content is generated. None of the people are real. I mean, the algorithm isn't tailoring whose content to show you, but it's purely generating content that is completely catered to you, with people and everything completely catered to you. I don't think it's out of the question. It almost seems inevitable in a way, but that's not too far away, I think. That's actually very possibly real in five years or something like that.

Lenny Rachitsky (01:14:00):
What I'm imagining, because it's hard to imagine a social network where it's people because usually we want to know who these people are. I don't care random sharing status updates, but I can see a TikTok that is all AI.

Gaurav Misra (01:14:11):
Exactly, exactly.

Lenny Rachitsky (01:14:13):
Wow, just content tuned to your loves and interests.

Gaurav Misra (01:14:17):
Exactly.

Lenny Rachitsky (01:14:17):
And just random videos. Wow.

Gaurav Misra (01:14:21):
Yep. Because do you know, you see a TikTok feed, you don't even know who's real or not today, right? It's not like we-

Lenny Rachitsky (01:14:27):
Right. That's how I would approach it. I would just join TikTok and start uploading videos that are AI generated.

Gaurav Misra (01:14:32):
Exactly.

Lenny Rachitsky (01:14:33):
And then build a whole network of that. Oh my god, the future is wild.

(01:14:37):
Let's go to failure corner. Something that I try to do with this podcast is share moments where things didn't go well. There's all these stories of everything's going great all the time. All this foundries killing it, building a billion-dollar company. Oh, so awesome. But they don't know all the things that go wrong. So let me ask you, is there a story you can share of when things didn't work out? When you failed?

Gaurav Misra (01:14:59):
At the beginning of the company, we actually had a bunch of time where we spent figuring out what we wanted to do, and I think it's an unconventional story almost in a way because we started off the company, the first thing we did was build the Captions app. We launched the app. That was the first thing we did. Took two days to build it. We put it out there and it immediately took off. It was absolutely shocking because I built it on a weekend. We put it out there, I called my co-founder on Monday. I'm like, "It's at the top of the app store. We're getting like 600 videos a day."

Lenny Rachitsky (01:15:31):
Top of the app store, holy shit.

Gaurav Misra (01:15:33):
And we didn't do anything to enable that. It just happened on its own. It was almost anti-climactic in a way because we thought it would be a lot more time spent figuring out the product before that would happen. And so it felt like, "Wait, this can't be it, right? It can't be this fast. How did this happen?" So we got distracted because of that, because we were like, "Oh, okay. Well, maybe ... This is cool. It'll work. That's great, but we got to figure out what the product is."

(01:16:07):
And so we spent at least a year, year and a half thinking about building social networks and all kinds of things when we should have been working on Captions because there was product market fit there. And how we figured that out is Captions was sitting on my personal account, so I wasn't checking that a lot. About a year and a half into the company, as we were working on other projects and stuff, I went back to my personal account, just opened it, and I saw that there was $500,000 in there.

(01:16:38):
I looked at a chart and it was just growing. The revenue was just growing completely on its own. No employees, no releases, no bug fixes, no customer support. There was like 2,000 open support tickets that were unanswered for a year and a half, and great reviews. It's just going completely on its own. And so that was a clear sign to me. It was like, "Oh my God, you should have been working on that. That product works."

(01:17:05):
And so we immediately had a meeting. I mean, it was tough to figure out what the right path was at that point because we'd invested so much time in other things as well, but reset, and we got back on the track with Captions, and literally as soon as we started releasing the first features into it, it blew up. What looked like a vertical line at that time became a horizontal line, and the new vertical line was so vertical that the old vertical line became a horizontal line, essentially. And it's continued since then, which is crazy. So we basically wasted about a year and a half.

Lenny Rachitsky (01:17:42):
I love that new way of thinking about a hockey stick moment where not only is it going vertical, but the rest of the chart is now just flat along the bottom of the axis.

Gaurav Misra (01:17:49):
Exactly. Yeah.

Lenny Rachitsky (01:17:51):
For people that may not know what Captions is, I try to describe it at the beginning and we'll link to it and stuff, but basically, the reason you thought it was nothing is it just adds captions to a video that you record.

Gaurav Misra (01:18:01):
It does.

Lenny Rachitsky (01:18:01):
Added captions.

Gaurav Misra (01:18:02):
Exactly, yep. So I think we wanted ... Our thought was we're going to build a social network, but first we got to build a creation tool for the social network. And we knew that we wanted to use AI to create video, and it seemed obvious that, "Oh, speech to text, a solved problem, we should start with that." So that's why we decided to start with Captions because it was a solved problem at the time. What was funny is that once GPT and stuff started coming out, a lot of the things that were unsolved became solved very quickly. So timing was almost perfect.

Lenny Rachitsky (01:18:37):
And that aligns to something you shared earlier. Just so many of these problems that were not yet solved are now possible, and the companies that are in the right place at the right time benefit greatly who've been just waiting for this part.

(01:18:50):
The other thing that I think is interesting about that story is you try to build a social network. I think it was around high schools and things like that. As we've seen, it's very difficult to build a new social network. So let me just get your sense. Do you think it's possible for somebody to come around and build a new, the next Facebook, the next Snap, the next whatever?

Gaurav Misra (01:19:09):
I think it's definitely possible. I do think ... Let me tell you something crazy, actually. The social network that we had at the time, we actually remove it from the app store, so it's not available anymore. But til today, there are people, there are thousands of people that are using it, posting on it, and all the different things, which actually speaks to the power of the social network in a way. It is hard to create and hard to kill. I mean, I think X is actually a great example of that too. A lot of movement happened there and it continues to work, I guess somehow. So testament to that.

Lenny Rachitsky (01:19:49):
The power of network effects, especially someone once described this so well, they're like Twitter/X. They changed the brand, they changed the team building it. They changed the URL. Like everything changed about it except the network effect of the people in it.

Gaurav Misra (01:20:07):
It's true. It's true.

Lenny Rachitsky (01:20:09):
I just saw a story that they're making billions of dollars. He's actually turned it around. It's actually becoming a really profitable company.

Gaurav Misra (01:20:16):
Wow.

Lenny Rachitsky (01:20:17):
Yeah. It just came out the other day. So Elon did it. Well, with that, we've reached our very exciting lightning round. Are you ready?

Gaurav Misra (01:20:25):
I'm ready. Let's do it.

Lenny Rachitsky (01:20:27):
What are two or three books that you have recommended most to other people?

Gaurav Misra (01:20:32):
I have to say here that I actually don't read books. It's actually something that I decided on purpose where I decided I don't want to build my skill in reading, and I want to build it in listening and watching instead, because I think that's the future.

Lenny Rachitsky (01:20:49):
I love how intentional that is, and I love how it's a really cool way of saying, I don't read books. The future isn't reading, but I love that you have books behind you, so [inaudible 01:20:58].

Gaurav Misra (01:20:58):
I do. Yeah.

Lenny Rachitsky (01:20:59):
[inaudible 01:20:59]

Gaurav Misra (01:21:00):
[inaudible 01:21:00] didn't read, they're back there.

Lenny Rachitsky (01:21:03):
That's funny. Okay, cool. I want to ask more questions, but I'm going to keep going. Lightning around. Speaking of watching and listening, do you have a favorite recent movie or TV show you've really enjoyed?

Gaurav Misra (01:21:12):
I like Silo and Severance. I mean, obviously, I think everyone's watching these. There's a book around Silo too.

Lenny Rachitsky (01:21:18):
I read that. I read all of them. There's three of them.

Gaurav Misra (01:21:20):
There are.

Lenny Rachitsky (01:21:20):
It sucks to watch the show because you know all the tricks that are about to happen, and I'm just like, "Why am I watching this? I know where this will go.

Gaurav Misra (01:21:27):
Yeah. I mean, for what it's worth, it does seem like the show is going on a slightly different path.

Lenny Rachitsky (01:21:31):
It is. That was also what annoyed me. Just like, "What the heck? This is made up. All is made up shit." I don't like that when I watch the show. So two reasons I'm not watching it but [inaudible 01:21:40].

Gaurav Misra (01:21:39):
Don't worry about it. I didn't actually read the book. My wife read the book and then she told me the story.

Lenny Rachitsky (01:21:44):
Okay, okay. I was worried. I was worried. Okay, cool, and Severance. Okay, great. I love Severance.

(01:21:51):
Next question. Do you have a favorite product you've recently discovered that you really like?

Gaurav Misra (01:21:55):
My favorite product, honestly, is Linear. I'm not going to lie, just because it's so well-designed and it's so easy to use. I also like Superhuman. I mean, these are obvious answers, but I do use these things every day and it's hard to create products that you use every day and don't hate. So props for them.

Lenny Rachitsky (01:22:13):
Cool. I haven't announced this on the podcast yet, but this is a good time, whoever's listening right now, is I just launched a bundle where if you become a paid subscriber to my newsletter, you get, listen to this, a year free of Linear and Superhuman and Notion and Granola, which is incredible AI app for note-taking and Perplexity, Perplexity Pro.

Gaurav Misra (01:22:35):
Ooh. Nice.

Lenny Rachitsky (01:22:36):
$2,000 in value for the price of my newsletter, 200 bucks, going to that.

Gaurav Misra (01:22:40):
Damn, that's real value.

Lenny Rachitsky (01:22:43):
It's an unbelievable deal, and it's a no-brainer at this point to buy a subscription, but this isn't an ad for my newsletter. I'll keep going.

(01:22:50):
Next question. Do you have a favorite life motto that you often find yourself coming back to, sharing with friends and family in work or in life?

Gaurav Misra (01:22:57):
I actually learned this because someone else told me that I keep repeating this thing, but I have this framework of how I want to operate at work, basically. Right? I think I love to compete and to win at the end of the day. And I think that to win, you have to be the best. But I also think the easiest way to be the best is to be the first, and that actually is key.

Lenny Rachitsky (01:23:25):
And so is the motto the easiest way? Is that the-

Gaurav Misra (01:23:27):
That's it. The easiest way to be the best is to be first.

Lenny Rachitsky (01:23:31):
Be the first. Interesting. Okay. I have to resist following threads here because I want to make this lightning round.

(01:23:37):
Okay. Final question, just for fun. What's the coolest, most wild AI video you've seen recently? Is there one that comes to mind of like, "Wow, that was something"?

Gaurav Misra (01:23:47):
I mean, honestly, I got to say the OmniHuman stuff was pretty cool.

Lenny Rachitsky (01:23:52):
The ByteDance video that we talked about.

Gaurav Misra (01:23:52):
Yeah, exactly. I mean, the broccoli talking. I don't know if you saw that one. There was a little broccoli delivering a little speech.

Lenny Rachitsky (01:24:01):
Interesting.

Gaurav Misra (01:24:03):
Yeah, it looked like it was animated by an animator.

Lenny Rachitsky (01:24:08):
Just imagine being a kid these days and just seeing stuff like that.

Gaurav Misra (01:24:11):
I think you're probably just used to it, right? You're just like, this is just normal.

Lenny Rachitsky (01:24:13):
Mm-hmm. It's just like we were saying, AGI is just going to come around.

Gaurav Misra (01:24:17):
Exactly.

Lenny Rachitsky (01:24:17):
All right. Cool. What's for dinner? Cool. That's great.

Gaurav Misra (01:24:20):
Yep.

Lenny Rachitsky (01:24:20):
Amazing. Gaurav, this was incredible. It was so insightful on so many levels. Two final questions. Where can folks find you and what you're building if they want to learn more? And then how can listeners be useful to you?

Gaurav Misra (01:24:30):
Awesome. Yeah, I mean, definitely find me on LinkedIn. That's where I live most of the time. My DMs are open, et cetera, et cetera. So feel free to send me a message. And I think what'll be useful, I mean, we're building out our early product and design team, so if AI video is interesting, if consumer apps are interesting, now's the time to join. We're really small, early, we work together across the team, so there's going to be no better time to join, basically.

Lenny Rachitsky (01:25:01):
And you get to ship a marketable feature every week.

Gaurav Misra (01:25:03):
Exactly. I mean, that's the PM's dream. Think about it. Right?

Lenny Rachitsky (01:25:06):
The PM's dream. Yeah, I like that that's a filter. The people that get excited about that, great fit. The people that are stressed out by that, not the place to be.

Gaurav Misra (01:25:15):
Exactly.

Lenny Rachitsky (01:25:17):
So awesome. All right. Gaurav, thank you so much for being here.

Gaurav Misra (01:25:20):
No, thank you. Appreciate it.

Lenny Rachitsky (01:25:22):
Bye everyone.

(01:25:25):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

