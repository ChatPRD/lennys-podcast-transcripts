---
guest: Keith Coleman & Jay Baxter
title: An inside look at X’s Community Notes | Keith Coleman & Jay Baxter
youtube_url: https://www.youtube.com/watch?v=8dgyqYHLcCI
video_id: 8dgyqYHLcCI
description: Keith Coleman (VP of Product) and Jay Baxter (founding ML engineer),
  the minds behind Community Notes, reveal how a small, scrappy team inside Twitter/X
  built the most trusted crowdsourced...
duration_seconds: 6478.0
duration: '1:47:58'
view_count: 8772
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- okrs
- roadmap
- iteration
- experimentation
- analytics
- hiring
- management
- strategy
- vision
- mission
- competition
- market
- persona
---

# An inside look at X’s Community Notes | Keith Coleman & Jay Baxter

## Transcript

Lenny Rachitsky (00:00:00):
The work that you guys do has had such a tremendous impact on the way the world works. I want to start with just giving people a brief understanding of what is Community Notes.

Keith Coleman (00:00:09):
Someone on X can see a post. If they think it's misleading, they can propose a note that they think other people might find informative. Other people can then rate that note.

Jay Baxter (00:00:18):
We actually look for agreement from people who have disagreed in the past. And what we see is when people actually have that sort of surprising agreement, that's what makes the notes so neutral and accurate and well- written, really, overall.

Lenny Rachitsky (00:00:31):
There's many people that are very polarized. How do you deal with people that are super anti-vax, super Jan 6?

Keith Coleman (00:00:36):
One philosophical thing that's important is that we want all of humanity to participate and sometimes people are surprised by that. We have all of humanity. We then have the data to understand what notes will be helpful to actual humanity. Every post is eligible for notes. We shouldn't exempt Elon. We shouldn't exempt government figures. We should be like everyone... Even advertisers can get notes.

Jay Baxter (00:00:58):
There have been external studies run by people totally independent of us who have found that if you take a post with or without a Community Note, that actually people's agreement with the core claims in the post does change if they see it with a note versus without.

Lenny Rachitsky (00:01:13):
Is there anything else along the lines of just working for Elon within an org Elon runs that might surprise people?

Keith Coleman (00:01:18):
If I were to start a company in that company, it would be even leaner than I would've made it before. I've been amazed with just how much the team is able to accomplish with a small group and I think because of a small group-

Lenny Rachitsky (00:01:33):
Today, my guests are Keith Coleman, Product Lead for Community Notes, and Jay Baxter, Founding ML Engineer and Researcher for Community Notes. This conversation may be my newest favorite podcast episode so far. Community Notes is one of the most impactful and clever and, also, underappreciated products in the world right now.

(00:01:52):
If you ever use X/Twitter and you see a note underneath a tweet correcting the misinformation in that tweet, that is Community Notes. I've never heard a deep dive into the story behind the product and the team that built it and I'm excited to bring you just that. We get into the surprising origin story of the product, how the algorithm actually works, how the algorithm emerged out of an internal contest within Twitter, the principles behind Community Notes, and why staying true to them has been so key to its success. Also, how it survived four different leaders, including Elon and Jack, and why it's now a big part of the solution to solving misinformation on the internet. Including recently being adopted by Meta as their main fact-checking tool. This is an incredibly special episode and I'm so excited to bring it to you.

(00:02:36):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a subscriber of my newsletter, you now get a year free of Notion and Superhuman and Granola and Linear and Perplexity Pro. Check that out at lennysnewsletter.com.

(00:02:51):
With that, I bring you Keith Coleman and Jay Baxter. This episode is brought to you by WorkOS. If you're building a SaaS app, at some point, your customers will start asking for enterprise features like SAML Authentication and SCIM Provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features.

(00:03:19):
Today, hundreds of companies are already powered by WorkOS. Including ones you probably know like Vercel, Webflow, and Loom. WorkOS also recently acquired Warrant, the Fine Grain Authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases.

(00:03:51):
If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:04:15):
This episode is brought to you by Productboard, the leading product management platform for the enterprise. For over 10 years, Productboard has helped customer-centric organizations like Zoom, Salesforce, and Autodesk build the right products faster. And as an end- to-end platform, Productboard seamlessly supports all stages of the product development lifecycle from gathering customer insights, to planning a roadmap, to aligning stakeholders, to earning customer buy-in, all with a single source of truth.

(00:04:43):
And now, product leaders can get even more visibility into customer needs with Productboard Pulse, a new voice of customer solution. Built-in intelligence helps you analyze trends across all of your feedback and then dive deeper by asking AI your follow-up questions. See how Productboard can help your team deliver higher-impact products that solve real customer needs and advance your business goals. For a special offer and free 15-day trial, visit productboard.com/lenny. That's productboard.com/lenny.

(00:05:19):
Keith and Jay, thank you so much for being here. Welcome to the podcast.

Keith Coleman (00:05:23):
It's great to be here. [inaudible 00:05:25].

Jay Baxter (00:05:25):
Thanks for having us on.

Lenny Rachitsky (00:05:26):
It's so my pleasure. I'm so thrilled to be having this conversation. The work that you guys do has had such a tremendous impact on the way the world works. So many product teams are always talking about driving impact and want to drive impact. You guys have actually built things that have changed the world in meaningful ways and continue to do that. And I've never really heard the backstory of how Community Notes came to be and how it works and all these things, so I'm really appreciative of you guys making time to chat.

Keith Coleman (00:05:52):
Yeah. First, thanks for saying that. That's why we built this thing is to help people and it's great to hear it. It's great to see people enjoying it and finding it useful.

Lenny Rachitsky (00:06:02):
I want to start with just giving people a brief understanding of what is Community Notes. I think a lot of people kind of heard about it, kind of maybe see it on X. As they scroll through, they see these notes but they're like, "I don't actually know what this is." So can you just briefly describe what is Community Notes?

Keith Coleman (00:06:18):
Community Notes is a way for the people, like the public, to add context to posts that might be misleading. The basic way it works is that someone on X can see a post. If they think it's misleading, they can propose a note that they think other people might find informative. Other people can then rate that note. And if the note is found helpful by people who normally disagree with each other, indicating that it's probably accurate, it's probably really neutrally-worded, it's probably informative, then it will show to everyone on X. The goal is just to get people more information about what they're seeing so they can make better decisions in their lives.

Lenny Rachitsky (00:06:57):
Amazing, and I think hearing this, it's absurd that this works. I think when people originally heard this idea like, "No way this is going to work." And so, just to dive a little bit deeper, can you give us a deeper understanding of how it actually works? Because I think it's the algorithm that you guys designed that is so clever that allowed this to work. So talk a little bit about that algorithm.

Jay Baxter (00:07:22):
Yeah. So I think a key misunderstanding a lot of people have if they haven't really dived into details, they just think that maybe someone can write a note and it appears immediately or we're just taking a majority rules vote of who thinks the note's good. I think both of those approaches would probably lead to biased or inaccurate notes. I think the key thing, really, that we do is we actually look for agreement from people who have disagreed in the past.

(00:07:48):
And what we see is when people actually have that sort of surprising agreement, that's what makes the notes so neutral and accurate and well-written, really, overall. It's just that people who are very polarized, overall, often can't find agreement when things aren't accurate, right? I think it also provides some good anti-manipulation properties. I think people are often... If you said... I think back in 2020 before we started building anything here, whether this could work at all, I think a room of ML engineers would say, "Oh, you have to keep it closed source. People are going to be manipulating this all the time. You have to use ground truth labels from fact checkers. There's no way that you could bootstrap the system without external labels." But it turns out that you can do that with this kind of bridging-based agreement algorithm is what we call it.

Lenny Rachitsky (00:08:41):
Okay. So just to summarize and make it super clear. It's basically people... Someone writes a note. This information is fault... What's a good example, just as we talk about this, like a classic example?

Keith Coleman (00:08:50):
A really classic example is an AI generated image or an out of context image like, "Look what's happening here." But it's actually from five years ago in a different country and a different topic or something-

Lenny Rachitsky (00:09:00):
Oh, man. I've seen this so many times where it's like, "Look what's happening in San Francisco," and I'm like, "No, this is a whole different city and that's not-"

Keith Coleman (00:09:06):
Totally. Yeah.

Lenny Rachitsky (00:09:08):
Yeah. Okay. So someone posts this AI image. Someone writes a note, "This is actually five years ago in a different city," and this algorithm helps understand if this note is true and it's just regular people doing this.

Jay Baxter (00:09:23):
Yep. Regular people who have signed up to be Community Notes contributors. So there are a few checks, like you do have to have a verified phone number for instance. But yeah, at the end of the day, these are regular people. Not necessarily professional fact checkers or anything like that.

Keith Coleman (00:09:40):
And yeah, that was really important to us too. There was a question at the beginning, to the point Jay was making of like, "Did anyone think this was going to work?" Obviously, it was a crazy idea. We didn't know if regular people were going to be able to do this task and certainly people had concerns about whether they would do it effectively.

(00:09:58):
Initially, some people inside the company were suggesting like, "Hey, why don't you have journalists or some select group be the first participants?" But very specifically we were like, "No. We're trying to move away from the idea of curated editorial decisions being made around this. This is supposed to be open to everyone." So we very intentionally try to allow all humans in. People are randomly selected and that's important to it feeling fair, feeling open, feeling trustable.

Lenny Rachitsky (00:10:27):
Yeah. And again, it's just like this sounds like the holy grail of understanding what is true and it actually works. And works so well that Meta recently, as you all know, decided to adopt this exact system for them instead of having tens of thousands of fact checkers reviewing things.

Jay Baxter (00:10:46):
One distinction that I would make, which maybe can come off as nitpicky but I think is important, is Community Notes adds additional context. It's not fact-checking necessarily, right? So there are cases where the post could be true. But maybe, it's just misleading because there there's no context or there's missing context. We cover those cases and I think that's an important distinction. We just have the philosophy that users should be able to make up their own minds, right? Like, "Here's extra context, take it or leave it," right?

Lenny Rachitsky (00:11:18):
Yeah. What I think about, you shared this with me, this example of a picture with a cat and somebody's Community Note was just, "That's a dog." Or is it the other way around or that's a-

Jay Baxter (00:11:31):
Yeah. "A Palestinian boy shares his bread with a dog," was the post and it's a picture of this cat. So obviously, this particular note is not super necessary because it just says, "That's a cat," and links to a Wikipedia for cat. It's a good example that the system is... This is not something a professional fact-checker or whatever or you think would need fact-checking. But it's proof that the system is really run by the users at the end of the day and adds some comic relief, I guess. And the note is correct.

Lenny Rachitsky (00:12:06):
Okay. It's important.

Jay Baxter (00:12:08):
Yeah.

