---
guest: Alex Hardimen
title: An inside look at how the New York Times builds product | Alex Hardiman (CPO,
  the New York Times)
youtube_url: https://www.youtube.com/watch?v=y3-cwoHMwQs
video_id: y3-cwoHMwQs
description: 'Alex Hardiman is Chief Product Officer at the New York Times, where
  she oversees the company’s news, cooking, games, audio and advertising products.
  Previously, Alex was Chief Product Officer...

  '
duration_seconds: 4041.0
duration: '1:07:21'
view_count: 6759
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- metrics
- kpis
- roadmap
- prioritization
- iteration
- experimentation
- funnel
- conversion
- monetization
- subscription
- revenue
- culture
- leadership
---

# An inside look at how the New York Times builds product | Alex Hardiman (CPO, the New York Times)

## Transcript

Alex Hardiman (00:00:00):
One thing that's really interesting is that our impact and our business goals are in service of our mission, which is to seek the truth and help people understand the world, not the other way around. What it means is that the way that we think about impact is growing a giant subscription business. That business exists to strengthen an informed democracy at a time when people are struggling to understand basic facts and struggling to understand each other. That means that impact for us is growing subscribers, but it's also when a deeply reported story triggers an important policy change or a new law.

Alex Hardiman (00:00:40):
When you're a product manager, you're involved again in driving specific metrics like engagement or subscribers, but you're also trying to help stories find their real audience in ways that trigger just this whole different side of mission and purpose driven impact. I didn't feel that when I was at a place like Facebook.

Lenny (00:01:00):
Welcome to Lenny's Podcast. I'm Lenny and my goal here is to help you get better at the craft of building and growing products. Today, my guest is Alex Hardiman. Alex is Chief Product Officer at the New York Times where she leads teams that build the company's news, cooking, games, audio, and advertising products. Prior to this role, she was Chief Product Officer at The Atlantic, and before that, she spent two years at Facebook where she led their news product amongst other things. As you'll hear in our conversation, Alex has been at the center of the storm so many times, including at Facebook right after the 2016 election.

Lenny (00:01:33):
Then, at the New York Times right as COVID hit. She hears so many stories and insights about how the New York Times builds product, what it's like for product teams to work with journalists, what's good and bad about working at a company like the New York Times versus FAANG tech type company, and also how they went about acquiring and integrating world. I had such a blast doing this interview and I hope that you enjoy it as much as I did. With that, I bring you Alex Hardiman. Today's episode is brought to you by Miro. Creating a product, especially one that your users can't live without is damn hard, but it's made easier by working closely with your colleagues to capture ideas, get feedback, and being able to iterate quickly.

Lenny (00:02:19):
That's where Miro comes in. Miro is an online visual whiteboard that's designed specifically for teams like yours. I actually use Miro to come up with a plan for this very ad. With Miro, you can build out your product strategy by brainstorming with sticky notes, comments, slide reactions, voting tools, even a timer to keep your team on track. You can also bring your whole distributed team together around wire frames where anyone can draw their own ideas with pen tool or put their own images or mockups right into the Miro board. With one of Miro's ready made templates, you can go from discovery and research, to product roadmaps, to customer journey flows, to final mocks.

Lenny (00:02:57):
Want to see how I use Miro? Head on over to my Miro board at miro.com/lenny to see my most popular podcast episodes, my favorite Miro templates. You can also leave feedback on this podcast episode and more. That's M-I-R-O.com/lenny. This episode is brought to you by Athletic Greens. I've been hearing about AG1 on basically every podcast that I listened to, like Tim Ferriss and Lex Fridman. I finally gave it a shot earlier this year and it has quickly become a core part of my morning routine, especially on days that I need to go deep on writing or record a podcast like this. Here's three things that I love about AG1. One, with a small scoop that dissolves in water, you are absorbing 75 vitamins, minerals, probiotics, and adaptogens.

Lenny (00:03:48):
I like to think of it as a little safety net for my nutrition in case I've missed something in my diet. Two, they treat AG1 like a software product. Apparently, they're on their 52nd iteration and they're constantly evolving it based on the latest science, research studies, and internal testing that they do. Three, it's just one easy thing that I can do every single day to take care of myself. Right now, it's time to reclaim your health and arm your immune system with convenient daily nutrition. It's just one scoop and a cup of water every day, and that's it. There's no need for a million different pills and supplements to look out for your health.

Lenny (00:04:25):
To make it easy, Athletic Greens is going to give you a free one-year supply of immune supporting Vitamin D and five free travel packs with your first purchase. All you have to do is visit athleticgreens.com/lenny. Again, that's athleticgreens.com/lenny. Take ownership over your health and pick up the ultimate daily nutritional insurance. Alex, thank you for being here. Welcome to the podcast.

Alex Hardiman (00:04:52):
Thanks so much, Lenny. It's really awesome to be here with you.

Lenny (00:04:55):
What's interesting is I think you may be the first product leader on this podcast who doesn't work at a big tech FAANG startup, and so I'm really excited to just dig into see what it's like to build product at a company like the New York Times.

Alex Hardiman (00:05:08):
Thank you. No, no, that sounds awesome. Let's dive right in.

Lenny (00:05:12):
Okay, before we dive in, I'd love to get a little bit of background on just your career. I'm curious, what was your career path to becoming the chief product officer at the New York Times?

Alex Hardiman (00:05:23):
Thanks for asking. I've definitely spent most of my career right at the intersection of journalism and tech. I think in hindsight, if you were to ask my family, they probably wouldn't be that surprised, even though for me I was just rolling with it and following what felt like a really interesting set of problems to solve. But when I just look at my family, there is a ton of journalism in our DNA. My grandfather was a news anchor on the West Coast and I really revered him. My great-grandmother, she was pretty amazing. She actually started one of the first TV stations in the Midwest back in the '50s when it was still pioneering territory.

Alex Hardiman (00:06:01):
For me, one of my first, the dream for me was to try to find a way to build things in the new space. That's how I first ended up at The New York Times. I've had two stints at The New York Times. My first stint was for a decade, from 2000 to 2016, and it was during a really interesting time of pretty big transformation. There's so much to talk about within that decade, but I would say there are two really big things that happened in that moment. The first was really trying to work with the company to shift from being a print first product into a mobile first product. If you go back to 2006 and you think about it, the Times had no mobile presence whatsoever.

Alex Hardiman (00:06:40):
Even the iPhone 2G and the App Store didn't come out I think until like 2008. We just really started investing in small mobile use cases, first on the margins and then more and more aggressively until we were just leading with mobile in everything that we did. New journalism formats, new product features, new revenue opportunities, that type of thing. Then, the second big thing that marked my journey at The New York Times was the shift to a direct to consumer subscription model. This was back in 2011, and there was just a lot of skepticism, including from people at The New York Times, about whether or not people would pay for quality journalism.

Alex Hardiman (00:07:17):
We brought in consultants and they said, "Maybe over the course of history it'll get to one million subscribers, if you're lucky." It felt like a really big nervous [inaudible 00:07:27] at the time. But thank goodness it helped make a market for paid journalism, that has really helped a lot of news organizations find new ways to support quality coverage. But after a decade I did what I think a lot of people did, was you look around and you say, "I love what I do, but I would love to go learn how to do product in the context of a product led digital first company." That's when I went to Facebook and I left in 2016.

