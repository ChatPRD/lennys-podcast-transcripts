---
guest: Julia Schottenstein
title: M&A, competition, pricing, and investing | Julia Schottenstein (dbt Labs)
youtube_url: https://www.youtube.com/watch?v=y9hmrMBRPDI
video_id: y9hmrMBRPDI
description: 'Julia Schottenstein is a product lead at dbt Labs, a data transformation
  company, and an active angel investor in data and infrastructure startups. She first
  got excited about dbt in 2019 when...

  '
duration_seconds: 3651.0
duration: '1:00:51'
view_count: 3577
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- metrics
- prioritization
- analytics
- conversion
- pricing
- revenue
- culture
- management
- strategy
- vision
- mission
- positioning
- competition
---

# M&A, competition, pricing, and investing | Julia Schottenstein (dbt Labs)

## Transcript

Julia Schottenstein (00:00:00):
M&A is always about creating plan Bs. And the way I would think about it is for any one company, there's only ever two to three buyers that find what you're building to be extremely strategic. And the strategy that I would do in how do you get noticed is I would figure out the area that you bring a competitive advantage. And I would inflict pain on that potential buyer. Make it impossible for them to not notice you because that's when they're going to have their ears perk up and say, "Well, what's going on with this company?"

(00:00:33):
The really important piece here is you want to do that in a way that's still friendly and open. I see a lot of founders get this wrong and they prematurely will shut down a conversation or they won't talk to an incumbent or a potential future buyer because they take too competitive of a stance. But that's a mistake because M&A is all about creating plan Bs and you don't want to shut that door down prematurely because you don't know if you can really go the distance and be an independent company. So you want to have optionality.

Lenny (00:01:04):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard one experiences building and growing today's most successful products. Today my guest is Julia Schottenstein. Julia is a product leader at dbt Labs where she leads the dbt Cloud product. She's also the co-host of the dbt Labs podcast called Analytics Engineering Podcast, a show about data trends that impact analytics engineers work. As you'll hear in this episode, Julia actually led the acquisition of a startup that I'm an investor in called Transform from the side of dbt Labs.

(00:01:37):
And in our conversation, we dig into the M&A process and get into a bunch of advice for how to improve your odds of having a good outcome and just approaching M&A broadly. We also dig into the story of dbt, which is one of the most successful startups out there that you probably don't know about. And we talked about what they did right to get to where they are now. We also cover how to best think about competition, a bunch of frameworks for thinking about product and advice on how to approach pricing and also open source. Enjoy this episode with Julia Schottenstein after a short word from our sponsors.

(00:02:11):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate your growth. Thousands of fast-growing companies like Gusto, Calm, Quora and Modern Treasury Trust, Vanta to help build scale, manage, and demonstrate their security and compliance programs and get ready for audits in weeks, not months. By offering the most in-demand security and privacy frameworks such as SOC 2, ISO 27001, GDPR, HIPAA, and many more. Vanta helps companies obtain the reports they need to accelerate growth, build efficient compliance processes, mitigate risks to their businesses, and build trust with external stakeholders. Over 5,000 best scoring companies use Vanta to automate up to 90% of the work involved with SOC 2 and these other frameworks. For a limited time Lenny's podcast listeners get $1,000 off Vanta. Go to vanta.com/lenny, to learn more and to claim your discounts Get started today.

(00:03:10):
This episode is brought to you by Superhuman. How much time do you spend in email each day? How about your team? You may not realize this, but your email tools are wasting your time. Superhuman is blazingly fast. Email for high performing teams built to work with Gmail and Outlook. Teams who use Superhuman spend half the time in their inboxes respond to twice the number of emails and save over four hours a week. That's over a month of save time per year. With Superhuman, you can split your inbox into streams for VIPs, team members and emails from your favorite products to reduce context switching. And make sure you never miss an important email.

(00:03:48):
You can start reminders if you don't hear back so that you can follow up and never drop the ball on an email thread. You can also work faster than ever before with powerful AI features like writing, editing, summarizing and even translating. Join the ranks of the most productive teams and unleash the power of Superhuman. Try one month free at superhuman.com/lenny. That's superhuman.com/lenny.

(00:04:15):
Julia, welcome to the podcast.

Julia Schottenstein (00:04:17):
Super excited to be here.

Lenny (00:04:19):
So you have a really interesting career path in that you went from VC into product management. Usually it's the other way around. Usually PMs become VCs and it's right to see this version of it. So I wanted to start with just a question of just how did that come to be?

Julia Schottenstein (00:04:34):
I do have an unusual background, but it doesn't surprise me that people who are interested in product are also interested in investing and vice versa. For me, I've always had three interests broadly and that's an interest in business, an interest in technology and an interest in markets. And I get to express those interests both in investing and in product, but just with different weights. So in product you go a lot deeper on the tech and markets is less of a focus, but you still get to do all three. So I have a unusual background and I used to be a professional investor at NEA. Spent all my time investing in early stage startups that built for technical audiences. So think dev tools, infra data companies.

(00:05:22):
And in 2019 I first discovered dbt, which was an open source data transformation framework. And I got really very, very excited about dbt because when I talked to people that were using it, the way that they described their experience on dbt was like unlike anything I had heard before. It was much more of an identity for them than just a tool that they were using to get their job done. And that really struck me. And as I thought about what was happening in the market, there was a lot going on in 2019. The markets were changing quite a bit. Cloud data warehouses were starting to explode. This was the year where Snowflake went from a 4 billion company to a 12 billion company. And I thought to myself, if dbt worked, it could work in a really extraordinary way. And I naturally tried to spend all my time getting close to Tristan, who's the CEO and founder and I wanted to invest.

Lenny (00:06:24):
Okay. So at this point you're a spec at NEA, you're trying to invest in dbt and okay, keep going.

