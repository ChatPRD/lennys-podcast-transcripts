---
guest: Stewart Butterfield
title: Mental models for building products people love ft. Stewart Butterfield
youtube_url: https://www.youtube.com/watch?v=kLe-zy5r0Mk
video_id: kLe-zy5r0Mk
description: 'Stewart Butterfield is the co-founder of Slack and Flickr, two of the
  most influential products in internet history. After selling Slack to Salesforce
  in one of tech’s biggest acquisitions,...

  '
duration_seconds: 5436.0
duration: '1:30:36'
view_count: 37741
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- metrics
- prioritization
- user research
- iteration
- analytics
- pricing
- revenue
- culture
- leadership
- management
- strategy
- vision
- positioning
---

# Mental models for building products people love ft. Stewart Butterfield

## Transcript

Stewart Butterfield (00:00:00):
This is 2014. That was the year that Slack actually launched. I was interviewed by MIT Technology Review and asked if we were working to improve Slack. I said, "I feel like what we have right now is just a giant piece of shit. It's just terrible and we should be humiliated that we offer this to the public."

(00:00:14):
To me that was like, "You should be embarrassed." If you can't see almost limitless opportunities to improve, then you shouldn't be designing the product.

Lenny Rachitsky (00:00:24):
Slack was famous for being one of the early, consumerized B2B SaaS products.

Stewart Butterfield (00:00:29):
At more than one company all hands, I made everyone in the company repeat this as a chant. In the long run, the measure of our success will be the amount of value that we create for customers, and you can put effort into demonstrating that you have created this value and stuff like that, but there's no substitute for actually having created it.

Lenny Rachitsky (00:00:45):
Something else I heard that you often espouse is friction in a product experience is actually often a good thing?

Stewart Butterfield (00:00:52):
It became an assumption that it should always be trying to remove friction when the challenge is really comprehension. If your software stops me and asks me to make a decision and I don't really understand it, you make me feel stupid. If people could get over the idea of reducing friction as a number of goal or reducing the number of clicks or taps to do something, and instead focus on how can I make this simple? How do I prevent people from having to think in order to use my software?

Lenny Rachitsky (00:01:15):
You started two companies, both famously pivoted. I imagine many people come to you for advice on pivoting.

Stewart Butterfield (00:01:20):
The decision is about have you exhausted the possibilities? Creating the distance so that you can make an intellectual rational decision about it rather than an emotional decision is essential. And the reason I say you have to be coldly rational about it is because it's fucking humiliating.

Lenny Rachitsky (00:01:36):
Today, my guest is Stewart Butterfield, a founder and product legend who rarely does podcasts. Stewart founded Flickr and then Slack, which he sold to Salesforce in one of the biggest acquisitions in tech history at the time. There is so much product and leadership wisdom locked away in his head. I feel like our conversation just scratched the surface. We chat about utility curves, something he calls the owner's delusion, a hilarious pattern he sees at companies he calls hyperrealistic work-like activities, what he's learned about product and craft and taste and Parkinson's law, why you need to obsess with not making your users think, the backstory on his legendary we don't sell saddles here memo, and so much more. A huge thank you to Noah Weiss, Chris Cordell, Ali Rael, and Johnny Rogers for suggesting topics and questions for this conversation. This is a really special one and I really hope to have Stewart back to delve even deeper.

(00:02:27):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. And if you become an annual subscriber of my newsletter, you get 17 incredible products for free for an entire year, including Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Head on over to lennysnewsletter.com and click Product Pass. With that, I bring you Stewart Butterfield after a short word from our sponsors.

(00:02:57):
Here's a puzzle for you. What do OpenAI, Cursor, Perplexity, Vercel, Plaid and hundreds of other winning companies have in common? The answer is they're all powered by today's sponsor, WorkOS. If you're building software for enterprises, you've probably felt the pain of integrating single sign-on, SCIM, RBAC, audit logs, and other features required by big customers. WorkOS turns those deal blockers into drop-in APIs with a modern developer platform built specifically for B2B SaaS.

(00:03:26):
Whether you're a seed-stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise-ready and unlocking growth. They're essentially Stripe for enterprise features. Visit WorkOS.com to get started or just hit up their Slack support where they have real engineers in there who answer your questions superfast. WorkOS allows you to build like the best with delightful APIs, comprehensive docs, and a smooth developer experience. Go to workos.com to make your app enterprise-ready today.

(00:03:58):
This episode is brought to you by Metronome. You just launched your new shiny AI product. The new pricing page looks awesome, but behind it, last-minute glue code, messy spreadsheets, and running ad hoc queries to figure out what to bill. Customers get invoices they can't understand. Engineers are chasing billing bugs. Finance can't close the books. With Metronome, you hand it all off to the real-time billing infrastructure that just works. Reliable, flexible, and built to grow with you. Metronome turns raw usage events into accurate invoices, gives customers bills they actually understand and keeps every team in sync in real-time. Whether you're launching usage-based pricing, managing enterprise contracts, or rolling out new AI services, Metronome does the heavy lifting so that you can focus on your product, not your billing. That's why some of the fastest growing companies in the world like OpenAI and Anthropic run their billing on Metronome. Visit metronome.com to learn more. That's metronome.com.

(00:04:59):
Stewart, thank you so much for being here and welcome to the podcast.

Stewart Butterfield (00:05:02):
Thank you for having me. I'm excited.

Lenny Rachitsky (00:05:05):
I'm even more excited. I'm so honored to have you here. I never told you this, but you've been towards the very top of my wish list of guests I have on this podcast ever since I started this podcast a few years ago, so I'm very excited that we're finally making this happen. I have so many questions for you. My first question is just what the heck are you up to these days? I feel like ever since you left Slack, we haven't heard much from Stewart. I'm curious what you're up to you hopefully or just chilling.

Stewart Butterfield (00:05:28):
I'm mostly just chilling. I left Salesforce two and a half years ago and I have a two and a half year old, so she was actually born three days after my last day, so a lot of time with family and it's an enormous privilege to be able to spend time with young kids while they're young. No new company to announce or anything like that. I do get a lot of emails and texts. Basically every three to six weeks there's this cycle because Cal Henderson who's the CTO of Slack and who also, we worked together on Flickr, so have worked together now for 23 years, have been talking about what we want to do next if there is something.

(00:06:10):
But honestly, the big challenge has been I think these things are destroying the world and what we're good at is making software. So you find some way to make software that helped people use their phones less often, then that would be a big winner, but haven't come up with anything good. A lot of philanthropic work, nothing to announce there yet, but there's some cool projects that I'm working on, and a lot of just personal creative art projects and supporting other artists and stuff like that.

Lenny Rachitsky (00:06:45):
To prep for this chat, I talked to so many people that have worked with you over the years to try to figure out what you taught them about building product, building teams, building companies that most stuck with them, that most helped them build amazing products. The first is a concept called utility curves. This came up a bunch across so many people that have worked with you. Talk about what is a utility curve, how you use that to build better products.

Stewart Butterfield (00:07:08):
This is pretty easy because it's a very familiar S-curve where you have, it's flat and it starts arcing up and then there's a really steep part and then it levels off again. And on the horizontal axis, you can think of cost or effort and on the vertical axis, it's value or convenience. It depends exactly what you're talking about, but the idea is the first bit of effort you put into something doesn't result in a huge amount of value. And then there's some magic threshold where it produces an enormous amount of value and then continued investment doesn't really pay off. The most basic example I can think of is let's say you're making a hammer, and on that bottom axis, it's now quality, and if the hammer has a handle that breaks with any impact, then is totally useless. And if you make it a little bit stronger, it's still pretty useless and it's like junk, junk, junk, junk, junk. Okay, good, great. Then it doesn't matter anymore.

(00:08:06):
If you're making an app, okay, this app's going to have users and so let's make a user's table and a database, and so far you have generated no value. The reason I felt like this was so important is because we would talk about a feature, and usually features are thought of as a binary. You either have this feature or you don't. The argument I guess was have we just not invested enough in this or have we got all the value or convenience or quality or whatever that we could get out of this? And we had pointed diminishing returns and it just doesn't matter.

(00:08:46):
I think in many cases, people will add a feature, it's not good enough and so people don't use it or appreciate it, but now you've added some complexity to the app and then people give up or take it back or they try something in testing and they don't get the results they want, and so they decide that this a thing is worth doing. We would try to really investigate and decide whether we were on the first shallow part of the curve, the second shallow part of the curve, or we're just coming up to it. So I think it's a lot easier to understand the value of this when you're talking about a specific app and a specific feature, but I think it was ultimately helpful in getting people to understand whether something was worth it or not.