Alex Hardiman (00:07:52):
The timing is actually pretty important in terms of my experience at Facebook, because when I first joined Facebook, I totally left the media space. I was focused on building out a team that was really trying to help micro sellers in markets like India and other parts of APAC, who were coming online for the first time in really low bandwidth areas, and just wanted to sell their goods through social commerce. Really looking at what WhatsApp and Line and other regional competitors were doing. We were focused on business messaging and the interoperability of the Facebook apps from more of a small business perspective. It was really awesome work.

Alex Hardiman (00:08:28):
Then, the 2016 presidential election happened. I had only been there for a couple of months and as has been discussed very widely and reported widely, it was a wild time where there was just so much reckoning around misinformation, disinformation, election integrity, platform responsibility. I went over very quickly to help out on the news front where I led the product and engineering teams and it was really hard, really interesting work. I did that for a couple of years, decided-

Lenny (00:08:58):
Before we move on.

Alex Hardiman (00:09:00):
Yeah.

Lenny (00:09:00):
I'm curious. Okay. Wait, you were leading the news product at Facebook during the election?

Alex Hardiman (00:09:03):
Right after the election.

Lenny (00:09:05):
Right after the election, after everyone was coming after Facebook trying to tear it down?

Alex Hardiman (00:09:09):
Yeah.

Lenny (00:09:09):
Wow. What year was that?

Alex Hardiman (00:09:13):
I joined in early 2017 on that effort. The election was November, 2016.

Lenny (00:09:19):
Oh, my God. Before you move on, just what was that like? I don't know how one can describe that experience, but what do you think about when you think back to that time?

Alex Hardiman (00:09:28):
I think about wartime product management, right? You're coming in, and I think there was ... What I appreciated about that time inside of Facebook was that there was just this incredible humility that was needed to really understand and first diagnose what was actually happening on the platform, and the approach to content on Facebook historically it was very binary. You basically had content from friends and family and then you had public contents. Public content could come from anywhere. It could come from a reputable news organization or it could come from my younger brother posting something and declaring it to be true.

Alex Hardiman (00:10:06):
What we really tried to do very quickly was try to unpack the categories of public content to say that there actually is something that is factually accurate information, and that requires a certain craft from the journalistic trade. There are ways to really look at what is trusted information, how you make that a little bit more essential and visible to people on the platform, while then reducing things that are at best dubious or at worse truly misleading propaganda. It was really fascinating and really hard just because the platform hadn't been built to think about classification of coverage in that way.

Alex Hardiman (00:10:44):
Let alone to have the right goals and responsibilities and incentives. There was just a ton of work to figure out how to make the platform far safer and far more informative after, I would say, a pretty intense election cycle.

Lenny (00:10:58):
Yeah. I was going to ask you about this later, but I feel like you're drawn towards just crazy, wild and crazy center of the storm roles. I guess that one you didn't expect necessarily to become that. I imagine The New York Times has a lot of that, but maybe a quick question there. What have you learned about just living in a world of just constant chaos and stress and urgency, endless urgency?

Alex Hardiman (00:11:21):
I would say, if you did ask my family and my husband, he would say that I'm always attracted to the more chaotic problems. I just actually think that that's where product people thrive. The idea of being able to take all of these crazy inputs, trying to create a very structured model to figure out, "Okay, what is true? Where do we have conviction? Where do we have questions? What are the most important problems to solve? How do you prioritize? How do you get a team rallied around a shared context in one single goal? These are actually the conditions where product manager, I think, thrive.

Alex Hardiman (00:11:55):
For me, just having been in the journalism space for about two decades now, it's just been or the tech space around news, it's just been a constant set of upheaval and transformation. Some things within our control, some things entirely outside of our control, and so I love it. For me, there's nothing else I'd rather be doing than trying to solve these problems in the world at scale. But it does take a certain amount of just grit and resilience, and the ability to really focus on the most important problems in a given moment. Also, the ability to let other things slide when you have to.

Alex Hardiman (00:12:32):
But again, I feel like these are core product skills that we look for in terms of leadership and grit, and the ability to drive through really, really tough problems that there's no playbook for, nobody has ever really done before.

Lenny (00:12:43):
Yeah. You said PMs thrive in this. I think some do. Some are like, "No, leave me out of that."

Alex Hardiman (00:12:48):
I guess that's true.

Lenny (00:12:50):
There's a metaphor I like to use when I give PM's advice on where to work within a company, which is there's like the Eye of Sauron, which is the number one most important thing to the CEO at that time. My advice is often don't avoid that thing, usually, but work maybe to the side of that because you don't want to work on something that doesn't matter, that's like over in the shire land. You want to be something that matters but not maybe the most important thing. I feel like you're the opposite. You're like, "Where's the Eye of Sauron focused? I'm going to go there and build stuff." That's pretty awesome.

Alex Hardiman (00:13:20):
Awesome, sometimes, I'm sure there are moments too where it would be nice to chill, but I am drawn to those types of problems for sure. This feels like therapy, Lenny. I'm into it.

Lenny (00:13:31):
Tell me about your mother.

Alex Hardiman (00:13:34):
She's wonderful.

Lenny (00:13:37):
Okay, great. That's the end of that one. I'll let you finish your career overview and then-

Alex Hardiman (00:13:42):
I feel like we're almost at present, which is I found that there was so much incredible experience that I was able to soak up and lean at a place like Facebook. For me, I really wanted to figure out how to apply that back into organizations that just had more of a classic journalistic mission and purpose, so I went to the Atlantic for a year. They had just been purchased by the Emerson Collective, so it was a really fun moment of just investment and expansion and ambition. We launched their consumer business. Then, I came back to The New York Times in late 2019, right before the pandemic, and I've been there ever since.

Lenny (00:14:19):
Oh my, just your timing is impeccable every time.

Alex Hardiman (00:14:22):
It really is.

Lenny (00:14:24):
I was doing some research on you before this chat and when you came back to The New York Times, there's all these stories about how big of a deal it was. Returns to The New York Times. That must have been something coming back, because you're there for 10 years initially, and then you came back. What was that experience like just coming back to something like that after being away?

Alex Hardiman (00:14:43):
I felt really lucky. When I left The New York Times back in 2016, it was on really, really good terms. It almost felt as like, I'm going on an externship and I really hope that one day I'll be able to come back and just do my job better. Because I do think there's real value in being able to do product in a bunch of different contexts. You're just so much better at pattern recognition, learning how to solve a diversity of problems, learning to work through things. I had a lot of great support when I left, which was really important. I don't think everyone necessarily has the privilege of that support when they exit a company. When I came back, it was just a real moment of excitement. My interview process, I joked with my boss at the time. But it did actually feel more like therapy.

Alex Hardiman (00:15:30):
When you've worked with people for a decade before and you go in, the conversation isn't the normal list of interview questions. It's like, "Okay, here's what type of leader you were a couple of years ago. Here are the conditions on the ground now, how do you feel about X? How do you feel about Y? Are you still passionate about solving this? What else have you learned that's going to make you better?" It was wonderful. It was one of the best interview processes because you're talking to a bunch of people who knew what you were like when you were leading as a person at a different point in your career and they're pushing you to be better. I felt like I got the best chance of a lifetime to come back and try to do my job better than I had been able to do it before, and that's pretty cool.

Lenny (00:16:12):
You've been there three years at this point?

Alex Hardiman (00:16:14):
Yeah, three years on Halloween, so coming up very soon.

Lenny (00:16:18):
Oh, wow. That's three days from now when we're recording. I wonder when this comes out. I'm curious, at a company like New York Times, which is, I imagine people think when they think product, they think it's the newspaper. At Airbnb we have this challenge where when we talk to hosts, "Here's the product." You're like, "What is your product? Is it our homes?" You have to help people understand, "Okay, when we talk product, we mean the website and app." What do you think of the product at The New York Times? Then, is it a challenge to help people understand, here's what the product team does?