Julia Schottenstein (00:06:29):
Yeah. So I was very, very excited. I thought if this worked, it could work in a really extraordinary way and I spent all my time trying to get Tristan to like me so that I could invest in the company. And then in 2020, I finally got the call that I was waiting for. Tristan said, "We're going to raise some money." He had a term sheet from a firm that he liked. It was a good venture fund, but he also liked me and he wanted to give me a shot and I was super excited to get that message because this is my chance. And unfortunately I ended up losing that deal to Sequoia. It's a formidable partner.

Lenny (00:07:04):
Reasonable loss.

Julia Schottenstein (00:07:05):
I was just so convicted that if was going to be a special company that I asked to even put my personal money in and I asked to put a very irresponsible, irrational amount, nearly like 20% of my liquid net worth into dbt because I was so convinced that this was special. And sometimes when deals don't work out as an investor, you can create this narrative in your head like, "Good, I dodged a bullet or better off without them or screw them." But for me that was quite the opposite with dbt. I really felt like dbt was this runaway train and it was special and I wanted to jump on board. So a few months later I ended up calling Tristan and asked him if I could be a part of the company that built the product that I thought was so special. So that was my unique path into product and to dbt.

Lenny (00:08:02):
So you invested in dbt and then an opportunity opened up where you ended up working there?

Julia Schottenstein (00:08:08):
No, I think if I was able to invest I wouldn't be here. So I got no, the board ended up vetoing my personal investment, but it's okay because I ended up dedicating all of my personal time to building the company.

Lenny (00:08:23):
Awesome. Okay. So something you touched on there that was really interesting of what you saw about dbt that was so interesting and I think this is maybe a broader question of just in your time investing and finding a company like dbt early, what have you learned about just picking well, finding companies early especially? What are signs in your experience of just that this is going to be something really interesting that you might want to join? And this is more for people listening that are thinking about joining a company early on. What do you think they should look for?

Julia Schottenstein (00:08:52):
So the way I would look at joining an early stage company would be the same way I would evaluate investing in one. So there are four things that I care about when I'm looking at really early stage companies and it's people, market, product and distribution. And I'll touch on each of those four to say a little bit more about what specifically I'm looking at. So people, this is really the CEO, the founder of the company put simply do you trust this person to lead. And for me, Tristan had this really rare ability to paint a very compelling future of the industry and how dbt was going to be a part of making that vision a reality. But he also was really, really detailed in the day-to-day work of the analytics engineering work. And it was that range in scale that made me feel like this is a founder that's very rare and compelling.

(00:09:42):
The next is markets. We touched on it a little bit, but what I'm looking for in markets it's like is it growing? Is there space for new entrant to make its mark? And when it came to dbt, it was an explosive time in cloud data warehouses and it was that chaos that was really the opportunity for dbt because they created some orderliness and structure to the way that people worked with their data in the cloud data warehouse. So that was very compelling. The next is product. Everyone who's listening hopefully either is interested in products or has a product background. So I won't say too much there, but can you talk to users or potential customers, are they building something that's really special, unique? Can you hear that, spark that enthusiasm and figure out if this is going to be special.

(00:10:31):
And then the last, I think this is more important arguably than if they have a good product but is distribution, do they have an advantage on how are they going to get to market because that's really, really hard? And think about how they think about their competitive advantage on either the ecosystem or distribution and how they're going to ultimately sell the product. You're not going to get a 10 out of 10 on all four dimensions. So when you're joining a company, you also have the benefit of dedicating your time. So try to think if they're weaker on one dimension, what is it that you bring to the table or what are you special at that could potentially de-risk the success of the company

Lenny (00:11:11):
In terms of spark with a product. Right now on product market fit, now how do you know if you have product market fit? And a lot of it often comes down to there's a emotional reaction from someone you're talking to about the product you're building. There's like, "Holy shit, I want this now." Is there anything even more specific you've seen of just what is a sign that this, there's a spark that people are just really enthused? You talked about people made dbt part of their identity. Is there anything else there?

Julia Schottenstein (00:11:36):
Yeah. It's can they not stop talking about it and that's the chatter about a product, they want to share it with their teammates or to other people at different companies. That just top of mind love and wanting to share what they've found with others is really a great sign that you're onto something. And then that spark will help do a lot of the work on how do you get to market because your evangelists are really your users of people that love what you're building.

Lenny (00:12:06):
What about in terms of the distribution bucket? What are some examples of just really important, I don't know, unique or effective distribution strategies or I don't know, unfair advantages you've seen maybe with dbt, maybe other companies? What are some examples of that?

Julia Schottenstein (00:12:20):
So dbt had an ecosystem advantage and they were open source and this helped really dramatically for lots of people to have low barrier friction to just try it out and spread organically. They first got started with very horizontal. People could just get started without ever even talking to sales and think that was a competitive advantage. But not all companies need to be product led. Some companies are enterprise top-down sales. So in those situations think about does the team really know how to land a complex enterprise sale? Do they have a background in that particular space? Do they have a network of connections? Can be different depending on what the company is selling, but you either want to see a company that's really strong at enterprise or really strong at the bottoms up.

Lenny (00:13:11):
Okay, cool. So I want to shift a bit to talking about an area that you have a lot of experience in which a lot of people are also really interested in right now, which is M&A. I've invested in a lot of companies and maybe, I don't know, once a month I'm getting an email from a startup I've been investor in. There's just like, we're looking at maybe selling the company, things aren't working out the way we were hoping. And you've been on I think maybe all sides of the table of M&A transactions, including I think you led the acquisition of a company... I was an investor in the dbt acquired that I think is public company called Transform. So my question is just for founders who are currently thinking about M&A meaning acquisition essentially. What's your best advice for them for how to be most successful in M&A outcome for themselves?

