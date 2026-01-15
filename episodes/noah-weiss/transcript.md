---
guest: Noah Weiss
title: The 10 traits of great PMs, AI, and Slack’s approach to product | Noah Weiss
  (Slack, Google)
youtube_url: https://www.youtube.com/watch?v=XrRlVOWe5GE
video_id: XrRlVOWe5GE
description: 'Noah Weiss is Chief Product Officer at Slack, where he leads all aspects
  of the product organization, including the self-service SMB business, the team that
  launched huddles and clips, and...

  '
duration_seconds: 5134.0
duration: '1:25:34'
view_count: 10335
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- onboarding
- metrics
- roadmap
- user research
- experimentation
- data-driven
- analytics
- funnel
- freemium
- subscription
- revenue
---

# The 10 traits of great PMs, AI, and Slack’s approach to product | Noah Weiss (Slack, Google)

## Transcript

Noah Weiss (00:00:00):
We have this mental metaphor that we talk a lot about, getting to the next hill. The actual wording is "Take bigger boulder bets." I think teams can often get lost crawling up that hill, not realizing that there's a huge, incredibly beautiful range behind it where we've over time freighted new teams from scratch that incubated in a new area before the areas mature.

Noah Weiss (00:00:19):
We did that with a lot of these native audiovisual products like huddles and clips really in the pandemic because our customers were demanding it from us. I think in the AI space, we're trying to hear from customers, what do you wish Slack could do if it had these new superpowers? Let's incubate a couple teams or prototype, give them space to run and pilot and then get something to launch that's amazing. Blows people away. That's the formula that we've seen.

Lenny (00:00:45):
Welcome to Lenny's podcast where I interview world-class product leaders and growth experts to learn from their hard one experiences building and growing today's most successful products. Today my guest is Noah Weiss. Noah is chief product officer at Slack where he spent the last seven years. Prior to that he was head of product at Foursquare, which is near and dear to my heart as you'll hear at the top of this episode. Prior to that, he was a PM at Google and at Fog Creek Software.

Lenny (00:01:10):
In our conversation we cover the 10 traits of great product managers, how to work effectively with strongly opinionated and product-minded founders, what Noah has learned about working effectively with AI in your product over his last 15 years at Google and Foursquare and now Slack. We talk about a process called Complaint Storms that helps Slack build better product. Plus, what he is learned from Slack's self-service business plateauing back in 2019 and how they turned it around and what they took away from that experience.

Lenny (00:01:38):
Also, how he thinks about competition with Microsoft Teams and with Discord. Also, a bunch of new data advice, which I found very helpful. This was such a great in-depth conversation about all things product and leadership, and I'm really excited for you to hear this episode. With that, I bring you Noah Weiss after a short word from our sponsors.

Lenny (00:01:58):
This episode is brought to you by Sidebar. Are you looking to land your next big career move or start your own thing? One of the most effective ways to create a big leap in your career and something that worked really well for me a few years ago is to create a personal board of directors, a trusted peer group where you can discuss challenges you're having, get career advice, and just gut check how you're thinking about your work, your career, and your life.

Lenny (00:02:22):
This has been a big trajectory changer for me, but it's hard to build this trusted group. With Sidebar, senior leaders are matched with highly vetted, private supportive peer groups to lean on for unbiased opinions, diverse perspectives and raw feedback. Everyone has their own zone of genius. Together, we're better prepared to navigate professional pitfalls leading to more responsibility, faster promotions, and bigger impact.

Lenny (00:02:46):
Guided by world-class programming and facilitation, Sidebar enables you to get focused tactical feedback at every step of your journey. If you're a listener of this podcast, you're likely already driven and committed to growth. A Sidebar personal board of directors is the missing piece to catalyze that journey. Why spend a decade finding your people when you can meet them at sidebar today? Jump the growing wait list of thousands of leaders from top tech companies by visiting sidebar.com/lenny to learn more. That's sidebar.com/lenny.

Lenny (00:03:17):
This episode is brought to you by Superhuman. How much time do you spend in email each day? How about your team? You may not realize this, but your email tools are wasting your time. Superhuman is blazingly fast email for high performing teams. Built to work with Gmail and Outlook, teams who use Superhuman spend half the time in their inboxes respond to twice the number of emails and save over four hours a week.

Lenny (00:03:42):
That's over a month of save time per year. With Superhuman, you can split your inbox into streams or VIPs, team members and emails from your favorite products to reduce context switching and make sure you never miss an important email. You can start reminders if you don't hear back so that you can follow up and never drop the ball on an email thread. You can also work faster than ever before with powerful AI features like writing, editing, summarizing and even translating.

Lenny (00:04:08):
Join the ranks of the most productive teams and unleash the power of Superhuman. Try one month free at superhuman.com/lenny. That's superhuman.com/lenny. Noah, welcome to the podcast.

Noah Weiss (00:04:25):
Thank you for having me. I'm excited to finally get to join and been a longtime listener.

Lenny (00:04:29):
I feel the same way in reverse. I've been really excited that you're finally on the podcast. I don't know if you know this, but this is actually going to be the last podcast I'm recording before I go on pat leave. This is going to play while I'm on break. Coincidentally, you're actually just returning from pat leave is what I just learned.

Noah Weiss (00:04:46):
Yeah.

Lenny (00:04:48):
Let me ask you a question. What advice do you have for someone about to enter the beginning of baby life from someone that is exiting that and going back to work?

Noah Weiss (00:04:55):
First off, I mean obviously congratulations, you're about to go on. A rollercoaster of emotion, sleep and everything else. I literally went back to work two days ago. I think my, maybe, advice about being a new parent is better than my advice about being at PM right now. Here are the three ... My wife and I wind up coming up with three maxims that we want to be using throughout the first two months to keep ourselves grounded.

Noah Weiss (00:05:19):
First one, I would say a little bit better every day. No matter how many books you read and how much money ouster you consume, there's nothing like actually doing it. It's a physical thing being a new parent. Getting a little bit better every day, giving yourself permission to be like that didn't go great and that's okay. That's number one.

Noah Weiss (00:05:39):
Number two, don't over extrapolate from the early days. The fourth trimester is a real thing. These babies come out. They're not fully baked. They can't even support their own heads. If you try to extrapolate everything, the next 18 years are going to be the first 18 days, it's going to be sobering. Keep that perspective. They develop so much every week, part of the fun.

Noah Weiss (00:06:03):
Then the third thing, which I got advice from this from a good friend is like you got to fully get into it as a parent. There's nothing that replaces. Actually, you got to change the diapers. You got to do the feeds. When they're up, even though they can't talk, you got to talk to them. You got to listen to what they're saying and just be fully present near the moment.

Noah Weiss (00:06:24):
I realized for myself, and then basically at full digital detox. You saw how long it took for me to reply to your emails. I was like, "Throw the devices away. Just fully with our daughter, [inaudible 00:06:34], and our family." I feel like it was so much more rewarding. I felt really connected with her now after these couple months. It's a crazy time. You're going to really love it. It's going to drive you mad at that times as well. That's all of it.

Lenny (00:06:47):
All right. We're going to be pivoting this podcast into a parenting podcast. This is awesome advice. I wrote everything you just said on this little post-it as you're talking. I'm going to put that up in our nursery and see how it all goes. One thing that's tough about my career path in this weird life is I don't get a nice pat leave, paid pat leave from a big company.

Lenny (00:07:06):
I've actually been working on stacking guest post and podcast ahead of my leave so that I can actually, as exactly as you said, just get fully into it.

Noah Weiss (00:07:14):
Smart.

Lenny (00:07:16):
Yeah. I have awesome guest posts coming. All these podcasts are backlogged, so I'm hoping it all works out.

Noah Weiss (00:07:21):
That's a smart way to do it. Yeah.

Lenny (00:07:23):
On a totally different topic, you're ahead of product at Foursquare. I don't know if you know this. I actually built a startup on Foursquare's API. It's a company called Localmind. For folks that don't know about it, the way it worked is basically let you talk to someone, checked in on Foursquare anywhere in the world if you're thinking about going there.

Lenny (00:07:39):
You could be like, "Hey, is this bar fun right now? What's happening there?" Before you actually show up. We ended up selling the company to Airbnb. Ended up not being a big problem for enough people and that's how I ended up at Airbnb. But it was quite magical and API was amazing. I guess I just want to say thank you for building an awesome product and awesome API.

Noah Weiss (00:07:58):
Thank you for being a developer on top of the ecosystem. I mean it's interesting with Foursquare. I will talk about this I'm sure later. I feel like I have more lessons learned and more scar tissue from the crazy up and down of ... I don't know what. It was 2010 to 2015 roughly. I think there's something actually where you learn more from the things that don't fully work out or don't quite achieve what you wanted to achieve.

Noah Weiss (00:08:27):
You actually have a feedback loop where you get a lot of negative signal about like, "Okay. That didn't work. That didn't work. What can I actually learn, take away from that?" It's still great. I still love using Foursquare. I think we got caught in the death star of Instagram's ascent back in 2012, 2013. But I hope a product like that exists forever in the future and I'm glad you got to build the company, landed Airbnb through it. It's a great story.

Lenny (00:08:52):
Looking back at Foursquare, do you think there was a path to building a massive consumer app type business or is that just never going to work out? I know they went in direction of B2B data business. I guess was there a path or was it just like, "No. That was never going to work out?"

Noah Weiss (00:09:09):
It's tricky. I mean I'm not going to do 30-minute post, because I probably bore everyone. But it's not about this. We've all thought about this a lot on the early team there. I think the biggest probably lesson learned, frankly, is that we were really close with the Instagram folks early on. They were big developers on our platform. They used the Foursquare API before they were bought by Facebook.