Alex Hardiman (00:16:46):
It's a really good question. At the most basic level, I would say that our product is our journalism, which we then marry with a really compelling and useful user experience, in a way that helps people really act on our journalism so that they can understand and engage with the world around them. For about 150 years, our product was pretty simple. It was a printed newspaper, which is still very beloved today, but the UX of the newspaper was, it was a predictable structure. It was a very finite amount of news. It was time bound, which I think is a really lovely thing in terms of setting expectation. It also has the packaging of the newspaper just such serendipity, where you can move across news, opinion, culture, games.

Alex Hardiman (00:17:31):
It's a really great bounded product in and of itself. But about 25 years ago, when we started shifting over to digital, the web, and mobile, the world just fully opened up in a way. We just saw this really tremendous disaggregation and distribution of our journalism. We really tried to meet the moment by building a wide array of products in the news space to extend our reach. Our products then, our digital products were our website, our apps, newsletters, we dabbled with a lot in the VR/AR space early on. That was, I would say, the first big extension of our products. When we then pivoted though to a subscription model, it was a really interesting moment where we actually had to take more of a destination first approach.

Alex Hardiman (00:18:15):
It was almost like the beginning of us rebundling all of what we did, but on our own destination again, in digital destination. Because in order to build a really thriving subscription business, you really need a direct relationship with your customer as opposed to just relying on platforms to really distribute your coverage. That's where, again, we really started rebundling the breadth and depth of value that people once found in the Sunday newspaper at digital scale. Now, today, our product bundle includes even so much more than news, which I hope we'll talk about a little bit more later. We've really scaled our products in a bunch of different categories where we feel like we can really help people understand and engage with the world.

Alex Hardiman (00:18:57):
We have cooking, we have games, we have sports, we have Wirecutter, which is a great innovation surface. We're playing with a new audio app all around audio journalism. We have now six fully fledged different product destinations. The next thing for us to do is to really figure out how to put those together into a bundle that really becomes the essential subscription for any curious English speaking person around the world, who really wants to know what's happening and wants to be able to, again, act and engage and make great decisions based on the products that we build.

Lenny (00:19:36):
Got it. It sounds like the strategy is a subscription bundle where you just keep bundling awesome stuff into this bundle. It's an obvious thing everyone has, whether you want cooking or games or The New York Times online.

Alex Hardiman (00:19:48):
I think that's right. We did this pretty great exercise and strategy projects over the last year. We took a look and we said, "What is the largest addressable market where The New York Times can be truly valuable every single day to a group of people?" What we found was that there are about 135 million people around the world we believe are willing to pay for the type of high quality journalism based products that the New York Times produces, in the categories of news, gameplay, cooking and recipes, sports, which is why we acquired the athletic shopping recommendations and audio. In order for us to really capture as much of that audience and really serve them well, there are really three things that we need to do to make that essential subscription work.

Alex Hardiman (00:20:37):
The first is we absolutely need to have the best news destination in the world. When you think about the New York Times, we actually have the solar system metaphor where for us news is the sun in the sense that it's why we exist. It is what gives us our brand heritage and reputation. It's what instills trust. It's also where we just have the largest audience when you think about a funnel for our portfolio, and it's also where we just have the most amount of high quality coverage. But then that sun helps you give birth to other satellite planets or products that have a lot of the same DNA. Again, like great trusted journalism, great journalists who just have real expertise.

Alex Hardiman (00:21:16):
A great product experience that allows you to really unlock that value distribution reach, and the other ingredients that you would need for successful products to work. We're really focused on building out beyond news products that really help people engage with their passions and life needs that go beyond news. Then, the third thing is what you're describing as the bundle, how do we create a connected family of products that puts all of those things together so that wherever you come into the New York Times, to news or maybe through Wordle, you know that you're having the best experience within that category.

Alex Hardiman (00:21:49):
But then you also can quickly experience and discover everything else that we offer. That's the strategy and the vision, and it's a huge ambition. We want to get to 15 million subscribers by 2027. We're just over 9 million today, and I really think we can do it.

Lenny (00:22:06):
Awesome. I actually wanted to chat about goals and how you think about success as a product team. I imagine the north star metric is what you just said, which is subscribers. If that's true, what other goals do you have across teams? Maybe even further, I'm packing a lot of questions into one question, but I'm curious just how your product team looks. How many PMs do you have? Roughly, how do you structure the teams? Then, roughly, what kind of goals do they all have to try and imagine the product team at New York Times?

Alex Hardiman (00:22:34):
Let's start with structure. First, I love this question talking about my team because I love hyping them. They're amazing, and our success is truly only as good as our people. Yeah, it is so true. For us, when we think about our org structure, the way to set that up so that our people can really do their best work is that we have two axis. We have functions and then we have missions. I oversee two functions, which is the functions of product and design. The functions themselves, it's normal of what you would find in terms of functional responsibilities. We focus on standards of craft and excellence, career growth, career frameworks, equitable promotion processes, community of practices, skill development, all of that.

Alex Hardiman (00:23:21):
But missions is where a lot of the work happens. These are cross-functional teams, very similar to what we had at a place like Facebook. These cross-functional teams are led by usually a general manager, a product leader, or an engineering leader. They're all pursuing the same high level goals and objectives. Cross-functional missions at the Times, it can include a lot of the same skill sets that you would find at a tech company, PMs, engineers, designers, data scientists, researchers, product marketers. But the big difference is we also have editors, if it's a product space that directly shapes our journalism. I can talk more about that because it's a pretty interesting differentiating factor.

Lenny (00:24:02):
Yeah, that's super interesting. There's a journalist within cross-functional product teams?

Alex Hardiman (00:24:05):
Exactly. But we have three different types of missions. We have consumer missions, we have monetization missions, and we have platform missions. Editors are embedded within consumer missions. Those are the missions that I oversee, where we're focused on creating really great products, again, in categories like news, cooking, games, audio, et cetera. That is where having editors involved, particularly like editors who are very product minded, it brings in the best of their expertise and marries it with a lot of the normal signal that you look for in terms of data research and other insights. When you're trying to make sure that you understand a consumer problem and that you're really finding the best creative solution for it.

Lenny (00:24:48):
Cool.

Alex Hardiman (00:24:49):
It is really cool. It's one of the, I think, most gratifying parts of working at a news organization like the Times. But if you work on a different mission, like a monetization mission, we have two really big ones. One is subscriber growth, the other one that's also really important is digital advertising. They build centralized commercial products that we can then scale across all of the products in our bundle. The subscriber growth team, for instance, they look at making sure that we have really great account ID management for subscribers. If you're buying a subscription through games or through news. Or, if you're on the digital advertising team, you're trying to make sure that we have a first party data program that's really privacy safe, that works as well in cooking as it does in the news space.

Alex Hardiman (00:25:33):
Then, there's a totally different third bucket of mission that we have, which is all of our platform teams. This is everything from monetization platforms like our commerce engine, which is so important, because we're a subscription business, to data platforms where you might have our ML platform or experimentation tooling, to just basic infrastructure. Those are shared across the bundle, which just really helps make it so much easier, more efficient for really engineers to ship code and do their best work. A lot of this actually, I think, probably is pretty familiar to how you might organize at a tech company minus the editors.