Lenny Rachitsky (00:09:31):
So just to mirror back what I'm hearing, there's this, if you visualize this curve at the bottom, it's like I don't even know what this is. And then up the curve is like, okay, I sort of get it. And then at the top is, okay, I can't live without this now that I understand what this is for, it feels like it's a really a different way of thinking about getting to the aha moment for someone where they see, okay, saved items, I get it, I need to use this constantly. It feels like this works both for a specific feature and also just for Slack, getting people to even understand here's what Slack can do for you. And then now I can't live without Slack. And essentially this is a lens you use to figure out where to spend product resources because if you don't get up that curve to I get it and I can't live without it, nothing else matters. Is that the framework?

Stewart Butterfield (00:10:13):
Yeah, and I think then you layer on another concept like the, Bezos used the term divine discontent. The line actually moves because once people are familiar with a piece of software or the way a feature is implemented or something like that, their standards go up, and so there's this competition. And again, this axis can be, utility is the best general term for it, but it could be quality, convenience, speed, it could be any number of things, but as you improve your search capability or as you improve your login experience or your forget password experience or your checkout experience or whatever everyone else is as well. And so there's this continued investment and when forget about thinking about a new feature, you're looking at how the product works overall and usually things get implemented once, and then if they're lucky, they get improved upon periodically. Most things get improved upon very infrequently and some things get improved upon never.

(00:11:22):
I want to give an example at the absolute extreme because I actually don't know how long this has been, but I try not to criticize other people's software so much because I'm very familiar with the trade-offs and prioritization and how hard it can be and blah, blah, blah, blah. But okay, so most people have the Gmail Calendar app on their phone. I travel a fair bit. I'm mostly in the Eastern Time Zone, sometimes in Mountain Time, sometimes in Pacific, sometimes in English time, and sometimes in Japan, Central Europe. There's maybe 10 time zones, 12 time zones that I would ever choose. When you hit the option to set the time zone on an event in Google Calendar, on the iOS app, it presents all the time zones in the world in alphabetical order. And I mean, there's probably worse orderings, but there's no value in that.

(00:12:24):
And even when you start searching, it still presents them in alphabetical order by country with that turn. So if I'm in California and I'm trying to set the appointment for next week when I'm back in New York and I type in E-A-S-T and I get a bunch of garbage, okay, Eastern, and then the first one is Eastern Australia, New South Wales, and then Eastern Australia, Queensland, and then Eastern Australia, Daylight Savings and Eastern Australia standard time. And then you're like, "Well, fuck, I can't remember which one is Daylight Savings and which one is standard time?" I could keep going like this for a while. This is an app that's used by at least hundreds of millions of people, presumably every single Google employee. It's bananas how bad it is. There's so many, there's all these clever things you could do. Like you know me, I'm on the West Coast, first option should be the East Coast and vice versa. But it definitely shouldn't be that every time zone is presented with equal value. I don't a couple hundred time zones. I grew up in Canada. Newfoundland has its own time zone, which is offset by half an hour. The population of Newfoundland has about half a million people. Not that many people go to visit Newfoundland, maybe a million people in all of history so like a million and a half out of 8 billion people. And there's Newfoundland, the same with China time, which is like 25% of the world's population in this.

(00:13:51):
Anyway, that was a little bit longer than I intended to go on this example, but it's crazy because no one's going to switch to Gmail or to G Suite, Google Calendar from Outlook Exchange because the time zone picker is good, so maybe in some sense it doesn't matter, but at the same time there's a real value in delighting customers and there's an emotional connection that they form or don't form. And in some cases that could be really positive like they would recommend it. And when they switch companies or decide to start their own company, they're going to choose to use this product or advocate for it because of that emotional connection and vice versa.

(00:14:34):
They'll also be like, "I hate this thing that drives me bananas. I really think we should stop using it," or advocate for the alternative. And I think people just don't appreciate or come back to those things often enough. And then there's this category of really essential parts of the app again like account creation, sign up, forgot password, things like that, that for most organizations very infrequently get a lot of love and iteration and improvement despite the fact that the quality bar has gone up across the board and continually goes up.

Lenny Rachitsky (00:15:11):
Let's go down that rabbit hole a little bit more around delight and craft. Slack was famous for being one of the early, let's say consumerized B2B SaaS products. Slack leaned into delight and experience and craft and a great experience. And you just as a product leader, I'd say are known as very taste forward, very craft oriented leader, which is pretty rare and I think continues to be rare. So there's a few things I want to talk about here. One is taste. I heard at a talk, you gave a talk on taste and you have a really unique perspective on just what taste is, what product taste looks like. Can you share that?

Stewart Butterfield (00:15:49):
There is a lot of you going back to the utility curves again, people who are obsessed with this one little thing and keep on adding more and more detailed improvements beyond the point where it makes much of a difference. But I guess a couple of things about taste. So one is can you learn to develop it? I think so because the word literally comes from experiencing food and putting stuff in your mouth. And can people become better chefs with training? Yes, absolutely. Undoubtedly, some people have a natural advantage and are born with this ability to make discernments that are difficult for other people to make and stuff like that. But you can definitely practice and you can definitely get better. The second thing I'd say is you can create a real advantage for yourself, for your product, for your company by leaning into it because most people don't have good taste and don't invest. You're probably familiar with, again, Jeff Bezos line, your margin is my opportunity and pretty obvious what he meant by that.

(00:16:54):
I would tell the story at Slack over and over again. It actually made it part of the new hire welcome. I'm in Vancouver at our Vancouver office and I'm going for a walk with Brandon Velestuk who's our, at the time creative director for product development, I think that was his title. And we're in the Yaletown neighborhood in Vancouver so there's really narrow sidewalks because it used to be a warehouse district and now it's fancy restaurants and nail salons and boutiques and stuff. And as it does in Vancouver, it starts to rain. We don't have umbrellas. We're walking back to the office and most people have umbrellas and we're on these narrow sidewalks with people coming towards us with umbrellas. We noticed how few people would move their umbrella out of the way. And of course, the other person, their umbrella, the pokey bits are exactly at eye level for people walking towards them. We would get forced off the sidewalk or having to duck down or whatever.

(00:17:54):
It became a game like we were guessing is this person going to tilt their umbrella out of the way so we can pass or not? And something like one-third of the people would do it. And we had this conversation about it where it's like, okay, I can think of three reasons why people wouldn't do it. One is they have very few avenues in their life to exercise power and this is one of them. And they're just, want to get out there and dominate people and cause suffering. Shouldn't ascribe to malice that which can be ascribed to ignorance so that probably is the explanation for a tiny, tiny, tiny percentage of people.

(00:18:34):
But the other two explanations aren't that great either. One is that they see it's happening, they see they're pushing other people off the sidewalk or poking them in the eye or whatever, and they're just like, "Fuck, that's too bad. I wish there was something I could do about that, but I can't think of anything." And the last reason is they just don't notice it all. They're just oblivious to their impact on other people. And they're so in their head, and I can't really think of any other explanations for it besides that.

(00:19:03):
And so we would say it's not like tilting your umbrella is our opportunity. That's not a great rephrase of your margin is my opportunity, but your failure to really be consider it exercise this courtesy and really be empathic about other people's experience is an advantage that you can create a critical advantage. I think that there's many reasons why Slack was successful at the moment. It was successful and we think we had a bunch of really wonderful tailwinds and all of that stuff, but it wouldn't have grown the way it did without those little conveniences which caused people to form an emotional connection because a lot of our growth came from startup A uses Slack, and then someone leaves startup A for startup B, and startup B doesn't use Slack yet. And they would be like, "Oh my God, you guys, you really, this is so good. We got to try it." And the spread was driven by that and people really genuinely advocating for it.

Lenny Rachitsky (00:20:07):
That is an amazing metaphor. I love that one moment became a value of product craftsmanship at Slack.

Stewart Butterfield (00:20:14):
Tilt your umbrella was a very common saying on company swag and stuff like that.

Lenny Rachitsky (00:20:20):
Is there an example, I imagine there are many, but from the time of building Slack, especially in the early days where you chose to go big on craftsmanship and experience and delight versus speed where you thought looking back that was a really great idea and worth really core just to success.

Stewart Butterfield (00:20:37):
Here's a bunch of little examples. Someone else came up with this idea, and I'm trying to remember who it was, but let's see, maybe Andrea Torres, maybe Ben Brown, something like that who was like, "Why did we ask people for email address and password if their ownership of the email address was the thing that allowed them to create the account in the first place? Why don't we just ask them for their email address and then send them a link?"

(00:21:07):
And so when Slack's first version of the mobile app came out, we're like, "Typing your password on your phone if you have any minimal threshold of password hygiene is a terrible experience." Capital H, lowercase Q, six, caret, period. So let's just have them enter the email address. We'll send them a link. The link will automatically open the app and authenticate them. And so there's one, a little example.

Lenny Rachitsky (00:21:33):
Wow. So you guys invented the magic link experience.

