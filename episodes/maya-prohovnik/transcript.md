---
guest: Maya Prohovnik
title: Building Anchor, selling to Spotify, and lessons learned | Maya Prohovnik (Head
  of Podcast Product)
youtube_url: https://www.youtube.com/watch?v=1gXNOJEWajU
video_id: 1gXNOJEWajU
description: 'Maya Prohovnik is currently Spotify’s Head of Podcast Product. She was
  employee #1 at Anchor, which was acquired by Spotify in 2019 and now powers more
  than 80% of all new podcasts created...

  '
duration_seconds: 4056.0
duration: '1:07:36'
view_count: 3797
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- onboarding
- metrics
- roadmap
- user research
- data-driven
- monetization
- subscription
- revenue
- hiring
- culture
- leadership
- management
- strategy
---

# Building Anchor, selling to Spotify, and lessons learned | Maya Prohovnik (Head of Podcast Product)

## Transcript

Maya Prohovnik (00:00:00):
We were obsessed with reducing friction, this was our constant battle. And so we hired a couple of college interns and we brought them in and we were like, people are going to push this magical one button in the Anchor app and they're going to say, I want to distribute my podcast, and your job is going to be to do all that same manual stuff manually, but to them it's going to feel magical and it happened automatically. I still don't know how many people know this. I think people think that we had some secret backdoor deal with Apple for distribution, but we just had college students making Apple podcast accounts and then submitting hundreds of thousands of podcasts through these accounts, and I think that was a really big part of why we got so much hosting market share so quickly because it was such an insane benefit over the other platforms which otherwise had been commoditized at that point.

Lenny (00:00:48):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard win experiences building and growing today's most successful products. Today my guest is Maya Prohovnik. Maya is Spotify's head of product for podcasting where she oversees product design and engineering teams responsible for building the tools and experiences for podcasters and their listeners. Maya was also employee number one at Anchor, which Spotify acquired five years ago, which became the core of Spotify's podcasting hosting platform, which now powers over 75% of all new podcasts created in the world. In our conversation, we dig into why Maya is obsessed with dogfooding and why she encourages everyone on her team to create their own podcast. She's got four podcasts of her own, which are all very highly rated and people love. We dig into how she stays productive and organized in a very hectic senior leadership role, what she's done to allow for Anchor to continue to operate like a startup within a larger organization.

Lenny (00:01:44):
Also, a bunch of really fun early Anchor stories, including how interns uploaded podcasts to Apple and Spotify manually before they could automate that. Plus, how to find a balance between using your gut and using data to make decisions. Also, public speaking tips, so much more. Maya is amazing and I'm really excited for you to hear this episode. With that, I bring you Maya Prohovnik after a short word from our sponsors. This episode is brought to you by Sidebar. Are you looking to land your next big career move or start your own thing? One of the most effective ways to create a big leap in your career and something that worked really well for me a few years ago is to create a personal board of directors. A trusted peer group where you can discuss challenges you're having, get career advice, and just gut check how you're thinking about your work, your career, and your life.

Lenny (00:02:33):
This has been a big trajectory changer for me, but it's hard to build this trusted group. With Sidebar, senior leaders are matched with highly vetted private supportive peer groups to lean on for unbiased opinions, diverse perspectives, and raw feedback. Everyone has their own zone of genius, so together we're better prepared to navigate professional pitfalls leading to more responsibility, faster promotions, and bigger impact. Guided by world-class programming and facilitation Sidebar enables you to get focused tactical feedback at every step of your journey. If you're a listener of this podcast, you're likely already driven and committed to growth. A Sidebar personal board of directors is the missing piece to catalyze that journey. Why spend a decade finding your people when you can meet them at Sidebar today, jump the growing wait list of thousands of leaders from top tech companies by visiting sidebar.com/lenny to learn more. That's sidebar.com/lenny.

Lenny (00:03:29):
This episode is brought to you by Wix Studio. Your agency has just landed a dream client. You already have big ideas for the website, but you have the tools to bring your ambitious vision to life. Let me tell you about Wix Studio, the new platform that lets agencies deliver exceptional client sites with maximum efficiency. How? First, let's talk about advanced design capabilities. With Wix Studio, you can build unique layouts with a revolutionary grid experience and watches elements scale proportionally by default. No-code animations at Sparks of delight while adding custom CSS gives total design control. Bring ambitious client projects to life with any industry with a fully integrated suite of business solutions from e-commerce to events, bookings and more, and extend the capabilities even further with hundreds of APIs and integrations. You know what else? The workflows just make sense. There's the built-in AI tools, the on canvas collaborating, a centralized workspace, the reuse of assets across sites, the seamless client handover, and that's not all. Find out more at wix.com/studio. Maya, thank you so much for being here, and welcome to the podcast.

Maya Prohovnik (00:04:38):
Thank you so much for having me. You and I have been trying to get together for almost a year now.

Lenny (00:04:42):
Oh, man. But it all worked out and it's going to be very worth it.

Maya Prohovnik (00:04:45):
You had a kid. I took parental leave.

Lenny (00:04:47):
Oh, right. That is true. Man, overlapping kid journeys. I also have been just really looking forward to this chat partly because you're amazing and partly because it just feels very meta to have the head of product of Spotify podcasting on the podcast, and I imagine many people are listening to this on Spotify, so there's this, I don't know, turtles all the way down situation happening.

Maya Prohovnik (00:05:08):
I totally agree. I was thinking the same thing when I was preparing for it where it's like so much of what we have to talk about is so meta, and then we also have you and I know each other because you've been sending me feedback about the podcast experience on Spotify, so lots of circular stuff there.

Lenny (00:05:22):
Speaking of Spotify and podcasting, clearly you've done an incredible job building podcasting on Spotify. From what I've read, it's the number one podcasting platform now. Is there a stat you could share by just the percentage of the market share essentially of Spotify podcasting?

Maya Prohovnik (00:05:37):
I think we are now officially over a third of global market share of podcast listening, which is pretty insane.

Lenny (00:05:43):
That is insane.

Maya Prohovnik (00:05:44):
Yeah.

Lenny (00:05:44):
Also, I think on the hosting side, it's an even bigger number. Is there a stat you can share by just maybe new podcasts that are launched and how many are hosted on Spotify?

Maya Prohovnik (00:05:53):
Yeah, I think at this point it's more than 75% of all new shows on Spotify are hosted with Spotify for podcasters, which used to be Anchor. When we were acquired by Spotify, I think Anchor had already gotten to 40% of all new podcasts or something crazy. So, yeah.

Lenny (00:06:09):
Insane. Okay, so for these reasons, I want to spend the time that we have together unpacking how you operate as a product leader and essentially what you've learned about product org leadership growth and all those things. How's that sound?

Maya Prohovnik (00:06:22):
That sounds perfect. My favorite topics.

Lenny (00:06:24):
Okay, let's do it. So as the first question I asked a PM who actually works for you, Wilma Chu, what to ask you, and the first thing that came to mind for her was this idea of dogfooding and how important dogfooding is to your way of operating as a product leader. As an example, you have three of your own podcasts on Spotify and I checked them out and they're all very highly rated, so they're not just like bullshit podcasts, they're real people actually listen and enjoy them. So my question to you is just why is dogfooding so important to you? How do you actually operationalize it? And then also maybe just talk about these podcasts that you have.

Maya Prohovnik (00:06:58):
Sure. Well, I can talk about them forever, so be careful because I'll take up the whole hour with that. But I actually have four podcasts. There's two that I don't update as much anymore. So my first ever podcast was about Stephen King books. I'm a big Stephen King super fan. So, when I joined Anchor, and we weren't even fully podcasts yet, if you recall, we were something else audio, we were trying to avoid being podcasts for a while and then we decided to just be podcasts. But when I got into audio and trying to help audio creators, the first thing I did was make my own podcast because I was like, I know nothing about production or what it feels to even be a creator in that way.

Maya Prohovnik (00:07:35):
And so I started my Stephen King podcast because that is the number one thing that I just love to talk about every day, which is one of my tips for podcasters. If you're trying to figure out what to make a show about, it's what can you talk about for? So I did that one for a while actually. I spent a ton of time editing it. I spent a ton of time on SEO and marketing it, and it got to the point, I think at its peak I was getting 5,000 listeners in a episode, which now seems small for a podcast, I know.

