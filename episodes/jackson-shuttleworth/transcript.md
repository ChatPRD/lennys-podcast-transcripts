---
guest: Jackson Shuttleworth
title: 'Behind the product: Duolingo streaks | Jackson Shuttleworth (Group PM, Retention
  Team)'
youtube_url: https://www.youtube.com/watch?v=_CCwoQZH5hI
video_id: _CCwoQZH5hI
description: 'Jackson Shuttleworth is a Group PM at Duolingo, where he leads the retention
  team and the powerful streak feature. The streak feature, which gamifies consecutive
  days of learning, has been...

  '
duration_seconds: 5312.0
duration: '1:28:32'
view_count: 28994
channel: Lenny's Podcast
keywords:
- growth
- retention
- churn
- metrics
- okrs
- roadmap
- iteration
- analytics
- funnel
- monetization
- subscription
- revenue
- hiring
- culture
- management
---

# Behind the product: Duolingo streaks | Jackson Shuttleworth (Group PM, Retention Team)

## Transcript

Jackson Shuttleworth (00:00:00):
... Duolingo is a $14 billion company, it's hitting all-time highs too, it just keeps going up, but I think it doubled in value in the past six months. Streaks is the most impactful feature. We have, right now, over 9 million users with a year plus streak. If you look at the numbers, I think it's been our biggest growth lever. What Duolingo really focuses on is, how do we help users build habits around language learning? Getting user come back the next day is the biggest problem to solve.

Lenny Rachitsky (00:00:25):
Let's get into the motherload of learnings from the journey of streaks, talk about the key lessons, insights, and also wrong turns along the way.

Jackson Shuttleworth (00:00:30):
I'd say test everything, we've run in the last four years over 600 experiments on the streaks, so every other day. We've actually set up really good infrastructure for copy testing. We used to say continue, our standard CTA is continue, and we changed that to commit to my goal, and it was a massive win.

Lenny Rachitsky (00:00:48):
There's so much human psychology that you all learn through all these experiments of just how to motivate people, what motivates, what demotivates.

Jackson Shuttleworth (00:00:55):
Say that you played a mobile game, or that you've done it for 3,000 days in a row, I don't know, maybe that hits a little bit different than you've learned Spanish for 3,000 days in a row.

Lenny Rachitsky (00:01:07):
Today, my guest is Jackson Shuttleworth. Jackson is a group product manager at Duolingo, leading the retention team. This is a different kind of episode that I'm experimenting with, where we spent the entire conversation focused on the journey and lessons of a single feature, in this case, Duolingo streaks. Duolingo is a $14 billion business, just over the past six months, they doubled in value, they're hitting all time highs in usage and market cap, they're also one of the very few successful and also the single biggest consumer app business in the world. And as you'll hear from Jackson, the streaks feature is the single most impactful feature that most contributed to this growth and success. In other words, you could argue this one feature created billions of dollars of value, which to me means it is worth studying in depth.

(00:01:59):
In our conversation, Jackson shares the history of the streaks feature, all of the biggest wins and wrong turns they've taken along the way, what he and his team have learned about what works and doesn't work with a streaks mechanic, and also how they set up their teams to operate in a way that allows them to run over 600 experiments on this product and continue to find big wins. I hope to do more episodes like this on features and products that you'd love to hear more about, so leave a comment either on YouTube or on Substack, and tell me which product or feature you'd love to see me cover. And if you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube, it's the best way to avoid missing future episodes, and it helps the podcast tremendously. With that, I bring you Jackson Shuttleworth.

(00:02:44):
Jackson, thank you so much for being here and welcome to the podcast.

Jackson Shuttleworth (00:02:48):
Yeah, thank you. Long time listener, first time caller.

Lenny Rachitsky (00:02:52):
I appreciate it. So, this is going to be a really interesting conversation, I've never done an episode like this before, where we basically spent an hour, an hour and a half going into one feature of one product, but this is a very special feature, it's a very special product. Have you ever spent an hour, an hour and a half just talking about this one feature with anyone?

Jackson Shuttleworth (00:03:13):
Well, internally, so when we onboard new folks to the team, we'll do, I actually just did this with somebody that joined the team recently, where we spent, yeah, I was like, hey, let's spend an hour just talking about the streak. We got through an hour and I got through about 30% of what I wanted to share, there's just so much, we'll talk about this, but there's so much that we've learned over the years, but never anything externally like this. I think we've shared bits and pieces of learnings, but this will be the motherload of learnings hopefully-

Lenny Rachitsky (00:03:14):
Here we go.

Jackson Shuttleworth (00:03:41):
... of how Duolingo built the streak.

Lenny Rachitsky (00:03:42):
We should title this the Motherload of Learnings of Duolingo Streaks. This episode is brought to you by Pendo, the only all-in-one product experience platform for any type of application. Tired of bouncing around multiple tools to uncover what's really happening inside your product? With all the tools you need in one simple-to-use platform, Pendo makes it easy to answer critical questions about how users are engaging with your product, and then turn those insights into action. Also, you can get your users to do what you actually want them to do. First, Pendo is built around product analytics, seeing what your users are actually doing in your apps so that you can optimize their experience. Next, Pendo lets you deploy in-app guides that lead users through the actions that matter most. Then, Pendo integrates user feedback so that you can capture and analyze what people actually want. And the new thing in Pendo, session replays, a very cool way to visualize user sessions.

(00:04:37):
I'm not surprised at all that over 10,000 companies use it today. Visit pendo.io/Lenny to create your free Pendo account today and start building better experiences across every corner of your product. P.S. Do you want to take your product-led know-how a step further? Check out Pendo's lineup of free certification courses, led by talk product experts, and designed to help you grow in advance in your career. Learn more and experience the power of the Pendo platform today at pendo.io/Lenny.

Speaker 3 (00:05:05):
Pendo.

Lenny Rachitsky (00:05:10):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now, you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA, and more, with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance, alongside reporting and tracking risk. Plus, you can save hours by security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/Lenny. That's V-A-N-T-A.com/Lenny.

(00:06:03):
Okay, so for people that don't know anything about what Duolingo streaks are, can you just first give a brief explanation of what is Duolingo streaks? What is this feature all about?

Jackson Shuttleworth (00:06:10):
Well, presumably people know, Duolingo is a language learning app, the Duolingo streak tracks, currently anyway, how many days in a row you've done a lesson. So, you come to Duolingo, you do a lesson, your first lesson you'll start a streak, and then every consecutive day that you come use the app, you'll extend your streak. And I should actually put an asterisk around how many days in a row because we also have built flexibility into the feature. So, we have these things called streak freezes, it's like insurance for your streaks. So, it's a pretty simple feature, in theory, but over time we've layered on challenges, and goal setting, and rewards, and social features... A lot of our notifications are tied to the streak. So, pretty simple feature to understand, but it's been a really rich feature for us to build on top of.

Lenny Rachitsky (00:06:58):
Some people might be hearing this and be like, Duolingo streaks, what's the big deal? There's other people that are like, holy, I want to learn everything I can possibly learn about Duolingo streaks, so many companies are trying to copy what you've learned from this. Give people a sense of the impact that this one feature has had on Duolingo's success and growth.

Jackson Shuttleworth (00:07:15):
And this is not just the subjective retention PM talking, I think this is our biggest feature, with the exception of the lessons. And I think it's actually [inaudible 00:07:24] start that. Streaks are a great engagement hack. I'm of the opinion that any team, any app out there can introduce a streak, and if you figure it out, it probably works to retain users, but at the core, you have to have an app that people want to use, and people really like using Duolingo. It's fun, it's delightful, you learn something. And so, it allows us to layer an engagement mechanic on top of that the streak is really powerful. So, it ships a disgusting amount of DAUs, again, it is one of our golden geese. And again, what's cool is that, you look at notifications, notifications for Duolingo is massive. Us sending better, whether it's copy or timing, so many of our notifications work because they reference the streak, because users care about the streak.

(00:08:10):
And so, not only is it itself, us iterating on the streak a huge driver of DAUs, but it's also something that enables other really high valuable features. I was looking up some stats before I came on, and it's pretty crazy. So, we have right now over 9 million users with a year plus streak.

Lenny Rachitsky (00:08:30):
Wow.

Jackson Shuttleworth (00:08:30):
So, 9 million of our users have used Duolingo every year, almost every day, for well over a year. Which is pretty... I don't know, I like to imagine things in terms of like, okay, well, if you put all these people in a city, or in a place, where would it be? I'm like, ah, it's like a very large city, 9 million people.

Lenny Rachitsky (00:08:53):
For a year, have a year long streak.

Jackson Shuttleworth (00:08:53):
For a year.

Lenny Rachitsky (00:08:56):
That's incredible. I was just looking at the stock of Duolingo, so Duolingo is a $14 billion company at the time we're recording this. It's hitting all-time highs too, it just keeps going up. I think it doubled in value in the past six months, something like that. And what I'm hearing from you is streaks is, other than just the core learning feature, which is just the product of Duolingo, this is the most feature in terms of growth, and in that retention specifically.

Jackson Shuttleworth (00:09:24):
If you look at the numbers, I think pretty objectively has been our biggest growth lever for driving DAUs, and also say a lot of it's just related to how we think about growth at Duolingo. And a lot of what we try to do is organic growth. We think about growth just as much as bringing new users onto the platform is not losing them. If you're just bringing people onto the platform, then they churn, that's not going to be sustainable. And so, as much as we can do to keep our users coming back and actually retaining as users, it's going to give us a much easier base to continue growing DAUs off of.

Lenny Rachitsky (00:09:57):
Perfect. Okay. Talk about how this feature originally came to be. What was the original version of it? What was the original insight that led to [inaudible 00:10:05]-