Lenny Rachitsky (00:12:08):
When does a post get triggered to even be considered for Community Note? Is there a threshold or is it just you can write a Community Note on anything and people decide what they would vote on? How does that work?

Keith Coleman (00:12:19):
So every post is eligible for notes and that was, again, another really important principle. It's like, "We shouldn't exempt Elon. We shouldn't exempt government figures. We should..." Everyone, even advertisers, can get notes. So any posts on the platform can get a note. And if you look in practice, you'll see notes appearing on world leaders, on Elon, on ads, on media organizations, and on, obviously, just regular people using social media. But yeah, the idea is really that it's an even playing field. For a note to be proposed, the person proposing it has to have earned the ability to write notes. So there is that aspect where you have to earn in to be able to do this. And the way you earn that ability is through your ratings by demonstrating the ability to help identify notes that are found helpful to a broad range of people. So basically, if you have an ability to see and know, recognize what's helpful with a lot of people, then you have the ability to start proposing notes.

Lenny Rachitsky (00:13:20):
I actually signed up to be on... What do you call these people? Note take-

Jay Baxter (00:13:24):
Contributors.

Lenny Rachitsky (00:13:25):
Okay. Contributors. Yeah. So I've been rating. I haven't achieved-

Keith Coleman (00:13:29):
Nice.

Lenny Rachitsky (00:13:29):
I can't write notes yet.

Keith Coleman (00:13:30):
Yeah. It's not super easy. It takes some effort.

Lenny Rachitsky (00:13:33):
Are there stats you can share about the scale of Community Notes at this point, especially things that might surprise people?

Keith Coleman (00:13:39):
Yeah. I mean, the service is growing rapidly, so there are hundreds of notes per day. And to put that into context, I saw some stats recently from someone at UC Berkeley saying there was something like 10 traditional fact checks a day. So in contrast, there's hundreds of notes a day that are getting shown. They span a huge range of topics from, obviously, politics, news, out to entertainment, sports, gaming. Just whatever is going on that day.

(00:14:07):
In addition to there being hundreds of these individual notes, they can also be matched to multiple posts. So if someone writes a note on an image or a video, like let's say it's AI generated or something like that, that note will automatically be matched to all posts that contain the same image. So you can have a single note matching to thousands of posts. And over let's say the last year, 2024, we had something like 95,000 notes that were seen about 30 billion times. That's more than double the prior year. Prior year was something like 37K notes seen 14 billion times. So that rate is increasing dramatically when you think about 30 billion views, that's a lot of information that is getting out there that might not have been out there otherwise, which is pretty cool. And part of the reason it is expanding like that is the contributor base is expanding. There's something like 950,000 contributors around the world. That's nearing a million people making this happen which is amazing.

Lenny Rachitsky (00:15:13):
Wow. And I'm one of those, right? I count as a contributor?

Keith Coleman (00:15:15):
Yeah. Yep. No. If you're signed up as a contributor, you count.

Lenny Rachitsky (00:15:16):
Okay. Cool.

Jay Baxter (00:15:18):
Then, there's more people on the waitlist too. So there's plenty of headroom for more growth. Regarding the matching on media and URLs, I think that's a huge way to get extra coverage. Also, I do think we've been very careful to make sure that those matches are precise. Because I think one thing that people love about Community Notes compared to other types of fact checking is that, actually, the notes are custom written for the particular claim you're seeing, right? So often, a fact check warning would just say something like, "Get the facts here." And then, there's a link to some generic page about voting information, which is so not helpful to have the information behind a click. So pulling the context up so that you have zero clicks that you need to make and keeping it specific is so important.

Lenny Rachitsky (00:16:11):
One feature I love that I imagine you guys thought deeply about is if I liked the post in the past, I get notified later if a community note shows up, so that I'm not remembering this false information.

Keith Coleman (00:16:22):
Yeah. I mean, we try to make notes as fast as we can, so we want them to appear instantly if possible. But inevitably, there's going to be a time gap between when a post goes live and when people figure out what's going on and when they get the note out there. And so, we send those notifications to try to close that gap. And yeah, we get a lot of love for that. We see people take screenshots and share them. They're excited about it. And it's also a pretty cool example of something you can do on the internet, in the social media world that was difficult in a print or standard news world where you would see maybe a correction the next day in a corner of a paper that was hard to read. Here, you're getting a ping about it if you've engaged with a post and note shows up.

Lenny Rachitsky (00:17:05):
One user feedback point is I'd love the push to just tell me, "Here's what you got wrong." Because I find that I actually have to go into it and read it and I feel like the push could just be like, "Here's more context to this thing." You're like-

Jay Baxter (00:17:20):
Agreed.

Keith Coleman (00:17:20):
We'll go take a look at that-

Lenny Rachitsky (00:17:21):
There we go. Live user feedback.

Keith Coleman (00:17:24):
Nice.

Lenny Rachitsky (00:17:25):
Okay. I want to get into the origin story of this whole thing. But two more questions, because we're on this thread. One is what's the the threshold for a note to show up on a note? Is that information you can share, just how does that work?

Jay Baxter (00:17:35):
So just because of the details of the way the algorithm works, it uses this machine learning algorithm called Matrix factorization where we fit it with Gradient Descent and whatnot. The threshold is it's 0.4 on this made up scale-

Lenny Rachitsky (00:17:52):
0.4. Great.

Jay Baxter (00:17:53):
Yeah. I mean, in practice, what it means is basically a majority of people... If there is a polarized divide relevant to the notes. Obviously, some notes are not about politics or something polarizing. But if there is, then a sizable majority of people on both sides would generally need to find the note helpful. And then, there are other rules that come into play beyond that main one. So even if it's above that threshold, it might get filtered out if... There's a separate algorithm that's looking at agreement between people's incorrect tags. So like maybe people found the note helpful but incorrect, right? It happens. And in those cases, it doesn't matter if it's above the helpfulness threshold.

Lenny Rachitsky (00:18:39):
This is probably the wrong way to think about it, but is it 40% of people that normally disagree, agree-

Jay Baxter (00:18:45):
No.

Lenny Rachitsky (00:18:45):
Okay. It's-

Jay Baxter (00:18:45):
It means nothing like that. It's just like on some arbitrary scale-

Lenny Rachitsky (00:18:48):
Okay.

Jay Baxter (00:18:48):
Yeah.

Keith Coleman (00:18:49):
Yeah. If we change random other things about the algorithm, that number would also have to change to an equally seemingly arbitrary number. We arrived at some numbers like that by gauging user feedback. So we could share a lot of notes with people, get feedback on which ones are helpful, and just a line emerged about indicating where things go from questionable to pretty clearly helpful.

Jay Baxter (00:19:13):
Yeah. And it is set right now, by the way, to be really conservative, I think. We just are pretty particular about quality and we really want note quality to be really high. I think Keith and I both believe that we live or die based on the quality of the notes at the end of the day. So we'd rather not show a note that maybe good, but we didn't have enough signal on than the other way around.

Lenny Rachitsky (00:19:41):
That makes so much sense. I've never seen a Community Note that is wrong and breaking that promise is a big deal. So I completely get why you guys are super conservative there. Okay. Two more questions [inaudible 00:19:53] because I'm just curious. These weren't on my list of questions to ask, but I feel like people wonder this. How many notes are written versus end up showing up and triggering on a-

Keith Coleman (00:20:02):
We probably show about 8% of notes that get proposed. It's been between, let's say, 7% and 10% or 11%, something like that over time. The number can vary a little bit. And as Jay said, there are undoubtedly... And you can see it, there's clearly more good notes than we show, but the goal is to hold a really high bar. We want to show a note when it's going to be helpful, when it's not going to appear biased and undermine trust in the system. We want these to be neutral, informative, helpful. And as Jay was saying, we view the worst possible mistake as showing a bad note because that's going to undermine trust and the trust is why people like the product.

(00:20:47):
So yeah, the bar is there. And like I said, there's clearly some in that remaining, let's call it 90%, that are good. And then, there's a lot that are just not that great and there's some that are bad. And if you write one of these ones that are bad which bad being defined as people who normally disagree find the note not helpful, so it's like the inverse of the ones we show. If you write one that people normally disagree, find not helpful, you actually will ultimately lose your ability to write and have to earn it back. That other 90% is a mix. Sometimes people look at the number, they're like, "Oh, why don't you show more?" It's like, "Well, you probably actually don't really want us showing most of those." The gold here is that the system is able to filter out the good ones.

Lenny Rachitsky (00:21:31):
That makes sense. Okay. One other question is there's many people that are very polarized, like very disagreeable with a lot of things. How do they filter into this algorithm? How do you deal with people that are super anti-vax, super Jan 6, like all these very extreme potential views?

Jay Baxter (00:21:47):
If people really are so polarized that there isn't agreement among people that typically disagree, it's possible that this is one of those notes that might be correct, but it wouldn't be helpful to show as context. Maybe it's about a claim that people have really entrenched opinions about and they've read hundreds of things about it already.

(00:22:15):
Probably this is just not going to improve people's understanding. It's just not going to be a helpful user experience. So it might not be the worst thing in those cases to not show the note. People, a few years ago, were pretty pessimistic that maybe fact-checking never changes people's understandings about what's true. Actually, there have been external studies run by people totally independent of us who have found that if you take a community note or posts with or without a community note... That actually, people's agreement with the core claims in the post does change if they see it with the note versus without. So we are having an impact on this thing that people previously thought was maybe not so easy to do.

(00:22:59):
And so, it's nice to focus on the cases where there is the bridging agreement. I would also say there is this reputation component to the algorithm as well. So if you consistently rate notes in a way that is counter to the bridging-based consensus, then we will stop counting your ratings. So if you're the kind of person who constantly rates bad notes as helpful, we do filter you out. So there's a difference between those types of people versus the good but polarized ones.

Keith Coleman (00:23:30):
Yeah. I think one philosophical thing that's important is that we want all of humanity to participate. And sometimes, people are surprised by that. They'll be like, "Oh, aren't there people who shouldn't be doing this?", or like, "Their thinking is so extreme or something, maybe they shouldn't participate." But our view is it's actually we want to have all of humanity here. Because if we have all of humanity, we then have the data to understand what notes will be helpful to actual humanity. We can better model that better or better understand and better show those notes.

(00:24:03):
So it's advantageous to have people who have all sorts of points of views and we don't expect that every note will be loved by every single person. That's an impossible bar. But we do intend to show the notes that 80% of people are going to read and say, "Wow. I'm glad I knew that." And so, in that sense, it doesn't matter how maybe extreme someone views a person's views as. It's still great to have them in the program. So no matter what your views are, please sign up and participate. It helps identify what's really helpful.

