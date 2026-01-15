---
guest: Varun Parmar
title: An inside look at how Miro builds product | Varun Parmar (CPO of Miro)
youtube_url: https://www.youtube.com/watch?v=furNg4njlsg
video_id: furNg4njlsg
description: 'Varun Parmar is the Chief Product Officer of Miro and has over two decades
  of experience in the tech industry. Prior to joining Miro, Varun held executive
  positions as Chief Product Officer...

  '
duration_seconds: 5111.0
duration: '1:25:11'
view_count: 13074
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- metrics
- okrs
- roadmap
- analytics
- funnel
- pricing
- hiring
- culture
- leadership
- management
- strategy
- vision
- mission
---

# An inside look at how Miro builds product | Varun Parmar (CPO of Miro)

## Transcript

Varun Parmar (00:00:00):
Every single day, every single time somebody is pushing your code to production and you're releasing a feature or an enhancement, you are making the product better or you're making the product worse, but the products never remain same. So with every release that your competitor is making and every release that you're making, you are either making chess points, moves against them, positive points, or you're going negative. I think that framework, it actually drives an insane amount of clarity in terms of what you're doing and what the impact is going to be.

Lenny (00:00:33):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard-won experiences building and growing today's most successful products. Today my guest is Varun Parmar. Varun is chief product Officer at Miro, and prior to Miro, he was senior vice president and chief product officer at Box. As I share with Varun at the start of our chat, I've always been really curious about the product culture at Miro, partly because everyone I've ever met from Miro has been super interesting and super smart, and partly because they've been able to grow as a business and a product in an incredibly competitive market.

(00:01:07):
In our conversation, we get really deep into the product values and principles at Miro, their product development process, how Varun approaches competitive threats, how a bimonthly company-wide product demo ritual led to saving months of engineering work on a feature, plus insights into how Miro got started, how they grow today, and what their product team has learned about working with a large sales org. Varun is amazing, I learned a lot, and I hope you find it as interesting as I did. With that, I bring you Varun Parmar after a short word from our sponsors.

(00:01:39):
Today's episode is brought to you by Miro, an online collaborative whiteboard that's designed specifically for teams like yours. I have a quick request. Head on over to my Miro board at miro.com/lenny and let me know which guests you'd want me to have on this year. I've already gotten a bunch of great suggestions, which you'll see when you go there, so just keep it coming. While you're on the Miro board, I encourage you to play around with the tool. It's a great shared space to capture ideas, get feedback, and collaborate with your colleagues on anything that you're working on. For example, with Miro, you can plan out next quarter's entire product strategy. You can start by brainstorming, using sticky notes, live reactions, a voting tool, even an estimation app to scope out your team's sprints. Then your whole distributed team can come together around wire frames, draw ideas with a pen tool, and then put full mocks right into the Miro board.

(00:02:29):
With one of Miro's ready-made templates, you can go from discovery and research to product roadmaps to customer journey flows to final mocks, all in Miro. Head on over to miro.com/lenny to leave your suggestions. That's M-I-R-O.com/lenny. This episode is brought to you by Braintrust, where the world's most innovative companies go to find talent fast so that they can innovate faster. Let's be honest, it's a lot of work to build a company and if you want to stay ahead of the game, you need to be able to hire the right talent quickly and confidently. Braintrust is the first decentralized talent network where you can find, hire and manage high quality contractors in engineering, design and product for a fraction of the cost of agencies. Braintrust charges a flat rate of only 10%, unlike agency fees of up to 70%, so you can make your budget go four times further.

(00:03:22):
Plus they're the only network that takes 0% of what the talent makes, so they're able to attract and retain the world's best tech talent. Take it from DoorDash, Airbnb, Plaid, and hundreds of other high growth startups that have shaved their hiring process from months to weeks at less than a quarter of the cost by hiring through Braintrust network of 20,000 high quality vetted candidates ready to work. Whether you're looking to fill in gaps, upskill your staff or build a team for that dream project that finally got funded, contact Braintrust and you'll get matched with three candidates in just 48 hours. Visit useBraintrust.com/lenny or find them in my show notes for today's episode. That's usebraintrust.com/lenny for when you need talent yesterday. Varun, welcome to the podcast.

Varun Parmar (00:04:10):
Thank you, Lenny. So excited to be here. Thanks for having me.

Lenny (00:04:13):
I'm really excited to have you here. I've been looking forward to having a chance to dig into Miro's product culture and the way Miro works for a while. We've actually had a few guests, ex-Miro... Mironeers, is that what you call yourselves?

Varun Parmar (00:04:25):
Yes, Mironeers.

Lenny (00:04:27):
Okay. Mironeers. So we had Elena Verna on the podcast, who's amazing, and Barbara who I think worked in marketing and everyone I've always met from Miro has been just really smart and really interesting and it just feels like you guys have a really interesting product culture that I haven't felt like has been shared a lot, and so I have a bunch of stuff I want to dig into there. One question I have at the bat, you guys have a really interesting history and specifically the way your company's structured, which is that you're collocated in Amsterdam and San Francisco. First of all, is that correct?

Varun Parmar (00:05:00):
The company is a global company, so we've got 12 different hubs. We have multiple offices in US, four different offices, and then multiple hubs in Europe as well, and presence in AsiaPac as well. I think by now we have a global footprint, yeah.

Lenny (00:05:17):
Got it. A question I wanted to ask off the bat is just how has that cross-cultural approach to product teams impacted the way that you guys built product and the way the company operates?

Varun Parmar (00:05:30):
The one thing that's really interesting, Lenny, around the way Miro is set up is that our product organization is actually based in Europe and our go-to-market organization is worldwide. Our product management team, our designers, our engineers are located across three different hubs in Europe. What that sort of leads to is a couple of practices that we have as part of our culture. The first one is practicing empathy to gain insights. It's not just practicing empathy in terms of customers and figuring out what customer pain points and problems we can solve, but given our distributed nature in terms of having a global footprint and a lot of our go to market teams, folks in sales and marketing and customer success are in different continents or geographies, we have to make sure that we actually practice that internally. When we are interacting with folks, let's say in San Francisco, and those folks are out there meeting some of our large customers and stuff, how do we, in the product organization, understand their perspective, and bring that perspective into how we design, prioritize and build products? I think that's one thing that's unique.

(00:06:43):
I would say the other thing that's less to do with the location, but I think is sort of the core cultural value or philosophy that Andre, who's the founder and CEO has instilled in all of us, is practicing teamwork, how do we actually come together as a team, and bring down the silos that might exist across functions? I'll talk a little bit around how we are structured in the product organization so that it's a cross-functional perspective we bring to everything that we're doing because we believe the best work happens when we bring different diverse perspectives to the problem and then co-create the outcome that the customer is looking for.

Lenny (00:07:20):
I want to pull on these threads actually real quick. You talked about this value of empathy and the importance of having empathy across... because you guys are located in different locations and have different cultures, and also this idea of teamwork. What's something that you've done that helps you do that, either build empathy and maintain empathy across teams or make sure that people work in teams and not like, "Hey, there's this other team over there doing something else"?

Varun Parmar (00:07:45):
One of the most powerful things that I've seen work is the questions that you ask, the questions that you ask when you're going through product review or you are going to sit down and talk to someone and trying to understand why did they prioritize something over the other and was it something that was done through interactions they've had with folks internally or externally? I think it's the set of questions to ask in terms of how did they get to where they are today and was it informed by understanding of the insights that collectively the organization has? Was it informed by their understanding of where the market is evolving, where the competition is going.

(00:08:31):
Was it informed through the series of insights they have, either through inbound feedback that's coming through our different channels where customers are giving feedback or some outbound interactions that they've had? I think just trying to double click and getting to the details in terms of what insight led them to recommend certain things or make a left turn or a right turn is where I think is the most powerful way to make sure that those things are informed through practicing empathy internally and externally.

Lenny (00:08:59):
Got it. There's this kind of cultural value of just assuming good intention and asking questions to understand where someone came from. I don't know if you'll have something off the top of your head, but is there a story or an example of that comes to mind where that was done well or not done well, I don't know, in something you recently were building?

Varun Parmar (00:09:16):
Maybe there are certain things, for example, anytime we're trying to build a new experience, one of the approach we want to take is very quickly validate that our original hypothesis, is that sound or not. We are big fans of the Design Sprint framework, what Jake Knapp has done I think is really amazing. In a short five-day window, you can get a small set of people to quickly mock up a concept, convert it into some sort of a prototype and then go out there and get some sort of a validation. Oftentimes when we are working on some of these new things, we have our product teams that are focused on zero to one initiatives, run this five-day initiative, and at the end of it we say, "Oh, this is great. Who did you get insight from?" There's a capability that we recently released, it's called Miro Talktrack, which essentially allows you to asynchronously do asynchronous collaboration by recording audio video on top of a Miro board.