Julia Schottenstein (00:13:57):
When it comes to acquisitions, the time to start thinking about an M&A strategy is hopefully when you don't need one. And the best strategy that I could give a founder is to have a really strong offense in building their company. And when founders start their businesses, they don't usually set out to start a company to sell it to another business. They start it to be an enduring independent standalone company. And if you have that path, then you'll have the upper hand in absolutely every single M&A conversation because you have a viable alternative, which is do nothing, stay the course, you don't have to sell. But of course that's not the case for most companies. Most companies don't have a viable path to being an independent company forever. So they have to think about M&A. So M&A is always about creating plan Bs.

(00:14:49):
And the way I would think about it is for any one company, there's only ever two to three buyers that find what you're building to be extremely strategic. And the strategy that I would do and how do you get noticed is I would figure out the area that you bring a competitive advantage and I would inflict pain on that potential buyer. Make it impossible for them to not notice you because that's when they're going to have their ears perk up and say, "Well, what's going on with this company?" We just bought this company Transform. They are playing a really good playbook here.

(00:15:25):
And the really important piece here is you want to do that in a way that's still friendly and open. I see a lot of founders get this wrong and they prematurely will shut down a conversation or they won't talk to an incumbent or a potential future buyer because they take too competitive of a stance. But that's a mistake because M&A is all about creating plan Bs and you don't want to shut that door down prematurely because you don't know if you can really go the distance and be an independent company. So you want to have optionality.

Lenny (00:15:54):
I love this term with pain on your potential acquirers. What are some examples of that? Who's done that well or what's an example of that interaction?

Julia Schottenstein (00:16:03):
Yeah. I mean I can share the transform stories of a company we just acquired, we announced it in February. So dbt Labs, we build transformations, that's our main product. And we were venturing into a new product area that we call the semantic layer. And to describe what that is quickly, it's allowing companies to define their business metrics and so that whenever anyone queries it, we always serve back consistent data on those business metrics and transform. They were a pure play company only in this metrics layer, semantic layer. And they had a really strong product.

(00:16:41):
They had figured out some of the technical challenges and they had solved it early on. They had the benefit of having worked at Airbnb, which and Airbnb in the data world is famous for having a really successful semantic layer metrics layer called Minerva. And what we had at dbt Labs is really good distribution and ecosystem, but we were a little behind in bringing a product to market and we felt that pressure from Transform because they were doing such a great job at being vocal and loud about how their semantic layer solves these really hard technical problems.

(00:17:20):
But they didn't have any distribution. So that was really tough for them and they were putting pressure, but they were still positioning their company as a partner to us because they wanted our community to be excited about what they were building and hopefully lure them over to use their product. So because they had positioned themselves as a friendly partner when really we were trying to compete for this similar use case, when it came time to do an acquisition, we were really excited because we knew their product was good and they had already done a lot of the work to make integrating with dbt possible and that helps us post acquisition do the integration much more easily.

Lenny (00:18:01):
How do you just think about either as a startup or even an incumbent about how to think about competition, how much emphasis, how much energy to put into thinking what competitors are doing and just how that informs your strategy?

Julia Schottenstein (00:18:15):
So we recently codified our philosophy when it comes to competition. And I'll give Nick Handel the founder of Transform who led this exercise at dbt Labs. But we really have three pillars when it comes to competition. So the first is hold true to our vision. We're really excited about the path and the journey that we're going on at dbt Labs and we don't want the distraction. So occasionally you'll have competitors maybe throw shade or throw stones, but most of that is just noise. If you have a lot of conviction that you're going in the right journey, you want to just keep your eyes straight ahead and run your best race and not be too distracted by what maybe some critics are saying.

(00:19:00):
The second philosophy we have is really a grow the pie philosophy. So we want to work with our partners in our ecosystem to make the opportunity set even larger and we see that today. We mostly serve reporting and BI use cases, we're seeing lots of companies start to operationalize their data. Now with this big wave of ML, clean Transform data assets are being used to train machine learning models so that the pie continues to grow. Let's focus on that as our target and work with people to make the opportunity set really attractive and not try to slice it up too thinly.

(00:19:37):
And then the last one is we want to lean into our strengths. So we have an ambition to be a platform company and we know what we're good at, but we also want to leave space for our ecosystem to offer solutions to our users that help them out. And we really want to foster an ecosystem where we can partner with lots of companies in the modern data stack. And generally speaking, when it comes to competition, we take a really long-term view and there are a few areas that we do want to hold our ground and that's in our transformation standard as well as our semantic standard because we believe those two are better served together for the user's sake. But for everything else, we really feel like we can work with our ecosystem and accomplish what we want to accomplish and also help them accomplish their goals too.

Lenny (00:20:27):
This might be a good time to just chat about dbt and the success the company has had. So many startups have tried to become a standard default layer of what's now called the modern data stack. And I don't know any startup doesn't use dbt or planning to use dbt. It's just a incredibly rare success story somewhere to snowflake where it's just like it's the default for building large data startups and most startups these days work with a lot of data. So my question is just like what do you think dbt did most right to win in this and continue to win?

Julia Schottenstein (00:21:01):
So I think dbt did a lot of things right, but I'll point out too that really stick out to me. And the first is just power and simplicity and the second is a commitment to being open. And I'll touch on what I mean by those two things. So when dbt was first getting started, you would hear a lot from companies, I don't understand, what's so special about dbt? We have a SQL templating tool at our company, we built one in-house. Like this is really straightforward and simple and it's true like dbt is really simple, but that is the power of it.

(00:21:37):
So our founders, Tristan, Drew and Connor, they had a belief that the people who do data analysis work, that really work closely with their business stakeholders should also be the ones to contribute to creating clean data assets in production because that data prep work is a necessary prerequisite for any analysis that you do. So dbt was really this belief that if you know SQL, we want to invite you to do these workflows that were traditionally held by data engineers but you had to earn that. So dbt has this nice framework where it's harder to mess up, keeps data quality really high, but it is pretty simple to get started and learn and learn. And that was really the unlock in the industry. We were definitely solving a pain point at the right time.

