---
guest: Boz
title: Making Meta | Andrew ‘Boz’ Bosworth (CTO)
youtube_url: https://www.youtube.com/watch?v=_XqDB2Upr3s
video_id: _XqDB2Upr3s
description: 'Andrew Bosworth—or Boz, as most people know him—is the chief technology
  officer at Meta and head of Reality Labs, the company’s augmented reality/virtual
  reality (AR/VR) organization,...

  '
duration_seconds: 6141.0
duration: '1:42:21'
view_count: 37528
channel: Lenny's Podcast
keywords:
- growth
- roadmap
- experimentation
- analytics
- monetization
- culture
- leadership
- management
- strategy
- vision
- mission
- competition
- market
- persona
- design
---

# Making Meta | Andrew ‘Boz’ Bosworth (CTO)

## Transcript

Lenny (00:00:00):
You were basically the 10th engineer at Facebook. I imagine there was a lot of pain and suffering that people don't often hear about.

Andrew ‘Boz’ Bosworth (00:00:07):
I didn't sleep for more than four hours at a time. I'd wake up every four hours and check the report and see if anyone was attacking the site. They don't tell you about that stuff in the movies.

Lenny (00:00:14):
You worked 120 hours per week., you had no hobbies.

Andrew ‘Boz’ Bosworth (00:00:17):
I don't want to take away from the romanticism of it. It's just that most often, we hear those romantic stories from the successes. It's a healthy thing for people to want to throw themselves into something and take that risk, but it is not glamorous at the time.

Lenny (00:00:29):
The newsfeed. That was one of your early projects at Facebook. People did not want it. They were wrong, clearly.

Andrew ‘Boz’ Bosworth (00:00:33):
Now, newsfeed was an easier case than people suspect. Everyone was outraged at the same time as they immediately doubled their usage of the product.

Lenny (00:00:40):
In terms of the economic utility, the Venn diagram of Boz, of newsfeed and ads created $1 trillion of value.

(00:00:48):
Today, my guest is Andrew Bosworth, or Boz, as most people know him. Boz is the chief technology officer of Meta. He joined what was then called Facebook in early 2006 as one of the first engineers, and during his 18-year tenure at Meta, he created some of the most impactful and important products in internet history, including the Facebook newsfeed, which was the first ever algorithmically ranked content feed of any social network, and is basically what people think of as Facebook today.

(00:01:17):
He also built the original Facebook mobile ads platform, which he then ran for another four years. He also helped build and scale the Facebook messaging system, the profile, the timeline, Facebook groups, and even the internal engineering boot camp. Most recently, he served as VP of ads and business platform, where he led engineering product, research, analytics, and design. And in 2017, he created the company's AR/VR organization, now called Reality Labs.

(00:01:42):
These days, Andrew leads Meta's efforts in AR, VR and mixed reality, along with consumer hardware across Quest, Ray-Ban, Meta smart glasses, and more.

(00:01:52):
In our wide-ranging conversation, we touch on so many important lessons and stories, what it was really like in the early days of Facebook, why you should be asking your manager for help more often, why communication is the job. Lessons from Meta's turnaround over the past couple of years, Boz's thoughts on the Apple Vision Pro, a bunch of leadership and career advice, what it was like to build the very first newsfeed, and lessons from that experience, and stories of failure and stories of success, and so much more.

(00:02:22):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes, and it helps the podcast tremendously.

(00:02:32):
With that, I bring you Andrew Bosworth, a.k.a. Boz, after a short word from our sponsors.

(00:02:39):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO-27001, HIPAA and more, with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance, alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's Vanta.com/lenny. This episode is brought to you by Eppo. Eppo is a next-generation, A-B testing and feature management platform, built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features, and Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does. When I was at Airbnb, one of the things that I loved most was our experimentation platform where I could set up experiments easily, troubleshoot issues, and analyze performance, all on my own. Eppo does all that and more with advanced statistical methods that can help you shave weeks off experiment time, an accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles. Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A-B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny, and 10x your experiment velocity. That's geteppo.com/lenny.

(00:04:47):
Boz, thank you so much for being here. Welcome to the podcast.

Andrew ‘Boz’ Bosworth (00:04:55):
Thanks for having me. I've been a long-time fan of your program and all the things that you've been putting out, so I'm glad to finally get a chance to join.

Lenny (00:05:01):
Same. I'm really excited to have you here. I have at least a billion questions I want to ask you. But I want to start with a few fun facts that I've found about you, and what if I go through them and then just pick one that stands out, and then tell the story behind it? How does that sound?

Andrew ‘Boz’ Bosworth (00:05:17):
All right, sounds good.

Lenny (00:05:18):
Okay. You went to 14 proms.

Andrew ‘Boz’ Bosworth (00:05:22):
Yeah. It's true.

Lenny (00:05:22):
Okay, I'm going to keep going. Okay.

Andrew ‘Boz’ Bosworth (00:05:25):
Wow, that's a strong opener.

Lenny (00:05:27):
That might be the one. You were a national Taekwondo champion in college. You were Mark Zuckerberg's TA in college in a class on AI, which isn't actually how you landed at Facebook, from my understanding. Harvard was recruiting you to play football for them. You were very active in the 4-H Club, and you raised animals and showed them at county fairs when you were growing up. You once shared a stage with David Copperfield.

Andrew ‘Boz’ Bosworth (00:05:52):
That's true.

Lenny (00:05:52):
MC Hammer once told you that your outfit was stylish. And president George W. Bush complimented you on your shoes and the shine of your head.

Andrew ‘Boz’ Bosworth (00:06:03):
Yeah, these are all true. I want to say, wow. First of all, I got to make sure that people understand, I was a national collegiate champion, in as a green belt, which that's like being the JV champion. Just so everyone's clear on what that is.

Lenny (00:06:15):
W's a W.

Andrew ‘Boz’ Bosworth (00:06:16):
Heavyweight sparring. I'll tell... The prom story is a funny one. It's related to the 4-H story. I was a big-time 4-H'er, National 4-H Hall of Fame, did all this stuff there.

(00:06:29):
As a comeup to that, 4-H is a wonderful program, youth program, it's coed program, and I was all over the state, all over the country, doing leadership events and doing these conferences, and doing a lot of public speaking.

(00:06:39):
And almost every 4-H event has a dance. People don't know that. At the end of a conference, at the end of the, literally camp, you'd go camping for a week, at the end there's a dance.

(00:06:49):
And so, as a consequence, the most important thing, if wanted to go to a lot of proms, I was a good dancer. And it turns out, the high-level bit, at least in the 1990s, for girls selecting who they might want to go to prom with was, will he and can he dance? And the answer with me was yes. And combine that with the fact that I knew a bunch of girls who went to different schools, that's the recipe for success right there, if that's the goal that somebody has. Two my junior year and 12 my senior year. I once went to three in one weekend, a Friday, a Saturday, and a Sunday night.

Lenny (00:07:21):
Another fun fact about you is you were basically the 10th engineer at Facebook, initially, way before it was a clear success story. I imagine there was a lot of pain and suffering and struggle that people don't often hear about those early days. They see a movie like The Social Network. It looks like, "Oh, that was so much fun. I've got to start a company. It's going to become a trillion-dollar success story." I'm curious just what those early days were like. Are there memories that stand out to you?

Andrew ‘Boz’ Bosworth (00:07:47):
Yeah, there's a bit of a joke in the 10th thing, which is me and five other guys all joined at the same time, and there was nine engineers before us. We joined the same day, so we're all the 10th engineer. So, somewhere between 10 and 16, depending on how you want to do the numeration on that.

(00:07:59):
I've written about this in my blog, and I tell this story a lot, which is it was fun, and there was tremendous camaraderie and memories that were formed, but they were formed in a kind of forge of really intense times.

(00:08:13):
At that time, almost all of us lived within one mile of the office. We ate most of our meals together because we were working, not to say we weren't also friends, but because we were working, it's like, oh cool, you just roll into a meal and roll back into work.

(00:08:26):
And there's little things that you don't appreciate, which is like there was nobody to help you. There was no expert. And so, it wasn't like, "Hey, I'm struggling with this one tricky problem. Who should I talk to?" It's like, nobody. You should talk to yourself and figure this out. Or it's like, "Oh, man. My servers are out of capacity." It's like, "Cool. You should go to Fry's Electronics, you should buy a bunch of components, you should build a new server, and then you should run it. Maybe drive into the colo, rack it, and then get back and run it."

(00:08:52):
People really undervalue the fact that when you go to work, even a moderate mid-size corporation today, especially with the tremendous growth of startups supporting startups, things like payroll and finance and IT and HR, these things are professionally handled in many cases.

(00:09:10):
That was just not the case in the early 2000s. It was just you, and your personal car, and whatever you wanted to do with your time.

(00:09:18):
So, I don't want to take away from the romanticism of it, it's just that it's most often we hear those romantic stories from the successes. We so rarely hear somebody who went through really sacrificing a lot of my 20s from any kind of social or outgoing, fun environment.

(00:09:37):
It paid off for me, so no one feels bad for me, nor should they. But there are other people who do the exact same thing, maybe they worked harder, maybe they were smarter, maybe they did better, and it didn't play out for them. And it's a big sacrifice.

(00:09:48):
And so, I love the enthusiasm for startups, I love startup culture. I think it's a healthy thing for people to want to throw themselves into something and take that risk. But it is not glamorous at the time. In retrospect, it's like, "Oh, it can be..." We have a little halo around it. But at the time, it doesn't feel glamorous.

Lenny (00:10:06):
Yeah. In this post you mentioned, you said that you worked 120 hours per week.

Andrew ‘Boz’ Bosworth (00:10:07):
Yeah.

Lenny (00:10:10):
You had no hobbies, and you gained a lot of weight.

Andrew ‘Boz’ Bosworth (00:10:15):
Yeah. We drank a lot to make up for it, so I gained a lot of... And you weren't eating healthy. It was crazy.

(00:10:22):
I think I've told this before. There was a time where one of the first things I built was an anti-spam, kind of anti-scraping defense mechanism. But we didn't have any ops support. There was no 24/7 online support.

(00:10:35):
So, I built this tool. I had to wake up every four hours. For about two years, I didn't sleep for more than four hours at a time. I had to wake up every four hours and check the report, and to see if anyone was attacking the site. And if they were, I was up, and I had to go battle back. And if they weren't, cool, I'd go back to sleep. But that's the thing, they don't tell you about that stuff in the movies.

Lenny (00:10:55):
That's almost worse than having a kid, a newborn.

Andrew ‘Boz’ Bosworth (00:10:59):
And nobody asked me to do it. Nobody even asked me to do the anti-spam, anti-scraping stuff. I just thought it was a problem, and I went and did that, and that was the solution I come with. If I was a better engineer, maybe I'd have solved a better problem.

Lenny (00:11:11):
So, maybe just to close out that thread, when you talk to founders, what advice do you give them along these lines?

Andrew ‘Boz’ Bosworth (00:11:18):
I want to be cautious about this, because what I tell founders... The first thing I tell founders is that I've never been a founder, and I want to recognize the difference. I joined January 9th, 2006. That's almost two years after Mark started the company. I wasn't involved with fundraising, I didn't have to do any of that side of the things, and I didn't even have to deal with the board or the business side of things. I really was lucky, in a way, to have joined when I did.

(00:11:42):
But the first thing I tell founders is like, "You should take my advice with a grain of salt. I have not actually been in your shoes."

(00:11:47):
If I can compliment you, really, one of the things I like about your program is, there's a whole system of professionals in our industry. And when I grew up in technology in the valley, you always heard about the ACM, right? The Association of Computing Machinery. You heard of these legendary professional organizations that supported people in our fields.

(00:12:09):
And by the nature of the rapid pace of change in the technology, and the nature of the engagement of those institutions, even academics, even academia broadly, kind of are out of touch. The tools that you got from those places weren't useful in our field.