Lenny Rachitsky (00:24:39):
Cool. And we'll link to people if they want to actually sign up, so they know how to do this. Something we didn't actually specify, these are all volunteers. No one's getting paid to be doing these notes and voting, right?

Keith Coleman (00:24:49):
Yeah. It's totally based on intrinsic motivation and we think that's a great reason to be doing it. When you talk to the most active contributors, a lot of them, they want to have better information out in the world and that's a great motivation. So yeah, that's why they... If you think about, like for these people, the impact they can have is nuts. So when we first launched US-wide, this was like in 2022, a note appeared on a White House tweet and the White House deleted the tweet and reissued an updated statement.

(00:25:25):
Imagine being the person who wrote that. You probably have 12 followers. Your posts probably get a couple likes. And here, you just put a note on the White House and they changed their public talking points based on what you did. That is an incredible amount of impact. So you could see why people are motivated to do it when they care about what's going on in the world. You don't have to be a big, well-known person to shape the discourse and information flow in a way that's helpful.

Lenny Rachitsky (00:25:59):
It's insane. There's so much to love about this. One is just the meritocracy of this whole operation of just anybody that is true and correct can participate and have impact. Also, it just shows you how much information we get that is just wrong. We had no idea how often we see things that are wrong and now we do.

Keith Coleman (00:26:18):
Working on this product has made me realize just how many things I used to trust by default, that now I look at more skeptically.

Lenny Rachitsky (00:26:26):
Definitely mean these days. Okay. Before we get to the origin story, is there anything else along those lines you guys think might be really important to share, that are really interesting?

Jay Baxter (00:26:36):
Sure. I guess one other thing is that although we don't actually use the fact that a post was noted in the core ranking algorithm, which we think is a nice property. There is a really big impact just organically, meaning not from the algorithm but just from user behavior, where people will like and re-share or quote posts way less when-

Jay Baxter (00:27:00):
Quote. Posts way less when notes are applied. I don't know, for people out there who typically run A-B tests on big platforms, you may already be familiar with this, but 1% is typically an awesome effect size for any algorithm change. We saw more like 30 to 40% engagement rate drops for likes and reposts in A-B tests we were ran when showing a post with or without a note, which is just crazy big. That's just an A-B test on the engagement rate, so that's not the network effect. If you capture the overall network effect of how post spread less by that person's repost, basically if you look top line with a difference in differences approach, multiple different external research groups have both found consistently that there's a 50 or 60% drop in total reposts, which is just nuts after a note is applied. It's having a really big impact on spread actually, too.

Lenny Rachitsky (00:28:05):
That's so great to hear. It's what I would want to see and it's incredible impact. Basically, an AI image of something false would just go crazy on Twitter, and did before Community Notes came out, and now what you're saying is just adding that context, not actually... Like you're saying, the algorithm doesn't demote it. If there's something incorrect, it's just people are like, "Okay, this is false, why would I want to retweet this?" That makes sense.

Keith Coleman (00:28:28):
Correct.

Jay Baxter (00:28:29):
Right.

Keith Coleman (00:28:29):
Yeah, the notes just totally take the wind out these stories. The thing will be going viral, note appears, resharing drops 50 to 60%, and that's it. At 50 to 60% per generation, the virality quickly goes to zero.

Jay Baxter (00:28:45):
By the way, I have very mixed feelings about this next one, but authors become 80% more likely to decrease, sorry, to delete their post after they get noted, which okay, that's great, because less misinfo out there, but I'm pan about, because those are usually the best notes. If the note was so just good that you had no other option but to delete your post, those notes don't get seen by other people, right? Because-

Lenny Rachitsky (00:29:13):
That's hard.

Jay Baxter (00:29:14):
There's an argument, by the way, that seeing... Just because you might see the same misleading claim elsewhere off X, or somewhere else on X, it might be good to actually show... Better to have seen the post with the note than not see it at all.

Lenny Rachitsky (00:29:28):
Yeah.

Jay Baxter (00:29:29):
Unsure about that claim.

Lenny Rachitsky (00:29:31):
That is so interesting.

Jay Baxter (00:29:32):
Yeah.

Lenny Rachitsky (00:29:33):
Yeah, I'd be so sad if I was that community note writer and just... Man, it's so good. They just can't even keep the post up. Okay. Coming back from today's world, where this small amount of code is changing the way people understand the world and what they believe, and making the White House rescind their announcements, zooming back to the beginning of how this whole project started, what I heard just briefly is, Keith, you were just tired of managing PMs, you wanted to just work on something yourself, you wanted to work on something impactful away from corporate BS, and you basically just started looking for something that was impactful, important, and you found this. Talk about just how it all came to be at the beginnings of the story.

Keith Coleman (00:30:19):
Yeah. I mean, for me, the beginnings actually go back to why I joined, it was then, Twitter in 2016. I had a startup and we'd had some acquisition offers, and one of them was from this company, Twitter. It was 2016, it was the middle of the election between Donald Trump and Hillary Clinton, and there were something like three televised debates, but every day, there was a debate happening on Twitter, and it was very clear, this is where people are talking about these things that matter, where information is being shared, where ideas are being formed. As a user, it was obvious that I could get good information there, but it was also obvious that there was questionable information floating around. I remember just looking, as an outsider, thinking like, "Wow, this is a really hard problem and it also seems really important," so we ended up going to Twitter and the company was in a turnaround at that point.

(00:31:21):
My first three years was just helping to get the company growing again, working on everything that was the consumer product, getting user growth going back and people wanting to work there again, et cetera, but a few years in, I was reflecting on what we had done. I think we had done a lot of good work getting momentum going, and people in the us and in the industry had tried things to deal with misleading information, but nothing was really working. It was obvious nothing was working. Nothing could handle the scale of the problem, nothing could handle the speed, and a lot of people just didn't trust the existing approaches. The existing approaches were either fact-checkers or internal trust and safety teams making decisions about what was or was not misleading. A lot of people just didn't want or trust that to be the way this was decided, which is very reasonable.

(00:32:19):
I'm looking at that, I was still managing a large PM team. That's a whole story in itself. That job required a lot of energy in, and I didn't feel like I always saw the output that I wanted to see from it. I didn't see the change in the product I wanted to see and I was contemplating, "Should I go start a company? Should I do something else?" And I kept coming back to this problem. I'm like, "Man, how is the world going to deal with this information quality issue of what we get on social media?" Wherever get it. I'm at this company where you can make a difference on this problem, why not go and try some crazy ideas and see if one of them might work? I had a kid, I came back from paternity leave, I went to my boss, Kayvon. I was like, "Hey, Kayvon. How about I just stop doing my job and I go work on this instead? 'This' being trying some crazy ideas to see if we can deal with misleading info."

(00:33:24):
He was stoked, so I went off and started working on that. It started with just reading any research I could on the problem and existing solutions. What was or was not working, what were the issues, and then into prototyping. Then it ultimately led to us building and piloting this idea that became Community Notes.

Lenny Rachitsky (00:33:46):
Amazing. I have so many questions and we're going to keep going through the story, but when you joined Twitter, what was the... It was called Twitter. At this point, I'm going to try to call it X now, which I know is important to your boss. What era of Twitter was it at that point? It was Kayvon joined and who was the CEO? Because there's been many.

Keith Coleman (00:34:05):
Okay, yeah. I came in December 2016, so Jack had relatively recently come back as CEO to turn the company around, and just to give you a sense of the state of the company, something like a third of employees were leaving every year. Just imagine a third of your team gone every year. The stock was in the toilet, the product was not really growing, so Jack was working on a turnaround and Kayvon was there already. Kayvon was running Periscope with a bunch of video stuff, and that group continued to... Jack was there up through the start of the Community Notes, then Birdwatch Project, and... Yeah.

Lenny Rachitsky (00:34:50):
Okay, and it was called Birdwatch. I don't think we've used that term yet, but that's an important point. It was called Birdwatch initially.

Keith Coleman (00:34:55):
Yeah. It was originally called Birdwatch when we started the project, but obviously, somewhat famously the name changed along the way.

Lenny Rachitsky (00:35:05):
Yeah, maybe let's just tell that story real quick, and I know we're zooming it forward, but just... I have this Twitter thread that I saw between Jack and Elon when they're debating what to call it, and Elon's like, "Birdwatch sounds creepy, I want to change it". Is there anything there you can share?

Keith Coleman (00:35:19):
Yeah, the story there... The story, that's funny. Elon came in, acquired the company, and we had just launched the product relatively recently in the US. It had been in pilot for a year, but we had just made it available US-wide, and I guess he'd been seeing the notes. Soon after the exhibition, he DM'd me and he was like, "Hey, this Community Notes thing is awesome," and I was like, "I'm glad you like it, let's talk," so we talked the next day and he kept referring to it as "This Community Notes thing." I was like, "It's interesting you keep calling it that, because that's actually the very first thing that I called it." The very first figma mockup I made depicting this thing was called "Community Notes." I don't know why, it just felt really natural, so that's the first prototype we had tested.

(00:36:14):
Later, the project changed the same to Birdwatch, but Elon was like, "Hey, let's just call it that." The next day, we just changed the name. It's always notable for the team when you change the name, but really, the team was excited about it. I think it is a much more understandable name. Jack has made fun of it, calling it "The ultimate Facebook name," or something like that.

Jay Baxter (00:36:41):
The most boring Facebook name [inaudible 00:36:44].

Keith Coleman (00:36:44):
Boring name, which is funny, because they're now launching Community Notes. I think it is a very understandable, intuitive name, and I think it has served the product really well. There's a reason it was the name in the very first mockup.

Lenny Rachitsky (00:36:57):
Yeah, I think descriptive names just makes sense. This connection with Elon, and I want to talk later about just how you've dealt with so many strong personalities over and kept this alive throughout so many changes, but before we get to that, you did something that I think a lot of product leaders, angel leaders, just people that have managed people dream of give up all this power, in air quotes, and career trajectory and influence and just, "Forget all that. I'm going to go back to just building something awesome, small team." Is there any advice there that you could share from that experience that you think might be helpful for other leaders to share or to hear to help them maybe do that same jump? Because that's really difficult in practice. Easy to talk about, hard to do.

Keith Coleman (00:37:42):
Yeah, I think it is a difficult jump. I've done it a bunch of times in my career and I've always been very happy with it, where I started with a small team, that it grew into something bigger, and then I was like, "We're dealing with a lot of big production stuff, team's really big. I want to go back to doing something like crazy and new with a small team again." I've done that sawtooth leap a bunch of times, but it can be hard, because certainly, the natural... The classic career path is, I don't know, rewards or running a large organization or being a manager, or things like that, but I think, at the end of the day, you got to work on stuff you love, you got to be having fun, and I think people want to be having impact.

