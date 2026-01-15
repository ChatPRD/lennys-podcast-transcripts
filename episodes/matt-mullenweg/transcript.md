---
guest: Matt Mullenweg
title: The one question that saves product careers | Matt LeMay
youtube_url: https://www.youtube.com/watch?v=ts9ZvlkeWGs
video_id: ts9ZvlkeWGs
description: 'Matt LeMay spent 13 years as a music critic at Pitchfork before becoming
  one of product management’s most influential voices. He’s consulted with companies
  from startups to Fortune 500s...

  '
duration_seconds: 5529.0
duration: '1:32:09'
view_count: 27437
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- iteration
- subscription
- revenue
- hiring
- culture
- leadership
- management
- vision
- mission
- competition
- market
- persona
- design
---

# The one question that saves product careers | Matt LeMay

## Transcript

Lenny Rachitsky (00:00:00):
If you're really open and open source, sometimes you have to stand up the bullies and you have to fight to protect your open source ideals.

Speaker 1 (00:00:05):
Please put your hands together for Matt Mullenweg.

Lenny Rachitsky (00:00:08):
Matt Mullenweg has been making some questionable moves recently. There's a lot going on with Matt and WordPress these days. 20+ years of good sentiment burned in days. You are like a 100% beloved hero of open source and internet and now you're in this, a lot of people don't like you.

Matt Mullenweg (00:00:23):
If you were kind of inside baseball with WordPress, it's actually a lot of people who have been unhappy with me over the years. Previously, 1% of the world thought I was terrible and now I feel like it's up to four or 5%.

Lenny Rachitsky (00:00:35):
People that don't know what the hell's going on, what's just like the high level overview of what's going on?

Matt Mullenweg (00:00:39):
There's a company called WP Engine. By 2018, they got bought out by a private equity firm called Silver Lake. Since 2019, WP Engine has kind of changed a bit. They started using the trademark, they're offering something called WordPress. They're referred to it as like a bastardized hacked up version of it. It's diluting our brand.

Lenny Rachitsky (00:00:56):
Why do you think so many people are looking at you as the bad guy?

Matt Mullenweg (00:00:58):
A lie gets around the world seven times before the truth has time to get out of bed.

Lenny Rachitsky (00:01:07):
Today my guest is Matt Mullenweg. Matt is the co-creator of WordPress, which powers 40% of websites on the internet today, including whitehouse.gov. He's also the CEO of Automatic, which is valued at over $7 billion and owns products like WordPress.com, Tumblr, WooCommerce, Gravatar, and Pocket Casts. There is a lot of drama these days around Matt and WordPress and within the open source community, so I thought I'd have Matt on to address many of the criticisms head-on that he hasn't addressed in other places and also just get the full story on what's going on. We also chat about what incepted him to spend over half his life at this point on open source and creating WordPress. Also, why products like Llama are what he calls 'fake open source' and his perspective on AI and open source. Also, how AI is actually trained on open source code and what that means for the future and his approach for deciding what companies to acquire within Automatic.

(00:02:03):
If you enjoy this episode, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you now get a year free of Notion and Superhuman and Perplexity Pro and Linear and Granola. Check it out at lenny'snewsletter.com. With that, I bring you Matt Mullenweg.

(00:02:24):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and skim provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow and Loom. WorkOS also recently acquired Warrant, the fine grain authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, skim or user management, you should consider WorkOS. It's a drop-in replacement for auth zero and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more, that's workos.com.

(00:03:42):
This episode is brought to you by Vanta and I am very excited to have Christina Cacioppo, CEO and co-founder Vanta joining me for this very short conversation.

Christina Cacioppo (00:03:51):
Great to be here, big fan of the podcast and the newsletter.

Lenny Rachitsky (00:03:54):
Vanta is a longtime sponsor of the show, but for some of our newer listeners, what does Vanta do and who is it for?

Christina Cacioppo (00:04:01):
Sure. So we started Vanta in 2018 focused on founders helping them start to build out their security programs and get credit for all of that hard security work with compliance certifications like SOC 2 or ISO 27001. Today we currently help over 9,000 companies including some startup household names like Atlassian, Ramp and LangChain start and scale their security programs and ultimately build trust by automating compliance, centralizing GRC, and accelerating security reviews.

Lenny Rachitsky (00:04:31):
That is awesome. I know from experience that these things take a lot of time and a lot of resources and nobody wants to spend time doing this.

Christina Cacioppo (00:04:39):
That is very much our experience before the company and to some extent during it. But the idea is with automation, with AI, with software, we are helping customers build trust with prospects and customers in an efficient way. And our joke, we started this compliance company so you don't have to.

Lenny Rachitsky (00:04:55):
We appreciate you for doing that and you have a special discount for listeners, they can get $1000 off Vanta at vanta.com/lenny, that's V-A-N-T-A .com/lenny for $1,000 off Vanta. Thanks for that, Christina.

Christina Cacioppo (00:05:10):
Thank you.

Lenny Rachitsky (00:05:14):
Matt, thank you so much for being here. Welcome to the podcast.

Matt Mullenweg (00:05:17):
Thanks, big fan and long time listener, so happy to be on.

Lenny Rachitsky (00:05:21):
I'm a long time fan. I've been wanting to get you on this podcast for so long and this is such an interesting time to be chatting with you, there's a lot going on with Matt and WordPress these days, so it's really interesting, almost good that we waited a little bit to talk so we're going to get into a lot of that stuff. But I want to start with just what is it that you do, Matt? What are all the things you're involved in? Give people a sense of just the things you're working on.

Matt Mullenweg (00:05:44):
So first, when I was 19, I co-founded an open source project called WordPress with Mike Little and we started just blogging software, then became sort of a full site thing and then became a platform that really tons of stuff is built on and now it's kind of transitioning into this cool WASM can be embedded anywhere or run locally or make mobile apps. It's really interesting seeing WordPress used as an engine for powering things I would say don't even look like a website, which is kind of wild to me, but that's kind of the beauty of the open source people do things with that you don't expect. End up dropping out of college, moving to San Francisco and then worked at CNET for a year as project manager actually, that's how they hired me.

Lenny Rachitsky (00:06:27):
I want to talk about that, but go on.

Matt Mullenweg (00:06:30):
And then had this vision where instead of downloading the software and setting up a database and everything, we made a SaaS version of WordPress. I pitched it at CNET, they didn't want to do it, so I was like, "Okay, I got to do this," so I left and started a company called Automatic. And the idea was to essentially compliment the core WordPress software with some commercial services, things that run in the cloud, like Akismet which is our machine learning AI, I guess you'd call it AI now, but anti-spam system, or Jetpack, which is iCloud for WordPress. It does the backups and the real time sync and everything like that.

(00:07:04):
So that was 19 years ago, so that's now grown to be over 1700 people in actually 90 countries so we've actually been fully distributed and remote and asynchronous from the start, which I think is one of our superpowers. I actually wasn't the CEO in the beginning, but in 2014, so I guess 11 years ago, I became CEO. The original CEO was... Well, I guess I wasn't the very beginning, but then I hired Tony Schneider from BCL, probably four or five months in.

(00:07:35):
And yeah, so that is a very full-time thing and Automatic does a lot of products, WooCommerce, which is open source Shopify, which is now half our revenue. And then we have some really cool apps so like Beeper, DayOne, Simplenote, Rocket Casts or trying to fill up your home screens with open web, open source things that are very privacy and user-centric. So running that company is definitely a full-time job. I still run WordPress.org and the WordPress project, so I'm the lead developer there and so sort of manage all those releases in the community and the directories and all the sort of things we do on WordPress.org and this cool thing called Openverse we took over Creative Commons, which is a way you can find sort open licensed images and audio and video. So basically if you notice a throughput through all these things, it's open source.

(00:08:31):
On the nights and weekends or side, a few hours a week I do some angel investing. So I've done over 100 angel investments through an entity called Audrey Capital, which is sort of, if anything's in the sort of WordPress space, I invest in it through Automatic, but if anything's a little more further afield I do it through Audrey Capital and have done some really exciting investments there, everything from name brands like Stripe and SpaceX, but also it was in the seat of Calm or a lot of home automation stuff like Ring, August, smart things. Yeah, just check out Audrey Capital, it's got some fun stuff in there. Daylight Computer, which is one I'm very excited about right now.

(00:09:11):
And I guess finally I love San Francisco, so I an a co-owner of a cool grungy jazz club in North Beach called Keys with Simon Rowe. So if Wednesday through Saturday night, you want to see some awesome live jazz, check out Keys.

Lenny Rachitsky (00:09:28):
Wow, okay. You said too much, I get it now. Jazz club I was not aware of, I got to check this out. It's called Keys?

Matt Mullenweg (00:09:36):
Yeah, keys Jazz Bistro.

Lenny Rachitsky (00:09:38):
Okay, cool.

Matt Mullenweg (00:09:39):
It's over on Broadway in Columbus, kind of right around there.

Lenny Rachitsky (00:09:42):
Amazing. That was news to me. Going back to Automatic, I think people don't get the scale of this thing, so just to mirror back, if you think that even add to what you've said, 1700 people work there, 90 different countries. Also, you didn't share this stat, it was something like 43% of internet websites are built on WordPress, run on WordPress.

Matt Mullenweg (00:10:02):
Yeah, so when we started, a lot of websites were built on custom CMSs and there's a lot of fragmentation in the space, but now WordPress has grown to be over 40% of all websites in the world, which is 10x the number two, which right now is Shopify.

Lenny Rachitsky (00:10:17):
Right, they're like at 4%. I was looking at that list.

Matt Mullenweg (00:10:20):
They're around 4%, yeah.

Lenny Rachitsky (00:10:21):
That's unreal.

Matt Mullenweg (00:10:22):
It used to be open source was the top three. Unfortunately, Jula and Drupal have fallen behind, and so now it's like Shopify, Wix, Squarespace are the top ones but WordPress is still, because we have this flywheel of open source community, its movements, any open source like Linux or Apache or Wikipedia, it has some positive flywheel effects when it takes off.