(00:12:23):
So, I do think the mentorship that we give each other has been a critical and sustaining resource. There is, today, now, resources like your podcasts and your newsletter that are actually really designed to help people who are professionals in our industry in a way that is almost kind of missing for 15, 20 years, and I love to see that. Because if you're an up-and-coming [inaudible 00:12:45], literally you used to have to know somebody and ask them a question.

(00:12:48):
And so, a lot of times what I'm helping founders with, I can help them with the strategy, I can help them think through the technology choices, I can help through business, I can think through the management, the organization structure. But I also try to be very clear, there's a bunch of stuff that I just was never exposed to.

(00:13:00):
So, even as we just talk about how tough it was for the average engineer joining Facebook in 2006, man, it was even tougher for Mark Zuckerberg in 2004, probably. And that's a story that's been told, I'm sure, but still. So, I think these are both... It's almost all scale and variant. No matter how far you dial back, the challenges are interesting and are worth talking about.

Lenny (00:13:22):
One of maybe your most popular posts is this quote that you share about the advice you often give. What you say is, "The advice I find I have to give more frequently than any other in my career, as a manager, a board member, an advisor and a friend, is for people to more directly leverage their leaders." Can you talk about that and what that means, and what that looks like?

Andrew ‘Boz’ Bosworth (00:13:40):
It's such a normal and natural healthy thing. And by the way, we do it in our personal relationships. Like I said in the post, we want to do it ourselves. We want to do it ourselves to prove to everyone that we can do it ourselves.

(00:13:52):
And we think in our heads, "If I ask for help, haven't I already given up that goal? Haven't I just admitted defeat on one of my top level goals, which is to demonstrate that I can do it myself?"

(00:14:04):
But what so often we forget is, more often than not, your job is not to do it yourself. Your job is to get it done, is to have the thing done, done well, done right, done competently. And a lot of times, the tools that you need to do that live with your manager, with your partner, with your advisor, with your mentor. That's where they live.

(00:14:25):
So, how many times as a manager have I gone through, and somebody's told them, "Here's the job." They're like, "I got it." They go off, they come back, it's done, it's wrong. And I'm not blaming them for it being wrong. They didn't check in with me. They misunderstood. We miscommunicated. I'll take the L on that. That's no problem.

(00:14:42):
But here we are, six months later, it's not done right because they misunderstood the brief. We miscommunicated with the brief.

(00:14:49):
Or they come back, and it took a year. And I'm like, "Why did this take a year instead of six months?" And they're like, "Oh, man. I had all these things I had to deal with." Where, if they had emailed me, I could have bulldozed that stuff. I could have cleared the path. I could have said, " Oh, no, no, no. Don't worry about that. This is the thing." And then we'd have been done six months sooner, and they would've been less frustrated. And so, light touches.

(00:15:09):
Now, I do think as a manager we also have a job to say, "Hey, that's kind of the work, so you got to kind of go figure that out." And one of my things I always tell my managers, one of the most powerful things we do is refuse to rule. Someone will bring me a thing. A lot of times we feel obligated to weigh in and help. I'll be like, "Nope, but look, I think you've got it. I think the challenges you're facing are the right challenges. I think you're approaching it in the right way. Just do your best there." And that's what it is. And so, there is a responsibility as well for those of us who are leaders, mentors, advisors, board members to do that.

(00:15:39):
But, by the way, we do this... Personal relationships. You're with your partner, and you're trying to do something the right way, but you're not talking to them about it. You're just taking a huge risk there, and for very little reward. They're not going to be mad if you ask them, like, "Hey, is this how you wanted it done? I don't know."

(00:15:56):
And so, I do think it's kind of funny how much we build these castles in our mind, these little silos that keep us from engaging the structures that are built around us, that are designed to help us succeed. I saw this great quote, actually just yesterday. I saw Patrick Stewart, who is one of my favorite actors of all time, and whose characters I love, and he talked about people going on casting calls. And this is a brutal thing for actors, right? You're going on 30, 40 things, you're getting rejected. It's tough. Everyone's kind of heard about this. And he said, "No one wants you to succeed more than the person you are auditioning for, because they want you to be awesome. Because as soon as you are awesome, they're done. They want you to be amazing."

(00:16:37):
That's like your manager. Nobody wants you to be more awesome than your manager does, because when you're amazing, your manager, his life gets easier, her life gets easier. So, I just think that's the mentality we get into is like, "No, no, no. They're testing me." They're not. They are rooting for you. I promise you that.

Lenny (00:16:53):
I love that advice. I imagine the reason people don't do this, as you said, is they don't want their managers to think they don't know what they're doing, or they can't solve it. Do you have any advice and guidance for when it makes sense to go reach out and ask?

Andrew ‘Boz’ Bosworth (00:17:06):
One of the things I think, for people who are timid about this especially, is I think you can put a framing around it that's really easy for your manager to engage with. You can say, "Hey, I'm making progress on this. This is what I'm blocked on, this is the current program." And I'll even say, "Hey, if this all looks good to you, no response required. If there is something here that you want me to do better, different, that you think you could help with, let me know."

(00:17:32):
I love a typed, five-, 10-sentence email, "No response required. Here's where things are." Even if everything is going really well, I'm like, cool, this person understands the urgency, they understand the assignment, and they're giving me a little heartbeat, a little ping back.

(00:17:53):
And then also, if two weeks later, let's say the blocking issue is bad, then you say, "Hey, I am sorry, but I do actually need your help now. I'm actually blocked on this thing." I have the context. I have a mental model of you toiling away on the right thing, on the thing I asked you to do over there. Even then, when you're blocked, you can make my life super easy. Like, "Hey, what I'd love for you to do, if you could send an email to this person, here's a draft with this thought, that would help."

(00:18:23):
Or it's like, here are specific questions framed up. "I think this is what you want. Is this right? Yes or no? If no, okay, we'll come back and we'll spend more time. If yes, we're all good." So now, not only am I up to speed, I have a mental model, I'm engaged. Also, you've made it super cheap for me to help you. And people are always surprised. People who work for me are always surprised when I tell them how big a part of my job is doing these little types of things.

(00:18:53):
It's a little spinning plates at my scale. I've got 10,000 or 15,000 employees, depending on how you want to count different things. And so, you're just like, every now and then I got to get a whole new plate, a whole new rod, and just really put the effort into it. But for the most part, I'm just trying to touch everything and keep the momentum going. And so, if something falls, and somebody didn't tell me that "Hey, we're losing rotational velocity here. We're losing momentum." Oh, I'm bummed. I'm like, "Ah, now that plate fell. I got to start a whole new thing over here now."

(00:19:22):
So, I think people underestimate. They think of my job differently than my job actually... My job is actually tons of little touches.

Lenny (00:19:29):
So, I think a key takeaway here is, one, index more towards asking your manager and leaders for help. And I love this way of framing it of, it doesn't always need to be like, "Here's what I need from you." It's, "Here's what's happening. Here's things that might be blocking me. Here's questions I have. Here's things that are going on."

(00:19:44):
This is actually similar to something I found really powerful that I'll share real quickly, this idea of a state of... I call it the State of Lenny email. And I sent this email to my manager every week. The State of Lenny. It's kind of like State of the Union. And it's, "Here's my current priorities, here's what's on my mind broadly, and then here's blockers that I need your help with.

Andrew ‘Boz’ Bosworth (00:20:02):
We actually used to have a format for that we called HPMs. Highlight, people, me. And every manager at Facebook from like 2008 to like 2014 would send to their manager, or even their leadership group. I mean, at one point when I was running what we called comm apps, I just sent it to Zuck and the whole leadership group.

(00:20:24):
It's like, what's the highlights include? And it highlights [inaudible 00:20:27] flow. What's the big ticket things you need to know? Where are people? Like is somebody in trouble? Is somebody at risk? Is somebody doing really amazing work that needs a shout-out? And then me, how are you personally doing? HPMs, we called them.

(00:20:39):
Actually, it's funny. I hadn't thought about that in a long time. But yeah, no, I think this kind of thing can work. And look, every manager is different, so even at the Meta level, by the way, is another success. I think what people do is they want to treat every manager the same, and that's not going to work because every manager is different.

(00:20:54):
But every manager, you can ask, "How do you like to get updates?" You can ask them when you first start working with them. Like, "Hey, what's your cadence? How do you like to stay informed?" And so, for me, I do regular one-on-ones. As the org's has gotten bigger, those have gotten more distant, so people have replaced those with more written things.

(00:21:11):
But no manager will get pissed at you if you're like, "How do you like to get information about me?" That's a totally reasonable thing to ask.

Lenny (00:21:18):
I love the specific idea you shared of just drafting the email to say the other team leader, "Here's what I need you to tell them. That would really unblock this thing." And that's such a cool idea.

Andrew ‘Boz’ Bosworth (00:21:27):
By the way, I always put my own... I don't take that copy paste it. I'm always looking at that and be like, "Okay, I understand." A lot of it is actually not about what you want the other person to hear, it's about the voice, the tone.

(00:21:41):
It includes a lot of history. I don't know. Have you been going back and forth with them for 12 rounds, and this is going to feel to them like I'm really coming over the top? Or is this like, "Hey, first time you're hearing about this, my bad. Here's what we're doing. Need your help."

(00:21:54):
So, a lot of that isn't even about making my life easy because I want to copy paste. A lot of it is, actually, there's a rich set of information in how you tone and how you draft that note that's going to help me land it correctly and not feel like I'm just out of band, heavy coming in.

Lenny (00:22:11):
This touches on something that I often hear is very core to the way Meta works, which is transparency. Anyone can ask Zuck questions at the Q&A's. People are encouraged to post constantly internally of what they're thinking, what they're working on. All the data is shared publicly. Which often leads to leaks, which I hear you hate, and that is a pet peeve of yours.

Andrew ‘Boz’ Bosworth (00:22:32):
Just feels like a violation of the team trust. Just feels like... I grew up with playing sports, right? I was football, soccer, track. And you just can't imagine one of your guys calling out the play to the other team. Can you imagine what you would do in that case? "You're off the team. I'm sorry, you can't be here." Anyways, sorry. Carry on.

Lenny (00:22:48):
Yeah, and there's so many more people, it's hard to find. Who is this? So, with this downside as an example, and I imagine there's other downsides also takes a lot of work, and it puts people on the spot a lot of times, what have you seen as benefits and why is that such a big part of Meta's way of working?

Andrew ‘Boz’ Bosworth (00:23:05):
Yeah. This kind of comes back to, I think, the principle that really good, talented people, you want to leverage them fully. You really want to make sure that they are fully leveraged. And so, anytime they have the wrong information, or they don't have the information, you've now blocked one of the economically most valuable things that your company possesses, which is this person's time, attention, talent. Not only that, you've also made them more frustrated, and now they are more likely to leave.

(00:23:35):
If the lifeblood of any company are the people inside of it who collectively commit to some kind of a goal and a mission and work together, then you want to maximize that potential. And creating this really open information ecosystem is one of the ways that we do that. So often, great, phenomenal work that has happened at our company has not come from this one top-down mandate, but has come from people understanding not just what we're trying to accomplish top down, but also having way more information at their disposal to be able to act on it.

(00:24:16):
People talk about top-down or bottoms-up culture, and it's a bit of a myth, in my opinion. If you've ever met Mark Zuckerberg, it's not a bottoms-up thing. The ideas that we're pursuing are Mark Zuckerberg's ideas, first and foremost. That's not to say that he's not open to new ones, and of course he is, and that's a form of bottom-up, people can bring ideas to him and he internalizes them and acts them or not. But when he brings things top-down, he's not micromanaging, he's in the details. I'll be careful on that.

(00:24:44):
But he does create the space for you to bring back three or four versions of the thing that he's talking about, and then he shapes it from there. And you can't do that if there's... If you don't have degrees of freedom, sure, but also if you don't have the information. Otherwise, if you don't have the information available, what we're trying to accomplish, why we're trying to do it, what the infrastructure is like, what the availability is like, what the performance is going to be like, well, you just are stuck. You're just going to have to follow the script. That's very boring for high-talent, high-creativity, high-engaged people.