Lenny (00:07:59):
No, that's very legit.

Maya Prohovnik (00:08:01):
Yeah, for a test podcast that I was just doing to learn how to do my job, I was so excited to get that audience and I fell off because, well, mostly I had a kid, I joined Spotify. My life's really busy and that level of production is so hard to do if it's not your full-time job, but I still get emails all the time from people who are like, please bring it back. I never found another great Stephen King because I really got deep into the books and the connection between the books. So that was one of them. The second one I did, still going today. So my husband and I have this Big Brother podcast, the show Big Brother, it's terrible.

Maya Prohovnik (00:08:33):
I would not recommend listening to my podcast unless you are a Big Brother super fan, and I actually started that one because I wanted to get the other end of the spectrum where something we were really focused on with Anchor at the time was first time creators really growing the pie of podcasters and specifically we had this theory that podcast creation of the future would be mobile first and we had this really high-powered mobile app, and so I was like, I'm going to make a podcast that's fully mobile, not highly edited, not worry about making something that sounds like a traditional podcast. And I really leaned into all the Anchor features. So it's fully recorded on my phone. I do almost no editing, but I think the thing that's kept us going, because it's been six or seven years now we've been doing the show, it's really the community, the people who call in.

Maya Prohovnik (00:09:15):
I have no idea who these people are. I have no idea how they found this terrible show, but they love it. They call in every week. And that I think is one of the many things I've learned from dogfooding, a podcast creation app is that community piece is so important. If you don't know if anyone's listening, if you don't know what they like about it, if you don't know if they're coming back, it's so hard to keep investing the time. And then I made a show, my least known podcast, because it only got like 25 listeners for episode, it's about my favorite book of all time called Children of Time. It's actually a trilogy. And the reason it got almost no listeners is because there were tons of spoilers in the podcast and the book is like 800 pages long. So we were like, do not listen if you haven't read the book.

Maya Prohovnik (00:09:53):
So, it was very niche, but I think it's a really good podcast if you've read Children of Time. And then my last one I just started doing a couple of years ago is about parenting. So I have a son who's two and a half now and we have been documenting our journey as parents all the way from, we went through IVF, so starting with sort of fertility, I have a really fun episode about childbirth if people are interested in that sort of thing. And then ever since then it's just been episodes about the transition to parenthood, which has not been particularly easy for us, and now my son's a toddler, so lots of fun things happening there. You're not there yet, but you will be and then you can listen to my toddler episodes.

Lenny (00:10:27):
Yeah. I got to listen to the next... A few months ahead to learn from what you've learned.

Maya Prohovnik (00:10:31):
Yes, I think that's a good tactic.

Lenny (00:10:33):
Before we talk about dogfooding, have you ever considered going full-time on this stuff? This is always an option for people and clearly you've done great. At least two podcasts are killing it.

Maya Prohovnik (00:10:44):
I have not. And I think it's so funny because with my parenting podcast too, and even my terrible Big Brother podcast, I get compliments all the time and people are like, "I love listening to this." And my husband also is a really funny and a really good podcaster, but I don't know why I don't think of myself as a creator. I think to me it still feels like this exercise where it's like I'm making my podcast, but I'm really doing it so that I can learn about our product and get in the mindset of a creator. So I think the problem is I'm just too much of a product person. It's a means to an end for me instead of the end itself. But that is an interesting question because I know most people who podcasts, their ultimate goal is obviously to be able to do it full-time and that is interesting that I haven't thought about it.

Lenny (00:11:31):
You have a good backup plan of things if anything goes off the rails.

Maya Prohovnik (00:11:34):
I guess so, yeah.

Lenny (00:11:35):
Awesome. Okay. Just coming back to this idea of dogfooding, where does that come from for you? What have you learned about just how to execute that?

Maya Prohovnik (00:11:40):
It's just always been my natural state. I've had a handful of different product jobs and I guess they've all been tangentially related to helping creators or creative people. And so I think for me it's like I don't know how you can build those tools if you don't understand that mindset. I'm not surprised that it came to Wilma's mind when you asked her what to ask me because I am constantly yelling at my product team who do not have podcasts and being like, I really don't think that you can build the right things. If they talk to users all the time, they see the data, but all of them, once they finally start doing their podcast, they're like, I get it. Something clicked and now I feel like I really understand what they need. And I guess building tools for creators is similar to building a B2B product where you really have to understand business, it's their livelihood.

Maya Prohovnik (00:12:25):
And so I think if you're just looking at a list of feature requests, you're not necessarily going to prioritize it in the same way as if you deeply feel those problems. And I think for me, I don't know if I mentioned this to you, but when I first got into tech, I started in customer support, that was how I got into product, and so I think I just am a very user focused product person. I think there's different schools of thought for product and for me it's always been about making people happy, making their experience better, solving real problems in their lives. And so for me, becoming one of the users, I think it's made it so much easier for me to advocate for that being a pretty big chunk of the roadmap.

Maya Prohovnik (00:13:04):
I think if you don't have that, especially coming from someone in leadership, it's so easy to just fall into that trap of like, well, we're working on the next big strategic thing, which is two years away, and then in the meantime your users are getting no value and then they're just going somewhere else. So I don't know. I think it's really important to me. It makes sense to me and also, I'm not sure how else I would do product. I've never really not done it that way. It

Lenny (00:13:25):
Reminds me of Airbnb Brian was a huge advocate on the host side of the product is like, you need to be a host, but many people couldn't because they didn't have a place that could be hosted. Is there anything you've learned about just how to make this a thing that actually works effectively, a way to operationalize this for people listening, they're like, "Oh, I should start encouraging my team to do?"

Maya Prohovnik (00:13:42):
I'm constantly reminding our team to do this. And then I think that also comes from the other people who are doing it. So we really elevate the people on our team who have their own podcasts, we help them tell their stories internally. Whenever we do an offsite or any team activity, we'll always incorporate podcast creation or some way of making sure everyone on the team is using the tools. I don't know, I think a lot of it just comes from, I'm so vocal about this stuff. The other night I was recording a podcast and I DMed one of the engineers on our team and told him about this tiny little iOS bug and he was like, why are you DMing me about this at nine o'clock at night? I think I was also supposed to be on vacation, I can't remember.

Maya Prohovnik (00:14:20):
But then he got the bug fix the next day. And so I do think making that something that's really top of mind for the team that we do need to fix problems, that these things matter, I don't know. I always listen to the podcast that my team makes, so it's like I know they're going to get at least one listener. And then I think also I try, I think because I understand a big part of building tools for podcasters is understanding all the barriers to entry. It's actually a really difficult thing trying to get someone to put their voice out there, share their story, it's a really emotional journey. And so I feel like I've tried to turn some of the things that I've learned about podcasting into, I've never written it down, maybe I should, but I have a playbook that I'll tell people when they're considering making their own podcast.

Maya Prohovnik (00:15:02):
So it's just things like don't try and record by yourself, find a friend. That's a much easier way to get into it or don't follow a script because then you're going to feel really awkward and uncomfortable and not feel good about it afterwards. Or don't just record a test thing for 30 seconds and publish it because you have to make yourself feel the pain that we're trying to understand in our users.

Lenny (00:15:24):
What's cool about that that could turn into just onboarding education, basically your experience of making a podcast informs how to help new podcasters become successful.

Maya Prohovnik (00:15:31):
Totally, yeah. And also this is less about dogfooding, but one of my favorite things is I'm always just trying to convince everyone I meet to start a podcast, that's just become my annoying thing. And so if I'm interviewing someone for a job or if I'm at a party and mingling with people, it's like somehow the conversation always turns to their passions and then I'm like, you should make a podcast about it. And then they're like, well, I can't. And then I work my way through all the reasons they say they can't do it, and then they go start a podcast. So I'm like one person at a time.

Lenny (00:16:00):
I see how you're growing the platform now.

Maya Prohovnik (00:16:02):
Yes, exactly.