Lenny (00:26:14):
Awesome. On that info piece, that reminds me of something I definitely wanted to talk about, which is something New York Times is really known for is the visualizations and these immersive stories that you all put out. I'm so curious just how that gets done. I feel like if I was on a product team at a regular, like a big tech FAANG company, I'd be like, "Shit, all these ad hoc things I got to do for all these stories, such a pain in the butt." That's so important to the New York Times and the online experience. I'm curious just like what is it like to build these things, say the election widgets, and all of that stuff?

Lenny (00:26:47):
Then, I don't know, I was just reading a story about climate change and it's this really beautiful immersive story of just what is happening with the world. There's a bunch of questions there, but I guess roughly just how does that get done, something like that?

Alex Hardiman (00:27:01):
Well, first, thanks for saying that. I really appreciate it. I do think there's something really special about some of the ways that we marry the journalism and the presentation. I want to start just by giving credit where credit's due, which is I think some of the most interesting and inventive and compelling formats, they actually do start off as one-off experiments that are spun up in the newsroom by embedded teams that we have within graphics, visual journalism, interactive news teams. This is where we have editors, journalists, engineers, data scientists, designers, literally all hunkered down together focusing on how to make one story come to life in the best possible way.

Lenny (00:27:37):
Who has the idea usually? Is it like the journalists working on that, they're like, "Hey, I think we should make something really great."

Alex Hardiman (00:27:42):
Exactly. Yeah, one of the things ... We have a newsroom of over 2000 people. You basically have people who've been experts on certain beats like climate, for instance, for decades. They have the nugget of the idea. They start to do reporting and then they really pull in others from visuals, from interactive just to say, "How can I really make sure that I can tell this story with as much impact and weight as possible?" That's where the magic starts to happen, when you pull in all of those other skill sets together to help dream up how that story might be told.

Lenny (00:28:18):
They're like, "Alex, we need one of these for our story. Can you get us on the list?" How does that process go?

Alex Hardiman (00:28:26):
No, no, no. These are teams that are really autonomous in the newsroom. For one-off, truly special features, I'll give you an example of one that I found to be particularly powerful. I don't know if you read Jodi Kantor, who is one of our ... a really incredible investigative reporter. You might know for some of her work that she did around MeToo and Harvey Weinstein, in that investigation.

Lenny (00:28:46):
Yeah.

Alex Hardiman (00:28:47):
She recently did a piece on how employers are tracking and monitoring remote workers with tools like productivity scores. The story itself was designed to show a person's own productivity score in the moment as they read the article.

Lenny (00:29:02):
Oh, shit.

Alex Hardiman (00:29:02):
It was super visceral, really creepy in the most effective way. In my mind, that's the type of magical experience that only happens when you actually have dedicated designers, engineers, and others who can really sit down with a reporter to say, "Let's figure out how to shape that story in the most magical way." The speed of news is so fast that you don't have time to mess with roadmaps. We really have teams who are freed up from some of the normal processes around that, so they can really just focus on storytelling for really big stories and pieces. But on top of that, what we do have is a storytelling product team. What they do is they really take notice of things that are starting to work in more of the experimental phase, some of these one-offs.

Alex Hardiman (00:29:50):
Then, they work closely with editors to test and find product market fit for new formats that can actually scale across many parts of the report, so that over time when you open the app, the app is more accessible, more engaging, because we still have the traditional story based article, but we're also shifting more of the distribution of stories into video, into visuals, into live. If you even look at live, we've broken out of the tyranny of the article in many ways, where you have live reporter updates that are the size of length of tweets. People filing from the ground in Ukraine, trying to give you a sense of what's happening in a very immediate and real way.

Alex Hardiman (00:30:31):
That's where we do have teams, product teams who have to think in two modes. First, they have to be able to think in the moment with editors, where you might not always have all the right data at your fingertips and you just have to make a call, like, "What is the best experience to tell this story in a really truthful, accurate, accessible way?" Then, the other mode is when they're not shipping at the speed of news, they're trying to build end to end systems so that we're building the tooling to actually create the stories at the same time as the consumer experience, which is a totally different mode of system level thinking.

Alex Hardiman (00:31:04):
It's a very cool space. That product team is, they're pulling off some pretty incredible work because they can operate in those two modes. It's like, in the moment, in the moment of the story, but also trying to build the systems that allow you to reshape the composition of storytelling formats that we have across our products over time.

Lenny (00:31:23):
That is super cool. What percentage of these fancy stories are using that platform and building on something that already exists versus a one-off experiment would you say roughly?

Alex Hardiman (00:31:32):
The majority are on our platforms hands down. Yeah. Yeah.

Lenny (00:31:36):
Okay. That makes sense. Then, just so I understand, so you said Jodi was the journalist?

Alex Hardiman (00:31:41):
Yeah.

Lenny (00:31:41):
You mentioned. Does she has a product team dedicated to her work?

Alex Hardiman (00:31:45):
No, what we have is we have a centralized interactive news team, graphics team, data journalism team. Those editors partner with different journalists when they have really big stories to help bring their story to life.

Lenny (00:32:00):
I see. Do they have to come to this team and be like, "Hey, I'd love your time." How does that prioritization ... Because I imagine a lot of journalists are coming to them like, "Hey, my story is going to be awesome. We need you."

Alex Hardiman (00:32:10):
You know what? To be totally honest, I'm not involved. Somehow it works.

Lenny (00:32:19):
That's a great leadership sign. It just works and you set it up and it's working, so that's great.

Alex Hardiman (00:32:25):
Well, and the newsroom has set it up and something that is just, again, very interesting about the way that we are set up is that we have our newsroom and then we have our business side. The business side is where you have all of the product teams and there is intense collaboration between the two, but they do have different leadership structures because that's how we maintain the independence of our coverage. Our product teams sit within the newsroom if they're focused on storytelling, live, anything related to the coverage.

Alex Hardiman (00:32:54):
The only distinction really that I think I'm trying to make is that product teams really help stories find their widest audience and be as engaging and as impactful as can be. But product teams don't have any influence over the selection of the stories. That is what the newsroom retains as editorial.

Lenny (00:33:14):
Okay. You mentioned Wordle and you all acquired Wordle recently. I'm just curious what that was all like. I imagine it's still being integrated. Were you involved in the exploration and purchase process and what went on there?

Alex Hardiman (00:33:28):
Wordle has been such a fun ride. Maybe I'll first just bring you behind the scenes on how the deal came to be, and then we can talk a little bit more about what the integration process has been like.

Lenny (00:33:37):
Yeah, sounds great.

Alex Hardiman (00:33:37):
I first heard about Wordle in early January because a New York Times reporter, Daniel Victor, actually wrote a piece about Josh Wardle, who's a software engineer in Brooklyn, and how he had created the game. It really is this gesture of love for his partner, and I certainly wasn't the only person to read through that column. Everyone inside the New York Times perked up. I remember reaching out to Jonathan Knight, who's the general manager of games, he's on my team. He had already taken notice well before the piece was published, and he had already reached out to Josh to see if he would be interested in having games join our portfolio.

Alex Hardiman (00:34:16):
We just all loved Wordle immediately because if you've played it, it shares a lot of the DNA of other really successful word games that we have at the New York Times, like Spelling Bee or the Crossword Mini. If anything, Josh was really forthright that he created it because he was inspired by those games. Then, in the context of just our subscription strategy, games is such an important category for us. We really see games and demand for games as this, basically, it's a counterpoint to the news. It gives people a chance to actually take a break. It's fun. It doesn't feel like empty calories. It's really time well spent.