(00:25:15):
Now, it does come at a tremendous price. You have to get really good at managing information on the incoming. Most people at most companies consume all the information that's given to them, but the information itself is carefully managed. They're getting all the information they're intended to get.

(00:25:32):
We've turned that on its head, and it sounds great, but it's not free. Even somebody senior coming from outside of the company to the company, one of the things I have to coach them on is, how do you find signal amongst all the noise?

(00:25:45):
You have to have a system for managing your information. You have to have a system for triaging the incoming, getting rid of a bunch of stuff that is on the wrong channel, or it doesn't matter to you, figuring out what's the... groups that you want to be a part of, but you consume only when you choose to and-

Andrew ‘Boz’ Bosworth (00:26:00):
... groups that you want to be a part of but you consume only when you choose to. And where are the things where you're getting push notice? Like that's the real time thing, and that takes some time.

Lenny (00:26:08):
This point you made about bottom up versus top down is really interesting, because, when I think of Meta, I think it's a very bottom up culture. I hear everyone comes up with their ideas, runs experiments, is very encouraged to just try stuff, and it's really interesting to hear that. And it makes a lot of sense that most of the big ideas actually do come from the top.

Andrew ‘Boz’ Bosworth (00:26:26):
It's of these mythology things. I don't think it's the wrong... As a contract, it's more bottoms up than many other companies, because you do have these degrees of freedom within the construct. But make no mistake, like Mark or me or Chris Cox or Javi, they have very strong opinions about what we should be doing as a company, and your bottoms up-ness works within that framework. But it is true that you can ask Mark any question, and he's going to answer it. Same with me, same with Chris, same with Javi and also that we certainly take inspiration from the discussion that we have with employees. So I don't know, it's just not as black and white as people tend to paint it.

Lenny (00:27:02):
I think one of the biggest lessons here is making it at least feel like you have a lot of say, even though a company is very, "Here's the big strategic [inaudible 00:27:10]," you're very good at making people feel like they can have an impact and a say.

Andrew ‘Boz’ Bosworth (00:27:14):
And can I tell you, the most important thing is just giving people clear guidelines so they know where they... Like, "Where do they have space and where do they have no space?" One of the things that we go in these reviews with Mark or my team with me I'm sure, and I'm like, "For this part of the UI, it is going to... Like, I will draw it for you. It's going to be like this." And this other part. I'm like, "Cool, that's important, too. I don't have a clear vision of it. Why don't you do it?" So there's just really clear guardrails of like, "Okay, where are we just on assignment? And where do we have more flexibility?"

Lenny (00:27:45):
Is there an example of that that comes to mind where you were just very in the details and drawing the screen?

Andrew ‘Boz’ Bosworth (00:27:51):
Over the course of time, there's been quite a few examples. I think early on, when we were working on News Feed, mark was absolutely whiteboarding every single pixel that the team had to put on the front end. On the back end, he was like, "Make it rank, have some ranking." So I felt like I was lucky there. I was just like, "Cool, I'm off to the races on some ranking stuff." And Chris Cox and all these other guys are having to really pixel-match these things. But it's not always that way by the way. So now fast-forward and we're talking about ranking, it's not like Mark is always hands-off on that. When we got into modernizing our ranking systems, which we've done over the last five years, Mark was heavily involved and like, " Hey, what's the mix shift and how are you weighing different things?"

(00:28:33):
And so it can go both ways. For me personally, I've gotten really involved in some relatively esoteric things. I was really adamant, for example, that hand tracking and mixed reality make it into the headset. Let's just say that there weren't any supporters in the team. Obviously we had a hand tracking team, which is phenomenal, mixed reality team, but there was a lot of people who were like... They did not feel those features were going to be critical for this to become a mainstream device. I always believed that they were for ease of use and for... So I just really forced the issue and didn't give anyone any room and held really high standards for the performance benchmarks we were going to hit on the hand tracking. And teams told me it was impossible. And it wasn't. It did great.

Lenny (00:29:11):
This touches on something that comes up a lot on this podcast. And there's this debate between how in-the-weeds founders and execs should be, whether they delegate, empower, versus, "No, we're just going to do it this way. I'm going to be very involved in every mock." And there's always this up and down that happens where it's like, "Okay, cool, we're going to let people run and do their thing," and then things start to not work as well often. And then, "We're going to take back control." You have just a perspective on when it makes sense to go deep, how founders execs should think about that?

Andrew ‘Boz’ Bosworth (00:29:41):
Such a useless answer for founders, it depends on the weeds. There are some weeds that really matter and there's some weeds that really just don't, and I should say, that doesn't mean they don't matter at all. You have to do them, but they aren't the hinge upon which success or failure will happen. Yeah, there's people I really respect, Brian Chesky's been on and said, "Look, the Airbnb is going to work only on the things that I can work on. It's that's the extent of what it's going to do." And that's a super extreme form of it. I have a lot of respect for him and how they're working things. I think that if you have great super talented people that you can trust who can own bigger pieces, that's one option. If there are ways to structure it so that you can check in effectively and make sure that it's on track, that's another way to structure it.

(00:30:27):
And there probably is still work happening at Airbnb, that has to happen, finance and accounting and HR, that Brian isn't personally managing. So there are clearly non-technical areas that we do. Or legal. There are areas that we do trust that this is happening at. And so I think a lot of founders regret delegating too much, from my conversations. And I totally get that. Or they delegated something critical that really turned out to be the most important thing. For me, the judgment is like, "How do you, most important, determine what is what matters the most?" And so Mark, we joke inside of Meta, to this day, we call it the eye of Sauron. When Mark has determined that the thing that you're working on is the most important thing, there is no detail too small for him to notice.

(00:31:17):
He will be in a review, and in the same review. We'll be like, "Strategically, I think we're off course. And also, this one pixel is definitely wrong. You have to fix that." That's a big range. Frankly, I'll be a little bit self-congratulatory, I pride myself on being able to do the same. And I think people who work with me often comment that the style of leadership that we have, and I think Chris Cox is the same, is where it's like we will go where hide a low on the things that matter a ton. And there's a bunch of other things that certainly matter. We're glad we're doing them, but either they have pretty clear roadmaps, pretty clear examples in the industry, or it's like that's a feature that you have to have but isn't going to determine success or failure. So getting it into rough shape and then iterating on it is fine. And so I think it really does depend on the weeds, how deep you want to get.

Lenny (00:32:08):
It's so funny, I use exactly that same metaphor, the eye of Sauron, when I talk about working on things that Airbnb that matter a lot to Brian. And my advice to people is, "You don't want to be in that eye of Sauron for too long in your career, because you're just going to burn out if you're working on the most important thing all the time, but want to be close. You don't want to be in the Shire, but you want to be around the [inaudible 00:32:26].

Andrew ‘Boz’ Bosworth (00:32:26):
That's right. They're both... So I worked for years in ads. From 2012 to 2017, I ran ads in a business platform, this big ads group, and it was an area where certainly it was very important, but Mark had so many other things going on with the transition to mobile, he did kind of delegate it to me. And it was awesome, and it was so cool to have that kind of trust from him. And also, you're constantly terrified, because like, "Mark does not know. What if this is all..." My leads would be worried, because they just hadn't had a review with Mark in a while. And it's like, yeah, you suffer in the intensity of the gaze of Sauron. You also suffer in the shadow of its absence. There's no perfect place to be.

Lenny (00:33:09):
That's hilarious. I'm trying to think of the part of Middle Earth that is a metaphor for that.

Andrew ‘Boz’ Bosworth (00:33:14):
Yeah.

Lenny (00:33:15):
Okay, so you talked about the News Feed, which was one of your very earliest projects at Facebook. Here's a couple fun facts I know about the News Feed. One is that it was the very first algorithmic News Feed of its kind of any social network and maybe of any sort of product like this. And two, it was the very first AI code that was written at Facebook to rank the actual News Feed. So there were a lot of firsts, and clearly this became a huge deal. The News Feed is essentially what people think of when they think of Facebook now, but it was super controversial when it came out. People were very against this. They did not want to be sharing this much information with people, or so they thought, and then they realized eventually, "Oh, this is actually exactly what I want." What did you learn from going through that experience of building something that people initially reject and then later realize that they actually do want this and this is exactly what they're waiting for?

Andrew ‘Boz’ Bosworth (00:34:08):
This is a story that you tell a lot actually through your interviews, which is just like, "You have to have conviction in what you're building." You're choosing your customers as much as your customers are choosing you, is one way I think about it sometimes, and one mistake that you do see sometimes startups make is they get an early cohort of users whose needs actually take them kind of orthogonal to a larger market. And so they become kind of held hostage by their earliest customers now. So time and time again, we've had a vision for what we thought this should look like, and it wasn't the thing we were delivering right now. And so people who were using the thing we currently had were not sure that that change was what they wanted. But we had a confidence that over time they would, and we're not always right, but in these cases we were right. Now News Feed was an easier case than people suspect, because everyone was outraged at the same time as they immediately doubled their usage of the product.

(00:35:05):
So we had a few advantages there, which was, it was literally like everyone was like, "I hate this so much." And they would refresh, refresh, refresh. And so we were like, Okay, wait, there's cognitive dissonance here between what the stated preferences and what the revealed preferences are in the economic sense. So News Feed was a little easier than people suspect, to us, to stick with. But people sometimes misunderstand that. They think, "Oh, the lesson is don't listen to your customers. Not at all." And we certainly care a tremendous amount. And even with News Feed, we did actually screw some things up. I kind of always make this joke that it's almost like... You know when you're at the party and music's loud, you're talking to somebody and the music cuts out right when you're saying something at a super high volume, and so everyone in the party hears the last thing you said?

(00:35:42):
Now you were saying it in a public place, so it wasn't like it was a private comment, but you also didn't mean to broadcast it at that volume. We kind of did that to the entire user base. We took what had been wall posts, which sure, anybody could have gone to that profile and seen and then put it kind of on blast, on Main, as the kids say these days, "Put it on Main," and someone's like, "Ah." So we did that. I don't want to say it like... We did screw things up. It wasn't like, "Oh, this is a clause execution." So another thing to know is like, "When did you screw something small up, and when did you do something big up?" When is the thing itself wrong, versus when were the details wrong? That is an art. That is a real art, and you don't always have user data to determine it like we did.

(00:36:25):
And so a lot of that is, "Do you have a clear vision and intuition for what you expected to happen?" And then what happened instead and can you diagnose the delta there? So in the News Feed case, we made a bunch of little mistakes. The thing itself was right, and I really am quite proud of the work we did there. Me and Chris Cox at the most core probably in the engineering side, which you saw as the PM, there was no ranked feeds before that. We did have some AI that I built before for the anti-spam, anti... things, but it was pretty rudimentary, but it was probably the first consumer AI that was in a website of that kind around content. And we built the most efficient monetizing surface in history outside of Search, I think. [inaudible 00:37:04] for those who are curious, I don't use monetization because I think money's the most important thing. I do think it suggests the economic power you've created, which I do think correlates very strongly with human utility. Although obviously I respect that some people may disagree.

Lenny (00:37:17):
In terms of the economic utility, the Venn diagram of Boz, of News Feed and ads, create $1 trillion dollars of value.

Andrew ‘Boz’ Bosworth (00:37:24):
It's not-

Lenny (00:37:24):
Well done.

Andrew ‘Boz’ Bosworth (00:37:25):
It's not nothing, not nothing.

Lenny (00:37:27):
[inaudible 00:37:27].

Andrew ‘Boz’ Bosworth (00:37:27):
We're proud of that work.

Lenny (00:37:28):
You have this quote in one of your posts about the News Feed where you said, "It consumed me more fully than anything in life had ever consumed me. It opened up to me the truth that when you're passionate about something, you do better work, you do smarter work and you're, in order of magnitude, more productive."