Lenny (00:16:04):
Very unscalable, hands to hand combat at parties. I get it. Okay. One thing you mentioned about being maybe the only listen of your coworkers podcast reminds me there's this platform where you could find Spotify music that has never ever been played once and you could be their first play and just go through.

Maya Prohovnik (00:16:22):
That is so cool.

Lenny (00:16:24):
It's very touching, right?

Maya Prohovnik (00:16:25):
Yes. I haven't seen that and now I'm like, how can we productize that for podcasters? That's such a cool thing.

Lenny (00:16:31):
Anyway, another area that I've heard you're really strong at and came up with Wilma and a few other people I talked to is you find a really good balance between being very data-driven and also very gut driven, and this is something a lot of product leaders try to get better at. And so I'm curious just what have you learned about try to find that balance and also is there an example of something where you went against the data and went with your gut and it worked out.

Maya Prohovnik (00:16:58):
If you remember the old days of the internet, I feel like there was really this different way of thinking about product development where it was so much more about what felt good and what made you feel something as a user in that product. And so it's like we used to be a lot more playful I think with software. I think we used to put a lot more emphasis on things like delightful animations or fun little Easter eggs, and I am not sure when or where that got lost, but it feels like product management as a role has gotten formalized and become a little bit more scientific, I'm generalizing, but I think a lot of product managers can be so focused on using the right frameworks and making sure that they have the right roadmap and all of this stuff.

Maya Prohovnik (00:17:37):
And then it's like you find yourself in this cycle where you're just building things to build them and not really thinking about the connection to the end user. I think data is amazing and I'm like, we have such an incredible insights team at Spotify, both my insights team and then the broader one. I think we are so lucky and we have so much knowledge about our users and different cohorts and what people need and what they're missing, and so I think that's extremely valuable. I think where people get into trouble is when they think that they can rely solely on the data. And so what I spend a lot of time talking to my team about is how we can balance that. So thinking about, I guess a couple general things I would say are there are right and wrong times I think for both for your gut and for data. And then there are lots of different kinds of data and different ways to use that data.

Maya Prohovnik (00:18:21):
So I think when you're in the trap of just being like, well, this is the process we always have with insights and we're just going to run this every time we have a feature, I don't think you're going to have a great time. I think if you think of it as part of the creative process as a PM where you're like, I have a hypothesis, I have some data that is helping me understand that hypothesis in the first place or form it in the first place, then I'm going to do some user research and try a couple of things and see what works for people. Then I'm going to make sure that we have success metrics and that we know what we're looking for when we launch, then we're going to follow, et cetera. So I think there's different times and places for all the different types of data collection that you can do.

Maya Prohovnik (00:18:58):
The other thing I would say is something that I have had to learn as a leader, especially as part of a larger organization, when we were a startup Anchor was like 20 people when we got acquired by Spotify. And by the way, Spotify is my first big tech company, so I've always been at startups, so I've learned a lot about that. But when I was leading product at a startup, it's like we're a small team, we're really focused on moving quickly. There isn't a whole lot of stopping to ask what data is supporting this or it's just like we talked to some users and we're like, great, that's a problem. We're just going to go and fix it. And I think at Spotify there's obviously at places like Spotify, I mean, large organizations, there's obviously a lot more people that you need to coordinate.

Maya Prohovnik (00:19:38):
There's a lot of people you have to influence that aren't on your immediate team. And so I think something that I've had to learn is that being gut driven isn't the same as just saying to people, I told you or I believe this, so you have to do it. There really is an art I think to balancing that. And I think that what I try to do is always still as objectively as possible explain why my gut is feeling that way. So it's like you can refer back to your years of experience or other things that you've done that have been similar. You can talk about your experience as a user testing this stuff. You can bring in stories and anecdotes from users to help back it up. And so I have found that that works obviously a lot better.

Maya Prohovnik (00:20:18):
And I think that in the times that either I have done this or I've seen other leaders do it, where they're just like, well, we're just going to do it this way even if you guys don't agree or if the data says something different, those projects are always immediately doomed from the beginning. They're never going to work. You can't drag all these people through something that they don't believe in. So I think I would think of your gut actually as a type of data and I think it's a totally valid one and it's just I think you need to be clear that that's what you're working with, but then it should be taken as seriously as any other data point. So I try and think of it that way where it's like this should all ideally work together. And obviously the more data you have and the more types of data you have, the more convincing you're going to be and the more right you're going to be.

Maya Prohovnik (00:20:56):
So I think it all helps. There were so many of these in the early days of Anchor because I don't even know, I don't think we had a data scientist until we were part of Spotify, so I think it was just engineers running queries. But there were a couple times where we had to move Anchor from 1.0 to 2.0 and then from 2.0 to 3.0, we did these big, I don't like to call them pivots, but sort of evolutions let's say, of our product or our strategy terminology also very important when you're trying to convince people of things. So when I was thinking about those big transitions for us as a team, I think both times we had these big moments with our teams where we had to get everyone on board with making these big changes. So with Anchor 1.0, I don't know if you remember, but it was actually similar to what Clubhouse I think just rebranded to more voice messaging and short form and more about connections between people.

Maya Prohovnik (00:21:50):
And that was the first thing we ever launched and people loved it. People were very excited about it, the data was all good. We had extremely retained users. We anecdotally, we were hearing all this stuff from users all the time that they were staying up all night to use the app, people were meeting each other and falling in love and getting married on our platform, all of these really kind of magical things and we were seeing the user base was growing consistently. But I think we had this feeling, and when I say, I mean, mostly Mike and I at the time, Mike was our CEO, that it just wasn't ever going to be big enough. And so we had this really interesting moment where the users were all telling us, there's no problem. We love this product. They were using it every day, they were coming back. It was slowly growing and we were just like, this just isn't going to get us to where we need to be, our original goal had been we wanted to democratize audio.

Maya Prohovnik (00:22:42):
We wanted to make it something where anyone could easily tell their story, and we were like, if we keep digging ourselves into this niche that a small number of people really, really love, that's great, but that's not really the mission that we sent out set out to solve. And so the 1.0 to 2.0 transition was I think actually pretty painful because for all of those people who had been invested in 1.0, 2.0 didn't work for them. 2.0 was much more about content creation and making more of a radio station, and it was less about telling your personal story and close relationships and more about projecting and using different tools. Anyway, so we made that call I think pretty much just on gut and it was like, this is a business decision. This is where we think the next phase needs to be.

Maya Prohovnik (00:23:25):
When we built Anchor 2.0, it was a lot more like the tools that we wanted to use, even though it wasn't what the user base was asking for. So I think that's one example of sometimes it's that whole users don't always know what to ask for, they don't always know what problems they need you to solve for them. And so I think you really have to be able to hear what's behind it or really even if the data is looking okay, think about if it's heading to where you need it to go.

Lenny (00:23:51):
Before you move on, that's actually such an interesting story because it's so hard to have a product that's working that people love and decide to change it completely. Many founders are probably stuck in this where they're just like, hey, this is working and we're feeling some fit. Is there anything else you learned from that? Because that's a really interesting insight and it worked out in your case clearly.

Maya Prohovnik (00:24:15):
It absolutely worked out. I mean, I think it was a terrifying transition. Us at the time, it took us a few months to build a whole new app, it takes longer now, but the whole time we were building it, we were like, we weren't sure if it was a mistake and we would go back and forth and we would feel guilty when we were talking to our users about what they wanted us to be working on. But I think it was one of those things where as soon as we launched 2.0, our numbers started shooting up and we started seeing more kinds of people were using it and people were suddenly using it in the way that we had always imagined as a replacement for the old school, very difficult to make traditional podcasts.

Maya Prohovnik (00:24:50):
I don't know. I guess the lesson is you have to be able to tell the signal through the noise, and even if you've got lots of vocal users asking for something, we used to have this rule, the 80/20 rule, where it's like you can't just build for that 20, I don't think we made this up by the way. I think this is a common thing, but we'd always refer to it and say, we want to be building for the 80%, and even though the 20% are going to be more vocal, that's just going to get you deeper into that hole of that problem of you're not really building for everyone. And I think particularly when you're trying to build a creative platform, you're trying to democratize something and your target user is everyone on the planet. I think you really have to be willing to kill your darlings and let things go when they're not getting where you need them to be.