Lenny Rachitsky (00:10:48):
Awesome, okay. And then there's a few other things you didn't mention, I want to get to this later, but I'll just mention now, you guys own Tumblr, you bought Tumblr, which I don't think a lot of people necessarily know.

Matt Mullenweg (00:10:56):
I'm sorry, I forgot to mention that, Tumblr.

Lenny Rachitsky (00:10:58):
We're going to get into that, yeah.

Matt Mullenweg (00:11:00):
Yeah, running a social network is definitely the hardest thing I've ever attempted. I thought we knew what we were doing because WordPress ran so much of the web, we dealt with, I thought, every content moderation thing you could ever deal with, but social networks are a whole other ballgame.

Lenny Rachitsky (00:11:15):
Okay, a couple more fun facts before we get into some other stuff I want to chat about. Fun fact number one is you were super involved in the Bay Lights project. I didn't know this. For people that don't know what the Bay Lights, if you're in San Francisco you definitely know what the Bay Lights project is and I'm sure you love it, for people that don't know what this is about, what is this project and how have you been involved? Why have you been instrumental in to make this a thing?

Matt Mullenweg (00:11:37):
Bay Lights, there's two famous bridges in San Francisco, the Golden Gate Bridge, which is kind of the iconic one, there's actually the Bay Bridge, which is the workhorse of San Francisco. It's one of the busiest bridges in the country. And it's really beautiful from an engineering point of view. And so kind of a vision between Ben Davis and artist Leo Villarreal, who's an amazing light artist, actually who started Burning Man was to put, gosh, I forget the number, I think 18,000 LEDs on the side of the bridge on all the cables and create this really beautiful, gentle kind of algorithmic light piece, light art piece.

(00:12:18):
And yeah, Ben Davis was dating an artist friend of mine and we were over and having drinks on my patio and we were looking at the Bay Bridge and I had this kind of thing where there's some lights at the top of the Bay Bridge and I was like, "Oh, wouldn't it be cool if those lights were Christmas lights and they could do patterns or something?" It's the lights to keep planes from hitting it. And I was like, "Oh, you could program that." He was like, "Yeah." It was almost like the Social Network thing where a million's cool, but a billion would be really cool. He was like, "Yeah, that would be cool, but what if we put the whole side of it?" And so I was like, "Oh, cool," and sort of made an angel investment in that thing. They hadn't raised anything or had, I don't even think an entity at that point, but I was like to get you started, I forget what it was, 100 or 150k so I gave them that first bit and then it kind of blossomed into a thing.

(00:13:07):
And then sort of fast-forward, I don't remember the exact timeline, but they were kind of at a final bit of fundraise and they weren't able to close that last bit and I actually mortgaged my condos and donated the last million, million and a half to finish out that project. The Bay Lights were online for 10 years. The technology degraded, and so the environment's very harsh. So actually we just completed a fundraise and are reinstalling the Bay Lights. They're calling it Bay Lights 360. So now it'll be both sides of the bridge, it'll be visible from also Oakland and the Treasure Island because the first version, the city was very worried about the drivers seeing the lights and it might distract them so we had to angle them so that you could only see it from San Francisco, which was a compromise we didn't love because we love the East Bay and everything else like that too. So new version is coming online hopefully later this year in the fall. And also that turned into a nonprofit called Illuminate, which I'm on the board of run by Ben Davis, who I mentioned previously, that does cool public art stuff around the city. So they're responsible for the Grace Lights, all the JFK Boulevard stuff where that has some murals and the beer garden and all the chairs, that's all Illuminate. So their thing is radical public art. So it's like art that needs to be free and accessible. And I think that's so important for San Francisco. We have great institutions know the SF, MoMA, the Opera, etc, that have huge budgets like 100 million a year and Illuminate literally one 10th of that has created something that millions of people can enjoy.

(00:14:40):
And I like to think that anyone along the Embarcadero, you might be going through a tough time, obviously we have people who are struggling with mental health and homelessness and everything like that, but maybe seeing a little bit of art can help raise your soul a little bit. And that's how I think about philanthropy as well. You need to work on the base issues, the fundamentals at the bottom of Maslow's Hierarchy of Needs, and then you also have to work on the things that raise your soul a little bit, so arts. So I like that barbell approach to philanthropy.

Lenny Rachitsky (00:15:13):
Elon has a great quote along those lines, "You can't just work on solving problems all day, you need something inspiring to think about and to work towards." First of all, thank you for doing this. If you live in SF, you're like, this makes the city better, just having this around. I didn't realize you were involved in helping come up with the idea itself. I know that you did mortgaged your house to make it possible.

Matt Mullenweg (00:15:32):
I can't take any credit for the idea, I was exposed to it. I had an adjacent idea and they had a way cooler one with a real artist and everything like that. So I was just happy to be there. It's like being an angel investor, you can support the entrepreneurs and the people who truly do it.

Lenny Rachitsky (00:15:49):
Yeah, okay. And the other funny thing you said is about they were worried about the angle of the lights distracting people. What's funny is when I drive across the bridge, you can only see it when you're driving towards San Francisco looking backwards. So I'm looking in my rearview mirror or in the mirror turning around to the kind and it feels more dangerous, the lights shining in my face.

Matt Mullenweg (00:16:07):
They call it impossible works of art. There were like 13 agencies that had to sign off, they were worried the lights would distract birds or seals or environmental reviews, and it was really a lot of public bureaucrats and to make that happen, there was 20 places where someone could have said no and it never would happen. So it's very inspiring to see the city come together.

(00:16:31):
Also in San Francisco, I feel like is entering new chapter right now, going from the doom loop to the boom loop. I'm a big believer in the city. So much innovation has come here from food, the burrito, fortune cookies, all these sorts of things are from San Francisco to obviously all the tech innovation that we're all familiar with. It's kind of the city of the future and I don't know what it is in the water from the '60s until now, cultural innovations, things that happen and influenced the whole world, Burning Man, Grateful Dead, et cetera. That all starts in San Francisco. So it's exciting to be here.

Lenny Rachitsky (00:17:03):
Let's set the so back, as they say on Twitter. Okay, someone very close to you told me that you're an excellent rapper. I'm not going to ask you to rap, but if you ever want to answer any questions in rap form, feel free.

Matt Mullenweg (00:17:17):
Oh man, that would be fun. I've dreamed about being able to do a Q&A and rhyme, but I don't think I'm that talented.

Lenny Rachitsky (00:17:26):
Planting the seed, I'm planting the seed. So I want to get into all the drama there in this world and right now, but I want to first lay the foundation of how you got into this and where this all came from. So let's talk about just the origin story of you and open source. More than half of your life, you've been working on open source, you've been working on WordPress, specifically WordPress is such a core community within the open source. What was kind of the origin story of you becoming obsessed and, I don't know, open source-pilled?

Matt Mullenweg (00:17:56):
I was a broke kid in Houston, Texas, and my passions were jazz. Houston has actually amazing music programs in the public schools, and so I was very fortunate to go to some of the best civil arts programs, including my high school called the High School for Performing and Visual Arts, where Beyoncé went, Robert Glasper, amazing folks went there. And so music was a big part of my life, and actually economics. So I had this fun teacher, Scott Roman, who participated in our school in the Federal Reserve Challenge, which was run by the Federal Reserve that sets the interest rates and backs the national banking system and everything like that, has this competition for high school students. It ended up being the first academic competition this art school ever won. And yeah, first year we kind of didn't get that far, second year we went all the way to nationals so I got to meet Alan Greenspan, Ben Bernanke was our judge, went to DC. So that was very, very exciting.

(00:19:01):
And so being exposed to us having a great liberal arts education, the ideas of Frederick Hayek, Agnes Smith, Alexander Hamilton, Ben Franklin, Thucydides, all these sorts of things, that philosophy really influenced me. And combine that with that, music lessons were expensive, so we couldn't really afford them, so I would barter and trade. I'd build websites for local musicians and exchange for lessons. So these websites, I would start to put software on forums or different things and that kind of exposed me to open source. So my father was also an engineer, he worked for oil companies and things, but his world was all Microsoft, it was all proprietary. And I always kind of grew up in early days of the internet, so was Slashdots and Jeffrey Zeldman talked about web standards and all these things are really kind of the social milieu and zeitgeist that I grew up in.

(00:19:56):
So combining all this philosophy I studied, it felt that open source was actually the most important idea of our generation. If the founding fathers were around today, I think they would be open source advocates. If you think about it as more and more of our lives are influenced and actually controlled by the software we use, if we don't have fundamental freedoms attached to that software, we're not truly free.

(00:20:24):
So WordPress is under license called the GPL, which has four freedoms, the freedom to use the software for any purpose, so we can use it for anything, whether I agree with you or not, the terms of service is you could do whatever you want with it. The freedom to see how the software works, open up the hood, see how it works, see every line of code, you can audit it. The freedom to change it is the third freedom. And then finally the freedom to redistribute those changes so you can share them. And the GPL has a fun little hack where if you share them, you have to provide those same freedoms to who you share it with. So it's called a viral open source license as opposed to the MIT license or some of the others that aren't.

(00:21:03):
So yeah, just kind of decided that this was what I was going to devote my life to. And so that became getting involved with some early open source projects, WordPress was actually a fork of abandoned open source project called B2. So the code base actually started was something that was already out there that I was a user and contributor to kind of volunteer on the forums and contribute code. And then when it was abandoned, myself and Mike were one of four or five different forks that started that, picked it up and tried to continue it for our own use and then later for our larger community.

Lenny Rachitsky (00:21:36):
It feels like a lot of people are coming around to exactly your worldview in, say, I was just watching a video of Jack Dorsey talking about how we're just controlled by algorithms and we don't know how they work and we are not in control of our lives. Have you seen that video?

Matt Mullenweg (00:21:52):
No, but I actually love that. Also, some people who maybe made their first billion or whatever from proprietary software then come back and it's so cool to see folks like Marc Andreessen or Bill Gurley be huge advocates for open source. I actually remember one of my early meetings with Andreessen Horowitz, Marc Andreessen. I didn't realize that at the time, Tony Schneider and I were sort fundraising and Marc really grilled us, he's like, "How can you build a business on open source? How can you be remote and distributed? Look around Silicon Valley, Google, Microsoft, Oracle, Sun, every great company has had an office. How are you going to build something that can change the internet with people all around the world?" And just had this long hour long debate and we walked out of that, I was like, "Wow, that was the worst meeting ever. They just hate everything we're doing."