Jackson Shuttleworth (00:10:04):
Yeah, so the oldest streaks or as old as Duolingo itself. When we launched Duolingo, we launched with a streak... And I say we, I was just graduating undergrad when Duolingo launched. So, this is well before my time. But we launched with a streak feature. Initially how the feature worked was you'd come to Duolingo and you'd set a goal for yourself, and it was an XP based goal. So, Duolingo, a little bit of nomenclature, we have an experience point based system that drives a lot of our features in the app. And the way you'd set it is you'd say, based on what your language learning goal was, maybe you have a 10 experience point goal versus a 50 experience point goal. And so, extending your streak would be, hey, can you hit 50 experience points? If that's what you set your goal to be.

(00:10:50):
And this worked well, I think this also speaks to how Duolingo initially grew. Luis launched it with a TEDTalk, we probably had a more tech-forward user base initially, and so this whole idea of an experience points based streak system made sense. But what that also meant is that you could have a user come and use the app, do multiple lessons a day, and maybe they just set too hard of a goal for themselves, and then lose their streak. Which, you don't need to be an expert in streaks to understand that's probably not good. The nice thing with how we initially set it up though is it really did connect with what your goal was. So, if you were serious, let's track how good you are at being a serious language learner.

(00:11:28):
But I'd say one of the most impactful experiments we ran was about, this was actually as I was joining, or just after I joined we had run this experiment, was to move it from a XP based streak to just do one lesson a day, and you'd extend your streak. And the risk that you can sort of imagine is, well, then users kind of care less about it because it's not connected with their goal. And we saw none of that. This was a huge driver of DAUs, just making it easier to extend your streak, but I think really importantly it's still meaningful. The unit of use, and as you're thinking about building a streak, I think it's really important to think about what the unit of use of your app is. The unit of use for Duolingo is doing a lesson. And so, if what we care about is users coming back every day and doing a lesson, because it shows that they're actually engaging with the app, then it doesn't hurt us to make our streak focus on just do one unit versus multiple.

(00:12:23):
And so, that was probably the big [inaudible 00:12:25] change experiment that we ran at the time was moving from an XP-based streak to a one lesson streak. It's also simple, and I think that's one of the things to think about with streaks. It's always easy as a PM to have a million goals or objectives for what you want your feature to be and potentially build a more complex feature, and a one lesson streak, it's just easy for more users to understand.

Lenny Rachitsky (00:12:46):
Yeah, that's exactly what I was going to say. And just for folks that aren't super familiar with XP, it's basically experience points and you get them from doing things, it's like a [inaudible 00:12:53]-

Jackson Shuttleworth (00:12:53):
Yeah, you do stuff on Duolingo, and then based on what you did and how well you did it, we give you experience points, this actually drives a number of our features in our apps. So, leaderboards is the big one, we have a leaderboard system, where you try over the course of the week, you battle with 29 other people, and you want to win, that's all driven by XP. So, we do have other features in the app that really benefit from this XP system-

Lenny Rachitsky (00:13:16):
Cool.

Jackson Shuttleworth (00:13:16):
... the streak is just no longer one of them.

Lenny Rachitsky (00:13:18):
Awesome. Okay, so I want to talk about the journey from that point to what it is today, but a quick tangent, I saw Luis tweet just this week, someone asked him, "How do you decide whether to optimize for learning or engagement?" And he's like, "No question, everything we do is focused on engagement because you won't learn anything if you're not coming back to the app."

Jackson Shuttleworth (00:13:39):
As an engagement PM, that was the coolest thing he could have ever said. It's, well, again, very much as subjectively I guess as an engagement PM, that's how I've... I am sure the learning folks at Duolingo will cringe when they hear it, I see myself as a learning PM as much as an engagement PM, because the easiest way not to learn on Duolingo is not to come back the next day. And so, if we don't make the app retentive, you will have no opportunity to engage with our learning features. Now, I do think that there is a long tail of learning, where, if you start to dumb down, and honestly this is something we wrestle with the streak as well, you start to dumb down the experience, and your users aren't actually learning, they're not going to care.

(00:14:20):
Streaks work best when they're sitting on top of an app that users care about. But yeah, if you don't come learn on Duolingo.... If you don't come back to Duolingo, then you're not learning. We track a lot of this with, the work that we do, we make sure that as we're making changes to the streak, we're not hurting the learning experience and we don't have a ton of interaction with it. So, we're constantly thinking about this, but thank you Luis for saying that.

Lenny Rachitsky (00:14:48):
It makes sense to me. Okay, so lets get into the motherload of learnings from the journey of streaks. So, the first version went from XP to one lesson, talk about the key lessons, insights, and also wrong turns along the way to what we see today.

Jackson Shuttleworth (00:15:03):
Duolingo has very much, has a strong test it philosophy, we're willing to test a lot of different... Honestly, we'd much rather test it than debate it for days and days. So, we actually followed up this experiment with, and this is a little bit later, with hey, what if we make it even easier to extend your streak? And so, we actually tested, hey, if you do one exercise, just one exercise in a lesson will extend your streak. A lot of the insight was good, you look at the funnel, hey, there's a lot of users who are starting but not finishing lessons, they're not extending your streak, the loss aversion doesn't kick in, they don't come back... So, this followed that train of thought. What we realized when we ran this experiment is DAUs moved not one bit. And what we were doing by... And if we go back to unit of measure, we had dumbed down the unit of... Nobody thinks about, oh, I just want to come do one question on Duolingo, nobody thinks about that.

(00:16:05):
So, we had a less clear unit of measure that we were basing our streak around, and the users that we were capturing with our streak, you come, you do one or two questions on Duolingo, then you leave, were the least engaged users imaginable. And so, I think that's something also to think about as you're building your streak, is like what is the user that you're solving for? So, not only what is the habit that you're building for, but what is the level of commitment, and that was an example where we over indexed on a type of user who we honestly just weren't going to keep, that was a very easy shutdown decision.

Lenny Rachitsky (00:16:39):
That's an awesome story, just to comment in that real quick. Just you went, let's just go to the extreme and make it just like streaks, yeah, get everyone going streaks forever, and then... I love that it turned out and it's not bringing users that you want, and it's dumbing down experience. It makes me think of Farmville, where you have to go and harvest your crops every, whatever, hour, that lasts for a bit and then eventually people are like, what the hell am I doing with my life?

Jackson Shuttleworth (00:17:04):
Yeah, exactly. We test every, I was looking at the numbers as well, we've run in the last four years, over 600 experiments on the streaks. So, every other day effectively-

Lenny Rachitsky (00:17:14):
600, wow.

Jackson Shuttleworth (00:17:15):
... we're running an experiment. And they range from big, like this, changing how the mechanic works, to let's swap a string with another string and see if that copy is better for users. So, we're constantly testing on everything. I do think that, I'd be more careful running that experiment now, at some point your streak gets big enough that, again, I got 9 million users on the streak, I got to be really careful... Those are our best retaining users, you got to be careful. But in the early days of the streak, I'd say test everything. See what... Don't get super caught up in it has to be like this, just test a bunch of stuff and see what speaks most to users. Because I think, again, you will constantly be surprised by the insights that you get from whether you... We shut down about half of our experiments, so half of our experiments lose, we still learned a ton by virtue of running them. So, super, super valuable.

Lenny Rachitsky (00:18:08):
That's actually a good success rate, a lot of companies have only 20% of experiments be positive. What's your policy on if it's neutral, do you ship it, or do you kill it?

Jackson Shuttleworth (00:18:18):
It really depends. If we're adding something and it's neutral, we tend to shut it down because it's just more cognitive load, it's something that we're going to have to start building around, a new UI element that we have to figure out how it fits into our system. I'd say when we do ship a neutral experiment is, something that we have real conviction around, okay, yeah, maybe this was neutral but it's going to give us a new platform to then build on top of, so that experience might be neutral, but now we can build these DAU positive experiments. My general take there is though, in that case, build that in as part of your V1 so that you make sure that at least your hypothesis around this roadmap has play should probably be the case, but in general, shutting down a neutral experiment so you don't introduce more complexity to the app is the way we tend to go.

Lenny Rachitsky (00:19:10):
Makes sense. All right, what else? What else have you learned along the journey?

Jackson Shuttleworth (00:19:13):
Well, maybe I can talk about a few different ways that we structure, a few different themes that I think we lean on. So, the first is focusing on the zero to seven day user experience. And I would say this is, if you look at whatever our breakdown of experiments are, we run definitely more than average number of experiments on getting users to go from a zero to seven day streak. And a lot of this is because we've looked at the data for our retention curves, and what we found is that once you get to seven days, loss aversion kicks in, and you retain. So, going from a one to a two-day streak, huge jump in retention, two to three day streak, slightly less but still huge and it's up until day seven. Once you hit day seven, it flans out. And it's not to say that if you have a 30-day streak, you're way more attentive than day seven, but not in the order of magnitude that it is from day one through seven.

(00:20:05):
So, we do a ton of work to get users to that point where loss aversion kicks in, and then they don't want to lead the app. One of the fun ones that we did, and it's honestly as much about process as it is about the feature itself, was we have a feature called streak goal, and it is... Again, so much of this stuff seems so obvious in retrospect, but it was really novel at the time. We had this idea of like, hey, maybe we'll just goal users to hitting a certain streak length. As you can imagine, this is pretty powerful user psychology, and we started with the simplest version of this. And this is how Duolingo does a lot of our testing. Rather than design the big complex feature for V1, just do the simplest encapsulation of what that feature can be, see if it has legs, and then just add to it iteratively over time, this is partially how we get to 600+ experiments on streaks, they're not all big ones.

(00:21:01):
But we started... And it was funny, we actually took a learning from our monetization win teams. One of the strings that they had, the pieces of copy that they had, worked really, really well was, I think it was your 5.6 x more likely to finish the course if you subscribe to Plus. Now, it's Super, our subscription. It was a really good hook that if you really cared, you'd sign up. And so, we had a similar thought, where it's like, oh, let's just tell you how much more likely you are to finish the course if you get a 30-day streak.