(00:38:29):
I think there's one myth that can get in people's ways. The idea that the more people you manage or the larger your scope is, the more impact you have. I definitely do not think that is true. I mean, look at Community Notes for example. If I had stayed running a large consumer PM team, what would I have produced? 16 more pages of OKRs? I don't know, a bunch of documents? I think building Community Notes has had way bigger impact on the world. It's become the industry standard for how to deal with this now, which is super cool. People love it, it's the first thing that is plausibly dealing with the internet-scale issue of information quality. I think it's unquestionably a bigger impact than I would've had if I were just doing whatever, doing some standard management track thing like I was doing before. I think that's true of so many other small companies and startups. Someone screenshotted I think it's Blake Scholl's LinkedIn the other day. He went from director of coupons or something to building the first supersonic-

Lenny Rachitsky (00:39:37):
Yeah, from Groupon.

Keith Coleman (00:39:41):
Those stories are everywhere when you look, so I definitely have found that, for me, I love building hands-on, I love trying crazy new ideas. I love the zero-to-one experience. It's fun to scale things up too, and it can be fun to operate at scale, but this team is a good example of one that operates at a very large scale, but that is still very small.

Lenny Rachitsky (00:40:03):
Yeah, I think the way you guys operate is what more and more companies are trying to do, remove middle management layers, create small teams that just execute and build impact, just like Ics. Whenever I say IC, I have a comment on YouTube, where like, "What is IC?" I'm just going to explain, individual contributor, non-manager is when I say the word IC. Let me follow this thread, and when I asked people about how you set up the team to operate effectively and protect it initially, there's this term, "Thermal," that came up a lot. It was like a thermal team, if that's how you describe it.

Keith Coleman (00:40:37):
Yeah.

Lenny Rachitsky (00:40:38):
What is thermal?

Keith Coleman (00:40:39):
Yeah, so anyone who's worked in a larger company probably knows that things can get bureaucratic or bogged-down, decision-making can be slow. There's these large planning cycles, people can try to take someone from one team, move them to another at random arbitrary times that can disrupt a project, all sorts of things like that. Our company, this is a number of years ago when we started this project, we had a lot of founders in the company. Kayvon is an example of founder who is helping to run the company, and he had this idea, "Hey, why don't we create this program, call it Thermal, where we could have teams that were somewhat isolated from that." They could run through their own process, they would have one clear owner. The team would be entirely dedicated to that project and we would just repeatedly make funding decisions as to whether to continue the effort.

Lenny Rachitsky (00:41:31):
Why was it called Thermal, by the way? What was the idea there?

Keith Coleman (00:41:35):
I think it was an old bird analogy of thermals lifting the bird on their wings. Twitter 1.0 obviously had a lot of bird analogies, bless its heart, so that was one of them. I loved the idea, as someone who liked the startup environment, so when we were starting this project, I was like, "Hey, Kayvon. Why don't we make this the first Thermal project?" And he was like, "Yeah, let's do it," so we started with that way of operating and it gave us, from day one, a lot of freedom and autonomy that I think was really important to make the product work.

Lenny Rachitsky (00:42:15):
Just be very specific about it. What makes it a Thermal project? How do you set that up? This is asking from perspective, if a company wants to build their own something like this, what does that look like?

Keith Coleman (00:42:24):
Yeah, I think there's a bunch of key attributes. One key attribute is there's one clear driver of the project, who's effectively a founder. I guess maybe you could have two or something, but really clear, there's driver of the project and also there's one clear decision-maker that they go to.

Lenny Rachitsky (00:42:43):
Outside of the team?

Keith Coleman (00:42:44):
Outside of the team. That was true back when we started and it is true now. If we need something or have a question about something, I talk to Elon. It was like that from the beginning, it's like that now, and I think that's a big reason we're able to make decisions effectively, quickly, in a simple way.

Lenny Rachitsky (00:43:02):
It probably has to be someone very senior, not [inaudible 00:43:05] manager.

Keith Coleman (00:43:06):
Someone senior who can make the decisions you need made, whatever they are. I think that's really important, that clear decision-making structure. Another was 100% focus, so everyone on the project is expected to be totally focused on it. A lot of companies, it can be easy to have people's attention spread across a bunch of things, and it makes it hard to get stuff done. You'll talk to whoever that person is, you'll ask them for help on something, and they'll be like, "Yeah, I'll help you. I got to finish this thing, and it'll take me a week or two and then I'll get to it." A week or two delay totally changes the momentum of a project. When we were 100% focused, we talk in the morning, it's like, "Hey, Jay. Why don't we try this thing in the algorithm?" He's like, "Yeah." Then that afternoon or the next day, we're looking at results.

(00:43:59):
Because of that total focus, the rate of iteration goes way up. Then beyond that, there was also just the ability to use whatever our own decision-making process was. We didn't need to write OKRs or... For others standard practices. Obviously, we had to make sure we were responsibly building the product and everything, but we didn't need to use the standard practices. I think that's another great example, OKRs, I understand why they can be helpful, but they can also be not necessarily the right cadence at which to set goals. I think it's really unclear that quarterly or annual goals are actually the right pace. We would set the goal for the next milestone that mattered, and we would work on that. We reached that milestone, we would have an idea of what was coming after, and then when we hit that, we'd set the next milestone. Whether that was two weeks, a month, three months, whatever it was. We set our own pace and goals at that pace, and that just I think is a lot more natural for the development of something.

Jay Baxter (00:45:06):
The whole OKR determination and planning process took longer than it would take us to pick a goal and then execute on it and finish it.

Lenny Rachitsky (00:45:15):
How big was the team early on that you set up? How many engineers?

Keith Coleman (00:45:19):
It started with just me and then, when we decided to build the thing, we figured we needed about five. We wanted it to be as small as we possibly could. It was clear we needed someone on ML doing scoring, it was clear we needed someone to do some client engineering work, someone to do backend engineering work. There may have been one or two other. We needed a designer and a researcher to help us understand the customer base and make sure we were building the thing in a way that was actually going to resonate with people. I think it was backend, frontend, ML, design research. That was the original team, from what I remember.

Lenny Rachitsky (00:46:01):
Amazing. Basically, one of each function. A question I have for Jay, actually, is there's all this talk of small teams and moving fast, but sometimes you just need more engineers to build the thing. Is there anything you've learned about just how to keep a team small while moving as fast as you are, and not need or need to hire more engineers?

Jay Baxter (00:46:22):
I think, in the beginning when we were iterating on what should even the requirements be, it was definitely good to just have one ML engineer, but I think, at some point, we got clear on what the goals of the algorithm should really be and we tried... I think, at the very beginning, it wasn't clear that we needed to build this bridging-based algorithm. The actual first algorithm that I put into production was very focused on anti-manipulation. It was this page rank variant, but it didn't solve the problem of bias, basically. If there are more users on one side, a page rank type graph algorithm can actually amplify those biases. I think, after building that prototype and getting data from that, it was clear that the bridging-based algorithm was going to be the way that we needed to solve it, and at that point, basically I set up a bake-off. Kind of a Kaggle competition or something. That was the key time where it was really important to pull in other engineers.

Lenny Rachitsky (00:47:34):
That is such a cool story. I want to follow that thread. Before we do that, you just mentioned you guys yell "Thermal." What does that mean? Is that YOLO, like a version of... Okay.

Keith Coleman (00:47:43):
We're just going to ship, because we're thermal project.

Jay Baxter (00:47:46):
Ship it.

Lenny Rachitsky (00:47:47):
Okay. Marketers, I know that you love [inaudible 00:47:52], so let me get right to the point. Wix Studio gives you everything you need to cater to any client at any scale, all in one place. Here's how your workflow could look. Scale content with dynamic pages and reusable assets effortlessly, fast-track projects with built-in marketing integrations like Meta, CAPI, Zapier, Google Ads, and more. A-B test landing pages in days, not weeks, with intuitive design tools, connected tracking, and analytics tools, like Google Analytics and Semrush. Encapture key business events without the hassle of manual setup, manage all your client's social media and communications from a unified dashboard, then create, schedule, and post content across all their channels. If you're working on content-rich sites, Wix Studio's No-Code CMS lets you build and manage without touching the design. When you're ready for more, Wix Studio grows with you. Add your own code, create custom integrations with Wix-made APIs, or leverage robust native business solutions. Drive real client growth with Wix Studio. Go to Wixstudio.com.

(00:48:52):
Okay, so coming back to this algorithm, this is actually really interesting, because I've never heard any of this. I was going to ask just what inspired this actual algorithm, and you basically did an internal competition amongst ML engineers to see who had the most successful algorithm. Netflix-contest style, Kaggle style.

Jay Baxter (00:49:09):
Yeah, yeah. This particular idea of finding content that is liked by people on opposite sides of a polarized divider who typically disagree, this was not an idea out of thin air. I think Keith had found some of Chris Bale's work, he had made this list of accounts that were often liked by people who were on both sides politically. There is other projects, like polls out there that look for agreement among people who typically disagree, but I think that it wasn't obvious that our project definitely needed to use that from the very beginning. When you implement it and compare it against these other type... PageRank seems, obviously, it's designed to be manipulation-resistant. Naturally, if you just have a voting ring of people who all vote themselves up, then PageRank can filter that out very well, but that just wasn't the main attack vector, I guess.

(00:50:15):
We had to get some real data from the pilot to realize that, "Okay, the real thing going on here is people are polarized," so it was only once we got that, the real data from the pilot, that I think it was clear that the bridging-based algorithm was the direction we really needed to go.

Lenny Rachitsky (00:50:34):
I want to come back to the way you operate the team. I hear that you run the whole team off a single Google Doc that's like a four-year-old doc that you just keep adding goals to, bullet points. Is that true?

Keith Coleman (00:50:47):
There is a very long-running doc that has had to be chopped and purged, because it was breaking Google Docs in Chrome at various points in time. It's like a note-taking doc. It's really where we coordinate what we're doing. The team meets on a daily basis, we spend whatever amount of time we need to get on the same page about what we're building. We might talk about anything from what's most important right now to, "What should we work on next?" To, "What are we trying to launch right now, and why is it not launched? What's in the way of launching it?" We might review new modeling or scoring algorithm update and try to understand what's working in it, what's not. We'll just cover whatever we want or whatever feels most important. As you said, we set our goals very dynamically, so whatever seems like the most important thing for us to work on now and next is what we spend our time on. I think that's served the project really well versus feeling attached to some quarterly goals, or something. We'll look at, "What is going to help people the most?" Or, "What's the biggest problem right now?" What are either one of those? And we will go tackle it. We might change our roadmap multiple times in two weeks based on what we see.

Lenny Rachitsky (00:52:08):
I'm hearing no Jira, no Asana, no Monday.com.

Keith Coleman (00:52:11):
No.

Lenny Rachitsky (00:52:12):
Okay.