Stewart Butterfield (00:21:36):
Someone else invented. I want to be clear that I had seen that idea somewhere else, someone else, a blog post about it or something like that. But we were the first ones, to my knowledge, that really scaled that and made it a standard. There is another one which we really puzzled about in the very early days where people have a long history of using messaging apps from AOL Instant Messenger to SMS to WhatsApp, where their expectation is they get a notification for every message that's received. And in the case of Slack, that doesn't make as much sense because you're a member of many channels and the messages may not be for you, and so that's why we have the @ tagging people. And we certainly didn't invent that, that was Twitter.

(00:22:23):
But what we realized was people were signing up for Slack, and it's one engineer on this team inside of this larger organization, inside this larger company, and they would pull in the person next to them and they would say, "Let's try it out."

(00:22:35):
And then they would send a message and then one person would be like, "I didn't get a notification. This is bullshit."

(00:22:43):
We reluctantly decided that we had to send notifications for every single message as the default for new accounts. But once you had, I don't remember what the threshold would happen, I think it's once you had received 10 messages, we would pop up this little thing that says, "Hey, you have our default settings for notifications. We don't want Slack to be noisy for you. Would you like to switch to our-"

Stewart Butterfield (00:23:00):
... For notifications. We don't want Slack to be noisy for you. Would you like to switch to our recommended settings? And then they would just click a link and it would have what should be the default, which is, you only get a notification if it's a DM or someone tags you. But we realized it was worth that investment to get people over the hump. I'll give one more simple one and then one kind of more complex. One, people would just like the, I can't remember if it's called urgent or important, but the flag in Outlook, set the priority of a message for the recipients always got abused inside of every company. As soon as someone does it, everyone's like, "Okay, I'm going to do that too for my message."

(00:23:41):
And so all of your messages have the little flag and it becomes useless. We have @everyone, which causes a notification to be sent to every member of the channel when the message is sent and people would start, someone would find this feature inside of a organization. They would @everyone, everyone would get a notification and then the next person to send a message who was like, " Well, my thing's more important than Bob's thing. I'm going to also @everyone." And it became really obnoxious and people would complain about it, but it was, I don't know, I guess tragedy of the commons. It's not quite exactly the same thing, but it was this real dynamic that happened over and over again.

(00:24:16):
So we came up with what was called the shouty rooster, and internally we said, "Don't be a cock." But we didn't obviously say that publicly when you @everyone, a little rooster would pop up and it would have you sound waves coming out of its mouth and being really obnoxious and say, "Hey, this is going to cause a notification for 147 people in eight different time zones. Are you sure you want to send this message with the @everyone?" And of course, that worked amazingly and it dropped off. And again, it was really trying to shape people's behavior so that they used, one is not to be very flexible, but we knew that there was ways to use it that would be annoying and difficult for everyone. And so try to shape the communication culture inside the organization to take best advantage on it.

Lenny Rachitsky (00:25:02):
That feature still exists. I see that rooster all the, no, I don't see it all, well, actually I do @channel, because I run a big Slack, so I see that rooster, that survived.

Stewart Butterfield (00:25:11):
Yeah. Yeah, that survived and good because it was a trivially easy thing to implement and made a really big difference. But it also taught people how the product worked, because people probably didn't know that @everyone or @channel... Didn't think about the cost, at least.

Lenny Rachitsky (00:25:31):
Genius.

Stewart Butterfield (00:25:32):
Yeah. Here's one more. So we decided we were going to Do Not Disturb as a feature. And we had this, not conundrum, but you're trying to take into account all the different uses of Slack because by the time we implemented this, 2017, there was tens of thousands of paying customers, the organizations, hundreds of probably millions of users, maybe hundreds of thousands of organizations. I don't remember how many. And everyone had set up stuff the way that they liked it, including things like ops alerts going into channels for on-call engineers for some of the biggest systems and apps in the world. And so we couldn't just deploy it right away. We realized that some of the decision-makers, the owners of the organizations were going to have really strong opinions about this. We also realized that some of the end users are going to have strong opinions, and we wanted to figure out a way to balance the concerns and give people appropriate means of control.

(00:26:37):
So we came up with this really elaborate system for the rollout, which was, we told everyone, I'm sorry, every Slack administrator that this was coming weeks before it came. And we told them that we were going to set a default for their organization, which I believe was either 7:00 P.M. to 7:00 A.M. in their local time zone, or 8: 00 A.M. to 8:00 P.M., I can't remember which it was, but also that they could override that default, and also that the individual end users could override that system owner default. And finally, that the system owner could, if they changed the default again, would override all of the end user's preferences and then the end users could override them again. And it wasn't to create this dynamic where people were at war, but so that you could change a policy and then people could still customize and stuff like that.

(00:27:32):
But this was a much longer and more convoluted process, but it allowed the millions of people who were using Slack to get the feature without creating a bunch of conflict and without people turning it off automatically. And I think critically, with setting a bunch of defaults, because if we didn't set the default, most people wouldn't turn it on at all. If we didn't default you to Do Not Disturb from 8:00 P.M. to 8:00 A.M. you probably, if you're the average person, wouldn't ever do it yourself. So that's another elaborate example where I think that investment made sense because it was a critical feature for a lot of people. And if we hadn't done it that way, I think it would've caused a lot of complaints and conflict and stuff like that.

Lenny Rachitsky (00:28:22):
Those are amazing examples. I very much appreciate that Do Not Disturb feature when you guys launched that. I still remember that coming out. I'm sure a lot of people are very thankful for that.

Stewart Butterfield (00:28:30):
Yeah.

Lenny Rachitsky (00:28:31):
Something else I heard that you often espouse, which is counterintuitive to a lot of people is about friction, friction in the product experience. That friction is actually often a good thing. It's a feature, not a bug a lot of times if you use it well. Talk about your experience there.

Stewart Butterfield (00:28:46):
Yeah. So yes, and there's also another issue around friction, which is it became like a mantra or just kind of an assumption that you should always be trying to remove friction. And in some cases that's true. We would talk about it in Slack. It was hard to market. It was hard to explain what it was if you had never used it before. You could say a messaging app for businesses or whatever, but a critical disadvantage to Slack doing out-of-home advertising, putting up a billboard versus beer or cars is, no one needs to be explained why they would want a car or beer, but everyone will have to explain one day why they want Slack. And so the problem there is comprehension, and this will come up an enormous amount. So now imagine you want to get tickets to the Taylor Swift concert in San Francisco and you go to the Ticketmaster website.

(00:29:43):
If you think about both your comprehension, it's perfect to this case. And that translates into the specificity of your intent and the degree of your intent is also kind of maxed out. So look, I really want to get these tickets. I know exactly what they are. They're Taylor Swift tickets for this date at this venue. And so in that scenario, it doesn't really matter if Ticketmaster's website is slow, it doesn't really matter if the payments page errors out, you're going to persist and get through it. So obviously they're better to reduce friction, but in some sense there's not a huge amount of value in doing that. For most creators of products, there are a handful of cases where that really is true for you as well. And they include things like user registration, authentication, checkout flows for e-commerce. I am significantly more likely to buy something if there's Apple Pay or Shop Pay or something like that.

(00:30:44):
I'm significantly less likely to carry through the purchase of something if I have to manually enter all of the fields of my address one at a time rather than having one of those address pickers. It's crazy, but the issue is my intent isn't always 100%, and the specificity of my intent isn't always 100%. So if your thing is direct to consumer T-shirts and you acquire customers through Instagram ads, all of them know what T-shirts are. It's like, "This looks like a good T-shirt to me." But I'm rarely 100% intent. I might have a very specific intent, but my intent's like 70%. So if you're, the amount of friction is above that, I'm not going to do it. But now, okay, people coming to Slack.com, some friend had mentioned Slack and talked their ear off at some point months ago, and then they saw a news article and then they saw someone's tweet and then they saw an ad on about the website they were visiting and they finally said, "Okay, I'm going to go to this website."

(00:31:46):
So their intent is at the absolute minimum threshold, it was before that last event happened, they were below and now they're above, but they're just above. The specificity of their intent like, "I need to get Taylor Swift concerts for this date at this venue." Is also very low, because they're like, "It's a work thing. I'm not sure it's a spreadsheet or a calendar or exactly what it is." So they were coming in at 0.1% over these critical thresholds. What was the challenge? It wasn't friction, because it's not like they were aiming for something and they knew what they were aiming for and they were just trying to get themselves to that point.

(00:32:34):
What we had to worry about was creating comprehension and in two senses, what is this thing? And what am I supposed to do next? And that creation of comprehension in the sense of explaining stuff, that creation of comprehension in the sense of the design of the UI, of the screen, of the page or whatever, and the visual hierarchy and the affordances that are there and the indication of things to interact with and which thing should be the next thing to do and all that stuff, that becomes really critical.

(00:33:09):
And I think very, very few people recognize that. They're like, "I want to get people who come to my webpage to the sign up form as quickly as possible." But if they don't know what they're signing up for and they don't know what it's going to do after, is it going to spam them? They don't know, "Am I going to have to pay on the next step or what?" Then they're just going to back out. And this was a lifelong battle because the remove friction orientation is so deep in people. Again, it really makes a difference in those cases where people do have an intent and they do know what they're trying to do is a poor approach when the challenge is really comprehension, and I think the secret is most, 70%, 80% or whatever of a product design is in that comprehension step because people, if they do ever open the preferences tab and look at all the options, rarely have an idea.