(00:22:26):
And then the second thing is this commitment to being open. So dbt is open source and that's the main guts of dbt where you write your business logic and it helps in a number of ways. Specifically it helps with flywheel, keep the flywheel running and also with network effects. And I'll explain what that looks like. So dbt is really easy to get started with at your company with reduced friction. We're building a product that people, so they talk about it, they want to share it both at their organization and with other companies. Other companies get started with dbt again with reduced friction.

(00:23:05):
We now get to see this really diverse set of use cases for dbt across company sizes, across industries and it allows us to build a truly horizontal company. As our company grows, we get to invest back into our community and our product and the flywheel begins to spin faster. And then meanwhile we have a really large user base. So we have 20,000 companies using dbt every single week and that attracts partners to want to build for dbt and so they share best practices, build workflows, and now if you're a company and you've standardized on dbt, you've really unlocked an integrated modern data ecosystem that wasn't available for you before. So that has a flywheel and also benefits everyone that decides to be on the standard. So it's those two really important trends that made dbt so powerful today.

Lenny (00:24:02):
So what I'm hearing there is essentially the product was right for what people needed to solve. There's also a product led component, open source, free self-serve piece that people adopted, used and started working and then scaled and started paying for it. And then there's an alignment of the vision of where this was going and how it fit with how people wanted this to work for them. Is there anything else? Because a lot of startups do that and that all sounds really smart and good, but a lot of startups try to do those things and no one cares. Maybe their product isn't necessarily what people are looking for, maybe they don't get the right distribution. I don't know. Is there anything else that you think they did really well that helped them kickstart this to even be a thing? Is it timing that was really great? Is it specific influencers early on?

Julia Schottenstein (00:24:48):
Yeah. I think timing was really important with the success of dbt. That they were there when the cloud data warehouses were really exploding and growing in an enormous way. And dbt Labs started as Fishtown Analytics, a consulting firm. So they worked really, really closely and hands-on with all of their consulting partners to get the pain point and really solve firsthand challenges that they saw. I think that combination of being at the right place at the right time and also getting to work really closely with people's day-to-day problems created a really special experience.

Lenny (00:25:29):
I didn't know that. That's a really important element of the story is basically they were focused... How long did they do that Fishtown Analytics consultancy?

Julia Schottenstein (00:25:38):
Board consulting part of the business was almost two years.

Lenny (00:25:42):
Okay. So they basically spent two years solving this problem basically manually for people, and that's such a great way to understand real pain and figure out how to solve it.

Julia Schottenstein (00:25:53):
Totally.

Lenny (00:25:54):
Awesome. Okay, so that's a really interesting insight. Just spend a few years. It sounds like it was almost manually helping people transform their data using whatever tools already existed.

Julia Schottenstein (00:26:05):
Yeah. Well, they were building dbt and using dbt to help them do their jobs better and supporting their clients. And whenever they encountered paper cuts or friction or the workflow was taking longer than they expected, they would build that into dbt. And that really matured the experience of the product because the people who were building it, the founders were also day-to-day working with these customers or clients that had pain points.

Lenny (00:26:36):
That reminds me of a story you told me about how you made your eng team do some manual work of an algorithm involved in transformation. Can you share that?

Julia Schottenstein (00:26:47):
Okay. So I'm going to preface this story by sharing that I'm a huge math nerd and one of my favorite books on logic is called Girdle Escher Bach. And in this book there's a fun scene where there's an ant farm that bands together to do the work of a computer flipping bits from zero to one to solve logic gates. So this chapter of that book was really the inspiration for an exercise that I ran my team through. So about a year ago we were doing a big zero to one new project at dbt Labs and we were going to change the algorithm for how we built customers data transformation graphs. And I needed a way for the team to really internalize all of the changes that we were going to be making and I needed them to own it because otherwise they wouldn't be able to anticipate all of the edge cases and it wouldn't be quite as durable. You couldn't copy paste the algorithm.

(00:27:41):
So I showed up to a team offsite with a spool of rope and sticky notes and I think my team looked at me crazy, went with two heads when I started to tie people up to create a graph. So each note of the graph was an engineer and the rope was the edges of the graph to connect them. And then we worked through the new algorithm extremely slowly, step by step. And it was a way that you couldn't leave that exercise without knowing exactly what was going on because everyone had a role to play.

(00:28:16):
So I think a lot of times when you're starting something new, you get into a situation where a few people really understand it and they're running way ahead of the rest of the pack. But I needed a way for the whole team to go along for the journey. So I'm constantly trying to create these important moments or memorable moments for the team so that it's centered around our mission and they can have the ownership of taking the project and making it successful. So it was perhaps a overly creative or kooky way to spend the day, but it was really successful.

Lenny (00:28:49):
What was the actual algorithm you were trying to implement?

Julia Schottenstein (00:28:53):
We were trying to figure out how to make flipping the way that we run people's dags from an imperative way to a declarative way. So instead of running things left to when data arrived in your warehouse. You think about it as reverse, like what would need to happen to make your data SLAs be materialized in time.

Lenny (00:29:16):
Awesome. And sounds like the team found that valuable.

Julia Schottenstein (00:29:20):
Yeah.

Lenny (00:29:20):
Okay. Reminds me of a clip from this last season of Ted Lasso where they have used red strings and I won't get into it, but if you've seen it you will know what I'm talking about. I want to come back to your chatting about open source versus not open source. So some part of dbt was is open source and some isn't. I'm curious how the team decides what is open source and what should be open source, what isn't open source and what to charge for?

Julia Schottenstein (00:29:50):
We think about dbt open source. It's really the guts of the data transformation. It's where you describe your business logic. And then on the cloud side we build proprietary software that supercharges the development life cycle and the productionization of dbt at scale. So what we think about as leaving for our cloud offering is we deal with state, so stateful interactions and also any cross team or structural collaboration. We want to reserve that for our proprietary offering. And I think it's really important to have that distinction of what do you believe should be open source or what is the open standard that really matters? And ecosystem to us is really important. So it's important that that remains open source, but then we want to supercharge that experience with an open core model and build proprietary software that makes people much more successful at using dbt.