(00:21:34):
And so, we started with that, and I think it was like you're seven times more likely to finish the course if you have a 30-day streak, and just that message when you started your streak, I telling you that, was awesome. Huge win. Indicating an outcome... And Duolingo doesn't have, we have a gem economy but we don't actually have, it's all you learning. But being able to actually talk about it in terms of the outcomes that a user would think about, in this case, trying to finish the course, was a huge win. So, this is where we started and we're like, ah, goal setting, all right, we should go much harder on this.

Lenny Rachitsky (00:22:06):
Found a-

Jackson Shuttleworth (00:22:06):
Yeah, we found our thing, and now let's just beat the heck out of it. So, we followed that up with another experiment, where we tested different lengths. So, we test 14 days and 50 days, and we found that they were all good, but they appealed to different users. And so, we started to realize, all right, well, we probably need to be more thoughtful about who we give these different options to. And so, then we followed that experiment up with, all right, let's start with 30 days, and then we're going to let you opt out, we'll say, no, I don't think I can hit it. And our thinking was, and then if you say no, we'll hit you with an easier goal. Because we just wanted to get you to commit to a goal. And this was a fascinating one because it was a good win to give users that easier goal, to try to capture them before they said no, but it was almost just as big a win to add that opt out button.

(00:22:58):
So, we tested separately, and I'm a huge fan of testing way too many arms for an experiment, just to be able to isolate your hypotheses, but we captured just what happens if we add an opt-out button, and adding an opt-out button... And you would think, as a PM, oh, now users might not engage with my feature, that's a bad thing, but it was a huge win to let them do that. And the learning here was that this intentionality of saying, no, I want it... Previously it was just a continue button, but now it's like, no, I want to hit 30 days, and having that be an intentional decision for them, yes or no, even though again, this had no impact, or no impact past this screen. Everything that I'm talking about now was just that screen that day, and then was all thrown out. So, that optionality was a huge insight, and so because of that, we built a goal setting feature where you could choose between different goals, giving users that optionality was likewise a huge win.

(00:23:57):
I'll say one final learning on this, again, you talk about friction, and good and bad friction, we thought once we built a goal picker screen, where you could pick between different streak lengths, we were like, oh, well, let's recommend that users do a harder goal, thinking that okay, well, a harder goal is going to be better retention, and we'll the preselect harder goal for them. And based on all the learnings that I just shared with you, you probably imagine lost pretty significantly, we realized that yes, we could speed users through the screen more by virtue of picking a goal for them, but that act of selecting, I think it's 30 days, I think it's 14 days, was where we were getting so much of the engagement from this feature.

Lenny Rachitsky (00:24:39):
There's so much human psychology that you all learn through all these experiments of just how to motivate people, what motivates, what demotivates, it feels like you guys should write a book on human psychology and motivation.

Jackson Shuttleworth (00:24:51):
I feel very much like a amateur armchair psychologist with everything that, at least as far as people who want to learn languages on their phone go, I really understand those folks.

Lenny Rachitsky (00:25:03):
Right. So, one theme I'm hearing here so far is you guys are basically just mining for gold, just looking for a vein in some mine, and once you hit it you're like, ooh, this worked, you just go crazy on just testing all kinds of things to see how far you can take that one little thread.

Jackson Shuttleworth (00:25:22):
Yeah, and I think, I shared how this idea came partially from a monetization win that they had, I think there's a lot of, because Duolingo runs... I don't know what percentile we're in, but it's got to be a very high percentile of per capita experiments run for a company, based on company size. We're just constantly learning so many things and there's a really great cross-sharing of monetization say, hey, this thing worked for us, is that something you can use? So, I'd say it's rare that we go into something where it's just like, let's just try something. Typically, we have some insight because of all of these experiments that we've run, that hey, if we do this, I don't know, it's one here, or it's worked here, it's driven this user engagement, if we massage that and try in this scenario, or a different screen, we come in at least with a strong hypothesis of this will work.

(00:26:17):
A lot of times we do look, and we're like, a lot of the apps that we look at actually are games themselves, so it's like, all right, you're playing Royal Match, or there's the new Pokemon trading card game that I'm spending way too much time on, you look at these games and see what they're doing, and it's really good fodder for what we can do. But a lot of times you're at least going in with a strong hypothesis based on what you've seen work elsewhere.

Lenny Rachitsky (00:26:39):
Got it. So, just to double down on that point, it's not just random experiments, it's here's a hypothesis we're fairly confident, or has a chance to be true, let's try it. It's not just let's just try everything?

Jackson Shuttleworth (00:26:49):
Yeah. And I think that how strongly you feel about the hypothesis directly ties to how hard that experiment is. With copy, for instance, we've actually set up really good infrastructure for copy testing. I'm of the opinion that companies should run, as long as you have the user base to do it, copy test constantly. The amount of copy tests that we've had that have won, and I don't know, you just try things and you figure out what wins is definitely legion, and [inaudible 00:27:15] massive wins from little copy changes.

Lenny Rachitsky (00:27:18):
Is there an example of that, of just the impact?

Jackson Shuttleworth (00:27:20):
Going back to that goal screen, we used to say Continue, our standard CTA is Continue, and we changed that to Commit To My Goal, and it was a massive win. And again, it was like, okay, users tapping on that, what are we asking them to do? Commit to the goal, what is that going to lead them to do? Commit, not churn. Just that little copy change, that one time, right there, led to huge wins. And copy changes are so cheap, it's just you translate, for us, we have a lot of users all over the world, and a lot of UI languages, but just come up with a bunch of ideas, translate some strings... This is one where the feedback that you'll typically get from Luis. So, all of our changes at Duolingo go through product review that are reviewed by Luis, so Luis reviews every single change that we propose, every experiment that we run.

(00:28:12):
Typically with copy, he's just like, I don't know, test it, there's nothing better than be told by Luis, I don't think this is going to win, but sure, if you want to. And a lot of times, to his credit, he's right, and a lot of times our intuition was right, but it's just so cheap to do it. I think when the lift is smaller, it's great to have a hypothesis, but you don't need to beat it up too much.

Lenny Rachitsky (00:28:36):
So, on this thread, I didn't realize Louis reviews everything you're planning to change, and this may be the answer to the question I was going to ask, which is, one of the criticisms of running a product and company this way, of just experimenting constantly with all these micro improvements and changes, is it can lead to something, like a monstrosity of a product and experience that isn't consistent and cohesive, and just that often happens. Is the solution to that having the founder basically review all the changes? Is there anything else y'all do to avoid it becoming Farmville or whatever, is a good example of that?

Jackson Shuttleworth (00:29:06):
Yeah, our product review structure where we've got our head of product design, one of the lead, the product management leaders, and then Luis, NPR. And because they see everything, and they have a really high product bar, and so that helps. I think over time we just, as PMs, have to look at, okay, where is our feature headed? And so, we do this with the streak at least on a quarterly basis, to look at, okay, well, what have we learned, how has our streak developed, and how do we imagine this going in near future? It's easy to do, and in some sort of awful local maxima, if you're not constantly looking at your roadmap and you don't have a clear strategy. For me it's like, if you have a clear strategy where your feature is going, hopefully all of those A/B tests are not just done to get some cheap gain, they're done with a long-term goal in mind.

(00:30:03):
I do think though, and we do this every now and then with the streak, eventually you just hit a local maxima, and you say, you talked about launching neutral experiments, this is a great example, where it's like all right, cool, now we need to throw a bunch of this stuff out, based on all the learnings, can we reset this real estate, can we reset this UI, reset this feature, in such a way that is just as good as what we have now but is way more plain or simple, that we can, again, start to layer on? Those are really hard experiments to get to win obviously, because they are so optimized, but they're really important to do, otherwise, yeah, you just end up with a kitchen sink of a feature.

Lenny Rachitsky (00:30:39):
One other tidbit I just want to mention, an advantage you all have that other companies don't have is people want to learn a language, and so getting pushed to come back to an app for something that they want to do, it's not an advantage a lot of products have. So, anything you want to add there, of just like this is why Duolingo might be a little different from what you're working on.

Jackson Shuttleworth (00:31:03):
That is definitely a benefit, if I had an app... And that this is actually why I think a lot of mobile games do streaks differently, because to say that you played a mobile game, and as somebody who plays a lot of mobile games, that you've done it for 3000 days in a row, I don't know, maybe that hits a little bit different than you've learned Spanish for 3000 days in a row. I think the comparison set is much larger though, than a lot of companies give themselves credit for, and I think that there's... There's a lot of ways that companies think about their... There are very few companies I imagine out there in the world saying, oh, we don't do some degree of good for our users... Even if it's like a game, it's like, I don't know, you're giving somebody a moment away from the craziness of their lives.

(00:31:47):
And so, I do think though that is contingent on companies who are going to figure out if a streak works for them, to figure out how can you frame the streak in such a way that a user does feel good about it. And it's easier for a Duolingo, but I think there's creative ways to phrase this for users. The other thing maybe just on that that I'll say is, the streak works really well for Duolingo because with language learning it's really hard to see day-to-day progress in becoming more fluent. And fluency is not even the right word, it's like becoming better at Spanish or whatever, it is a years long process for someone to get better at a language.

(00:32:25):
Duolingo makes it easier, but you still got to put in thousands of hours if you're going to reach C1 or C2 fluency, and that is really hard to track on a day-to-day, and so the streak works really well for us because we might not be able to tell you, hey, you now know 0.01% more Spanish, but we can show you, hey, you've gotten your streak a little bit higher. And so, I think this works particularly well when you're an app that is doing something that's going to be sensed or felt over a longer term to help contextualize that progress in a way that makes more sense, or at least feels more tangible to a user.

Lenny Rachitsky (00:33:02):
Great, that was a great context. Empowering to a lot of companies that aren't necessarily doing language learning. Okay. So, it took us on a long tangent away from lessons and experiments you ran along the journey of iterating on the streak. So, a few things you've shared so far is just, it started with this XP idea, and then went to a lesson, then you iterated on ways to make it simpler, maybe harder, you added streak goals, where you commit to I'm going to hit a certain goal of streak. What else? What else have you found that has worked, didn't work, lessons learned?