(00:34:09):
And if you can't teach them or make it possible for them to discover what the capabilities are, then they're not going to take advantage of them and they're not going to get as much out of it. And I think that the trick is for most of the unique parts of any application, most of the specific things that your app, your product, your software does are areas where the challenge is going to be comprehension inside of friction. It really could be anything Shopify, the purpose of the service for its end users is generally going to be kind to clear. But most people, most first-time store openers don't know that they can get reports or if they know that they can get reports, they don't know what kinds of reports. And if they know what kinds of reports they can get, they don't know how they can tweak them and what the timing should be and which things that are more important to display.

(00:35:03):
And I could go on and on and on and on, and people just don't recognize that. So I want to see if this is still true. I'm just going to open my phone and clock app. And they had the craziest description for alarms. It's a little bit different, but people can look at their own phone. So I have, it says alarms and it says sleep and a vertical bar, wake up and says, no alarm, and a button that says change. And then if you hit it, it says sleep is off. In order to automatically turn on sleep features and edit your schedule, you need to turn sleep on. So obviously sleep was a good name for this thing if you already had a way of getting people to understand it. If you don't, it's ungrammatical and incomprehensible and why would you ever do it? And I got to guess, it's been like this for years, 90 plus percent and maybe 98% of people just do what I do, which is that you just create, "I want the alarm on and I'm going to set the time for it."

(00:36:11):
And I don't know what turning sleep on does, but it's just the lack of comprehension prevents people from getting the value. And I'm sure that there's a bunch of value behind turning sleep on, whatever that means and people spend a lot of time on those features and it integrates with biometrics and your watch or who knows. Again, I still don't know because turning sleep on is like, what does that do? And what is it going to cost me? And what impact it's going to have? Those examples are just to me all over the place. And the reason I don't use most software where there was an actual choice point or the reason I don't use most features where there was a choice point for me is because I didn't understand what they were going to do and I don't give a shit. And if there is one mantra that I would use to replace that it's, Don't Make Me Think, I don't know if you remember that book.

Lenny Rachitsky (00:37:02):
Absolutely.

Stewart Butterfield (00:37:04):
Yeah. And honestly, it's been many more than 10 years since I read it, so I don't even remember all of the examples in the book, but as a mantra that was up there with utility curves because for two reasons. One is it's just like it's expensive to make a decision. You literally burn glucose. There's a metabolic action. There's ATP created in the mitochondria and your neurons and a bunch of stuff is happening and people do get decision fatigue and there is cognitive cost of all these things. But also there's an emotional aspect, which is, if your software stops me a second and asks me to make a decision and I don't really understand it, you make me feel stupid. I'm like, "I don't understand this."

(00:37:50):
Some people, maybe their orientation is, "Okay, the software is stupid." But I think most people are like, "Oh, I'm dumb." And if you ever talk to people who aren't especially technologically savvy, the canonical example is people who are under 50 talking to their parents about using some piece of software and what they're supposed to do, the parents always feel stupid like they're the ones that are wrong. And so if you're causing people to think, in the best case, it's unnecessary use of their biological resources, and in the worst case you've now made them feel bad, emotionally bad, and they're going to associate that with the product forever. And these are things that are just kind of rolling one into the other.

(00:38:35):
So I'm going to keep going with one last thing, because they just kind of come together, which is along with reduced friction, it's like reduce the number of clicks or taps it takes for someone to accomplish something which is almost always exactly the wrong thing. It's the easiest way you could make any action in your app, a single click or tap by just exposing every single possibility on one screen that scrolls for thousands and thousands and thousands and thousands of pages. And obviously that's terrible. So why do people think that a little bit of that is good? And here's an example. You open a menu, there's 14 things that people might want to do.

(00:39:22):
Level one is group them into like items and put a vertical, sorry, horizontal divider between them so at least people can kind of chunk and see what there is. Step two is present the two or three most common things or the five most common things, whatever and then have some form of other and then you go to a sub menu that has more items and the decision of how to tune that becomes incredibly important. I'm going to pick on Google again just because it is, I feel like I'm Donald Trump here, but I'm going to interrupt myself again with a story. It's-

Lenny Rachitsky (00:39:57):
Yeah, let's do it.

Stewart Butterfield (00:39:58):
At some conference or event, I don't remember what it was, and this is probably eight years ago and we're in the bar after the sessions ended at this thing. John Collison from Stripe is there and Sundar, CEO of Google is there. And John, sorry, Patrick goes up to Sundar and they can talk about anything. Stripe wasn't the behemoth, it was now at that point, but it was still a significant company, was up and coming. And what does Patrick want to talk to the Sundar about? It's in the Gmail app, the dragging of people. When you reply all to a message, you often want to change the two recipient to CC and move someone from CC to two or something like that. And just how physically the degree of dexterity that's required to do that inside of the Gmail app is very high.

(00:40:56):
It still hasn't been fixed, but it really struck me that Patrick could have asked for anything. It could have been any talk, it could have been a partnership. It was so irritating to him that it worked like this, he couldn't quite get over it. So anyway, back to bashing on Google, who in many respects do an incredible job and there's all kinds of amazing stuff they do on blah, blah, blah, but the Gmail actions on an individual email are broken into two very long menu items that are different. And one of them doesn't exist on either menu. There is an unlabeled icon is the only way to do it, and that's to mark something as unread once it's read. I have no idea why some of the actions are in one menu and some of the actions are in another menu. I think it's because some of them have to do with an individual email and some of them have to do with the whole thread, but it doesn't seem very consistent.

(00:41:55):
Every possible thing is listed there in one place. And so it becomes incredibly difficult to use because sometimes you have to tap in both menus, read all of the options, and say, "Okay, I've used the process of elimination and it's not here, so it must be there." Uber doesn't work like this anymore, but when I first brought this up to people inside of Slack, there was a moment when the Uber app, when you opened it was just, "Where would you like to go?" And other. And other was everything like change your payment method, set your location, anything you could do in Uber. And that was perfect because almost all the time people just wanted to choose where they wanted to go. Sometimes you wanted to change where your pickup was because you weren't there yet or whatever. And that was just like, what could be simpler than, "I'm going to tell you where I want to go or I'm going to achieve something else."?

(00:42:47):
I really tried to push people to what is the thing that people, or what is the two things or what is maybe three things that people could want to do here and then put everything behind other. And then if it takes them eight clicks or taps to do something, but every single one is trivially easy, that's great. If you reduce that to two clicks or taps, but every part of it is this fraught decision where I'm opening all of the menus and trying to figure out which thing is the right thing, and the more, comparing three things to each other is this difficult four things, it's kind of geometrically more expensive to compare 15 different options all to the other to see if this is the one that you might want. That just becomes impossibly expensive. So to me, those are all really connected. And if people could get over the idea of reducing friction as the [inaudible 00:43:42] or reducing the number of clicks or taps to do something and instead focus on how can I make this simple? How do I prevent people from having to think in order to use my software? How can I make this trivially easy? One last example, because this was really influential for me. So I was going back and forth in Vancouver in San Francisco at the time when we were talking about all this inside of Slack, and I was behind a teenager in line aboard the plane and it was like, we're on the jet way. It took a long time. And I was watching her use Snapchat and it was insane.

(00:44:11):
She was tapping at least four times a second, sometimes six or seven times a second. It was like dismissing stories and doing stuff. But there was a fluidity to it because everything was like, do I want to see this again? Do I want to see the next story from this person? Do I want to switch to a different person? Instead, a notification came up, she answered someone's thing, she took a selfie of herself and everything was just like... So she was tapping four times a second for six minutes. I mean, probably there was some breaks in there. And that was the highest and best use of Snapchat for a 15 year old girl in 2016 or whenever that was. And imagine if the goal was to try to make her tap less, how much of an impediment it would've been to the experience that both her and Snapchat wanted to create?

Lenny Rachitsky (00:45:06):
It's so fun to listen to this and the examples you gave of, it gives us a lot of insight into the way your mind works of just constantly unsatisfied with the way other products work with your product. And I think that's core. Patrick is a good example of Stripe. I feel like that's a recurring theme with very successful product leaders is just constantly unsatisfied and unhappy with how things work.

Stewart Butterfield (00:45:27):
Yeah.

Lenny Rachitsky (00:45:28):
I love just even the way you summarize this, just a really good reframing of, instead of obsessing with reducing friction and reducing steps, instead think, how do I reduce the amount of thinking the user has to do? I've never heard of it described as, you have to think about the ATP and glucose being used to actually think, and your goal is to reduce that versus let's just reduce friction, reduce clicks.

Stewart Butterfield (00:45:52):
Yeah. I think in my more cynical examples, I would say to people, " Stop what you're doing for a second, close-"