Andrew ‘Boz’ Bosworth (00:37:43):
There's no substitute for it. One thing I've learned about myself since that post actually is just the degree to which I am somebody who is inclined to be passionate about things. And it's a gift that I'm lucky to have, and I understand that's not every person. And so actually the ads thing is a good example. When Mark told me to go work on ads, I was like, " No, I don't want to. I don't think I have a passion for that." I had this idea of myself. I had a very strong identity of myself as this AI infrastructure product guy, and I was working in this space and nope, I was wrong. I just am a guy who gets excited about things. Once I get into ads, it's like, "Oh, this is fascinating. It's a three-sided marketplace, and there's all these different..." It felt like I was playing chess times in terms of the moves with the other players in the industry, and I was super pumped about that.

(00:38:26):
And then when he wanted me to work on hardware, I was like, "No, I'm not. I'm a software guy. I'm a software guy, Mark." And now, I love this work. That's such a fascinating space that I've learned so much. So I do think that's right. I do think what I find something I'm passionate about that's good. What I have learned since then is to give myself a space to understand if I can get passionate about it. Now, there are parts of jobs that I've had before where I just never found the passion, and after six months I just have to move on. Literally it's like I'll either quit, get fired, I'm doing bad work, I don't care about the work. And so I do have a self-awareness. It's not that I can get passionate about anything, but I do have a pretty broad palette, it turns out.

Lenny (00:39:01):
I think that's a really interesting career lesson of, "Don't assume you won't be excited about something that may come up." Is there anything there that you'd share with folks of just like, "Explore it, give it six months, see if you can get excited about it?"

Andrew ‘Boz’ Bosworth (00:39:14):
Absolutely. So I have a very unusual career arc in some ways, which is I really almost changed jobs every six months for a long time. I was working on this integrity stuff with News Feed in the background. Then I was working on News Feed for about a year. Then I worked on site speed and infrastructure and detecting SAVs and issues. And then I worked on Bootcamp, and then I worked on messaging and groups. I had this really funny thing. I was kind of joking it was like, for those who are old enough to remember Karate Kid, I felt like I was painting a lot of fences, waxing a lot of cars, and at the end I knew karate. I was like at the end, at the end I had the payoff, because I'd gone through and I'd met a lot of people and I'd worked in these different areas and I understood different dynamics. Well, other people who joined in my cohort were getting promoted, but they were in a single track. They just stayed in one place and they got promoted, whereas I kept moving around. And it probably at some point early in my career felt like I was moving more slowly relative to my peers. And then when I finally turned the corner, really with the ads appointment, which I did for five years, I went vertical. I just like my career went vertical. And since then I've kind of been on that trajectory. And so advice I most often give people, for me at least, the lesson that I take from this, is I just was willing to learn aggressively. I would move because I wasn't learning enough. I was bored, and so I wasn't learning enough new stuff. And what was cool about finally getting to the ads job, and likewise in the job I'm in now, is those jobs, I learned a ton for five years. I'd never stopped learning in those jobs. You will occasionally find those jobs where they're super deep and you can just keep learning.

(00:40:50):
Meanwhile, a lot of my friends whose careers were on a better trajectory [inaudible 00:40:55] then earlier, they literally got bored of what they were doing, but they didn't have any place to jump to. There wasn't some other... They'd become domain specialists in a domain that they'd kind of exhausted for themselves. And maybe they'd even stuck around longer than they wanted to because it was comfortable or because the company wanted them to. And it ended up kind of being a hindrance to them in the middle of their career. And so for me, it's like, "Jump into new things, give it six months. If it's not the thing, no problem. You just built a ton of new skills that's going to come in handy, I promise you that. Keep going." And likewise, when you do make that jump early career, optimize for learning, optimize for... Think about a compound interest. It's like the first 10 years of compound interest don't look that impressive. It's like after 10 years it starts to look good.

Lenny (00:41:43):
I love that advice. It's similar advice I always give of, "Variety of experience often ends up being the most valuable thing you build over time," just trying to bunch of stuff, doing some internal tools, maybe working on customer support, I don't know, trust and safety, user-facing products, infrastructure. I'm thinking from a PM's perspective, maybe an engineers, and other functions. One question along those lines. So we talked about the eye of Sauron and working on the most important thing at the company. Do you have any advice on how much of your career you should be working in that center?

Andrew ‘Boz’ Bosworth (00:42:12):
Yeah, listen, [inaudible 00:42:12] being equal, I think there's two really good places to be. I think one is carrying a lot of water in areas that the company's not paying attention to but you are important. And it needs to be a lot. You got to own that stuff and really move mountains over there, because I promise you, as an executive, when there's a huge dam holding up the floodwaters, you respect the heck out of the person who is holding that dam up. You're like, "You keep doing that, Atlas, that is good work over there." The second-best place to be, or maybe equally, is on the most important thing. And on the most important thing, that's where you get to the advice that Eric Schmidt gave Sheryl Sandberg, which is like, "Hey, it's a rocket ship. Get on. Don't ask what seat I'm in. Just get on."

(00:42:59):
If it's the most important thing, you're going to get a smaller piece. Everyone wants to be there. Get the piece. If it's the most important thing, get the piece that you can crush, kill, do a great job at and grow from, because you're going to get a ton of visibility, you're going to get a ton of experience. You're going to see what it looks like in the fire, in the fire, and that is invaluable. You will use that everywhere. And so I say that. That's at project selection time, but now I'll be cautious. Understand, projects that start in the fire, hopefully, are forged in some manner of metal that cools and is no longer in the fire, like God willing. And likewise, things like dams that are holding up floodwaters have a tendency to crack or break or floods overcome [inaudible 00:43:42]. So I think you do want to be at selection time in one of those two places, but then you also... You're going to stick with the ride.

(00:43:50):
And again, to my point, if you're not engaged, if you aren't doing great work, if you don't love it, then move on. If you've exhausted it, you used to love it, but you don't anymore, move on. If you still love it and you're engaged, great. That's cool. That's a great thing. You deserve to go from the forge to the dam and back over time. You don't have to always just keep jumping onto the latest fire. I tried to do that once, after the ad [inaudible 00:44:14]. Actually, so I spent six months and we built the first mobile ad product in 2012 and kind of saved the IPO, which had gotten pretty grim [inaudible 00:44:23]-

Lenny (00:44:23):
Yeah, I remember that.

Andrew ‘Boz’ Bosworth (00:44:24):
... that point. And I told Mark, I was like, "This is so fun. Maybe you can just keep doing this, just putting me on the biggest fire every six months." And he turns to me, he said, "Buzz, that's not a real job."

(00:44:32):
He's like, "I need you to stay here and usher this forward," which I did for the next four and a half years. And it was amazing. It was amazing. And again, I do give him such... It's funny, I'm going to get a hard time in this. One of our biggest critics as well as being one of his biggest fans. I have both those jobs, but today we're talking about stuff that I think Mark really demonstrates really well. And he did a great job of pushing me in my career to different places where I didn't think I could succeed. And he saw the opportunity that made it happen.

Lenny (00:45:01):
What have you learned about that, giving Mark negative criticism, anything that he accepts? What do you learned about that?

Andrew ‘Boz’ Bosworth (00:45:08):
Mark's voracious for all information and all points of view. One of the things that's pretty interesting, I talked earlier about how much, as a founder, I think especially, you have to have tremendous conviction. You just have to have a tremendous degree of confidence. And I think Mark is somebody who is maybe the strongest willpower of a person I've ever met, just in a pure willpower sense. One thing that's interesting about Mark is you'll give him feedback, he listens. He's a kind person to work for, so you'll give him feedback, and he'll listen. Truly. He'll most often tell you that you're wrong, why you're wrong. That's just like most often. And what will happen is... It's uncanny. It's like over the course of the next week or two, you'll just see shifts. And I don't think he's doing it...

(00:45:55):
I've always joked that the information gets to him. So much information every day gets him. And then at night, he re-compiles the whole world with all that information and comes back. And by the way, this is not just true about product work. In my head, I was thinking about product stuff where he was like, "Hey, I think this product is doing this wrong." He's like, "No, no, that's why it's not that way." And the product will start to shift. Also to give him feedback just on his own presence in a meeting or delivery, he'll be like, "Oh, well here's why I did it that way." And then a couple weeks later, you'll get in a similar situation, and he will moderate how he shows up. So I actually find him somebody who's really satisfying to give him feedback. It really works. It's very effective, but you do have to take the long view on it. And he will have a... The things he did, he didn't do an accident. He will have a reason why he did them the way he did them.

Lenny (00:46:39):
It's a great example of strong opinions, loosely held.

Andrew ‘Boz’ Bosworth (00:46:42):
Yeah, that's right.

Lenny (00:46:44):
It also makes me think, I think you used the compiler analogy. I'm thinking the model training. He's retrained his model overnight.

Andrew ‘Boz’ Bosworth (00:46:50):
Yeah, that's right. It's funny. One of the things that's so funny about Mark is if you give him some feedback in the morning, the next six meetings he has, whether it's about that product or not, he'll ask people what they think of that feedback. He won't attribute. He's just like, "Hey, what do you think about this in this product? And so you'll be in a meeting with him and you'll see him doing it. He'll come to the meeting with you about some other topic. He'll be like, "Hey boss, what do you think about this product and this idea?" And so he will, over the course of the day, take that little note and kind of pressure test it, and he loves to triangulate. Where are all the points of view on this that maybe you didn't see? So he really values a broad perspective on each thing that's being discussed, which is really fun.

Lenny (00:47:29):
Trying to get more training data for his model. I get it.

Andrew ‘Boz’ Bosworth (00:47:32):
You can't get me to call Mark an LLM. That's not fair. That's [inaudible 00:47:35].

Lenny (00:47:35):
We could all hope to be as smart as Mark. As you were talking, I noticed your tattoos, and it reminded me that you've got at least two tattoos that I'm aware of.

Andrew ‘Boz’ Bosworth (00:47:35):
Oh, yeah.

Lenny (00:47:45):
One is of California, which I completely understand. California is a very special place, but you have this other tattoo that is just the words Veritas. Can you talk about what that's about and why that's important to you?

Andrew ‘Boz’ Bosworth (00:47:58):
The funny thing about tattoos in general is I came out of high school, I was like... I don't know if there was an archetype for me, but I didn't drink until I was 21. I was a very rule-following person. I was like, "Why are you going to get a tattoo, affect your body? "Why would you dye your hair? Just let it be what it was." And some of this was I think I was somebody who was privileged and had a great deal of self-confidence in who I was and what I wanted to be, and that was fine. But in some ways I was also weirdly judgey about other people in a way that's kind of off- brain for me, certainly today it would be, but at the time, getting a tattoo is a big deal for me. I was like, "Oh, this is just the vehicle for my life and you can do whatever you want with it. And it's not like a... It's something that you possess, and if you feel like if you want to decorate it, you can decorate it.

(00:48:47):
And so getting a tattoo was a big deal to me actually, and I completely shifted my mindset of how I thought about my body and how I thought about people's body and their presence and their time, maybe to some degree, even an understanding of mortality. Like, "Hey, can't take it with you. It's all going to go..." When you're 18, you think you're going to live forever, and by the time you're 22, a grizzled 22-year-old veteran, you're like, "Ah, tattoo that bad boy up. It's all going down." And so yeah, that's why I got the Veritas tattoo, which is Latin for truth, which is... I will say it's a little cheesy, because it's also Harvard's motto. But I got it in a monotype font. This is the programmer's font here.

(00:49:28):
The other thing that's interesting to me about tattoos was it's also part of a generational shift. We grew up in a time when tattoos were really seen by adults as gangs or bikers or sailors or certain types. Now my understanding, I saw a stat recently that more people in my generation have tattoos than don't have tattoos. And so I think we also just culturally shifted positions in a way that... I find richness of self-expression wonderful. I really think it's great. And so I'm here for all of it.

Lenny (00:49:56):
My assumption from what you're describing is, this idea of truth is very important to the way you think and work.