(00:22:48):
And then the next day they were like, "Hey, we're interested." I was like, "What happened?" I didn't realize that he had this idea where he wanted to attack the ideas and see how we defended it was how they battle tested things. I guess kind of like a Microsoft culture or whatever where you really grill the idea, I just wasn't familiar with that. But it's so cool now that some of these folks that I've learned so much from are such good advocates for open source.

Lenny Rachitsky (00:23:15):
Yeah, it's so interesting. I just had the Community Notes team on the podcast, and that's an amazing example of open source, Meta is adopting it from Twitter/X. Speaking of open source, one of the interesting, maybe most common ways people hear about open source these days is AI and AI models, and there's a couple areas here, one is you wrote this really interesting post where you talk about how Meta talks about Llama as an open source project, but you called it a false prophet. What is it about Llama that isn't open source? What are people missing when they see Llama and they're like, "Oh, Meta is amazing open sourcing everything."

Matt Mullenweg (00:23:52):
Llama, you can obviously download and run locally and all these sorts of things, right? You don't have to use their SaaS service. However, there's a clause in it that says if you're above a certain threshold of monthly active users...

Matt Mullenweg (00:24:00):
... as if you're above a certain threshold of monthly active users. I forget what it is. It's big. It's like 750 million, so it's pretty high. You need a license from them. And so that does not give you the freedom to use the software for any purpose. If at some point you have to ask for permission, you're kind of at the whims of this company who you might be aligned with or you might be an enemy with. And also, how do you define that? So, for example, on WordPress, our products don't have 750 million monthly active registered users, but we reach billions of people per month in terms of visitors. So, is that defined? So, there's just ambiguity there. So, I still think what they've done is amazing and I like that they're releasing it. I was very confused for why they insist on calling it open source because they...

(00:24:54):
Actually, Meta has been a huge open source contributor. React. They've had incredible improvements to the PHP engine, which we benefit from a lot. So, they're actually a big open source contributor. I think Mark Zuckerberg really understands and loves open source too. My best guess now, I don't have any inside information here, but I think they're calling it open source because there's some European regulation about open source versus proprietary AI models. So, I think it might be a weird regulatory thing because clearly they understand this isn't open source. When I wrote the blog post, I was just kind of confused, and thought, "Oh, maybe if I get this message out there, they'll change." And then when they didn't, I was like, "Oh, there must be something else going on. I think it might be this regulatory thing." We were actually a big part of, actually many, many years ago, I think it was React that they were doing something with a licensing or a patent restriction on, and the WordPress community actually got Meta to change that and reverse something they were doing to lock it down.

(00:25:53):
So, I consider my role as an open source advocate to actually be my primary thing. And it's very much my life mission. I hope to work on WordPress the rest of my life, but also just open source in general. I also support Drupal and Joomla. Anything else that's open source, I'm going to be a supporter of because I think when people choose that versus proprietary software, we're increasing the freedom and liberty in the world. It's incumbent on us to make open source, to make a better user experience, to make a better product so that people choose it, and then the world becomes more free, not less free.

Lenny Rachitsky (00:26:36):
It also feels it's important to you to, I don't know, white open source washing, like avoid people using the term when it's not true. And it's interesting in this case, that the thing that makes it not truly open source is the limit. There's a limit where you can no longer use it the way you want. Is that the issue?

Matt Mullenweg (00:26:53):
Yeah. And there's actually an open source OSI. There's a formal definition for what makes an open source license. And there's actually many dozens of open source licenses, and sort of public domain licenses and other things. So, it's also their stance that this is not an open source license.

Lenny Rachitsky (00:27:15):
Something else that I think is really interesting when it comes to AI and open source, you wrote about this and it blew my mind, such a good point, that the code that these models were trained on was open source code because that's all they have access to. They don't have Windows code, they don't have Shopify code. And what a cool, I don't know, another success story slash... I don't know. I guess, how do you feel about that, that all these AI models are trained on code you wrote in open source community?

Matt Mullenweg (00:27:43):
That's beautiful. It's one of the safest things to train on, right, because the license of open source very explicitly allows that. I also like to think about I have some window where my creative output is useful to society. And if you fast forward like 50 or 100, I do believe that the utility for proprietary software eventually approaches zero. When we're sending people to Mars, the operating system of the rockets and the devices and everything like that is not going to be built on the Windows NT kernel, as amazing feat of engineering that that proprietary kernel is. It's going to be built on an open source kernel, Linux or BSD or something like that. And so if you want to be part of something that sort of becomes the fabric of humanity's foundation, like things that allows a Cambrian explosion of things built on top of it, a renaissance of ideas, you want to be involved with open source.

(00:28:38):
And so I really hope that more and more people... I'm a little bit of an evangelist here. I'm a missionary, where I really want to encourage more and more people to consider at least making part of their time, even if just a few hours a week, contributing to open source because you could be part of something that is a huge impact. And it's fun, especially if you're a younger developer or designer or PM or whatever, you can't walk up to Facebook and change your home page or say, "I'd like to change this feature," but you could come to an open source project, some of which have hundreds of millions of users. You could go to WordPress or, gosh, Bitcoin.

(00:29:20):
Or there's all these things are open source, Chromium, Firefox, and you could actually change a feature or project management things or change the design or improve it. And that's I think really, really special. And sort of the thrill for me of knowing that code I wrote is now executing millions of times per seconds and millions of servers around the world, that kind of thrill, that high is, when I first had my first open source contribution, such a thrill. And I've been sort of chasing that and enjoying that ever since.

Lenny Rachitsky (00:29:53):
Say someone wants to actually do this, where do they go? How do they do this? Do they just pick up a project, go to WordPress. org and here's how you contribute? What's a next step there?

Matt Mullenweg (00:30:03):
Yeah, pick a project that you use or like. That's obviously a nice one. For WordPress, we have this... It's called make.WordPress.org. That's where we make WordPress. And there's different groups, there's accessibility, there's design, there's the core code, there's plugins, there's all sorts of ways. So, really whatever your talent is, there's people who translate, there's people who do support, there's people who write documentation, there's people who organize events, so whatever you feel like your talent in the world is either that you have or that you want to cultivate. I learned how to code while building WordPress basically. I didn't have too much formal training there. So, it's a great way to [inaudible 00:30:48] your skills as well, and work with some of the best developers and others in the world.

Lenny Rachitsky (00:30:53):
This also made me think about AI agents are coming around, Devin and all these AI driven coding agents. Do you have a prediction at when most of the code contributed to the open source projects will be Devin and AI agents such type projects?

Matt Mullenweg (00:31:10):
I think Google talked about 25% of their code or characters committed are now sort of AI-assisted, and they're probably on the bleeding edge. I don't know how much of WordPress's code right now is AI-assisted or something like that. But I think over the next five years it definitely approaches maybe a majority. And I'm actually very, very excited, so one of the big challenges that we have as a very open platform is we have this open plugin and theme architecture, so the 60,000 plugins and themes and the way WordPress works is these plugins and themes can modify every single part of the code, so you can really customize everything. However, many of these plugins and themes don't have the same sort of robust security and review process that core has. So, that's where when you hear about security issues with WordPress, it's very rarely in core anymore.

(00:32:03):
We haven't had a remote exploit, knock on wood, it's like I think five or six years or something, but in the plugins it can be somewhat more frequent. And so one thing I'm very, very excited about the next year or two is actually more automated scanning because obviously that code basis is so many tens of millions, maybe over 100 million lines of code at this point. It's impossible for humans to review that, so we kind of rely on developers to review that and manage. And of course, we have bug bounties and everything do that, so when things get reported, we fix it quickly. But I can't wait for more automated scanning there, and I think that could vastly upgrade the security of open source. The other thing that's really exciting is right now you see people building apps and stuff and it's just sort of custom generated code, but I think the next generation of these models or sort of the next layer there is because...

(00:32:54):
As everyone knows, just writing the code is just one part of it. It's maintaining it that really becomes the life cycle of it. And Stewart Brand's new book is all about maintenance, which I'm very excited about. He's publishing, I think, with Strike. And it's actually kind of open source. He's open sourcing the book, so you can see it being written online. But anyway, to go back, I think that if... And they're starting to do that, is when the open source models you say like, "Hey, build me a website." It actually installs WordPress, and then builds on top of that, and then customizes on top of that. Then you get for free that core engine that's always being audited and updated and getting passkey support or whatever the new things are sort of continuously. And then your custom stuff can be on top of that, which I think is actually a lot more powerful than building something proprietary or custom from the ground up.

Lenny Rachitsky (00:33:43):
I love this book concept about maintenance. My sister's partner has this quote that I've always come back to, "Life is maintenance." You basically... Everything you acquire and deal with... You get a generator for your house, you have to maintain that forever now. You get this backpack, okay, now you have to maintain this thing, keep it nice, nice jacket. Everything is maintenance. Everything in your life is just maintenance. And I wonder if that's what the book's about.

Matt Mullenweg (00:34:09):
Well, that's why I think technical debt is one of the most interesting concepts. There's so many companies as well that maybe have big market caps, but I feel like they might have billions or tens of billions of dollars of technical debt. You can see in the interface or how their products integrate with themselves through things. And I think about that a lot in our own company. We definitely have some products, almost a little embarrassed coming on because you have such great product people. And we have some variable quality around some of our things right now. If you check out Gravatar right now, I'm actually really proud of it. It's I think a really great user experience, very slick. But there's parts of... Well, I always say, "I'm the unhappiest WordPress user in the world," so there's parts of WordPress and WordPress.com that I'm a little embarrassed and ashamed of.