Stewart Butterfield (00:46:01):
Stop what you're doing for a second. Close your eyes, take a couple of deep breaths, and then pretend that you're an actual human being. And open their eyes again, and then look at this thing and see, can you figure out what it's supposed to do or say. Or what action you're supposed to take or what the impact will be if you take that action. There's a whole nother related cycle. But before I get into it, I know that I am verbose. I want to wrap up your last example of people being unsatisfied.

(00:46:31):
So here's the quote that I was trying to find. This is 2014, so like that was the year that Slack actually launched officially in February. And this is now near the end of the year. I was interviewed by MIT Technology Review and asked if we were working to improve Slack. I said, "Oh God, yeah. I try to instill this into the rest of the team, but certainly I feel like what we have right now is just a giant piece of shit. It's just terrible and we should be humiliated that we offer this to the public. Not everyone finds that motivational though."

(00:47:06):
So I came into the office the next day and people had printed out on like 40 pieces of 8.5 by 11 paper that quote, and pasted it up on the wall. But to me that was like, you should be embarrassed by it. It should be a perpetual desire to improve. You should probably be like, "Oh, this is great," and you could be proud of individual pieces of work. But in the aggregate, if you can't see almost limitless opportunities to improve, then you shouldn't be designing the product, or you shouldn't be in charge of the company, or you shouldn't almost nothing.

(00:47:45):
Again, you could reduce it down to a tiny feature is anywhere close to perfect. And if A, that's acknowledged freely inside the organization. And B, people think about continually improving as the goal. And that could be like Six Sigma Toyota, Kaizen, that kind of side of thing. Or it could be that story that... I can't remember his name right now. The guy who started Bridgewater tells about Michael Jordan-

Lenny Rachitsky (00:48:11):
Ray Dalio.

Stewart Butterfield (00:48:12):
Yeah, Ray Dalio in his book talks about Michael Jordan learning to ski. Every time he messed up, he wanted the ski instructor to tell him exactly what he was doing wrong. Because to him, every one of those was a gem that he could collect, and he could actually become a good skier. And what he wanted to do was become a good skier. That requires a lot of trust inside the organization.

(00:48:36):
But if you can get to the point where like, "Hey, we are trying to find improvements. We're trying to be critical because you're trying to make this as great as it can possibly be." And not always, not with every person, but most of the time with most people, you can get them to the point where that really direct criticism is actually motivational. It is like people are grateful to have the feedback, whether that's coming from their peers inside the company or from end users of the product. Because you realize, oh yeah, that is bad and we should fix it.

Lenny Rachitsky (00:49:10):
This episode is brought to you by Lovable. Not only are they the fastest growing company in history, I use it regularly and I could not recommend it more highly. If you've ever had an idea for an app but didn't know where to start, Lovable is for you. Lovable lets you build working apps and websites by simply chatting with AI. Then you can customize it at automations and deploy it to live domain. It's perfect for marketers, spinning up tools, product managers prototyping new ideas, and founders launching their next business.

(00:49:39):
Unlike NoCo Tools, Lovable isn't about static pages. It builds full apps with real functionality, and it's fast. What used to take weeks, months, or years, you can now do over a weekend. So if you've been sitting on an idea, now is the time to bring it to life. Get started for free at Lovable.dev. That's lovable.dev. This makes me think about, let's call it a rant that you have about how it takes a lot of work to make anything work at all. That just the default state is not working. Can you just share what you share there.

Stewart Butterfield (00:50:13):
Yeah. I mean, so this is a lot to do with, and maybe this is more recently, it shows up in politics a lot for me. But by the way, if anyone listening to this can help me find this tweet store from somewhere between 2016 and 2020, I don't have a precise idea. And it was this guy's thread about how hard it was to get a stop sign set up. And I believe it was in response to someone claiming that Bitcoin is going to replace US dollars, something about crypto. And his point was like, here's what happened when we tried to get a stop sign put up on a residential street in my neighborhood. And the literal years it took, and the number of agencies that were involved.

(00:50:58):
Like the engineering department, traffic planners, the HOA, and... I don't remember all of the organizations because, and I did that I could search better and find this again. Because it was truly a masterpiece of how difficult it is to get a stop sign put up in most places. The message that I hear from most politicians, and unfortunately this works really well, is things should be good. But they're not because someone is doing something bad, which is preventing the goodness.

(00:51:29):
So billionaires are making things unaffordable. Or immigrants are taking your jobs. Or lazy freeloaders are sucking off a government tea, and causing us all have to pay more taxes, or something like that. The reality is almost nothing works. It's actually another call. I said in this case, John has a great encapsulation of this and I'm sure you're familiar with it, like that. It ends with the world as a museum of passion projects. Because for anything to get done at all requires not just the resources and effort required to instantiate that thing in the real world, but all of the politicking and the sociology and the convincing.

(00:52:15):
And there's a book called Why Nothing Works Recently, which is like, it's not an... I'm sorry to the author, if they... I doubt they're listening, but just it's not like an amazingly written book. I found it a little bit repetitive, but the content was really incredible, just explaining why it's so hard. And how there's this progressive increase in the number of vetoes that are available for any kind of course of action and how difficult it is... And this shows up in permitting for new construction and stuff like that. But also shows up obviously inside of organizations.

(00:52:55):
And the challenge is that people, A, I think this is evolutionary biological. It's hard for us to understand the world, except by anthropomorphizing it. And so if it didn't rain this year, it's because a God is mad, and probably because we didn't sacrifice enough goats or something last year. It's hard for people to understand just that, wow, weather is incredibly complex and chaotic, and ecosystems and climatology, and all that.

(00:53:27):
Same thing with the world. Like if I am struggling to pay all of my bills and be able to afford a little bit of luxury in the sense of location or a present for my kids or whatever, it's got to be somebody's fault. There has to be a decision that's made somewhere. And the reality is everything is so complicated. Everything is so multivariate, it's not satisfying. It's a terrible political message.

(00:53:56):
It's much easier to say that there is like, oh, we understand why things are bad in the way that you're concerned about. And it's turns out that it's some someone's decision, and because of them it's bad. And so if we got rid of them or were able to overcome their decision, overturn it, and institute our own thing, then things would be good for you. And this really to me shows up inside of those organizations as well. I'll pause there.

Lenny Rachitsky (00:54:25):
I know kind of along those lines, you're a big believer in something called Parkinson's Law.

Stewart Butterfield (00:54:31):
Yeah. So the original of that is, I think it's 1956. It's an article in The Economist by Parkinson. And the Maxim is work expands to fill the time available for its completion. And the way that it shows up, this is a little bit subtle. So like one of the things I found, since I don't have a job is there's much less time pressure. And that maxim, like if you want something done, give it to a busy person. The inverse is also true that like, if you're not that busy, wow, basic things take a really long time.

(00:55:09):
And so Parkinson actually starts out with his example of writing and posting a letter. And I don't remember who he used with the first example, but someone who's incredibly busy and has all these things they have to respond to. And then another case like a retired robot who has all the time in the world. It takes her a long time to write the letter. It takes her a long time to put it in the envelope, and then you go to the post office and post it.

(00:55:28):
But the real meat of it is, for me later when he talks about the size of the organization, and he uses a bunch of examples. This is again 1950s, and he's British, so he's looking at the Royal Navy. And specifically he's looking at a chart that shows the relationship between the number of capital ships in the Navy, the number of sailors, and the number of administrators. And very familiar graph for people looking at any part of government. Any part of the relationship between the number of administrators at a university and the number of students and faculty, teaching faculty. Where it's like, okay, the number of ships goes like this and the number of sailors is looking right along with it. And the number of administrators goes like this.

(00:56:14):
And the reason this ties into the work expands to fill the time available for its completion is people hire, and they train. And here's the sad truth for anyone running a company is there are exceptions. There's certain types of engineers that are an exception to this. But the overwhelming majority of people you hire want to hire more people who report to them. And it's not because they're evil, and it's not because they're stupid. In fact, they're smart because everyone knows that the number of people who report to you correlates with your career trajectory, the amount of money that you're paid. The amount of authority you have inside the organization and on and on and on.

(00:56:57):
So we would hire 27 Royal product managers in Slack who immediately want to hire someone. It's like, what the hell? What would that person do? And they articulate it this way, but essentially it's like, "Well, that person would do the product management and then I would do strategy."

Lenny Rachitsky (00:57:11):
Classic.

Stewart Butterfield (00:57:12):
It's really, I think the essential thing to understand about this is it's not because people are evil, and it's not because they're stupid. And it's to me, very related to everything is complex. And if maybe this is my butterfly's law, I haven't thought about this way before. But I tweeted this a very, very long time ago like if you... Everything is simple if you have no idea what you're talking about. So the other side of that is like if something seems simple, probably you don't understand it. And there's obvious exceptions to that.