Lenny (00:30:48):
Today's episode is brought to you by AssemblyAI. If you're looking to build AI powered features in your audio and video products, then you need to know about AssemblyAI, which makes it easy to transcribe and understand speech at scale. What I love about AssemblyAI is you can use their simple API to access the latest AI breakthroughs from top tier research labs. Product team that startups and enterprises are using AssemblyAI to automatically transcribe and summarize phone calls and virtual meetings, detect topics in podcasts, pinpoint when sensitive content spoken and lots more. All of AssemblyAI's models which are accessed through their API are production ready.

(00:31:26):
So many PMs I know are considering or already building with AI and AssemblyAI is the fastest way to build with AI for audio use cases. Now's the time to check out AssemblyAI, which makes it easy to bring the highest accuracy transcription plus valuable insights to your customers. Just like Spotify, CallRail and writer do for theirs. Visit assemblyai.com/lenny to try their API for free and start testing their models with their no code playground. That's assemblyai.com/lenny. I know you also spent a lot of time thinking about pricing and willingness to pay and things along those lines.

(00:32:03):
Is there anything you could share about which is what you've learned about how to think about pricing for a tool like this or even in general?

Julia Schottenstein (00:32:09):
Pricing and willingness to pay is such a hard conversation and lots of startups don't do this early enough in their company journey. Likely a side effect of zero interest rates where investors were happy funding GitHub stars and usage and companies never thought about how am I going to make revenue or make money, which is it's important. So for us at dbt Labs, I don't claim to be perfect at it, but we're trying to get a better muscle around it. And I always think about Madhavan who wrote this book Pricing Innovation. I know you've had him on the show before, but he shares that you don't get to decide if you're going to have a pricing or willingness to pay a conversation. You only get to decide what. So it's much better to have that conversation before you build the product than have it when your sales team's trying to sell something and people aren't excited about what you've built, aren't willing to pay for it.

(00:33:04):
And at dbt Labs we have this value, it's one of our core values that says we are more concerned with value creation than value capture. And we really mean this. When we talk about what is the value of dbt Labs to our customers, they often talk about how it's either 20 to 35% as valuable as what they spend on their cloud data warehouse. But what we charge our customers is a very small fraction of that 20 to 35% and that's by design. And last year we did our first ever pricing change in the company history and you learn a tremendous amount when you have that event because you get to test the price elasticity by of your customers.

(00:33:49):
And it's so important to learn that lesson while the company is still smaller or the stakes are lower because pricing just is always evolving. It's not a fixed thing, it gets more complex over time. So we have to think about it quite a bit because my team builds proprietary software for dbt cloud and when we lose a deal we most often lose it to dbt open source and we like it that way. We're happy to lose to ourselves, but we have to really think very deeply about what are people willing to pay for and what moves the needle for them and focus on that.

Lenny (00:34:26):
I'm so curious what that pricing process was like to figure out what to change. Is there anything you could share about just what that was for you or what are some just surprises that came out of that process or just like, "Wow, we didn't expect that in these conversations?"

Julia Schottenstein (00:34:42):
It's really like an all hands on deck conversation. Pricing is so cross-cutting because it's a finance discussion as well. You're modeling out things in spreadsheets and figuring out how that might impact the business. But you can't just solve these problems in spreadsheets. You have to go talk to customers, test the waters, understand where people's appetites are and sussing that out is really hard. And then of course there's a product piece to it too where you have to affect it and communicate it as well. So it was very cross-cutting. We learned a lot. We track our conversion rates really carefully. We track our turn rates very carefully and I think largely we were happy with the change that we made and we felt like one of the big things that we were trying to solve for was have our pricing catch up to how people valued the tool.

Lenny (00:35:40):
How many people did you end up talking to, who was doing these conversations and is there anything really important you learned about how to ask these questions and these sorts of leanness to pay conversations?

Julia Schottenstein (00:35:50):
So we talked to dozens. It was combination of product and product marketing, having the conversations and people aren't very willing to share explicitly what they will pay. But there's some tools that we use on relative value. People most think about what is the relative value of dbt in their cloud warehouse. And we also tried to employ some of the tactics that we tried to suss out what do people view as very inexpensive? What's a price point that's very cheap or a no-brainer? What price point is maybe fair or comfortable for them and what would be too expensive? And then we had all the data back to figure out where we landed.

Lenny (00:36:34):
I want to come back to M&A for a bit. I had a few more questions there and I moved on from that. So again, you've done a lot of work within the M&A realm. Something that I saw recently, and this connects to the fact that a lot of startups now are looking to get sold. This VC hunter walk, he's a founder of Home Brew Ventures, had this interesting blog post where he basically suggested you should actually think about being public about the fact that you're selling your company. Which is crazy because in the past you never want to come across as too selly. I don't want people to think I'm desperate. And his point is many startups are desperate right now and it's okay to be public about that. And then in theory creates more of a bidding situation where many people know versus keeping it secret and in closed rooms. So my question is just what do you think of that? Do you think that's effective strategy? Is it not?

Julia Schottenstein (00:37:28):
I think it's good advice. If you're in a Hail Mary situation where you're looking for a home or you need an exit for your business, it's better to be transparent and cast a wider net. And you're right, in previous times founders tried to be a little bit cute or obfuscate that they were evasive the situation that they were in because they wanted to drum up some competitive interest when there really wasn't any. But unfortunately in today's climate, too many companies are in that spot so it's impossible to hide it. So the better approach is just to be transparent and I see it pretty regularly and there's absolutely no shame in sending a note that says something like, "Hey, we're looking for an exit for our company X, Y, and Z didn't pan out as we expected. We built a really interesting product and we want to keep the team together. We're running a process. Are you interested?" Really just as simple as that.