(00:10:16):
We had two fundamental choices we could make. One, we could go down the path of what everyone's doing where you could do a screen recording and then spit out a series of videos, like pixels being captured. Or what we did was we actually went down a different path and the path that we went down was we basically synchronized the movement of the board. Let's say Lenny's presenting a board, some template he's created in terms of best practices for PMs, but he wants to have some sort of a talk track on top of it, an audio video feed. What we are doing is we're actually capturing the movement of the board that Lenny's going through along with the video talk track that's on top. The reason why we did that was because we had an insight that came through some of our interviews.

(00:10:56):
What our users want to do is they want to use Miro for collaboration. While communication is an important aspect of how teams come together, where we believe our sweet spot is that we want people to use Miro for collaboration. By making sure that they could actually use a video recording and while the video recording is playing, they could add in a sticky note, they could add in a comment, they could actually give a reaction. We were able to develop this insight by practicing empathy as part of the Design Sprint framework when we went and started to show our original concept and we walled and built on top of that.

Lenny (00:11:31):
That is a really cool story. That came out of this Sprint framework, these five-day sprint approach.

Varun Parmar (00:11:36):
Yes, that's right. Yeah.

Lenny (00:11:37):
That is cool. I got to have that guy on this podcast. Jake Knapp, you said, right?

Varun Parmar (00:11:41):
Yes, yes, yes. I can text him right now and I can make the introductions, yes.

Lenny (00:11:45):
Let's pull him right into this podcast live, tell us how the Sprint process works. That is awesome. This connects a little bit to another question I wanted to ask around the top is, you guys are in a really competitive space and it feels like Miro was very early in online collaborative whiteboarding space and then I think during COVID it just became huge, with the remote work exploding. Like, "Holy shit, everyone needs this immediately." Over the years, many companies have come into the space that you are all in and it feels like Miro continues to do extremely well. I remember when Figma launched FigJam, there was a lot of just like, "Miro's dead. Figma's getting into the space, they're juggernaut, game over." Clearly that's not been the case and it just feels like, I don't know what it is internally that you all do that continues to allow you to compete and continue to innovate in the space. I'm curious just like is there something to how Miro approaches competition and also just, I don't know, the way they approach these sorts of challenges that is unique or interesting that you can share?

Varun Parmar (00:12:45):
If you look at the mission for Miro, we empower teams to create the next big thing and our focus is to enable teams that are innovating, and generally innovation happens at the intersection of a bunch of cross-functional folks coming together. Like we discussed, folks in product management or design or engineering or analytics or product marketing or research. What we find, Lenny, is that there are a lot of tools out there and those tools are generally sort of focused on a particular persona and maybe they're trying to solve the needs of a designer and a designer has a workflow that they're trying to do and they're using a specific tool and they sit at the adjacency of extending that core use case. The fundamental value that Miro provides is that we enable teams. I think what's unique about our product, and we can talk about the capabilities and roadmaps and use cases that we are investing in and we already have as part of the product, is that we take a team-centric lens.

(00:13:50):
So we're not saying, "Hey, we're building a tool that just works for designers," or "Hey, we're building a tool that just works for engineers." Because we fundamentally believe that innovation happens when cross-functional teams come together. When you look at the problem through that lens, you realize that you have to actually architect your solution. You have to think about the use cases and you have to go and prioritize certain experiences that are different and our customers see value in that, right? I think that's probably one sort of big macro aspect of how we think about our capabilities and products and why our customers think of us differently. I'd say that's say one point.

(00:14:27):
I think the second thing is Miro is actually used obviously by teams that are creating these innovative products and we actually have broad applicability across industries and verticals. While some tools might be hyper-focused on digital experiences and Miro's has great offerings there in terms of core capabilities, what we find is that Miro is used equally by companies in manufacturing, by companies in healthcare, by companies in architecture and engineering and construction functions, by companies that are in aerospace, governmental agencies and medical agencies and so on and so forth. I think the platform is actually much more agnostic in terms of its capabilities and what we offer that actually makes it more accessible and appealing to organizations that want to go beyond just digital experiences.

(00:15:26):
Then I would say finally there are capabilities that are available very, very uniquely to Miro that are valued by our users. That again is a big reason people come to Miro. For example, if Lenny's trying to conduct a big workshop with a bunch of product folks and he wants to facilitate that workshop and wants to have certain folks focus on one part of the board and while others focus on the other part, then there are some advanced capabilities that enable certain use cases like workshops. Or if you want to use Miro for some team rituals or from some agile practices, there are core set of capabilities that you could use the product for that are missing in some of the other capabilities. I would say a combination of all of those three things continue to drive differentiation. I would say on top of that, we are a big fan of our community and we believe that community love is what drives us. That's the fuel that keeps us going every single day.

Lenny (00:16:31):
Awesome. Just to summarize and I was taking notes as you're chatting, just thinking about what allows you all to continue to do well in the market, considering all the competition constantly coming at you. One, as you mentioned, just there's kind of like a innate multi-functional architecture which is hard for someone to copy if they weren't built from that without the start. Two, it sounds like you are focusing on a wide spectrum of personas and it's not just tech employees basically. Also, just there's specific features that end up being really important that maybe people have a hard time building and then this last piece of the community. Awesome.

Varun Parmar (00:17:08):
Yep.

Lenny (00:17:09):
Let's dig into the product team a little bit and understand how you all build product and structure product team. How many PMs are there at Miro? Then just broadly, how many employees, just to give people a set of, little bit of context?

Varun Parmar (00:17:20):
Give or take about 1,800 employees at Miro globally across all of the 12 hubs, and specifically in terms of the number of product managers, there are over 450 PMs in the team.

Lenny (00:17:34):
Then how's the product team structured? Is it like outcome oriented? Is it product area oriented? Is it user persona oriented? Is it something else? How do you think about the structure of the product team?

Varun Parmar (00:17:46):
Yeah, so I would say it's maybe a hybrid structure that we have, but the foundation of the team setup is around persona. We have what we refer to as streams, some companies refer to as domains, but essentially it's a set of individuals that are focused on solving the problems for a key persona. Just to give you an example, we have a stream that's focused on enterprise, and in enterprise we are looking at the IT admin persona, we're looking at the security persona or the compliance persona. There are a set of folks who are creating a roadmap and innovating for that audience. There's another stream which is called platform where we are going after the developer install base, folks that want to use Miro as a platform and build apps that they can actually make available either on the marketplace for everyone to use or they could be developers that are inside of a large organization and they're trying to integrate Miro with their specific use cases and workflows and business systems. That's another sort of stream that's focused on that, and there are a couple of other streams like that.

(00:18:53):
Then finally there are some just horizontal sort of streams, if you will. We have a big focus given that we are a PLG-led company around growth and self-serve business. We've got a stream that's actually focused on our core internal infrastructure. We've got a stream that's actually focused on data science that's doing all of the magic that we started to release in terms of Miro AI, et cetera, et cetera. I would say it's a combination of those. At the heart of it is we are focused on personas and we are sort of aligning people around solving problems and creating value for that persona.

Lenny (00:19:24):
That is really interesting. One of the downsides of a persona-based approach I imagine is that features keep getting added that solve that user's pain points. What have you learned about keeping the product consistent and having a holistic perspective on the experience? How do you address Those challenges?

Varun Parmar (00:19:43):
Architecturally, there are two sort of things that we have done that allow us to not pigeonhole ourselves into that specific way of working. I completely agree with you, you could lead to that. The first one is actually when we think about the product org, we call our org, it's called AMPED, A-M-P-E-D. This is actually going back to our earlier point, Lenny, we had around what's unique about the product culture, what's unique about Miro, and we talked about teams coming together, removing barriers or silos cross-functionally. AMPED stands for analytics, marketing, product, engineering and design. And everything that we do in the product org, when we say the product org, we actually don't meet product managers. We actually don't mean product managers, designers and engineers. What we mean by product org in Miro is this AMPED function. By having this cross-functional representation where product marketing team is deeply, deeply embedded inside of each of these streams, what we do is that we have different perspectives that come in where they say, "Oh, wait a second, did you think about the end user experience?"