(00:57:53):
But for anything that involves a large organization or a lot of human beings, if the problem seems simple, you don't get it. So every budget process, no head of engineering know, head of sales, no CFO, no GC, who's ever going to come back and say, "Oh, I've actually think next year we can just hire fewer people. Or we're going to keep it flat or we're going to shrink through attrition because we don't need any more people to do what we're doing." Not because they're evil, not because they're stupid, but it's almost overpowering impulse inside the organization that often leads to disastrous results. And so there's an...

(00:58:30):
I'll give one example from Slack's history, and I have tried in the past to disguise this example so that no one feels bad about it but I... Unfortunately, the specifics are so important to the example that it's not disguised and so I'll just reiterate that the people involved aren't stupid or evil. And one example that's from the outside. So the example inside of Slack was we introduced threads, which was the ability to reply to a message inside of a channel. And let's say you, Lenny, post a message. I, Stewart reply to it. You will automatically get a notification. And now Sarah later on replies to the same message. Both you and I, as people who have push in that thread will receive a notification that there's been more activity, and so on. So like every single time anyone replies to it.

(00:59:23):
So when the feature first was released or like when we did the final product review before it was released, the input box was pre-populated with at the person before you in the thread. And I was using the feature and I would put the insertion point there, select all delete, and then start writing my message. And even if I wanted to add someone specifically, I almost never wanted to start my sentence with at that, because it just made it hard to reference what they were saying before. So I said, "Get rid of this because, A, I think most people won't use it. Or if they did want to add someone, they're not going to want to do it at the beginning of the sentence.

(01:00:07):
And by the way, you're teaching them to use the product wrong. Because it's important that everyone understand that every previous poster in this thread will automatically receive a notification unless they've figured it."

(01:00:20):
So okay, we release it. Six months goes by and suddenly the at thing comes back. And so I messaged someone around the team and I said, "Hey, there's been a regression. This is super weird. I don't know what happened. But the at thing came back." And they said, "Oh no, this is on purpose. We did a bunch of research." And so I was like, "What?" And I went through this and it was, if I recall correctly, it wasn't even P-95 certainty on this analysis. But it was something like when we do this, threads are 2.17 messages long, versus 2.14 messages long on average for when we don't do it.

(01:00:59):
And so first of all, why is a longer thread better? Like maybe a shorter thread is better? It can be fewer messages that people have to go back and forth. Also, that's such a tiny difference. Also, again, I don't remember the actual statistical analysis, so I'm not going to claim that it was incorrect. But I'm pretty sure this was outside the bounds of certainty that they can have. But the real thing was, oh my God, so you guys put flags into the product, you A-B tested it. You did the instrumentation. You created tables in the database or whatever we're using to record all of that.

(01:01:39):
You wrote queries to pull that. You created charts based on that data. You had meetings to discuss it. And just kind unpacking all of the things that would've had to happen for this to come back. And it's like thousands of person hours at a minimum, because any feature change at that scale of organization, it's involving like a dozen people. Engineering, QA, analytics teams, project managers, user research and stuff like that. The problem with that, so I think it was a bad idea, right? But the problem with that was the difference that you could possibly achieve between having this feature and not having this feature is like this much whatever units you want. The cost of doing the analysis was this much. So it's guaranteed to be a loser.

(01:02:29):
Like there's just, there's no world in which anyone could imagine putting the at previous respondent in the thread at the beginning of the message could possibly make that much of a difference to the quality of Slack, and how much utility it provides for people and all of that. But you know that to put the feature flags in, to ship new versions of the product, to put the instrumentation in. To have it all the API calls to record every action that people take to do all the analytics, to create the dashboard. To put paste a screenshot of that into a Google Slides presentation. To send the invitations to the meeting, to reschedule the meeting because someone couldn't make it. To have everyone sit down and look at the thing. Like guaranteed loser.

(01:03:14):
And I know that Fareed told you to ask me about this hyper realistic work-like activities. And so here's my grand theory. Hyper realistic work-like activities goes along with this other concept called known valuable work to do. And when I say known, I mean both you know what it is and you know that it's valuable. And the problem with almost every organization at the very beginning, you have an enormous amount of work that you know what to do, and you know that it's going to be valuable. So like starting a business, open a bank account. Because there's almost infinite general value of opening a bank account. You have to do it. It's very simple to do.

(01:04:01):
And so at the very beginning of any startup, they're like, "I'm creating a user's table, and I'm doing sorting passwords," and you're doing all the things that are kind of absolutely necessary. And everyone knows exactly what they are. And so everyone's going to work in the morning and they're like right on. And I have 10 things to do, and every single one of them is something I know how to do. And it's definitely going to be valuable. Time goes on. And the relationship between the supply of work to do and the demand for doing work just starts to change.

(01:04:32):
More and more people get hired. Every product manager wants to hire a junior product manager. Every new person, the first person you bring in on the risk and compliance team is like, "Oh my God, there's so many risks and things we have to be compliant with. We better hire more people on my team to do more risk and compliance work." Which probably to some degree is right. But we're going to have more and more of those people and they're going to call meetings with each other.

(01:04:54):
And now suddenly you have all these people with work to do and you've done all the easy obvious stuff. And now your questions are like, "God, should we do FedRAMP high and make a Slack version? Which is going to require us to have wholly separate physical infrastructure for the hardware that runs the software? And also a whole different operations team, which has only US citizens on it? What is the possible number of dollars that we could make from doing this? And how much complexity is going to be when we want to do updates to the software because we update two totally separate independent systems and rec."

(01:05:27):
It just gets out of whack, and so people end up... Like if you hire 17 product marketers, you're going to have 17 product marketers worth of demand for work to do. And if you don't have sufficient supply of product marketing work to do, they're just going to do other stuff. Again, very important, not because they're stupid, not because they're evil. But because they're like, I'm a product marketer and I want to be recognized for my work. And my spouse has criticized me because they take, I should have already got promoted in the last cycle, and they really got to demonstrate some wins here and whatever it is.

(01:06:02):
And so people are like calling meetings with their colleagues to preview the deck that they're going to show in the big meeting to get feedback on whether they should improve some of the slides. And that hyper-realistic work-like activity is superficially identical to work. Like we are sitting in a conference room and there's something being projected up there, and we're all talking about it. And that's exactly what work is. Hopefully not all of work for everyone inside of your company. But that's exactly what we do when we're working.

(01:06:34):
But this is actually a fake bit of work, and it's so subtle that I'll do it. Our board members will do it. Every executive will do it. And the further you are from having all of the context and all of the information and the decision-making authority and stuff like that, the easier it is to get trapped in this stuff. And people will just perform enormous amounts of hyper-realistic work-like activities, and have no idea that that's what they're doing. And the result of that, I guess, is that if you are a leader, if you're manager, director, an executive, you're the CEO, it's on you to ensure that there is sufficient supply of known valuable work to do. And there almost always is, but it's creating the clarity around that. Creating the alignment. Making sure everyone understands it, but that's what they're supposed to be doing, and then obviously doing it.

Lenny Rachitsky (01:07:26):
Amazing. I could listen to Stewart's rants all day. Hyper- realistic work-life activities. We need to coin this-

Stewart Butterfield (01:07:34):
Unfortunately, it doesn't make a good acronym. It's pretty ugly.

Lenny Rachitsky (01:07:34):
Okay.

Stewart Butterfield (01:07:37):
[inaudible 01:07:37].

Lenny Rachitsky (01:07:36):
Okay. [inaudible 01:07:37] it a try. And just to close the loop on that, the solution is the leader recognizing this is happening and stopping it. Telling people why are we spending time on this thing that is not going to get us anywhere?

Stewart Butterfield (01:07:48):
Yeah. And what you just said probably isn't the best way because that sounds like you're chiding them, and they're dumb. When it's actually your responsibility to make sure that there's sufficient clarity around what the priorities are, and explicitly saying no to things upfront and stuff like that. Rather than merging and say like, "Hey, you guys are a bunch of idiots wasting your time on this thing that doesn't matter." Whose fault is it? It's the manager's fault. It's the VP of whatever's fault. It's the CX, whatever, it's the C... Ultimately, it's the leader of the organization that has the responsibility to make sure that there is sufficient known-valuable work to do. And that's actually harder than it might appear.

Lenny Rachitsky (01:08:32):
Okay. Before we run out of time, I want to touch on two other topics. One is, when people think of Stewart Butterfield, I think a lot of people think of, We Don't Sell Saddles Here. Your legendary Medium post that is just, I don't know, it's become a historic piece of literature in the annals of product building and in startups. I haven't heard people ask you much about this recently. So let me just ask a couple of questions. What was the reason you put that out? What was the backstory on writing that memo? Why was it necessary?

Stewart Butterfield (01:09:01):
Well, it really was an internal memo.

Lenny Rachitsky (01:09:00):
... Memo. Why was it necessary?