Jackson Shuttleworth (00:33:32):
Again, sticking with this one to seven day streak, the idea of a streak, particularly probably to this audience, is obvious. Like, oh, it's a streak, it just counts how many days. We've realized over time that a lot of users do not understand how a streak works, and it can be as small as, well, I don't understand how streak freezes work, or I don't... Like my mom the other day was talking to you about it, she's like, "Oh, I didn't use Duolingo and I come back and my streak's still there." So, there's certain elements of the feature that we can do better at explaining, but even what a streak is, it's tracking how many days that I've used the app, yeah, the more that we can make the feature easily comprehensible to users, the more retentive it is. And we've run a number of experiments to do this.

(00:34:23):
You asked about early easy copy changes that we made. Actually, this is my first win experiment when I joined Duolingo was, when you start a streak, we have little copy at the bottom of the screen that just, I don't know, it's like flavor copy, we use it to celebrate you, or give you context, and I ran some tests that just tried to in eight words explained what a streak was, that was it. And it was a massive win because it really dumbed down here is exactly how the streak worked, and it really helped users just understand what they needed to do. And I think this is something that's like, you constantly got to remind yourself, particularly if you work in tech and you're building cool tech features, but your user base is not a bunch of tech workers, to think about, all right, who is my audience? And for us it's not just tech workers, it's not people in America, it's people all over the world of all ages of all cultures, and so making sure that your feature is even something as simple as the streak is understandable is critical.

Lenny Rachitsky (00:35:27):
What was the actual copy, do you remember?

Jackson Shuttleworth (00:35:29):
It was... I think it's still on the app, it's like, "Start a day to extend your streak, but miss a day and it resets," something like that.

Lenny Rachitsky (00:35:38):
That makes sense to me. Very clear.

Jackson Shuttleworth (00:35:40):
Yeah.

Lenny Rachitsky (00:35:41):
In eight words, I love that. Okay. And then, when you say massive win by the way, just to give people a reference point, what does that look like? What is a massive win in this scale?

Jackson Shuttleworth (00:35:50):
Well, and it's funny, and this was four years ago, but I think it was in the order of magnitude of over 10,000 DAUs for us, and actually, maybe a small bit of context. So, Duolingo really cares about the metric CURR current user retention rate, and actually our first ever Duolingo post with Lenny was the newsletter that our former head of product wrote, Jorge.

Lenny Rachitsky (00:36:11):
Still the single most popular newsletter post of all time in my newsletter, across 300 plus-

Jackson Shuttleworth (00:36:15):
I would highly recommend that if you were interested in this, give it a read. To summarize, basically, what we found is that, if we wanted to drive DAUs, and Duolingo cares, our growth North Star is DAUs, the metric that is most effective, where a percentage change in that metric is most effective at driving DAUs is current user retention rate. And this is just users who are not new or resurrected, getting them to come back tomorrow. And so, most of the work that our teams do, our retention-based teams do is focused on CURR. And so, the retention team that I lead focused on CURR, it just so happens the streak is the best feature at driving CURR. And so, this experiment was the biggest CURR win that we had had, and it was like a top three CURR win, anyway for us. Just this little copy. And that's why I say, test copy 1000 different ways, sometimes it's not the big beautiful feature that's going to drive the huge gains, sometimes it's just something simple as a few words.

Lenny Rachitsky (00:37:15):
I love this. Okay, so you said 10,000 DAUs, I think that references you guys measure incremental impact and absolute numbers of new daily users you're going to drive attributed to that experiment, is what it sounds like.

Jackson Shuttleworth (00:37:28):
Yeah, and we do both. We'll also look at, a lot of times I'll look at, for retention, day one versus day seven versus day 14, a lot of what I'm looking for is for us to have a better day 14 impact than better day one impact because it means that users are retaining better over time. This is particularly for users that would see a feature multiple times. I just like absolute DAU numbers because as long as you're controlling for different biases, like a recency bias or a novelty bias, it's a really easy way to just have an absolute comparison. You start to look at percentage changes and then it's influenced by who your treatment, how many users saw the experiment, but at least an absolute number is easier, in my mind, to start comparing.. Again, there are pitfalls with it, but we find that that's a pretty useful way.

Lenny Rachitsky (00:38:20):
That lesson comes up a lot on this podcast, and that approach to experiment.

Jackson Shuttleworth (00:38:25):
[inaudible 00:38:25].

Lenny Rachitsky (00:38:25):
So, yeah, you're in good company. Quick tangent, if there's not an answer to this, no problem, coming back to the idea of just experimenting like crazy and not creating a product that nobody wants to use anymore, is there an example of an experiment that was positive that you all decided, no, we don't actually think this is what we want in the product, they ended up not shipping?

Jackson Shuttleworth (00:38:47):
Retention doesn't only work on the streak, although you would think... Most of our work is the streak. We've touched a lot of different surfaces over the years and there was one experiment that we launched that, we talked about XP earlier, in the lesson, the only UI elements are a progress bar at the top, and then how many hearts you have. So, we keep it really simple, and this very much speaks to the design philosophy of Duolingo, which is simpler UI is better, and we decided, hey, let's add XP in there. And so let's show your XP ticking up as you're going through a lesson, that's going to make the user feel good, it's going to show you what you've earned, you're going to be less likely to quit, all of these good reasons to do it. And then you finish the lesson and then we'll show you've collected all this XP.

(00:39:29):
And it won, the hypothesis was a good one. But we realized, and I remember having this conversation with Luis, is like, cool, this is our most important screen in the app, it is our lesson, it is where users learn, and the focus here is on learning. And now you've added this other thing up there that could be distracting for users. And I think the question, we talked about roadmaps and strategy here, the question that he had for me, and I didn't have a good answer for at the time, was like, so what else are you going to do with this? What's your iteration ideas? Where's this going to go? Is this going to make the lesson experience more gamified? And what we realized is that, honestly, it was just an easy engagement win idea, but we had touched our most sacred space in the app to do that.

(00:40:16):
And so, that was a case where it's like, yeah, it was a nice win, but we'd added that UI element, and at least at the time it was less clear what we would do with it and we realized that long term it was just going to get in the way, and we'd rather, for simplicity's sake, pause that, shut it down, and keep the lesson to be a little bit of learning sanctuary it was. Now, it's funny, nowadays I think we actually have enough XP based mechanics and fun things that we can do, that I think actually a lot of the beliefs about the in-lesson experience have changed, such as something like that could work, but at the time didn't feel good to keep that around.

Lenny Rachitsky (00:40:56):
That is an awesome example. Hopefully we have time to talk about how the team operates, where my mind goes is like, oh, but you have all these PMs and teams that want to show impact, and the performance reviews, and all that stuff, and you're not shipping something, they're like, oh look, we did a win. So, I want to chat about that later, but let's keep going on things you've learned and things that didn't work along the journey.

Jackson Shuttleworth (00:41:15):
The other thing that I'll call out with the streak, it's like we have the... The image of the streak is this flame. And we have the streak flame, and it's very much core to our iconography. It's important to acknowledge that that's a metaphor for a retention mechanic. The idea of keeping a flame lit. And again, I think we've established the flame is for a lot of users as sort of their understanding of a streak, which is great, but there's a lot of people in different cultural context and different stages of life, where the idea of keeping a flame lit to show your commitment to something makes less sense. We did some UXR in India many years ago, and this was something that just did not resonate at all there, which was a really interesting learning. And that's something it's like, again, depending upon what your user base is, the more global UXR you can do to understand how users are actually understanding and experience your feature, the better, because you just, again, encounter insights like this.

(00:42:12):
And so, even our screen design, we used to have a flame, it was mostly this flame that would light up every day. But again, it was like an indication of a metaphor for a mechanic, and when we redesigned it, we did this, Kurt, one of our animators, did this awesome odometer animation where it's like your number would tick every day... It looked good, but from a product perspective, what was cool is we actually focused the design on the screen to show your number going up, and then it would say seven day streak, eight day streak. And I think that as you're thinking about designing around a streak, don't get too caught up into what is this the beautiful story that you're trying to tell, at the expense of it being a really comprehensible feature. And so, as you're thinking about product design, making that product design a clear distillation of this is what we're actually tracking, form should follow a function here, was a learning for us. And you'll see that now in a lot of places where we're showing streak, we're really leading with the number, not necessarily the flame.

Lenny Rachitsky (00:43:18):
That's a theme that I'm hearing again and again is clarity, don't obsess with making it too clever, and don't ever think it, just clarity has a big impact.

Jackson Shuttleworth (00:43:29):
Clarity also doesn't have to come at the expense of delight. And this is something where you hit a milestone and Duo gets, it becomes, we call him a Phoenix Duo, and he becomes awesome, and lights on fire, and I think there are things that you can do to still make the experience really exciting and delightful and celebratory, and I would not lose that, but just don't do it at the expense... And I think it's also about figuring out, you can get away with doing more of this for users who are deeper into their streak experience than users who are starting, where it's like your goal for the one-day streak user is just to make sure, do they understand how this feature works?

(00:44:06):
Even something... Again, just another random experiment. At the bottom of the streak screen we have a calendar, and over the years it just looks more and more calendar-like, and that is simply because we find that the more we make it look like a calendar, days on top, little circles, the check... The more we make it look like calendar, the more that people realize, hey, this is a daily mechanic. And so, think about the screen holistically, but every single thing that you're doing on the screen, how can you use it to communicate what is the point of this feature? How does it work?

Lenny Rachitsky (00:44:37):
This episode is brought to you by Coda. I use Coda every day to coordinate my podcasting and newsletter workflows. From collecting questions for guests to storing all my research to managing my newsletter content calendar, Coda is my go-to app and has been for years. Coda combines the best of documents, spreadsheets, and apps to help me get more done, and Coda can help your team to stay aligned and ship faster by managing your planning cycle in just one location, set and measure OKRs with full visibility across teams and stakeholders, map dependencies, create progress visualizations, and identify risk areas.