Lenny (00:38:24):
I've seen a lot of companies put together these really detailed decks or even websites of just like, here's the team, here's what we built to be very promotional about it. Is that something you've seen? Is that something you'd recommend?

Julia Schottenstein (00:38:35):
Yeah. Usually in these situations people are acquiring the teams and so having your data room together, really the most important thing is these are the team members that are going to come along with the acquisition is the biggest motivator for why a buyer would get excited.

Lenny (00:38:52):
You made this point earlier that a lot of the seeds need to be planted early for you to have the best outcome. And this reminded me... So I had a startup local mine that we sold to Airbnb and I met Airbnb initially at a year before we actually started exploring the process at a random party at South by Southwest where I was, I actually have no memory of this party, but the head of product at Airbnb, Joe bought, remembered it and came back to us a year later and just like, "Hey, what are you guys up to? Maybe we could collaborate on some stuff," and that led to an acquisition. So I think that's just wanted to touch a ban on that point of just the power of, the way I thought about it is let a thousand flowers bloom, just like meet everyone. Get the word out that you're around and what you're doing so that in the future when someone has that problem they're like, "That company, maybe we should talk to them."

Julia Schottenstein (00:39:37):
Yeah, you want to make sure that the buyer knows who you are before the acquisition moment and hopefully that's because you've made an impact and they like what you're building. Maybe you've inflicted some pain on them. But yeah, certainly creating those connections well ahead of an exit event is important.

Lenny (00:39:58):
And specifically there it's meet people at your competitors potentially. For us, Airbnb was never even a potential company we would sell to because it had nothing to do with it but ended up making sense down the road. What's like the realm of the companies and people that you think people should think about meeting?

Julia Schottenstein (00:40:12):
If the company is buying a lot or they're active, they often have corp dev teams and so use that corp dev team to your advantage. It's their job to meet absolutely every company that could be potentially interested. So take that meeting, say you're not interested in an acquisition just yet, but push them to make an introduction to someone that could sponsor the deal. So usually that's someone in product or maybe a GM and use that as a starting point for maybe just a conversation, maybe something more like a partnership but get the corp dev team to work for you.

Lenny (00:40:50):
What if you're at the other end of the spectrum and you're in dire straits right now and you're just like, "Man, what do we do to potentially sell this company?" I know odds are not going to be great, but just what do you suggest folks do in terms of I guess finding connections to potential companies that might be acquirers?

Julia Schottenstein (00:41:07):
Yeah. I mean use your network. Usually your venture capitalist has a really big network and one of the things that I hear founders feeling the most nervous about is a duty to return the money to the investors. And maybe this is a unpopular thing to say on a podcast, but your investors understand that they're not making their money back. And what they want to do instead is have you end up at a really great company like an Airbnb because that will help them down the road. So it's all about the long game, but use your investors to help you find connections at different companies that could be buying and don't worry so much about disappointing them or being really realistic about where you are in your company journey.

Lenny (00:41:55):
To build on that, I'm just an angel investor, I'm not like the lead fund and they feel differently I imagine. But the last thing I want for a founders to get stuck at a company they hate and just so that they could return some money or have some outcome rather they just give up, move on. Life is short.

Julia Schottenstein (00:42:11):
Yeah. I think founders forget that it is so risky investing in early stage companies that 50% of portfolios investments don't return anything. And that's just part of the game and it's a very acceptable path where hey, we gave it our best shot. It didn't work out and moving on.

Lenny (00:42:36):
Which is tough a lot of times for founders that are told like it's all about grit and not giving up and don't quit. Sometimes you should quit.

Julia Schottenstein (00:42:43):
Gosh, yeah. I don't want to say that. I think being founders, it's an extremely lonely role sometimes and it is very hard to know what your next chapter will look like or what the journey will look like and sometimes you really are out of cash and you do have to find a home. But I hope that you can continue to fight and find a way forward.

Lenny (00:43:08):
Agreed. Specifically for people thinking about selling their company, are there any companies you think are good companies for people to look at right now that are actively acquiring or open to M&A?

Julia Schottenstein (00:43:19):
This is a tough one. I think a lot of companies are on the sidelines for a number of reasons. And they could be on the sidelines because they just did an acquisition and they're trying to digest or integrate that company. They could be on the sidelines because they're not growing headcount as much and M&A is often org chart gymnastics of folding the target companies headcount into your budget and plan and maybe just don't have a lot of space. Or probably more common right now is there's just a general uncertainty about the future. And in highly volatile markets people want to take care of their own and even the best M&A deals at a level of complexity that a lot of buyers are just not looking to take on right now.

(00:44:07):
So there are a number of reasons why people might sit out, but what I would do if I were in a position of wanting to sell my company is I would come up with a buyer set of maybe a dozen and really there aren't more than a dozen companies that will find what you're doing to be a very good fit. Start with your buyer set and then start calling the list by looking at some of the criteria that might count people out. And then go have those conversations. And if you're in a Hail Mary situation, be very transparent about it. Maybe open up the buyer list. But if you still have some room, I would maybe focus on two to three partner or buyers and really play a different playbook, which is inflict pain. Make it really hard for them to not notice you but do it with a smile and be friendly at while you do that.

Lenny (00:44:57):
Sometimes with M&A discussions, there's a lot of subtlety to the way you communicate where you don't come out and be like, please we'd love to sell our company to you. Any advice on just the phrasing and how to approach it or do you think it's just, it's fine, just tell us we're looking to sell our company. Are you interested in being buyer?

Julia Schottenstein (00:45:15):
Yeah. I just wouldn't be too clever here. Everyone understands like I'm evaluating strategic alternatives. It means you're looking to sell your company and it depends. Do you have time? If you have time, yeah. Don't come out and say, "Hey, I'm for sale." That's not going to end up in a good outcome. But depends where you are in your company journey. If you have time, then don't talk about M&A at all. That's the last thing that you want to speak about. Instead, you're talking about maybe collaborating or partnerships. How do we work together? Knowledge sharing and M&A is a dirty word if you have a lot of runway and you're going to try to continue to pursue an independent path, but if you're out of time, you're out of time.