Stewart Butterfield (01:09:01):
Well, it really was an internal memo and there's a bit of a digression. One of the crappy things about Slack is if all your corporate communication is on email, depending on exactly how it works and what system you use, you probably walk away with an archive of everything you said at Company X. If it's Slack, once you're turned off, you lose access to all that history. And so it's kind of like, "Oh, man. If I had only exported all of my messages before I left, I would have all this stuff," but that was absolutely verbatim. I did not change a word of what I said inside the company. Well, I think we were still eight people. Maybe at most 10, but I think it was eight people.

Lenny Rachitsky (01:09:45):
It was before Slack launched even.

Stewart Butterfield (01:09:47):
Yeah, it was before Slack launched. It was when we're doing private beta. And the point of it was to start to instill those ideas as early as possible and really create this alignment inside of that small team so that it could persist to survive as we grew and scaled. Yeah, that was the idea.

Lenny Rachitsky (01:10:11):
And the gist, just for people that aren't super familiar with it, but we'll link to it, is just it's not enough just to build a great product. You just as much have to put effort into communicating what this does for them, the problem this is solving for them, the outcome this is going to achieve for them. Is that a good way to think about it?

Stewart Butterfield (01:10:28):
Yeah. And again, comparing it to beer or cars, beer goes back to pre-civilization. Cars were obviously [inaudible 01:10:38], but at some point you had to convince people why they would want a car instead of a horse. For your new AI-based recruiting tool or your calendar app or whatever, there's some reason why you think that people should use yours instead of the thing that they're using now, which might be a wholesale one-for- one replacement, or more often is a change in the way that you're working that has a bunch of other adjacencies and you want to expand into these other categories. You're not just responsible for creating the product, but also, to a certain degree, creating the market.

(01:11:15):
There's this book, Positioning, which is an absolute classic. It's very short. I would recommend everyone read it, where the point of it is, from my perspective, it's almost impossible to create a new idea in someone's head. It's much easier to take a couple of existing ideas and put them together. So it's much easier to say it's like Jaws meets Star Wars, or it's Uber for Pets or something like that, than to come up with an actual new idea. But you have to do that because if your thing is different in any significant way from the alternatives, you're not just creating the product. You're creating the market. They're really kind of one and the same.

Lenny Rachitsky (01:11:56):
The reason I wanted to touch on it is I think still people continue to not listen to this advice and continue to over-invest in more features, more products, things like that. Just the specific example of, "We don't sell saddles here," just to quickly communicate this to folks, and correct me if I'm missing anything, is just instead of, "Hey, look at this amazing saddle we've bought," which you want to communicate as, "Here, go horseback riding. Look at this incredible experience you can have." And then they decide, "Oh, shit. I need to go buy a saddle to do that."

Stewart Butterfield (01:12:23):
Yeah. And 100%, that aspect of it is not original because I think that's something that marketers have done for a long time, certainly in the marcom and advertising. If you want to sell Harley-Davidson's, there are people who are going to geek out on the engines and stuff like that and the quality of the leather and stuff like that. But when you're selling the motorcycle, you're selling the open road and freedom and the wind in your hair. And if you're Lululemon, you are obviously selling yoga pants, but you're also selling health and aspiration and being the best version of yourself and a bunch of other stuff. Oh my God, I forgot the classic version of it.

Lenny Rachitsky (01:13:00):
There's the ship ...

Stewart Butterfield (01:13:00):
You're selling the screwdriver.

Lenny Rachitsky (01:13:04):
Oh, yeah. The nail.

Stewart Butterfield (01:13:05):
Yeah, the nail. Anyway.

Lenny Rachitsky (01:13:07):
Yeah, we missed that one. Well, there's the one I think about is instead of trying to convince men to build a ship, instill a yearning for the sea.

Stewart Butterfield (01:13:16):
Yes. Exactly. That's something that goes back in history.

Lenny Rachitsky (01:13:21):
Okay. Let me ask you about pivoting. You are potentially the king of pivots. You started two companies both famously pivoted, both from video games, which is why I asked you about that at the beginning, into very successful companies. I imagine many people come to you for advice on pivoting. Let me just ask when folks come to you asking, "Should I stick with my idea? Should I pivot?" what sort of advice do you find most helps them?

Stewart Butterfield (01:13:43):
Yeah, I mean, I think it's partly an intuition because obviously the decision is about, "Have you exhausted the possibilities?" and in the case where we were working on Glitch, this game where we used IRC for internal communication and we added a bunch of IRC which became the Proto Slack. I think Slack had an enormous advantage in the fact that we are working on this for several years without actually explicitly working on it and only doing the minimum number of features that were absolutely guaranteed to be successful in the sense that it was so irritating that we couldn't stand it anymore or such an obvious improvement that we couldn't help but take advantage of it. We still had $ 9 million left and everyone still liked the game and we were all happy working on it, but I think by that point I had exhausted every non-verdiculous long shot idea to make it commercially successful, and so I decided to abandon it.

(01:14:52):
But the default advice for anyone in anything is persevere. It's like a kitten hanging off the branch and a poster says, "Hang in there." There's so many stories of, "So-and-so started out going door-to-door and was rejected by everyone and then suddenly there was Nike," or something like that and just, "If you stick with it long enough, you'll eventually be successful." I think you have to really be coldly rational. Some of this shows up in the book Thinking in Bets. Some of it's in Annie Duke's second book, the title of which I'm forgetting right now, but someone will know it.

Lenny Rachitsky (01:15:35):
Yeah, Thinking in Bets, and then what was the second? I forget.

Stewart Butterfield (01:15:39):
She actually uses Glitch and Slack as an example of a smart fold basically. My expected value here has diminished to the point where this alternative looks more attractive. And the reason I say you have to be coldly rational about it is because it's fucking humiliating. I convinced so many and you have to convince so many people to get a company off the ground. You have to go to investors. You have to go to early employees and say, "You should leave your other job and come work for this because here's the incredible feature we're imagining." You have to go to the press and you have to make all these promises and you have users and you've committed things to the users and you've convinced them to give up their time for this thing. And so I think for a lot of people, it feels better to just keep doing it until it dies of suffocation due to lack of capital or something like that. Then just to admit, "Okay, I was wrong. This didn't work," and it's humiliating. It's painful. It's wrenching. It has a bad impact.

(01:16:46):
When we shut down Glitch, there was a lot of people who loved it and would spend all of their free time and couldn't wait to get home from work to go play it more. And that was their community and the community just disappeared, all these people and all these identities that have been created. And obviously, people lost their jobs and people who had moved their families to a different city in order to take this job now weren't going to have a job anymore. So pivots aren't something I take lightly. I think it's very different to be like, "There's three of us and we started making this app and then we pivoted to a different app." That doesn't even really count. If you're six months into something, you're still messing around. You're trying to figure out what it is that you're building. It's not really a pivot. Obviously in this case, it worked out great and there's survivorship bias and that doesn't mean that everyone should pivot all the time. But I think creating the distance so that you can make an intellectual, rational decision about it rather than an emotional decision is essential.

Lenny Rachitsky (01:17:50):
I love, also, your piece of advice of just exhaust. Once you've exhausted all the ideas, that's a really good time to see what else is out there.

Stewart Butterfield (01:17:56):
Yeah, just all the good ideas.

Lenny Rachitsky (01:17:59):
All the good ideas,

Stewart Butterfield (01:18:00):
All the realistic. Yeah.

Lenny Rachitsky (01:18:03):
Yeah. The point you made about just kind of persevering, I just had Melanie Perkins, CEO of Canva, in the podcast. 100 investors rejected her before somebody finally decided to invest and she just kept pushing.

Stewart Butterfield (01:18:19):
Yeah. I think that's a slightly different example, right? She eventually believed in the concept of the product and in the vision. It was just trying to figure out the right articulation to get investors who ended up being obviously very, very happy.

Lenny Rachitsky (01:18:31):
Extremely happy. Oh, geez. Okay. Maybe a final topic depending on how time goes. I want to talk about generosity. I talked to a bunch of people, as I said, that have worked with you and the number one theme that came up again and again and again when I asked them about you and what has stuck most with them is just generosity. So I'm going to read a few examples that I heard from folks that are examples of your generosity over the years.

(01:18:57):
So one person shared that he needed a little money before Christmas and he said, "Stewart literally walked me out of the building, went to the cash machine, handed me $500, told me to go home to my family." Other folks shared that, when you talked about Glitch just recently when you had to lay people off, you cried real tears when you were laying people off and then you spent an incredible amount of time helping them find new jobs and extending their severance pay and just taking it extremely, extremely seriously, much more than I think most people feel like CEOs do. Someone else shared that you paid 100% of employees health insurance to give them just fewer things to think about.

(01:19:35):
When you went public, you basically created the best possible situation for employees, no lockup, direct listing. Also, with the structure of the Slack deal, people said that acquisition was very employee friendly. That's employees. There's also just the way you thought about customers. A few examples: You gave free credits to businesses who were struggling to pay the bills during COVID. You released this fair billing, which I think was very innovative at the time, where you stopped charging people for seats they weren't using, even though they signed a deal to charge for those seats. A lot of times, you slipped release schedules because you just wanted to make features better and better for people. And I'll end with this quote: "Stewart is a leader who takes the responsibility he feels for his employees personally, and to which he extends the most generous circumstances he could muster. That feels worth celebrating."