Andrew ‘Boz’ Bosworth (00:50:01):
My reputation does precede me on this point, I'm afraid, which is... I think when I was young, I saw being honest... And I was wrong by the way. I saw being honest as kind of a get out of jail free card. You could say whatever you wanted as long as you're being honest. That's just not the case at all. I've written about this before, but by far my biggest professional regrets were me not being kind. And I used to think... I wrote this note a while back called Be Kind, where being nice, that's like patronizing, or telling somebody things that are half-truths or just getting by. And I'm against that. But being kind isn't that. Being kind is like, "Hey, how can I deliver this feedback in a way that is actually productive and helpful, in a way that is going to help them and not cause them just to feel bad and helpless?

(00:50:50):
And I think I did that wrong a lot as a kid, as a young man. And so being honest is still a big part of my personality. No one would ever accuse me of being dishonest who knows me. And I think people understand and respect that I'm pretty direct, and if I have concerns or issues, I'm going to bring them up. I'm just much better at bringing them up now and expressing a true care and belief. I wouldn't bring it up if I didn't think we could do better, if I didn't think we could fix it, if I didn't believe in this situation. And so being honest is still a huge part of my identity, and I think that's something I'm very proud of. But I will say the contextualization of how I'm honest has changed immensely since I got this tattoo.

Lenny (00:51:29):
That seems reasonable. This touches a little bit on something I definitely wanted to talk about, which is one of your most classic pieces, and this is the way I first learned about you, is a piece that is called Communication is the Job.

Andrew ‘Boz’ Bosworth (00:51:40):
Yep.

Lenny (00:51:41):
I know many people have read this, many people haven't. I'd love for you to just talk about what this means and why this is important, why this is something that you wanted to share.

Andrew ‘Boz’ Bosworth (00:51:49):
Yeah, it's one of the things that, especially if you aspire to be a leader... And leadership isn't management, and leadership isn't being the only person responsible, it's not even always the same as accountability. But if you want to have an impact...

Andrew ‘Boz’ Bosworth (00:52:00):
It's not even always the same as accountability, but if you want to have an impact on the world around you, it is exclusively done through the creation of artifacts or verbalizations that affect other humans. That is all there is. That's all there is if you want to have an impact, if you want to create some kind of a lasting change. And it could be in your little relationship, it could be in your team, it could be in your company, it could be in the world. It is down to communication. And so often you hear people saying, "Oh yeah, I wrote that up a year ago." It's like, "Yeah, but you did a bad job of writing it up a year ago, or we would've not wasted a year not doing it."

(00:52:47):
People always think that's, "Oh, I had that idea," and that's means anything. It means nothing. It means absolutely nothing. Or it's like, "Oh, I wrote this post." Well, you didn't break through with it. That's on you. It's not on the audience. People want to blame the audience. Well, the audience is just there. I mentioned this even earlier, and I hope people caught it, when I said, "Hey," I give somebody a piece of work and they come back six months later and they have done the wrong thing, I'll take the L. I will take the L on it. It's not great for them. They'll be pissed they wasted their time, but like I said, that's my responsibility. I did not communicate clearly what I wanted, what the expectations were.

(00:53:25):
Could they have also helped themselves? Sure, they could have, and that's a thing that takes all sides. We should work on this problem for both angles. I have another post called Listening is the Job, which is the other side of this. But communication is the job is, I really believe... Actually, it's the relationship to this idea that came out of the US Marines and the SEALs of extreme ownership, which is... So whenever thing goes wrong, I ask myself, "What could I have done differently in terms of how I communicated things for this to have gone better?" Could I have set priorities better? Could I have set expectations better? Did I need to have a better metric that I pointed the team at? Did I put the wrong people on it?

(00:54:04):
By the way, the thing I talk about is org charts are communication devices. They don't exist. There's not a physical string between you and your manager. They're just communication tools that are supposed to give people a rough sense of how things are organized and where to go with who. And so all these things are communication. Silence is communication, me not reaching out to you to check on you, to check on your project. We talked about the [inaudible 00:54:29] earlier. What does that mean? That means trust. That means responsibility. The absence of check-ins has meaning. You cannot not communicate. You are always communicating something with your face, with your clothes, with your body. What are you communicating?

(00:54:45):
I'll give you a funny example, which I hope we get to put in the podcast, because if you're watching this on video, you will have noticed that my camera cannot stop adjusting light. It's just constantly too dark or too bright. I'm trying a new camera. I'm a nerdy guy. I try a lot of camera gear, I try a lot of microphone gear. I love to have all the latest gadgets and gizmos, so I'm trying something new. It's not working. And in my head I'm like, what is this communicating about me? People are going to think that I don't care or that I'm not competent.

(00:55:15):
That's what I'm talking about. And now, I felt compelled to explain it in the podcast so that I can communicate clearly that that's not the case. I really just think so much of what I try to do in my professional life is understand the mental model of other people. Where are they right now? And I mean specific people, like my managers or my key technical leaders, and I mean general people like teams, and I mean broadly just the average human. Where are they at in this conversation? And how can I craft my language, my presence, my persona, everything to usher them from where they are to where I want to get them?

(00:55:52):
And that requires me to have a very clear idea of where I want to get them, have to have a clear idea of where they are. And I want to tell you, it's not as much work as it sounds like. I think no one would accuse me of having this big fabricated persona. It's not that. But it is having tremendous empathy for where people are starting. That was the lead for me. All the rest of it, all the rest of how I show up in meetings trying to smile more, because I'm like a big scary guy, those things are little things that you work on and they become second nature and they're easy. The hard thing is just having the empathy for your audience and being, "Where are they? Where are they starting?" And when you miss taking responsibility for that, extreme responsibility for that.

Lenny (00:56:31):
There's so much good advice in that. There's so many threads I want to follow, but let's just follow this last one of trying to understand how someone is best communicated to. Is there an example to make that a little more real for people of just what you've done to, "Oh, here's how I'm going to communicate with this person?"

Andrew ‘Boz’ Bosworth (00:56:46):
I'll give you a couple. One is multimodality. There's an old saying, repetition never spoiled the prayer. And I think most experienced communicators, whether they be writers, whether they be public speakers, talk about the importance of reiterating a point several times and in several different ways to make sure that people have a chance to internalize it. You want to use it, you want to say it directly, you want to use metaphor. And so for me, I will give an all-hands and then write a post with the content of the all-hands, because different people are going to respond differently to these modalities and are going to absorb information at different rates on these different modalities. That's a trivial one.

(00:57:23):
Another one that I think of all the time is making sure that you address people's fears and concerns. People will not listen to you if they think you don't know what's going on. And so, one of my favorite things to do when we're talking about some kind of issue is right up top and say, "Hey, let me be clear. This is the issue we're having. I know we're having it. I know what matters." And then I'll say the same thing that I would've said, but they would've literally ignored me, because how can they trust my conclusions if they don't accept the premise? You know what I'm saying? I think there's a whole piece there. Obviously when you're in person, it's a lot easier because you're reading facial expressions. Even on this, I'm reading you nodding on that. I'm like, "Okay, he's with me." And then I throw in a, "You know what I mean?" Whereas if you give me a cocked head, I then bring a second example to try to drive the point home. But you build yourself up. Most people are going to realistically start in their careers trying to influence one or two people. That's where you start. One or two people. That's who you got to communicate with. Your manager, one teammate, that's who you got. And then you build up and build up and build up a skillset to do it at a larger and larger scale.

Lenny (00:58:36):
I love so much of this advice. I think it's also helpful for relationships. "Here's what you're upset about."

Andrew ‘Boz’ Bosworth (00:58:42):
Totally, a hundred percent.

Lenny (00:58:43):
"Here's what I think we can do."

Andrew ‘Boz’ Bosworth (00:58:46):
Again, the work that I've had so graciously supported to do on myself at Meta with great mentors, Sheryl Sandberg, Mark Zuckerberg, a bunch of others and coaches absolutely made me a better partner and husband, and my wife. And then by the way, vice versa. Having kids and getting deep in the literature around raising children. Congratulations to you, by the way. Getting deep in that literature made me a better manager. Absolutely made me a better manager in terms of thinking about how people are managing their emotions and how to engage with them in those times.

Lenny (00:59:16):
Amazing. We need a second edition of this Boz's Parenting Advice.

Andrew ‘Boz’ Bosworth (00:59:19):
That's right.

Lenny (00:59:20):
And relationship advice.

Andrew ‘Boz’ Bosworth (00:59:21):
It's all the good stuff. No bad kids, Lansbury, it's good inside, Dr. Becky. It's all-

Lenny (00:59:28):
I like Dr. Becky.

Andrew ‘Boz’ Bosworth (00:59:28):
I really think that the modern parenting canon is really rich.

Lenny (00:59:33):
Amazing, so much good content. This episode is brought to you by Explo, a game-changer for customer-facing analytics and data reporting. Are your users craving more dashboards, reports, and analytics within your product? Are you tired of trying to build it yourself?

(00:59:49):
As a product leader, you probably have these requests on your roadmap, but the struggle to prioritize them is real. Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Explo. Explo is a fully white-labeled embedded analytics solution designed entirely with your user in mind. Getting started is easy. Explo connects to any relational database or warehouse, and with its low-code functionality, you can build and style dashboards in minutes.

(01:00:18):
Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part, your end-users can use Explo's AI features for their own report and dashboard generation, eliminating customer data requests for your support team. Build and embed a fully white-labeled analytics experience in days. Try it for free at explo.co/lenny. That's E-X-P-L-O dot C-O slash Lenny.

(01:00:47):
Okay. You mentioned this gadget and these cameras you like to play with. Let's talk about the Vision Pro and VR headsets. Have you tried the Vision Pro? Thoughts?

Andrew ‘Boz’ Bosworth (01:00:57):
Actually, Mark and I tried it together and I want to say, first of all, when the headset came out, we breathed a little sigh of relief because the stuff inside of it didn't represent a fundamental breakthrough. Everything inside of it was something that we probably could have gone and done, with the exception of Apple silicon, which is a marvel, but it's worth nothing. Apple Silicon is like a 2X marvel when doing things like scaling display resolution is unfortunately a quadratic proposition, and so a 2X linear scaling advantage doesn't buy you as much as you might expect when you're trying to scale resolution. And so that was step one. But we still assumed at that price point, with their legendary attention to detail and polish, they probably produced a great product. And the line that I said actually my own podcast with Matthew Ball a week ago was, "Look, I was prepared to come to market and say we have the best value headset. If you want an outstanding, best possible headset for the money, we've got it. It's the Quest 3."

(01:01:55):
And I was so thrilled when I tried the AVP next to Mark, we were like, "No, we think we have the actual best headset." Now, we're not saying it's the best at all things. If you're sitting still and watching a movie a high-res movie, Apple Vision Pro is really great. It's really great. The resolution shines. The way they've tuned the pass-through shines if you're stationary and looking straight ahead. And they've done some really nice things with the UI. It's one of these things that we do get annoyed about, a mile aside, we get a little bit annoyed about as product people.

(01:02:31):
I know that this happens to all of us. It happens to Apple, happens to Google, happens to us. We have a bunch of internal things we've been playing with, which will at some point ship and we will be accused of having stolen them when we actually did not steal them. If you want, you can go see my Quora answer on the history of the like button where this happened previously, where we had built the like button internally before it was launched elsewhere. Anyways, it's a whole thing. This happens in our industry a lot, and I really shouldn't care as much. It's a little bit of my ego peeking through, which I should control and tamp down, if I'm being responsible.

(01:03:03):
The beautiful UI polishes, they did a tremendous job with eye tracking. One of the things that's interesting about the eye tracking is, to do it the way they've done it, that's why you have to have the prescription insert, so it doesn't support your glasses. You have to get prescription inserts. They're expensive. And they can shoot the cameras that track your eyes through the lens as well as the light around it. Ours go from the side on the Quest Pro, and that allows you to wear corrective lenses.