Lenny (00:46:08):
That's such good advice. I remember the term we used was we want to explore a strategic partnership and everyone's just like, I knows what you mean by that, but you just don't want to say it.

Julia Schottenstein (00:46:19):
Yeah. It's like everyone in the room's looking like yeah. Okay. Strategic partnership or a strategic alternative, it's like we all know these code words and we understand the situation you're in.

Lenny (00:46:31):
Yeah. When do you think M&A market might pick up again? I know it's impossible to predict. Do you have any sense?

Julia Schottenstein (00:46:37):
Yeah. I wish I had a magic ball. That'd be pretty sweet. I think what is happening though is we're far enough out from the peak of the markets. So the peak was really November of 2021. And why does that matter? Two things. One, founders are coming to terms with valuations that they maybe received at the highest of the market, are no longer going to hold in this market and companies are out of cash or maybe out of options. We'll be better assets entering the market soon. And at a certain point the opportunities will just be too great. That will incentivize a lot of the buyers that have been on the bench to start participating again in the M&A market. And I don't know exactly when that will be, but I think we're pretty close. I think we're pretty close.

Lenny (00:47:28):
And you mentioned a value that you have at dbt. I forget exactly what it was, but I'm curious what are the other values that you have at dbt, whatever you can share. Always curious what principles and values companies come down to help drive the way they think.

Julia Schottenstein (00:47:42):
The value that I shared is we are more concerned with value creation than value capture and that really drives everything that we do. We try to put a lot of good out into the world and it pays back slowly. The whole mission of dbt Labs is to help analytics engineers disseminate organizational knowledge through data. So we really believe also being participants of sharing that information and getting more people knowledgeable about all sorts of things.

(00:48:13):
Transparency wins. We're a really transparent company. We share our board decks. We have lots of communication and participation in all of our Slacks. We're writing culture. We have hard conversations in the open. So that's another a big one. Transparency always wins. We are humble. We don't ever feel like we are successful. We come at this from a very humble space where we feel like we have to serve our community and our users and that really motivates us. And then another one is just work done well as its own end and it's really focusing on the journey and not the end destination.

Lenny (00:48:56):
Awesome. I want to do a post someday of just like, here's the values all these different successful companies have come to and see if there's any patterns. I'm actually doing a post right now on Snowflake and on Figma and what you touched on. There's such a connection and a thread of obsessing with your users and making sure they're happy at Figma. I forget exactly what it is, but it's just like in this article, it's going to come out tomorrow actually. So people get a sense of when we recorded this where they think of their company as software as a service where service is their number one goal. They actually provide service and software is just a way to do that. And then it's Snowflake. Their number one core value is put customers first and they talk a lot about how they just actually informs their prioritization all I think, and all their thinking. So it's interesting. That also comes up a lot in what you're talking about, which I think it's easy to say, but I think what actually separates companies that succeed is they actually put this into practice.

Julia Schottenstein (00:49:51):
It's really interesting too because a lot of the people who work at dbt Labs came from the community, so they feel this real ownership in making the experience an excellent one because they were so compelled to come join dbt Labs because the product changed the way that they work or changed their lives. So that commitment to the community and product experience is really, really strong.

Lenny (00:50:14):
This isn't another thread. Maybe we'll go down real quick. I'm working on a different post around Reddit and how to work with really opinionated users that strong opinions about changes to the product and the way they described it, these guys were there for five years working with the community on the product. Is that to your users, the product is their baby, basically. It's like they think it's theirs versus the companies. And I'm curious, having a really strong opinionated community, what it sounds like you also have, what have you learned about just working with them to build product that makes them happy and avoid revolts and really upsetness?

Julia Schottenstein (00:50:51):
It's hard as you grow. I think it's just a challenge cause our community gets bigger. You can't service everybody's needs. But I think what we've done is everyone is very deep in our own product. I think one of the cool stats is at dbt Labs we have over 30% of our employee headcount has contributed to our data transformation workflow. So that's across every discipline. It's in obviously product, obviously in our data team. Our marketing team also contributes to data transformation. And our engineering team will also contribute to our internal dbt analytics project and that sense of really understanding what the experience is like and then soliciting as much feedback as we possibly can. We have a dbt Slack community of 50,000 and all of our employees are in that Slack channel regularly and can feel when we mess up or we don't quite deliver an experience that we're proud of, you will just see dozens of people trying to jump on board and try to make it better.

Lenny (00:52:02):
Is there any other frameworks or just general processes that you found to be release useful in building awesome product running teams?

Julia Schottenstein (00:52:10):
I'm not a big framework person, but there's two sayings that I find myself repeating or I either to myself or to others. And it's worse is better and tech debt is a champagne problem. And what do I mean by that? It's really to help me combat this perfectionism because perfect doesn't exist and you should instead go with good enough because when you ship, that's the moment when you get to learn a lot from your users and you just can't anticipate it. You try very hard to understand exactly how people will use the product and get all the edges ironed out. But you can't until you ship. And I'll share an example. So my team helps support the dbt cloud scheduler and the initial version of the dbt cloud scheduler was pretty naive. We were a little embarrassed by it.

(00:53:02):
It was a big old for loop over a big old jobs table. So we would look like is it time for this job to run? Okay. Yes, run this job. Okay. It's not time for this job to run next, continue on. Is it time? Yes, run this job. And it would just loop over and it's extremely naive and very simple, but it got the job done. And I try to remind the engineers, we would be so lucky to have tech debt because that means people are using the product. And now we've had to rebuild our scheduler several times over because we do have meaningful scale. We have 8,000 companies using our scheduler. We have to manage 10 million runs per month. But what we didn't need at launch was a distributed scheduler with coworkers and RabbitMQ. We just didn't need it because we had no users. So these two sayings that worse is better and tech debt is a champagne problem, just really reminds people like, let's ship, let's get it out into the user's hands and then we'll learn and iterate and it'll be a better experience for them.