(01:20:25):
So first of all, I just want to celebrate you. I think it's really rare and inspiring to meet a leader like that. Clearly, you've had a lot of impact on a lot of people. I don't know exactly the question I want to ask, but I guess in what part is this intentional, just like, "This is how we win. I'm going to be very generous and help people because I know this will help long-term"? How much of this is just a [inaudible 01:20:48] and it's just the way you are as a person?

Stewart Butterfield (01:20:49):
I think a lot of it is just the way I am as a person and I had wonderful parents who raised me right, but I think there is a little bit of a lesson there and I'm just going to assume people's familiarity with the prisoner's dilemma. The acts of generosity to me are, "Oh, I am demonstrating that I am going to cooperate as we iterate in this game." And if you do that, then people will also cooperate and you both benefit. Whereas if you never really know if the other person is going to defect at the first opportunity, then your best bet is to defect. And so there's a game theoretic aspect, usually in games that are much, much, much more complicated than the prisoner's dilemma.

(01:21:36):
I think one thing I didn't touch on before, but to me was important enough, is that at more than one company all hands, I made everyone in the company repeat this as a chant. It was, "In the long run, the measure of our success will be the amount of value that we create for customers." And I wanted to be super clear and explicit about that because it should be if anything you're doing feels like a little bit shady, a little bit cheating, a little bit maximizing at the wrong moment or taking advantage of a customer or anything like that, definitely shouldn't do it. Because to me, I mean I think it's literally true, but it's also an ethical way to run a business. And it's not just that the ethics are good. It's like there's advantages for you. You're able to attract a better class of employees. If all your employees are ethical, then it's going to be a better place for everyone to work and you're going to be happier and you're going to have fewer internal problems and all that stuff.

(01:22:48):
But I think it really is true that especially in the long run, you can't destroy value for your customers and expect to be successful. You have to actually make their lives better. And you could put effort into pointing it out to them and demonstrating that you have created this value and stuff like that, but there's no substitute for actually having created it. And I think that is incredibly important and that implies a real generosity, whether that's in negotiating terms with an enterprise deal or that's policy decisions. One time that it blew up in our face was our SLA was like, "For any downtime, you get 100 times your money back." Because from my perspective, it's like if we're down for two minutes, it's like pennies. It doesn't really make any difference. If we're down for 10 hours or something like that, then we have bigger problems than paying back people.

(01:23:51):
Fast-forward, we now have hundreds of millions of dollars in revenue and we've gone public. And shortly after we go public, we have one of the biggest outages we ever had. I don't remember how long it was, but it was many hours. But by the time we got that scale, 100 times the money back for the third of a day that we were down was $8 million or something like that. It didn't cost us any money because we just gave it to people in the form of credits, but it meant that a bunch of revenue that we had already anticipated for the next quarter wasn't going to show up because people's credits were going to offset what they would've otherwise paid us. And so we definitely changed the terms of service after that because being a public company is a little bit different. But in every other respect, I think they were all really important decisions that were helpful in us becoming successful.

Lenny Rachitsky (01:24:47):
Was that policy ... It was automatic? You didn't even have to claim it. It was just automatically you get this credit?

Stewart Butterfield (01:24:52):
And the default is you don't have to pay if you let us know. This was, "We will automatically, proactively, preemptively without any input from you ..."

Lenny Rachitsky (01:25:00):
Too generous.

Stewart Butterfield (01:25:01):
"Apply this credit to your account, and just send you a message that it happened. And by the way, we will do it on the aggregate for downtime, even if the issue didn't affect you as a customer."

Lenny Rachitsky (01:25:13):
Wow. Too generous. You found the edge of where you want to be.

Stewart Butterfield (01:25:13):
Yeah.

Lenny Rachitsky (01:25:18):
What was that mantra again that you had the company chant? I think this is a really nice way to end it.

Stewart Butterfield (01:25:22):
It was, "In the long run, the measure of our success will be the amount of value we create for customers."

Lenny Rachitsky (01:25:28):
Incredible. I'm just trying to picture the entire team at Slack reciting this mantra.

Stewart Butterfield (01:25:33):
It was hundreds of people. It felt very like, Kim Jong-Un or Stalin or something like that.

Lenny Rachitsky (01:25:38):
Well, on that note, most people don't know this about you, but your actual name when you were born was not Stewart. It was Dharma.

Stewart Butterfield (01:25:46):
Yeah.

Lenny Rachitsky (01:25:46):
And this all makes sense as you learn that.

Stewart Butterfield (01:25:49):
Yeah. My name is Dharma Jeremy Butterfield, so my parents named me. And when I was 12, I changed it because I just really wanted to be normal and for some reason I thought Stewart was a normal name. And by the way, you'll notice this now that I said it. Any character except for Stuart Little the mouse, anytime you see a character in a movie, a novel, TV show or whatever, there's only the loser Stewart and the asshole Stewart. It's obviously, in the collective consciousness, a terrible name and I shouldn't have chosen it and I regret it. But by the time I realized that, Dharma and Greg had already come out and it would've seemed like I was bandwagon jumping. And people thought it was a girl's name, even though in India it's obviously only a boy's name.

(01:26:32):
I'm going to add just one last little tidbit because I forgot about this earlier on and I think it helps tie things together, and it's called the owner's delusion. And this is based on something I posted on Twitter. The person who came up with the name later deleted their account and so I have no idea who it was and who to credit for this. But what I had posted was, and this was a long time ago when restaurant websites have gotten better and it doesn't really matter because Google Local was taking over everything, but this is, let's say, 10 years ago.

(01:27:00):
There's five things you could possibly want when you go to a restaurant's website and it's their street address, their phone number, the menu, the hours of operation ... Oh my God, I'm forgetting the fifth thing. Oh, and making a reservation, how to make a reservation. And again, this problem has to some extent taken care of it's itself or at least improved, but what you would get was this super slow loading photo, the Ken Burns effect as it [inaudible 01:27:30] ...

Lenny Rachitsky (01:27:29):
The flashed.

Stewart Butterfield (01:27:30):
And then fading in and then some music starts playing. And then if they show you the phone number, it's not clickable.

Lenny Rachitsky (01:27:38):
Image.

Stewart Butterfield (01:27:39):
It's not even text that you can copy because yes, it's an image. And they don't have the hours. They don't put the address or whatever and it's just like, "What?" For sure, whoever made this website for the restaurant owner and the restaurant owner themselves have definitely been in the position where they went to somebody else's restaurant website because they wanted to get the address or the opening hours or the phone number or whatever. So why does it end up like this and what should we call this?

(01:28:01):
And whoever replied to the tweet, she said, "We should call it the owner's delusion," and I was like, "Oh my God. That's perfect." And I think that is incredibly powerful and what ends up with the result, like Apple naming whatever that feature is called Sleep, which it's too hard to understand what that can possibly mean. And that's why people anticipate, despite the fact that when they get to your website for the first time, their intent is absolutely the minimum number of micro points above the threshold required from them to actually take that action.

(01:28:41):
You're like, "All right. Welcome to my website," and there's a bunch of BS and there's a bunch of stuff that doesn't make any sense and the buttons are inscrutable. And it's unclear what to do next because I think that my thing is so important and I don't recognize that you are at work and you were late this morning and you have to go to the bathroom and you're just a regular human being who has stuff going on, that you're concerned that your kid is a fuck-up and they're getting in trouble at school and stuff like that. They're not subjects who paid money to go to your play and are sitting in the audience and waiting for that curtain to go out. They're people who are going to bounce in a fraction of a second. And so everyone should always be conscious of the owner's solution.

Lenny Rachitsky (01:29:27):
I love that. What's the solution? Is it have other people look at it and give you feedback?

Stewart Butterfield (01:29:31):
Yeah, and recognize it. And unfortunately, it's one of those things like Murphy's Law.

Lenny Rachitsky (01:29:35):
Yeah.

Stewart Butterfield (01:29:37):
Even you can go wrong even when you take into account Murphy's Law.

Lenny Rachitsky (01:29:39):
That's right.

Stewart Butterfield (01:29:41):
But if you don't name it and recognize it and discuss it and train yourself to think that way, take a breath, pretend you're a regular person, and then look at this again and see if it makes sense, then you're screwed.

Lenny Rachitsky (01:29:55):
I love that. I love that you threw this in here. I have a billion other questions I'm going to ask you in part two when we do this someday. Stewart, thank you so much for doing this. Thank you so much for being here.

Stewart Butterfield (01:30:04):
Yeah. Thank you for having me, Lenny. I really enjoyed it.

Lenny Rachitsky (01:30:07):
Same here. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