Alex Hardiman (00:34:54):
We were just thinking of Wordle as such a wonderful addition to our games franchise to really give people more reasons to feel like they had a relationship with the New York Times every day. The whole thesis of the acquisition just made so much sense. Our team just very quickly engaged with Josh and the acquisition talks were incredibly fast. The whole thing took place in a matter of weeks, which is way faster than any other acquisition I've been a part of. It was a very amicable process. We were just super delighted to bring Wordle on board, but it happened in record speed.

Lenny (00:35:27):
Well, yeah, it felt fast from the outside too. It became a huge deal. Then, "Okay, New York Times buys them." Yeah, it's impressive. You said you acquired Athletic. How often are you acquiring companies?

Alex Hardiman (00:35:37):
We also acquired The Athletic, and that was back in around the same time. I think for now we feel like we actually ... we have all of the major categories to make the essential subscription work. For us to get to 15 million subscribers we really feel like news, sports, games, cooking, audio and shopping, those are the categories, and we just have to make them the best possible versions of themselves, those products, so that we can really provide just tremendous value every day to people. That doesn't mean that we won't make some other acquisitions. The next Wordle would absolutely love to hear about it.

Alex Hardiman (00:36:14):
But I do think there's also a real lesson for a lot of companies, not only about when you acquire what's the opportunity, but also are you ready to actually integrate an acquisition? We learned a lot just around Wordle in terms of what that process is like. I just want to say I'm really proud of how thoughtful and considerate our games team was about the integration process, because Wordle players feel such connection to the game. We really wanted to make sure not to interfere with the core magic of the experience. If you are an eight-year old kid or an 88-year old adult, there's real resonance with Wordle and people just have such a connection to it. We really wanted to make sure we didn't mess it up. Do you want to go a little bit deeper, just almost what that looks like?

Lenny (00:37:00):
Yeah, absolutely.

Alex Hardiman (00:37:01):
Because we definitely learned a lot. When we acquired Wordle, it was a simple web game with no backend. That meant that people's stats and streaks, which was that was the value in terms of social currency that people were sharing after playing, those stats and streaks were stored in local browsers. It was really important for us to make sure that the game board experience in the core loop of the game remained unchanged. But we also found that because everything was stored locally and people care so much about their stats and streaks, if they got a new iPhone, if they switched browsers, all of a sudden they lost all of that history that they had with the game.

Alex Hardiman (00:37:39):
What we decided to do was undertake a project to connect Wordle to a New York Times account, which was free, because Wordle is a free game, just so that it knows who you are and so that your stats and streaks can be protected. Then, we could also bring Wordle to more surfaces because we wanted ... if you go to the homepage of the news app or if you go to the games app, we wanted to make it easier to find because people would come for Spelling Bee or Crosswords and they also wanted their Wordle. It was a pretty big effort to rewrite Wordle in our tech stack, give people the ability to store their stats and streaks, bring games to all of our major surfaces.

Alex Hardiman (00:38:16):
We just tried to do it in a thoughtful way, where we didn't break anything. The experience was hopefully seamless, and that the only thing you would notice that's changed is that the New York Times knows enough about who you are so that your stats carry over and you can play anywhere. But that doesn't mean that there aren't some surprises along the way, especially when you're doing backend work. We had this pretty crazy moment a couple months ago, right when the Supreme Court's draft ruling on Roe v. Wade leaked. An engineer on the games team happened to notice that the Wordle solution the next day was fetus. Which is just an extraordinarily bad coincidence, because the word had been loaded into the game by the game founder months beforehand.

Alex Hardiman (00:39:02):
It was so important for us that we didn't have ... this lovely diversion from the news feel almost like it was commentary on a very contentious story that was happening. I don't know if you caught wind of that, but you'd think that you could easily change the word on the backend, but because we were midstream on the migration process and some users were on the original Wordle game, others had migrated to the new version. It meant that we actually couldn't change the word on the backend for everyone, only for some people. This was a moment where we just had to come out and really tell the world, "We're mid integration. We're really not trying to communicate more than Wordle being a fun diversion from the news. Here's what happened, and why."

Alex Hardiman (00:39:50):
Everyone understood. This is where coming out being really transparent about the facts and in some cases just exposing more about the product development process really helps demystify some of the rumors that people might otherwise think. It was one of those like, "Oh, man, I couldn't have imagined that that type of terrible coincidence would happen." But you just have to be prepared for everything, even when you're integrating what should just be a fun game.

Lenny (00:40:16):
Imagine, no matter what you tell people, some folks are just not going to believe a very simple explanation of what was going on.

Alex Hardiman (00:40:23):
It's true. All you can do is be as honest and transparent. What I will say is a lot of people still think we try to make Wordle harder, we don't, I promise. It's not a thing.

Lenny (00:40:33):
Yeah, it's not like the crossword puzzle where it gets harder every day of the week.

Alex Hardiman (00:40:38):
No, no. It's not, it's not.

Lenny (00:40:43):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements. Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals or it can put your business on hold.

Lenny (00:41:17):
If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Beginning a SOC 2 report can be a huge burden, especially for startups. It's time consuming, tedious, and expensive. Enter Vanta, over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time, Lenny's Podcast listeners get $1,000 off of Vanta.

Lenny (00:41:49):
Just go to vanta.com/lenny. That's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today. Are there any other stories that come to mind that reflect just how interesting/wild it is to work at the New York Times as a product leader?

Alex Hardiman (00:42:12):
If we could of go back to when I started at the New York Times, because I started in late 2019, it was just right before the pandemic. It was pretty wild to come back to the company and to get shifted into this moment of needing to build products that really were trying to help people through the moment. At a time when our journalists were covering the story and all of New York Times' employees were trying to live through it. It was COVID 24/7 in terms of work and life. For me, I remember in the earliest days when we were first really reporting on COVID and learning about it, we had reporters on the ground in Wuhan even before we knew how COVID was transmitted.

Alex Hardiman (00:42:52):
Then, when the world shut down, for the Times, we went fully remote in March, 2020, and I remember the day so well because it was the beginning of spring break, of course, all plans were canceled. My kids, I had no idea what to do with them. My husband and I panic packed, put them in a car, drove to go see some friends in Vermont, and we decided we were going to do a kid daycare pool share just to figure out how to keep working with someone overseeing the kids. We got there late at night and I literally just went into a laundry closet and I didn't emerge for two weeks because my Slack was blowing up about all of the work that we needed to do to make our products as useful as possible.

Alex Hardiman (00:43:32):
The kids were being crazy and we just had to get to work. What was really stunning about this moment in time was that as people were getting sick and we were reporting about all of the trends that we were seeing, we saw that other institutions, especially the government, were not actually stepping up to help people understand the basic facts about what was happening. This is a product leader, it's a real wartime moment where you just need to blow up roadmaps, share context with everyone and say, "Okay, everyone, we have a totally different mandate than what we did a couple weeks ago." Given the needs in the world and the mission of the New York Times and our purpose, which is to help people access information to make informed decision about their lives, we're going to do a whole bunch of these things.

Alex Hardiman (00:44:17):
We're going to build a comprehensive public data set of COVID cases. Nobody else is doing it. We really just started scraping and pulling this together, and what was a single spreadsheet at the time. We pulled a bunch of engineers from other teams to go help build out that database. We launched entirely new formats and data tools to make our journalism a lot more easier to follow. Things like tools to be able to look up infection rates and eventually vaccination rates down at your local zip code level. We made our most important COVID coverage free to everybody. It was really important that if it was something related to public safety, we didn't put it behind a paywall.