Lenny (00:25:35):
That's probably the most common cases. Something is working, but it's not working incredibly well. What do we do? And so that's really interesting. I feel like the first thing you said there is really important of just we had a much bigger mission and vision, and even though this is working, this is never going to get there. There's no path to building a massive business.

Maya Prohovnik (00:25:52):
I do think that's so important, and I give a lot of credit to Mike and our co-founders. I think they really knew what they wanted to do when they started the company and they were very firm on that and never varied that throughout the years throughout the acquisition. And so I do think not everyone's goal is to build a massive multi-billion dollar world changing business, that's okay if that's not your goal, but if that is your goal, you have to stick to it and it's really hard, but you have to keep pivoting to get to where you want to be.

Lenny (00:26:21):
Kill your darlings. I love that phrase, I use it all the time. I think you had a second example. I have a couple other questions of Anchor, but did you want to share another example?

Maya Prohovnik (00:26:28):
Sure, I can just quickly, my second example was, so we actually had to do it again. So we went from Anchor 1.0 to 2.0, we were like, that was totally the right call. And then Anchor 2.0, we were still in this phase where we would always joke about it because people would be like, "Oh, it's kind of like making a podcast." And we would be like, it's not a podcast because we're trying to be bigger than podcasts. Because we were at the time, 2015, there were still so few people podcasting, it was still so hard to do. And so we originally were really stuck on this idea that podcasting was going to be limiting and that we wanted to be the next thing. In the early days of Anchor, we had all this nautical terminology, so we would call them waves and I don't remember what else, but we had cute nautical terms for everything we were trying to resist podcast and podcaster and those things.

Maya Prohovnik (00:27:11):
And when we launched Anchor 2.0, we started getting all of this really great traction and the number one feature requests that we got from people is they were like, great, I love using these tools and then I want to export it as a podcast and publish it and get people listening that way. And we resisted it for probably, I don't know, six months or something and we were like, absolutely not, that's not what we're doing. And I think that one was such an interesting lesson because we had just learned that we did the right thing by not listening to our users. So for a while we dug in and we were like, that's not the direction we're going in, they don't know what they actually want. And then when we decided, I think we started with like, oh, we'll do a little test and let people export us podcasts and see what happens.

Maya Prohovnik (00:27:48):
And when we look back at our data, that's the moment when we saw the beginning of that hockey stick growth where it's like we had been growing, we had been doing well, and then you zoom out and you're like, okay, that was very clearly the thing we were missing. Yet again, we had to stop what we were doing, we rebuilt the entire app, we built it around RSS and podcasting and being able to export. And we actually did some really cool things to make it really easy for people to publish their podcast everywhere. So I think that was really the moment that it took off. And I think it's so interesting putting those two things together because it was the opposite thing the second time that we had to give up on a piece of what we had thought was so inherently true about our business.

Maya Prohovnik (00:28:28):
And so I don't know what lesson to tell people to take away from that other than I think you have to just stay, especially in a startup mentality, you have to stay willing to be flexible and take in new information and new data points as your product matures and as your user base changes, there's going to be new things that you learn that are going to change how you think about it. And I think again, the one thing that was unwavering for us was our mission and everything else was mutable for us where we were like, whatever we need to do to get there will work. And I do think looking back, it's astonishing how brave we were that we kept finding some product market fit and being like, nope, that's not enough. And then moving to the next thing. And I think that obviously worked out really well for us and meant that we were able to do what we set out to do and really democratize the medium and make things a lot easier for a lot more people.

Lenny (00:29:15):
I think another lesson there is just try stuff. Like you said, you tried this export thing, let's just see what happens. No, we don't think this is where we need to go, but let's just try it and maybe it'll work. And clearly that became the core of the product and platform.

Maya Prohovnik (00:29:27):
Totally. And also, you never know which of those tiny product changes are going to end up being this existential moment for your business. You really have to keep your eyes open and be ready for that to happen anytime, especially when you're still trying to figure out where your place is going to be.

Lenny (00:29:42):
You mentioned there was this feature that made it easy to distribute your podcast, and this touches on a question that actually asked Mike Mignano, the CEO of anchor what to ask you. And he's like, ask her about the story of how you made that actually possible to distribute the podcast to platforms, and it ended up being a very unscalable solution.

Maya Prohovnik (00:30:00):
One of our principles from the very early days of Anchor was build things that don't scale, where we were like, we're a ridiculously tiny team. We're trying to do this really big thing. We had raised very little money, and so we were always just trying to figure out how can we hack into whatever growth we're trying to make happen. So when it turned out that people wanted to distribute their podcasts everywhere, it's gotten a little bit easier. But at the time, I'm sure you remember what podcast distribution was like, where it's like there's all of these different podcast platforms you have to manually distribute to all of them. Apple Podcasts in particular can be really difficult for people who aren't tech-savvy because there's this whole, you have to prove that you own your RSS feed, you have to know what an RSS feed is.

Maya Prohovnik (00:30:44):
You have to sometimes deal with 301 redirects. There's just all this stuff that's deeply technical in a way that we were just like it doesn't need to be. And so one of the steps there was to submit your podcast to Apple Podcasts, you had to have an Apple ID, and there are a lot of people in the world who don't have iPhones, and so we're building for everybody. So we were like, how can we reduce that friction? We were obsessed with reducing friction, this was our constant battle. And so we had this idea, we hired a couple of college interns and we brought them in and we were like, people are going to push this magical one button in the Anchor app and they're going to say, I want to distribute my podcast, and your job is going to be to do all that same manual stuff manually, but to them it's going to feel magical and it happened automatically. I still don't know how many people know this.

Maya Prohovnik (00:31:27):
I think people think that we had some secret backdoor deal with Apple for distribution, but we just had college students making Apple podcast accounts and then submitting hundreds of thousands of podcasts through these accounts. And that resulted in lots of interesting technical and relationship situations. It was a really interesting thing, and eventually that didn't scale, eventually we stopped doing that, obviously, but I think that is such a cool example of the importance of how you're packaging what you're offering to people where if we had said you request distribution and we'll have one of our team members get back to you in three days and let you know when you're on Apple Podcasts, that doesn't feel very magical or it's really saving you any time. If all you see as a user is you're hitting a button and then 24 hours later you're somehow magically on Apple Podcasts, that was so much easier than manual distribution was at the time.

Maya Prohovnik (00:32:20):
And I think that was a really big part of why we got so much hosting market share so quickly because it was such an insane benefit over the other platforms which otherwise had been commoditized at that point. So, it's funny now to think back on that, but I think it's also related to we were so good at being willing to humor what seemed like stupid ideas and try them. And so that is something that I definitely recommend to product people is let yourself have the silly ideas we always talked about yes and when someone has an idea, how can you build on it and think about how it might work instead of saying, no, that can't work because, and so we had a number of those things where it was like nobody understood how we were doing things so differently, and it was just because we weren't afraid to do the silly unscalable thing for a while.

Lenny (00:33:08):
I love that story. Touches on two things, one is I was just doing an interview around how to drive word to mouth growth and make that a big driver of your growth. And the main message there is just make something remarkable and knock people's socks off that they're just like, oh wow, this is crazy, I'm going to share it with my friend. And that's such a good example of that where everyone's like, wow, that was easy, I'm going to tell all my other friends that are launching podcasts. The other is, I wonder just how much of tech is built off of college interns, the beginnings of companies or how important college interns are to technology and innovation. It feels like there's always an intern story.

Maya Prohovnik (00:33:42):
Yeah, I know. I think they must be. And for the record, we paid them very well, these were not unpaid interns, just to be clear. But no, I think it is amazing, and I think it was also such a cool opportunity. One of those interns actually is still a PM on my team today. She ended up converting a full-time after she graduated. And I remember I had a lot of cool college internships and it's such a cool way to get exposure to industries that you otherwise wouldn't get to. So I would definitely recommend that college kids start with, it's okay if your first job is like a repetitive, not very exciting thing. If you do a good job, it will lead to something very exciting maybe.