(00:34:52):
We have a really large surface area that we cover with relatively few people, and so there's some parts we haven't looked at in a little while that we need to get around to. And it's a big focus for us this year, is actually kind of going back to basics, back to core, and improving all of those kind of nooks and crannies of the user experience, and also ruthlessly editing and cutting as much as possible, because we just launched a lot of stuff over the past 21 years that maybe is not as relevant today or it doesn't need to be there.

Lenny Rachitsky (00:35:21):
That sounds like excellent work for this AI agent of the future that's coming soon. There's one other area I want to mine and that's community, community building, building this ecosystem that you've created around WordPress. It might be one of the most successful, biggest communities on the internet. I'm curious just what lessons you've learned about what it takes to build a successful community, online especially.

Matt Mullenweg (00:35:48):
This is probably influenced by economics and jazz. And economics is all about systems thinking. And what are the incentive structures of how you set something up? And then in jazz is all about collaboration. So, if there's something unique I have for your audience, I would say it's don't just build a product, build a movement. And to the extent that we've been successful, I think it's that we give people something to believe in, a philosophy, a worldview. Even silly things, like we had this tagline in the footer of the WordPress.org when we started, it's still there, it says, "Code is poetry." This idea that we're not just writing code, we're trying to create something that can have elements. We name every WordPress release after a jazz musician for the past 60 releases or so. So, those sorts of things bring a little art and soul and some fun into it as well.

(00:36:44):
It doesn't have to be serious all the time. I think they can give something to believe in and work on and aim towards that's more than just a paycheck or more than just the utility, the base utility of the software. So, it's not just the software, it's also like: how are the meetups? How are people getting together? What events are you running? Are there forums? How do people contribute? Is there office hours or town halls? I do a lot of Q&A. So, what are the things you're doing around the software that's allowing people to get involved, that's inviting contributions, that's allowing people to build on top of it? I've studied platforms quite a bit like Microsoft and others, so our whole ecosystem of plugins and themes is part of what's made WordPress so successful, and the moat that we have.

(00:37:33):
The core features of a CMS, you can kind of write with a few developers in a few weeks or something. It's not... It's basically CRUD operations, but to replicate those 60,000 plugins and themes, gosh, no one's done it. That's a huge moat. And proprietary services can create platforms. Shopify has a third-party ecosystem and things like that, but it's never a true platform. And a true platform, it's when your ecosystem makes more money than the core does. And so many times, whether it was the Facebook platform, I'm putting that in air quotes, or the Shopify platform, companies build on it and then they get the rug pulled out from under them because they're too successful.

(00:38:15):
And then the sort of thing you're building on decides, "Oh, we want that money or we want that growth." And they sort of change the API or remove your access. There's so many examples of this, especially on, I think, Facebook and Shopify and others, where people got too successful and all of a sudden they knock on the door and they say, "Oh, that's a mighty nice app you have there. I'd love to offer you some warrants where we own a bunch of your company or we're going to shut it off," or those sorts of things.

(00:38:42):
And again, you don't have freedom unless you're building on open source. That's why more and more companies and people are choosing... If they're going to build a business on top of something else, if you build it on an open source, you have that guarantee. Even if I grew devil horns and became evil and automatic decided to know whatever, WordPress would still belong just as much to you as it would to me. People can fork the code. They can still own it. They can still build on top of it. So, those things I think are really important.

Lenny Rachitsky (00:39:13):
What a segue to all of this drama that's swirling around you these days. I think a lot of people do feel like there's devil horns that have appeared, and so I'm excited to dig into this stuff. I find that every time you go on a podcast these days, if we don't get into this, everyone's just like, "Why is Matt not answering these questions?" Let's get into the hard stuff. So, I'm going to ask you some hard questions. For people that don't know what the hell's going on, they're like, "What are you even talking about?" or just have a sense something is swirling with WordPress and, Matt, I don't know what's going on, what's just like the high level overview of what's going on?

Matt Mullenweg (00:39:48):
So ,to set it, you can get WordPress from WordPress.com or us, but also you can get WordPress from dozens of other hosts. The biggest in the world are like GoDaddy, Hostinger, Newfold. It's not the biggest, but it is in the top 10 or something. It has about 700,000 WordPress installs. There's a company called WP Engine. In 2019, WP Engine started as very WordPress oriented and they contributed a lot to the community and everything like that. They were very respectful about distinguishing themselves from core, so people really realized it wasn't officially associated and everything. But in 2019 they got bought out by a private equity firm called Silver Lake. And anyone who follows business, when private equity buys something, there's some the good ones, but there's also many, many stories about how they can really hollow things out, really optimize our profits, become user hostile.

(00:40:45):
Actually recently read a story where one of the reasons there was a shortage of firetrucks these LA fires was that the fire truck manufacturers have been rolled up by a private equity firm, and they've been raising prices and their supply constraint and things like that. So, there's literally a shortage in firetrucks right now because of private equity. And of course, if you look at healthcare or other things, there's so many examples of where private equity can really, I think, be one of the darker parts of capitalism. So, since 2019, WP Engine has kind of changed a bit, and they really stopped contributing to core and they started using the trademark in a way that was very confusing in the marketplace. And particularly in the past year, year and a half or so, we're just getting lot... I get a lot of support for requests for WP Engine.

(00:41:36):
And when we do surveys, we'd find that 20, 30, 40% of people thought they were officially associated because how they were using our logo and presenting the brand and everything like that was very confusing to people. And as you know, if you don't protect a trademark, you lose it. And also the version of WordPress that they were offering actually wasn't our core vision of the functionality of WordPress. So to save money, they were actually turning off features like revisions. So, a cool part about WordPress that... actually one of my favorite features, is every change to every single post or page is saved forever, just like Wikipedia. So, if you make a mistake, you can always undo it. And of course, as building a great product, that sort of user safety of an undo is so critical.

(00:42:19):
Now, obviously you have to store these revisions, so it takes up more database space. Now, it's trivial, it's megabytes, so on modern databases is not that big a deal. But to save money, they actually turned us off, so they broke the undo feature in WordPress to essentially save money. And so you have this thing where they're offering something called WordPress. I think I refer to it as a bastardized hacked up version of it. It's diluting our brand, and then also people think it's official. So, even close friends of mine were like, "Oh yeah, I signed up for this thing. I thought I was supporting you."

(00:42:49):
And it's came to a head. So, past 18 months they've also... We contacted them and said, "Hey, you need a trademark license or something if you're going to use this or change how you're doing things," and tried to negotiate something and had many different term sheets over the months offered and different things, and they just kept stretching it out. And I was like, "What's going on here?" And I think part of what was going on is last year they tried to sell the company. So, private equity usually holds things for five to seven years, so they were kind of five years into this. They tried to shop it around and sell it. They weren't able to find a buyer.

(00:43:25):
They said, "Well, they don't have any IP, and it feels like they're using your trademark, so they're going to have trouble with you. They don't have a license and things like that." So, while they were negotiating with us, it appears they were also preparing this lawsuit against us. So again, I've been very fortunate in my business career that we've invested in dozens of companies, we've acquired lots of things, by and large, 99% of the time people I've dealt with in business have been ethical, straightforward, honest. I haven't really faced any baldfaced lying or duplicitous behavior. Very, very rarely people who just say one thing and do another or are fraudulent in their behavior, but I think that was happening here.

(00:44:17):
And so I also just wasn't prepared for it. I was thinking I was a little naive and kind of didn't realize what was going on for a while. So, it came to a head, and at WordCamp US in September, I was like, "Okay, well, if you're still not going to even agree to negotiate, I'm going to give this presentation about how I think both private equity has messed up a lot of open source projects in the past, and how in particular, [inaudible 00:44:46] has done some very bad or evil things." And they were like, "Okay, go for it." So, I did the presentation. I think it was on a Thursday or a Friday. Kind of spicy. People were like, "Oh, can't believe he did that."

(00:45:00):
And then on Monday they launched this with Quinn Emanuel, which is kind of the baddest, nastiest law firm, it's like who Elon uses when he sues people, launched this big multimillion dollar lawsuit against both me personally and WordPress.org, so the WordPress community and Automattic. And also they're spending millions of dollars a month on both lawyers and PR. So, they're doing... If you read... Oh gosh, who was the celebrity that they were recently talking about this, like dark PR stuff where they're boosting things on social networks?

Lenny Rachitsky (00:45:35):
Oh, Blake Lively and-

Matt Mullenweg (00:45:37):
Blake Lively, yeah, yeah.

Lenny Rachitsky (00:45:37):
... the other guy.

Matt Mullenweg (00:45:38):
So, all that stuff is happening, so there's... And I warned people. I think in the presentation I say, "Hey, there's going to be a smear campaign against me." And internally in the company, I was like, "Hey, they're going to dig up everything that's ever happens. Anything bad anyone's ever said to me is going to all of a sudden become a news item." And that has happened. It's been true. So, right now there is a portion of the internet that does think I have devil horns and everything. Fortunately, this is not my first rodeo. I know a lot of people think like, "Oh, Matt was nice for 20 years, and then got mean." But one thing, if you're really open and open source, sometimes you have to stand up the bullies, and you have to fight to protect your open source ideals.

(00:46:19):
Otherwise people could take advantage of it in a way that ultimately can destroy everything you've created. So, this is probably the fourth time the internet has decided I'm the main character or really evil. And the previous ones we don't remember anymore. It's Hot Nacho or the Easter Massacre of Themes or these are the things that aren't even on my Wikipedia page anymore, but those seemed like really big deals at the time.

Lenny Rachitsky (00:46:43):
Those are your incidents. Those weren't like historical battles.

Matt Mullenweg (00:46:46):
No, no, these are things that, yeah, I was involved in.

Lenny Rachitsky (00:46:48):
Cool names at least.

Matt Mullenweg (00:46:49):
Including some things I had screwed up, like Hot Nacho was definitely a screw-up on my end very early in the WordPress side, but...

Lenny Rachitsky (00:46:55):
Wow. Okay, I'm not going to follow those threads, but those are great names.