(00:20:49):
If you think about the end user experience, you know have someone on the team that says, "Wait a second, did you actually think about the enterprise requirements or what's needed in the largest corporation?" I think the unique setup of bringing these cross-functional folks allows us to sort of course correct. The second thing is the ways of working that we have. We have these product reviews that happen. We generally classify anything that we are doing in terms of its complexity around a small, medium or high complexity, and anything that's being worked on is actually being shared with the entire organization. If it's something that's small to medium, it's actually shared with the entire product org. In fact, if you are non-product, you can actually subscribe to that Slack channel as well. Everybody sees what the product org is working on, everybody sees what the core hypothesis is, "What is the solution for that, what is the proposed design for it, how are we thinking about the capabilities?"

(00:21:49):
Then anything that's big actually goes through a formal process like a product review where there's a meeting and a bunch of us are in there and it's up to us, including the product leaders, to basically make sure that we are connecting the dots in terms of having a much more holistic perspective. I would say lastly, as Miro has sort of scaled the spectrum of companies all the way from a team that might have two or three people and might be taking out their credit card and using Miro for their own team all the way to a large corporation that might have 50,000, 80,000 employees, all of them are using Miro. We've come to realize that at some point the deep enterprise requirements need to be encapsulated in a set of requirements or best practices and we need to make sure that those get democratized across all of the feature teams.

(00:22:36):
When I'm thinking about building a new feature, I have a checklist in front of me where I can say, "Here are the 10 things that I need to think of that I need to incorporate early on in my thinking in the architecture, in the definition of the process, so that it doesn't come downstream." I would say that's an area where we're still working on and more recently we put more focus and energy and there's a product manager who's now leading that particular charter.

Lenny (00:22:57):
I love all these details. This AMPED structure, I love that. There's analytics, you said product marketing, analyst marketing and then product engineering design. It's rare that you see marketing as a part of teams, as a leadership, kind of part of the leadership group. Do you have a sense of what impact adding that had on the team or where that came from? Or is that just historically been something Miro has prioritized, marketing and product marketing?

Varun Parmar (00:23:25):
This was done before I got here and I wish I could take credit for it, but I can't. I think this was the result of an observation, which is quite similar to what you're saying, which is while we might be developing a lot of the features and PMs or thinking bottoms-up in terms of what we are building, we might find that what we have built might not be able to capture the imagination of what we originally thought it would. A big part of that is how are you going to think about positioning, how are you going to think about competitive differentiation? How are you going to package it up so that the sellers that are out there are able to position it in a way that the customer, in this case the buyer, might be an IT professional, might a line business leader, can basically see the full vision of where we are going? I think by having product marketing as part of AMPED, we now bring that unique perspective that may be missing in certain teams.

(00:24:24):
PMs are more acting as product owners or more focused on core problem and solution but not thinking about positioning, because that's so important, especially when you're thinking about a market that we are increasingly in that there is competition there. That's one of the first things we started off with and that's top of mind for you as well, is that everything that we are doing has to be looked through that lens. One of the core philosophies that I have, Lenny, is that the success of a company is a direct relation of what the competition allows you to do. I feel like not many people talk about that, but in many cases in my professional career, and I've been at it for close to 24, 25 years, is that every single instance when I looked at a company accelerated their growth or there was a deceleration of growth, it was a direct relation to what the competition allowed you to do. Obviously, you have to do everything that you should be doing, but competition is the biggest variable that allows you to figure that out.

Lenny (00:25:24):
I want to hear more about your core product philosophies, but let me dig into the one you just shared. What you find is that the way you grow or stop growing is often a direct result of your competition. Is there an example of that that comes to mind? I'm guessing maybe Box versus Dropbox is an experience you had there, or if not, what's an example of that that you've experienced, to make it a little more concrete even?

Varun Parmar (00:25:50):
For those of us who've been in the collaboration space, and I've been doing collaboration and productivity apps for over 20 years, over two decades, at some point, you have companies like Microsoft that get really attracted to a space and you can see the trajectory of a business that's growing at a certain clip and then all of a sudden there's a competitive product that enters that has the might of distribution and the might of pricing, and that's just a direct example. I think I've seen that multiple times, first at Adobe where I was part of the document cloud business, clearly saw that at Box as well.

(00:26:27):
I think you can, in general, sort of look at every single category and you can say that there was a category leader and they were growing at a certain clip or a certain pace and all of a sudden there were a bunch of entrants that get in and what happens to your growth rate? It's all dependent on how strong is the competitor in terms of providing a good enough solution? That's one. The second is how strong is the competition in terms of their distribution outreach? Then the third thing is how strong is the competition in terms of the pricing and packaging?

Lenny (00:26:55):
I really like this discussion, especially because often the advice is, "Don't worry about the competition, just focus on the customer, it's going to be fine." Which what you're saying is that's not right, and I agree. What do you do with that in mind? How does that impact the way you build product or strategy? Is there some you could share that maybe tactically someone could leverage to how they're approaching their product strategy?

Varun Parmar (00:27:18):
It depends on who the competition is and what is their unfair advantage here. We talked about one specific competitor and I have a lot of respect for them, by the way, and I learn a lot from them every single day in terms of how they make bets and how they enter markets and stuff. At some point I'm going to write a book on them, I feel.

Lenny (00:27:35):
Ooh. We'll have to come back to talk about that.

Varun Parmar (00:27:38):
That's right, yeah. I think it sort of comes down to how do you think about your unique place relative to all of these players, and in your customer's mind are they able to clearly understand what is the unique value that you deliver relative to everything else? Part of that is the unique capabilities you provide. Part of that is how you're packaging those unique capabilities to them, and making sure that they in their mind can see how you coexist in this overall sort of tech ecosystem that they might be investing in, to enable their employees or to enable them to operate. So I think it's sort of looking at that from that lens, yeah.

Lenny (00:28:26):
Got it. So what I'm hearing is be very clear about your differentiator and continue to invest there and then make sure your positioning is clear around why you're... just identifying, "Here's why we're different and we're not just a better or worse version of this thing" or "Here's why we're different" and making sure that's really clear.

Varun Parmar (00:28:43):
Exactly. I think the other thing I would say, there's another core philosophy I have, which is products either get better over a period of time or they get worse. Products never remain the same. I think you can take that philosophy to a bunch of things in life, but I'm going to take the lens of products, which is my core philosophy is every single day, every single time somebody is pushing your code to production and you're releasing a feature or an enhancement, you are making the product better or you're making the product worse, but the products never remain same. The lens for this, Lenny, is actually from a customer's perspective, from the end user perspective. The thing is that if you are a player where there's no one else in the market, that's one thing, so that's great. Kudos to you for actually identifying a blue ocean strategy and sort of executing to that. But most markets, most products, actually have either direct or indirect competitors that are available.

(00:29:40):
From the customer's mind, you're doing something, the competitor is doing something, so in their mind they're looking at these products and they're looking at these companies and they're saying, "Which is better versus not?" So with every release that your competitor is making and every release that you're making, you're either making chess points, moves against them, positive points, or you're going negative. I think that framework, if you have in mind, it actually drives an insane amount of clarity in terms of what you're doing and what the impact is going to be. Because every single move that you're making, the customer has that sort of in their mind, if not explicitly, implicitly that they're actually comparing these things. I think it brings a level of focus in terms of where you need to invest and why you need to invest and why this is going to make those decisions.

(00:30:28):
I think it allows at least for product leaders to make some high quality decisions around the bets that they're making and how they're going to play out in terms of eventual once the dust settles and the market at large is going to say, "I'm going to standardize on something and now I feel I need to go get it for everyone." Or "This is the tool that I want to use for this particular use case." That all of these decisions that you are making ladder up to that final sort of play that you have to do in terms of the market consolidation that eventually happens.

Lenny (00:30:59):
This is so interesting. Essentially what you're saying is that you find that being very close to and understanding the competition really well is really essential, versus this kind of the other end of the spectrum almost from just like, "Don't worry about the competition, don't pay attention." I like this point, metaphor of just like, "Are we moving ahead or further behind?" Is that where you operationalize that to track that? Then also just how do you not over-obsess with, "Let's just catch up, get more features," that kind of thing? How do you find that balance?

Varun Parmar (00:31:28):
I'll be honest, I don't think we've figured it out. We haven't cracked the nut in terms of how to operationalize this, but I know you are way smarter than me on some of these things, so maybe we can-

Lenny (00:31:39):
Unlikely.

Varun Parmar (00:31:39):
... partner on this and come up with something.

Lenny (00:31:43):
All right, that'll be something we work on. Any other product philosophies that you want to share? That was awesome.