Noah Weiss (00:09:28):
I think in hindsight we were a little bit mistaken to believe that the idea that the atomic unit would be a person talking about a place that they're at and you have to have a physical place to tie it to versus a person sharing a moment or an experience that they're having in the world. Sometimes that might have a place connected to it.

Noah Weiss (00:09:47):
I think that one change in framer on what you would say a customer actually wanted to do, that probably was the thing that took this away on the social side. I think on the more local discovery side, it's actually what people wind up be using the product much more for over time getting personalized recommendations and getting tips when you go to a place and all the push notifications.

Noah Weiss (00:10:10):
Again, it was hard to stay ahead, I think specifically of Google, because they had billion plus Google Maps users distributed on Android and iOS. Even though they might only take a couple years, eventually they would wind up replicating a lot of the functionality and then I think it was hard to regain that momentum. Much of this stuff is luck and timing and just coincidences of history.

Noah Weiss (00:10:37):
I think there was a path. I think in the end we lost their social sales and then Google was able to catch up on the utility side. Now the company's built a really valuable B2B API company which offers a story. I mean Slack is in some ways a pivot, obviously, from a consumer company to a B2B company. But that that's my mini postmortem, what could have been with Foursquare.

Lenny (00:11:00):
It's interesting how many consumer companies pivot to B2B because it turns out that's where the money ends up being.

Noah Weiss (00:11:06):
Yeah. I think the feedback to you get from our people willing to pay for the product that you're building is so much faster than can I build a large-scale consumer business and when they hope to have enough reach to then slap ads onto it. That's a much more of a try to hit a home run and hope it works out. But you don't really know if you're doing it along the way. Yeah. I think B2B is a easier to have a more incremental, successfully business than pure consumer.

Lenny (00:11:34):
Okay. Speaking of Foursquare, Dennis Crowley was the CEO and founder, a very strong product-minded founder. I know you've worked with a number of very strong product-minded founders including Stewart Butterfield, Dennis, obviously we just talked about, maybe others. I'm curious what you've learned as a product leader working with very opinionated founders.

Lenny (00:11:56):
I think this is interesting not just as a product leader working with very product-minded CEOs, but also as a first PM at a startup you're often put in this tough spot of just the founders just telling you what to do and you have to go build it versus having a lot of say in agency. I'm curious what you've learned about working and being successful in that position, which is often really hard.

Noah Weiss (00:12:14):
I would say to folks in general, if you're joining company and the CEO does the role that is your functional area of expertise, it's probably the area where you'll learn the most because they're hopefully world class at it. But also, one will you'll be the most frustrated at times because you're going to feel like you have less agency. You should just know that going into it.

Noah Weiss (00:12:33):
If you go to company to run by a former marketer and you're in marketing, they'll probably want to have a lot of say and influence over that. I think just going into knowing that is good. Looking back, I would say probably two main things stand out of what's really worked with both Dennis and Stewart, not just for me but I think for the teams that work with him as well.

Noah Weiss (00:12:52):
The first is, I think as much as possible, I think maybe we'll talk about this a little bit later as well, is getting to the point where you have alignment on the principles for what it means to build a great product of that company. Not just about if the intuition and tasting gut, but how do you distill that to principles that become the language of the company so that everybody else can start thinking through a similar frame or similar lens when you're designing a product.

Noah Weiss (00:13:17):
Because otherwise it can feel a little bit Goldilocks every time a team builds something, they take it to the CEO. CEO is like, "No, not quite right. Again, no, not exactly that." Then you don't have the language to actually have a more constructive review. Then doing that at the little strategy as well. I think the product founder CEO is always going to be the holder of the vision for the company. I'm sure at Airbnb. I imagine Brian was very much like that as well.

Lenny (00:13:40):
Absolutely.

Noah Weiss (00:13:41):
I think it's actually great to say, "Okay. The overall vision for the company, is it the responsibility of any one team to have everyone buy into that vision, but then to have space for teams to be able to actually do creative work, do explorations because you know that it's aligned with that high level vision."

Noah Weiss (00:13:57):
If you can get that alignment and you can get those principles as the common language of what creative software looks like, I think you can have a really good working relationship. Then the other bit I would just say is I think when to involve the founder CEO in a project is really important. The short version I think that works the best is almost like a U-curve where the X-axis is time and the Y-axis is level of involvement.

Noah Weiss (00:14:22):
I think you want to get the founder CEO really involved early on, especially if it's a big new project, to make sure that there's strategic buy-in that you agree on the principle strategy and approaching you agree on the goals and the anti-goals, getting that to then the team can run and explore. Then I think at the very end you want them to really be bought in that did you build something that's up to the quality ... the company?

Noah Weiss (00:14:43):
Is this something that's going to customers, literally taste the soup. What's missing in it? I think at most companies that have a maniacally customer-focused founder, if you don't do that last step, it's going to be much more painful after you launch because they weren't part of that co-creation of the team. I think that formula winds up working pretty well if you throw in that alignment on principles and envision.

Lenny (00:15:08):
That usually sounds nice in theory, but I often imagine you get to that final step and the founder is like, "What the hell is this? This is not at all what I was hoping it be." Is there an example of that, that comes to mind where you maybe went through that and then it's just like, "No. That did not work out the way we expected" and if not, no problem.

Noah Weiss (00:15:26):
Yeah. I mean I think that does happen. The ship is maybe ... the end of the year is the level of engagement and often that last level of engagement, that's where there's actually the most rapid refinement that you're doing. I think what's important there is that hopefully you're refining in code and you're not still at static design mocks because using the software is so different than looking at what the software will visually appear.

Noah Weiss (00:15:51):
I think what we would wind up doing with Stewart at Slack, for example, is we would get the entire development team, engineers design product, user research and Stewart together in a room and we almost do a bug bash together. The idea was like, "We're doing it all together. We're trying to make the best product possible, making great softwares really messy and we're all trying to clean up the mess together."

Noah Weiss (00:16:15):
Sometimes you might find things like, "Okay. This entry point really isn't working, maybe we have to move this entry point. That's maybe a bigger change." But I think often what you'd find is just all those bits of polish and refinement and doing the little delightful things that might otherwise be missing to raise that craft bar and doing a real collective way so it doesn't just feel like the team says. "We want to ship." The founder says, "No, it's not ready."

Noah Weiss (00:16:38):
Ideally as a group you're saying, We want to get it to a bar that's going to delight our users and here's the gap from where we are today to what we want to shift." I think that mentality winds up being a lot more constructive, but that's not always easy to do.

Lenny (00:16:54):
You talked about creating these principles, which is an awesome approach of just creating guardrails for the team so they think the way the founder and the head of product think. What are some examples of principles you have and had early on maybe at Foursquare or Slack?

Noah Weiss (00:17:07):
I mean Slack I think is where we enshrined them much more because we scaled the org so much, more that we needed principles. I think for us, they were really about unpacking just the mission, which for Slack is making people's working lives simpler, more pleasant, more productive. That's the mission of the company. The question is how does software help do that? That's what the principles or their answer.

Noah Weiss (00:17:31):
For us, we've got five, four principles. They've largely stayed the same. Some of the language has changed over the last couple of years. But at least for the last four or five years we've had these. The first is be a great host, which is all about that level of craft, the relentlessly saving people's steps. If you're, let's say, a host at Airbnb, it's like putting clean towels on the bed. No one has to wonder "Are these for me?" That type of foresight.

Lenny (00:17:57):
That's actually a value at Airbnb. Exactly.

Noah Weiss (00:17:59):
Oh, really?

Lenny (00:18:00):
It's actually be a host at Airbnb is one of the four core values.

Noah Weiss (00:18:03):
Right. Maybe we borrowed that or someone was inspired by it. But be a great host. It sounded aspirational. I love that.

Lenny (00:18:09):
Yeah. Yeah. It's a little bigger.

Noah Weiss (00:18:11):
There's a famous user design book called Don't Make Me Think, which we sold the title of for our next principle. That's really just about as people building the software, you know how it works so well. You care about all the nuances and intricacies and you really want your users to love it as much as you do. But often actually, that owner's delusion that someone else will care as much about the software that you built as you do, prevents you from actually making something that's simple, comprehensible, understandable.

Noah Weiss (00:18:43):
One of the core tenets of Slack is pretty complex under the surface, is how do we actually make people not have to think, how do we not reinvent the wheel if there's existing design patterns to use, how do we actually wind up designing for people who come from many different backgrounds and we cater to their needs in ways that don't make them have to customize it too much?

Noah Weiss (00:19:03):
There's a saying we also have, which is more clicks can often be okay. You'll often have in optimization experimentation circles like, "Oh, every click, remove it." But I actually think in a lot of software when it's not transactional, helping people understand what they're doing, giving them confidence, helping them have trust in the steps, we've seen that that can actually be a better experience. That's another example of don't make it stressful, help people chill out when they're using this offer. That's the idea beyond that one.

Lenny (00:19:32):
Shifting a little bit. I know you guys have been working on a bunch of AI stuff at Slack. I believe you've been working on AI related stuff for many years. I think at Google you worked on a lot of AI related products. I feel like a lot of people are just getting into this and trying to figure out, "How do we integrate AI and ML and LLMs into our product and how do we not just waste our time chasing things?"

Lenny (00:19:55):
I want to ask you just in your time working with AI over the many years you've been doing it and share a little bit about what you've been doing there. What are some things you've learned about how to be actually effective and build valuable products and not just fall for the shiny object issue and trap?