(00:46:59):
This episode is brought to you by Loom. Loom lets you record your screen, your camera, and your voice to share video messages easily. Record a Loom and send it out with just a link to gather feedback, add context or share an update. So, now you can delete that novel-length email that you were writing. Instead, you can record your screen and share your message faster. Loom can help you have fewer meetings, and make the meetings that you do have much more productive. Meetings start with everyone on the same page and end early. Problem solved, time saved. We know that everyone is in a one-take wonder when it comes to recording videos, so Loom comes with easy editing and AI features to help you record once and get back to the work that counts. Save time, align your team, stay connected and get more done with Loom. Now part of Atlassian, the makers of Jira. Try Loom for free today at Loom.com/Lenny. That's L-O-O-M.com/Lenny.

(00:47:59):
So, you mentioned this talk you gave at WordCamp, and you said at the beginning of the talk, like, "I'm-"

Lenny Rachitsky (00:48:00):
... at WordCamp, and you said at the beginning of the talk... oh no, afterwards you were like, "I was really nervous to give this talk," and obviously you can see why. Just what finally convinced you this was time? Was it just to go, as you described, scorched earth nuclear? Was it like WordCamp is coming up and this is the moment to go public with this? Was there something else that kind of crossed the line?

Matt Mullenweg (00:48:24):
It was a unique opportunity because we were essentially saying that, hey, WP Engine isn't going to be allowed to sponsor WordCamps anymore. They're not going to be a... Because we had, again, up to that point really done everything to bring them in and have to be part of the community. So I really had to also explain to our community, hey, why we're going to be excluding this company that a lot of people saw as doing good. If you go to the WP Engine website, they have whole pages about how much they contribute and give back and how they... they do kind of greenwash or open source wash a lot of what they do. So all their marketing branding was around this positive stuff, and so I was like, "Hey, we need to just explain this case."

(00:49:03):
But yeah, again, my defaults and how we've worked with, by the way, every other company in the WordPress space, many of which are much, much larger and make sometimes billions more in revenue than WP Engine, is collaborative. So if there's a trademark violation, usually it's not even lawyers get involved. It's just like there's a email, we have a conversation, we do a call, we talk about it. That's how things get resolved and that's my default. I'm a lover, not a fighter, and that's why this thing doesn't happen very often. I like to say that, yes, if WordPress community or whatever was doing this like every year or every couple months, yeah, you should worry about it, but it kind of happens every like 10 years.

Lenny Rachitsky (00:49:46):
So if I could mirror back the issues that you ran into, and I want to go through this a little bit more, the problems you had with WP Engine in this case. One is they were using the trademark both WordPress and WooCommerce without license, and they're just abusing it, confusing people. A lot of people thought WP Engine was actually Automattic and WordPress official. They weren't contributing to the project. They were just making basically a bunch of money and not doing the work off this company they bought and they're just kind of hollowing it out as you described. And then they're also cutting corners, making the product worse, and that kind of reflects on the whole brand of WordPress.

Matt Mullenweg (00:50:22):
That's a great summary, yeah.

Lenny Rachitsky (00:50:24):
Awesome. I'm curious just which of those three, or is it something even else that most bothered you about this? What's just like, "This is the thing that's eating me"? If I had to guess, it'd be damaging the legacy potentially of this thing you've worked on for most of your life. Maybe it's that, maybe it's just taking advantage of the community. What's the thing that you think is the root of this, just like, "Just this needs to stop"?

Matt Mullenweg (00:50:50):
Well, I guess the one thing I'd add to your list was as this was happening they were pretending to good faith negotiate. And in fact, at one point the executive, we were talking about her joining Automattic and running WordPress out of Oregon and when she thought... the VP and she going to sell, she was thinking about what was next. So yeah, a lot of this stuff was, I think that duplicitous behavior also kind of forced us to an edge more than even those other things that you mentioned. There's lots of companies that don't contribute back and it's not as big a deal. But yeah, the legal issue was definitely the trademark thing. So what pushed it to the edge? I think just the magnitude of the issue. They would refer to themselves as WordPress Engine in client meetings and other things. They were very cavalier about how they would imply their association with the project.

Lenny Rachitsky (00:51:46):
Obviously, as you can tell on socials, a lot of people are just really upset and a lot of people blame you. There's just, like I said, every time you're on a podcast or on Twitter, people are just like, "Matt, what about this? Why this sucks? Why are you doing this?" And I want to go through some of those things, but just not many people go through... I think you were like a hundred percent beloved hero of open source and internet and now you're in this... a lot of people don't like you. Just as a human, just what is that? How do you work through that? How do you deal with that? What's that been like?

Matt Mullenweg (00:52:17):
If you were kind of inside baseball with WordPress, it's actually a lot of people who have been unhappy with me over the years, and when we introduced something like Gutenberg, people hated it. Actually when we introduced a visual editor, people hated it.

Lenny Rachitsky (00:52:29):
You've had practice.

Matt Mullenweg (00:52:30):
These are huge controversies in the WordPress history. There actually hasn't been a fork or WordPress around all this latest stuff, but there was when we introduced Gutenberg. It's one called ClassicPress where people actually forked the software. So how I would describe it is previously like 1% of the world thought I was terrible, and now I feel like it's up to like 4 or 5%. So it's still not the majority, but as you know, something negative you feel seven times more than something positive. And when people are angry with you, it's kind of like restaurant reviews or whatever, they're more likely to leave a bad review than a good review.

(00:53:14):
The people who WordPress, 98% of all the core developers have stayed and contribute and are working on the next version and are supportive and all these sorts of things. And part of the reason these folks are so good is they don't spend all their time on Twitter and Reddit arguing with folks, and also the arguments could be... they're very frustrating because people don't engage in good faith. They don't really change their mind when new facts are introduced.

(00:53:43):
And so I've done my best actually because from the open source side I'm really used to engaging with things, and I think that's been one thing I've learned from this is in some forums it doesn't matter how you engage and especially if you have bots or other things running there. I'd leave comments on Reddit and immediately get like 40 downvotes. I'm like, "Hey, this is a article about me and I'm adding a fact to the thing. Why is it getting downvoted? This is very relevant to the discussion." But it's literally hidden. So when you see that thread, you'd have to click like three or four times to see the comment I had left, and so it can really change the perception. And then when you read these things, I think it's just very human nature. Even folks very close to me, if you read a thread and it's all super negative, it's hard to not be influenced by that because we're social creatures.

Lenny Rachitsky (00:54:36):
100%.

Matt Mullenweg (00:54:37):
Now the good news is I've had lots of credibility weighted support from people like Marc Benioff or other open source leaders or the core people in WordPress, Matias, Mary Hubbard, all the core committers. The international community actually, like just in Japan, they don't care about this stuff. So these are actually, if you look by number of commits and lines of code and everything like that, the folks who actually are most crucial in WordPress. So I feel like that's been a good balance as well for me because there are days where I'm like, "Gosh, am I an idiot?" or it could be really down reading all these things. So that is part of what allows me to balance and get back to that sort of positive, optimistic space that I think you need to be in to do great software and great work.

Lenny Rachitsky (00:55:27):
Yeah. The internet can be brutal. Let me go through a couple of specific things that people pointed out because I think you've been on a lot of podcasts and people haven't asked you these questions and I think a lot of people are just like, "But, Matt, what about this? This is really bad." So let me just ask you a couple of things here. One is there's just like a frustration in the community around the instability that this has just caused in the WordPress community. I'll read you a couple quotes. "Real people are receiving fewer projects on WordPress because C-suite are seeing WordPress as unstable because of this feud, and I work at Enterprise and we're very concerned about the stability of this platform and our projects." Just thoughts on that and the impact that it's had on the community.

Matt Mullenweg (00:56:05):
Yeah, I think this is until this gets resolved... which by the way I hope it is soon. I think there's no business reason for this to continue. I really hope that they come to a settlement or something. We're ready. They could end this tomorrow if they wanted to. WP Engine could. We can't. We're just defending right now. So it's really incumbent on them. All of our competitors, by the way, are like, "Great. WordPress, the king on the hill, all of a sudden we can use this." And so there's also not just from WP Engine, but also from all the competitors to WordPress, and all the people who would love to capture some market share, they're really leaning into this. So I've seen white papers, I've seen all sorts of things where people talk about this.

(00:56:49):
We're actually in the next couple of days going to publish something really cool on the WordPress.org blog though that shows if you actually look at the numbers, like the activity, number of commits, plugin updates, downloads, installs of WordPress since September 20th when this all started, it's quite healthy. And so I'm not saying that there isn't examples of where someone lost a project or something like that. I'm sure it's happened. It's the internet's big. WordPress has so many millions of users and developers and everything that you're going to get some example. But by the numbers things are actually quite healthy, and in some ways it's not that there's no press is bad press, it's raised the awareness of WordPress quite a bit. So people who haven't talked about WordPress in years are now like, "Oh, Let's talk about it." And so a little bit of drama I think, I wouldn't do this all the time, but a little bit can be a good thing.

Lenny Rachitsky (00:57:39):
Okay, so one of the most common frustrations I've seen on the internet, people complaining is around the trademark. I don't know all the details, but my understanding is there's kind of a... you moved the trademark to be owned by the foundation and Automattic is exclusive rights to use the trademark. And I think people are like, "Oh, I thought it was the foundation owned it, but maybe Matt still owns it and then you're trying to monetize it through this agreement with WP Engine." Is there anything you can share there that'll make people feel and see your side of the story?

Matt Mullenweg (00:58:10):
Yeah, this is totally fair because it's complicated, but people are saying this has been private. This has all been very public and documented on the internet from the beginning. So WordPress.org has always been me personally, and I think because it's... part of the reason we started there is . com was not available when we started. So that's why we started on the .org and things like that. But I think people also assume .org means nonprofit or something, and that's sometimes true but it's not always. It's not a requirement of the .org domain. Then when I founded Automattic and when we did register the trademark that actually was registered under Automattic. So it used to be, for the first five years of the project or whatever, that Automattic just owned everything outright. And again, I had investors and the board and that was under the control of that.