Lenny (00:54:08):
That's a good segue to my last question. So weren't a PM before this role. You have strong experience in investing, investment banking business in general. I'm curious what you think product managers should maybe focus on more or learn more or lean into to become stronger product leaders based on the experience you've had moving into product.

Julia Schottenstein (00:54:30):
So I pull a lot on my experience or some of the things that I did was as an investor in my current role in product. And maybe I'll touch on what is the scale of a venture capitalist might be a little bit foreign for people, but venture capitalists, they spend all their day meeting lots of different companies, context switching. They have to know a little bit about quite a lot of different things. And they do this to refine their investment tastes or find their investor judgment. And they're also investing a lot in their network and connecting people, supporting people, and mining people for ideas that are way smarter than they are. So you do that all the time in Venture and I've brought a lot of those skills with me into product and it translates really well.

(00:55:17):
The first is I still spend a lot of time investing in my network and I think it's an underrated way for a PM to spend their time. And I try to build a network of operators at other companies that are like dbt Labs that are growing nicely, maybe a little bit ahead of where we are. And I ask them questions, how did you navigate open source? How did you navigate pricing? How did you navigate acquisitions? And then I take the best ideas, figure out which ones I can apply and bring it back to dbt Labs. The second thing is I really think my special T or my superpower is that I'm a T-shaped generalist. So I know a little about a lot of things from finance to business to product. I have to go a lot deeper in product in the areas that I specialize in. That's where the tail of the tea comes in. But it's precisely because I've had a diverse background that makes me more effective when I'm trying to get things done within the organization. Because I have just more credible experiences that I can pull from.

(00:56:18):
And then the last thing that I think maybe doesn't show up day to day in my product work, but in investing, you're constantly thinking about risk and the power laws, and we touched on this before, but most investments don't work out. You lose the dollars that you put in, but all the returns come from these rare events that make up for all the losses. You have to think about what are the uncapped upside opportunities in investing. And I think in product, you still have to do the same thing. If 50% of the things I worked on went to zero, we'd have a problem. But it encourages me to continue to make bets for the company that has the chance of bending the trajectory of our business.

Lenny (00:57:03):
We've reached our very exciting lightning round. I've got six questions for you. Are you ready?

Julia Schottenstein (00:57:07):
Yeah, let's do it.

Lenny (00:57:08):
What are two or three books that you've recommended most to other people?

Julia Schottenstein (00:57:12):
Okay. So two books that helped me learn a lot about myself. Range, it's a book about generalist and also Quiet, it's a book about introverts. And then I like a lot of biographies. So a few of my favorites are Snowball about Warren Buffet, Made in America, about Sam Walton and Leonardo da Vinci.

Lenny (00:57:31):
What is a favorite recent movie or TV show?

Julia Schottenstein (00:57:34):
So I almost watched a movie in preparation for this podcast, but I really don't watch things except in the holiday. During the holidays, I like Succession, but I have not seen the latest season.

Lenny (00:57:46):
Wow. You're in store for a treat. Favorite interview question you like to ask?

Julia Schottenstein (00:57:53):
When's the last time you had to teach yourself something new and how'd you do it? So I like to test for growth mindset and a thirst for learning. And then also why dbt Labs. I think a lot of people who come to dbt Labs have very authentic reasons why they're drawn to the company. And in moments where in things are tough, it's the answer to that question of why are you here, it's going to make all the difference.

Lenny (00:58:17):
And sounds like what you look for is just like an genuine enthusiasm.

Julia Schottenstein (00:58:21):
Yeah.

Lenny (00:58:22):
Awesome. What are some favorite products you recently discovered that you really like?

Julia Schottenstein (00:58:27):
I like Belly. It's a consumer social app that lets you find and discover restaurants and rate them with your friends. It's been a lot of fun looking at the New York City restaurant scene.

Lenny (00:58:37):
I've never heard of that. Awesome. What is something relatively minor you've changed in the way you all do? Product that has had a lot of impact?

Julia Schottenstein (00:58:42):
Do fewer things and try to single thread the team as much as possible.

Lenny (00:58:50):
And single thread meaning like one main priority, one goal?

Julia Schottenstein (00:58:53):
One mission. Yeah. We're all working rowing in the same direction.

Lenny (00:58:57):
Final question. You have a podcast, first of all, tell us what it's called, but second of all, what's a favorite podcast of yours other than this podcast and your podcast?

Julia Schottenstein (00:59:05):
Yeah. It's called the Analytics Engineering Podcast, so if you want to learn more about the data industry, I host it every other week with our CEO Tristan Handy. It's a lot of fun. Check it out. Other podcasts that I really like are In Depth, it's First Rounds podcast by Bretton. He interviews a lot of operators about how they do their very best work. And another podcast that I really like is the Logan Bartlett Show, which touches on timely trends in tech.

Lenny (00:59:34):
And In Depth I think Todd Jackson actually hosts a lot of the episodes too. Also, a huge fan of the podcast. Definitely check it out. And then say your podcast again and how can folks find it?

Julia Schottenstein (00:59:43):
It's called the Analytics Engineering Podcast.

Lenny (00:59:47):
And it's just in podcasting apps?

Julia Schottenstein (00:59:48):
Yes.

Lenny (00:59:49):
Amazing. Check it out. Julia, we've talked about inflicting pain and strategic partnerships and why worse is better. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out and how can listeners be useful to you?

Julia Schottenstein (01:00:03):
You can find me on Twitter J_Schottenstein, and you can also find me in the dbt community Slack also, Julia Schottenstein. Send me a note, reach me there and I'd love to hear from you if you have data problems or we can help serve your needs better, would love to chat.

Lenny (01:00:22):
Thank you so much for being here, Julia.

Julia Schottenstein (01:00:24):
Awesome. Thanks Lenny.

Lenny (01:00:25):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