Noah Weiss (00:20:11):
I mean, it's almost 15 years ago now that I was working at Google in search on what later became called the knowledge graph. This idea of building a canonical repository of information of people, places, things in the world and relationships between them. Back then, it was a lot of the same ideas, but obviously the techniques. I have got a lot more mature.

Noah Weiss (00:20:33):
We used natural language processing to extract all this information from the web and try to build this database of facts. An idea then was could you take queries, people have like, "What are the tallest fountains in Europe or what of the most popular beaches in Southern California?" Be able to actually give answers not just 10 blue links.

Noah Weiss (00:20:53):
I think the thing that's really changed, it's super exciting in the last 6, 12 months with LMs and chat GPT and everything else is the idea that now you can take not just knowledge about the world but actually have natural language generation where suddenly the computer can talk back to you in a way that feels extremely human. Then the creative applications of that are pretty massive and exciting.

Noah Weiss (00:21:19):
That's, I guess, the lineage there. I think from over the years back at Google at Foursquare, we did a lot of personalization and recommendations at Slack we have search and ML that's coming infused throughout the product. I think a couple things come out as ... I guess the principles that we've used over the years, back then at Google, one of the big ones, was that the promise of the UI has to match the quality of the underlying data, which is to say ... I think this is actually one of the failings of the various LMs right now is they all appear supremely confident even when they're completely hallucinating.

Noah Weiss (00:21:53):
I think that's going to be something that people are going to have to work on a lot, which is to figure out how to be not so faultless, to acknowledge when you're not sure, because otherwise, it undermines the trust people have in the system. Using a lot of transparency about where the data comes from so people can actually build credibility and the tools is really important.

Noah Weiss (00:22:11):
Then I think making sure that as you're designing the products that you have virtuous cycles that are naturally part of the product experience where you can get training data as a byproduct of people naturally using the software and then can make the model that you're building behind the scenes smarter, more accurate, more predictive.

Noah Weiss (00:22:29):
A classic example of that would be Netflix back in the day, their rating system, they actually have a feedback loop from their customers then make the system better at predicting. I think people you are still trying to figure out what does that look like in this world in LLMs?

Lenny (00:22:42):
Something I hope that you're all building at Slack is a way to ask a bot questions based on all the conversations in the Slack. I've been looking for that product for a while now.

Noah Weiss (00:22:51):
I can safely say we have a lot of prototypes internally where we are playing with this. I think it is actually funny as a aside in one of the original Slack, I don't know, product vision decks back in 2014. There was our whole strategy, there's four parts. Then part number four, which was a joke at the time, was then do magic AI stuff on top.

Noah Weiss (00:23:13):
We didn't even know what the state of AI would be. By the time hopefully companies have their collective knowledge in Slack and now we're finally at the period where the magic AI stuff seems finally pretty amazing, pretty magical. Yeah. We're doing a lot of prototyping internally and also trying to work with the ecosystem around as well, because there's so many companies doing amazing work in this space.

Noah Weiss (00:23:33):
That if you work at a company where you have so much knowledge in your Slack channel repository that you can suddenly get amazing leaps in productivity to help you better do your job because that knowledge is in Slack, but it's sometimes hard to reach and I think these technologies can make that possible.

Lenny (00:23:50):
This reminds me of something Gustav, the CPO and CTO and co-president of Spotify share that they always have a deck and a vision of just a play button within Spotify, you just play and all magic happens and it's the best music and thing exactly what you want to hear and just how that isn't actually possible and it's still not possible. Exactly to your point, you have to really think about how does it act? How close is it to the reality? If it's not actually there, he was saying how like, "We'll pick two songs that are correct at a 10 just because we don't really know exactly what you want to hear right now."

Lenny (00:24:23):
There's no point in trying to design that right now because that's not actually going to be delivering on the promise.

Noah Weiss (00:24:27):
Right. Yeah. I love that. Our version of that has always been that you open up Slack and suddenly instead of having to read through dozens of channels or find these mentions that magically Slack could just tell you in order that you would care about a summary of all the interesting things that have happened and then let you dig in if you want to your very own personal chief of staff who knew everything that you cared about and read everything that you could read.

Noah Weiss (00:24:52):
I don't think that's going to quite be possible anytime soon. But I think Spotify heading towards that north star you wind up developing. I hope a lot of really compelling projects experiences along the way.

Lenny (00:25:02):
Yeah, man. The more I think about it, the more amazing opportunities exist in Slack. It's all text. It's amazing. Okay. There's a lot of cool stuff coming I imagine.

Noah Weiss (00:25:10):
Yes.

Lenny (00:25:10):
I can't wait.

Noah Weiss (00:25:11):
Yes.

Lenny (00:25:12):
On that topic, how do you think about creating teams within Slack and AI specifically? Are you recommending each team think about how AI can make their stuff better or are you dedicating, "Here's the AI team and they're going to work on stuff" and you guys just keep ship what you're shipping and keep moving your metrics?

Noah Weiss (00:25:29):
I mean the unfair answer is a hybrid of the two, which is to say we have a central machine learning and search team. But a lot of people have expertise in this field to build infrastructure that everybody can use. What we've done is because the space is evolving so quickly, literally every month, the capabilities are evolving, the risks and tradeoffs are evolving a ton.

Noah Weiss (00:25:52):
What we want to do is actually spin up a couple different teams that are focused on prototyping, using that common infrastructure but in specific directions that are all a little bit different. We've got a common ML, let's say in search team and now we have a bunch of teams that are working in parallel and different customer problems that we're trying to solve using that shared infrastructure.

Noah Weiss (00:26:17):
I think this isn't the steady state. I think over time, what it'll probably look like is that all the existing product areas, as soon as we know more of the shape of what the technology is capable of will just have AI capabilities as part of their roadmaps. Just like every product team is responsible for their own mobile roadmap. They don't outsource it to someone else.

Noah Weiss (00:26:37):
But I think today when things are moving so quickly, you actually want a little bit of a more ad hoc, flexible approach to move quickly and that's what we're doing.

Lenny (00:26:49):
That's what I've been hearing from everyone I've been asking this question. The search ranking team is always seems to be the center of all this and then it's a few experiments here and there. That's an interesting pattern I've been noticing.

Noah Weiss (00:26:58):
Good to know.

Lenny (00:27:00):
I heard that you have a process internally called Complaint-Storms. I'd love to understand what that is.

Noah Weiss (00:27:05):
It something that started. I want to say back in end of 2019, maybe early 2020. The idea a little bit was how do we help as a team look at the software that we build with fresh eyes, because we've been set at Slack for a long time. Slack maybe more than almost any other company maybe like Figma is probably similar. I was listening to the podcast just earlier today where if you work on Figma, you work on Slack.

Noah Weiss (00:27:30):
You also live in Slack and you live in Figma all day so you can become more of a power user than anyone else on earth. What we were realizing, especially for people trying to build Slack for the next million customers, the people who have never used Slack before, it was becoming increasingly hard to have empathy for what their usage of Slack would look like. How would they look at it in a more critical way? How would they care less than we cared?

Noah Weiss (00:27:56):
What we started doing with these complaints storms and idea was really simple, which is we'd get a team together often Stewart myself would also join and we'd actually start off with other products first in adjacent spaces and we'd say, "Okay. As a group we're going to go through the customer journey from the moment you land on the website through, let's say it's a workplace product, getting your first account going, getting the first couple of users on board, getting to the point of value.

Noah Weiss (00:28:21):
We're going to do it on one screen. Someone's going to project and then people are going to fill in every issue, everything that's confusing, every pain point, not bones, but ways in which if you didn't care about the software, you don't work on it, what would actually confuse you? What would stop you in your tracks?

Noah Weiss (00:28:38):
From that you went generating a bunch of amazing inspiration by looking at someone else's product in a really critical way for things you might want to try in your own product. Once you get to that, then it becomes easier to actually do with your own software, but it is a little painful obviously. Same with watching usability tests to look at your own baby in a way that is, "Okay. I'm trying to find all the words. I'm trying to find all the problems."

Noah Weiss (00:29:03):
But that's one up being a pretty great source. Whenever a team I think either gets stuck or feels like they reach a dead end in a direction is doing complaint-storms about the product area that they're in or using adjacent products just to get inspiration. Then I think it unlocks a lot more creative views than the problem space.

Lenny (00:29:23):
It's similar to a process that I learned Stripe has called friction logging. But I love the nuance here of starting with someone else's product because I could totally see how that makes you feel better looking at your product in real life. It's not like we suck. It's okay, everyone's has so much opportunity.

Noah Weiss (00:29:38):
Exactly. Yeah. I've heard that from Stripe, too. I think gets a similar place. I think it's the doing it ... I think the byproduct is that you also get calibration on product pace, product quality, and as a team you develop that together. Again, similar to the principles, it's like how do you get these things that are hard to actually feel collectively on the same page about and how do you calibrate? It's another good way to do it.

Lenny (00:30:01):
I'm imagining some PMs might be hearing this and wonder, "Okay. Great. Now the founders and the execs have all these things that they want us to fix. I have goals to hit. I got a roadmap. How do you think about prioritizing things that come up in these sorts of sessions for the team and how do they mix and match versus all the other stuff that you want to do? Or is it just like they don't actually have a huge roadmap and this is a way to inform the roadmap?

Noah Weiss (00:30:23):
No. I mean, more broadly, I think the way that we think about, or us to think about our roadmap for any feature team at Slack is that it's a portfolio and it's meant to be a portfolio that's diversified a couple different ways. I think one is you want to diversify things that are meant to be new capabilities versus making the thing you've already built a little bit better every day. Similar to parenting.