Lenny (00:34:15):
I love that. Imagine a place where you can find all your potential customers and get your message in front of them in a cost-efficient way. If you're a B2B business, that place exists, and it's called LinkedIn. LinkedIn ads allows you to build the right relationships, drive results, and reach your customers in a respectful environment. Two of my portfolio companies, Webflow and Census, are LinkedIn success stories. Census had a 10x increase in pipeline with a LinkedIn startup team for Webflow after ramping up on LinkedIn and Q4, they had the highest marketing source revenue quarter to date. With LinkedIn ads you'll have direct access to and can build relationships with decision makers including 950 million members, 180 million senior execs and over 10 million C-level executives. You'll be able to drive results with targeting and measurement tools built specifically for B2B. In tech, LinkedIn generated two to 5x higher return on ad spend than any other social media platforms.

Lenny (00:35:14):
Audiences on LinkedIn have two times the buying power of the average web audience, and you'll work with a partner who respects the B2B world you operate in make B2B marketing everything it can be and get $100 credit on your next campaign. Just go to linkedin.com/podlenny to claim your credit. That's linkedin.com/podlenny. Terms and conditions apply. So we've been talking about Anchor and I think what's really interesting about Anchor is it's one of the very rare success stories of an acquisition working out incredibly well. It was a small startup now powering two thirds of all new podcasts. It's pretty insane. So I want to spend a little time on just what worked in making that possible. So let me ask first around the integration piece, just how you integrated successfully, and then I want to talk about just operationalizing and making it continue running successfully.

Maya Prohovnik (00:36:03):
Totally.

Lenny (00:36:04):
Yeah. So on the first piece, just what did you do right to integrate Anchor into Spotify to make it effective and continue working?

Maya Prohovnik (00:36:10):
I think it's a combination of luck and hard work because Spotify is genuinely an amazing company. I mean, you've met now a bunch of people who I work with at Spotify, including my boss, Gustav. It's an incredible company. They're Swedish. So just their mindset about everything in the first place is amazing. But also, I have been so impressed that they are the type of company that can still move quickly and make really big strategic decisions and strategic shifts. It never feels like they're slowing down. And so I think our way of working worked with them. And then I think the other thing that we had to our benefit was they really saw the same vision that we had. So it was like they also wanted to change podcasting and make it more democratized and make it more two-way and bring it into the future.

Maya Prohovnik (00:36:53):
And it was so interesting because when we started talking to them, both of us had this chicken or egg marketplace problem where we had this critical mass of creators. They had a critical mass at that point of consumers, but if you don't have both on the same place, then you're still stuck with the limitations of RSS feeds. And so I think we were both coming at the acquisition with the same frustration just from two different angles. And so both of us really saw that benefit in joining up. And so I think one of the big ways we were lucky is that what I've seen happen in a lot of acquisitions is you have an idea of what you're getting acquired for and you get excited and really attached to that vision, and then when that vision doesn't end up fitting into the company strategy, there's nowhere else to go.

Maya Prohovnik (00:37:34):
And I think in a lot of ways Anchor did really well fit into Spotify's culture and their roadmap, but there were many things that changed around that initial vision. And I think we were really good at making sure that we stayed valuable to Spotify. That was one of our goals when we got acquired where we were like, we're tiny startup people, and we're like, we're not going to get lost in this big sea. When we came in, it was like we were very vocal about everything that we were doing, we did lots of internal marketing and made sure people were excited. We built a lot of really strong relationships. We made sure that every team at Spotify knew about us and what we were doing. We were constantly asking how we could help other teams. And when the strategy shifted, which it has dozens of times since we've gotten acquired almost five years ago, not like we just blindly followed, but we were always willing to get excited about whatever the next thing was and willing to be helpful and figure out how to make that work.

Maya Prohovnik (00:38:30):
And I think it actually goes back to the sticking to the mission in the first place where Spotify and we want podcasting to be able to be a huge business for the industry. We think it's been held back by a lot of things for a long time. And so we've had various hypotheses about how we can get there and we try things and if something doesn't work, we go onto the next thing. But that goal hasn't really changed.

Lenny (00:38:55):
That makes a lot of sense. And I love the idea of just staying excited about what is happening. I think a lot of founders join and they're like, "Oh, it's so annoying to work in this big company." "Oh man, we have this original plan, it's just not happening." And I think even if you're probably not, even if you're not excited, I think it's effective to communicate that you're excited and be on board and then shift things in what direction you think maybe needs to go instead.

Maya Prohovnik (00:39:19):
Totally, yeah.

Lenny (00:39:20):
Okay. And then in terms of operating within Spotify, from what I understand, your team is still very startupy and there's this really fast moving mentality. What have you learned and how do you do that? How do you make that happen within a larger company?

Maya Prohovnik (00:39:34):
We've definitely slowed down a little, I will say. I'm always joking about when we first got acquired, I remember we had to do this spreadsheet outlining our roadmap and estimate are things like small, extra large, whatever, and Spotify's definition of small with something like a quarter. And I was like, we've never built anything that took more than three months. And now it's like now we build lots of things to take more than three months. But the first thing that comes to mind, so when we were a startup, one of the first things we did when we were only a few people, we decided what our core values were going to be. And I think they maybe very trivially have changed over the years, but we essentially still have the same four core values that we decided on seven or eight years ago now. And when we got acquired, we had a conversation with our team where we said, we're going to of course embrace Spotify's culture and Spotify's core values, but we're not going to forget who we are as a team.

Maya Prohovnik (00:40:28):
And I think part of what really... And one of our core values by the way, is move fast. So that's something that's very deep within our DNA. But I think one of the things that helped with that is Daniel Eck, when we got acquired, came and talked to our team, which was so cool and so motivational. And one of the things he said to us was, we had a reputation at the time for moving very quickly, even compared to other startups. We were shipping a new feature every two weeks, it was insane. And Daniel said to us, not only do I want you to not move slower, that's part of why we're acquiring you so that you can move quickly. But he said, I also want you to help me teach the rest of Spotify how to move more quickly, and I found that so motivating.

Maya Prohovnik (00:41:04):
Because I think I definitely had that feeling going from startup to larger organization where I had this fear that it was just going to be bureaucracy and things moving so slowly. And I really loved that. That was one of his goals was that he was like, I want to make sure Spotify also grew really quickly and he was trying to figure out how to help them keep moving as quickly as they used to. And so I think that's something that I really took to heart and that I've continued to remind my team of even to this day where I think of that as part of my job here to help people think about how we can move quickly and what really matters. And I think at any large organization, there's obviously a lot more complexities, there's a lot more stakeholders.

Maya Prohovnik (00:41:42):
So to some extent it's necessary to slow down and be thoughtful. But I think the things that I always try to push people on is the unnecessary things that slow you down. So I think that's what we spend a lot of time on, both within our team and when we're collaborating with other teams at Spotify because we work with basically everyone at this point. So I think that was really cool that he gave us that mission when we joined.

Lenny (00:42:03):
On that note, is there anything that has been a real challenge or become really annoying? Just real talk about the flip side of that. Everyone's always like, "Oh, it's all working out great." Is there anything you could share that's just like, "Oh wow, that was really hard and we overcame it, or a real challenge that we didn't expect?"

Maya Prohovnik (00:42:19):
I think that the downside of Daniel's advice, so one of the things he said to us, he was literally say no to all the meetings. You're going to get invited to all these off sites and meetings and everyone's going to want to meet you guys and they're going to want you to come to all of these events and whatever. And he was like, just keep being Anchor. Just keep doing what you're doing for at least the next year. Don't worry about what Spotify's doing. And on the one hand, of course, we loved that as startup people we're like, cool, we're going to get to stay us within this larger organization. But the downside that we didn't really realize until a year later was that we weren't really able to build relationships. We had some culture problems where our team started to feel like because they weren't part of Spotify, they had some existential, they didn't feel attached to the work that we were doing.

Maya Prohovnik (00:43:03):
And so for a year we operated on our own. We moved really quickly, we were able to get a lot done, but then I think our next phase had to be really deeply incorporating into Spotify. And so we stopped calling our team Anchor internally, we started collaborating more with other teams. And I think that is the necessary trade-off is the more deeply you're embedded, the slower things are going to go. But I think that has been really amazing for making sure that our team actually felt like a part of the larger mission that Spotify was doing. And the one other thing I'll say that I found pretty striking. So, Spotify, as you know, did a lot of podcast acquisitions soon after the Anchor one. And so I got to know a lot of the other founders and early employees who have been acquired by Spotify and something that I've found with them and just with other acquired founders who I've talked to since, I don't know, I feel like people don't talk about this enough publicly.