(00:45:12):
You can also access hundreds of pressure-tested templates for everything from roadmap strategy to final decision-making frameworks. See for yourself why companies like DoorDash, Figma, and Qualtrics run on Coda. Take advantage of this special limited-time offer just for startups, head over to coda.io/Lenny and sign up to get six free months of the team plan. That's coda.io/Lenny to sign up and get six months of the team plan. Coda.io/Lenny.

(00:45:43):
I imagine one of the biggest wins was just giving people flexibility along the journey, like streak freezes and all these things, is that a big vein of opportunity discovery?

Jackson Shuttleworth (00:45:52):
It is. Actually, I'm going to show you one of the most thoughtful gifts that anybody has ever given to me, this is our Duolingo Serenity, or Streak Serenity Prayer, my co-lead, Antonia-

Lenny Rachitsky (00:45:52):
It's like knitted, right?

Jackson Shuttleworth (00:46:05):
... [inaudible 00:46:05] this for me. It's amazing.

Lenny Rachitsky (00:46:06):
Wow.

Jackson Shuttleworth (00:46:06):
And so it says, "Luis, grant me the serenity to accept the flexibility I need, the courage to reach perfection when I can, and the wisdom to celebrate regardless."

Lenny Rachitsky (00:46:14):
Aw.

Jackson Shuttleworth (00:46:15):
And that actually is kind of our strategy with the streaks.

Lenny Rachitsky (00:46:19):
I love the show and tell by the way, that was great.

Jackson Shuttleworth (00:46:20):
Yeah. Well, I guess for podcast listeners, we'll have to get an image somewhere. This idea of flexibility versus perfection, and then regardless, celebration, is core to how we think about the streak. Because I think for the streak for us, it's very much a bend not break. If you're going to miss a day, I'd rather you come back, having missed that day, to an intact streak, but if you don't have to miss a day, I'd much rather you don't, I'd much rather you come back and use the app every day. So, that thing on flexibility though, that's almost certainly been the biggest, from a mechanic perspective, the biggest DAU driver. One of the earliest experiments we ran was going from you used to only be able to have one streak freeze and then we let you have either two or three. So, we tested two different arms. It was, again, another huge DAU win.

(00:47:12):
This actually is funny, it was something that... And this is, again, a callback to that growth model post from Jorge. It actually was really bad for CURR because we were basically saying, hey, you can take a day off, and that's okay, but it was really good for, this is going to be like Alphabet Soup, [inaudible 00:47:31], a weekly active user return rate. So, basically, users who had taken a day off, we were getting them to come back more at higher rates, and so it made up for our losses in CURR. But effectively, what this meant is that, why two streak freezes work better than one was, I don't know, sometimes people just need a little bit more flexibility than one day. But again, the really interesting insight of this experiment was that three streak freezes was actually no better than two streak freezes. And there were two competing things here, and I think this is important if you're going to build a streak to figure out what your flexibility mechanic is.

(00:48:03):
We were getting more users to return after longer times away to an intact streak. But if you start taking three days off from any habit, it's just going to be less likely that you return even four days later. And so, we had these competing things where more users might be returning to a streak, but a lot of users were also just not coming back, we were training them to take more time off. So, that flexibility, what's the right amount of... We've again, this is another area we've run hundreds of experiments on, what is the right amount of flexibility? And we are constantly surprised here. I still don't have the answer for at every point in your streak journey how much flexibility you need. One thing that I can say with certainty though is, give more flexibility when a user is starting their streak. Again, one of our biggest streak freeze experiment wins... I feel like I'm constantly saying this, one of our biggest wins, but they all were really, really big.

(00:48:59):
One of our biggest streak freeze wins was when you start a new streak, we give you two streak freezes. And again, it's so funny to think back, it's like how are we not doing this to begin with? But at the time, the streak freeze was an overly gamified mechanic, you had to buy them with gems, that's our in-app currency, because we wanted the whole idea of this to feel like it was really something you earned, that there was a little bit of pain to getting that streak freeze. And so, we tested though, what if we just give users when they start off their streak two streak freezes, and holy smokes to that win.

(00:49:33):
And it's sort of obvious now, in retrospect, but if you have a one or a two or a three-day streak, it's really easy just to let it die and restart, again, you need to get to seven days, what we've seen in the data, for it to really lock in. And so, giving users more flexibility so that it's harder to lose their streak initially, and then conversely, and this is what we keep learning, eventually, once people get on long streaks, you don't want to give them as much flexibility. Because there's a lot of times where, yeah, users don't... And I'm like this, I've got a 400-day streak. Note that that is a lot less time than I've been at Duolingo, I have lost and restarted streaks a lot of times at my time at Duolingo.

(00:50:14):
But you start getting on long streaks, and you really care about this feature, you really care about your streak. And most people, as long as you're not backpacking through, I don't know, the back country of Utah, you'll be in a place where you can get service. And so, figuring out who is the user that actually could use Duolingo, and not conditioning them to start taking days off that they didn't otherwise need to do is important to figure out where that line is for your feature.

Lenny Rachitsky (00:50:46):
This is fascinating. You can also buy a streak, right? With money. That's a feature, right?

Jackson Shuttleworth (00:50:51):
Yeah. And it's funny, this is also something that we [inaudible 00:50:54]-

Lenny Rachitsky (00:50:53):
You can buy a freeze, sorry, not a streak.

Jackson Shuttleworth (00:50:56):
Yeah. So, you can buy a streak freeze, and the way it works is you can buy gems, and then you can use those gems to buy a streak... And this is something we wrestle with. We're actively working on an experiment, right now that's having a small hit to revenue, but it's a really nice win for retention, and I think it's actually worth thinking about from day one, as you're building a streak, do you see this more as a monetization feature, or do you see this more as a retention feature? What's the role of monetization in this? What's the role of retention? And I think for us it started out much more organically, and so we have a lot of monetization hooks, that again, is the retention PM, I would love to get rid of. But again, it's sort of part of how the streak works right now. And so, we always have this tension of, hey, if we start to make it harder to buy streak freezes, then fewer people buy them, buy gems to buy them, and so there's this more convoluted series of impacts that happen.

Lenny Rachitsky (00:51:49):
Yeah, no, I love that people wanting to buy streak freeze is like the ultimate sign of how much streaks matter.

Jackson Shuttleworth (00:51:57):
Yeah, streak freeze is the other big one that we've recently demonetized, or introduced a free option for, is getting back a lost streak. So, used to lose a streak, we had a feature, in the day, back in the day, called Streak Repair, we'd give you your streak back, you had to pay gems. But what we found that worked way better was a feature called Earn Back, and this is basically where you would have to do a certain number of lessons, as long as you came back within a window soon after losing your streak, do a few lessons and we just give you your streak back. And that was such a retention winner. And again, what we thought about was it feels like you've earned it so much more when you've done... You deserve to have your streak back, we haven't cheapen the streak because you've done something.

(00:52:44):
And in this sense, this idea of cheapening the streak is something, like from a philosophical... Philosophy of the streak. From a philosophical level, we wrestle with all the time, of, cool, we're giving out more streak freezes, at what point do we cross the line and users start to realize their streak means nothing? Now, everything that we've seen, users are totally cool with using streak freezes and still thinking about their streak is this meaningful thing, but my co-lead, Antonia, who made that awesome cross-stitch for me, she is the keeper for us of the sanctity of the streak. And a lot of times as we... And I think this is really important to have, as you're thinking about building your streak. You can almost always get engagement wins, up to a certain point, by just cheapening the streak, making it easier to extend, letting users have more flexibility, but you kind of got to hold the line at some point.

(00:53:30):
And it's not clear where that line is. And once you... You talk about one-way doors or two-way doors, there's a point where you go too far and it's a one-way door, and all of a sudden those users, those 9 million users on one-year streaks don't care about their streak anymore. And that is, I don't know, again, retention PM perspective, that'd be an extinction level event for us. I don't want all of these users to stop caring about their streak. And so, to have somebody who is invested in the sanctity of this streak, and for us it's Antonia and Luis, he's very good about this, is really important, just so you make sure you don't go too far.

Lenny Rachitsky (00:54:06):
That's an awesome insight. So, to protect... And push notifications I think are another example of this in general for companies, how much is too much? Because everyone is just like, let's just send another push, it's fine, just one more. And so, your solution to that is a person is like the keeper, and almost the gatekeeper, plus the founder, of how far is too far.

Jackson Shuttleworth (00:54:26):
It's good if you can have that. I think push notifications are also easier because there's a lot of things you can do around, all right, we'll send a budget cap for how many notifications we'll send, you can-

Lenny Rachitsky (00:54:36):
It's like [inaudible 00:54:38] policy.

Jackson Shuttleworth (00:54:38):
Yeah, policies. But I think with a lot of things, at least for the streak, it's harder to create policies for in the same way, a lot of it has to be done based on feel, and so you just got to use your best judgment at times.

Lenny Rachitsky (00:54:49):
Sweet. Okay. Any other, maybe one or two more lessons from this journey of what streaks has become today.

Jackson Shuttleworth (00:54:56):
You mentioned notifications, and I've mentioned this a few times. One... It's funny, you tend to think of, exactly as you say, you can just always send another notification, it's going to be some win, and at some point it'll be a bad experience, but it's tough to see that. There's actually a notification that we... So, we send two notifications related to your core streak each day, the first is a practice reminder, we send it, this is actually an interesting insight, 23 and a half hours after you practice the day before. Whoa, that is a lot.

Lenny Rachitsky (00:55:21):
23 and a half. Okay,

Jackson Shuttleworth (00:55:23):
So, basically, if you practice at noon today, we'll send it to you at 11:30 AM tomorrow, and we have done-

Lenny Rachitsky (00:55:31):
And it's, because it's like assuming they are free in that time the day before, maybe they'll be free at the same time?