Noah Weiss (00:30:47):
Are there things that are meant to be risky that you aren't sure are going to work but might have a lot of upside versus things that are known bets. Then I think often you're balancing are you doing things that are meant to have impact that you're already very confident in versus things that are meant to learn about a new possibility space.

Noah Weiss (00:31:05):
I think for most teams, this stuff usually wind up tactically filling up that bucket of, "Let's make the existing product a little bit better every day for users." At Slack we have this thing we call customer Love Sprints, which is an interesting way team to figure out how to get this on their roadmap is it's hard to allocate that work throughout the quarter.

Noah Weiss (00:31:26):
What we'll wind up doing often is have a team do a two-week customer love sprint, almost like a hackathon, but with that burndown list of what we think is the lowest effort, highest impact changes that we can make to generate more love from our customers and whatever that feature areas. Then people just sprint for two weeks, design product engineering, and then you have a bunch of things that you celebrate.

Noah Weiss (00:31:48):
At the end, the goal is to ship all of them. This isn't hacks that you throw away. That's how we end up prioritizing it off in that work is actually making it this really fun total change of pace throughout the quarter to not do big feature work that may take months, but to do all these small delightful things that customers are going to love at the end. That's the other way that we figure out how to balance it in.

Lenny (00:32:11):
I love that. How often do you do these sorts of customer Love Sprints?

Noah Weiss (00:32:14):
I would think teams that work on very user facing products do it at least once a quarter. I think other teams that work on maybe less user facing might do it maybe twice a year. But quarterly is a pretty healthy cadence.

Lenny (00:32:26):
Wow. I didn't know about that. That connects to ... Slack has always been a very delightful product. I remember early on the animations were so awesome, the little twirly, I don't know, pounds hashtag thing. It feels like Slack has always invested in delight. How do you operationalize that? Is it these customer Love Sprints? Is there something else that's just like we need to allocate some percentage, just make things really fun even though it's not going to move any metric?

Noah Weiss (00:32:51):
I would say it's a little bit good DNA of the company, honestly, which is that for co-founders trying to build a massive online role playing game for many years that was called Glitch and their background was all in building delightful, playful experiences. Glitch didn't work out. But, yeah, there's a whole long backstory. But the short version is a tool they had built internally that they then wound up spitting out a company from which became Slack.

Noah Weiss (00:33:18):
I think that DNA we're trying to build a consumer grade experience that just happens to be for work is really ingrained in the company. It's also a big part of how we hire. I would say certainly the majority of PMs designers and engineers who joined Slack had never worked at an enterprise software company before. It's not like most people had worked at Oracle or SAP, it's most people had worked at consumer companies or game companies.

Noah Weiss (00:33:44):
They bring that focus in the spirit and then I would say the last bit beyond kind of the principles and the complaints-storms and the customer love is that we have this amazing team that we call the CET team, the Customer Experience Team. They're in some ways the team that is doing our scale at Foursquare is most often in touch with our customers.

Noah Weiss (00:34:02):
From the very early days people used to do CE shifts if you worked in products so that you can actually figure out what's frustrating, what's confusing. We have a really great pipeline for getting the insights from the CE team of what are the obstacles, the pain points, the most frequent complaints into the hands of the product teams to be able to prioritize, to figure out, yeah, not all these are going to move a given metric. They might not achieve something for the business.

Noah Weiss (00:34:28):
But collectively, I think the way that Slack thinks about competition is we obsess it about customers. We build something they'll love enough to tell their coworkers and the rest takes care of itself.

Lenny (00:34:41):
Speaking of competition, something I wanted to ask you a bit about. Early on Slack was competing against this product called HipChat and that's actually what I used at our startup and we love HipChat. It was so hilarious, just these memes everywhere and their billboards are amazing. But then Slack ate their lunch later on. I'm just thinking out loud, discord feels like that was the big threat and how Microsoft Teams obviously.

Lenny (00:35:03):
I'm curious just how you think about competition and even just what you've learned about working in a space where there's a lot of competition and thinking about that long-term and even short-term.

Noah Weiss (00:35:12):
Yeah. I mean each of those is an interesting mini lesson learned about those. I think the through line for all of them I would say is still the max that we have in trailing, which is we're customer obsessed but competitor aware. I think it's a little bit different. I think some companies are like ... I don't know, Uber for example, I think was notorious competitor obsessed and they tried to delete customers when they could.

Noah Weiss (00:35:35):
I think HipChat. I don't think Slack sought out to kill HipChat. At Foursquare we used ... I think it was called Campfire back in the day for the 37 singles people. It was a whole generation of those products. I think Slack came along and I think they had a couple of innovations. One was they had a great mobile experience that synced across every client. Search actually worked and then they brought a lot of the best parts of consumer messaging into the workplace like the emoji and reactions and all those bits.

Noah Weiss (00:36:04):
I think it turns out that if you're 10X better on a couple of those axes, then you can see a huge change in behavior. I think that's what happened with that move from the HipChat Campfire to Slack world. Discords interesting. I mean we keep aware of Discord. But it is so much more focused on the consumer. Originally, it was [inaudible 00:36:23] out for community space. I think at Slack the lesson I would have, I think we learned in a good way is we've always really been focused on groups of people who are trying to do work together.

Noah Weiss (00:36:33):
That winds up being a completely different audience to build for than communities. I think that focus has been really helpful and I think Discord's amazing and many people love it and the people who use Discord certainly use it in very different way than people who use Slack at work.

Noah Weiss (00:36:49):
I think Microsoft obviously has become over time the biggest competitor there. I think the origin of Teams really was a defensive move for them to protect Office because Office is an incredible, very profitable monopoly in the productivity space. I think when they built Teams it was more of a covering their flank versus Slack on the ascent.

Noah Weiss (00:37:10):
I think as Teams has evolved over time, it's become much more of a video conferencing product that competes with Zoom and Google Meet. The people who use Teams use it completely different than Slack where you live and breathe and channels and work and workflows all day long.

Noah Weiss (00:37:25):
I think what we've seen there too is that a lot of our customers, they happily use both. Most Fortune 500 companies have either a subscription or a Google Workplace subscription and all of those customers who use those also use Slack. We like to say that Slack is this connected tissue that makes all the rest of your tools that much better.

Noah Weiss (00:37:44):
I think there we've taken very much an open ecosystem and platform approach and we've just been focused on how do we keep building the best version of what Slack can be as a new category of software for our customers and staying aware of our competitors, but really obsessed on what are the new ways that we can delight our users as the years go by.

Lenny (00:38:04):
Slack is a big-ish company within now let's say a big company. But it feels like you still are launching really interesting stuff, you launch huddles, clips, there's this AI stuff coming, sounds like. I'm curious what you have done at Slack to enable these sorts of zero to one bets and what you've seen is important to allow for innovation along those lines.

Noah Weiss (00:38:26):
I think maybe we're all a little self-delusional, because I think everyone who works at Slack likes to think that we're still at a small startup. I think keeping that spirit alive, honestly culturally has been a big part of it. I think going back to the principles early on, one of the ones that we did talk about, literally one of the actual wording is take bigger boulder bets.

Noah Weiss (00:38:43):
The idea there is that it's really easy to fall into the trap of just constant incrementalism. The concept, it's like a feature team and you have like a KPI and you feel like your whole life is measured by that similar KPI going up 1% a quarter and then you lose sight of what's beyond the horizon. We have this mental metaphor that we talk a lot about getting to the next hill.

Noah Weiss (00:39:07):
The idea is that if you're in a mountain range and you're maybe in the little valley, you can see what's right in front of you. But you have no idea how tall the mountains are behind. I think teams can often get lost crawling up that hill, not realizing that there's a huge, incredibly beautiful range behind it.

Noah Weiss (00:39:26):
Take bigger boulder bets. Get to the next hill to see what the horizon wants around you. That's how we think about it strategically. Then I think structurally the way we've approached it is that we've over time freighted new teams from scratch that incubated in a new area before the area mature. We did that with a lot of these native audiovisual products like huddles and clips really in the pandemic because our customers were demanding it from us.

Noah Weiss (00:39:49):
They were like, "We love living in Slack all day. But we feel disconnected from our teammates when we can't be in the same physical place. What can you do to help us?" That's where that came from. I think in the AI space now, it's a similar thing, which is what we're trying to hear from customers. What do you wish Slack could do if it had these new superpowers? Let's incubate a couple teams, a prototype there and then figure out what can get to real product market fit.

Noah Weiss (00:40:14):
I think when we have those teams, I think it's important to just give them space to run, to give them ... get a gel free card for maybe the normal process of, "Okay. Our planning quarterly reviews" and make it feel something that is the pace of learning is what matters. How fast are you prototyping, how fast are you learning from users and then getting to do that publicly and pilot and then get something to launch that's amazing, blows people away. That's the formula that we've seen.

Lenny (00:40:43):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate your growth. Thousands of fast-growing companies like Gusto, Com, Quora, and Modern Treasury trust Vanta to help build, scale, manage, and demonstrate their security and compliance programs and get ready for audits in weeks, not months.

Lenny (00:41:01):
By offering the most in-demand security and privacy frameworks such as SOC 2, ISO 27,001, GDPR, HIPAA, and many more, Vanta helps companies obtain the reports they need to accelerate growth, build efficient compliance processes, mitigate risks to their businesses, and build trust with external stakeholders. Over 5,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2 and these other frameworks. For a limited time, Lenny's podcast listeners get $1,000 off Vanta. Go to vanta.com/lenny, that's V-A-N-T-A .com/lenny to learn more and to claim your discounts. Get started today.