Alex Hardiman (00:44:53):
Our mission is to do better than that. We really made sure that we had that information available to everyone. We also just found that for journalists who hadn't actually been in Wuhan, they just needed tips to an internal safety guidance for reporting, and so we made that publicly available. It was just one of those really interesting moments where everything felt so crazy in this moment of crisis. But building purposeful products that made a really difficult moment feel not only possible but promising, was one of the most unifying moments, I would say, for our teams.

Alex Hardiman (00:45:29):
Because even though people were working so hard and balancing work life and personal life, no one doubted for a second that the work they were doing was of greater good for the world. There's real privilege in being able to spend your time doing those things. But it's one of the biggest news stories of our lifetime and to be at the forefront of that, I think for all of us, was a pretty incredible and humbling experience.

Lenny (00:45:55):
Wow. People talk about having impact and driving impact and it's usually like, move this metric some percentage, but that is some incredible impact. Helping people avoid COVID, avoid dying, keeping their families safe. It's got to be some of the most fulfilling work that you and your team has done and ideally it wouldn't have happened, but it was also probably incredibly fulfilling.

Alex Hardiman (00:46:20):
Thank you for saying that. One of the most validating tricks that we did look at was we realized that at the height of the pandemic, when there was just so much confusion about literally what to do, how to live each day in March, 2020, we saw that half of the country came to the New York Times. There is something again that is just so powerful about very straightforward data journalism, deep reporting, service guidance on how to make a mask if you don't have one. Just like all of these basics. Just seeing the whole organization pivot from their normal job into this mode and was pretty incredible, and the world responded, which was really validating too.

Lenny (00:47:00):
I imagine there's also a bit of burnout that happens working, where it goes on and on and on. You're like, "Oh, my God, when is this going to slow down?" How do you help people avoid burnout? How do you catch burnout as a leader on a product team?

Alex Hardiman (00:47:15):
This is one of the most honestly, hard and important topics that I think we're always still grappling with. As a company, we really did try to lead originally with giving people more time off, more support, like financial support and other assistance with daycare, health benefits, all of the basics. I think now what we're really trying to do beyond that is be so much more focused on the things that we need to do and all of the things that we're really happy to stop doing. Because part of, I think, context switching is one of the things that is really, really difficult. It's hard to context switch in your job.

Alex Hardiman (00:47:53):
It's really hard to context switch across your job and your life. There are a lot of things that we as a company can't necessarily control in people's lives, but within the job, the places where we can be so much more focused and thoughtful about the small number of important things that we must do at a given point in time, that's really the place where we're really trying to come in and be as empathetic and as honest about what we need to do and what we don't need to do. A lot of it really comes down to, I think, making hard calls. We're not always perfect at it. I'm sure that there are things that we could be more diligent about.

Alex Hardiman (00:48:27):
But I would say over on balance, we've seen a lot of people stay at the company because they're figuring out they work remotely, maybe they come back to the office. They're figuring out how to live their life in a very different way from a couple of years ago. We're really here to try to meet them and make that as possible as possible. We need incredible people across a bunch of different skill sets, a bunch of different backgrounds. The only way to do that is to really be very flexible and accommodating in terms of trying to meet people where they are in their lives, but it's tricky.

Alex Hardiman (00:49:03):
There is no perfect answer for this, but we're really trying because the success of the company only works when we have people who feel valued and they can do their best work and live really rich lives on top of that. I think we're all still figuring out what that looks like now that we're starting to come out of the official pandemic and really just learning how to live with COVID.

Lenny (00:49:23):
Right, absolutely. You mentioned that you're all remote now. Is that the policy going forward?

Alex Hardiman (00:49:29):
We actually just started going back into the office a couple of days per week, which is very encouraged. We're still finding our groove. We do have a good number of people though who are fully remote as well. It's more of an evolution in terms of trying to find the right balance of taking advantage of in-person work, because there are some moments where it really does make such a difference when you have people together working through hard problems in real life. That camaraderie, those relationships really, really do matter. Also, being realistic about the fact that there are a lot of people who would love to work at the New York Times, but might not be able to live in the New York City area.

Alex Hardiman (00:50:11):
So, how do we make sure that we can be a remote friendly company for them too? Yeah, so we're very hybrid, we're still testing our way through it. But by and large, we're shipping so much tremendous work, which I think is a reflection of us being able to do the hybrid thing and just try to get better and better at it each day, each week.

Lenny (00:50:30):
Yeah, it's hard. As an outsider, I can't imagine a New York Times being all remote. It feels like that kind of company just, it's all happening in a building somewhere probably. I'm also a big fan of in-person, it feels like as a company, it feels like you have an advantage if you're working in-person generally.

Alex Hardiman (00:50:46):
We certainly see that, and so the center of gravity is in New York and is in the office, but again, with a lot of flexibility for people's lives. We're really trying to figure out that balance.

Lenny (00:50:58):
Just a couple more questions before we get to our very exciting lightning round. Where's the New York Times in the next five, 10 years as a product specifically different from other folks? Then, broadly, I don't know, if you have any insights or opinions on just what is the future of news, do share.

Alex Hardiman (00:51:13):
I think the New York Times is in a pretty unique spot compared to other news organizations right now. I have tremendous respect for other high quality organizations like The Journal and The Post and The FT and The Guardian. They're just doing such incredible work. But when I go back to what differentiates us, it's this idea of becoming an essential subscription that really helps people. It meets their most important news and life needs across all of the categories that we've been talking about, like news, games, audio, cooking, et cetera.

Alex Hardiman (00:51:44):
Up until, I would say, this year we were more of a news brand with a collection of adjacent lifestyle products, but with the acquisition of Wordle and the Athletic, along with just the continued growth of cooking and Wirecutter and some of our other offerings, I really do think that has transformed us into a brand capable of really being that essential subscription that helps every single day people with news and life needs in a way that doesn't just associate the New York Times with [inaudible 00:52:12] categories. Imagine that you open the New York Times app and you are starting with a great breaking news story. Then, you skip over to the latest coverage in China.

Alex Hardiman (00:52:25):
Then, you decide that you want to take a small break to play Spelling Bee, and then you want to plan a Korean dinner party with Eric Kim, who I don't know if you know has some of the best Korean recipes. He's amazing. Then, you're like, "Wow, I need a rice cooker to be able to make that recipe, so I need to go get the best recommendation from Wirecutter."

Lenny (00:52:43):
I just did exactly that, actually.

Alex Hardiman (00:52:45):
Did you?

Lenny (00:52:45):
Yeah.

Alex Hardiman (00:52:47):
Then, I would love to go watch the Britney Spears documentary, which is also part of the New York Times franchise, which is amazing. Or, I want to go listen to Kevin Roose and Casey Newton's Hard Fork podcast, which is wildly fun and just launched a couple weeks ago, if you haven't heard that. This is, I think, the future for us of being a connected family of products, where we can meet so many different needs that are first anchored in news, but then stretched into other facets of your lives. I don't really see other news organizations really operating at that scale and that ambition, and that's the future for us.

Alex Hardiman (00:53:24):
We really just think that the New York Times can mean so much more to so many more people. We're a journalism company, but we're building just tremendous software, and so the product ambitions are only getting bigger and bigger, and that's why I feel like I've got the luckiest job in the world right now.

Lenny (00:53:42):
That is a compelling vision. I feel like you can build your own metaverse in the New York Times where you just spend all of your days inside the New York Times' suite of products.