Varun Parmar (00:31:52):
This is all sort of related to it. It's like a string of pearls. I think there's maybe one more pearl we can actually thread into the needle right here.

Lenny (00:31:59):
Let's do it.

Varun Parmar (00:32:00):
Which is we talked about how do you ladder this up and stuff, and then the question is, okay, how do you know that everything that you're doing, is that in the right direction or not? Should you move slow and be much more mindful about the things that you're doing or should you move fast and make certain bets and then decide certain things and stuff? I think there are two views that are out there. My personal perspective on this is that what you want to do is that you want to be the first one to hit the brick wall. This is particularly true when you are in a market that is competitive. The reason for that is that if you consider yourself as an innovation-centric company and you believe that you are building experiences that fundamentally don't exist anywhere else and you're sort of paving the way for the rest of the folks to basically get inspired with how you are building these experiences, speed is the single biggest determinant, in my experience, in terms of who ends up being more successful versus not.

(00:33:14):
I don't know, maybe this is a little bit controversial where people say, Go slow to actually go fast." I think I have a lot of respect for that and there's certain areas you should do that, but when you are trying to figure out new experiences and stuff and you don't know if it's going to resonate or not, speed is something that you should accelerate for the organization. I think Frank Slootman talks about this a lot in his book and how can you accelerate? I think for me from a product perspective, the fundamental concept is can you be the first one to hit the brick wall where you have the learning faster than anyone else in the market so that you can decide, "Oh my god, the path that I was going was not the right path. I need to do 10 degrees west or I need to do 30 degrees east." I think as long as you're one or two or three steps ahead of everyone else in terms of uncovering or discovering those insights, then I think you can continue to be ahead of the pack in terms of building your product in business.

Lenny (00:34:21):
You're talking about urgency. I've never met a founder or a product leader who doesn't want their team to move faster. They're always encouraging their team, "How do we move faster?" I'm curious if there's something you've learned tactically about helping your team move more quickly. You mentioned Frank Slootman's book. Amp It Up is what it's called, by the way, in case folks want to check it out and he's big on just like creating a sense of urgency, constant urgency, and we'll link to that and share notes. But yeah, what have you found helps create urgency and generally helps your teams move faster other than just like, "Move faster, everyone"?

Varun Parmar (00:34:52):
My fundamental belief here, Lenny, is that every product manager... I can talk to product managers because there is reason certain ones, someone wants to be a product manager, because in my view it's one of the most thankless jobs, like you get to do a lot of [inaudible 00:35:10] and it's like, "Why you have to do this?" But it attracts a certain personality and that personality is driven by challenge and that personality wants to prove that they can solve this challenge and do something amazing. I think fundamentally the product persona actually wants to move fast. I think the reason why in some cases we are not able to move fast is because of roadblocks that we run into and those roadblocks can manifest themselves into technical challenges, they can manifest them in cells of organizational challenges, they could be priority challenges and so on and so forth.

(00:35:52):
My fundamental approach to solving that is to ensure that the product leads who are working on these capabilities can instantly raise their hand and call out that there are challenges that they are running into. Then the job of the leadership team, the product management team, is to essentially go and quickly resolve those issues. I think if you are able to resolve those issues, then what it does is it actually starts a virtuous cycle where you can actually start to see those wins. Once you see those wins, you actually create that courage to do more things. Maybe because you've seen how that specific roadblock was solved and you have a pattern matching that you've developed now, you can solve a lot of those things on your own and it's the next level of challenge that you now going to raise your hand.

(00:36:41):
What that does is it starts to build this organizational competency in terms of how you can figure out what to build. We all find these people in our organizations where there's someone somehow is able to do certain things in one-tenth the time that it would take a normal person. It's not that they are 10 times faster, it's just that in my observation that they've figured out which part of the core base they should build in versus not, who should be part of their team and who should not be, how they need to define that from a scope perspective, what does success look like, and it's the architecture of bringing all of these things together that actually brings that magic formula line in terms of "Hey, we are able to deliver faster."

Lenny (00:37:19):
I really like this topic. What I'm hearing is one of the biggest roots of slowdown in a company and product development is blockers not being unblocked, and I always feel the same thing. I feel like a PM's number one job is to unblock their team because their job is basically make the most out of their team that they're marshaling towards some outcome. The way you do that is just figure out what's slowing them down. You just talked about this idea of a PM raises their hand to leadership, "Hey, we're blocked by this thing." Is there a process you've come up with there that helps you do that, it's connected to-

Varun Parmar (00:37:51):
Yeah, I would say we are trying to sort of systematically ingrain this in the culture of the organization. We have a motto in the product org, it's very simple, single sentence, deliver customer value faster with high quality. That's it. Everything that we do, and when I say everything, everything, Lenny, from performance and reward system and measurements, everything is based on this one single statement and it has three attributes. The first one is deliver customer value, and we believe customer value is only delivered when customers use it. Anytime as a PM at Miro, when you ship something, we are looking at, "Well, what was the metric you were going to move and how much did it move?" We have some original targets that we can go back to. That's the first aspect of what we're doing, deliver customer value.

(00:38:35):
The second one is move faster, and there are certain cycle times that we are measuring across the organization. From the time you came up with the idea to the time that you actually pitched a solution to the time you actually shipped it, to the time we actually moved the metric, it's information that has been collected and is being made available to the organization. You can say, "Hey, if it was a small, medium or large, what's the average? What's the medium, what's the variance?" And you can say, "Hey, looking at this data, what can be improved?" That's on the faster aspect of it. Then the last one is around high quality, which is we want to build best in class collaboration experiences, so we are always getting inspired by what we find in applications and experiences that we see around us and we are saying, "Hey, when it comes to designing, sharing flows, we believe that these are the three apps that have best in class sharing flows when it comes to designing some synchronous capabilities like this. These are the best in class apps that we should look at."

(00:39:31):
We are always trying to make sure that we are benchmarking ourselves against that and we have our design team. On a regular basis, like when we ship stuff on a monthly basis, our design leadership team does a triage of everything that got shipped into high quality or not high quality. It's just like a binary function, and we're doing that and we're saying, "Hey, the reason why we believe it's not high quality is because A, B, C, D, E and we're making it available to other designers so they can actually start to build that telemetry in terms of some things are more subjective." But you can start to see some patent matching and say like, "Hey, this is what great looks like."

Lenny (00:40:06):
This episode is brought to you by Linear. Let's be honest, the issue tracker that you're using today isn't very helpful. Why is it that always seems to be working against you instead of working for you? Why does it feel like such a chore to use? Well, Linear is different. It's incredibly fast, beautifully designed, and it comes with powerful workflows that streamline your entire product development process, from issue tracking all the way to managing product roadmaps. Linear's designed for the way modern software teams work. What users love about linear are the powerful keyboard shortcuts, efficient GitHub integrations, cycles that actually create progress, and built-in project updates that keep everyone in sync. In short, it just works. Linear is the default tool of choice among startups and it powers a wide range of large established companies such as Vercel, Retool and Cash App. See for yourself why product teams describe using linear as magical. Visit linear.app/lenny to try Linear for free with your team and get 25% off when you upgrade. That's linear.app/lenny.

(00:41:15):
Okay, so every month or so the design team looks at everything that's shipped and puts things into a bucket. Either this is... It's like a binary thing, high quality or not high quality.

Varun Parmar (00:41:24):
Yes.

Lenny (00:41:24):
Wow, that is so cool. Then, one, what do they do with that? Do they send it out to the product team? Then two, is this just like FYI or is it like, "We need to fix all these low quality things going back"? Or is it more just like, "For the future, please be aware these are not high quality"?

Varun Parmar (00:41:39):
Yeah, so it's actually both. Generally what happens is that the design leadership team is doing this and there's one particular design leader who's the designated person to make sure that this is happening on a regular basis. Right now the way we're using it is that we are actually using it to calibrate and align around the design leadership around what we mean by high quality. Because it's one of those things, it's like if you've never seen colors and I ask you, "Lenny, describe pink and compare that to red," and if you haven't seen colors, how do you describe colors? You can't. But if I show you and I say, "Lenny, these are three examples of what pink is and these are three examples of red is," then you're like, "Oh, I get pink and I get red." There are certain things that you just like when you write it's very, very hard to describe it, but if you show specific examples, it's very clear, "Oh, I get it. I get how pink is different than red." But if I try to describe it, it's going to be very hard.