Lenny (00:41:39):
One of the things I love learning about from product teams is their unique rituals and traditions. I'm curious what's maybe the most interesting or unique or fun or funny ritual or tradition on the product team of things you all maybe do regularly?

Noah Weiss (00:41:56):
One of the things that we do, which is always a little bit funny, I mean, it's more of a emotional thing rather than a practical thing is that at all hands we'll often wind up taking specific tweets that people had about the product and Twitter. People say the craziest thing sometimes. Sometimes they're really heartwarming like customer love, but often it's just the meanest, most frustrating complaints that people have.

Noah Weiss (00:42:21):
It's honestly meant for us to just have a pulse on, we're at people actually saying and feeling in the wild and not thinking too seriously, but keeping that sense of ... I think that the distance you have from your users as your user base gets more and more diverse and larger I think can make it harder to actually develop the product because you're not designing for yourself anymore.

Noah Weiss (00:42:41):
I think all the ways that we help keep people grounded in what are actual users actually saying. That's one big way. The other that reminded me of which is actually probably better, maybe delete that last one because it's kind of boring.

Lenny (00:42:55):
No. It's great. We're not deleting nothing.

Noah Weiss (00:42:57):
Fine. Usability. I'm a big believer in you want to be data-informed, but you don't want to be so data-driven that you actually don't have a pulse of what real people feel when they're using your product. We're really big into user research, not as it gives you the answer, but it helps at least pose a lot of questions for you when you watch how someone actually uses the software.

Noah Weiss (00:43:21):
Historically, it's really hard to get PMs, let alone engineers actually attend user research sessions. What we wound up doing, especially in the pandemic when we first went remote, is now you can dial into usability sessions and to make it really attractive for the team, what we would do is have people live in a thread, write their real time thoughts of ... so painful, how they use that, or I can't believe they missed that, or, oh, that gave me this idea from seeing how they were doing that to do this other thing.

Noah Weiss (00:43:50):
Then you wind up having the PMs, the engineers, designers and the user researcher all in one Slack thread live, responding, reacting to usability session. Then suddenly that thread becomes actually the best source of truth for the research report that then gets written up.

Noah Weiss (00:44:06):
But I think most importantly, it gets the team almost like the complaint-storms, but actually watching someone else do it in the shoes of an actual human being trying to use the thing that you thought was so brilliant and yet has all these flaws. It's humbling. It's filled with humor and also it's I think really constructive for the teams to do it that way.

Lenny (00:44:27):
I was going to ask where they actually share these thoughts. In Slack makes a lot of sense.

Noah Weiss (00:44:31):
Yeah. I mean it turns into a report at some point, but literally just link back to the original thread and then you have 100 people's reaction as the report is ongoing.

Lenny (00:44:41):
If only there was a AI tool to summarize all of your thoughts.

Noah Weiss (00:44:45):
We've got a prototype for that. Hopefully it'll work well enough that actually be useful for customers, too.

Lenny (00:44:51):
You tweeted once about how ... I think maybe around the time you joined Slack around 2019 that the self-service business of Slack basically plateaued and it wasn't clear why. I'm curious just what that period was like and how did you get to the bottom of what was going on and turn things around.

Noah Weiss (00:45:09):
Yeah. It was actually a couple years after I joined, but it was a point where I was focused on the self-service business because we had this period with Slack where I would say maybe 2014 to 2017 where it was almost all self-service and it was just growing like gangbusters. Then we started spinning up the sales team and an enterprise team. We started focusing mostly on that.

Noah Weiss (00:45:30):
I think we saw the team that was working on, but it was primarily the company's focus was all driving enterprise deals, getting to that next level of maturity. Then in 2019, I think we started to see that when we looked beneath the surface, the fundamentals of the self-service business weren't looking as healthy as they used to be.

Noah Weiss (00:45:50):
I think the biggest thing as we dug into it was a little bit to what we were talking about earlier with the motivation and complaints terms is it was getting harder to understand what the next generation of Slack customers really wanted from the product. Whether you're thinking about this as crossing the chasm or moving from kind of early adopters to the needs, the more majority or later adopters, I think we're at that point where not every technologically sophisticated company on earth was using Slack, but most were, and we were getting into a market that customers just had different needs. They had different levels of sophistication.

Noah Weiss (00:46:24):
We did a lot of user research. We looked at all these cohort curves, which you can imagine suddenly they're like, "Huh, they're not as healthy as they used to be like. What's going on?" I think we got a bunch of insights from it. But I think really what we want to change about how we were operating was instead of to continue to try to optimize the things that had worked over the last couple years, we said, "Okay. Let's throw the whole roadmap away and instead let's come up with a bunch of hypotheses about what could be new levers that could actually help based on the insights that we now have about the next set of customers."

Noah Weiss (00:46:56):
"We're going to try to quickly learn which of these levers are real and which of these are just totally off the mark." We had to say for the next six months, we're probably not going to drive any impact at all. It's only going to be about learning. But at the end of that, hopefully we wind up finding a couple different levers that had years of room run and that's what wound up happening.

Noah Weiss (00:47:19):
We wound up doubling the rate of our new pay customer growth in the year and a couple years after that and accelerating the self-service business. I think it really came from stepping back, being humble, not feeling like we deserve to have every company on earth sign up and then figuring out how to optimize for learning. In the long term you could get the impact.

Noah Weiss (00:47:39):
But knowing that for the next couple quarters we're going to sacrifice impact for the sake of learning. I think that was a good muscle to build, but it was definitely not easy to do at the time.

Lenny (00:47:49):
Well, the story begs the question, what are the levers that worked? Whatever you can share.

Noah Weiss (00:47:53):
One of the big things that we wound up focusing on is what we talk about is comprehension, desirability. The fundamental challenge I think for new users or new teams using your product once you get past the kind of tech early adopters is do they comprehend what this thing is for? Do they understand how it works? Then desirability is why should they care? Most people at work are not like," Hey. You know what I want to do today is start using an entirely new tool and convince all my coworkers to get on board.

Noah Weiss (00:48:22):
That is not part of your job. Your job has goals and measurements and everything else. Really ... understanding that. How do you push on that in that new user experience? It sounds maybe a little ludicrous, but Slack always has a free product. Obviously, there's a free tier that you can use, but we had never actually figured out a trial strategy where we actually gave you a taste of the paid product.

Noah Weiss (00:48:44):
Either we're on the free tier or we get to pay for the paid tier. And that wound up being one of, I think the Ripest veins is figuring out how to give people a taste of the full premium Slack experience so that they would never want to go back and doing that in a variety of different points in the customer journey. Then I'd say the other biggest thing I would call the one out is we really need to figure out a new north star metric for motivating the teams across Slack.

Noah Weiss (00:49:09):
At that point in time, we basically had paid customers and then we had creative teams, which is the very, very beginning, very, very end of the journey. We did a lot of quantitative research and data science and wound up coming up with this new metric we call successful teams, which is a little bit ... I feel a lot of companies have this Facebook, I'm lucky number seven or whatever it was.

Noah Weiss (00:49:28):
Where what we found was that if you could get five people using Slack, the majority of the work week to just communicate at all, that would be a successful team there were going to be 400% more likely to upgrade over the next six months. That seems like a very low bar, five people to use Slack throughout the work week, not even every day. But it turns out that if you could get that level of critical mass the rest would take care of itself.

Noah Weiss (00:49:54):
We wound up motivating not just the team that was focused on self-service but all these other feature teams across the company to drive more new successful teams, knowing that if we can move that which is much earlier in the funnel but not a top of funnel metric, then it would actually drive upgrades and paid customers and thus revenue long-term. That was a huge turning point for how we rally product teams around somebody to actually drive that self-service business.

Lenny (00:50:22):
Man, this feels like its own podcast. Just to analyze the things you learned down this journey, and there's so many takeaways here. One is just the importance of an activation metric that is predictive of retention sales. It sounds like you landed on five people in a company like DAU basically for a week, something like that. That's awesome.

Lenny (00:50:40):
Then the other interesting takeaway here is I'm actually doing a bunch of interviews with founders of the most successful B2B companies and interestingly, not all, maybe half are like, "I still don't think we have product market fit. They're at a billion dollars valuation growing crazy." They're like, I feel like I have product market fit with the current users but I don't with the people I want next.

Noah Weiss (00:51:08):
That's exactly right. I think that's exactly right. I think of product market fit is almost like you keep stacking these S-curves where you get product market fit in a small group and then you suddenly reach exponential growth because you can crack that coal group, that type of audience, but then you start declining because you start hitting the ceiling of, we've got in, I don't know what it might be every development team in the US to be using this product.

Noah Weiss (00:51:30):
Then you jump up to the next S-curve, which is like how do we get technology savvy teams that aren't developers or how do we get people who are in large eventerprises who are outside the US. Each become new curves that you have to build product market fit for. I think it's just all a huge exercise in being self-critical, being humble, not presuming that you've cracked this thing forever and keeping kind of a very beginner's mindset of what does the next audience need. "

Noah Weiss (00:51:58):
Your previous audience. Didn't need it all.

Lenny (00:52:01):
If you think about the pie chart of what you had to change to make it work, how much of it was it messaging, positioning, onboarding, optimization versus product features?

Noah Weiss (00:52:10):
I would say maybe 60-40 in the sense of the early journey. I mean not just obviously positioning messaging, but the entire experience of unboxing Slack if you will with your team. We called it the day one journey, but extended to really kind of day 30 in reality and it's a single player and multiplayer experience. It is really complex.