Keith Coleman (00:52:12):
Yeah, I mean, we have to use Jira to coordinate with some other teams. Sometimes when we file a request, we have to make a Jira ticket. But no, I am not a fan of heavyweight task management. I love being on the same page, being able to keep most things in my head, and having a really light way to write down the things that the team can't keep in its head.

Jay Baxter (00:52:34):
We did use Asana briefly, but my memory of it is that you spent more time in the meeting grooming a backlog of irrelevant stuff than actually talking about the proper priorities. I think it's nice in the Google Doc that, if something becomes irrelevant, it can just fall off without needing explicit backlog grooming.

Lenny Rachitsky (00:52:58):
Just to maybe summarize a little bit of how you guys operate that might inspire other companies to set teams up like this, so I'm going to go through a few things you shared. One is one person in charge of the team, like the founder almost. They're basically the founder of the team. They have one very senior, essentially, sponsor/decision-maker that they interface with. In your case, Elon, no big deal. In other cases, it could be the CTO, CPO, someone like that. The team is focused 100% on its product and goal. You keep the team very small, so you start with one person of each function. One front-end engineer, back-end, ML person, designer, researcher, PM, and then Google Docs is almost basically for your project management. Yeah, it's basically run with Google Docs, stop, don't use big, complicated products.

Keith Coleman (00:53:50):
I think that's a pretty good recipe. On the Google Docs, people can do what they want. If they want to use thumbnails, go for it. I think those first ingredients, really, are key structurally. Then beyond that, it's a matter of having an ambitious goal that gets-

Keith Coleman (00:54:00):
And then beyond that, it's a matter of having an ambitious goal that gets people fired up to go do great work.

Lenny Rachitsky (00:54:06):
Yeah. Awesome. I think there's a lot there that a lot of people think they should do when they set these teams up, but they don't actually do, and it feels like each of these is just a really key ingredient to it to actually succeeding.

Keith Coleman (00:54:17):
It definitely really helped us succeed. I don't know that the project would be here if it was not for some of those elements.

Lenny Rachitsky (00:54:24):
That's a powerful statement. This thing that has changed the way the world understands what is true would not have existed if you didn't set it up in this specific way.

Keith Coleman (00:54:34):
Yeah. I don't know if I would've begun the project had I not known. We had that structure, that ability to make decisions, the autonomy, the speed, the ability to go fast. We started with that in 1.0 and it's been continued and if anything, furthered in X. X as a whole company operates with a lot of those attributes, and I think it's one of the reasons the product is successful. I think those are big reasons why at least, Jay can speak for himself, I have so much fun working on this. I love working on it. It's great to wake up every day and solve these problems. We get to do them efficiently, make decisions quickly, build stuff that helps a lot of people. It's awesome.

Jay Baxter (00:55:25):
This whether thermal or Elon way of operating is definitely more fun and the fact that... That combined with the awesome mission is super important for internal recruiting. I remember when I was first chatting to Keith about this back in early 2020, I had another project. I worked on a few, but one was like personalize the number of push notifications that we send, and it drove a lot of DAU without losing opt-outs significantly. So that was setting me on track, or if I had kept working on that, I could have probably gotten a promotion from that with low risk, or I could take this huge career... It's not as big at a career risk as joining or founding an actual external startup, but there is still career risk, I guess, in joining a team like this. I think all of the same aspects of recruiting that apply to external startups and apply internally, and if you can have an exciting vision, that is key.

Keith Coleman (00:56:30):
Related to that and your list, Lenny, one thing we missed that's super important is that on this project, and I think of successful projects like it in startups, is that people are self-selecting to join. We did not assign anyone to this project. People reached out to join or they applied to join the job. I and the team interviewed every single person that joined the team and we were like, "We want that person on the team. They want to be on the team." And so people are totally bought in to the goal, mission, the way the team works, the other people they're going to be working with. And that makes a huge difference.

(00:57:10):
So a great time to do that is at the start of one of these things. If you're going to try something crazy, it's going to be tough if you're just assigning random people to it. But if you let people opt in and self-select much more likely to be successful. And one thing that I have observed at X, which really surprised me was that this is also possible at a large scale. One of the things that Elon did when he bought the company was he basically asked people to self-select to stay. You had to click the button. And he sent an email out that was like, "Hey, Twitter 2.0."

Lenny Rachitsky (00:57:44):
Fork in the road. Right? [inaudible 00:57:46]

Keith Coleman (00:57:45):
Fork in the road. Fork in the road. Exactly. He's like, "Twitter 2.0, now X, it's going to be hardcore. We're going to do ambitious things. You're going to work your butt off." And you had to click on the form and say, "Yes, I want to join." And I think that was really important for the company because you want people to opt into that. You want the people to be saying, "Yeah, that's what I want to do," and the company's going to be a lot more successful. If people aren't sure, it's better for them probably to go do something else and where they're naturally more aligned and happier. And I thought that was a great approach to taking a large company and getting it down to people who are really excited about working together on a mission. So for us, we did it from day one, which I think is an easy way to do it, but it's possible to do it later as well.

Lenny Rachitsky (00:58:33):
I love that you described it as fun and I think a lot of people when they see Elon laying off a bunch of people, being very hardcore himself, people don't imagine it as a fun place to work. And it's clear how much you guys love working on this, how fun it is and how interesting it is. And it's interesting to hear that 'cause I think a lot of people don't feel that externally. Is there anything else along the lines of just working for Elon within an org Elon runs that might surprise people about just the way of working that's interesting or surprising or you think other companies might want to think about adopting?

Keith Coleman (00:59:07):
I've always liked lean teams, but my experience at X has made me change the way I would think about running a future org-... If I were to start a company and had to change the way I think about starting that company, I would be even leaner than I would've made it before. I've been amazed with just how much the team is able to accomplish with a small group. And I think because of a small group, shortly after the acquisition, we had this product called Spaces. It had been in the product before, but it was pretty small scale, and Elon wanted to run these large spaces. I forget who the first people he was going to bring on were, but he was going to be there. Ultimately, these things have gone on to host politicians and things like that, and he's like, "Guys, we got to scale this up." I forget the numbers.

(00:59:57):
He's like, "We need to be able to scale a million people," or something like that. I'm getting the numbers wrong. "You need to be able to scale way up." This is the kind of thing at 1.0 That would've taken a year if it had ever happened, and the team did it in two or three weeks. And it was really exciting and inspiring to see. I didn't work on that, but I watched it from the outside. I'm like, "Wow, with this tiny team motivated behind a big goal that was like, 'Hey, guys, it's not like, are we going to do this?' It's, 'We are going to do this.'" They got it done in two or three weeks. That must've felt amazing for them. It was certainly exciting to see. But I've definitely come to appreciate just how lean something can be and not just get by but actually thrive because it's that lean.

Lenny Rachitsky (01:00:42):
I think the point you made about people opting into that is important, 'cause I think a lot of people hearing that would be like, "I would never want to be asked to build something like that in two weeks." And I think a lot of people do, and we love that kind of experience, especially working with the Elon, especially shipping something at that scale. But I think there's an important element there of just like, "Okay, I don't want to do that. I have other things to do in my life other than ship spaces." So I think that's a key point you've raised of just there's an opt-in step.

Keith Coleman (01:01:10):
Totally. I think the opt in is important, and it may even be that you want to opt in at one point in your life, and maybe at another point in your life something else is better. I think whatever it is you're choosing to do, it's nice to be opting in to feel like it's aligned with how you want to spend your time.

Lenny Rachitsky (01:01:25):
Something on my mind, and I don't know if you guys want to go here, but it's something I think a lot of people think about is when Elon came in, he let go of 80% of folks. And everyone's just like, "Twitter is dead. It's all going to fall apart. There's no way they can run this thing with that small of a staff," and clearly they were wrong. Clearly, it's working great. It's becoming a massive deal in the world and continues to grow. Is there anything about that that you were surprised by or anything about just how it continues to operate so well in spite of that big shift?

Keith Coleman (01:01:57):
I think the leaner team, the reduced process in bureaucracy is a big reason it does move as fast as it does. It's easier to get stuff done faster here. Yeah. I think that shrinking is actually a big reason for the increased pace of launches, the increased pace of experimentation. One thing that I noticed a result of that is the people who are here, they seem to all really feel like owners. They take the sense of responsibility that an owner takes in the product. They'll try to track down what's wrong, fix whatever is needed, jump in to help build or fix, improve any system that needs help, even if it's outside of their space. And there's the flip side of that too. For people who've worked at big companies, they may have experienced this thing where there's like ano-... You want to change something in some other system or product, and so you reach out to that team. And maybe they're a little resistant, they'll maybe be like, "Oh, we'll get to that next quarter or so-

Lenny Rachitsky (01:03:07):
They have their own goals to hit. Yeah. [inaudible 01:03:08]

Keith Coleman (01:03:08):
Yeah. Exactly. They don't really necessarily want to help you or they're busy. Here, you're like, "Hey, guys, we need to do this thing with that other system you work on." And they're like, "Great! Here's the code. Here are the docs. Send us the fab if you have any questions, and we'll get it in." And it's just the thing, you can just jump in and get it done. And that kind of collaborative effort, like the sense of shared ownership, I think from my experience came from or was a result of the shrinking of the team down to people who wanted to be there and work together to build this thing. So I think that's been a really positive impact. It's not always easy. Certainly, a lot of people have a lot of responsibilities, but they're here because they're up for it.

Jay Baxter (01:03:53):
Yeah. I think one other thing that's key is when you are forced to have such a small team, well, this is important anyways, but deleting code is more important than writing it a lot of the time. So I think so often maybe due to promotion incentives or just regular human tendency, engineers have a tendency to add these little incremental wins that actually add more of a long-term maintenance cost than is clear, because you just run a little one month A-B test, you see this significant win and you don't realize the maintenance burden you just added to your team for the rest of eternity until you turn the thing off. So I think there's a lot to be gained and you get forced to do this, by the way, when you have such a small team. It's just auditing parts of your system and deleting the things where the maintenance cost is worse than the gains. So I think we did have to do this across the company after the big layoffs, and systems are leaner now and they can be worked on by fewer numbers of people.

Lenny Rachitsky (01:05:02):
That's an amazing point. I remember Elon's being like, "Here, we have to throw away the whole thing. We have to re-architect everything. It's stupid the way it's built." And it sounds like that actually worked.

Jay Baxter (01:05:10):
Yeah, so-

Lenny Rachitsky (01:05:10):
Well.

Jay Baxter (01:05:11):
You don't have to rewrite everything from scratch. Some things are good, I guess, to rewrite. But just even deleting the unnecessary cruft and keeping the rest of the core system, that's awesome.