Jackson Shuttleworth (00:55:36):
And we actually moved, we used to let users set this practice reminder time, and our thinking was, cool, you're going to say 7:00 PM, that's when I really want to extend my streak each day, and then you know what? I say this to somebody with two kids, life gets in the way, life always gets in the way, and when you think you're going to practice will change, your life will change, whatever. And what we realize is the best indicator of when you should practice was when did you practice the day before. We could almost certainly get more detailed, we have tried a bunch of ways to have much more complex logic, and what always wins is 23 and a half hours.

Lenny Rachitsky (00:56:07):
That's so interesting. Revealed behavior versus stated.

Jackson Shuttleworth (00:56:10):
Yeah, exactly. So, again, we send this practice reminder 23 and a half hours later, the other thing that we'll do though is we'll send a, what we call a streak saver, and this is at 10:00 at night, if you have not extended your streak, we'll send you a message saying, hey, it's your last chance, this is it, if you don't extend your streak. And you would think that, that's kind of spammy, that's kind of annoying, to get a notification from an app at 10:00 PM, but what we found is because people care about their streak, their streak is this good thing that they attach positive emotions, that they don't really want to lose, that notification reminding them, hey, come back and... People see this by and large as a positive notification and not a negative notification.

(00:56:53):
Obviously, it serves our purpose as well of getting users to come back and not lose their streaks, but again, I think if you can think about your notification strategy related to what is the feature that it's tied to, how do users perceive that? You can almost certainly, not get away with more, but you can be thoughtful about notification load, and when to send notifications, and again, for us, this late night message, that's also highly impactful, super good, is actually something that could be perceived as spammy, but a lot of our users really do... Somebody who, it's often late at night, and I work here, and I'm like, oh, forgot to do my... I was think about Duolingo all day, here it is, 11:15, and I still haven't done it, that message is really powerful.

Lenny Rachitsky (00:57:36):
Yeah. It has saved me many times, I totally know that message, and I love that it's a late night message from an app, very rarely do you actually, are happy about that, and I love that this actually is a good example where-

Jackson Shuttleworth (00:57:51):
It's really funny, all of the stories that you hear about people extending their streak, if you look around a Duolingo party, where it's like 11:30, 11:45, all the Duolingo employees, they're are doing their lesson at the last minute. You always see these pictures of people in the club doing, or at a concert doing Duolingo, and yeah, because it's like otherwise you're going to use a streak freezer, or God forbid you will lose your streak.

Lenny Rachitsky (00:58:14):
That's so funny. Okay, anything else? And if there's more than one more, definitely share, but any other really interesting lessons or wrong turns or insights?

Jackson Shuttleworth (00:58:23):
I talked about streak freezes, and we've done a lot with streak freeze, but I think if you're going to make flexibility a thing, it's probably also useful thinking about how do you celebrate perfection. And so, we have a feature that we have, it is the simplest thing in the world, it's called Perfect Streak. And it's just, if you don't use the streak freeze for a few days, we make your streak look gold, and we make your little progress bar on the calendar just look a little bit nicer. There's no reward for doing it, you don't get anything other than this nice little indication, and it is awesome. It is a simple feature, it is ultra not complex, and it is really powerful, not only for getting users to, as a bit of a reward, they'd be hey, get to seven days without using a streak freeze and your streak becomes perfect, but it's also a really nice indication of users who aren't using streak freezes.

(00:59:14):
Here is the thing that if you don't use a streak freeze, which, again candidly, I would love for you never to use a streak freeze, if you don't use a streak freeze, your streak will stay perfect. It's funny, we actually just, we're constantly responding to bug reports about the streak. It is... I swear to God, we have the best infrastructure around this feature because it is so important. We had an employee who lost her, I think a four-month perfect streak, and it was a big deal for her because she did her lesson, and she was crossing international dateline, there was a bunch of stuff going on that was like, it was just kind of weird in our backend. But people start to care about perfection as much as they do their streak, and for that person it was a big deal when they lost their perfect streak. And so, this is just an example of, look, if you're going to go after flexibility, which is good, finding a way to pull users back into perfection is a really important counterweight to have.

Lenny Rachitsky (01:00:13):
What I'm imagining is you guys need a Amazon style chatbot that just gives you the streak back, it's just like, okay, here you go.

Jackson Shuttleworth (01:00:20):
We have very much... So, we have, if people lose their streak, there's ways to get in contact with us, but we've actually thought about that, where it's like, okay, we should just build a self-service feature, and if we think that your excuse is good enough, whatever, we'll just [inaudible 01:00:34].

Lenny Rachitsky (01:00:34):
Yeah, yeah. [inaudible 01:00:35].

Jackson Shuttleworth (01:00:36):
Because again, I'd much rather you be on a streak than have lost it, particularly [inaudible 01:00:41].

Lenny Rachitsky (01:00:41):
Right. But it also can feel that easy. I love this, I also love this point about just the power of the animation and user experience having impact, that's really interesting. Is that something you find often, just celebrating and making it feel really amazing without copy or any feature is just like, holy, you're awesome?

Jackson Shuttleworth (01:01:02):
This is another thing where it's like when users care about the feature, using not only animation, haptics, sound effects, using... And it's funny, we don't have sound effects on the streak, this is probably something we'll look at in the not too distant in future, but haptics are something we have done a lot of testing on-

Lenny Rachitsky (01:01:18):
Like the phone vibrating in various ways.

Jackson Shuttleworth (01:01:20):
Yeah, exactly, your phone, there being a really cool haptic pattern as you extend your streak, all of this stuff wins. And it's cool because I think it wins... There's a few reasons. One is it just makes you feel good, you get some cool moment in your streak, and we celebrate you, and we celebrate you in this visual way, and your phone's buzzing, it just feels awesome. The other thing it does is it causes you to pause on that screen, and I think there's this desire, as you think through a lot of, as PMs think through, oh, how can I get users through this funnel as painlessly as possible? I talked about [inaudible 01:01:52]. There's a lot of times where I don't, I want you to stop. I want you to stop and land on the screen.

(01:01:56):
You got to be careful not to do this for too many screens, but the one big ones, sometimes I just want you to pause there and enjoy the moment. If I can get you to enjoy the moment more, you're going to care more about your streak, and you're going to be coming back tomorrow. And so, animations that are cool, and that cause you to really soak it in, haptics that feel good, all of that comes together to make you really focus on that moment, all of that just gets users more connected to their streak. So, animation in the right times works well and it's something we've had win quite a lot.

Lenny Rachitsky (01:02:29):
Who designs the haptic stuff? Is there a haptic designer?

Jackson Shuttleworth (01:02:33):
For the longest time it would be a product designer, or actually, it initially started as the engineer would be like, all right, would cobble together haptics, based on what they felt good, then it became a product design role, where they would use their best judgment. We actually just recently required an animation studio, Hobbs in Detroit, and now they are the sort of keepers of, they do a lot of motion design work, haptics very close to that, and so they do a lot of that. I do remember trying to hire for a while a haptics contractor, like haptics design, and it was the saddest hiring I've ever done, because it was just, I don't know, it was such a specific... I don't know. I just went through a lot of people who, it's just a really tricky space of kind of sound effects, kind of motion design, sort of technical...

Lenny Rachitsky (01:03:22):
Yeah, such a unique role.

Jackson Shuttleworth (01:03:25):
Very unique specific skill set.

Lenny Rachitsky (01:03:27):
Right. And there's very few apps that really need this this deeply, so you're almost creating this person.

Jackson Shuttleworth (01:03:32):
Yeah.

Lenny Rachitsky (01:03:33):
That is fascinating. That's like a whole podcast on its own. By the way, I was going to say as you're talking about this, I love that it's a win to celebrate people that don't lose their streak, you introduce this way to make it flexible, and that's a big win, and then you go the opposite direction of, if you don't use this feature, you also feel even better.

Jackson Shuttleworth (01:03:51):
Well, and it's funny, you talked about the danger of feature bloat, or we sort of talked about the danger of feature bloat, this is actually something I'm constantly thinking about with this. We have the streak, but then we also have the perfect streak, and we count how many weeks you've had a perfect streak. Well, all of a sudden we have two streak numbers that are competing with each other. It's funny, we actually don't introduce the concept of a perfect streak until after you've hit seven days, and some of this is just because the cognitive load of additional streak features. A lot of our cooler streak features, you got to get on a long enough streak. And not to say we haven't tested it because we have, because we test everything, introducing these features earlier, but what we've found is that pretty universally they lose when we introduce too many things, too many concepts to users too early in the experience, it's just hard for them to manage.

Lenny Rachitsky (01:04:39):
Okay, sweet. I know that we can go down this track for hours and hours, there's endless learnings about all the things you all have done along the journey. I want to shift to talking about how your team operates. So, there's a lot of threads you touched on of just how a team can do this so well, shift 600 experiments, as you said, continue to find opportunity. What are some maybe lessons or advice you'd have for folks that are like, oh wow, I want to work more like this, from your team's experience, how does your team to operate that folks can learn from?

Jackson Shuttleworth (01:05:13):
Yeah, maybe just a little bit of context. Duolingo cares a lot about... So, most of our teams are metric-based teams. So, we do the most work with streak, but the metric, what we really care about at the end of the day is CURR, and DAUs, because we see that DAUs hit CURR. And so, when you can be really laser focused on, my goal each quarter is to make this metric go up, I think it's much easier to make sure that you're working on the highest ROI thing. I think when you think more about like, oh, I want to make this feature better, I think it's easier to get lost in what better means, and how you think about better. And so, I do think that having a really strong degree of focus as a team on what is the metric that I'm caring about, and how is that directing my efforts is-

Lenny Rachitsky (01:05:59):
Versus feature-oriented. So, basically your teams are structured around a metric/a goal/outcome versus we own this feature, or this product.

Jackson Shuttleworth (01:06:07):
So, retention owns streak, I guess, but that's only because we've seen streak drive CURR better than any feature. But we are not, we have this IAP hook with our streak freeze purchases, there are other teams that work on, that can and have worked on the streak, because it's not ours to say, no, no, no, we do all the iterations here, we just know that it drives our metric better. In the same way that leaderboards, we have a team that focuses on how much time you spent, we want users to spend more time on Duolingo so they're learning more. Leaderboards is the best vector for doing it, so that team does a lot of leaderboards work, but every now and then I have an idea that I think will be highly retentive, and I will go in, and I'll pitch to them, and then we'll do some change to the leaderboard to make it more retentive.