Maya Prohovnik (00:43:59):
Maybe people are somewhere and I just haven't seen it. I think that people who get acquired, especially founders, actually go through a relatively deep depression and existential crisis after getting acquired. And I never would've thought, when you're talking to people about getting acquired, it sounds like such an obvious positive. Like you said, it's like this amazing positive exit and it was objectively so good for our team and for us and for our users, and I think for the industry. And I personally did not expect to go through that. Because I was like of course you want an exit, that's what you're working towards that whole time that you're a startup. And I've talked to a lot of these founders and I think it is a process I think that everyone has to go through because either you decide I'm going to stay here and I'm going to do this for a long time and I can make this work for me.

Maya Prohovnik (00:44:44):
Or you're like, I'm just a startup founder and this doesn't really work for me and I'm going to go do my next thing. And so I think to some extent some of the things we were talking about, I think do help shake out whether people actually want to make those investments and figure out how to make things work at a big company. But I think the other thing that I've found is just I think there isn't enough support for that transition. And I think that for me, I've definitely landed on the side of, I love working at Spotify. I now am so excited to be part of a large organization and building things at this scale, but I really would've loved to been able to talk to someone about it or understand that there were other people going through that kind of thing.

Maya Prohovnik (00:45:25):
So I don't know if you want an example of how it's not all rainbows and sunshine, I definitely think there were some dark times there and I've since learned everyone goes through that just because I think just by definition, all the reasons that you start a company, that means your personality is someone who wants to be having that direct impact and having your own ownership and being able to make things move quickly, and that is just so different once you join a large organization.

Lenny (00:45:54):
Yeah, and those are amazing examples. I think what's interesting with startup life is eventually if things work out well, you'll either end up working for a larger company, that's a likely scenario if things tip go great or you're running a public company, which is also extremely painful and stressful.

Maya Prohovnik (00:46:11):
Yes, exactly.

Lenny (00:46:12):
Yeah. So, the paths are hard no matter what you end up doing, as much as you love that startup time. I actually went through the same thing when we sold our company to Airbnb. I was just like, man, I had this life goal of starting a company and now I've done it and now what do I do? And it was just like, huh, okay, I guess I got to figure it out.

Maya Prohovnik (00:46:29):
Right? It's like, who am I? And I think the thing that I think for me, and it sounds similar to you, I think I didn't realize how much value I put in the actual day-to-day of survival that comes with being part of a startup. That becomes almost your reason for being is like, I got to make this work and I got to keep the team motivated. And you're just going, going, going, and then when everything is suddenly stable, you're like, wait, what is my job now?

Lenny (00:46:57):
I saw a tweet actually recently, I forget who tweeted this, that CEOs that exit and go on vacation end up being more stressed and less healthy than running a really high stress, high growth company.

Maya Prohovnik (00:47:08):
That is wild. I get it though.

Lenny (00:47:10):
Yeah. Although I will say when I joined Airbnb and was just the PM of our team working on one thing, it was like, this is really cool. I don't have to worry about everything all the time, there's a really nice relief to that. But yeah, there's a life existential question of just like, wow, we did the thing. What am I? What else? There's usually not a goal beyond that.

Maya Prohovnik (00:47:31):
Totally.

Lenny (00:47:32):
What was it for you? Was it that, was it the feeling of I had this thing that I was running and now I don't?

Maya Prohovnik (00:47:37):
I think it was a little bit the fear of being like a cog in a wheel, which is not actually how I feel now that I work at Spotify. And I think the other was like we were doing great, we already were killing it at podcast hosting. And also it was just so fun. I really valued that small company, everyone knows each other. We're doing really hard work, but we're also having so much fun. And I think it felt like I couldn't translate that to a large organization where I was like, okay, now I have to do things how they do. And then I think what actually ended up happening is I actually love how Spotify runs their company and I'm still able to run my team the way that works for me. And so I think it just goes back to knowing what you care about, being really solidly attached to your own core values and being able to take that with you.

Lenny (00:48:25):
I think we're both examples of people that were startup people and then realized it's not so bad working at a big company. I stayed at Airbnb for seven years. I was like, no, no way, I'm going to be here for more than a year and a half or a year or two. How long have you been at Spotify? At this point?

Maya Prohovnik (00:48:37):
I'm going on five years. Yeah.

Lenny (00:48:41):
No, I think this is just a example of it's you think you're not going to enjoy working at a larger company, but oftentimes it's actually pretty great for a lot of different reasons.

Maya Prohovnik (00:48:48):
Yes.

Lenny (00:48:49):
Shifting in a slightly different direction, just thinking about leadership and what you've learned to lead teams, lead large orgs, build products, is there any just, I don't know, frameworks or tools that you found to be effective?

Maya Prohovnik (00:49:05):
The big one for me is Radical Candor. And I know my team watching this is going to laugh at me because I talk about this every day. They're tired of hearing it, but have you read it?

Lenny (00:49:15):
I have. I love it.

Maya Prohovnik (00:49:17):
Yeah. It's my all time favorite book. And I think it really shifted for me, honestly how I relate to people in general. But I think especially with managing, giving feedback, being able to collaborate and push back in a direct way, direct and constructive way on peers and that sort of thing. So I make all of my managers on my team read it. We talk about it constantly in our team, and I think that the general concepts for anyone who's not familiar is you need to care personally and challenge directly. And if you're only doing one of those things, you're not giving feedback in an effective way. And the book just talks so much about the importance of feedback and how feedback is a gift, which I have now come to completely agree with. It's like anytime I've given someone effective feedback, it's always well received, even if it's tough to hear, people want to get better and they want to know how they can improve.

Maya Prohovnik (00:50:07):
And so I think anytime that you can give them specific feedback in a way that makes it clear that you care about them and want them to be able to reach their goals, I think it makes them stronger, it makes your relationship stronger. And I also think the one other big thing I took away from Radical Candor was when it comes to people not underperforming, it really reframed how I think about that because people are not generally inherently bad or lazy or ineffective, it's almost always because the role they're in is the wrong fit. And so being able to approach the conversation in that way means that you can come at it and in a caring way that lets them know you actually want them to be successful.

Maya Prohovnik (00:50:47):
And what I found is when you have the conversation in that way, they're much more receptive to it. And then you're able to either actually resolve the issues or you're able to help them figure out what the right fit is for them, which I think as a manager, it's so inspiring to me because that means that you get to keep mentoring them beyond. You're not just saying, this isn't working, I'm giving up on you, see you later. You're saying, I'm committed to helping you throughout your whole career and let's help you find the next step, even if that isn't on my team or at this company.

Lenny (00:51:16):
Awesome. Yeah, I love that book. And you talked about the two. There's this grid that-

Maya Prohovnik (00:51:21):
The quadrants?

Lenny (00:51:22):
Yeah, it talks about. And just to reinforce what you just said, the core is that when you want to give people direct feedback, but you want to make it clear you care deeply about them. And I love that she talks about if you do one of these wrong, here's what happens. If you challenge directly, but it doesn't feel like you care deeply, you're just an asshole and they're just like, yeah, God, you get really defensive. I should get her on this podcast. How cool would that be?

Maya Prohovnik (00:51:43):
Oh my God, that would be my, she's my... If I could meet one tech celebrity, it would be her.

Lenny (00:51:48):
Okay. I'm going to work on it. If you're listening and you're Kim Scott, let me know, I will try to get to her. Anything else in that bucket of frameworks or tools, things that you find really helpful leadership?

Maya Prohovnik (00:51:58):
The only other one, I'm not a huge framework person. I think this goes back to my gut thing, but the one other thing that I refer to often is I love the Eisenhower Matrix, which is also known as the four Ds. So it's do, defer, delegate, delete, you have also quadrants. Maybe my brain just works in quadrants. I don't know. But I totally subscribe to that and that's how I do everything, where I write everything down at the end of every day, I go through and I either do delegate, defer, delete, and it really helps you clear a lot of stuff out of your brain.