Lenny Rachitsky (01:05:23):
I love that we're creating a formula to run these sorts of companies and teams. There's so much here. I want to go back to the building of the original product. I took us on a long tangent and an amazing tangent, but I heard a story of when you launched Birdwatch at that point. You specifically wanted to keep expectations very low and there was a GIF in the thing, and it just looked like clearly this is not ready for prime time. Talk about just how you did that, how you launched it in a way where people weren't like, "It's never going to work."

Keith Coleman (01:05:53):
We were very disciplined, I guess you could say, about having the product prove itself at every given point. When we built the first mockups, these were just pictures of depicting what community notes might look like. We showed those to people across the political spectrum. We saw, hey, people really like these. Whether they're on the right or left, they seem very open to reading these community notes even when they're critical to people of their own side. So we're like, "All right. That gives us confidence that if we can build this, if we can actually make this as a reality, it's going to work." Then there's a question of can we make it a reality? Will people in the real world be able to write notes that are of this quality?

(01:06:35):
And so we had an internal pilot test version of this where you could write notes. And we first basically ran this through an Amazon MTurk type of participant test just to see if you just put some normal people in there, will they be able to write these notes? All those notes weren't good, but it was clear that there were people out there who could write good notes. So then like, "Okay, this is possible. What will happen if we actually do this out in the real world? And let's run a pilot and find out." And so we took that pilot that we'd run the MTurk of test on, and we released it to at first 1000 people, totally out in public, and we didn't know what was going to show up. You could imagine the notes could have been terrible.

(01:07:27):
And so we were talking, "Well, what do we do? We're going to put this out there. Everyone's going to have all these questions. They're probably going to be really skeptical, and we know it might be a total dumpster fire. And so what do we do to set expectations appropriately?" We felt like we could probably get there in the end, but we just didn't know what was going to happen at first. We wanted to set expectations, and so we're like, "Well, why don't we just stick..." There's the page where you see a post in the notes below. We're like, "Why don't we just stick a dumpster fire GIF on that page?" And you go there, you're like, "Hey, anything you see below here might just be a total dumpster fire. At least it would show we were aware of that as a possible risk." In the end, we did not do that. It cracked me up, but we thought it was like-

Lenny Rachitsky (01:08:13):
Oh, you didn't actually launch. Okay. That was just a concept. Okay.

Keith Coleman (01:08:16):
We had mockups of it, and every time I looked at the mockup, I laughed, but ultimately we had so much to explain on that page, like, what is this thing and how does it work? Ultimately, we're like, "Okay, this is probably going to distract from the point." So we pulled it. I wish maybe it had seen the light of day at one point, but yeah, ultimately we kept it simple and we focused that page on explaining what was going on here. But again, as has happened many times with the project, we put the pilot out there and the notes were good.

(01:08:48):
They weren't all good. It was a mixed bag, but there was gold in there. And from the very early days with just 1000 contributors, it was obvious that people could write notes that were informative, that were neutral, that spoke to controversial challenging topics, and that if we could just identify those from the rest, this was going to work. It was going to work as well as the very first mockups we had made. So that became the focus that is, how do we sift out the gold from the rest?

Lenny Rachitsky (01:09:19):
I think you may have shared with this with me, when someone noticed you guys were testing this and they took screenshots and tweeted it, and I think Elon replied, "This is cool."

Keith Coleman (01:09:27):
Yeah. Yeah. So in the very early days when it was just a Figma prototype, we were running these usertesting.com on moderated studies. I guess one of the participants sent one to an NBC reporter who wrote a bunch of stories on it. Anyway, that day, there was a lot of chatter about it on the service, and Elon... To put this back in time perspective, this is, I think, 2020, so two years before any acquisition stuff happened, Elon is just a Twitter user building rockets and electric cars and other cool stuff and stumbles on this thing that depicts the prototype that we've been testing. And he writes back, "Definitely worth trying, IMO." And I remember thinking that was cool back then and it's interesting to see, he's obviously had a very consistent point on it. I think the idea was appealing and he has obviously been a big fan of it in the product and had been a big supporter proponent. So yeah, it was cool that it came from... that support has been from the very early days before he was ever involved in the company.

Lenny Rachitsky (01:10:36):
I love that moment. That must have felt really wild for Elon to be commenting on this Figma prototype retesting.

Keith Coleman (01:10:42):
It was cool. It was cool.

Lenny Rachitsky (01:10:44):
Oh, man. So when we were preparing for this interview, I asked you guys what's the main thing you want to make sure people get and understand about why community notes has been so effective? And Keith, you specifically said that it was the principles behind how you wanted to approach this and how you continue to stick to this throughout. And we'll talk about how you kept it alive throughout all these different CO changes in leaders. But just talk about these principles, what the actual principles are and why that was so key to it working out.

Keith Coleman (01:11:16):
There are a number of principles that I think when we first shared them with people at the company seemed maybe a little bit crazy. But I think they are the reason the product works, and I think they've been very important, and we do. We come back to them regularly, today, all the time. Probably the craziest one is just that this thing is going to be the voice of the people. It's going to represent the voice of people. It's not going to represent the company's voice. So it is not a tech company deciding what shows. It is the people deciding what shows, and that had a lot of implications on the design. First of all, we don't have a button that will change the status of a note. So if a note is showing because the people have rated it and found it helpful, it is going to show. We can't change that.

(01:12:08):
And that is the kind of thing that when we first propose this, that's unsettling to people. They're like, "Wait, so something can go up and the company can't take it down, or can't change its status, get it to stop showing." And we're like, "Yeah, and it has to work that well. If it doesn't work well enough to do that, then it doesn't work." This is one of our key principles was, if there's a problem with a note that's so bad, you want to do something about it's a problem with the system. We need to redesign the system to be showing good notes. And so yeah, we had to get everyone comfortable with the idea that there was no button to change the status of a note. Similarly, as we talked about earlier, we wanted this to represent all of humanity.

(01:12:53):
And so we didn't want to be arbiters of who can come in and be a contributor and who can't. So we open it to everyone. You just have to meet a really basic objective criteria. You have to have a verified phone to help reduce the likelihood of having bots or things like that participating. But beyond that, it's random selection and it still is that way today. And again, that people took some time to get people comfortable with it. But I think that the fact that this is the voice of the people and reflects their output through an open and transparent process is so key to both why it is good, why it works, but also why it's trusted. So that's number one and I think will forever be the heart of the product. Another one that people thought was crazy was transparency.

(01:13:49):
The previous approaches to dealing with misleading info, it felt to a lot of people, like black box tech companies or media companies or leads or whatever making decisions. We're like, "People need to get comfortable with this. They need to trust this. So the whole thing has to be out in the open." The code that decides what notes share has to be out in the open. All of the data and ratings that make it happen have to be out in the open. People should be able to take the code and data and replicate the whole service and that we have done exactly what we've said we've done. And they should be able to audit it. They should be able to go and look and say, "Hey, I think this part could be better."

(01:14:28):
Or if they think we're biased, they should be able to work with the data and point it out. And if people have good observations, that should factor back into the code. And this is, again, something that's difficult to get people comfortable with, that everything is out there, you can't cover anything up. But I think that's so essential to people trusting it. Yeah, we set these out on day one. We go back to them constantly because we're always evolving the product, and we're always like got to make sure every new change is open. Whenever we update the scoring system, there's an update in GitHub when the data is published daily so you can download it. And so yeah, I think those have been really essential to the thing working.

Jay Baxter (01:15:13):
And by the way, these do not come without a cost. It's actually really hard from an end perspective to actually open source the actual algorithm that's running on the actual data. Because the way large-scale services like this are usually architected does not naturally lend itself to being run as a script by someone who's downloaded a TSV. So we actually have to take weird architectural decisions to make this possible in a way that probably wouldn't have been if we didn't start with this assumption from scratch. We would've had to maybe rewrite the system to make it like this.

Lenny Rachitsky (01:15:49):
What's an example of that?

Jay Baxter (01:15:50):
For instance, there's a matrix factorization that we train. Usually, you would train a matrix factor... train your ML model once and then serve it, I guess with a separate service. But we didn't want to have people externally spinning up services to be able to replicate the system that we had. So basically, I don't think it would've been actually very cool if we had open sourced the code in a way that wasn't actually runnable, I guess, by someone just... At this point, you can download Python code and run a script. You do need a lot of RAM right now, but you can do it on one machine.

Lenny Rachitsky (01:16:35):
Okay. How much RAM are we talking about?

Jay Baxter (01:16:37):
Oh, only like 500 gigs.

Lenny Rachitsky (01:16:41):
Okay. Okay. That's reasonable.

Jay Baxter (01:16:41):
It'll take a day if you don't do anything special to speed it up. Good to know, but yeah.

Lenny Rachitsky (01:16:45):
Cool.

Jay Baxter (01:16:46):
Possible is the key thing, and people have done it. Vitalik Buterin had a blog post where he talks about his explorations, making sure the algorithm really does what it says it does. And I think just the fact that a handful of people have done this, there's enough people who have done it that there's someone you'd probably trust who's verified it.

Lenny Rachitsky (01:17:11):
And that's rolling out to Meta. No big deal. I love just as you described these principles, just I could imagine a PM at a company being like, "Okay, guys. Here, I want to do this project." There's so much idealism to it that rarely works in real life; going to be open source. You're going to give it to everyone. We don't have actual control over what it's going to do, don't worry about it. It's going to just change the way people see this thing that we've been very careful about and then it works. And I think that's very rare and it's really impressive. And what I'm hearing partly is that sticking to those principles was actually really fundamental to it working and not bending over when someone's like, "No, no, no, we can't do this. What if we change this part?"

Keith Coleman (01:17:54):
I think if we had broken with any of those principles, if there was anything black box, if there was whatever, the product would be a lot harder to trust. And so I think it's because we've just stuck to them so cleanly simply that people can trust it.

Lenny Rachitsky (01:18:11):
You've talked about a few moments when it was like, wow, the White House changed their announcement because of the community note. We talked about the dog is a cat. Are there any other moments that after you launched of, "Holy shit, this is working? This is going to actually work."

Keith Coleman (01:18:26):
All along, we saw it working. We wanted to be confident whenever we expanded it to new audiences or new countries or whatever, we wanted to be confident it was going to work. So maybe held our breath a little bit just to see that it would do what we expected, but we always expected that. But that said, there were definitely stress cases. The one that comes to mind is the start of the Israel Hamas conflict in 2023 in October. That was probably the largest deluge of misleading information I've ever seen shared on the internet at one time. It was overwhelming. A number of photos and videos and whatever coming out related to that, it was insane. And just to give you an example, I think it was first three days or something of that conflict, we had 500 notes covering all sorts of different... out of context imagery.