(01:06:53):
But I do think having that clear metric of we're trying to drive CURR not we're trying to just make this feature better, helps at least make sure, give the team clear marching orders, and that focus I think is really good for prioritizing backlog.

Lenny Rachitsky (01:07:07):
Cool. This is a really important point, this is the same way Airbnb worked, when I worked there for a long time, is it's, here's a goal that we want your team to be responsible for, you can work on any product you need to hit this goal, as you said, often various products are most connected to what you're doing, but what you're describing is, even though a team's kind of... I imagine you own it from a [inaudible 01:07:29] perspective, and you're like are the shepherd of this part of the feature because it hits your goal, helps your goal most. But any other team can come in and be like, hey Jackson, we need to work on some streak stuff to help with learning, you're like, go for it. Just a tangent there. Do they work really closely with your team if they want to do some work in the code? How does that work logistically?

Jackson Shuttleworth (01:07:49):
Yeah. If you are, again, this is where I say there's soft ownership, we're not against teams doing things to the streak, but if we're going to do something given we probably have multiple quarters worth of a roadmap around the streak... I say probably, we do. Multiple quarters of roadmap for what we can do to the streak, if other teams want to come and mess with it, okay, we got to just figure out how is that going to work with what our plans for the streak were, how do we make sure a lot of times when teams are coming in thinking, hey, let's do this to the streak, they're in context that we might have, and so there's as much of a much simpler version of what we're doing now, a bit of a knowledge sharing, of saying, all right, well, this is what we think about the streak, this is what we've seen work, hasn't worked, how does that influence some of the hypothesis that you have. And so, I think getting that really... Making sure the juice is worth the squeeze.

Lenny Rachitsky (01:08:32):
Good old-fashioned product management work right there.

Jackson Shuttleworth (01:08:34):
Yeah.

Lenny Rachitsky (01:08:35):
Cool. What else is interesting about how you all operate and how you all work to achieve this sort of success?

Jackson Shuttleworth (01:08:41):
Again, my team lead runs, Antonia runs the most... A really process, if you're going to run this experiments, you have to be really process-oriented and really thoughtful about which experiments am I going to run when, how is that going to set up the next one, there's heavy Jira automation, I think sometimes the Atlassian suite makes my eyes bleed, but there's a lot of times where that degree of process helps the team unblock engineers and make them move really fast. And so, making sure that you have really good process around how are you going to run so many experiments, it's worth investing in.

Lenny Rachitsky (01:09:17):
Can you follow that thread actually? Just when you say that, what does that look like? What are some elements of that process to make this work efficiently?

Jackson Shuttleworth (01:09:25):
All the way down to, really detailed roadmaps around, all right, we're running this experiment is based on the results of this experiment, or might hook into an element of this feature, how do we make sure that we're lining up implementation on this so that as soon as this thing runs and we're ready to go, we can start rolling out the next one. I hate features just sitting around and us not, again, continuing that thread. So, it's not just thinking about what's our engineering bandwidth, but also what's the design bandwidth to make sure that we have the next iteration of this feature ready to go. We're planning months out, as we think about these feature iterations, even small ones, feature iterations, because when you lose cycles, not pushing on a feature, it's just sort of lost opportunity. And so, everything from being thoughtful about engineering roadmaps to design roadmaps to product roadmaps, all of that needs to come together in a system.

Lenny Rachitsky (01:10:19):
So, essentially, mapping dependencies across function, and you're saying in Jira you can do this.

Jackson Shuttleworth (01:10:25):
You can do a lot of it in Jira, there is a non-zero amount of Google Docs that we have, that sometimes does things a little bit... I don't know, sometimes it just looks a little bit nicer, it's a little more flexible.

Lenny Rachitsky (01:10:36):
Yeah. [inaudible 01:10:38].

Jackson Shuttleworth (01:10:37):
But Jira is our, it is where the motherload of process is.

Lenny Rachitsky (01:10:42):
Great. Okay. What else?

Jackson Shuttleworth (01:10:44):
Another thing that I'll just say is, we really resist the urge to do the big V1. And I think this is, I shared the streak goal example, where, a lot of times when we're exploring something we will say, okay, well, that's cool, how do we strip away a bunch of stuff and figure out what our core hypothesis is? And then, just ship that thing first as a V1. Because it's easy, and I've found this time and time again, it's easy to add things, features that make them win, I've worked in retention engagement long enough, I can add, I know enough things to pull, and bells to add, and whistles to make something win, but there's a lot of times where it's like cool, t [inaudible 01:11:27] because all the whistles you added, not because of what your core hypothesis was, and a lot of times if you can just really simplify what the feature is, it's also much easier to ship, it's easier to design.

(01:11:37):
You're not designing for a whole system, you're designing for something much simpler. And so, getting everybody to think that way, allows us to end up shipping faster, shipping simpler, designing faster, getting faster approval, getting insight, and then doing what I talked about with streak goal, being able to run iteration after iteration after iteration, add these things iteratively. And then not only by doing this are you able to move faster, but you get confidence at each step of the way, that, hey, my series of hypotheses is actually born out. Or if it's not, cool, then we're going to drop that part of the feature, and then just ship what actually matters.

Lenny Rachitsky (01:12:18):
If I can try to summarize the broad lesson so far that I'm hearing, and maybe you would've shared this, but I'm just thinking, if I were to try to design a company to operate, that we all operate, you essentially map all the levers that drive the business. So, you have this mapping of all the metrics that drive up to growth and daily active users. CURR ended up being the biggest specific metric to drive growth long term, so there's imagining a tree of all the opportunities you could work on, you found this is what is most connected to our growth. You basically just start mining, I don't know if mining is the right metaphor, but just looking for things that move that specific metric.

(01:13:04):
You just look and poke and explore, and then once you find one, you just go real deep on trying a lot of different... You come up with a hypothesis, and a strategy of here's how we think we can do this, and how we can move this, and then you just try a bunch of stuff. There's also this element of the Arrested Development quote, "There's always money in the banana stand," comes to mind, where it's just keep working on, see there's more, there's going to be more opportunity at this.

Jackson Shuttleworth (01:13:29):
When I joined Duolingo, the PM that I took over for, Anton, who used to lead the retention team, I remember saying, "Dude, the streak, it just counts up, you guys have been testing on it for years, how much more work can we do on the streak?" And he was like, Jackson, you child... He didn't say exactly this, but this is how I felt it. Like, Jackson, you child, we're not even 30% of the way optimized. And four years later, I say that with such conviction, we are so far away from... We've made a ton of strides, but we are still so far away, and every quarter where we ship a ton of wins and improvements to the streak, it just continues to prove to me that there is so much more to be done.

(01:14:11):
So, I think your framing of it is... And I would say there's a lot of thought that goes into, again, I talk about the strength of the hypothesis that you have to have as you start to build out larger feature strategy, I do think it's really important to not just do a bunch of random stuff but do it with intent, with a goal in mind, otherwise, you do end up in these local maximas. But yeah, there's still a bunch of stuff that we haven't tried that I think we have high confidence in working out and so we'll keep doing that.

Lenny Rachitsky (01:14:45):
Are there any other, say, lasting lessons from this journey that if someone were to try to operate this way, build streaks into their product, anything you'd recommend?

Jackson Shuttleworth (01:14:55):
Yeah, I really do think it starts with... Streaks are an engagement hack. You can make your app more retentive, I'm almost positive, almost every app out there can make it more retentive. It is loss aversion, that is, again, armchair psychologist Jackson, it's just a thing that works on humans. But if your app is not something that users want to use every day, or whatever cadence you want your app to be, to work on, it's going to be, you're only going to get so much from that streak, and honestly, it's probably going to distract you from what really should matter, which is making your app something that people want to use every day.

(01:15:35):
And so, if you start focusing on the streak but you haven't made that an enjoyable experience, you're just going to waste a lot of time, honestly. And so, I think making sure that you have your core loop of your app figured out, that it is giving value to users, it is something that they want to come back to every day, that really sets the stage for something to layer a streak on. So, resist the temptation, if you don't think you've reached that point, to go too hard down the path of streak.

Lenny Rachitsky (01:16:03):
That's a really good point. Just like a streak is not going to solve your problems if people don't actually care about the core value you're providing.

Jackson Shuttleworth (01:16:09):
No, and honestly, it'll probably cause more problems if what you end up focusing on is how do I make the streak highly engaging, but your app is... You're wasting time that could otherwise be better spent on solving more critical problems. So, that's one learning, the other thing that I'll say is, we met with one of our board members, Bing, Bing Gordon, a few weeks, or a few months ago rather, and he had this comment where he was just like, "The reason why users care about your streak so much is because you care about your streaks much." You being Duolingo. The reason why users care about our streak so much is because Duolingo cares about the streaks so much. And we're like, what do you mean? Well, he's like, well, after every session you see a big streak screen, and it's animated cooler than almost any other screen in the app, and then sometimes you see some other screens, and there's all these other... You don't let a user forget it, you talk about them in messages.

(01:17:01):
And so, I think it's worth thinking about, look, if you're going to build a streak, and then you're going to [inaudible 01:17:06] it off into the corner of your app, where users aren't going to see it, they're probably not going to care about it as much, which might be fine, because there might be other levers that you think are more important to pull on, but there's a reason why we focus as much on the streak as we do, and that's because we want it to be top of mind for users. And that's not by accident then that users start to care about it. And so, I think just as you're thinking about building the streak, making sure that you're giving it the visibility it deserves, if you want it to have the kind of impact that Duolingo has, it's sort of an important hierarchy principle to think about as you design things.

Lenny Rachitsky (01:17:42):
That's such a good point. You look for cues to the app of tell me what I should pay attention to, what's important? If you're just like fire, explosions, you made a streak, oh, maybe I should pay attention to this feature. And then the push notifications obviously encourage you there too. Anything else along those lines?