(00:42:35):
So we got into these endless conversations at some point about a year ago where we were saying, "We need high quality, we need high quality." And people are like, "Let's just go and define this thing." We had a bunch of our leaders go and write documents, really long documents in terms of what are the attributes and how do we define those attributes and how do we measure those attributes and how do we enable people to do that? It felt like it's a good thing because we are trying to codify it, but it also felt like it was a very heavy way of solving that problem. Then we just came up with this approach, which is like, "What's great versus not great" and just start classifying it. As you know, it's like modern AI systems are classification systems and we [inaudible 00:43:12]-

Lenny (00:43:12):
Yeah, I was going to say, sounds like reinforcement learning approach here.

Varun Parmar (00:43:14):
Exactly.

Lenny (00:43:14):
Defining cost.

Varun Parmar (00:43:15):
That's right. That's right. I think it's worked decently well. I would say with most things we need to operationalize it and we need to make sure that now we are democratizing it and everybody has access to it and so on and so forth. But I think it's been a good start and now we are sharing this more openly with others in the org.

Lenny (00:43:37):
When I said that, I imagined you... From the outside, you have a very unique culture and approach your product. That's a great example of that. I've never heard of a process like this. What I'm hearing is essentially you're trying to build the muscle within the organization of what is quality. It's like this continued heuristic of, "Okay, I get it." So PMs on the team start to understand in their head what that means.

Varun Parmar (00:43:56):
Right.

Lenny (00:43:57):
Super cool. You also talked about, in the middle part of that sentence, of moving faster and that you track and measure that somehow. Can you talk more about that? Because that's something every product team is always trying to understand. "How do we know if we're going faster, if we're going as fast as we could?" How do you actually do that? How do you measure these things?

Varun Parmar (00:44:13):
The core philosophy there is velocity is more like the game of golf where you're just playing against yourself. It's not like if Lenny and Varun are out at the golf course, it doesn't matter. I'm not competing against you, I'm just competing against myself because that's the only... I'm going to just hit the ball, so it's like how much better can we get? I think our core philosophies around that and what we're trying to do is that on all the product teams, the feature teams that we have, we're just collecting all the information and we are making it available to everyone so that they can actually see what the cycle times are. What we are interested in is from the time that you have an insight, from the time you believe "I can do something unique for my user, for my persona," how long does it take for you to actually deliver that value?

(00:45:04):
We have a product process that we follow, which starts with a P-strat, which is a strategy, and then we go into P0, which is definition of the problem, then we go into P1, which is definition of the solution, and then we go into P2, which is once the solution is shipped, are we hitting the metrics that we originally had defined upfront before we decided to work on this. You have all of these stage gates and then we basically classify everything that we are doing in small, medium, large. You can go in and you can say, "Hey, I thought this was a small thing," and small thing is something you can get it done in less than a month, and so on and so forth. There are 50 other product teams that are shipping these features, and what's the average, what's the variance, what's the median?

(00:45:48):
"Oh, wait a second, actually it seems like I took way more time in the problem definition stage. Let me actually try to go talk to this other product team that actually did it much faster," or "Oh, I actually did it really, really fast, and the reason why I did it fast was because of this. Let me go share this out with the broader team." Usually the product ops function, we call it product excellence internal, sort of product excellence function, is recording some of these things. I would say getting reliable data, and then because we have some things that are going through meetings and there are some things that are going through Slack, we could do better on some of those dimensions, but all of this data is available and we provided it openly and folks can benchmark themselves against that.

Lenny (00:46:34):
So cool. Okay, so you have this P-strat, you called it, document which is kind an initial concept and then it's interesting you use the P0, P1, which is often for bugs, but it's cool that you use it for defining your products. So P-strat is just an idea pitch. P0 is a spec, basically, like a one-pager for the product, and then P1 and P2 are basically getting to "Here's the actual product we're building." And you basically track time per step and map it to, "Here's how large this project should be." Over time you track per person, it sounds like, just like are you matching the benchmarks of how long a small project should take across each step?

Varun Parmar (00:47:13):
Yeah, exactly.

Lenny (00:47:14):
Wow, that is extremely cool. Whatever templates you can share, these things that we can include in the show notes would be awesome.

Varun Parmar (00:47:21):
Yes.

Lenny (00:47:22):
Because people are always looking for just like, "Ah, I want do some of this stuff." If they can just plug and play, the more, the merrier.

Varun Parmar (00:47:28):
Yes.

Lenny (00:47:29):
Shifting a little bit, it sounds like you guys are doing Scrum in some form. Can you just talk about just broadly the product development process? How long you or your sprints, how long do you plan for in the future, in detail specifically just like high level, how does the product development process work?

Varun Parmar (00:47:43):
There are certain things that I learned at Box and that inspired some things that we do at Miro, and there are certain things that we've evolved. One of the things that we've instituted is our roadmap process, so that's sort of the first thing around how the different teams are looking at the things that they're going to work on. We have a rolling six month roadmap, it seems large, but we've got, like I mentioned, a number of enterprise customers. If I've learned one thing that large enterprises is asking for a roadmap review. That tends to be my favorite meeting of sitting down with the enterprise leaders and walking through what we are working on. What we've done is we've tried to architect something which actually allows our customers to get what they're looking for, but at the same time does not remove the agility that is so important for us to deliver value faster.

(00:48:41):
What we do is we have a rolling six month roadmap that gets updated every three months and the first three months of that roadmap, we have a 80% position level, which means that 80% of the things that we claim to be on the roadmap will get done. That's the target. For the next three months, because it's six months, so the first three months is 80%, the next three months is 50%, so we have a much lower level of resolution in the next three months after that. What that allows the product teams to do is actually have flexibility, which is based on what the customers are asking for and based on what the competitive moves are, based on some technology breakthroughs that happen around large language models, they can pivot and they can pivot and move towards that and they won't get penalized either by the customer or internally in terms of doing that. That's what we do and that's all at on the backdrop of an annual strategy that we publish.

(00:49:34):
Every year we publish a strategy white paper that it gets published internally available to every single Mironeer across all functions that clearly articulates the key bets that we want to make. Why do we want to make those bets? What is the expected outcome and how does that ladder up into the overall business outcomes that we are trying to drive from an OKR perspective as well as the overall business strategy that we have. So people take that product strategy, white paper or artifact, and then against that they're building their roadmaps which get updated every three months. Then inside of the teams, we enable teams to be quite autonomous in terms of some of the rituals that they're doing. We want them to obviously embrace best practices. We've got a team of agile coaches that share best practices or are available to help if there's certain specific needs that teams have.

(00:50:31):
Then I think on top of that, there are certain key, I would say, rituals that we do that maybe are unique. For example, we have something called as Miro Connect, which happens every other Friday. Every other Friday, for example, in our Amsterdam office, you can go in there and at 4:00 in the afternoon, 4:00 to 7:00 or 8:00, and sometimes it goes really late, you've got a bunch of product teams sitting around tables and it feels like, "Oh, it's like a pitch or something." And people are coming in, they're having a good time, you've got a drink in your hand, there's maybe some light music playing in the background and you're going from table to table and you have teams that are actually showing all the amazing work that... If done right, it happens once in a while, but if done right, it's magical in terms of the outcomes that you can get.

(00:51:20):
I'll tell you, there was a team that actually was presenting at our Berlin hub and they were saying, "We're working on this feature, and there's an engineer who walks over to that desk and says, 'What are you working on?'" The team describes it, "Oh, we are trying to do something like this." And this engineer had actually worked on that particular problem in their prior life, literally they had implemented this. So he says, "So how are you going to implement this?" And the team, the engineer that's sitting there, says, "This is the approach I'm going to take and it's going to take me three months." He's like, "Oh, would you mind if I go and help you with this?" They're like, "Sure, more the merrier. Go ahead." So this person puts down their beer and says, "Okay, I'm having a good time. Let me just head back to my home." And in the next three or four hours goes and codes the entire thing, makes a poll request.

(00:52:10):
Next day in the morning one of the engineers from this core team that was exhibiting at Miro Connect looks at the poll request, reviews the code and says, "Yes, something that would have taken three months for this core team because they didn't have the expertise literally got done in three hours because there was another engineer that ran into them and said, "I know how this is done. I can actually help you here," and went ahead and did the right thing. We are trying to create these magic moments. It happens once in a while, but we have one success story and I like to tell that in every opportunity that I get. But that's another sort of unique thing that we've done in terms of book-ending things around how we operate here.

Lenny (00:52:50):
That story is like a dream for any PM. Just imagine saving months of work with one conversation. I imagine people were like, "How do we replicate this often?" I love that. With these meetings, just to understand, if their team is in Berlin, let's say, there's a screen there in front of a table and they're talking through a screen, like a video conference?