Lenny (00:52:27):
Interesting. So you don't even use it as a grid necessarily, it's more make a decision on all the things on your plate?

Maya Prohovnik (00:52:34):
Yeah, I do. I just tried using the grid view and it didn't work for me for some reason. So I just use a to-do list, and then I don't let myself finish working until I've gone through anything I didn't get through that day, and then I know what I have to do the next day.

Lenny (00:52:46):
So that touches on another area I wanted to touch on, which is productivity. I hear you're very good at being productive and making the use of your time. I guess one, where do you think that comes from? And then two, just any other tips, tactics, tools you find to be really effective in staying productive?

Maya Prohovnik (00:53:01):
Yeah, where does that come from? I think I am OCD. I think I'm an overachiever. I don't know, it's really important to me. I think when my team says that I'm very productive, the feedback I hear from them is they're impressed that they send me a doc and then I always read it. I think that's more about prioritizing my team and making sure that they're unblocked, which I take very seriously. I don't know other tips that I would give people. I write everything down because I think I'm one of those people I remember things best when they're written down and then I obsessively put things on my to-do list. Anything that anyone asks me to do goes on there, and then I have that method for organizing it later in the day.

Lenny (00:53:38):
Do you have an app for this or do you write it on paper?

Maya Prohovnik (00:53:40):
I use Todoist. I think you can use any, but it's the one that works best for me. I love using paper, but then if I don't have it with me, then I can't remember anything I have to do, so I've had to go digital.

Lenny (00:53:51):
Awesome. So it sounds like a big part of your process is just getting things out of your head and writing it down somewhere.

Maya Prohovnik (00:53:56):
Yes. I think that's huge. And I also think if you're in any sort of job, I think most PMs have this where it's so much of your job is actually deep thinking and problem solving. I just cannot get that done if I'm running through my to-do list in my head. So I think that was a big unlock for me when I realized that I just needed to, anytime I'm stressed, honestly, if I just sit and make a list of all the things I have to do, I'm like, oh, it's four things, I can get those done, it's okay.

Lenny (00:54:18):
Man, that tool of just making a list when you're stressed about, all the things you got to do, just making a list of it on paper, I find it so helpful.

Maya Prohovnik (00:54:27):
It works every time.

Lenny (00:54:28):
Have you read Getting Things Done by David Allen?

Maya Prohovnik (00:54:31):
It's on my list. I haven't read it.

Lenny (00:54:32):
Okay. That book totally transformed how I think about productivity, and you already doing a lot of what he recommends. It's like this very old book. And now he's just, I don't know, he's a public speaker dude that just goes around consulting. But this one, it has very simple approaches to being productive and it really changed the way I operate. And you're already doing a lot of it, so I don't know how much value you get out of it.

Maya Prohovnik (00:54:53):
I'll read it. I love this stuff.

Lenny (00:54:55):
A core concept is this idea of mind like water where you don't want to have anything in your head, you want to get it all out. And then there's these systems for how to process all the things you're getting out.

Maya Prohovnik (00:55:04):
Totally.

Lenny (00:55:05):
Maybe we'll get David Allen this. We got a whole list.

Maya Prohovnik (00:55:07):
I know we have a whole hit list.

Lenny (00:55:10):
Maybe it's just a final question. You're good at so many things, another thing you're really good at is public speaking. I was watching the last Spotify launch event and I was just like, holy moly, she's incredibly good at speaking and it's something I want to get better at and something I think a 100% of people want to get better at. So, I'm just curious, what have you learned about being an effective public speaker? Anything that you could recommend to people if they're trying to get better at this?

Maya Prohovnik (00:55:32):
Well, first of all, thank you for saying I'm awesome at so many things. This is my favorite podcast I've ever been on, you're just complimenting me the whole time, so I'll take it.

Lenny (00:55:39):
True.

Maya Prohovnik (00:55:41):
I think with public speaking, for me, the first thing that I had to do was decide that I didn't hate public speaking because I think it's human nature. It makes sense that we do not want to be in front of a crowd and we don't want to be performing. And it's just an unnatural thing that humans, I think make ourselves do. I remember actually when I was in high school, I had to give a presentation and I had so much anxiety I couldn't sleep the night before. And I remember I was getting ready for school that morning and I was like, I'm just not going to hate public speaking. I just can't get through my life feeling this way. And so I just got up there and I had fun with it, and it felt so much better to not feel worried about it.

Maya Prohovnik (00:56:18):
So I think ever since then I've been okay at it. And then I have gotten lots of opportunities to do big scary public speaking things for Spotify, and so I think I've had to get even better. I think my tips would be my biggest one is probably reframing. Everyone has this anxiety before they have to perform or they go on stage. Reframing that anxiety to understand that the thing your body is doing is surging you with adrenaline to help you. And so letting that feeling wash over you instead of fighting it, I think has been so effective for me because otherwise, it can feel like a panic attack. And so I think you have to be like, cool, my body's getting ready. We're excited, we're going to go do this on stage. That has been really helpful. I practice a million times anytime I have to do public speaking.

Maya Prohovnik (00:57:03):
So I think everybody has different memorization tactics, different ways of doing speaker notes that work for them. And so I think part of it is you have to do a bunch of public speaking to see what works for you. So some people work best with no notes. I almost read complete sentences a good, I can enunciate things while I'm reading, so that works best for me. Some people like bullets and then they go a little bit off the script. But I think once you figure out what method of speaker notes works for you, I rehearse probably at least 10 times all the way through once the speaker notes are final. And you can practice your exact delivery. You can practice where you're going to put jokes in. You can figure out what doesn't feel natural or where you're going to trip it up, and then you can change the words that you're using.

Maya Prohovnik (00:57:42):
And so I like to get to the point where I can remember ad-lib at least half of the notes that I have in there, and that way I know I'm going to feel confident coming off script. I make a lot of eye contact with the audience, which I think makes them think that I'm not reading speaker notes. So I think that's really important. If you can stand it, which I can't, record yourself or watch yourself in a mirror, it messes me up more. But I think for a lot of people, that can be really helpful to figure out where your issues are. I think the biggest thing for me honestly, is that the unfair advantage I have is if you really give a shit about what you're talking about, you are going to be such a better presenter because people are going to be able to tell that you care.

Maya Prohovnik (00:58:20):
And so I think even at a larger Spotify event where it's like I'm reading off a teleprompter and I'm reading, I'm marketing, but I'm helping write those words and then the way that I'm saying them matters because I'm talking to podcasters and I'm like, my mission in life is to make things better for you, not everyone gets that benefit, I guess. Sometimes you have to do public speaking about things that you're not very passionate about, but I certainly think that helps. And I think leaning into that, so when you can, telling personal stories, letting the audience get to know you, I like to work some humor into my presentations. I think that can really help as well.

Lenny (00:58:55):
That is awesome advice. I especially love letting the stress wash over you, because most of has this challenge. Your body's just doing all this shit that's just going to stress the shit out of you. And so the idea of just embracing it, just flowing with it.

Maya Prohovnik (00:59:10):
Yes, it's a superpower. It's like, that's so cool, that adrenaline works that way.

Lenny (00:59:14):
Yeah. Okay. I'm going to try that one.

Maya Prohovnik (00:59:16):
Also, if you're nervous, you can put your hands above your head that'll help the blood, I don't know, it helps it go into your head or something. I don't remember.

Lenny (00:59:23):
There's this whole power post thing that apparently has-

Maya Prohovnik (00:59:26):
Yes, exactly.

Lenny (00:59:26):
I think it's been disproven. People are like, no, there's no data that shows that. But the blood thing that's really interesting versus psychological benefits.

Maya Prohovnik (00:59:34):
I think there is a real physiological thing that happens.

Lenny (00:59:36):
That's cool. Okay. Amazing. Okay. Maybe as an actual last question, what's happening in the future of the Spotify podcasting platform? Anything you want to share about where things are going?