Noah Weiss (00:52:33):
But then I think what we realized was you can make that incredible, but if fundamental parts of the product were missing that would make it comprehensible to the next audience, then you're going to have problems. It sounds maybe impossible to remember, but Slack used to not have wizzywig message composition.

Noah Weiss (00:52:53):
You used to have to use mar, down. Making that wizzywig was a huge boost making mobile work offline so it worked no matter where you were in the world was another big one. All the things about configuring your sidebar notification so that as you scale it you should just Slack it and become overwhelming. Those are some of the foundational product investments that we wound up making so that next generation of Slack customers could get value and not be overwhelmed or daunted by it.

Lenny (00:53:22):
Maybe one last question along these lines, people look at Slack as maybe the first major product-led growth success story and they always look at Slack of like, "Oh, we just want to grow Slack. Let's see what they did." For people that are studying Slack's journey and success, what do you think Slack did right early on that maybe people don't recognize or don't appreciate enough that founders today should be thinking about more so versus just like let's just make a freemium product.

Noah Weiss (00:53:48):
Right. I mean, I think, maybe the most telling thing is when Slack started, certainly when I joined still, I don't think a word or acronym product-led growth existed. It wasn't like we were really good at taking this playbook and applying it. I think it was more that whole term of art became a thing as maybe many other freemium SaaS products took off.

Noah Weiss (00:54:13):
Not to be repetitive. But I think the core of it really was building a product that customers loved enough that they would put their own social capital on the line to get their coworkers on board 5 to 50 people." At the time the biggest company I imagined using Slack was 50 people because I don't know how this is going to work beyond that, maybe it'll become pandemonium. Obviously, that was the initial, I think real, real strong product market fit.

Noah Weiss (00:55:11):
But the other bit which then was what powered the enterprise business was teams of 5 to 50 people who worked at larger companies. I think what wound up happening was that you would have teams that was independently at a company like IBM or Disney or Capital One or whoever it might be, or Comcast discovering Slack using it for themselves because they thought it would just make their working lives simpler, more pleasant, more productive, and maybe not even know that anyone else at the company was using Slack.

Noah Weiss (00:55:39):
Then by the time we then scaled our enterprise sales team, I mean, truly the exercise initially was just take customer domain, sort by number of active users and call them in the order of that which is, "Hey, by the way, you have a couple thousand people actually using Slack at your company. Do you want to think about a broader deployment or controls or analytics?"

Noah Weiss (00:55:59):
I think that was it. That's consumer great experience that customers love enough to get their coworkers on and pay for themselves. Then at enterprise companies like having a bunch of different flowers sprouting so that eventually you could roll up an enterprise-wide deal and then was all the tactics. But I think that that was where it started.

Lenny (00:56:20):
The way you described it at the beginning of make a product that people want to share with their colleagues reminds me of a ... I was just listening to an interview with Seth Godin who's this marketing legend. I think he has a new book. He is on every podcast. He had this really great quote that the products that win are ones that you want to tell your friends about.

Lenny (00:56:37):
It's a really simple concept. Basically, it's like it's word of mouth is how you have to win. But I think that's so true and every successful company I talk to ends up being like, "We just want to build something people want to share with their friends," even if it's growing in some other way, SEO paid feels like that's always at the root of it is you just want to tell your friends about it because you love it. Slack I think is a great example of that.

Noah Weiss (00:56:58):
I think that's true. I mean obviously, there are categories of enterprise software that isn't true for in security or ...

Lenny (00:57:05):
But even that I think if it's an awesome security product you're like, "Hey, you got to check out this century or whatever or sneak."

Noah Weiss (00:57:13):
Yeah. Good friends with Vanta's CEO Christina. I feel like they run those stories where whoever would've thought that a compliance company would be something that people raved about to their other startup friends, like, "Oh, my God. You don't want to deal with SOC's compliance? You got in Vanta. It's amazing."

Noah Weiss (00:57:29):
Yeah. Maybe that is true. I think especially in this day and age where all the marketing acquisition channels have been so saturated, people optimizing so much, I think it's really hard to scale a big enough business if you don't have some amount of word of mouth and customer love driven growth. I think it's hard to scale it on like, "We're going to just play the cat game and in hopes that the numbers work out."

Lenny (00:57:51):
I remember Slack rolling out at Airbnb and all the designers getting so excited about it, creating their channels and everyone's just like, "What the hell are they doing as this thing?" Then it did exactly what you're describing just spread. Everyone's just like, "Whoa, this is cool." They're all telling each other that how useful it is to them and spread like crazy.

Noah Weiss (00:58:07):
I love that.

Lenny (00:58:09):
Is there anything else on Slack that you think would be interesting to share in terms of what makes it a successful product team, product business before I move on to another topic?

Noah Weiss (00:58:20):
The other thing I think is maybe a little bit interesting in terms of how we develop product and it's really different and it's changed over time, which is that obviously the easiest person to build for is yourself and the next easiest is people who look almost exactly like you or have similar preferences and sophistication. I think in the early days of Slack, that's basically what we did.

Noah Weiss (00:58:41):
I mean it was really just trying to build for small technologically savvy teams in terms of you could build a pretty big business making a great product for them. Over the years, obviously, that's changed. One of the things I think that we've done, which has worked really well, one obviously is we've figured out how to do experimentation in a SaaS product, which is not always obvious because the metrics are much longer term than you land at a checkout page and then you hit Checkout.

Noah Weiss (00:59:07):
But I think the other thing is we figured out how to scale up getting real customers using Slack in the wilds for new functionality. We have this really robust program that we call our pilot program where we have, I don't know, probably thousands of different customers that have all signed different agreements now where we can actually roll out to progressively larger user bases, because Slack is a multiplayer product.

Noah Weiss (00:59:30):
You often have to roll out real net new functionality to a whole company or whole team because otherwise you can't use huddles by yourself, for example. Then we have a really great program for actually getting feedback from those customers both through Slack connect itself through surveys and this winds up being a lifeblood of feature teams where you can, by the time you actually launch a big net new feature for Slack, have done so much customer feedback from people actually using in the wild to get work done and so much more confidence in what you're building from the metrics and the surveys that we do that you know can't guarantee it's going to be a hit.

Noah Weiss (01:00:05):
But you can be really confident not because it just worked well internally, which is no longer that predictive, but because it worked well for a thousand different companies, in 50 different countries, in 20 different industries. I think not early on SaaS companies don't need to figure that out, but I think as you grow and as you have a more diverse customer base as you said all these SaaS founders who said, "Hey, you got to keep reestablishing product market fit."

Noah Weiss (01:00:31):
I think that is a programmatic way of being able to do that with your product development process. That's pretty interesting.

Lenny (01:00:37):
Any tips for how to choose who to include in this group if someone wants to build something like this for themselves?

Noah Weiss (01:00:43):
I think the two most important things are you want a lot of diversity in terms of industry, company size, location and so on. I think you want to pick people who are actually motivated to want to be part of the development process and have a slightly higher risk tolerance. Not every company wants to actually be beta testing new functionality that might get removed.

Noah Weiss (01:01:05):
Making sure we have this champion network that we built that people who love Slack enough that they're willing to put up with a little bit of pain in that rougher period are willing to have something that they try to use and then we decide actually we're going to kill that feature before we ever ship it to everybody. Diversity and pain tolerance.

Lenny (01:01:24):
This reminds me of something else, the CTO Stripe shared of how they build new product, which is they pick a couple customers that need a problem solved and they just build it for them essentially and with them and in B2B. Generally, it's a lot easier to build something people really want because they are very motivated for you to solve their problem and they're going to put in the time. You don't need a thousands of people involved, you just need a couple.

Noah Weiss (01:01:46):
Yeah. I definitely think it was one of those things where if you can do it away and they say I can't live without it, the classic not ... Do you like it? Sure. But can you work without this thing? If the answer is definitely not, you've built something that probably a lot of other companies will want to.

Lenny (01:02:04):
All right. I'm going to shift to a totally different topic, which could also be its own whole podcast, but let's just see how it goes. You're with this, I'd say famous blog post on product management called The 10 Traits of Great Product Managers. I want to just try to go through this list briefly and just see how it goes. This could be an hour of conversation. But let's just run through it, because I think it'd be useful for people to hear and I think these are all 100% true even though you wrote this number of years ago at this point and let's just see what comes up. Then I have a few follow-up questions on this list.

Noah Weiss (01:02:34):
These traits are ... I wrote this other thing, which is the five minutes about product management, which are all the things that people think product management is and why they switch to the job and they're disappointed by. Then I was like, "Let me actually write a positive version of this," which is the things that the job actually is about. It's not a career ladder. It's not the, "Here's the structured interview things that you should interview for."

Noah Weiss (01:02:56):
But I think it's the actual job of product management, what is it about, what does success look like? I don't think they're really in a particular order in hindsight, but I'll read them in order. Living the future and work backwards I think is very much the idea of as a PM is one thing they're responsible for. It's having a longer-term vision and time horizon. How do you carve out time to not just be what are we doing over the next two weeks.

Noah Weiss (01:03:20):
But six months, a year, two years from now, how do you immerse yourself in them and bring ideas back, bring inspiration back to the team.

Lenny (01:03:27):
I'm going to just going to throw comments at as you're going through them, just add to them. I love that this is exactly Amazon's approach of work backwards, working backwards process. At Airbnb, this is actually the main thing Brian want pushed everyone to do is just think about the idealized product of a magical world where this is totally solid and then work backwards from that. Then Paul Graham talks about this, too, just live in the future and build it.