Varun Parmar (00:53:12):
Yeah. I mean, right now what we've figured out is that it is really hard to do these events over audio-video conferencing and stuff. So generally what happens is that you have an audio-video bridge that's playing, but mostly it's people walking up to the respective teams and then having a live conversation. That's usually how these things are operated. Yeah.

Lenny (00:53:34):
Got it. Okay, so you have six month rolling roadmaps. You have a yearly vision strategy for the company, two week sprints. Is there also a quarterly OKR sort of process or is it-

Varun Parmar (00:53:34):
Yeah.

Lenny (00:53:48):
... those or not? There is, okay.

Varun Parmar (00:53:48):
There is, yeah.

Lenny (00:53:49):
Can you just talk a little bit about how that works?

Varun Parmar (00:53:51):
Yes, yes, yes. At Miro, we practice OKRs and it starts off at the company level, and then those company level OKRs are taken by the AMPED organization. Like we describe, it's the AMPED organization, and then we break it up and I would say we have refined it over the period of time, the two years that I've been at Miro. Early on we were doing OKRs on a quarterly basis, and I would say more recently we've actually evolved to six month KRs. What we found was that six month was the right cadence in terms of giving enough time for teams to basically push forward in executing these KRS and minimizing the "overhead" of doing replan every single quarter. We found that it was much more effective and efficient for the entire organization to do it on a six-month basis. However, we are doing traction on a monthly basis. So every four weeks, as AMPED, we are looking at our KRS for the AMPED organization on a monthly basis doing traction. However, the planning, the targets, are done on a six-month basis.

Lenny (00:55:06):
I love how OKRs could just be anything, could be every six months, could have objectives, could have key results. It's just such a term that just applies to anything that people do with goals, basically.

Varun Parmar (00:55:17):
That's true.

Lenny (00:55:18):
And it works. It's great.

Varun Parmar (00:55:19):
That is so true.

Lenny (00:55:21):
Again, if there's any templates that your team could share of the way you do that stuff, that would be amazing, and we'll include that in the show notes.

Varun Parmar (00:55:27):
Yeah, absolutely. Because I think, as you would expect, we run Miro on Miro, so there's a lot of things that we could share as templates in terms of how we are running things on Miro, not just as OKRs, but in terms of product reviews. We have ways of how we are doing asynchronous reviews combined with synchronous reviews and there's this blended experiences that we have, and so we can definitely share out with the community how we do some of these things.

Lenny (00:55:55):
Awesome. That's a great segue to another question I was going to ask is just what other tools, what's in the stack of the product team's workflow? So Miro, obviously. Maybe talk about what use Miro for, but then what else is in there? What do you use for task management, bug tracking, things like that? Design?

Varun Parmar (00:56:12):
Starting from the bottom-up infrastructure view, so all of our tickets are handled in Jira and we are using some of the newer capabilities in Jira in terms of coming up with roadmaps and coming up with the priorities and stuff. On top of that, all of the specs generally get recorded in Confluence. Having said that, we're actually a big fan of tools like Google Docs as well as Coda that allows us to track our KRs in a pretty effective way. On top of that, obviously we use Miro a lot, I would say for a lot of our things, especially on the product and design side of the team. Generally all of our insights get captured inside of Miro board, so when we are going and conducting user experience interviews and stuff, we will record those and then those recordings get added to a Miro board, so Miro access the content hub or a team hub for a particular project.

(00:57:20):
Once you capture all of those insights, then generally all of the brainstorming and team ideation happens on the Miro board as well, so Miro's actually also used as a tool to facilitate meetings and workshops. Once all of that is synthesized into a set of recommendations and outcomes, so when we go into these product reviews that we were talking about, Lenny, the same Miro board then gets manifested into a set of presentations, so we use Miro for presentations. We've actually made some really amazing updates in terms of our capabilities there and if folks haven't checked them out, I would strongly encourage them. There's a capability called Showtime that basically abstracts out the UI and lets people focus on the content, but do it in a way that it's interactive so everyone that's on the call can have reactions, can share their comments and leave comments while the presentation is happening without actually disrupting any of the flow for the user, so we use that a lot for presentations as well.

(00:58:15):
I would say more recently what we've started to do is that we've started to move some of our synchronous meetings into asynchro view. I talked about this Talktrack feature that we have, and a lot of teams, what they would do is that they would actually send you five minute, 10 minute Talktrack in advance and it's just a link to a Miro board, you click on it and then you just sit back and relax. Then you have this magical experience where you're sitting back and the Miro board is automatically moving because Lenny was recording it like that. Then you have the video play and then you can pause it anytime, you can add in your comments and stuff so that the next time when you meet, instead of actually providing context to everyone, those synchronous sessions are lot more deliberate and focused on driving outcomes or achieving consensus, so people are just focusing on the comments that were added as part of a async product review so that when they meet synchronously they can use that. Miro boards are used for that as well.

(00:59:06):
I would say now a lot of our dashboarding shows up in Miro boards now. We recently released data visualization capabilities around most popular VI tools. At Miro we use Google Looker a lot, so a lot of our dashboards are in Looker, and what you would typically find is that our analyst team and product teams will just grab a link to a Looker dashboard, put it on a Miro board, and it unfolds into a full visualization. Unlike a screen grab, you never have to go update it because right there on the Miro board, it's always updated and you can refresh that, so you basically have this experience where Miro acts as that single source of truth for a lot of the teams across the entire journey of product development where a single Miro board is meeting the needs of multiple use cases there.

Lenny (00:59:51):
Then for the road-mapping, is that in Miro, each team's roadmap, or do you use something like Jira?

Varun Parmar (00:59:57):
Yeah, so I think we've got a couple of tools for road-mapping, and our observation is that while those tools are great for the unique needs that they're solving, we haven't found a universal solution for road-mapping. So there are some teams that use Miro for road-mapping and they would use the Kanban widget in Miro for that. What are they working on? What's coming next? What's in the backlog? But I would say it is a problem that is not completely solved in terms of how do we actually bring these artifacts together at scale.

(01:00:27):
What we are starting to see, and this is actually a unique use case of Miro, is that we actually enable our entire field organization using Talktracks. What happens is that we have our entire roadmap published out as a Miro board for enablement purposes, so that that's a artifact that is approved to be shown to a customer. What you will see is that you'll see five or six recordings in there, and the leader for enterprise has done a five-minute recording on everything they're working on. The leader for platform has done that. The leader for end user experience has done that. The person who's driving some of our AI experience has done that. So you can go in and you can just click on that video and you can meet your needs by using Miro and this capability that we have.

Lenny (01:01:09):
That's awesome. It sounds like each team can basically choose the tools they want to use. There's no standardized, everyone needs to use Jira or Miro for their roadmap. I like that. I like how teams do that often. Maybe one last question around the product org, and then I want to shift a little bit to growth and how Miro grows and things you have learned about growing. Question I always try to get to is how do you think about balancing new bets and innovation with maintenance and just general incremental work? Do you have some sort of philosophy as a product leader broadly, and then maybe at Miro specifically, of just how to balance investments in these two buckets and maybe three buckets, bugs, incremental work, and then just big bet? How do you think about that?

Varun Parmar (01:01:55):
We have some rule of thumbs in terms of how we want to allocate our investments across these buckets. I would say a lot of it, Lenny, actually depends on the state of the team. There are certain teams that have more tech debt than others. There are certain teams that are actually working on some really big zero to one features than other teams, and so I think there is a variance. The standard deviation actually is dependent on which part of the spectrum that you're in, which is are you a team that we believe needs to create the next generation experience on the platform and hence we have to prioritize innovative work or are you the team that's actually so critical to actually meeting our objective around better board performance or any of the other things that we believe are important and hence we need to invest in those critical areas?

(01:02:41):
But I would say in general innovation versus not, varies on a spectrum of anywhere from 60 to 80%. I would say about 20 to 40% of the available capacity at any given time is either getting allocated to architectural initiatives. There's a technology roadmap that our CTO is driving that we believe is extremely important as the platform scales, and now as we have over 50 million people on the platform, so we continuously have to invest in making sure that the platform can scale. There are certain teams that probably have 40 to 50% of their allocation towards that because they're a critical part of the component. There are other teams that are maybe more end user focused and are more UI focused where that allocation is lower. But I think general rule of thumb is 20% is always a given, but it can go as high as 40 to 50%.

Lenny (01:03:30):
On bigger bets and longer-term thinking?