Maya Prohovnik (00:59:45):
A lot of the things that I talked about at Stream on for anyone who saw that this year, I think are still very much our strategy. So I think for us in general, Spotify is really focused on making sure that we can... We have a massive audience, we have more than 500 million monthly active listeners. We want to help podcast creators reach that global audience, and so it's really important to us. I always tell my team the biggest problem that I want to solve for podcasters is discovery and audience growth, and I really think we can be the ones to do it, so I'm really excited about that. So discovery, monetization. We're really focused on making sure that creators of all shapes and sizes can make a living off of their work.

Maya Prohovnik (01:00:24):
And then I think in general, we're working on so many cool things at Spotify to make podcasts a more interactive format, something that allows you to get to know your audience and connect with your fan base. We talked about a couple features this past year. I definitely can't say anything specific, but what I can say is there is lots of really cool stuff coming next year that I'm very excited about. And I would say for anyone who wants to learn more, definitely sign up for Spotify for podcasters. It works whether you're hosted with Spotify or not, and you can start to get a sense of some of those features that we're opening up to everybody, but there's lots more cool stuff to come.

Lenny (01:00:58):
Amazing, mysterious, and exciting. With that, we've reached our very exciting lightning round. Are you ready?

Maya Prohovnik (01:01:05):
Yes.

Lenny (01:01:06):
What are two or three books that you recommend most to other people?

Maya Prohovnik (01:01:09):
Children of Time, and I guess I would say It by Stephen King. I recommend a lot of Stephen King books, but that's my all time favorite.

Lenny (01:01:16):
Very on brand with your podcasts. Makes sense. What is a recent movie or TV show that you've really enjoyed?

Maya Prohovnik (01:01:23):
TV show, I'll just say, I guess Pokerface was the last one that really blew my mind. Movies, I mean, Barbie was so good, and then I'll just give you a lesser known one. I just watched this crazy movie from the '80s that was made the same year Home Alone was, this just got featured on a podcast, so I think everybody's talking about it now, but it's a horror movie about a kid who's home alone, and then he has to fight Santa Claus in a home invasion situation. It is so good, it has a bunch of different names, but if you look up either Game Over or it's like Code Père Noël or something, it's an old French horror movie, so good.

Lenny (01:01:59):
Interesting that the other Home Alone is the one that did well in this one.

Maya Prohovnik (01:02:02):
Well, there was apparently a whole legal thing over it.

Lenny (01:02:05):
Oh, wow. They didn't have Macaulay Culkin. That's their missing piece. What is a favorite interview question that you'd like to ask candidates when you're interviewing?

Maya Prohovnik (01:02:14):
I have one. It is, if you could make a podcast about anything, what would it be? And it is the best. Honestly, you should ask people that even if you don't work in work in podcasting, because it tells you so much about candidates, and one thing that I feel very strongly is that the most important thing is that you're hiring passionate people, not people who are passionate necessarily about the thing that you're doing, but about anything. If they can't think of anything, that's a red flag for me.

Lenny (01:02:33):
That's awesome. It's like a variation of the question of Teach me something or tell me about something that you've learned recently. Really interesting tweak on that question and very appropriate. What is a favorite product or something awesome you've discovered recently that you really like digital or physical?

Maya Prohovnik (01:02:49):
Okay. Very unsexy answer, but I love 1-800-CONTACTS.

Lenny (01:02:53):
Okay.

Maya Prohovnik (01:02:54):
I'm so impressed with their product team. If you need new contacts, even if you need a new prescription, you can do the whole thing online in five minutes, and it's so well-thought-out and so thoughtful. I love them. And then the one other one I'll give a shout-out to, since becoming a parent, Love Every, do you subscribe to them?

Lenny (01:03:09):
Absolutely. I don't know anyone that doesn't have them.

Maya Prohovnik (01:03:12):
I know. It's so good.

Lenny (01:03:12):
They've cracked it.

Maya Prohovnik (01:03:14):
Yes.

Lenny (01:03:15):
Yeah. We are missing some of the toys, and so we're trying to find where they went because he's ready for the rattle.

Maya Prohovnik (01:03:25):
Yes. Awesome.

Lenny (01:03:25):
Yeah. I love everybody's amazing and their ads are really great. Oh, man.

Maya Prohovnik (01:03:27):
Yes. They're so good.

Lenny (01:03:29):
What is a favorite life motto that you come back to often share with folks? Anything there?

Maya Prohovnik (01:03:36):
"Only a fool wishes time away." Even if you're having a bad day, even if you're doing something boring or you're stressed, you have to do public speaking, that's still your life and you should enjoy it.

Lenny (01:03:47):
I love that. There's this phrase of just like, I'm just killing time right now, and I always think about that, just like, oh, but you don't have that much time. Maybe you shouldn't try to kill yourself.

Maya Prohovnik (01:03:57):
Yeah.

Lenny (01:03:58):
Even though sometimes things are boring, it reminds me of another quote of just, "Most of the world's problems are caused by our inability to sit in a room for 10 minutes quietly."

Maya Prohovnik (01:04:07):
Yes. Also, if you're bored, have a baby because you'll never be bored again.

Lenny (01:04:11):
Yeah. Yep, indeed. Speaking of parenting, what is a valuable lesson that your mom or your dad taught you?

Maya Prohovnik (01:04:18):
My mom always told me that my generosity would be rewarded, so anytime that I was nice or thought of someone else before me, she always made sure that I got some little reward or got to go out for ice cream or something, I think that really worked on me.

Lenny (01:04:34):
I love that. Final question, I saw somewhere that you raised bait backyard chickens. Is that true?

Maya Prohovnik (01:04:40):
I'm so happy you asked about my chickens'.

Lenny (01:04:43):
I love that reaction. So maybe just why did you decide to do that and any tips for someone that may want to explore it?

Maya Prohovnik (01:04:48):
Oh my God. Well, we should have started with this because I can talk about this for an hour and a half, but I love my chickens. I have eight of them, we've got one rooster and seven hens. I think that all of us should be a little bit closer to nature, to the, I was going to say, the food that we're eating, I'm not going to eat my chickens, but they make eggs for me. But I just think there is something very lacking in our modern lives, that connection to nature. When I feel stressed at work and I go outside and I hang out with my chickens, I pet them, and I give them treats and we talk to each other. It's like nothing makes me happier and feel more grounded than hanging out with my chickens. So I think everyone should have chickens. I would say they're pretty low maintenance, so if you're thinking about it, I would recommend it. And if you get chickens, my favorite thing that I did for them, I got this monthly subscription box for chickens I think it's called Coop Crate.

Lenny (01:05:40):
Love Every for Chickens.

Maya Prohovnik (01:05:41):
Yes, it's Love Every for Chickens and every month they send me chicken treats, but also fun little things for crazy chicken people, so it's clothes or a sticker, something funny.I'm very into the whole chicken thing, so, yeah.

Lenny (01:05:55):
Oh my God. Maybe just a tactical question, how much space do you need in your yard for chickens?

Maya Prohovnik (01:06:00):
Not that much, so we let them free-range. We have a pretty big yard, but I think their actual, so there's their little coop, and then they've got a run that's fenced in. The run is maybe like, I don't know, five feet by eight feet or something, but you can go a lot smaller. If you go to Home Depot, they actually sell pre-made coops and runs. I think if you have a decent sized backyard, they'll be fine. I've known people with pretty small yards, and you just let your chickens out and they're happy and they'll find worms in a few yards.

Lenny (01:06:27):
Oh man. All right. A new project to look into.

Maya Prohovnik (01:06:29):
Please get chickens, do it.

Lenny (01:06:31):
Okay. Maya, we've talked about chickens, dogfooding, gut level decisions, Radical Candor, so many things. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out, and how can listeners be useful to you?

Maya Prohovnik (01:06:43):
I'm on threads, I guess, and I'm on LinkedIn. I'm Maya Fish on most social media, and then I'm on LinkedIn, and then, what was the second one? How can people be useful to me?

Lenny (01:06:53):
Exactly.

Maya Prohovnik (01:06:55):
Listen to your podcast on Spotify, and then send me your feedback. I would love to know either as a podcast creator or as a podcast listener. Always happy to hear what Spotify can be doing more of or better to help you out.

Lenny (01:07:06):
Amazing. Maya, thank you so much for being here.

Maya Prohovnik (01:07:08):
Thank you so much.

Lenny (01:07:09):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