Jackson Shuttleworth (01:17:58):
Maybe final thing is, look, we ran so many tests on our Duolingo streak to figure out what worked. We have a philosophy at Duolingo, of test it first. We are a lot of times willing to test things. I really think that if you're going to try to introduce a streak, or you want to improve on the streak you have, don't get too caught up in the philosophy of everything, make sure your hypotheses feel like they're good, but my recommendation is just try things. And this is, again, you said it earlier, it's like this is as much human psychology as anything, and as soon as that becomes the case, you kind of just got to understand what users respond to. And the easiest way to do that is to stop spending time batting around ideas in a conference room and just try some stuff. So, huge recommendation to if you're going to invest in a streak, try and figure out what works through testing with users rather than trying to get it perfect on the first try.

Lenny Rachitsky (01:18:57):
Say someone's listening and they're like, should we do streak, is this worth doing? What's your take on just the chances that a streak feature would be helpful to another consumer?

Jackson Shuttleworth (01:19:07):
I am well known for saying in the company that I think every team, every app could benefit from a streak. Now, how you implement it is very different, and I think you got to, what is your user's use case? If they're going to come use, I don't know, tax software... Okay, you know what? Now that I say this, tax software would be a hard one, but maybe it's all about you need users to come back every day, during the tax season, or how many times... I don't know. Now, that I say this out loud-

Lenny Rachitsky (01:19:35):
Times you upload your [inaudible 01:19:37] forms.

Jackson Shuttleworth (01:19:37):
Yeah, that is a hard use case. But the vast majority of companies I think have a good idea of like, all right, here is my ideal use case, I want users to come here three times a month, that would be ideal. Or four times a month. You can build a streak to work. Peloton has weekly streaks because the idea of doing a Peloton workout every single day was hard for this user during COVID. It was just like every now and then you get on the Peloton, that was great, but the idea of a weekly streak was something that I could keep up. And so, I think figure out what your usage pattern is, as a user, and then build your streak around it. But as long as you're not a really, again, the tax example is probably a good counterfactual, but as long as you have some degree of frequency in your use, I think almost anything can have a streak.

Lenny Rachitsky (01:20:29):
So, Duolingo, it's, again, a $14 billion company, this feature, possibly the most contributing factor, other than the core product, to that level of success in market cap, and it's hard to imagine another just feature of a product that has had this much impact on growth and revenue and building this sort of business. So, I love that we spent this much time on it, the motherload, the motherload of advice and insights. So, thank you again for putting-

Jackson Shuttleworth (01:20:59):
Of course. Very fun.

Lenny Rachitsky (01:21:00):
With that, we've reached our very exciting lightning round. Are you ready?

Jackson Shuttleworth (01:21:05):
I'm ready.

Lenny Rachitsky (01:21:06):
First question, what are two or three books you've recommended most to other people?

Jackson Shuttleworth (01:21:10):
All right, I'll start with A Guide to Midwest Conversation. So, I'm based in Kansas City, I'm a proud Midwesterner, and us Midwesterners talk in a certain way. I think you hear about Minnesota nice, but we tend not to say what we mean, and it is a very funny primer into what Midwesterners actually mean when they say what they say. So, highly recommend reading that.

Lenny Rachitsky (01:21:33):
I like that you give that to people, just like, here's what I might be telling you, which you may not read.

Jackson Shuttleworth (01:21:38):
My wife is German, and I gave it to her so she could better understand.

Lenny Rachitsky (01:21:40):
I see German being the opposite of that, okay.

Jackson Shuttleworth (01:21:44):
Very different. Another book, this is a good one, Fate is the Hunter. This is a really cool book, it's a memoir of one of the early commercial airline pilots, and it is wild to hear the stories about what flying was back in the day. I'm a former management consultant, I flew every week for almost six years, and I never once had to worry about, am I going to make it to the other end of this flight alive? That was not the case back then, and so some of the stories about what it used to be like to be a pilot on some of these planes, before modern aviation technology, is fascinating, and makes you really appreciate what we have.

Lenny Rachitsky (01:22:20):
It feels good to read a book like that, being a software PM or engineer or whatever, how different that life is.

Jackson Shuttleworth (01:22:28):
Hardware is hard.

Lenny Rachitsky (01:22:28):
Hardware. Oh man, it's not haptic design. Okay. Next, unless there's any other books you're going to share? No, okay, great. What's a favorite recent movie or TV show you've really enjoyed?

Jackson Shuttleworth (01:22:40):
So, I have two kids, I watch a lot of Bluey, it's really good, I swear, it brings me no shortage of joy. But adult show or show not meant for four-year-olds that I have watched, I just finished the latest season of Emily in Paris, man, wonderful. I realize it's not the highest brow of television, but just beautiful people in beautiful cities, solving problems that are not earth-shattering, sometimes it is nice to just tune out. Also, I'm learning French on Duolingo, slight plug for the app, I can understand a lot of the French that is being spoken, and there is no better joy than having invested as much time as I have in French, and actually being able to use it. So, huge fan of Emily.

Lenny Rachitsky (01:23:21):
That is so funny, what a fun Venn diagram of interests. My mother-in loves Emily in Paris, I saw someone tweeting about what Visa is she on? How is she still in Paris?

Jackson Shuttleworth (01:23:33):
Yeah. You best just not ask questions, there's a lot of questions for this show that are better left unasked.

Lenny Rachitsky (01:23:40):
[inaudible 01:23:40] Okay. Do you have a favorite product you recently discovered that you really like? Other than Duolingo.

Jackson Shuttleworth (01:23:44):
Last week I went to Home Depot, and I bought a new ladder, and ladder innovations, you don't think of often, but you can make one of the legs go a little bit further than the other leg. And as somebody like myself who has a house that is built on a slight slope, every time I go up on my ladder, I take my life in my hands, but with this ladder, I'm always even. I cleaned my gutters twice last week just because of how awesome this ladder has... How much this ladder has changed my life. So, ladder innovation, I don't think it gets talked enough about and so I'm happy to give it the spotlight it deserves.

Lenny Rachitsky (01:24:18):
I appreciate you doing that, and it's the first ladder recommendation we've had on the podcast. Two more questions. Do you have a favorite life motto that you really find useful in work or in life they share with folks?

Jackson Shuttleworth (01:24:26):
This probably will not be much of a surprise based on how I've talked about our willingness to test things, but you miss 100% of the shots that you don't take. I'm a big fan of just trying things, even if your possibility of success is not 100, because you learn a lot along the way.

Lenny Rachitsky (01:24:44):
Final question, do you have any fun traditions at Duolingo, amongst either the PM team or the company in general that might be delightful to share?

Jackson Shuttleworth (01:24:53):
We have way too many traditions to count. I will share the weird tradition that we do at every retention standup, and this started during the pandemic, we obviously used to stand up in person, and then when we went remote, we did this thing where whoever's the last person to go would count down 3, 2, 1, and then we'd all try to clap at the same time, which was kind of fun and dorky, but we fell in love with it, and four years later we're still doing it. Recently we've added, we all say yee-haw in unison afterwards, I can't tell you why. But trying to synchronize a clap via Zoom, and then all shouting yee-haw... I did this in a phone booth the other day and after I came out someone told me, "You know that those aren't as soundproof as you think," but when you get a good opportunity to give a yee-haw, you can't pass up on it, so.

Lenny Rachitsky (01:25:47):
I love these little things, they sound so minor, but they're such important elements of team culture and tradition, and so important for PMs to find ways to just have fun and do something ridiculous.

Jackson Shuttleworth (01:25:58):
I will say, it took a while to get people behind shouting yee-haw, but now that we have people doing it, you can't take it away [inaudible 01:26:08], we all love it.

Lenny Rachitsky (01:26:09):
Oh man, I called our all hands for a while, y'all hands, feel free to steal that.

Jackson Shuttleworth (01:26:14):
You get it, you get it Lenny. Yeah.

Lenny Rachitsky (01:26:17):
I get it. Jackson, this is incredible, I feel like people are going to listen to this with notebooks, and just like, okay, here's a bunch of ideas we should try with whatever we're working on, whether it's streaks or not. Thank you so much for being here. Two final questions, where can folks find you online if they want to reach out, learn more, learn more about Duolingo? I know you're hiring product managers, so share more there, and finally, how can listeners be useful to you?

Jackson Shuttleworth (01:26:37):
Yes, you can find me on LinkedIn, that is where most of my online social media is, so Jackson Shuttleworth, and then how people can be useful to me, yes, as you said, we are hiring. We're actually hiring for my team. Are you interested in thinking about streaks as much as we do? We might be the right home for you, so please, you can apply on our website. We're also hiring from a number of other product management roles, and they're all as thrilling as this work is.

(01:27:05):
And then, I'm always interested about how other companies have implemented streaks and what they've learned, and so what I'd say is if you're a company who's implemented a streak maybe in a different way than Duolingo has, or you found a whole ton of success and another vector, another element of the feature that we didn't talk about today, I would love to know more. I used to catalog basically every streak I found out there, and as it's become more of a popular feature, it's just been hard to keep up on. So, if you have interesting streak insights to send my way, I would love to hear them.

Lenny Rachitsky (01:27:41):
I love that, a collection of all the best ways of doing streaks. Jackson, just I want to say congrats to your team and you for having so much impact. This is like the dream of a lot of PMs and teams, is to see this much impact and continue to ship wins, and so congrats, nice work.

Jackson Shuttleworth (01:27:57):
Thank you very much.

Lenny Rachitsky (01:27:58):
Thanks for [inaudible 01:27:59]. And with that, Jackson, thanks so much for being here.

Jackson Shuttleworth (01:28:02):
Yeah, thank you Lenny, this was a lot of fun.

Lenny Rachitsky (01:28:04):
Same. Bye everyone.

(01:28:07):
Thank you so much for listening, if you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lenny'sPodcasts.com. See you in the next episode.