Varun Parmar (01:03:33):
Yeah, 20 to 40% goes on the technology-related initiatives and maintenance and stuff.

Lenny (01:03:38):
Oh, got it. Infrastructure, maintenance, making sure everything's there. Got it.

Varun Parmar (01:03:44):
[inaudible 01:03:44] Exactly, yeah.

Lenny (01:03:44):
Then what about just big, long-term bets that you're not expecting to pay off anytime soon? Do you have a heuristic of just what percentage of, say, total resources you put there?

Varun Parmar (01:03:53):
You've probably seen this, the framework of three horizon, it's quite popular in McKinsey and Harvard [inaudible 01:04:01] school and so on and so forth, is horizon one business, which is the thing that's delivering food on the table. Generally there's about a 70% allocation of resources that we have, give or take. Then there is horizon two, which is an adjacent thing. With the next 12 to 36 months we believe it's material. Usually that tends to be around 20% of the allocation. Then there's horizon three, which is three years out, three to five years, next generation things, and that's about 10% of the ratio. So it's like 70/20/10 across horizon one, two, and three.

Lenny (01:04:30):
Awesome. Any other thoughts along the lines of just how you think about product before we shift? I only have a few questions around the growth story of Miro and what you've learned about growing.

Varun Parmar (01:04:41):
In terms of product leadership and what we believe is the way we want product leaders to be developed and I think it's more of a people philosophy. We have our product leadership which constitutes of all of the folks who are running all of these streams, and I always tell them that you have two personas that you have to think about. Everyone who's on the product leadership team is a product leadership team member. The fundamental thing that you have to do is drive accountability. The number one thing that a product leader on the product leadership team needs to do is drive accountability with others in the product leadership team. The other persona that they have is that they are a stream leader. They're actually responsible for delivering value for the respective persona and respective customers and stuff. So when you put on the persona hat of a stream leader, which is different than the persona or of a product leader, your number one metric, the number one goal that you have, is drive improvement.

(01:05:42):
When you go back and you work with your team, always have the lens are you improving things and whatever you want to improve, but you always have to ask yourself, "Today compared to yesterday, tomorrow compared to today, have I improved things? That's the yardstick you should think about. When you go sit in the product leadership team every Monday afternoon at 1:00 in the afternoon when we meet together, your number one goal is actually to drive accountability around this and are you making sure that we as leaders in the organization are doing the right thing for the company?" I think that's a philosophical construct that I always remind people in terms of what they should be doing. As an example, tomorrow we have calibrations, we have our annual review cycle happening in the company.

Lenny (01:05:42):
Good times. Always a blast.

Varun Parmar (01:06:23):
Yes, exactly, always fun and so critical as a leader, because it sets the tone for everything that you're going to do. In my opening remarks, the only thing I'm going to remind everyone in the room is that "Your number one goal here is to be a product leader and accountability is what you have to write. That's it. Just hold each other as accountable, including myself in terms of making sure that as we go in, that's the key thing." I think once people understand the duality of how they need to operate across those two specific goals, it actually leads to really high-performing teams and teams that actually are able to create somewhat of a magic if they are open and there is trust that has been built in the team.

Lenny (01:07:07):
When you say accountability, what does that look like? Is it pointing out, "Hey, you didn't achieve this thing we were trying to achieve" or "You didn't do a great job leading this meeting"? Is it just direct feedback often or is there some other way you see that manifested, and what do you like to see?

Varun Parmar (01:07:24):
Yeah, I think it's basically practicing feedback in a very open and constructive way and focusing on what is important for the business and not shying away from having some of those observations and conversations, not shying away from them. But it's all in the lens of what is the right thing to do for the business, and if you feel that that one or more members of the leadership team are not living up to what needs to be done, then just voicing it. It's not like you're complaining or anything, it's just like, "I have this perspective. Is this the right perspective or not?" Because actually it ties very well with the overall cultural values that we have.

(01:08:02):
If you do things with the lens that you are being empathetic, then you pose it as a question as opposed to a statement. I think that's one of the things that we practice a lot at Miro is that I believe that I am seeing there are certain things that are happening that it could be just me that I'm not seeing the other things. "But what is it? Can you help me understand? Can you help me figure out that why certain things are happening? Because I might just be missing the perspective." But because you bring it up, and that's part of practicing accountability in an empathetic way, it actually gets the entire team in the right mindset in terms of how they operate.

Lenny (01:08:39):
Has anyone given you some sort of direct feedback recently or pointed out something you didn't do well that held you accountable that you can share?

Varun Parmar (01:08:47):
All the time. Yeah, all the time. When we do our offsites, this is actually a fun thing, is that every offsite that I do with my leadership team, usually there is a one to two hour session where it is feedback to Varun, and I actually do it openly. I will have about eight to 10 people in the room and I will force people to be very honest and I want to show my vulnerabilities to everyone, that I am not perfect and I have lots of areas to improve. Every time people do it, it's interesting that they open up in very amazing ways and I think I love it because it helps me become better. It helps me identify my blind spots. But what it does is, because I do it in an open way, it brings a lot of trust. It brings trust that I do it openly and I'm an open book and they can share whatever they want, not just with me but openly in front of everyone.

Lenny (01:09:43):
Are you willing to share one thing they suggested that they pointed out that they wish you did differently or better?

Varun Parmar (01:09:48):
Yeah, I think in general, finding time with me tends to be a bit of a hard thing, and generally there's always this feedback, which is need more time, maybe more responsiveness over email or Slack or something like that. That's an area that I'm constantly working on and improving, so yeah.

Lenny (01:10:11):
That feels like a cop out. That doesn't feel too painful to hear. I'm like, "Yeah, yeah, I know. I don't have a lot of time. I'm sorry." But I get it, and that comes back to your point about blockers and how important it's to unblock teams because that leads to a lot faster progress.

Varun Parmar (01:10:26):
That's true, that's true.

Lenny (01:10:28):
Okay, so let me shift a little bit to Miro's growth and I only have a few questions here. I know it's getting late on your side so I don't want to keep you too long.

Varun Parmar (01:10:34):
Sure.

Lenny (01:10:35):
The first is something I'm on this constant quest to understand how companies got their first users, and I haven't actually heard the story of how Miro got its first thousand users or customers. I know you weren't there in the early days, but you happen to know how Miro initially grew and got their first thousand users and customers?

Varun Parmar (01:10:53):
I think the fundamental thing there is that we always had user first approach and reaching out to certain communities that were relevant to what was a key part of lighting the fire, if you will, the proverbial way people start to talk about the product. Given the collaborative nature of the product, some of the early adopters invited people who were also early adopters and the flywheel started to work. I've heard that we did a fair amount of content marketing and listing the product on sites like Capterra sort of helped. There was some early investments in terms of SEO and organic growth, so there was a focus there, which was the main source of driving traffic. The top of the funnel came through that.

(01:11:43):
The product teams were very intensely focused on building vital loops as a key mechanism of driving growth, once the traffic came in. Every interaction that actually introduced barrier, they looked at it and they looked at the data and they said, "Let's reduce this barrier. Let's remove this thing so that the product could be effectively embraced." It was an evolution over a period of time. There was also the fact that early on in the journey, some of the features were presented on a trial basis and then later on the model was evolved from a trial basis, time limited to a premium model that further accelerated the growth for the business. I would say those were some of the approaches that were taken to get to the first thousand users or so.

Lenny (01:12:34):
You talked about how Miro grows, where it has this magical loop of "I use Miro to for myself, then I share it with my team in whatever way I'm using it." They're like, "Oh, Miro, this is cool." Then they start using it and then they share it with people that they want to work with, and it creates this loop of growth." I imagine that's how Miro mostly grew initially and continues to grow. Is there anything surprising or unintuitive about how Miro grows that is beyond that? I imagine sales is a part of it and we can talk about that, but is there anything else that is interesting that is worth mentioning?

Varun Parmar (01:13:07):
No, I think that's the key of the growth. I think there are specific use cases where they are uniquely sort of geared towards inviting a lot of new people. For example, Miro is loved as a workshopping tool, and so generally one person is using Miro, but they invite 10, 15, 20, 50, 200, 300 people to that workshop. There are specific use cases where people get introduced to the product and then go and sign up for it and then start to use it for that use case or other use cases. I think the other accelerant in all of this is the templates that we have, in particular the role that Miroverse plays in all of this.