(01:03:27):
And so different choices like that have trade-offs, but it's still cool. It's great that they got that in there. At the same time, our hand tracking is better. Obviously, the app library we knew was going to be better. That's not totally fair to them. They've just launched and they have small volume still, but I just find the comfort... The thing that really got me the most, the field of view is really small on the Apple Vision Pro. And some people are characterizing it incorrectly on the internet. They're doing a characterization up close to the lens. Once you factor in the eye relief, the distance between where the lenses are and your eyeball is, their field of view gets pretty narrow for almost all faces relative to ours, which I find distracting.

(01:03:59):
Their displays are much dimmer than ours, and I find the motion blur really distracting when I'm in mixed reality use cases. And as I mentioned earlier in the podcast, I'm a huge mixed reality buff. I'm a huge fan of that potential for exactly the same reason that they are, by the way, which I think hands and mixed reality make it feel much more accessible to more people. I'm pretty glad we have the controller in our set though, because it really expands what you can do. And we don't just operate our computers with just one thing. We have a keyboard, we have a mouse, we do multiple modalities all the time. I really feel like the comfort, the lack of persistence and motion blur in our pass-through, the brightness of our displays, I was like, "Oh man, if you gave me one to take, I would take Quest 3."

(01:04:40):
Now, people have rightly said, "That's pretty biased." Of course it is. Go get your own opinion. But what kills me is most people haven't done that. They have not tried the Quest 3. That's what kills me the most. If you go and try Quest 3, ask yourself if you'd rather have seven of those, one for you and six of your best friends, or one Apple Vision Pro. I'm sure the answer isn't Quest 3 for every person. There are people for whom there are use cases that really fit their life, the Apple Vision Pro, I'm cool with it.

(01:05:05):
But people don't even know that the Quest 3, you can do Remote Desktop. You can do it both through an app called Remote Desktop, which is very popular, or you can go into workrooms and you can have three monitors surrounding you streamed from your machine. I think some of this is just people have not even done the work. They haven't even tried it. I welcome all of you who think I'm biased to prove one way or the other what you think, but don't do it without putting the Quest 3 on and giving it through its paces, because it's a pretty great device. And you can do a lot with $3,000 extra dollars.

(01:05:38):
How did they get away with that, by the way? We launched a headset that was $1,299 and people lost their minds about it. They're like, "Ah, $3,500, it's fine. This is fine. No one cares." I don't know. Fairness is too much to ask, and I don't care about that. Apple has earned the great brand that they've built. They truly have. I think it's tremendous. I certainly celebrate a large number of Apple product. I'm a huge fan of their work. I'm a huge fan of what they do. That's probably why I expected more from the AVP.

Lenny (01:06:06):
Well, I'll show you my favorite AR device, which is these Ray-Bans. I actually bought them.

Andrew ‘Boz’ Bosworth (01:06:13):
Yeah.

Lenny (01:06:13):
Here, I'll put them on it. Here, what I'm going to do is I'm going to record. I didn't tell you I was going to do this. I'm going to record this as we're talking. Look at this.

Andrew ‘Boz’ Bosworth (01:06:20):
I like that. They look so good on you too. This is a good fit.

Lenny (01:06:23):
My mother-in-law's like, "You look so sophisticated. You look really smart with these on." And we bought these actually to film our kids, or our kid, instead of having Cameron's face. And it's been awesome.

Andrew ‘Boz’ Bosworth (01:06:34):
It's really the best. It is so hard to look at a phone screen and have the real thing be in between you. No, the glass is the way to do it.

Lenny (01:06:43):
Look at this, my new look. I'm just going to have glasses on all the time.

Andrew ‘Boz’ Bosworth (01:06:46):
We got to get you the multimodal. I've been playing with that since December, where you can use the camera to ask a Meta AI assistant about things. It's really good. I was in a ski village recently with my family and I had them on. I'm just like, "Hey, take a look. Tell what you see." And I had found a sign and it gave me directions. "Hey, the bathrooms are down those stairs to the right. Do you want food? It's over to the right." It couldn't tell what village I was in, but it was like, "You're in a ski village somewhere. Here's the amenities." And I was like, "Wow." There's something real magical here.

Lenny (01:07:18):
I feel like I need this for my podcasting interview so I could just have a little voice tell me questions to be asking and where I'm at.

Andrew ‘Boz’ Bosworth (01:07:25):
Right, totally. Yeah.

Lenny (01:07:26):
How helpful would that be?

Andrew ‘Boz’ Bosworth (01:07:27):
Okay, I'm going to cheat on this one and say, obviously we've been talking for a while, but playing with glasses that have full AR capabilities, and we've got one that has rumored to be coming internally soon, so heavily rumored in fact that you might even say it's almost been confirmed. And what's been really fun is being able to play with these time machines, really, in terms of what they are. It's amazing technology. People were giving us speeches, big company-wide speeches, and had all their notes on the glasses. And they could control the slides just using a gesture.

Lenny (01:08:05):
Oh my God.

Andrew ‘Boz’ Bosworth (01:08:07):
There's exciting things afoot. The future's looking pretty bright.

Lenny (01:08:10):
Something that I wanted to touch on, which is when Mark put out this whole video of, "Here's what I think of Apple Vision Pro versus the Quest," a lot of people are just like, "Oh man, because he's putting out this video, he must be so afraid of what's happening and it's not the right move." What went into thinking? Was there strategic thinking there? Was it just him, "Here's what I think?"

Andrew ‘Boz’ Bosworth (01:08:29):
This guy does [inaudible 01:08:30] about the modern era. Everyone's in their Meta head about everything. Everything's a four-dimensional chess. That was just what Mark thought of the thing. That's what he thought about it. I think he wanted to make sure people remembered, hey, Quest 3 is literally a better device, and people haven't even tried it.

(01:08:46):
And so we're not always playing four-dimensional chess over here. Sometimes we're just like, "Here's a thing that I believe is true. I'm going to say it out loud with my mouth." That's what he did. It's not that hard. When I do it, everyone expects it because of my persona or brand or whatever the thing is. I guess people are surprised when a CEO does it. All right, I get that. That's cool. There's other sets of societal expectations there.

(01:09:08):
And we're all familiar with Apple putting the Welcome IBM ad in the New York Times, and then Slack doing the same thing with Microsoft and the Ballmer iPhone comments. None of those were true discussions of the technical merits of a product. Those were all just big, rally the troops gestures. This is not that. Mark is deep. He's an expert in this stuff. I'm an expert in this stuff. I feel great about our choices.

(01:09:39):
By the way, when I've used it, I could get myself completely into the head of the person who designed it. I can tell you from using it what instructions they were given, that team was given. I can tell you what they were optimizing for. I can tell you what constraints they were under. By all the choices they made, I can tell you all those things and I understand it coheres in that way. We made different choices. It shouldn't surprise anyone. We like our choices better. We could have made those choices. We didn't make those choices. We made these other choices.

(01:10:06):
And so for me, the weight, the wire, which just always brushes against my ear, the pocketable thing, I get it. That's not what I would've done, and I know that because I had the chance to do it and I chose not to. I don't know. I don't know why people are surprised. This wasn't some big, savvy strategic move. This was just, Mark's got a chance to use it. He's like, "Oh man, I think we should tell people what the real story is here." And we did.

Lenny (01:10:34):
I love that insight. And I know a lot of people watching are like, "Oh, shit, he's right. Wow. I didn't think of it that way." And so I think it had a lot of that impact.

(01:10:41):
I want to zoom out a little bit and talk about Meta's journey over the past couple years. It feels like there is a huge downturn in public perception of Meta and the stock price, and then over the past couple of years there's been a huge turnaround. And it feels like there's always a lot to learn from these periods. Just as an example of the stock price, I was just looking at it, it was down to $80-ish, and now today it's $487.

Andrew ‘Boz’ Bosworth (01:11:05):
Yeah.

Lenny (01:11:06):
I'm curious just what you've learned from going through that downturn and turnaround. And I know it's still in progress, but just what have you learned from that journey?

Andrew ‘Boz’ Bosworth (01:11:16):
Yeah. Well, there's a lot to take away, I got to tell you. I think we had the largest single day stock drop in history, followed 18 months later by this largest single day gain in stock market history.

Lenny (01:11:27):
Oh my God.

Andrew ‘Boz’ Bosworth (01:11:27):
As the legendary Lou Holtz said, " You're never as good as they say you are when you're winning, and you're never as bad as they say you are when you're losing." Mark has always brought that quote out to guide us internally to try to insulate ourselves a little bit from the vagaries of external opinion. And that's not just true with stock prices. That's true with media and press. It's true across a lot of things.

(01:11:53):
One of the things I told my team, and I still have to repeat it to them, is, "One of the things that's hard to remember when you're in it is that you know more than the critics do. You know more than the analysts in the marketplace do. You know more than the media does. You know more than the podcasters do. You know more than the Twitter does. You know more about what's real and substantial of value about our company than they do. That doesn't mean ignore them, because they have a different perspective and you need to understand it. Even if the totality is less than what you know, it may contain parts that you do not know." I'm a huge fan, I read the criticism of everything, and I read it very carefully, looking out for confirmation bias, looking out for things that I might be inclined to resist but are maybe true. I invite all critique, but I also don't accept the critique blindly. I don't just say, "Yes, this is obviously true."

(01:12:55):
Gell-Mann Amnesia is a great concept for everyone to understand. Gell-Mann Amnesia is this property where you'll read a newspaper article, let's say newspaper, why not, about a thing about which you are an expert, and you'll be baffled because here is an article that is not just wrong, it's inverted causality. Michael Crichton, I'll steal Michael Crichton's quote on this, "It's a wet sidewalks make rain story." And you'll be like, "What a terrible, bizarre story."

(01:13:22):
And then you will turn the page of the newspaper and it will be another article about a topic about which you know nothing, and you will read it as if it is the gospel truth. You'll figure it's, "Oh, no, look at this information about this foreign situation." Like I said, perfectly true. We should be smarter than that. And so does that mean you don't read the thing? No, you read it. You just read everything with that perspective of, "Wait a second, this is another point of view. And how do I integrate that into a whole perspective that I can have and be informed about?"

(01:13:55):
The first, the macro thing is taking the long view, realizing that when you're in the dumps, it's not as bad as you think, when you're at the top, it's not as good as you think. It's somewhere in between at all times. The second thing is communication is the job. We really did not communicate effectively, I think, with the market around our future investments. And listen, we've had two 10-year long huge investment areas. One has been AI, one has been reality labs. And AI's looking pretty good today. I can't think we can all agree with Lama 2, with Fair, the breakthroughs that we've had.

(01:14:33):
People don't notice that Fair, our AI research lab, is the second most cited research lab in AI behind Google. We've been doing this work. We didn't come here casually. We've been doing it, and so that's looking pretty good. I don't think we did enough to explain those best to people. Previously, the core business was going strong enough and they were willing to ignore them. And with the old Warren Buffett quote, "It's only when the tide goes out, we see who's not wearing swimming trunks." And so when the tide went out, when you have the Ukraine war and an interest rate hike and recessions, now everyone's scrambling for that incremental dollar and they're like, "Go get rid of this stuff."

(01:15:15):
And we had to tell the company, "You don't want to work at a company that, when times are tough, kills all future growth and just shores up in the core business." That's a company that's just committing itself to dying at some point, a little later than expected, but dying at some point. You want to work at a company that has a balanced portfolio of investments, which we had. We didn't explain that well, and so we spent that time explaining that to the market, to the press, to everybody.

(01:15:38):
And now, I think as people understand the size of it and the scope of it, and of course it helps that the core business has overcome its challenges there from ATT and the other kinds of stuff, it's looking pretty good. I do think one part is, as an internal person, really moderating your attachment to the external narratives and swings, that's super important. And you do that based on understanding your own expertise. And the second part is understanding why is there a delta. What is there? And grab that. It's usually communication.

Lenny (01:16:10):
There's also a big flattening of the org. This was something a lot of people talked about, where managers became ICs. Is there anything more there that you've learned of just how to adjust the org to be more efficient?

Andrew ‘Boz’ Bosworth (01:16:22):
Of course, and I should have included that in the first section. I was a bit eager to wrap it up elegantly in the two. But you're right.