(00:59:06):
Now, as Automattic became more successful I was able to consolidate some voting rights and other things and at least later advocate. Also remember, I was like 21 when all this was happening, so I was not maybe the most savvy about legal stuff or didn't always have the best advice. So later as I learned more, I was like, "Oh, I want to actually take this out of the company and create a nonprofit." And so we ended up creating a nonprofit. Now the rules around 501(3)(C) nonprofits run the IRS are actually very strict. So that's also something as people assume, it's like, oh, doesn't the nonprofit run the software, and we applied for that originally and it was denied by the IRS.

(00:59:47):
So we actually weren't able to put WordPress.org or the software itself under the nonprofit, but we were able to have sort of an educational purview. So what was eventually approved was sort of running the meetups and other things for WordPress, doing educational stuff. We sponsor a lot of learn to code or running workshops in other countries. We have this cool thing called do_action where we'll do a weekend where we take a bunch of nonprofits and build websites for them and stuff like that. So the nonprofit does a lot of exciting things there and then also negotiated with the investors and everyone at Automattic to actually put the trademark under the foundation.

(01:00:31):
Now the compromise there was that Automattic at this point is running WordPress.com. So to continue running that, which at the time had already tens of millions of users and everything, it needed a commercial license. And so the compromise is that the foundation would kind of own the trademark and license it out for non-commercial purposes. I had a license to run WordPress.org because obviously I need that. And then Automattic would retain the commercial license and the ability to sub-license that, so to sell that to others. So this was kind of the grand compromise and create this tripartite structure. I was very inspired by the three branches of government. So there's sort of power in each of those that I think sort of checks and balances each side of it which is on purpose.

Lenny Rachitsky (01:01:23):
Wow. Okay, I get why it's complicated. I get why people would be confused. This makes me think about OpenAI had a really strange structure and that got them in a lot of trouble, and it feels like when you're 21 you're like, "Oh, this makes a lot of sense. What a great concept we've come up here," and then all this complexity just adds to a lot of confusion around what's going on. So thank you for addressing that. Another, there's a kind of related question I've seen a couple of times is just why don't you let that .org be run by a community. Why not just give that up to someone else and not just you that's there?

Matt Mullenweg (01:01:53):
Yeah, and the frame of that question is kind of interesting because it implies I'm the only person making WordPress which is obviously not true. If you look at the daily commits and activity and everything, it is run by the community. So it's hundreds of volunteers every day that are actually doing the day-to-day work and making the daily decisions and everything happens. So there has been a radical delegation. However, there's ultimately a hierarchy, and I'm the CEO, so I'm like the final final decision-maker.

(01:02:24):
And so I think what people advocate for around this governance point of view is like, okay, well, install a board on top of you that ultimately makes decisions for the product or things like that. And there are other open source projects that have this structure. None of them have been successful as WordPress. So I think your audience in particular, is great software ever created by committee or does it more often reflects a vision of a leader or something that can allow us to... and I think particularly WordPress not just remaining relevant but actually accelerating growth over huge technological shifts over the past two decades.

(01:03:12):
When we started there was dynamic web apps or DHTML or JavaScript wasn't really a thing, and then the social web and then iPhones and then all this sort of stuff that's changed over time, and we've surfed a lot of these technological changes which is very, very hard to do. Most products do not remain relevant over multiple generational changes like that, and that's been because sometimes we've had to make very unpopular decisions. Gutenberg is a huge part of why WordPress is relevant today, and it's actually an open source project we do. It's the block editor. It's actually bigger than WordPress because it's not just used on WordPress, it's used on every WordPress site, but also like Tumblr, other people. I would actually love if Squarespace or Wix adopted Gutenberg. It's meant to be like a really open source framework.

(01:03:56):
But anyway, if we had voted for whether we should do that or not, everyone would've voted against it or the majority would have. It was really a few core people of us in the community, Matias, myself, other core contributors, Ella, Andrew Ozz, that said, "Hey, this is the future and it's going to take 10 years to do and it's going to be a long bet. It's going to suck for the first three or four years, and so everyone's going to hate it in the beginning."

(01:04:20):
But then later with iteration, we've had I think now 200 releases of Gutenberg. We do sort of a very strict every two weeks release schedule since it started. It's going to get pretty good, and it's at that point now where it's actually getting pretty darn good. And the next phase of it, actually I'm so excited about, it's going to be collaboration. So all the real time co-editing like Google Docs and Notion has, it's coming out to this open source thing, and with the technological changes, we're actually able to do it peer-to-peer. So we don't need a centralized server. We can use WebRTC and other cool technologies.

(01:04:49):
I mean, anyway, I'm going sidelining, but I think that sort of more... and if you look at a lot of great companies, there's a board or whatever but ultimately there's an executive, and some of the most iconic companies of our generations are ones where the executive retains some majority of voting control or other things like that which I've been able to do with Automattic and with WordPress. And I definitely think about succession planning and everything like that, but if or when I'm gone I don't want to pass it to a committee. I want to pass it to someone else who can have a role similar to mine and really sort of try to be a steward.

(01:05:34):
There ultimately is a check and balance on that because, again, the community could leave. They could fork the software. People could change. And so you're "in charge" quote, unquote, but you're also at surface. So it's a lot more being like a mayor than a CEO and that you ultimately are accountable to the folks who are contributing and new users and everything like that. So I do feel like there is a balance there. Some of this as well is that there's some people who aren't part of leadership who feel like they should be. So if you look at the Yoast or Korean things, these are folks who actually don't have commit status. They haven't contributed WordPress over the years and serve our normal hierarchy of the meritocracy of how you get the ability to commit code or things like that. They're like, "Hey, I want to lead a release." That's cool, dude, but there's a process. We have different people lead releases over the years, but they kind of worked their way up to it.

Lenny Rachitsky (01:06:28):
This makes so much sense to me. That's one of the themes of the podcast, just the power of a singular visionary and leader, founder mode as we've all heard is trending these days.

Matt Mullenweg (01:06:38):
You made famous, yeah.

Lenny Rachitsky (01:06:40):
I wouldn't say that it was. Yeah, Brian shared it, but then Paul Graham pointed afterwards and then I renamed the title of that episode Founder Mode to [inaudible 01:06:49]

Matt Mullenweg (01:06:49):
I really want your [inaudible 01:06:50]

Lenny Rachitsky (01:06:50):
If I zoom out, what I'm sensing here is there's people that have this ideal of how something like this should run, but they've never actually worked at a place where a nonprofit board runs it, runs a thing, and have seen what that actually looks like. And so I think there's a big disconnect between the ideal in theory and how does great stuff get built.

Matt Mullenweg (01:07:11):
And one of the things I think we've tried to demonstrate with WordPress is actually it's kind of like a open source side and a nonprofit side and a for-profit working in concert. And one of the things people don't necessarily appreciate as much about why WordPress has been so successful is because of Automattic and things like Akismet doing anti-spam or WordPress.com having a free version of WordPress that is introduced over a hundred million people to the software in a way that you could just sign up for free. You don't have to pay for hosting or download it yourself or things like that.

(01:07:43):
So that kind of for-profit, nonprofit, open source, working in concert I think is a really interesting model that we're starting to see a lot more companies do. It's actually very exciting to me that some of the things that were controversial when we started open source or distributed work are now the default for so many exciting new startups, and this whole ecosystems of really, really cool open source, like Cal.com for open source Calendly. There's so much cool stuff out there that actually there's a whole generation of younger entrepreneurs that I find very, very inspiring because they're also bringing modern design and web development and everything to open source which is very neat.

Lenny Rachitsky (01:08:21):
I anticipate a blog post one day, "I told you so, guys." Open source, remote work, I imagine there's a few more things there. There's one other thing I want to address. I haven't seen you talk about this. It comes up a bunch. It's around, this is very the weeds, but I think it's really important to people, and there's something here for a lot of people, the way you guys forked Advanced Custom Fields. So I think what happened here is you guys forked an existing plugin, I think somebody else's plugin, and then kind of pushed people to this plugin versus the original plugin. What can you share there?

Matt Mullenweg (01:08:55):
Yeah, this is very complex. So WordPress.org has kind of like a app store. After WP Engine started suing us, creating millions of dollars of legal fees and things, we blocked their access to WordPress.org. So this plugin they had, Advanced Custom Fields, wasn't able to be updated. At the same time a number of security issues were found in it, including some we reported, and so there had to be an update to it. So we're like, "Okay, we'll ship the update for you essentially." And then we were like, "Okay, I think we need to call it something different because it actually isn't theirs anymore." And they still offer Advanced Custom Fields on their own and people can download it from them, et cetera. So we made Secure Custom Fields which was originally under the same directory listing, so again, because we want all the users of it to get the security updates. This is controversial, and actually they actually got a preliminary injunction, so the judge said "Reverse this." So this has all been reversed by the way.

(01:10:04):
There now is a separate fork under separate listing of Secure Custom Fields which actually we have a team on it, developers, designers, and we're creating... just like WordPress was a fork, we've actually forged this. Actually WooCommerce was a forge. A lot of things are forks. So we forked it and now have a new name, new everything that we're doing a lot of product innovation and improving it. So there's a separate project now and separate directory listing for Secure Custom Fields. That's kind of fast-forward to today. They now have access to WordPress.org again. They have updated the plugin. Everything's back to how it was before, and there's now this separate thing called Secure Custom Fields that the WordPress project is officially supporting.

Lenny Rachitsky (01:10:46):
So I'm hearing essentially you blocked WP Engine as a part of this, we're just going to simplify WordPress, reduce confusion. They're being bad actors in the space, so we're going to block them, and in that block, there's like a dependency where people couldn't do a thing that they needed to do. So you're like, "And the one that exists, there's a problem with it, so we're going to make that dependence... release a version that you can actually use and fix the security issues."

Matt Mullenweg (01:11:09):
That was the intention. I think that there was a lot of perceptions around it that were different, but yeah, that was the goal.

Lenny Rachitsky (01:11:14):
Okay. Okay. Great. So maybe just the last question. We talked about just a lot of people see you with devil horns these days. They think you're doing bad things and they don't like the approach you're taking. You talked about there's this WP Engine spending a lot of money on PR and hiring this agency. I guess is there anything else that... why do you think so many people are looking at you as the bad guy? Is it mostly that you think... just where do you think it's coming from? Why are comments always so negative? And we talked a bit about it, but anything more there?