(01:19:32):
Someone would say, "Hey, this is happening here." It's actually from 2013 in Syria. There were people making fake battle footage in the video game simulator Arma 3. So there were notes explaining, this stuff looked realistic. And unless you saw the note, you wouldn't really know. There are all sorts of claims about what was going on in the ground, and that was definitely... The product was still pretty new at that point. We'd expanded in the U. S. less than a year before that. We had been rolling out throughout the world that year and then this large event happened. And I felt like we were just enough prepared at the right time for the system to be able to handle that.

(01:20:16):
Probably one of the most important things we did right before that was launch the ability to write notes on images and videos and have those matched to other posts. I remember at that time thinking, "Wow, I'm glad we launched that feature a few months ago versus still had it on the shelf," because it was really important in that conflict. And I think even it was just a few weeks before we had launched a major speed up in notes too. When we first built the product, the number one focus was always quality. We knew that the product would live and die by the quality of the notes. That was the thing we could never give up on. We also knew it needed to deliver speed and scale, but we're like, "We will get the quality in the right place, and we can speed it up and scale-

Keith Coleman (01:21:00):
Get the quality in the right place and we can speed it up and scale it out over time. And we had actually just launched a speed-up that took three hours off the time it needed to go live, and it was I think a matter of weeks before that conflict happened, so again, super glad that was out there. In the first few days of the conflict the median time from a post going live to a note showing up was five hours, which is like crazy fast. Typical fact checking is like two to four, at least it's really common to see it take two to four days. These notes were showing up in five hours and we're like, we are so glad we got those things out before this happened, it made the service a lot more helpful.

Jay Baxter (01:21:40):
One other thing that was, I think, nice to see working then was, one criticism of Community Notes some people bring up is, well if you always need agreement from people who typically disagree, then in these super polarized settings, that conflict being probably number one, then you wouldn't see any notes. But actually the reality was there were tons of notes about that conflict. So I think there was this kind of nice property where actually, and maybe this is a surprising fact, that there's more agreement out there across polarized divides than maybe conventional wisdom says, and the places where people agreed were really objectively true and verifiable. I guess maybe this is more true the more polarized the setting is, but where the agreement actually lends you, and basically notes that are very neutrally written, very focused on the facts and easy to verify information.

Lenny Rachitsky (01:22:46):
There's this talk for a while of just there's no more facts, nobody believes there is a single true fact anymore, everything is subjective, and I think Community Notes proves the opposite. Facts matter, there are facts that we can all agree with even on the most controversial topics.

Keith Coleman (01:23:04):
Yeah, we saw this really from day one, when we would show those prototypes to people just depicting the idea, it was really obvious that people cared more about, or they cared a lot about understanding reality and what was going on and they were willing to disagree with their side, so to speak, to recognize that. And I think that's not always that obvious to people. The world does feel really polarized, but people definitely are willing to cross partisan boundaries to get to accurate information and that's why the product works.

Lenny Rachitsky (01:23:38):
It feels like as we rely more and more on what we know and understand about the world is becoming social media online and moving this quickly, it's like I'm so thankful this exists because otherwise it'd just be, what do we trust anymore? This being out aligns with we need this thing to exist at the same time. And it feels like at the same time there's also people I just don't trust. I think people have shifted from I trust what I read to, okay, I shouldn't just believe everything I'm reading. Is there anything there you're noticing about just how people think about news they see and their shift of just like, I'm not going to believe everything. Is there anything that you've noticed about just human behavior or just the way we've shifted understanding what is true?

Keith Coleman (01:24:30):
We haven't done any research to look broadly at how people's perceptions are changing there, but I certainly have found myself that particularly seeing notes, I am more skeptical about what I read at first, and I think that's been helpful. And we hear that from people, that they think about things a bit more, and I think that's a good secondary effect and benefit of something like this, which is the more you see the patterns of how what you're reading can be wrong, the more you can thoughtfully question it and try to get a better understanding of what's really going on. So historically I think this was called media literacy, but basic idea of can you understand the ways in which things can go wrong and try to cut them yourself.

Jay Baxter (01:25:21):
Another aspect I think we help with that is discovery of the Community Notes. I think often before Community Notes you could have just been living in a little news filter bubble, or maybe there were fact checks out there that you should have been reading but you weren't discovering them. So the fact that the note applies, it is directly attached to the post and visible by anyone who sees the post helps cross those filter bubbles and can kind of... I think for some people it's the first time they've actually seen counter arguments to claims made in their own little echo chamber.

Lenny Rachitsky (01:25:59):
That's incredible, yeah. I love the point you're making about how it actually teaches people to be a little more skeptical of the things they read. It's an education system more than just, here, this one thing is wrong. I love that.

(01:26:13):
Okay, just a few more questions. There was an audience question asked on Twitter, we all asked on Twitter, "What do people want to know about Community Notes?" one was actually why you guys switched to anonymous contributors, what was the decision behind that?

Keith Coleman (01:26:26):
Yeah, we had this pilot where we were testing with a small number of contributors, a few thousand contributors, and we learned a lot through that pilot. Probably the biggest thing we learned was related to anonymity or pseudonymity of contributors. We had originally assumed that it was important that people contribute under their real handle, or their real name, or whatever it was. The first prototypes depicted that, we kind of thought that would be important for people trusting the note, and actually it was totally wrong. The best option was actually opposite of what we first tried.

(01:27:02):
We found a few things. One, people were hesitant to write a note on a controversial topic because they didn't want to get attacked or harassed online. And so some people were comfortable doing this but others were not, and so it meant there was more potential good notes to be written than were getting written, and this was very clear feedback from the pilot.

(01:27:24):
Two, and this is super interesting, people are actually more willing to cross partisan boundaries when they are anonymous or pseudonymous than when they are under their real name, and it intuitively makes a lot of sense. If you publicly are using your name, you feel are affiliated with one side versus the other, you might hesitate to be perceived as breaking with that side. But you may actually, for example, find a note helpful that's critical of that side, and there's a bunch of studies that show when people are anonymous, they're much more willing to cross partisan boundaries and work with the other side, agree with the other side, and we saw that too. And so by allowing people to be pseudonymous, you actually get more honest answers about what they really think and it helps find disagreement that really-

Lenny Rachitsky (01:28:11):
That's so counterintuitive.

Keith Coleman (01:28:12):
Yes.

Lenny Rachitsky (01:28:12):
You never hear the opposite always, and it's so interesting it's the opposite.

Keith Coleman (01:28:15):
Yeah, yeah.

Jay Baxter (01:28:17):
I think the same principle applies to making the likes private.

Lenny Rachitsky (01:28:21):
I was just thinking that.

Jay Baxter (01:28:21):
Yeah.

Lenny Rachitsky (01:28:23):
Yeah, I like a lot more stuff that's a little, definitely, I wouldn't have liked, yeah.

Keith Coleman (01:28:28):
It allows freedom for honesty, which is pretty great. And one of the criticisms of pseudonymity is it can generate, maybe people have reached the quality threshold that they put out there, but we have so many quality mechanisms in the system that that wasn't an issue, so we could keep quality high while opening up for that honesty.

Lenny Rachitsky (01:28:48):
Another question, you touched on this a little bit, which is around navigating the existing trust and safety apparatus of Twitter, which as you described, basically, previously, it was like we make decisions on what is true and not, and every company works this way, you guys basically upended that like, here's a completely different way, you have no control over what we say is true or not. Talk about just that experience of overcoming that, I imagine, very difficult hurdle of like, okay, forget all that, we're going to do it totally different.

Keith Coleman (01:29:20):
Yeah, it was definitely, what we were proposing was very different. I will say that I think people were sort of open-minded to it, generally speaking, and I think everyone had a sense that what was being done at the time wasn't really working that well or solving the problem, and people were open to new ideas, so that's a good foundation.

(01:29:39):
But I think one thing we did that was probably very helpful in that is we wanted the product to prove itself at any point. First it had to prove that people could possibly find notes helpful, then it had to prove that people could possibly write these notes that would be good quality. And so anytime that we were proposing doing something with the product, like running some research test, or running the pilot, or expanding the pilot, we always had the data that had convinced us that that was a good decision, like we were stepping into the next phase of expansion that made sense. And so I think we probably rarely proposed anything that seemed unwise, because we were holding such a high bar for quality ourselves, and I suspect that went a long way.

Lenny Rachitsky (01:30:33):
So it's partly, what I'm hearing is, take it step by step to prove this is actually working, and partly be confident it is working to yourself before you try to convince the trust and safety team this is the way to go.

Keith Coleman (01:30:46):
Exactly.

Lenny Rachitsky (01:30:49):
Was there a moment along that journey it shifted from no way this is a thing to okay, wow, let's actually consider this? Or was it this very gradual process?

Keith Coleman (01:30:59):
Whether other people were saying no way to wow, let's actually-

Lenny Rachitsky (01:31:03):
Yeah, just internally of just like, okay, we're going to actually stop this trust and safety way of operating and instead rely on Community Notes, was there a moment of like, okay, let's actually make that switch, or was that Elon actually, is that the big switch?

Keith Coleman (01:31:15):
The biggest change there happened in X, the biggest changes prior to that were just the decision to put this out there and have it be operating in public at first US wide scale. But yeah, then the bigger switches came in the X period.

Jay Baxter (01:31:36):
I think even though there was original research before Birdwatch had even started, or Community Notes had even started, from external researchers showing that crowdsourced fact-checkers, laypeople can do about as well as fact-checkers and actually the agreement rates were kind of similar between the groups. I think even though that research was out there, I think there were definitely a lot of people who didn't really believe it could work until it already worked.

Lenny Rachitsky (01:32:04):
Basically prove it, prove that it works. Yeah, that makes sense, versus just a bunch of docs and strategy and thinking, it's just like, look, it's actually working, you can see for yourself.

Jay Baxter (01:32:13):
Yeah.

Lenny Rachitsky (01:32:14):
Makes sense. Okay, possibly last question, we'll see which fractals of questions you guys bring up here. I referenced this a couple times, this incredible achievement of keeping a project alive through Jack and then, I have this note, and Kayvon running the show then, and then Parag running Twitter, and then Elon, and then Linda taking over as CEO, quite rare, especially something this visible, this impactful to everything that X is. Any lessons or keys to that actually working, of this project surviving throughout so many work changes and leaders?

Keith Coleman (01:32:54):
It definitely has been a crazy time to be building something. It's been fun. The craziness has been entertaining. I think one reason perhaps the product has done so well and survived is the nature of the product itself. It is designed to produce information that is found helpful by people who normally disagree. And so even if you have CEOs or leaders who might disagree, there's a good chance actually they'll find it helpful, they'll be like, wow, this thing does produce pretty useful output. So I think there's something in the nature of the product itself, that when people see it, whatever side they're on, left, up, down, they're likely to find it pretty helpful, so I do think that helps.