Lenny (01:16:27):
I appreciate it.

Andrew ‘Boz’ Bosworth (01:16:29):
We made significant shifts in how we operated the business, which was super painful. And listen, this goes back to the boom times of COVID, when it looked like there was a real lasting secular shift in things like e-commerce and in working remotely and these tool sits, which are exactly what we build, and it's primed us. And so we built up a huge workforce to pursue those opportunities. We still believe in those opportunities, but they're back on their original timeline. And actually, literally, if you look at a bunch of graphs that we have internally, it's literally the COVID boom and then, not bust really, but as it receded, everything's back on its original trajectory.

(01:17:16):
We didn't lose ground or lose time, but the pull forward didn't happen. Well, that means your economics don't make any sense anymore. Now, you made a bunch of investments that are going to yield too distant in the future, and getting there faster isn't going to help you and you're carrying a much extra cost. That sucks, man. It sucks. And we don't feel great about it. We really don't. It's a business, it's awful, and it happens.

(01:17:41):
I do think one thing that was interesting about that time was, for those of us who grew up and saw the .com boom firsthand, I was born and raised in the valley, so that was all around me when I was graduating high school and going to college, and then in the 2008 major recession on the housing crash and on the market and all that stuff. Now, let's imagine you graduated college in 2009-

Andrew ‘Boz’ Bosworth (01:18:00):
... all that stuff. Now let's imagine you graduated college in 2009 and got a job. Well shoot, you're 15 years in your career, you could be a director and you've never seen a downturn. I think we also had, in addition to what was very unfortunately conventional mis-forecasting in the business that caused us to over hire, that we had to correct for. You also had a workforce that was just not at all of a mentality that this could ever happen. This felt like it was an act of God when in fact it's like a cyclical nature of all businesses that this will happen at some time and you hope it doesn't and you wish it didn't, but you have to deal with it. And so I think we have a bit of a tough storm there for the whole industry and we're still feeling it. I think we're still feeling it.

(01:18:45):
Certainly we're happy at Meta to be beyond that point and we're growing again and executing at a stable rate and feeling really good about that, but quite a few of our other companies in the industry. And it's a very uncertain time for engineers, for PMs, for designers, for everyone and all the support functions around them. I'm super sympathetic for that. I think obviously the mis-forecasting that happened inside of Meta's walls happened everywhere and now that you have, especially with higher interest rates and cash isn't as cheap, runways are tighter. People are just making those pragmatic calls. I think we'll rally back from this. I think this is a normal thing that happens to industries, but it doesn't reduce my sympathy and empathy for those who have been affected by it or who live in fear of it.

Lenny (01:19:29):
I was talking to a friend who works at Meta and I was asking them what it's like to work at Meta and she was just like, "It's intense, and it used to be more chill. There were people that were coasting here and there," and now she's like, "No, all those people are gone now. It's just only the intense people left and we're working really hard." Does that bring up anything?

Andrew ‘Boz’ Bosworth (01:19:48):
Yeah. I don't want to comment on people who left. People left Meta for all kinds of different reasons and likewise role elimination happened in many cases because we just decided not to do this work at this point. We were going to do it two years from now and don't need to carry a team to do it. I think it's really hard to generalize because each of these is a specific person with a specific life and a story that is rich and deserves to be told. But I do think that if there was somebody coasting and you as a manager have to make tough calls on who you're bringing in which way you're going to bias my profound suspicion, and again, I don't know your friend who you spoke with, my profound suspicion is that person's probably already working hard. You know what I'm saying? That person's already probably working hard. I don't think we changed how hard any individual worked. I really don't believe that.

(01:20:35):
I do think there was a selection bias as to what was going to happen, and I think that's probably what you saw play. In fact, if there is a generality that can be found.

Lenny (01:20:43):
Maybe as a last question, I have this segment where I call Failure Corner where I ask people to share a failure of their career and what they learned from that experience. Is there something that comes to mind?

Andrew ‘Boz’ Bosworth (01:20:55):
I've failed tons of times. I've built products that nobody used. I've built technical architectures that didn't scale. I've failed all kinds of times. I don't regret most of those. Almost every one of those I learned from. It was a stop on the path to a better solution or it was a recognition that this thing wasn't going to work ever, which is its own kind of a gift. All the failures that I regret, that I take seriously are personal failures where I affected a person in a way that I'm not proud of, maybe wasn't proud of the time because I wasn't in control of my own emotions or mood. I was feeling fearful, I was feeling scared, and there's a bunch of these one or two that stand out that I don't feel comfortable sharing because the person affected, I think would prefer I didn't share.

(01:21:46):
I'll share one that was... I think the person's and I are tight now. We have this really silly discussion. I remember it so vividly. In the early days of client server architectures, which Facebook obviously is a website, so you're calling to a server to get the webpage, but then that server is going to call the other servers to gather things and that was one of the major clients of remote procedure calls because newsfeed ranking was all done on this other set of servers that had its own special requirements and special build and how it was put together. And so your main web server would put a call-out over a remote procedure, call to the remote server and get a response back. And we had this really janky RPC system that, I won't say who built it, but it was built and it was just a piece of garbage constantly failing. It was not robust at all. And one of our best engineers, Mark Sleek, built a new one called Thrift. It was a great, really great RPC infrastructure.

(01:22:47):
And one of my best friends, Dave Federman, one of my really good friends and a brilliant engineer, we were talking about how to do the encoding and I was like, "I want it to be binary encoding." I was like, "You should binary encoding. I want it to be super efficient on the wire," because I'm storing these RPCs. They do two jobs for us, one of which is the active RPC, but I also store the RPCs in a log and replay them to do the work that we were doing in newsfeed ranking. That's how it was done back in the day. It was all kind of asynchronous offline and so I wanted to be as tight as possible. My memory bandwidth was very limited and memory was so expensive back then and Dave Federman was like, "No, no, no, that's short-term thinking Boz, we should be using Linux style descriptors that are plain English language. Then you could look at the log, you can see what it is. It's possible memory bandwidth will get cheaper, but these logs being scrutable to development is going to be a better thing." This is nerd bait.

(01:23:42):
Those of you who have been engineers in this call, this is like Vim EMX. This is nerd bait. This goes deep. This is like a long old thing.

Lenny (01:23:51):
I love it. Keep it coming.

Andrew ‘Boz’ Bosworth (01:23:52):
It's a room full of engineers at the company and the company's not that big, and so there's probably half the engineers of the company in this room. I was yelling. Literally I'm turning red, I'm sweating. I'm so angry at Dave Federman for countermanding my proposal and I'm the major RPC customer. A couple things. This is so dumb. Mark Sleek just built two encoders. It's not that hard. You pick which encoder you want for your things. That's the easiest solution ever. Second thing is Dave was right, by the way. Within a year, the memory bandwidth definitely didn't matter relative to how inscrutable it was to try to get into these logs. I had to build a ton of extra custom software to parse the logs and understand what what's going on. But also it was a case where my identity was caught up in being right. And for those who don't know, identity threat is just the biggest... Your worst behavior is always going to come out when you think you're under identity threat.

(01:24:51):
When you feel like some core part of how you see yourself is in question, you will react with every ounce of your fiber to defend that conception of yourself because it's so expensive to reconceptualize who you are that you defend yourself. So my identity was being right. [inaudible 01:25:08] on the wrist. And it caused me to take one of my best friends, one of the best engineers I knew, a guy I literally lived with and getting a really embarrassing for me conflict, which everyone was just scratching their head like, "What is going on with Boz right now?" I looked like an unhinged crazy person. I remember the room, I remember where I was standing in the room. I remember everything about that moment and I had to go home and be like, "What the fuck was that? What happened?" I'm asking myself like, "What happened there?" And that was one of the many steps in the journey to recontextualizing what it was was not to be right and what meant to be open-minded and curious and how to engage in this competition.

(01:25:47):
I was 22. I don't make excuses for it now, but I remember there was a couple other examples like that in things that were less technical and more personal that I won't share, but I remember each of them vividly and those are the real failures for me.

Lenny (01:26:01):
I love how this story is so long ago at this point and it's still stuck with you and such an impact, I think.

Andrew ‘Boz’ Bosworth (01:26:06):
Oh, my god, I'll never forget that. It was embarrassing. And for those, that's the old quote, it's really one of the truest quotes, and I know it's cliche and sometimes cliches are cliches because they're good. It's like, "People, they don't remember what you said. They just remember how you made them feel." That's all anyone remembers is how you made them feel, and I think in that room, I made people feel unsafe, maybe. It was bad.

Lenny (01:26:27):
I like this concept of identity threat. They call this podcast episode identity threat.

Andrew ‘Boz’ Bosworth (01:26:32):
There you go.

Lenny (01:26:33):
Boz, we started this episode with a billion questions. I have a billion and one questions now. I wish we could keep going, but I know we have to wrap this up. Is there anything you wanted to share or leave listeners with before we get to our very exciting lightning round?

Andrew ‘Boz’ Bosworth (01:26:46):
Well, in the off chance that we do end up labeling this episode, identity threat, let me give you what really was... I made a lot of breakthroughs with coaching, learning about the feeling inside of my own body when I was feeling that identity threat and learning techniques and tactics to reduce the likelihood I would feel it and how to deal with it when it happened and how to repair when I did, I went through all that stuff. I would say the greatest lesson I learned would come years later and it was just from observing somebody. Ami Vora who was a legendary, long time came in and worked on our development platform, then worked with me on ads for a long time and then was the PM lead for WhatsApp for a long time. She's since gone on to do even more great things outside the company. Working with her, it was like watching an alien because her and I were so different in our approach and she approached...

(01:27:38):
She could have the most profound disagreement with somebody in the world and they would say the thing that she thought was not just wrong, but crazy wrong and she would respond. She would say, "Fascinating. You have to tell me more about why you think that." And I can't do it justice, she meant it from the core of her being. She saw this schism between her and that person and it could have been personal, it could have been professional, it could have been anything. She saw this schism and how they saw the world and how she saw the world and rather than reacting as if it was a threat that somebody saw it differently or rather than reacting afraid that maybe she was wrong and had done things wrong before, she reacted with the most genuine and profound curiosity. I just watched it absolutely tear down walls between points of view. People felt immediately her genuine heartfelt curiosity and would lean in and that would cause them to be open-minded.

(01:28:36):
And if she was right, which by the way she usually was, then they would leave being like, "Oh, okay, I was wrong about that," but she also would change her mind and that was the key. Ever since then, I really have tried to model that. When I have a strong internal clinch, I try to embrace curiosity like, "Wow, we do not see this thing the same way. That is fascinating. Tell me why you see that." And that can be by personal feedback. Someone's like, "Hey boss, I don't think you talk enough." "Wow, you don't think I talk enough? That is unexpected. I would love to hear more about that because no one's ever said that to me," so I wanted to give that to anybody who might recognize this behavior in themselves. There's lots of things that you can do and you should do that work.

(01:29:22):
The work of improving yourself is always fruitful and satisfying and it pays off, as we discussed, in every aspect of your life with your family, with your friends, and professionally. This is one that I really thought was so great was just curiosity. Embracing curiosity in those moments of challenge has really completely changed my life and I owe that to Ami Vora.

Lenny (01:29:40):
Wow, I love this example. It's basically an example of, "Yes, and?", but in a really... no one's going to be like, "Yes, and?" It's a really nice way of saying it, "Just fascinating. Tell me more."

Andrew ‘Boz’ Bosworth (01:29:50):
Fascinating. You've got to tell me why, I want to understand it.

Lenny (01:29:54):
I love that. Maybe that'll be the new title, fascinating.

Andrew ‘Boz’ Bosworth (01:29:56):
There you go.

Lenny (01:29:58):
Anyway, with that, Boz, we've reached our very exciting lightning round. Are you ready?

Andrew ‘Boz’ Bosworth (01:30:03):
I'm ready.

Lenny (01:30:04):
First question, what are two or three books that you've recommended most to other people?