Matt Mullenweg (01:11:46):
I don't know if I can say why. I do think one thing I've learned is that a lot of these things we've talked about are nuanced. So one essentially thing I've learned in this process is that it's hard to explain this stuff in 240 characters or the-

Matt Mullenweg (01:12:00):
... 40 characters. Some mediums do not lend themselves well to discussing this. And so I tried, but I'm participating less in Reddit or Twitter and trying to do more long form things like this, where you can actually have the context and things can't be taken out of context. Also, I think there's something where social networks sometimes are tuned to promote outrage. And it was very interesting. We ran a sentiment analysis recently. We were kind of looking at different social networks, analyzing all the comments, and we found, actually, that the negative, the sort of devil horn fraction on, what was it, like LinkedIn, Facebook, Instagram was like 8%. It's actually pretty small. On Reddit, it was bigger, I forget the exact number, but on Twitter it was 52%. You're like, whoa, what's going on there?

(01:12:53):
And so there's something in the algorithm, and again, we can't see how the algorithm works or what the incentives are, but it can promote the most controversial things. I think that's not a novel perception. There's a lot of discussion around how social media might be creating more fragmentation in society, and I think this is just an example of that, where when you have networks, when people are getting the majority of the information from social networks, and those networks are not designed to provide nuance or balance, or even promote truth necessarily, misinformation can get spread far more than... What's the saying? Like a lie gets around the world seven times before truth has time to-

Lenny Rachitsky (01:13:30):
Get out of bed.

Matt Mullenweg (01:13:31):
Get out of bed, yeah. There's been a lot of that. So there's actually been a lot of misinformation, untrue things that go viral, and then the untrue thing gets like 700,000 views, and the correction gets like 20,000 views. So there's been some of that happening. When mainstream media has covered this, it's actually been a lot better. So there's been some actually really good articles in some business publications and other things that sort of look at a more nuanced and balanced view. And I think the podcast have been pretty good, but definitely on Twitter, I think you can get a version of all of this that is both, I think, not entirely true and also pretty more negative.

Lenny Rachitsky (01:14:15):
Yeah. I imagine people are going to be like, "Lenny, you didn't ask him this thing. Here's the thing he said that I want to learn more about." I'm sure I missed some stuff, but from an outsider's perspective, this all make sense. There's a company, I don't think PE companies are bad innately, but their job is buy a company and make it run more efficiently, and then oftentimes sell it for more. So it makes sense that they buy a company, make it more efficient, cut some corners, don't put a lot of effort into making it awesome, even though I'm sure there's awesome people working in there, trying really hard to make it great. And basically what I'm feeling is they got to a point where this is hurting the ecosystem. They're feeling really dishonest with working with you, and there's a stalling technique. And so, makes sense to me why you just have to stand up and fight back. And it's hard, it's hard to do that. Is there anything else along this thread before we move on to a different topic, anything else you want to share before we close out this chapter?

Matt Mullenweg (01:15:15):
Well, if people have more questions, they can come to WordCamp Asia. We're going to do an open Q&A there. We do town halls in the WordPress.org Community. There's a Slack people can get on and ask questions. So there is kind of a lot of open ways to engage, and I'm definitely happy to do that. I'm probably not going to do it on Twitter as much, but when there's longer form opportunities to have a discussion here, particularly if it's more like real time, like this, I'm very happy to.

(01:15:43):
And that's why if you look at it, there's actually a big difference. WP Engine has not done any podcasts and no press. They don't respond to journalists, they don't talk about this. And I've done the opposite, where I'm really trying to be out there and engaged. And everyone's like, "Why don't you just let the lawyers do the talking?" And it's like, well, but we have community, and also I feel like we're in the right. So when you're in the wrong, you probably say only have the lawyers talk. When you're in the right, I think you should be out there and telling the story.

Lenny Rachitsky (01:16:10):
I remember at the end of your WordCamp talk, you were like, "Any questions?" after this big controversial talk, and I'm curious how it felt. All the questions initially were nothing to do with this. It's what it felt like. You're just like, oh, they already had these questions. They didn't even know what you said maybe, and I bet you're just like, wait, did anyone hear what I just said? Did it feel like that?

Matt Mullenweg (01:16:28):
Well, also, that's really like a WordPress community event, so it's a lot of the core developers and things, so they have WordPress questions, so that is something.

Lenny Rachitsky (01:16:37):
You're like, hello.

Matt Mullenweg (01:16:38):
I've now done hundreds and hundreds of these town halls and QAs, and I really enjoy it because you never know what's going to come up.

Lenny Rachitsky (01:16:42):
Yeah, okay. I want to talk about all the companies that you bought and will buy in the future. It's kind of like you're building a little Berkshire Hathaway. I think you've described it that way. It's kind of what it's feeling like. And Tumblr is really interesting. Until I started prepping for this, I didn't even know you guys own Tumblr. I haven't heard this story. Why did you guys buy Tumblr? What is going on with Tumblr? It was like a big deal back in the day. What is the current state of Tumblr? What is the story there?

Matt Mullenweg (01:17:10):
Oh, Tumblr is so interesting. At the time, I think it was one of our best competitors. They created this really amazing sort of hybrid of blogging and social networking. And if you kind of zoom back, a lot of things that are now standard on other social networks, even the ability to embed an image with a post, again, it was not supported originally on Twitter and other things. Remember they used to have, what was it, like tweet image, or you have to linked out to other things to post an image to Twitter. It wasn't native functionality, and Tumblr had these multiple post types. You could post a chat, an image. They were, I think, one of the first to support video, so they did a lot of, I think, product innovation under the leadership of David Karp, who's a really amazing entrepreneur and product leader.

(01:17:54):
Funny story, both David and I were at CNET at the same time. They had hired both of us.

Lenny Rachitsky (01:17:59):
What an alumni group at CNET.

Matt Mullenweg (01:18:02):
They could have kept both of us probably. But anyway, the Tumblr, I forget the year, but they sold, I think the same time that Instagram did, for a similar amount, $1.1 billion.

Lenny Rachitsky (01:18:14):
To you or to someone else?

Matt Mullenweg (01:18:16):
Instagram bought by Facebook, obviously.

Lenny Rachitsky (01:18:19):
Right, right. Tumblr.

Matt Mullenweg (01:18:20):
And Tumblr bought by Yahoo.

Lenny Rachitsky (01:18:21):
Oh, wow.

Matt Mullenweg (01:18:22):
Who was at the time, again, Yahoo, we don't think about it now, but I feel a little old. But at the time, Yahoo was one of the internet giants and had recently Marissa Mayer, who was one of the big early people at Google, I think part of creating the API program and everything like that, was the CEO of Yahoo. This was, I think, one of her first big acquisitions.

(01:18:46):
Now subsequently, obviously ,we know how Instagram went. I think people were like, "I can't believe you bought this for a billion dollars." And obviously now it's worth hundreds of billions. So that's had a really good trajectory. At Yahoo, I think things became more challenged. So again, this is a little bit of history, but Yahoo then had this thing where they owned part of Alibaba, which then became more valuable than the rest of the company. They had activist investors. I think they had some CEO switches. I think Marissa Mayer leaves or gets fired at some point. There's all this turnover, and I think Tumblr really languished under their ownership. And from what I can understand, the team was actually held back a lot from things they wanted to launch or ways they wanted to iterate. Then Yahoo merges with AOL, which is another kind of early internet thing. That goes for a little while. So again, then Tumblr's just kind of stuck underneath this stuff.

Lenny Rachitsky (01:19:43):
Tumbling along.

Matt Mullenweg (01:19:45):
Tumbling along. And then that gets bought by Verizon. So fast-forward to 2019. Verizon wants to get rid of Tumblr. And so they're kind of putting it up for sale and had a number of bidders. Automattic ended up buying it for a de minimis amount. I think it's been reported we bought it for $3 million.

Lenny Rachitsky (01:20:10):
What a deal. 3 million.

Matt Mullenweg (01:20:14):
But obviously, that represented a lot of value destruction over the years. Tumblr had had some tough times. They actually were banned from the App Store at one point for not moderating things well enough and having maybe a little too much porn. Obviously, Twitter [inaudible 01:20:31] porn. They maybe were a little too out there with it, and we're doing a good job filtering it and keeping away from App Store reviewers or whatever. And so Verizon, to their credit though, there were people bidding more. Actually I think a porn company was bidding on Tumblr that would've paid a lot more money. They really were looking for an acquirer that they felt like would be a good steward. From my point of view, I had such incredible respect for Tumblr as a product. And the community, still, despite all of this sort of stuff that had happened, I think at that point still was like, I forget the exact number, but call it 15, 20 million monthly active users.

(01:21:14):
So really, sort of active core. And one of the things that's so fascinating is over half of that user base was under the age of 25. And actually had a huge, I think, it was like 25 or 30% LGBT+. I think a very unique place on the internet, where people could have a social network where they could be anonymous, they could put on different identities, they could be someplace their parents weren't, like Facebook or Instagram, really still could take a special spot. So we ended up buying it. Now, people are like, "Oh, you bought it for $3 million." But we bought it sort of taking on all liabilities, including, I think they were under investigation by the FTC, there were lawsuits. There was all this sort of stuff. So it was free like a puppy, not free like-

Lenny Rachitsky (01:22:01):
Free like beer.

Matt Mullenweg (01:22:05):
Had a pretty big team, I think 185 people. We were taking a lot of burners, burning a ton of cash, and that was 2019. And so, it's been, I think, a humbling experience running a social network. It was very, very different from all the other products that we've done. And I think there's some incredible things about Tumblr and that I'm still very excited about. So where WordPress has primarily a desktop and web user base, Tumblr is obviously like 85% app-based, has a younger demographic. And so part of the vision that now we're executing on is actually we wanted to create a path for people using Tumblr to actually it being powered by WordPress on the back end. So Tumblr users could unlock themes, customization, plugins, et cetera. Actually, we're in the process right now of migrating the half a billion Tumblr sites to WordPress, probably one of the largest data migrations-

Lenny Rachitsky (01:22:58):
That makes sense.