(01:13:49):
Just to give you an example here, there was a template which was created around FIFA World Cup, so there was a FIFA World Cup diagram. Cornelius, he's the founder and managing director of a Canadian strategic service design consultancy firm. He created this Miroverse template and it had over 100,000 views and about 15,000 copies were made of the single template. Given the popularity of all of this, it actually got indexed by Google. When you went in the search, you actually saw the Miroverse FIFA template show up when you were trying to search for FIFA World Cup, and that was another sort of acquisition channel top of funnel that actually drew a lot of users to it. So I think I would say the Miroverse is also a key accelerant to this.

Lenny (01:14:45):
If you had to think about the pie chart of how Miro grows, what percentage roughly would you say is word of mouth, organic, versus what you just described, which is essentially a CO versus sales, outbound sales? How do you think about that? Is there a way to model that simply?

Varun Parmar (01:15:02):
Without getting into specific numbers and stuff, I would say fundamentally Miro is a product-led growth company and product channels are one of the highest contributors for growth of users. As the business has evolved to serve the needs of some of the largest corporations in the world, the enterprise segment and the enterprise persona when they're trying to provision Miro for tens of thousands of users who then go conduct hundreds of thousands of workshops on Miro that invite millions of users on the platform, is a key part of the flywheel that we are seeing. I would say product channels are probably very strong and increasingly enterprise is a key part of that acceleration.

Lenny (01:15:53):
A great segue to our final question, which is the idea that you started a product growth, sounds like clearly it's a big part of growth today, but as every product growth company does eventually you have a large sales team, I imagine, what have you learned as a product leader working with sales, especially at a product growth company about how to make that relationship work and have a product work effectively with a sales org?

Varun Parmar (01:16:15):
There are a few learnings and I would say maybe this is one area where we are working on how we could be doing better in terms of bringing ourselves closer to our high-touch and bringing high-touch closer to self-serve, in terms of how we operate overall. It's a lot of hard work, I would say first of all, basically, to bring both of these organizations together and you have to be very deliberate around the points of intersection and you have to make sure that these organizations don't consider themselves as competition. It's one product, one company, just two channels of how we are serving our customers. There's some things that we've done which is have the product marketing team that basically works across both of these functions and make sure that they are bridging what we are hearing from the sales organization in terms of what directly customers need on the enterprise side, and then what do we need on the self-serve side.

(01:17:23):
There's a full process in terms of how the handoff happens across the maturity of the account. It can start as a self-serve, it drives adoption, and once there's adoption, there's a hand raiser that happens and then there's a sales rep that gets engaged and you go through the qualification process and then you have an opportunity to expand the account. We've over the years sort of architected and built the entire funnel and what the process is, and that's also sort of a key part of how all of this operates. But like I said, I think there are a few areas where we could further streamline how we operate and think of it as one single unit.

Lenny (01:18:05):
I imagine that is true for every company out there.

Varun Parmar (01:18:07):
Yes.

Lenny (01:18:09):
One maybe final question before we get to our very exciting lightning round. What are some features that people could look forward to that are coming with Miro?

Varun Parmar (01:18:19):
We recently, about a month ago, announced Miro AI, the backdrop of all the amazing work that's happening around generative AI and large language models and stuff. I think it was really, really exciting to see all of the community enthusiasm around the use cases that we launch. So we're going to be taking it across the finish line and doing a general availability in the coming weeks and months. I think that's one big thing and we'll be adding more capabilities there. Just today we actually announced a bunch of really deep enhancements and updates around how Miro can be used for team rituals and agile practices. Now you can actually do retrospectives in Miro where you can have a private mode where while Lenny's typing his feedback during retrospective, nobody else can see it and then one click you can reveal it. I just saw some of the results of the feedback and it was rated as the number one feature people saw.

(01:19:14):
There's also some deeper integrations in terms of bringing an entire program board from Jira to start to do dependency mapping inside of Miro in a fun and collaborative way, to use this dependency mapping along with program board to start to do program increment planning, which is essentially scrum of scrums or big room planning that's happening. There's some really amazing capabilities that we've added there, which is on the backdrop of some of the updates we've made in terms of estimation of sprint story points and so on and so forth. Now there's a whole plethora of capabilities and apps that are available as part of the platform that allow you to have your entire team conduct your team rituals in Miro and you can automate certain things, you can streamline things, you can do certain things in async and then do the rest in synchronous ways, so I think that's been a big update as well.

Lenny (01:20:12):
Amazing. With that, we've reached our very exciting lightning round. I've got six questions for you. Are you ready?

Varun Parmar (01:20:19):
Yes.

Lenny (01:20:20):
All right, let's do it. What are two or three books that you have recommended most to other people?

Varun Parmar (01:20:26):
One is, I love this, When Breath Becomes Air by Paul Kalanithi. It's one of those really emotional books that at the end of it, you might have tears in your eyes, but really, really amazing. We talked about Frank Slootman's Amp It Up, and then Satya Nadella's Hit Refresh. I think philosophically some of the things that we talked about today are inspirations that I found in some of these books.

Lenny (01:20:49):
What's a recent favorite movie or TV show?

Varun Parmar (01:20:52):
Ted Lasso. I don't know if it's a recent one or not, but something-

Lenny (01:20:55):
It's a new season.

Varun Parmar (01:20:57):
Yeah, I've enjoyed a lot. I think it's a very positive and uplifting message. I think the performance is huge. It's humorous, the characters are well-developed, so I think overall it's a treat, at least for, me to watch.

Lenny (01:21:13):
What's a favorite interview question you like to ask?

Varun Parmar (01:21:16):
I actually ask a math problem. For those of you who interviewed with me, I have this math problem, which is based on how Adobe created its first Creative Suite bundle. I was actually part of the team that came up with the pricing and packaging for the first Creative Suite post-acquisition of Macromedia. It's a math problem that allows you very quickly to figure out people in terms of their problem-solving skills. Usually I give that problem to people. I've given it to, I don't know, 700, 800 people, so I now have a very, very well established standard distribution of how long it takes for people, where do they get stuck and where they've gotten stuck, for those people I've hired, what evidence do I have in terms of using that as a framework in terms of them being able to solve things? So that's my favorite question.

Lenny (01:22:08):
So you're saying you've mapped back people that have done a certain way on the problem with their success and you've kind of found that it's a good signal of their performance?

Varun Parmar (01:22:17):
Yes. Not directly, but yes, correlation and stuff.

Lenny (01:22:21):
That's amazing. That's one of the biggest problems with interviewing. You think you're asking all these amazing questions and it's such a good signal, you have no idea. No one goes back and is like, "Oh, this person sucked. This person didn't... " That's really cool to get that much data on that one question. Two more questions for you. What's something relatively minor that you've changed in how you do product development that has had a tremendous impact on your team's ability to execute?

Varun Parmar (01:22:44):
We talked about some of that, sort of removing the roadblocks. I think having this motto of great customer value faster with high quality, just the simplicity of that and it's actually part of our evaluation rubric, it's part of how we measure ourselves and stuff. So I think just coming up with these simple concepts that you can rally the organization around, and I think it's still a work in progress, but something that I believe is leading to positive outcomes.

Lenny (01:23:07):
Final question. What's your favorite Miro template?

Varun Parmar (01:23:10):
It's the FIFA World Cup actually. I am so fascinated with what was done. Yeah, it's the latest one, but I think there's a bunch of them in terms of retros as well, and I think... like your template as well.

Lenny (01:23:21):
Amazing. We will link to all of those. Varun, this was amazing. Everything I expected and more, your team is as interesting and unique as I thought, and I am excited for people to learn from you and we're going to share a lot of links alongside this episode in the show notes. Two final questions, where can folks find you online if they want to reach out and learn more, and how can listeners be useful to you?

Varun Parmar (01:23:43):
Thank you, Lenny. It was a lot of fun. I enjoyed our interaction. You folks can find me online on LinkedIn. I think that's probably the best way to connect with me. I think in terms of one or two things I can ask everyone is that, one is if you are an existing Miro user and you use the product for something interesting, I highly encourage you to contribute it as a template as part of Miroverse. There's a lot of folks who use that and we would love for you to contribute there. The second thing is, I know a lot of product development teams, PMs and designers are big fans of you, Lenny, so those are also the users that use Miro. If there's anything we could do to make the product better, if there's things that you feel like we can expand the platform into, we would love to hear from you and just reach out to me directly over LinkedIn, direct message or connect with me there and yeah, and let us know. We're here to serve.

Lenny (01:24:40):
Amazing. Varun, thank you again for being here.

Varun Parmar (01:24:43):
Thanks, Lenny. Awesome.

Lenny (01:24:45):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