Andrew ‘Boz’ Bosworth (01:30:09):
The Dream Machine, which is a tremendous history of pre-history, really of modern computing ostensibly following the life of J.C.R Licklider, but really it's much broader than that, is a tremendous missing piece of history in my opinion. I think in my discipline, in computer science, we were not properly educated. We learned about Alan Turing and we learned about some of the technical underpinnings of computer science theory, but the modern computer and the path to it is a profound and fascinating one, and it has particular resonance today as J.C.R Licklider's observation was human in the loop computing and I think we are now in human in the loop AI, and I think there's a tremendous resonance there. The second one is Good Inside, which is Dr. Becky's book, and again, I think it's a tremendous parenting book, but more than that, it does contain lessons for how we think about our own emotions and how we manage those, which I find to be useful in any context.

Lenny (01:31:00):
Amazing recommendations. She's also got an online community for people that-

Andrew ‘Boz’ Bosworth (01:31:03):
She has a wonderful online community, she's very engaged in it. And for those parents out there, you're a little early for this Lenny, but you'll get there. Having little scripts that I'm reading on Instagram that when I'm in a moment of tremendous emotional challenge with my children, I have the words handy. They're just top of mind for me. They've been cashed in, right? They're primed, is a big game changer.

Lenny (01:31:24):
This will be for our parenting episode down the road.

Andrew ‘Boz’ Bosworth (01:31:27):
That's right.

Lenny (01:31:28):
Is there a favorite recent movie or TV show that you've really enjoyed?

Andrew ‘Boz’ Bosworth (01:31:32):
Yeah. This is super conventional, but Mandalorian. One of the things that's been fun about that is really my kids again is we watched it with my kids, so we had a chance to go on the Galactic Star Cruiser. Again, y'all know I am a genuine and true nerd through and through. Huge fan of Scott Trowbridge and his work at Star Wars service lands in Disney and also of that. And so before that we got our kids who were nine and six and watched all the movies together, and then we were watching Mandalorian together as a family, and it's super fun and it's fun to have that kind of lore, a connection. So it's not just the classic kids movies, but there's something more, and I think for them they feel like it's an adult kind of conversation they get to be a part of. I've really enjoyed that. And I think the world of Dave Filoni and John Favreau and the team that's building that universe out.

Lenny (01:32:19):
This is the way.

Andrew ‘Boz’ Bosworth (01:32:19):
This is the way.

Lenny (01:32:20):
Do you have a favorite interview question that you like to ask candidates that you're interviewing?

Andrew ‘Boz’ Bosworth (01:32:25):
One of the most important things that I always ask people is what people who've worked with them would say are their greatest strengths and weaknesses. I like this for a couple of reasons, not least of which is I often do follow up with references and I like to triangulate their awareness of how other people calibrate though. And also how they respond to criticism. Sometimes candidates surprise me. They say, "Hey, you'll hear this critique a lot from me. I don't think it's fair." That can be an okay answer, but they've got to be a pretty robust there. Or it's like, "Hey, this is something I'm working on, here's what I'm working on." But I also like to hear what they think their superpowers are. And too often a lot of attention in interviews is paid to weaknesses, which I care about because I want to know what the downside is. But way more important to me is like, "What are you awesome at? What is the thing that if I can just hitch a wagon and ride, that's what I want to know. Where's the superpower that you're crushing it at?"

(01:33:22):
And what's funny is people are pretty rarely give my reference checks. They're not that often accurate about what the critiques are, but they're usually pretty accurate about what their strengths are.

Lenny (01:33:31):
Interesting. I'm also a huge proponent of strengths and not worrying too much about your weaknesses.

Andrew ‘Boz’ Bosworth (01:33:36):
But asking people to contextualize their performance through the team, that's so important. We do not achieve very much on our own.

Lenny (01:33:44):
Communication is the job. Amazing. Is there a favorite product that you recently discovered that you love? And Meta products are acceptable answers.

Andrew ‘Boz’ Bosworth (01:33:55):
The Ray-Ban Meta glasses would be a tempting answer. The multimodal stuff, which I'm going to get in trouble because I've been teasing this for months on social media and it's still a closed beta, and it's like, "We're growing the beta slowly," but it's like, "People already really badly want it." It was probably one of the most magical things I've gotten to try recently. It's not totally fair because it's also not you can buy the Ray-Ban Meta glasses and very soon, I won't say when, but very soon they'll have this capability, but it's more fun to think outside of the box. All right, this is such a... I'm going to get in trouble for this answer because it's a bit of a pretentious one. I'm not a car guy, let me say that right now. I don't like cars. I don't care about cars. I want a car that works and doesn't break. All my cars growing up, had over a hundred thousand miles in them because we only ever had used cars.

(01:34:38):
They were constantly breaking down and the power steering would go out while you're driving and you have to [inaudible 01:34:43] the thing and the brakes would go out or you'd throw a rod. I've done it all. I just wanted a car. And so then I drove a Honda Accord that I bought for 10 years and then I drove a Tesla Model S for 10 years. And a Tesla model S had a thing happen to it while it was parked, I will get into that. I get a new car and again, I'm like, "I want to get an electric car." And I was like, "I'm going to get something nice. I'm going to get something nice. I want to get something nice." I'm driving a Mercedes-Benz AMG EQS, and I didn't know cars could be this nice. I grew up driving used cars and whatever, I did not know it was possible. It is the best augmented reality product I think you could buy in the market today.

(01:35:29):
With the heads of display, it puts your turn in three-dimensional space. It's got cameras facing your eyes, so it's positioned correctly on this display relative to your eyes, the turn. And so when you come up, it's like you're hitting a little wall, you got to turn before you hit the wall. And I was like, "Oh my God, I think this car has a great augmented reality." Not a car guy, and I'm not trying to flex on this car or whatever it is. I like it a lot. I didn't know they could be that nice, but the thing that I thought was so impressive was they did an amazing job with augmented reality in this car.

Lenny (01:35:58):
Wow. Mercedes-Benz, a player in the augmented reality, mixed reality space.

Andrew ‘Boz’ Bosworth (01:36:01):
Big time. They're out there, they're in the lead.

Lenny (01:36:04):
I sometimes think about having a contest where I give away products people mention in this segment, and now you've blown my budget way out of proportion.

Andrew ‘Boz’ Bosworth (01:36:12):
Ray-Ban Metas, you can afford that.

Lenny (01:36:15):
That's an amazing, I'm going to have to check that out. I think we're going to increase some sales for Mercedes. Next question. Do you have a favorite life motto that you often come back to think about, share with friends and family, find useful?

Andrew ‘Boz’ Bosworth (01:36:27):
Yeah. We have a funny actually how we came about this. The motto my family has, my immediate family, me, my wife and kids is just trust yourself. Just trust yourself. Actually, the reason we have that motto is when we have a house, we have a few nice art pieces and one of them is a Tracy Amen, a famous UK based artist, and she does neon pieces and it says, "Trust yourself." And so it's in our bedroom hallway where me and all the kids and my wife are, it says, trust yourself and every morning the neon lights up and it's trust yourself. And then I had the chance to have a crest made in the UK and my family's English from way back. And so in the crest it says, "Trust yourself." And I always talk to my kids, especially. I really think people, when you're experiencing peer pressure like, "Who do you trust? Them or yourself? When you're having a lot of self-doubt and uncertainty, you have to trust yourself."

(01:37:17):
I just think so much of the success I've had, I think this is probably true of most people who went to startups and succeeded, was like, "I just had faith that I was making good decisions." I mean, this comes back to the conviction point I made earlier about how you do things like newsfeed or controversial things or how you make big expensive changes, just conviction. You have to believe you, your eyes, ears in an intellect have combined to give you a point of view that has intrinsic value and deserves your respect as opposed to reading that newspaper article about your company and believing it over what your own eyes and ears have told you. That's the motto that we go with.

Lenny (01:37:57):
And I think it's also important to say you won't always be right and that's okay.

Andrew ‘Boz’ Bosworth (01:37:59):
Totally. That's right. Trusting yourself also includes taking risks because you trust that you can deal and handle with what happens when the risks don't pay out.

Lenny (01:38:07):
Beautiful. Final question. I know that you're an amateur photographer, maybe semi-pro photographer, a lot of travel photography.

Andrew ‘Boz’ Bosworth (01:38:13):
Amateur. Amateur, amateur.

Lenny (01:38:15):
Amateur. Okay. You also have this website that I came across that I don't know if people know about it, it's this funny name. I'm not going to mention that. I don't know if you want people...

Andrew ‘Boz’ Bosworth (01:38:22):
Warden Shortbow, it's an anagram of my name. Warden Shortbow, an anagram of Andrew Bosworth, wardenshortbow.com. I love photography. I love it. It's a real passion of mine.

Lenny (01:38:30):
So here's the question. What's your favorite photo that you've taken?

Andrew ‘Boz’ Bosworth (01:38:33):
Art is actually a great place to talk about trusting yourself, by the way. And I know it's cheesy to say it, but I think Rick Rubin's recent interviews on what art is and how people make it is spot on. You have to make it for yourself and you have to love it. And if someone else loves it and it finds broader resonance, that's awesome, but that's not why you do it. And if you start to try to do it for broader resonance, then you're kind of chasing something else. It's media, it's entertainment, but it's not art. It's some other thing. And I say all this to basically tap dance and say, I kind of love a lot of my photos and it's very hard to pick a favorite. The one that is popping to my head, which has more emotional [inaudible 01:39:12] is a picture I took of my son playing in the street and just jumping in a puddle, wearing a rain boot, rain slick kind of a thing. And it's not sharp, it's not in focus. It's a vignette, it's an idea.

(01:39:27):
And I really do think Ansel Adams talked a lot about how the goal of the photographer is to create a capture that expresses to the viewer what it felt like to be there. And people forget that he was a master of the dark room even more so than maybe than the capture, the print. The print was where he did amazing work. And I've had the pleasure to go to his dark room in Big Sur and spend time with his son and watch them do development in that room. And he had elaborate scripts of how he would highlight, dodge and burn different parts of the photograph to get it to have the resonance that he wanted. And he fought for photography to be accepted as an artistic medium, which it wasn't, which I find so resonant in today's AI art conversations where once again, we're trying to gate keep what is art and you just don't get to do that unfortunately.

(01:40:20):
So this picture of my son, no one would call it a technical marvel, but as a vignette of it capturing for me personally, but also I think in general for parents, the ephemerality of these tremendously touching, charming human moments that you have with your children, that's the one that comes to mind.

Lenny (01:40:39):
Amazing. We're going to try to find it and link folks to it. And on the point of Rick Rubin, something he says along the same lines is that you think of art as your diary. I am just describing what I find interesting and important and nobody can come to me and say my diary is wrong. It's my diary, this is how I see the world, and that's okay. And that's where the best art comes from is just emboldening to this... there's an awesome video of him saying exactly this that I was recently watching actually. Boz, this was so much fun. I am so thankful we made time for this. I'm looking forward to our parenting and relationships podcast in the future. Joking, not joking. Two final questions. Where can folks find you online if they want to follow what you're up to and how can listeners be useful to you?

Andrew ‘Boz’ Bosworth (01:41:19):
Sure. I'm @boztank on Instagram and on Threads and also on X, facebook.com/boz. And I also have my own podcast, which is a technical deep dive, so it's pretty different, I would say. It's a technical deep dives to try to go deep on one or two topics each time. That's called Boz to the Future. You can find that on Spotify or iTunes.

Lenny (01:41:41):
Boz to the Future, buy some Quest stuff.

Andrew ‘Boz’ Bosworth (01:41:44):
Get yourself a Quest 3. Let's be honest. Dude, treat yourself.

Lenny (01:41:48):
There you go. Or these Ray-Ban sunglasses. I'm a big fan. Boz, again, thank you so much for being here.

Andrew ‘Boz’ Bosworth (01:41:52):
Cheers. Thanks, brother.

Lenny (01:41:53):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