Alex Hardiman (00:53:52):
Can I say though, there is a big difference. I think that for us our software actually helps people with real world outcomes in a very different way. We basically help you get access to information, decide how you're going to go to the ballot box. We give you information to go cook. Actually, there's something that I think is even more of a connection to the physical world, and it is very different from what the Metaverse is doing, but that's where we feel like we can drive as much impact as possible.

Lenny (00:54:20):
You can have your own competing metaverse. Here's a quick Wirecutter suggest idea for you, while we're chatting. I feel like Wirecutter, I use it all the time, everything I buy is based on Wirecutter recommendations, but I feel like there's an opportunity for design oriented version of Wirecutter. I don't know if anyone's thinking about that.

Alex Hardiman (00:54:37):
Tell me more.

Lenny (00:54:38):
Just Wirecutter's functional stuff. It's like, "Here's the best, I don't know, rice cooker." But like, what's the cutest but also the best? What's the cross section of looks good in my house and is the best. I'll be okay not the best best if it looks nicer, so a design lens to Wirecutter.

Alex Hardiman (00:54:54):
If it's Wirecutter meets high taste, basically. I like that. I like that. Okay.

Lenny (00:55:02):
I think there's a market there.

Alex Hardiman (00:55:04):
I'll definitely bring that back to the team. That's a good one.

Lenny (00:55:06):
There you go. Well, we've reached our very exciting lightning round where I'm just going to ask you, I have six questions, I'll get through them pretty quick. Whatever comes to mind, fire off. We'll go through it fast and fun. Sound good?

Alex Hardiman (00:55:21):
Great.

Lenny (00:55:21):
Okay. What are two or three books that you recommend most to other people?

Alex Hardiman (00:55:27):
I love Stripe Press, and so I think a lot of the books that they have are just such good references, like Elad Gill's High Growth Handbook, or Will Larson's An Elegant Puzzle. Then, some of the more topical ones like Revolt of the Public. I just find that they're evergreen in terms of their utility. Anyone can find value in them. I just loved the craft of the books themselves. They are amazing products in terms of the content and the form, so those are, in the product context and work context, those are hands down I would say the places where I go first.

Alex Hardiman (00:56:01):
But I do think, and I know this is this humanities major in me, I also always try to balance books and my own reading time and recommendations with fiction. I just think it's actually like, sometimes some of the best ideas and inspiration come when you go one or two steps away from the core books that are related to your practice. Right now, I'm actually rereading Giovanni's Room by James Baldwin. It's just so beautiful and so lyrical and it gets at more components of the human soul that, I know it sounds crazy, but I find like those are little sparks of ideas that ultimately come back into making products, and particularly news products where they're so creative in the way that they tell stories.

Alex Hardiman (00:56:46):
I always try to give people one pragmatic recommendation and then one slightly more field recommendation over in the world of fiction. If you haven't read Giovanni's Room, it is incredible and devastating, and I absolutely recommend it.

Lenny (00:57:00):
Wow. I feel like I just keep buying books after doing these podcasts. I have so many books I got to read. I'm also feeling like the combination of books you recommended is exactly what I would imagine someone leading product at New York Times would recommend, something product tactical and then just a beautiful piece of fiction.

Alex Hardiman (00:57:18):
I'm the cliché. I love it.

Lenny (00:57:21):
Great. No, no, no. I wouldn't put it that way. Okay. What's a favorite other podcast that you like to listen to? You mentioned one already, is that the one?

Alex Hardiman (00:57:28):
Everyone should listen to Hard Fork. It's great. But I just think The Daily continues to be, and again, I know it sounds self-serving, but being able to just listen to Michael Barbaro and Sabrina Tavernise once a day, just bring in journalists to talk and unpack a meaningful story, it's so visceral. I just find it to be one of the daily miracles that the New York Times is able to produce.

Lenny (00:57:51):
Yeah, that's wild. I can't imagine a daily thing like that doing that. Impressive. What's a recent favorite movie or TV show that you've seen that you've really enjoyed?

Alex Hardiman (00:58:01):
I am pretty old school. I am actually rewatching The Wire for the third time.

Lenny (00:58:06):
Wow. That's a lot of time commitment.

Alex Hardiman (00:58:09):
It is. I have very little time, but every five years my husband and I, we just can't get over the characters, the storylines. It's just one of the best made series for television ever. It's a work of art, and so I am that person, that is another cliché, who is rewatching The Wire right now.

Lenny (00:58:27):
What's your favorite season?

Alex Hardiman (00:58:28):
I would probably say it's season three, but when Stringer Bell passes away, it's the culmination of just so much. I probably shouldn't say that for anyone who hasn't seen The Wire. Oh, that's like the worst thing ever.

Lenny (00:58:43):
Spoiler alert in reverse.

Alex Hardiman (00:58:45):
Spoiler alert. I'm so sorry.

Lenny (00:58:46):
But that's not the character name, that's the actor, right?

Alex Hardiman (00:58:49):
No, no, I really just totally spoiled that.

Lenny (00:58:51):
Okay, that's cool. If you haven't seen it at this point, it's over, your loss.

Alex Hardiman (00:58:56):
Oh, boy. How awful. That's like a cardinals sin. But I do think season four, when it starts to get into the school system is also just, the actors are incredible. It's some of the best acting that I think has existed over the last couple of decades. Again, if you haven't seen it, please do yourself a favor and watch it. It's worth every episode.

Lenny (00:59:16):
Would you agree season two is the worst?

Alex Hardiman (00:59:19):
I thought that until I re-watched it.

Lenny (00:59:22):
Interesting.

Alex Hardiman (00:59:22):
I actually came around and it's not at the top of my list, but there's more to it than I think I originally gave it credit for.

Lenny (00:59:30):
Wow. I like this. Okay, great. What are four to five SaaS products that you or company uses most that you find really useful?

Alex Hardiman (00:59:39):
Probably pretty classic, we use G-Suite, Slack, Figma, Mode, GitHub. Those are the ones that I think just get hands down the most amount of usage across our teams.

Lenny (00:59:51):
The fourth one was Mode?

Alex Hardiman (00:59:52):
Yeah.

Lenny (00:59:53):
Is there any interesting new recent one that's like top of mind while we're on this topic?

Alex Hardiman (00:59:58):
Not really. No.

Lenny (01:00:02):
Okay, great. The winners keep winning, huh? These products?

Alex Hardiman (01:00:07):
Yeah. If anything, it's like when you don't talk about the SaaS products you use, I feel like that's more of a success because it's just, it works behind the scenes, it blends in and it just makes everyone so much more productive.

Lenny (01:00:19):
Yeah. Imagine all these companies have the New York Times logo on their site of people using that.

Alex Hardiman (01:00:24):
Maybe.

Lenny (01:00:24):
That would be a big deal when you guys adopt a product. Final question. Who else in the industry do you most respect as a thought leader and thinker?

Alex Hardiman (01:00:32):
This is a hard question, but I would say one of the people who I find to just be a really tremendous product thinker, leader, and ally for women is Fidji Simo. I was lucky enough to work with her and for her when I was at Facebook and just watching the way that she ... what she did with Facebook, what she then is doing at Instacart and the way that she really just helps so many other women in the field figure out how to be better at their craft, how to have more opportunity. I don't know how she has these many hours in her day, but she's pretty incredible, so I would love to give a shout out to her.

Lenny (01:01:10):
Awesome. I will try to get her on this podcast.

Alex Hardiman (01:01:13):
Oh, that would be amazing. All right. She's really-