Matt Mullenweg (01:23:00):
... that's happened in a while. So we're kind of trying to do this in a way that's invisible to users on the front end, so changing at the back end while maintaining the APIs and the interface and everything. So it's a fun engineering project. I kind of posted this kind of call to arms, got a lot of fun people applying for Automattic, and we hired a lot of great folks around this sort of audacious project, this big hairy audacious goal. And so that's where it's at now. I've sort of ran it personally for a few years while we're doing turnarounds, but there's a great team there, but still challenged, still not profitable, so we're still subsidizing it from the rest of Automattic's businesses. Fortunately, the rest of our business have done really well, so we were able to do that, but I definitely want to get to a place where it's sustainable.

(01:23:46):
And one of the things we're also experimenting with is can Tumblr have not just an advertising-driven model? I think ultimately the incentives of advertising social networks can lead to the kind of dynamics that you see on the more negative side of Twitter, Instagram, Facebook, et cetera. And so really trying to create a subscription model or a sort of first-party user-driven advertising, where you promote your blog posts or something like that, or you promote a WooCommerce product or something, where it's not a third-party ad ecosystem, which I think has a lot of weird code and malware and lots of stuff I don't love.

Lenny Rachitsky (01:24:21):
Wow, sounds like a lot you took on with this acquisition, and I love that you said you ran it initially. So this is a good segue to maybe my last question. I'm curious where this goes. Just how do you... Well, let me zoom out. There's a lot of people these days that are excited about roll of businesses. I'm going to buy a bunch of companies, make them better, make them awesome, save money, and then just keep building this holding company sort of thing. You guys are doing that, and it's working well. What do you look for? How do you decide a company's right for Automattic? What are the factors that are like, we should buy this, we can turn this around and turn it into a big success?

Matt Mullenweg (01:24:58):
I don't know if I would do another turnaround like Tumblr again, or at least not for many, many years. It's definitely a different thing. The vast majority of things we acquire, it's simply something that's done well, and we want to accelerate it, or sometimes acqui-hires, where we're plugging it into one of our existing projects, or we're taking the team and putting them on something we're already doing. So it's a really talented team. Tumblr, I think we ended up ultimately replacing 85, 90% of the team as well. So that's just very different. So I do think there are different ways of doing it, but if you look at our other acquisitions like Day One, et cetera, founder's still here, many years later, we're accelerating stuff like that. We brought it to Android, we're bringing it to it to web. It's more of taking something good and making it better. And probably our best example there is WooCommerce, which was a small company, I think 35, 40 people, based out of South Africa, and has obviously grown to... Again, I said Automattic makes about half a billion dollars a year now, and WooCommerce is a majority of that.

Lenny Rachitsky (01:26:06):
Speaking of that, actually, you haven't shared the revenue number. I know it's public. Just give people a sense of Automattic's revenue. Can you just share those numbers? Because I think it might blow people's minds.

Matt Mullenweg (01:26:15):
Yeah, I think we say publicly it's about a half a billion dollars in sort of ARR revenue right now.

Lenny Rachitsky (01:26:20):
Incredible. Okay. I have a question for you. It's kind of a hot seat question. As you talked, I wonder, I feel like people are thinking of this. So you've been talking about PE companies being often bad. You're buying Tumblr. You've talked about laying off a bunch of people, turning it all around. How's that different from a PE company, Matt?

Matt Mullenweg (01:26:39):
Yeah, and I agree with you that just because it's private equity doesn't mean it's bad. And also, something people say is like, "Hey, wait, don't you have private equity investors as well at Automattic?" And we do. Now, they own usually a small percentage, sometimes under 1%, and they don't have control of the company. So I think there's a distinguish. Is it a minority investment or a control investment? And with WP Engine, Silver Lake controls the company. And when they control the company, I think there's a spectrum of actions. Obviously, being more efficient is great, and we should all strive for that. And I think every business does, whether it's private equity or our business or things that are founder controlled. You always want to be more efficient. Now, there's some spectrum there where you over-optimize, or you could have dark patterns. Right now on WP Engine, it's very difficult to cancel your accounts. Actually, I think as of today, 45,000 sites have left, so they're, I think, down to 600. Yeah, well, because their customers have realized like, "Hey, this isn't WordPress, this isn't..." or, "They're suing the guy who started WordPress, so maybe we should not support this commercially." So we have the site wordpressenginetracker.com that sort of shows in real time the sites that are leaving. It's kind of an exciting thing to see that number tick up. Actually, maybe a good example as well, even though there's a lot of negativity, you actually look at how people are voting with their wallets. They're leaving.

(01:28:07):
So I think you have to judge as well, just look at the track record. So one of the things I'm very proud of with Automattic is we are an acquirer of first resort, and we have founders that have sold to us. Paul Mayne at Day One is a great example that didn't need to sell. They're wildly profitable, could have run it himself for a long, long time, but people choose to join because they feel like we'll be good stewards of it in the future, and ultimately just have to look at the track record.

(01:28:36):
So I think don't judge it by what it's called, judge it by the actions over time. And I hope to continue building that reputation for a place that's a good steward of communities and software and everything else for many years to come.

Lenny Rachitsky (01:28:52):
Matt, we covered so much. I asked you all the hard questions and more. Before we wrap up, is there anything else that you want to leave listeners with? Any last thoughts, comments, insights, stories?

Matt Mullenweg (01:29:04):
Yeah, follow me. I'm at photomatt, P-H-O-T-O-M-A-T-T, on Tumblr, Twitter, Instagram, everything like that. I post a lot about other stuff. I post a lot about AI and open source and other things. Some WordPress things in there as well. I have these life missions to democratize publishing and commerce. We added a new one last year, which is messaging, so it's in beta mode right now, but relaunching in a few months as a product called Beeper, which takes all your Telegram, Instagram DMs, Signal, everything, brings it all into one app. And you can do some really cool stuff like that, and especially when you start to imagine search or AI, local AI around that. So very, very excited about that relaunch. So I encourage people to, you check out the beta now, go to beeper.com/beta to get the new version, and we're going to relaunch that later in the year.

(01:29:50):
So yeah, I'm very excited about that. It's kind of fun to be working on something that's at the stage where WordPress was in 2003, 2004. So WordPress is quite mature at this point. WooCommerce is kind of where WordPress was in 2010. And then the Beeper stuff, the messaging stuff is where we were in 2003. So one thing that keeps me excited is working at different stages of this.

Lenny Rachitsky (01:30:12):
This feels like a reason to be doing your approach to Berkshire Hathaway is just stay active in early stage stuff and not just optimize established things. So it's beeper.com, by the way, awesome domain name. Photomatt, what's the story of photomatt? You're into photography, I imagine, is the story?

Matt Mullenweg (01:30:32):
Yeah, it's a little bit of a pun. So a fotomatt is also, F-O-T-O-M-A-T-T, is a place that you would go to develop your photos back when you would have film and develop things. So originally my username was Saxmatt because I played the saxophone. Sometimes people mishear that. And also, I started traveling so much. There's been years I do like 400,000 miles of air travel, because I go around the world to go to WordPress events and meet the community. And as a distributed company, we do lots of meetups. And so, it became hard to carry my saxophone around. So my method of artistic expression became photography, and that's actually kind of how WordPress started, was actually originally a site where I could share my photos before Flickr, before Facebook and everything like that, sort of use this gallery software, actually open source gallery software, PHP software, to sort of share all the photos I was taking.

(01:31:25):
And actually now on my website, I think I have over 38,000 photos I posted. And yeah, it's still one of the things I really love. So it's also a username that was available everywhere, and I still do it. So I'm actually going to the Maha Kumbh Mela, the big 300-million-person gathering at the Ganges River in a few weeks. And one, I'm just excited to experience that, it happens every 12 years, but two, I'm just really excited to take some time to do photography. And yeah, I really enjoy it.

Lenny Rachitsky (01:31:56):
You forgot to mention your website and your blog, your WordPress site itself, where you blog. Ma.tt, is the domain, which is amazing. I will point people to one of my favorite ritual you have on your blog, which is you share what's in your bag, you talk about how you travel all this, and I think every year you're like, here's the gadgets I use most and bring with me everywhere.

Matt Mullenweg (01:32:18):
It's my most popular post of the year by far.

Lenny Rachitsky (01:32:20):
I'm not surprised. You need an Amazon, just buy everything button. Yeah, because basically you're just trying to optimize for the least weight and most utility, right, out of all these gadgets that you're bringing with the on trips.

Matt Mullenweg (01:32:33):
Yeah, actually weighing it is something I just started doing this year because my bag actually got really heavy, got like 35 pounds or something. And so, some friends were like, "Hey, why don't we weigh everything and just go through." So now I'm posting the weights.

Lenny Rachitsky (01:32:45):
Oh my god. Okay. Anyway, we'll point people to that. Matt, thank you so much for doing this. This was awesome,

Matt Mullenweg (01:32:50):
Lenny, thank you so much. And I really appreciate the ability to discuss these things in a longer form. And also just your audience. Oh, I guess final thing I'll say is we're hiring a ton. So you have one of the most incredible audiences in the world. I recommend your podcast and newsletter to a lot of my colleagues. And so, if you're someone who loves this kind of stuff, I think there's a big opportunity at Automattic to have an impact on these things.

Lenny Rachitsky (01:33:11):
What roles are you hiring for most and where do people find these roles?

Matt Mullenweg (01:33:15):
Automattic.com, A-U-T-O-M-A-T-T-I-C. There's a Work with Us page. You can kind of see how we work. We're fully distributed and can manage that forever. We sort of started that. Another interesting thing is we actually pay the same salaries globally. So whether you're in California or Italy or Nigeria or wherever, we pay global salaries. So yeah, a lot of opportunities, and we're hiring for kind of everything, I would say, but particularly people with great design or product skills is probably one of the areas that you can have the biggest impact at Automattic right now.

Lenny Rachitsky (01:33:53):
All right. If you made it this far into the podcast, you should definitely apply. Matt, thank you. Thank you for being here. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or a leaving a review as that really helps other listeners find the podcast. You could find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