Noah Weiss (01:03:53):
I definitely riffed off at least the Paul Graham thing because I remember reading that essay of he thinks everyone thinks that you can get ideas by, I don't know, sitting with their co-founder laying in Dolores Park looking up at the sky and conjuring up the next unicorn or something. Definitely not how that works. You have to actually immerse yourself in the problem space and try to imagine what the future world looks like and then what's missing for people to get to that future state. Yeah. I agree.

Lenny (01:04:20):
I also saw a great tweet by [inaudible 01:04:21] the other day about how if you're working at a company with good leaders, they're never going to be sad that your vision is too big and too ambitious. If there's some reality to it that often they want that just like, "Let's go. Let's think bigger. How do we change the way we think about the future of all this stuff?"

Noah Weiss (01:04:39):
Yeah. I mean that was when I was at Google, the thing I took away most from any review with Larry and Sergei was they would ask how could we get 100X the scale or how could this work for this, would seem like an outlandish use case but would push the team to think much further into the future. Yeah. I think definitely what the founders always want.

Lenny (01:04:56):
That's what Brian Chesky always said too, just like, "How do we 10X this? What would it take to 10X this idea?

Noah Weiss (01:05:01):
Yeah.

Lenny (01:05:01):
Awesome. Okay.

Noah Weiss (01:05:02):
Okay. The second one, which is maybe obvious, but thinking about how do you actually amplify your team? How do you facilitate ideas? How do you create energy? How do you create momentum? A PM role I think can be a little bit unsatisfying if you're useful, where you create things yourself opposed to you are the one who's amplifying what the work that's being created by everyone else is. You have to get into that more of a facilitator mindset.

Lenny (01:05:26):
What I think about here is a lot of teams don't want PMs on their team or don't like PMs or don't think PMs are valuable. What I find is that just means your PMs not good because if you have a good PM, they're just going to help you do the best work of your life. They're going to help you clarify things, prioritize well, unblock you, all that stuff.

Noah Weiss (01:05:45):
Totally. I wish should find out who wrote that expression early on of PM should be mini-CEOs. I think that's the most dangerous piece of advice ever in the history of product management because I think that is how you end up having PMs who try to act like dictators instead of leaders and facilitators. Because if you're acting like that, yeah, your team can completely reject you and say I never want another PM again.

Lenny (01:06:09):
Yeah. So many UPMs are just like, "I'm finally going to have the power, finally." If they move from engineering or some other role and then they get there like, "Oh, what the hell? Is that to convince everyone of all these things I want to do?"

Noah Weiss (01:06:20):
That actually, I'm going to skip in a slightly different direction of the order of this post. But the fifth one that I wrote in there was your job as to facilitate the pace and quality of decision making. That is very different than you are the person who makes all the decisions. In fact, I think one of the things that PM struggled with early on is how do you actually get the team to be able to make high quality decisions quickly without you arbitrarily playing tiebreaker all the time.

Noah Weiss (01:06:48):
It's a soft art to be able to do that. But I think that is actually how you have a really healthy team dynamic instead of PM to want to say, "Okay. Now it's my turn to get to make the decisions." It's definitely not what the job is about.

Lenny (01:07:01):
What that makes me think about is I taught a course on product management at one point that I paused for now of just the core job of a PM is to figure out what's next for every single person on the team. There's this meme or GIF of a dog on a train and he's just laying the tracks as the team is moving forward ahead of them just one step at a time. To do that, this is such an important part of that is just help people make decisions, unblock them.

Noah Weiss (01:07:24):
Totally. I'll combine two of these together. One is you do have to have impeccable execution. This is more of a baseline thing. But I've never seen a PM who was disorganized or didn't do follow-up or wasn't clear about expectations or timelines. It's not high in Maslow's hierarchy of PM enjoyment. But I do think it's a baseline expectation.

Noah Weiss (01:07:47):
The thing I think is more enjoyable and probably the most important thing in the long-term is focusing on impact primarily to the customer experience but also to the business. I think there's that saying growth solves all problems. I think impact solves all PM issues, which is if a team is consistently building things people love and changing the director of the business, everything else is just an input.

Noah Weiss (01:08:16):
I think that focus and understanding as your point about laying the tracks is what direction do you need to go as a team to actually drive that impact? That's probably the single thing that PM can most control.

Lenny (01:08:28):
I love that. I always recommend exactly that if your career is not going as well as you'd hoped or you're not getting promoted, it's usually you're not delivering impact, whatever that means to the company. It may be moving a metric may mean building great product that the founders really love.

Noah Weiss (01:08:43):
Yeah.

Lenny (01:08:43):
Main impact can mean a lot of different things. But it's so true. On the executing impeccably bucket, the way I think about that is as a great PM you need to have this aura of "I've got this." Anytime someone puts something on your plate, it's not going to fall off. You're not going to forget about it. You're not going to let a ball drop that if the more you can create this aura of "I got this," the more responsibility people are going to give you, the more impact you'll end up having, the more people want to work with you and all that.

Noah Weiss (01:09:12):
Yeah. Ben Horowitz was a board member back at Foursquare. I remember he used to have this saying very Yoda of good leaders need to say what they're going to do and then do what they said. If they can't then they need to follow up and explain why. I mean that's like the amendment and I think that is what good execution looks like.

Lenny (01:09:33):
That last point is so important. You may not be able to do all the things on your plate, but just telling people. Hey, I'm not going to get to this thing. Let's reprioritize as such a small thing you could do and really creates that, or if you got this, they're not going to forget about this thing asked you to do.

Noah Weiss (01:09:47):
Yeah. You're the shock absorber for the team. You're the thing that builds people's confidence that things are going to be running smoothly and you'll get over the Navajo speed bumps and whatever else. I'll combine two or three of these that are related or just more skills. I said right well. I actually think especially as you get to more senior positions, writing is the only scalable way of having influence on a larger, larger product org.

Noah Weiss (01:10:15):
There's a book called On Writing by Stephen King, which I recommend to literally everybody. Stephen King, you're like ... See he's not maybe the most literary critical acclaimed author, but he's a prolific author who publishes things that people love and tell their friends about and he has a great short book on the practice of writing high-quality, high-volume production.

Lenny (01:10:39):
Before you move on, I'll throw a couple more books that I found useful in my writing. One is actually called On Writing Well. That's funny that they're so similarly titled, which basically every chapter is just another way to cut more from your writing. More and more parts you should cut. Interestingly, I do have a lot of guest posts in my newsletter and I find 90% of the time if I just cut the first paragraph of what they first took a crack at and jumps straight into the thing, immediately gets better. This book talks a lot about that.

Lenny (01:11:07):
Another book that is amazing for writing better is Nobody Wants to Read Your Shit by the guy that wrote The War of Art, forget his name. But that book is awesome and it's just like nobody wants to read what you're writing. Here's how to maybe make it something people want to read. Then recently I read one called Several Short Sentences or something like that. It's all about just writing short sentences and that helps a lot. There you go. Three more recommendations.

Noah Weiss (01:11:32):
Okay. I got to read the last two. I haven't read those, but they sound perfect. Okay. Maybe I'll throw one more. Let's say we talked about this earlier, but actually read this in the post many years ago, is optimizing for the pace of learning and knowing that long-term massive thing that's going to drive impact. I think it can be hard if you're a PM for a feature team. You're part of a big company. I don't know. I'm making this up.

Noah Weiss (01:11:55):
You're on the AdWords team at Google and you're responsible for the bid input selector or something and probably is a whole team, honestly, now at this point. You've got such a set of blinders on that I think it can be hard to think about what else could this team become, what else could you drive beyond the thing that's right in front of you?

Noah Weiss (01:12:16):
Optimizing for learning, being willing to take those bolder bets, knowing you can be wrong in the short-term, but that you'll learn new levers that will be really fruitful in the long-term. It's a portfolio approach to product, but I think a really important one.

Lenny (01:12:30):
I was just interviewing a product leader at Asana, Paige Costello. We were talking about how she's often the youngest person in the room and often manages people that are much older than her and more experienced than her and asked her just how do you that? How do you succeed in that environment?

Lenny (01:12:46):
What she's found is just being the person that has the answers and the insights in meetings, people obviously run to her like, "Hey, what do you think of this?" Because she just knows what people are going to need. I think that's exactly what you're talking about here is just be the person that knows the most about the problem, the customers, the space.

Noah Weiss (01:13:04):
Yeah. Then I'll combine the last two just because I know time. But the combination of ... I wrote data fluency, which is not to say that every PM needs to be a statistician. I mean it's great. I mean you've had a lot of great posts about how to understand some of the basics of experimentation, correlation, causation and statistical significance. That's all great.

Noah Weiss (01:13:23):
But by data fluency, I think it's more actually what you were just saying, which is you know enough about the insights about your customers that it can then inform making higher likelihood product bets and that data can be quantitative, that data can be survey based, it can be from doing 100 meetings with customers yourself. Those are all types of data inputs to me. Being really fluent and then maybe combining that with great product taste.

Noah Weiss (01:13:49):
I know it's a controversial statement now to say that there is taste for product. But I do think in all the love of the frameworks and the analytics and everything else and in the field of product, I think people sometimes lose sight of, "It's a creative field." It's not art on its own. But you could get all the inspiration from art and I actually think there's a lot ... there's a book, I think it's called Creative Selection, I forget the exact name of it, about some of the early iPhone development teams at Apple and working with Steve Jobs there.

Noah Weiss (01:14:21):
I've never worked at Apple. But I actually think it's the best book I've read about the just iterating creative work of building new products and what it means to have taste, which is to say you've developed some amount of intuition for what people will likely love before you're able to test it. Anyway, I think taste plus fluency and data, that too is a combination, is a pretty powerful combo.