Lenny (01:01:15):
That's what I need to do. Awesome. Good recommendation. Alex, this was amazing. I learned so much. This is such a fun conversation. Thank you, again, for doing this. Two last questions, where can folks find you online if they want to reach out and learn more? Maybe think about working at the New York Times and otherwise, how can listeners be useful to you?

Alex Hardiman (01:01:32):
Thanks. You can find me on Twitter, LinkedIn, all the usual channels. I would love to hear from anyone and would be delighted to also talk about what it's like to do product at the Times. Then, the thing that would be really useful is what is the one feature that would make the New York Times more essential and more valuable to you in your daily life? I would love to hear from people on that front.

Lenny (01:01:53):
All right. I shared mine, a design-oriented Wirecutter. I will be looking for that.

Alex Hardiman (01:01:59):
Thank you.

Lenny (01:01:59):
Awesome. Thank you, Alex.

Alex Hardiman (01:02:00):
No, of course. There's just one other whole theme, and I don't know if you want to chat through it, which is, what are some of the similarities and differences between product management in news organization?

Lenny (01:02:14):
Let's do it.

Alex Hardiman (01:02:14):
It's totally up to you. But if that's something that you'd be interested in talking through.

Lenny (01:02:20):
Absolutely.

Alex Hardiman (01:02:21):
I'm going to just focus on two themes that I think are pretty interesting. The first is just how we work at the New York Times, and we talked a little bit about working with journalism, and there are some really interesting differences. The second is just on the idea of impact. I think how the definition and the understanding of impact can be pretty different. First, just on the idea of how we work, there are a lot of similarities. I would say that product managers at the Times and at tech companies, they have a lot of the same skills. Like, we look for a great product sense, great execution, great leadership and drive.

Alex Hardiman (01:02:59):
Any good PM needs to know their industry, their customers, their market, their business, et cetera. We actually do see a lot of crossover between product managers from tech companies who come to the New York Times or tech PMs at the Times who go over to tech companies. I think that that's wonderful, but a key difference of when you're a product manager working at the New York Times is that you work across the full stack of the product. Meaning, we own our journalism and our content. We own our distribution and we own our products. That's really different from working at a big tech platform. When I was at Facebook, we controlled the software and the distribution, but we didn't control the content.

Alex Hardiman (01:03:39):
We had real limitations on understanding what was passing through. Was it high quality content, low quality content? It just led to, again, a lot of challenges that we already talked about. At the Times, when I think about how our best products are born, it's when you bring journalism and product lovers together. That means that PMs at the Times really need to understand the blend of art and science. They really need to value expert editorial judgment as they're also looking at individual KPIs, customer research and insights, et cetera. An interesting example, as I was trying to think about what would feel really different doing product at the Times compared to say Facebook is like, let's say you're at the product team and you're working on the home screen.

Alex Hardiman (01:04:25):
We always start with expert editorial judgment to curate the most important and interesting stories. But on top of that, we're training algorithms on specific data sets, like editorial important scores that actually come from our journalists. What that allows us to do is actually scale editorial judgment to a large group of readers. Those algorithms, what I think is just really great is they're trained on editorial signal and then they can still work towards driving towards outcomes like reach, engagement, conversion, et cetera. That's just such a different way of thinking. When I was at Facebook and we were focused on news ranking and feed, all we could do was train pieces of in information based on an engagement outcome.

Alex Hardiman (01:05:12):
We couldn't actually train it based on the quality of that piece of information itself. At the Times you get all, you have 2000 plus journalists and you're actually trying to structure their expertise into things that can actually translate into really great algorithmic decisioning, and that's just so different. No one else is really doing something in that space. Product managers are becoming very editorially minded and we're also getting editors to become more product minded. I just think that how we work there is so different and so unique. It's just a pretty fascinating part of, I think, how the sausage is made, if that makes sense.

Lenny (01:05:46):
Yeah. Thanks for sharing that. I think that's really important topic of just how it's different and why it's worth considering trying something like the New York Times as a place to work. What's interesting about what you're talking about, this also reminds me ironically of Substack, where they also are anti-algorithms and are also very focused on people and people recommending other people and just like individuals. I don't know if we want to get into this, but I guess do you have a opinion of Substack as a medium? Because folks leave New York Times to work on Substack, they come back. My whole living is on Substack. Any thoughts on the world of Substack?

Alex Hardiman (01:06:25):
Well, a couple of things. First, it's not that we're anti-algorithm on the New York Times front, it's just that we want our algorithms to reflect editorial judgment. That's really different. When it comes to Substack, actually, I think a lot of what Substack is doing is great. The idea of writers being able to make a living individually off of their craft, I think, is fantastic. The thing that I get excited about for Substack, but also for a company like the New York Times is trust right now with institutions has been declining, with governments, with religious institutions, with news organizations.

Alex Hardiman (01:07:00):
But trust with individual experts, where you have a real relationship, that really matters. That I think is one of the big unlocks in terms of helping the next generation of readers really start to create more of a relationship with high quality journalists and writers who have really important things to say about the world. I think whatever is happening in the world that helps great writers find their audiences, make a living, is wonderful. At the New York Times, a lot of what we're trying to do is, it's not the Substack model, but we have a lot more that we're doing to actually help get individual journalists out there.

Alex Hardiman (01:07:39):
They have their own subscribe only newsletters, podcasts. We're really trying to help them find a way to create a mini platform within the means and the scale of the New York Times. It's not quite the Substack model, but I do think that there's some interesting similarities, and the more that artists and creatives can help make a living, I think, it's just fantastic.

Lenny (01:08:00):
I'm here for it. I love this two-part encore bonus we just did. Anything else that you want to share before we wrap up?

Alex Hardiman (01:08:10):
I think the only other thing that I have come to learn when you're doing product management at a news organization compared to a place like Facebook is just how different the definition of impact can be. When I was at Facebook, we were incredibly focused on scale, engagement, and revenue, which is very appropriate. At a company like the New York Times, we also have a huge ambition to grow our subscriber base. But one thing that's really interesting is that our impact and our business goals are in service of our mission, which is to seek the truth and help people understand the world, not the other way around.

Alex Hardiman (01:08:51):
What it means is that the way that we think about impact is growing a giant subscription business. That business exists to strengthen an informed democracy at a time when people are struggling to understand basic facts and struggling to understand each other. That means that impact for us is growing subscribers, but it's also when a deeply reported story triggers an important policy change or a new law. When you're a product manager you're involved, again, in driving specific metrics like engagement or subscribers.

Alex Hardiman (01:09:26):
But you're also trying to help stories find their real audience in ways that trigger just this whole different side of mission and purpose driven impact. I didn't feel that when I was at a place like Facebook, but at the Times, I think it just gives product managers a bit of a broader aperture in the ways that they think about the relationship between business goals and mission impact goals, and it's pretty cool.

Lenny (01:09:50):
It does feel like it would be hard to find more meaningful, impactful work, and so that really resonates.

Alex Hardiman (01:09:57):
Oh, thanks. There are so many other important purposeful products and problems out there to solve in the world. We've talked about this, Lenny, but I just think that product managers and product thinking in so many contexts inside and outside of tech has never been more important in the world than right now. We need product managers everywhere diagnosing key problems and issues, coming up with radically novel solutions. This is the moment. It's really great to have your podcast and so many other resources out there to help new and other PMs just do their best craft. Thank you for having all of us in here.

Lenny (01:10:33):
I love that as a closing thought. Alex, thank you again so much for doing this.

Alex Hardiman (01:10:37):
Thank you so much, Lenny. This was really fun.

Lenny (01:10:40):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