(01:33:39):
I also think the team executed really well. We had ambitious goals that were exciting, they solved a real problem. This is a real problem that matters in the world. At every step, as we talked about, the product needed to prove itself, and we would make sure it proved itself and we would bring the results that convinced us and we'd share those with people. And so they would say, oh yeah, I agree, it kind of proved itself, let's take the next leap. And we've done that all along the way and we continue to operate that way, and I think that focus on the outcome and goal that matters, and executing against it, really helped.

(01:34:24):
The team did not get distracted by much all through the period during which the acquisition happened. There was a lot of opportunity for distraction. This team was shipping every week, we were super focused on the goal, let's make this thing work, let's get these notes out there, and I think people saw that execution and were excited to support it.

Lenny Rachitsky (01:34:49):
Yeah, like it's working, why would we mess with that? And it's important, and it keeps us from having to hire tens of thousands of people to fact check.

Keith Coleman (01:34:57):
The interesting thing about that is no one ever asked us or brought up or seemed to care about anything related to cost savings in this process. And I think that's an assumption people have outside the company, that this must have been a reason there was interest in it. But that was never a goal, it was not at all why the project was started, it was not why people were excited about the project. And I think that's also, for people outside who maybe don't see the conversations, it's kind of a heartening thing to know, is that the focus was always on solving the problem. The other approach is even if you had 10,000 people doing it, the real issue is that they don't work that well because they're not trusted or they don't scale or they're too slow. And so the goal was really always just help people stay informed at scale. Let's build an internet scale solution to an internet scale problem that people like.

Lenny Rachitsky (01:35:51):
Something I heard about you, Keith, when I was asking people about how this worked and why this worked so well is that they describe you with having a very low ego, and that allowed you to give up this whole team and power and influence and just the name, forget it, whatever you want, we'll call it Community Notes, great. Is there anything in there you can share of just how you think about that and how important that is as a product leader to have a low ego?

Keith Coleman (01:36:19):
For me, this project, I feel like I get to do community service with this project. I see my work as in service of the people and the community, and that's what motivates me. The only thing that I care about is delivering the outcome that the world finds helpful. And so in some ways the project has not been about ego, it's about truth-seeking, let's find... Not truth in the sense of what information is true, but let's find out what's actually going to make this work. How does it need to be structured, what should it be called? Whatever is going to produce the best outcome is what we should do. So I think I feel more attached to the product being helpful than to anything else, and so to whatever degree it might seem like low ego is probably more a result of wanting to actually solve the problem.

Lenny Rachitsky (01:37:15):
And I think partly what I'm hearing is just if you win and succeed, good things will happen, so focus on that.

Keith Coleman (01:37:20):
Certainly satisfying things will happen, it's very satisfying to have people appreciate it. It's satisfying that people on the left and right love it. It's satisfying that even people who receive notes, love notes, and reach out to them and post them, that's amazing, it feels so good to have helped give people that, and yeah, it's very motivating. It's a great reason to wake up in the morning.

Lenny Rachitsky (01:37:44):
It's absurd this has worked, but it's also like of course this would work, of course something like this should work. It's like such interesting-

Keith Coleman (01:37:50):
It's the internet, it's of the internet, that's why it works.

Lenny Rachitsky (01:37:55):
Oh man. Where's Community Notes going from here? What's happening, where's it going, what's the future?

Keith Coleman (01:38:03):
We're always working on basically more better notes faster. So there's clearly an opportunity to get more notes out there, we want them to stay as good or better than they are, we want to get them there faster, so we're always working on core product changes to help deliver that. Recently, for example, we just released an update to what we call the Community Notes bat signal, or the ability to request a Community Note. So anyone on X can say, "Hey, I think this post needs a Community Note," and now they can even add a source explaining why so that when a prospective writer sees that it's much easier for them to write a note. So we're always working on core things like that, core algorithm improvements.

(01:38:47):
I think there are also new frontiers that show a lot of potential, AI and LLMs are one. It's easy to imagine a lot of ways that AI could assist the people in this task they're doing of trying to get information out there quickly. And maybe Jay should talk about the Supernotes work that we've done with some folks outside the company.

Jay Baxter (01:39:13):
Yeah, so one cool thing about having public data and code is that external researchers can collaborate with you, and in this case Supernotes had this idea that we can basically take existing notes as input, existing proposed notes that maybe they have some problem, maybe they have part of the story, maybe they're worded in kind of a biased way. Basically take all these in, have an LLM generate a ton of different variants, and then basically make the simulated jury to basically get a representative group of contributors for community notes who would be rating the note and try to predict based on their past ratings how they would rate these LLM generated notes. And so this way you can actually, rather than just having an LLM write a note from scratch and hoping it's good, you can simulate the entire community notes rating process and explicitly create notes that are likely to be rated helpful by people.

(01:40:18):
So I think ideas like that are very promising for the future, and it's a nice way that LLMs and humans can work together. Obviously agents can browse the web too, and that's one way that you could imagine agents assisting humans is maybe checking whether a note is actually supported by the source. Although then you get into things like, well, are people going to actually be as diligent? Right now I think raters are very diligent because they know just some Community Notes contributor wrote this like, I better check this before I rate it helpful. But hopefully we can design things in a way such that people don't trust the output and actually verify it themselves before issuing a helpful rating.

Lenny Rachitsky (01:41:11):
Yeah, that is such an interesting area to explore where you want to avoid AI hallucinating slop versus make it easier and scale it even further. What an interesting challenge.

Keith Coleman (01:41:23):
What's cool about this project, in addition to the AI element, is that it's being done outside the company. We talked earlier about the open source transparency. The key reason we made this all open source was so people could see how it worked, but the dream is actually that, it's not just that the contributions to the notes and ratings are from the people, but the dream is actually the product is built by the people. What if the scoring algorithm were significantly or entirely written by the public? That would be incredible. And Supernotes is probably the first very substantial potential change in the algorithm of the way it works, that was kind of coming from the outside and plausibly could be part of the core, so we'd love to see the product go in that direction as well.

Lenny Rachitsky (01:42:08):
Sweet, go Supernotes. Well guys, the work you're doing is tremendous. This is every product person's dream, I think to work, on something like this. Small team, lots of support, lots of impact, just innately interesting, and so I think this is going to inspire a lot of people.

(01:42:27):
So let me just ask you, is there anything else you wanted to share? Anything else you think might be helpful for folks to leave them with?

Jay Baxter (01:42:33):
Sure, I guess one thing that just I thought was interesting over the course of working on this product is just there's... I think in a similar way to how retweets originally were not something Jack came up with, I think users just started doing it and then it became a core part of the product. There's a huge way already in which there's just a lot of surprising things that people wanted to use Community Notes for that I don't think we really expected, and it's kind of cool to see those user desires emerge.

(01:43:04):
I think one example, I guess we had always been imagining political type of misinformation, but for whatever reason there's a lot of people who love debating whether Messi or Ronaldo got more goals. I guess it's kind of a funny one. There's a community moderation aspect, so I think we also thought that this would be specifically for adding context to misleading or potentially misleading information, but what you can see is that there are some notes that go beyond that towards calling out content that they think is spammy or something. So I think that's just another dimension in which commuted notes is a product that's driven by the people.

Lenny Rachitsky (01:43:57):
That's so beautiful, basically they're trying to keep Twitter/X healthy and they're just like, no, this should be taken down, this tweet of spam.

Jay Baxter (01:44:05):
Yeah.

Lenny Rachitsky (01:44:06):
I love that. Is there an answer on the Messi versus, who is the other soccer player?

Jay Baxter (01:44:10):
Ronaldo.

Lenny Rachitsky (01:44:11):
Ronaldo, okay. Is there a definitive fact there or is that just unknowable?

Jay Baxter (01:44:17):
Yeah, I guess that's an interesting one because it's a case where raters are actually very polarized. I guess it actually kind of fits into the core algorithm where there's some people who are just diehard Messi fans or Ronaldo fans, just like they could be on politics, so we actually specifically modeled that topic, as well as some other topics, so we can estimate people's opinion on that particular debate. It's kind of funny that something like that would emerge.

Lenny Rachitsky (01:44:45):
You're saying that's the most controversial topic on X, Ronaldo versus Messi.

Jay Baxter (01:44:51):
That's a controversial one.

Lenny Rachitsky (01:44:52):
Oh wow, who knew? Okay. Keith, is there anything you wanted to add?

Keith Coleman (01:44:58):
Yeah, community Notes is cool itself, but I think what it points to about society is actually even bigger. Society often feels really polarized, you hear people talk about it all the time, no one can ever agree on anything, but actually Community Note shows you people really can agree on quite a lot. Even on super controversial topics related to politics and everything, there's a lot of agreement, that's why notes work.

(01:45:23):
And I think that's a really big reason for optimism about the world, is that while it might feel polarized, there's probably like an 80% set of people that agree on quite a lot of things. And imagine if we could use the same kind of approaches we use with notes, but to find agreement on legislation, or policies, or things like that that people want the government or the world to do, possibly we could get a lot more momentum behind these ideas that the people really want and everyone would be a lot happier. Maybe 10% of the people on the edges wouldn't be happy, but I bet there's a lot of agreement that we are not identifying, and if we did it, we'd all be pretty happy. So I don't know, I think it's easy for people to feel pessimistic about the world, but I think this product is a good reason to be optimistic about the future.

Lenny Rachitsky (01:46:12):
What an incredible way to end it. I can also see, Keith, why people want to join you and work with you and work on this team.

Keith Coleman (01:46:19):
Appreciate it. If you do want to join, we are hiring an ML engineer. You get to work on these amazing problems with us and have a lot of fun, so we're accepting applications at x.com/communitynotes.

Lenny Rachitsky (01:46:32):
Okay, great, I'm glad you gave the URL. Oh man, you're about to get flooded.

(01:46:36):
Guys, thank you so much for doing this. Is there anywhere other than that place to go off, join the team as an ML engineer, is there any other place you want to point people to, either your socials or anything else?

Keith Coleman (01:46:47):
I'm KeithColeman on X, please reach out if you have any feedback or want to help us out, whether you may want to work here or want to do something from the outside, we would love to talk.

Jay Baxter (01:46:58):
Yeah, I'm @ _JayBaxter_ at X. Yeah, I think in particular, besides just using Community Notes, it would be great to get more substantial contributions, pull requests, collaborate on projects like Supernotes, I think that's the most exciting type of stuff if people do want to contribute.

Lenny Rachitsky (01:47:22):
Ship some code guys. Amazing. Guys, thank you so much for doing this.

Keith Coleman (01:47:27):
Thanks for having us, Lenny.

Jay Baxter (01:47:29):
Thank you, thank so much.

Lenny Rachitsky (01:47:33):
It's my pleasure. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.