Lenny (01:14:48):
Let me ask you just a couple questions about this list before we get to a very exciting lightning round and I can let you go.

Noah Weiss (01:14:55):
Okay.

Lenny (01:14:56):
Of these 10 attributes, say you're a new product manager, if you had to pick two or three that you think are most important to get right and focus on in your early career, which would you say they would be?

Noah Weiss (01:15:06):
I think for early on in your career, what I would say is getting great at execution. It's a thing that you can most control. Then I think building that news for impact, even if the impact is more local, because that's how you actually will demonstrate momentum and build credibility and then actually do think early on getting really fluent on the data and the research side that you can have insights that you can read back to your team.

Noah Weiss (01:15:29):
Those are to me the most slammed up ways of becoming someone who starts to build credibility as a product manager in any organization.

Lenny (01:15:38):
Awesome. That's what I always tell on new PMs too, is just get really good at execution because that creates that aura of, "Oh, this person's just killing it. They're just shipping on time. People know it's happening. They're hitting dates," things like that.

Noah Weiss (01:15:48):
Yeah.

Lenny (01:15:49):
The last question is just say more of a senior product leader, say, on director. Are there three other attributes you think are ones they should focus on most or maybe the same?

Noah Weiss (01:15:59):
Yeah. I mean I think this is where the pace and quality decision making starts to matter a lot more because you're still unresponsible sometimes for teams of teams and you're helping to facilitate high quality decisions, often ones that have a lot of uncertainty or risk or ambiguity. How do you keep the organization unblocked, not just a team moving well.

Noah Weiss (01:16:21):
I think the living in the future and working backwards, I think the more senior you get, it's always going to be the product founder who is responsible for the ultimate vision, but you become more responsible for that meeting a longer-term strategy to realize that vision. Becoming just someone who can dedicate more of your time to be out of the fray of the day-to-day and think more about the longer-term strategy that you want to pursue.

Noah Weiss (01:16:47):
The last one, and we talked about just earlier, but I think being a really good writer, it is just the highest leverage usage of your time. If you want to influence an organization at least for one that doesn't just spend all day in meetings, but I think it's really hard to dedicate the time to it because you're probably spending most of your day in meetings. It's the antidote to that to scale your ability to influence the product direction and maybe even the principles and how you develop product at a company.

Lenny (01:17:17):
Well, with that, we've reached our very exciting lightning round. I've got six questions for you. Are you ready?

Noah Weiss (01:17:22):
Let's do it.

Lenny (01:17:23):
What are two or three books that you've recommended most to other people?

Noah Weiss (01:17:27):
These may not be the most unique, but I will say them, which is Innovator's Dilemma by Clayton Christiansen, whether you're working a large company and you're suffering it or you're working a startup and you're trying to out flank an incumbent, I still do think that and innovative solution, the follow on are the best books on product strategy to read.

Noah Weiss (01:17:47):
If you're moving into more of a leadership or management position, I think Radical Candor by Kim Scott is just incredible and worth everyone reading. Frankly, if you're a PM and you're doing soft influence, I think it's really important. Then the third one, which is maybe a little off the beat of path, there's a book called Leadership in Turbulent Times by Doris Goodwin who's a presidential historian.

Noah Weiss (01:18:12):
It's this amazing book that looks at four of the most notable presidents and how their leadership style evolved when they were in really critical hard times in their presidency. I just think it's actually the best book about leadership style and how do you evolve and how do you deal with crises, which again is maybe later on in your career. But I love getting inspiration from not just reading books about tech and product and I think that's one of the best ones.

Lenny (01:18:40):
What is a favorite recent movie or TV show you really enjoyed?

Noah Weiss (01:18:43):
The obvious answer, which I'm sure many people would say would be Succession. I'm not going to ruin anything for the finale because people haven't seen it all. But the writing, the Shakespearean level drama of it all, it's just incredible and just heart wrenching that you wind up loathing most of the characters. But you can't take yourself out of it.

Noah Weiss (01:19:03):
The one that's maybe less common, and I watched right when we started paternity leave is The Bear, I don't know if you heard about it.

Lenny (01:19:11):
The restaurants.

Noah Weiss (01:19:12):
Yeah.

Lenny (01:19:13):
Yeah. Seen that. Yeah.

Noah Weiss (01:19:14):
I'm a sucker for incredible cinematography, just what they do in basically the single room of this restaurant and kitchen and just the piece of it. I think it's just an incredible piece of art. I don't know if it's the best show ever, but it is a really moving, emotionally jarring piece of TV.

Lenny (01:19:34):
Also, quite stressful to watch.

Noah Weiss (01:19:36):
Very sure. I would not relax to it to go to sleep.

Lenny (01:19:39):
But Awesome. Okay. Favorite interview question that you'd like to ask candidates?

Noah Weiss (01:19:45):
That would depend a lot, I think on obviously, the seniority level and things like that. But I think the more general, and I always love to ask people is what unfair secrets have you learned to improve the velocity and energy level of a product team? When I say unfair or you in secret, I usually mean not something that you probably read on a medium input. But what did you learn? How did you learn it and how does it work and how do you apply it? You also just get amazing interesting bits of inspiration from asking that.

Lenny (01:20:17):
What is a favorite product you've recently discovered that you love?

Noah Weiss (01:20:21):
This will also serve for recommendations for you based on or you've not thread about parenting clients because none of the products I've learned or loved recently have been software. But they're all maybe software enabled. The Nanit, which is a weird name, but it's this AI-enabled camera for basically watching your day as they sleep. It's like incredible, look, because you sleep analytics and really helps you be a less neurotic parent. I would highly recommend it.

Noah Weiss (01:20:48):
The SNOO, which is basically this amazing device that can help soothe your kid when all they need is a little bit of that soothing while they sleep so that you can sleep a little bit more. You can tell the steam here is sleep. The last one is there's this chemical up baby that has this whole elaborate stroller system with interchangeable parts and, honestly, it's just an incredibly well-designed piece of hardware that works in and out of the car.

Noah Weiss (01:21:16):
Yeah. I think I've re-appreciated really well-designed hard products that are not necessarily hardware from Apple and that has been what baby new parents is about.

Lenny (01:21:26):
I have all three. Also, a huge shout-out to the Nanit team who sent me a Nanit and all the stuff around the Nanit. Thank you. I'm not going to name the specific PM who sent it to me, because I don't remember his name off the top of my head, but thank you, Nanit.

Noah Weiss (01:21:41):
Yeah. It turned out there was a whole world of baby tech, which I had no idea. I mean, it makes sense that existed, but you never know about until you're a parent. Now, I'm obsessed.

Lenny (01:21:49):
One tip that for Nanit, my wife and I have been playing with different names for our kid and we have been changing his name in the Nanit so that anytime we go into the room it sends us a push, "Hey, there's activity in the room with the names so that we could feel the different names."

Noah Weiss (01:22:05):
I love that. Yeah. My wife and I did something similar where we had three or four final name contenders and we didn't use the Nanit for. But we literal just picked a week and said, "On Monday we're going to like refer to the future baby by that name for the entire week and give some personification to it." That helped us get down from four to one. Yeah.

Lenny (01:22:28):
What a wide-ranging set of pieces of advice we got on this podcast. Two more questions. What is something relatively minor you've changed in how you develop product at Slack that has had a lot of impact on your ability to execute?

Noah Weiss (01:22:38):
By far, the biggest thing, which is more of a cultural shift is that we stopped spending so many cycles on design explorations of static mocks or walkthroughs and said, "How quickly can we get into prototyping the path in real software, even if it's messy and you throw it away," at least for something like Slack. You got to live and touch and smell the software. You can't just look at it. That's been a huge unlock for avoiding spending months on design debates and just getting to, well, how does the software feel? That's what matters.

Lenny (01:23:12):
Speaking of Slack, final question, what is your favorite Slack pro tip that people may not be aware of?

Noah Weiss (01:23:19):
I'm going to give two because if someone asks me this, "I'm like, these are the two things that if you're not in love with Slack, you'll fall in love with Slack." The first is obviously you have a sidebar, it can be unruly, but you can customize the sidebar into sections and each of those sections you can have settings like. "Show unread only" or "Sort by recency," or "Sort by alphabetical," whatever it might be. You can collapse the section so you don't see it all at once.

Noah Weiss (01:23:44):
I think having a well-managed sidebar, which doesn't actually take that long, it's like this amazing thing because then all this inbound is structured in an order and a grouping that fits how you want to view your working life. Customizing the sidebar. The second thing is just use the quick switcher for everything. Just hit Apple K and just start typing and it feels like they're playing a video game, just hopping around channels, people, files, search. Pretty much all the actions you can take are on as well.

Noah Weiss (01:24:15):
I think most SaaS products now have borrowed that pattern. You can use another software, but it works particularly well in Slack.

Lenny (01:24:23):
No. I know the last thing you needed was to record a podcast your first week back to work. I so appreciate you making the time. It feels like we're two ships passing in the night from pat leave and to new pat leave. Two final questions. Where can folks find you online if they want to reach out and learn more and how can listeners be useful to you?

Noah Weiss (01:24:39):
I will confess that I haven't used Twitter in months because I was doing digital detox, but still I think @Noah_Weiss is a pretty good place to find me online and whether there or anywhere else, still love to have peoples like Slack feature requests, especially about things that you wish were possible or that would get the rest of your company to join on Slack because you love it, but you can't convince them. Those are always golden nuggets.

Lenny (01:25:04):
Awesome. Noah, thank you so much for being here.

Noah Weiss (01:25:06):
Thank you so much for having me.

Lenny (01:25:08):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

