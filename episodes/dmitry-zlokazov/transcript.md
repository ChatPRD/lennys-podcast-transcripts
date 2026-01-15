---
guest: Dmitry Zlokazov
keywords:
- growth
- retention
- metrics
- roadmap
- mvp
- conversion
- pricing
- revenue
- hiring
- culture
- leadership
- management
- strategy
- vision
- competition
title: 'How Revolut trains world-class PMs: The "Local CEO" model, raw intellect &
  building wow products'
youtube_url: https://www.youtube.com/watch?v=-kPpd21bFrE
video_id: -kPpd21bFrE
description: Dmitry Zlokazov is the head of product at Revolut, the $45 billion fintech
  giant operating in over 50 countries, serving more than 50 million customers.
duration_seconds: 4202.0
duration: '1:10:02'
view_count: 24809
---

# How Revolut trains world-class PMs: The "Local CEO" model, raw intellect & building wow products

## Transcript

Dmitry Zlokazov (00:00:00):
Everyone is striving for talented, skillful, smart people. Revolut values way more raw intellect and this unquenched hunger to build things rather than experience.

Lenny Rachitsky (00:00:12):
I hear one of the ways you approach early products differently is you guys invest a lot in actually making it good.

Dmitry Zlokazov (00:00:18):
It's not getting traction. Is it because the underlying idea is wrong? Or maybe your product just sucks? By forcing everyone to build a product that people will love, we kind of cut out this part of uncertainty. We can cut down the product in terms of functionality to just most critical features, but we will never compromise on the quality and UX and the aesthetics.

Lenny Rachitsky (00:00:43):
Is there anything that you've figured out about just how to set up new products for success?

Dmitry Zlokazov (00:00:48):
If something is 99% done, it's closer to 0% rather than 100%.

Lenny Rachitsky (00:00:53):
Today, my guest is Dmitry Zlokazov. Dmitry is global head of product at Revolut, which is a finance super app offering customer savings and checking accounts, crypto, investing, joint accounts, even mortgages. Not only was it last valued at over $60 billion, but in the research that I've been doing into which companies hire and incubate the best product managers, Revolut was right at the top alongside Palantir and Intercom. And so in our conversation, we dig into what Revolut has learned about producing and hiring great product leaders, including a focus on ownership, having people solve really painful and complex problems while making the experience wow and lovable by users. Also indexing towards hiring really smart and driven people early in their career versus people with a ton of experience in the space and so much more. If you're looking for a job that will accelerate your product career or want to help your product team level up, this episode is for you.

(00:01:48):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of Linear, Superhuman, Notion, Perplexity, and Granola. Check it out at lennysnewsletter.com and click bundle. With that, I bring you Dmitry Zlokazov.

(00:02:08):
This entire episode is brought to you by Stripe. There's a reason that I've had more guests on this podcast from Stripe than any other company. It's because they hire the best people and they build incredible products. You probably know them for their payments platform, which powers my newsletter, and also companies like NVIDIA and Salesforce and Zoom and DoorDash. What you may not know is that they have several other products that can help accelerate your revenue, such as Stripe Billing, which powers billing for companies that you may have heard of. OpenAI, Anthropic, Figma, Atlassian, and over 300,000 other companies. Stripe Billing lets you bill and manage customers however you want from simple recurring billing to usage-based billing to sales-negotiated contracts.

(00:02:53):
There's also Stripe's Optimized Checkout suite, which is a plug-and-play super optimized payment flow that natively supports over 100 global dynamic payment methods. There's also a product called Link, which is an accelerated checkout experience built specifically to increase your checkout conversion. Every single one of the Forbes top 50 AI companies that have a product in the market today use Stripe to monetize it. Half of Fortune 100 companies use Stripe. $1.4 trillion flows through Stripe annually, which is equivalent to over 1% of global GDP. Use Stripe to handle all of your payment-related needs, billing, manage revenue operations, and launch or invent new business models. Learn more at stripe.com. Dmitry, thank you so much for being here and welcome to the podcast.

Dmitry Zlokazov (00:03:46):
Hi, Lenny. I'm happy to be here.

Lenny Rachitsky (00:03:48):
As you know, I've been doing a bunch of research into which companies hire and create the best product managers, and I've been triangulating this across a bunch of different data points. I've been looking at which companies alumni product managers get promoted most when they leave the company, become chief product officers at the highest rate when they leave the company, become the first PM at a startup, also start their own companies. And when I triangulate it across all these different data points, there's three companies that are kind of sat at the top, you guys, Revolut, Palantir, and Intercom.

(00:04:21):
Clearly you guys are doing something really special. I don't think a lot of people, especially in the US know a ton about Revolut, and so I'm really excited to have you here. I'm really excited to basically extract as much wisdom as I can from you about what you guys have figured out in helping in hiring and training product managers. So I want to actually start with giving people a slight understanding of what is Revolut. I think a lot of people in the US especially don't know much about it. So what's the simplest way to understand what you guys do?

Dmitry Zlokazov (00:04:49):
Revolut challenges banks in 50 different countries and it all started 10 years ago in London. So maybe let me give you a bit of a context, especially for someone based in the US, it's important to understand that European banking landscape is very diverse. In the US if you travel from state to state, things are different, but for example, you always pay in US dollars, right? In the UK you pay in British Pound. If you travel to mainland Europe, you will pay in Euro, but if you go to Switzerland, you'll pay in Swiss francs. If you go to Sweden, you'll pay in Swedish Krona and so on and so-and-so. Overall, there are 25 different currencies and every time you were traveling and paying in a different currency, banks were charging you exorbitant fees on top of terrible foreign exchange rates, and that's when Revolut launched as a multi-currency card and people loved it.

(00:05:51):
They loved that Revolut was saving them 50 or 100 euros, but even more so they loved the transparency and simplicity of the product and that's why when we started rolling out more and more products based on those principles, they were quickly getting trust of people. They were quickly getting traction. So that's how P2P transfers appeared, and then frictionless crypto buying and withdrawal to a bank account appeared. And then more and more products created products, savings products and so on.

Lenny Rachitsky (00:06:27):
Awesome. And then just to give people a few kind of scale of the company, how many employees are there roughly? I think the last valuation something around 60 billion. I don't know if you can even comment on that, but just what are some numbers real quick for people to understand the scale of the company at this point?

Dmitry Zlokazov (00:06:40):
The headcount is not something we're trying to increase, to be honest. Actually Revolut tries to stay as lean as possible, but I think it's just that our appetite for growth is so big that I think we're currently at maybe 6 or 7,000 employees.

Lenny Rachitsky (00:06:58):
Wow. Okay, cool. So let's get into what you've learned about building an amazing product team and also hiring an amazing product team. So first of all, you call your product managers product owners, and when we were chatting through initially it was like, "Oh, I see. It's just like a big scrum business," and they just have all these product owners who many times on this podcast people have talked about that's not actually a product manager, but that's not at all how you work. So in this context, product owner's an actual owner. Talk about just the story behind why you call your product managers, product owners.

Dmitry Zlokazov (00:07:28):
Yeah, it's not a scrum term for us, it's just our take on emphasizing how ownership is important, really. So product owners are central to the company and its growth. They are end-to-end responsible for the product, for this part of the business, and for their customers to be happy. And for that, they do really everything. They run the teams, they define which roadmap we need to build to improve certain business metrics, and they also contribute to high-level company strategy, but then most importantly, they execute on it relentlessly and they are ultimate responsible for the product to be shipped and achieve results.

Lenny Rachitsky (00:08:24):
There's always this term of mini-CEO, PM as a mini-CEO, and it feels like in your context, that's actually what you try to do with your product team is they're essentially mini-CEOs. They have a lot of power. I think engineers, designers report to them. Is that right?

Dmitry Zlokazov (00:08:35):
Yeah, correct. Well, I prefer to say local CEO.

Lenny Rachitsky (00:08:38):
Local CEO. Okay, let's talk about that. Yeah, yeah.

Dmitry Zlokazov (00:08:42):
Yeah, but that's true. So the way we operate, we have these fully cross-functional teams, meaning they're staffed with all necessary functions, engineers data, analysts, designers, operational managers and so on. And we also operate in metrics. So everyone has a line manager and a functional manager. So product owner is always the line manager for everyone on the team, meaning product owner defines what they need to do, but then functional managers, they define how these things are need to be built and essentially with the right level of quality and so on.

Lenny Rachitsky (00:09:28):
I love this because it's so fun just to learn about such different ways of operating. Another fact that I saw is that there's two types of product owners. There's kind of like a UX product owner, and then there's a different like technical product owner.

Dmitry Zlokazov (00:09:41):
We actually have three.

Lenny Rachitsky (00:09:42):
Three.

Dmitry Zlokazov (00:09:43):
And the third type becomes increasingly more important. So the first type is UX product owners. Then there are technical product owners, and then there are data science product owners. So UX product owners are the ones who work on consumer facing part of the product. Usually they have a great taste for things and they understand what constitutes UX that will work and which things will not work. So they also have this expertise in the industry. Then tech product owners, they are the ones who delve deepest into details. Usually those are former engineers who grew into making decisions and driving business. And the data science product owners are usually former data scientists who decided to grow into management positions, but they're still very hands-on.

(00:10:55):
And you know what? There are way more things that are common to each of these three specializations. So what we see sometimes is people just shifting them because I would say that what defines the specialization is probably 5, 10, 15% while 85 to 90% is common to each one of them. And those things are, so first of all, being a great problem solver and have a great linear thinking, but also have a creative approach towards nonlinear problems. Then building this context for customer and building empathy towards customer and translating it into the team.

(00:11:48):
Then going down to details very, very deep because in our domain there are no obvious things and you need to get to the root cause of the problem really, really deep to understand what will work and what will not work. And that means that you also need to be quite technical, even if you are an expert, you still need to often go as deep as sitting with engineers and reading code. And then I would also emphasize the importance of business acumen because we tend to measure and quantify product performance a lot. And you need to understand, okay, what things will we build that will drive eventually that business metric and that target?

Lenny Rachitsky (00:12:41):
So I love this idea of the product owners having to go really deep. I think a lot of people hearing this, they think they can go deep, go deep, really understand the details of what they're working on. I'm curious if there's an example that's illustrative of just what you actually mean here.

Dmitry Zlokazov (00:12:55):
For example, to provide the best possible product in every country of presence, we need to have necessary licenses. In Europe, it means that we need to launch local branches of our European bank, for example, a branch for France, a branch for Germany, or a branch for Italy. To launch a branch, you need to fully comply with all necessary regulation. You need to report necessary data on customers to various regulators and authorities. You need to register with local payment systems. And each of these things, they have a lot of projects nested within. We have a very lean team of just a few people who need to scope everything and do it at the scale of 50 countries. So the way we do it is we go very deep on example of each of these projects. For example, we launched a branch in Ireland, we launched a branch in Netherlands.

(00:14:01):
Then we reverse engineered what was the best process to do it, and then we went back up on top level and we said, okay, but what's the ideal framework of doing it at scale? And then we formalized it into a process really like an algorithmic process with steps and quality gates and assay needs, what people do we need to hire and how soon do we need to start doing that before we want to launch a new country. Then, so it's not only going deep, but also being flexible and doing this switch between zooming in very deep and then raising on the level of helicopter view and then understanding, okay, so this seems very, very complex in details, but then when you zoom out, how can we simplify it and build a robust process around it, which is scalable? And that's something that we have to do a lot.

Lenny Rachitsky (00:15:05):
As you're talking and we go through this chat, I'm keeping kind of track of what I think is most contributing to your alumni product owners, product managers becoming so successful. So a couple of things so far that I think are probably contributing to this is one is just having a lot of ownership over what they're building, which leads to building skills to start companies and become leaders at other companies. So these product owners that you have are just own a lot and are essentially GMs of whatever product they're working on. And then there's this depth and complexity where you have to really get good at understanding a problem really deeply. I imagine many of these people go on to work on something like that later, somewhere else because they've spent all this time, or they just get really good at dealing with complex many layered problems. So is there anything else just kind of along those lines as I say that you think is important?

Dmitry Zlokazov (00:15:54):
I would probably add an obsession with building wow product.

Lenny Rachitsky (00:16:03):
Wow. W-O-W?

Dmitry Zlokazov (00:16:04):
W-O-W.

Lenny Rachitsky (00:16:06):
Cool.

Dmitry Zlokazov (00:16:08):
I think in FinTech overall, this is probably the most neglected part usually, but it's also a part that we at Revolut, we pay enormous attention to. So it's not only when you do a trade in the app or when you send money, it's very important for it to be very fast and cheap process for you so that you don't pay a lot of fees. But we also pay a lot of attention to look and feel of the app and how smooth it is and how frictionless the process. Not only we invest in reducing clicks and optimizing finals, but we also want people to feel that we really cared about them. We also want people to feel that we love our customers and we applied extra effort for the product to look great and feel great. And I hear this a lot from our customers, like the app is something they really love and it helps them solve their problems. It's at least one of the ingredients of the company's success.

(00:17:22):
And I think people that work at Revolut, they built habit of paying attention to these small nuances, small details that make the product lovable. And then second is handling this context because it's a lot of details where you need to dive, but there are also a lot of dimensions where you need to dive into different details. And I think this ability to keep this large context in your mind and consider second order effects and view subjects from multiple angles, I think that this is also a very important skill that people usually train at Revolut.

Lenny Rachitsky (00:18:05):
Okay, cool. So we have three bullet points on the ingredients of great product managers slash owners that you guys incubate. On this wow piece, which I love. How do you operationalize this sort of thing? I imagine a big part of it is hiring people that are really good at this and value building lovable products. Is there any way you kind of have a process around making sure the things you ship are wow and lovable?

Dmitry Zlokazov (00:18:27):
Two things that you need to understand about how Revolut operates is that we operate in small lean teams that are tasked to build products and as I mentioned, and having end-to-end responsibility for products. And usually they're the ones who build it from zero and then they're growing and developing this product. And then another thing is that company is very flat and hierarchy is very flat. We still have our founders, Nick and Vlad, very hands-on going down to details for every product and every part of the business. And every week they have product reviews with every team giving an opportunity to every product owner present directly to CEO and CTO and show what increment has team achieved in the last week, but also get steering from founders, which is super valuable.

(00:19:31):
Essentially founders of the company, they still review a hundred percent of screens that are being shipped and everything that you will see in the app pass this review. And there are a lot of eyeballs that were scrutinizing this and thinking of all possible edge cases and nuances that we need to consider to make sure that every single customer will be happy in this product, in this flow.

Lenny Rachitsky (00:20:02):
That seems to be a consistent theme in products that are incredible is the founders are deeply involved in the experience and review everything. How many product owners are there at Revolut? Just to give people a sense by the way?

Dmitry Zlokazov (00:20:15):
Oh, I'm afraid to say it's already more than 150 people, maybe 170.

Lenny Rachitsky (00:20:20):
Cool. That's what I would expect. And then you said that there's kind of these three types, there's kind of like the eng type, the PM, traditional type, and there's the data product owner. When you hire the UX type of product owner today, is their previous role usually a product manager at another company?

Dmitry Zlokazov (00:20:36):
Yes, but I would say that not necessarily it's a very experienced product manager. Well maybe even it's way more important to have this hunger for building things and having the raw intellect. And we always try to find people with these intrinsic traits rather than hiring people who are very experienced but maybe are not super excited about building things.

Lenny Rachitsky (00:21:13):
What percentage of your product owners come from internal transfers from other functions?

Dmitry Zlokazov (00:21:18):
It's a quite substantial part of product owners who eventually become very successful by the way. So it's like a positive self-select, so it means that someone already succeeded in another role. So it's a guaranteed culture match, it's a guaranteed domain knowledge, and then they simply grow. Usually it could be operations managers or engineers. They grow into someone who now manages the team and that's why it's a very successful path.

Lenny Rachitsky (00:21:53):
So the other company on the list of top three companies that produce and hire the best PMs, according to the research I've done, Palantir. I just had someone that was at Palantir for a long time and we talked about exactly all the same questions. And interestingly so far we have kind of these three bullet points in terms of what product owners within Revolut get to do. There's a lot of ownership, there's a lot of depth and complexity, and there's a lot of focus on wow lovable products. So interestingly at Palantir also tons of ownership, also tons of depth and complexity. The other ingredient that I want to ask you about is they also have this concept of a forward deployed engineer where they put an engineer in the office of the company they're building the product from, they sit there building it for them with them.

(00:22:36):
And so there's a lot of skills built in terms of understanding customer problems, talking to customers, getting empathy building, things like that. Is there anything you guys do or focus on around just like talking to customers, the way you approach having your product owners work with customers, understand problems, things like that that might be helpful for people to hear?

Dmitry Zlokazov (00:22:56):
For us, it's a bit easy to reach out to customers simply because the customer base is so big, it's more than 50 million people and usually we ourselves are power users of the product. We receive our salary into Revolut and then we spend with Revolut, our friends the same. So it's like a no-brainer to talk to people continuously and even if you are not proactive in it, they will reach out. If you have a problem in the product, I guarantee that we know about it very, very soon. We've also built tools for product owners and designers to have an easy access to a panel of users via different tools so that they can just start an interviewing process or a survey or a test of different designs in a few clicks.

(00:23:52):
For me, it was very important to build this direct connection to customers because when you delegate such an important thing as customer research and collecting their feedback to someone, you will get a refined filtered version. You won't get these nuances of how people describe things, which emotions they feel like and so on, and where they think stuck. It's very easy to lose all those important bytes of information in this process. So I'm a strong believer that it's very important to have direct communication channel to customers.

Lenny Rachitsky (00:24:32):
As you describe this, it's funny how you guys are at the extreme opposite end of the spectrum from Palantir in terms of how easy it is for you to get feedback. They build stuff for the government and for Airbus where employees would never use a product like that or need a product like that. You guys are getting paid in Revolut using Revolut to pay for things and constantly in the product. And so I could see why there's less of a need for something like a forward deploy engineer. Okay, amazing. Let's talk about hiring then. Is there anything unique about how you approach hiring, sourcing, looking for people, what you look for in people that you think might be contributing to your alumni being so successful down the road?

Dmitry Zlokazov (00:25:12):
I think everyone is striving for talented, skillful smart people and experienced people. Revolut values way more raw intellect and this unquenched hunger to build things rather than experience. So let me maybe bring an example. Imagine we saw this, you hire a great experienced professional with amazing regalia of achieving a lot of things, but then what I see in product, the adoption curve is usually longer than in other functions because product owners by definition are the ones who are the experts in that domain and in all those intricacies of how product is built and how it's used. So what we see from these professionals is they still take a lot of time to ramp up and sometimes they also take time to adapt to new culture or worse, they just rest on their laurels. But you already have super inflated expectations and usually their compensation is by the way, quite high and which adds up to these expectations. And I myself, after conducting maybe 400 or 500 interviews with product owners at Revolut, I also see this.

(00:26:46):
Unfortunately, professionals with a lot of years of experience from established companies, they don't have this strong urge to change status quo, which by the way will require toil, tears, and sweat. And that's why even if a candidate doesn't have a lot of years of experience, but they love building things, they've done it, they worked with engineers maybe by the way, maybe in their own startup or one of the best profiles that I've seen is a tech co-founder. So I think that's probably the best way to boost career is to go and found something work in a startup, build things yourself or with a very small team, work in all different areas because in startup you have to work in all different areas. And then these kind of people, they really thrive at Revolut and even if they don't have a lot of years of experience, they actually attack a specific problem.

(00:28:09):
They have a sense of what can cause customer pain, and they are very fast moving to solve it quickly and then that's how they get appreciation from everyone around. The team starts respecting these people because they solve some specific problem and then they take another problem, they solve it and then they take another and that's how they grow in the company.

Lenny Rachitsky (00:28:33):
Essentially what I'm hearing is you hire kind of more junior or super high raw, intellect driven, passionate, how do you describe, hungry people? And this explains why so many people get promoted so much more that leave Revolut because they start their earlier in their career and you help them learn all these skills, ownership, depth, understanding, working in complex environments, building amazing products. So this all makes a lot of sense. Is there anything you figured out about where to find these people? Because this is the dream, hire amazingly smart people that are super driven that nobody knows about yet and then make them awesome. Have you found anything about where to source and find these folks?

Dmitry Zlokazov (00:29:14):
So the way we work, we have a weekly catch-ups with the recruitment team. So essentially they are also a team that runs in sprints. So every sprint we define what do we want to focus on, which areas, which companies. One of the great sources is actually looking into products and apps that we love ourselves. So if someone built a great product, then it's likely a high performer. So usually we provide some great products in specific areas that are more important for us to the sourcing team and they just try to source targeting those companies. It could be also different areas. It could be even schools, like good schools. And so it varies from sprint to sprint.

Lenny Rachitsky (00:30:06):
That makes sense. Gokul had this really good piece of advice, I think it was on the podcast, if not he tweeted about it, where you look at there's successful companies, but then there's also what function in that company is the key to their success. And so you want to go like a company A for sales, company B for customer support, company C for design. And so it sounds like that's kind of the way you guys think about it a little bit. Yeah, very cool. Okay. I love how we're uncovering and we're uncovering this mystery.

(00:30:33):
This entire episode is brought to you by Stripe. Every single one of the Forbes top 50 AI companies that has a product in the market today uses Stripe to monetize it. $1.4 trillion flows through Stripe annually, which is equivalent to over 1% of the entire global GDP. And Stripe isn't just a payments platform. They also have a product called Stripe Billing, which powers billing for companies that you may have heard of, OpenAI, Anthropic, Figma, Atlassian, and over 300,000 other companies. Stripe Billing lets you bill and manage customers no matter your pricing model from simple recurring billing to usage-based billing to sales negotiated contracts. Collect and retain more revenue, automate revenue management workflows, and accept payments globally. Use Stripe to handle all of your payment related needs, including billing, revenue operations, checkout flows, or simply launching or inventing new business models. Learn all the ways that Stripe can grow revenue for your business at stripe.com.

(00:31:33):
Let me go in a different direction and see if there's more to learn here. When it comes to running your teams, is there something that is kind of fairly contrarian in how you approach running the product team that is maybe not how other companies operate that you think is key to your success?

Dmitry Zlokazov (00:31:51):
I've changed in how I operate after I joined Revolut probably because Revolut is a founder-led company and probably it's because it's self-led, and also because my role is quite spread across many things. So my role at Revolut is leading product function across company, but also leading retail, which is a core part of Revolut business. And it's very easy to be spread thinly across all those domains and catching up with 50 or 70 projects that are being executed simultaneously, which would mean that you will just spend your entire week just catching up on statuses, not really adding value to anyone, but it's also scary to not do it because what if there are some things going wrong and you won't be able to stop it or steer in a better direction.

(00:32:57):
So I think that's why also a lot of managers, especially in senior positions, they kind of stay high level and they don't go very deep into details. But how we did differently at Revolut is to go very deep into details. We take maybe 7 or 10 projects which are most impactful for customers right now. And we go super deep into them, really, really deep sitting with engineers like reading code level and understanding, okay, how it's built exactly and what's the underlying issue. And you could think that, okay, but what about others? Let's say 50 or 60 items that are being executed. But the thing is that it actually, it's counterintuitive, but it works really well because first of all, teams, they talk to each other, there are formal and informal ways of communicating through meetups or just meeting in the office and they know which areas are being scrutinized right now and which team is being scrutinized.

(00:34:19):
And it also gives information on what are the current priorities in the company. But in addition, it's signaled to other teams that if they are not proactively executing things on the expected level, paying attention to all the details and being meticulous in all those details, especially in quality, they will be the ones that will be reviewed to a such deep level, next phase, next cycle. So as a result, it also builds a great discipline. And since Revolut is such a high concentration of very ambitious people who thrive for being best versions of themselves and grow, and it's very important for them to prove that they can deliver great things and build next great company. As a result, they do everything to operate autonomously. And when you start diving deep into details, you see that everything is fine, you see their modus operandi and you can understand, okay, if this team is on good track or not on good track. And if it's not on good track, it means that it probably will be one of your next areas as of focus.

Lenny Rachitsky (00:35:53):
Okay. So what I'm hearing is you said there's 50 to 60 things kind of projects being built at once.

Dmitry Zlokazov (00:35:58):
Maybe closer to a hundred, actually.

Lenny Rachitsky (00:35:59):
Okay. Okay. So there's like a hundred things happening at any point like features being built, products being launched, and this is you and the founders choose 7 to 10 to focus on, or is it just you?

Dmitry Zlokazov (00:36:13):
No, it's just me.

Lenny Rachitsky (00:36:15):
Just you. Okay. And by the way, do you have a leadership team that you're a part of with a design lead or is it just you basically at the top?

Dmitry Zlokazov (00:36:22):
So the way it's structured, my responsibility is a product function. We also have a head of design function. It's also part of my team, but then all the other functions, they are separate like engineering and data function, and all of them report directly into a CEO.

Lenny Rachitsky (00:36:41):
Got it. Okay. So out of a hundred things you choose, here's the 7 to 10 things I'm going to go deep on. These are the things that matter most to the business that if they don't go well, it'll have the most downside. And then you basically said you sit next to the engineers, you get really involved in every detail.

Dmitry Zlokazov (00:36:59):
Yeah, correct.

Lenny Rachitsky (00:37:00):
Awesome. Okay. That is definitely counterintuitive. We had Brian Chesky in the podcast and the way he approached this problem is he just cut down how many things happen at Airbnb because he wants to be involved in everything. And so I think it's cool to hear a different approach where we can still do a lot of stuff, but I'm going to choose, I'm going to go deep on the things that matter most.

Dmitry Zlokazov (00:37:21):
No, I think we'll never cut down things, it's just the appetite for growth and also entrepreneurial approach in the company is so high that we'll never allow ourselves to give up on some great opportunities, but also this approach is way more scalable. So while leadership and obviously founders themselves keep everyone accountable, go deep into details, it doesn't mean that they micromanage everyone. That's actually a very important thing. So the ideal position for any product owner is to be fully autonomous. And again, it doesn't mean that you will never be challenged, but if when you're challenged, you can show all the logic behind decisions you've made behind the roadmap. And even if metrics are not yet there, you will still let's say have this credit of trust to keep building things the way you want to build them. Eventually, yeah, you will be presenting the outputs of your activity on these weekly product reviews, but again, it's not a micromanagement either. It's more like, let's say a last line of control to make sure that what we're building all makes sense and that's value and is thoroughly thought in all details.

Lenny Rachitsky (00:38:48):
And then you said still every screen that is shipped, the founders review at some point, so it's not like someone's shipping stuff without the founders seeing it in some form.

Dmitry Zlokazov (00:38:56):
Yeah, yeah, exactly. They have a full overview over everything, but also it allows us to build so many things because there is actually little micromanagement. If founders had to be involved into everything, they had to cut things down. But by giving people autonomy, they actually boost company growth. And as a result, I think Revolut is a strong outlier in the industry in terms of how many products being shipped and how fast they shipped. Another thing here is what I mentioned previously is us investing heavily into platform so that every solution is scalable from the get go so that we don't have any custom solutions. And for example, take our credit team, they ship new products like loans or credit cards in the country literally every month. And it is just maybe 300 people. And I think that a credit division in an incumbent bank is maybe 2 or 3000 people building just credit products for a single country.

(00:40:28):
And our team is building it for 50 countries. And yeah, it's enabled through this approach with platforms which we build on top of small lean teams which are fully equipped with necessary functions and also have autonomy in defining what they're building and the flat hierarchy with everyone being accountable and founders having direct view of everyone and intervening if necessary.

Lenny Rachitsky (00:41:07):
I'm going to give people a list of the things you guys do. I didn't do this at the beginning because it would take too long, but you talk about all the products you're building and all the things that's going on. So I have a list here. It's probably incomplete, but just to give people a sense, so you guys have credit cards, debit cards, savings accounts, multi-currency accounts, domestic international transfers, joint accounts, minor accounts for less than 18 years old, stock trading, cryptocurrency purchasing, loans. Is there anything big I missed?

Dmitry Zlokazov (00:41:37):
I mean, some of those things are a huge by itself, let's say stock trading. It's not just stocks, it's also ETFs, bonds, and we're working on tax efficient accounts in different countries and crypto. We also allow staking crypto for example, we have on-ramp, off-ramp products, we have acquiring products. On credit, we have loans, we have a buy now per later product, we even launched mortgages. We launched first mortgages in Albania recently.

Lenny Rachitsky (00:42:17):
And then all of these across 50 different currencies and countries.

Dmitry Zlokazov (00:42:21):
Yeah, 50 different jurisdictions each with its own regulation, with its own requirements.

Lenny Rachitsky (00:42:28):
Oh, boy. It's a good example of Paul Graham has this concept of schlep blindness or schlepping where people want to avoid hard problems, but that's where the big opportunities are, solving really gnarly, painful problems. And that's basically what you guys did.

Dmitry Zlokazov (00:42:46):
Yeah, that's one of the things that excites me maybe the most at Revolut. The market is so big and there are still a lot of very inefficient players, and as a result, customers have a lot of problems that are unsolved. While we grow insanely and I think will soon be... When I joined, we had maybe just slightly north to 20 million customers. Now we are 50 million customers. Soon we'll be at 100 million customers. The degree of surrounding each customer with the ecosystem of our products extends a lot. So they become more and more people start using Revolut as their main bank account. They start receiving their salary into Revolut, holding their savings into Revolut because they love the product more. And so we can easily do another, I don't know, 2, 3X, 4X in customer base growth, but we can also do another 10X growth in how actively these people are using the product. So it's let's say what, 30, 40X to current, 45 billion valuation. Right? So it's a like a trillion-dollar company easily.

Lenny Rachitsky (00:44:13):
And on that note, I mean what I'm hearing is it's still a good time to join. There's a massive upside. So I know you guys are hiring, we'll just note that real quick. You're hiring product owners and a bunch of other roles, I imagine?

Dmitry Zlokazov (00:44:24):
Yeah, yeah. Well, as someone who owns the product function, I'm especially interested in product owners obviously, but we hire a lot of roles. I think we have maybe 3 or 400 open positions currently.

Lenny Rachitsky (00:44:39):
Oh my God. Okay. I want to talk a bit about new stuff that you work on. So new products that you decide to invest in. Is there anything that you've figured out about just how to set up new products for success? Because a lot of the stuff we've been talking about is staying on top of stuff that you're iterating on and making better. What have you learned about just helping new products succeed?

Dmitry Zlokazov (00:45:02):
Yeah, so we launched quite a few products that you actually maybe wouldn't expect from a bank starting with crypto that was insanely successful, but also non-financial services like booking a hotel through Revolut app, our loyalty program, rev points, which is sort of disrupting European market where people don't get great benefits from spending with card. In the US you can easily get, like what? 2% cashback with a credit card or in some sort of point. In Europe they don't have it. And we are actually the first to build a program on card spend rewarding people with really meaningful or monetary rewards. In the manner that I described. We understood, okay, what's the recipe of this success to then scale it and reproduce? So we built a new bets framework and essentially everyone can come up with a new idea. It could be a product owner, but it could be anyone, and they need to show some key important things which you usually can expect from a startup like market is there, business case is there.

(00:46:15):
We know that we can do it way better than competitors leverage and for example, some things that we have obviously some concepts of product and then what customer problem we're solving and so on. And there is very little bureaucracy, again, thanks to having founder hands-on, we can easily get a green light on anything, start launching it quickly. What we do is assemble same lean team with just a few people to build first version and then iterate and iterate. And the main thing here is to build first version very quickly to get feedback, but then not scale it before you polish the product. But then after we make sure that all metrics are fine, retention is great, we start scaling it. And the good news is that it can be instantly multiplied by our 50 million customer base and get great traction. So for example, one of the products that you mentioned, joint accounts essentially an account that you could have with a significant other one was one of the recently launched feature and it grew significantly and now it has over a million active users.

Lenny Rachitsky (00:47:33):
I hear one of the ways you kind of approach these early products differently is you guys invest a lot in actually making it good and not just like a scrappy MVP. Does that ring a bell? Does that resonate?

Dmitry Zlokazov (00:47:45):
Indeed, that's what I may be meant by keeping your first version narrowed down to a small user base. But even in this case, we still make sure that the product is well. So no one is excluded from this requirement of building a super polished product. It takes time, but it pays off. The thing is that when you launch a scrappy version and it's not getting traction, how do you know? Is it because the underlying idea is wrong or maybe your product just sucks and you need to improve it? So by forcing everyone to build a product that people will love by building a wow product, we kind of cut out this part of uncertainty. So bottom line, we can cut down the product in terms of functionality to just most critical features, but we will never compromise on the quality and UX and the aesthetics.

Lenny Rachitsky (00:48:56):
An interesting advantage you guys have that I'm realizing as you talk is most of the stuff you launch is stuff that is clearly something people will want because it's stuff that they get other places, but they get the advantages of it being integrated into all the other features and products you have. So it's like a cryptocurrency product. It's kind of like, okay, yeah, people would love a great cryptocurrency product built into this or joint accounts. So there's almost like a benefit of just like, okay, the people will want this, now let's just make it work really well with everything else we got and not hurt. You almost don't need to be the best at every product, although it sounds like you still try to be the best.

Dmitry Zlokazov (00:49:35):
But we must be the best. Yeah, a hundred percent.

Lenny Rachitsky (00:49:37):
But there's also, if you don't have the best joint account, but all the other stuff is awesome, people are like, "All right, it's fine. It just makes my life easier." But tell me what I might be missing because-

Dmitry Zlokazov (00:49:46):
So I think there are those kind of table stakes that we're building that anyone would expect from a bank. For example, savings account, right? It's just a basic thing that if a bank is not providing savings account, you wouldn't even consider it. But then we make sure that our rates are very competitive, if not the best. Then we make sure that there is no bad UX. Some banks, for example, they don't allow you to withdraw instantly and there are delays or they don't pay interest on daily basis. We will never do that. We will allow you if you want to move money out, you will be able to do it. You won't lose any interest. And interest is being paid daily and this is a fully flexible product. And then on top of it, what I would call maybe some delighters is we will allow you to open the savings account in many currencies.

(00:50:49):
So we want to add different currencies because now interest rates are going down, so people might find it valuable to open a savings account in, for example, I know in Europe, Swedish Krona interest rates are higher than Europe, but it could be even something like Brazilian Real with 12% interest rate versus 2 or 3% on euros. And then as the cherry on top, there is this all that in an amazing, you have very smooth, you can set custom wallpapers, you can set goals, you can automate a spare change towards your savings and all those features. So there is an underlying basic fundamental layer that where you need to be just on par with competition, but then there are a lot of things on top that just make people love your product way more. And obviously there are a lot of synergies in between those things. So yeah, thinking of crypto, you can just receive crypto on your wallet and then you can just instantly convert it to cash on your account or just spend it with your card. How amazing can it be? Just buy a coffee with Ethereum.

Lenny Rachitsky (00:52:09):
I love that. Okay, let me take this opportunity to try to summarize what I've learned from you so far in terms of what you guys have figured out about creating incredible product leaders. They go on to do wonderful things and basically one of the top three most successful companies at this. So there's kind of these two buckets as I talked to you and the Palantir guy, there's kind of like the hiring piece and then there's what you do to help incubate this kind of forge for incredible product leaders. So in what you do internally, kind of the four bullet points I've got here is give people a lot of ownership. They're essentially GMs of the product, the feature.

(00:52:46):
There's a lot of focus on depth and complexity and getting really good at solving really gnarly problems. And then there's a focus on building wow products, amazing lovable products that have a very high bar. And then there's kind of a subtle point that I think is probably impactful here is just working closely with detail-obsessed founders or product leaders like you and learning from you all and just seeing the value and impact of being super detail oriented. On that bucket, is there anything else that you think is super core that I missed before we get to hiring?

Dmitry Zlokazov (00:53:21):
Yeah, I would just maybe highlight the aspect of this going deep into details. There are two main streams. First is let's say being technical, understanding how underlying systems work, but second is also building empathy towards customers. Understand the possible contexts and making sure that your product will satisfy each one of them.

Lenny Rachitsky (00:53:46):
That's a great point. So it's actually understanding the bare metal of what is happening and how it's possible, and then making the experience as simple and wowable as possible.

Dmitry Zlokazov (00:53:56):
There is also a third aspect, but it's a boring one and it's complying with all possible regulations and making sure that your product will satisfy the regulator, but it's also an important part of the job.

Lenny Rachitsky (00:54:13):
What I get from that is just building patience with all-

Dmitry Zlokazov (00:54:18):
I would say it's actually being able to unblock your team and that sometimes require product owners to steam roll changes because it also means that you could easily get stuck with a lot of people just looking into each other and thinking, "Okay, can they approve it? Can they not approve it?" We try to innovate on it. We try to automate as many things as possible. We use even AI models for that, but it also requires a product owner to be able to get things done, just getting people down to consensus and understanding how your stakeholders, how to get them to the necessary decision and then blocking UTM so that eventually the value is shipped to customers.

Lenny Rachitsky (00:55:10):
Awesome. So essentially it's just getting done, plowing through blockers, dealing with many stakeholders.

Dmitry Zlokazov (00:55:18):
Yeah. That's always the most important.

Lenny Rachitsky (00:55:20):
Okay. That's a great addition. I could see why that would be really helpful for folks that are trying to get ahead in their career. And then on the hiring piece, what you look for is raw intellect, drive hunger, passion essentially. Those are the first two. And then interestingly, non-senior, not people with a ton of experience in the problem space, more so focusing on intellect and hunger. Is there anything else in that bucket that you think is important that leads to people being really successful?

Dmitry Zlokazov (00:55:49):
Most importantly, it's again, getting things done, getting your hands dirty, and great product owners are very hands-on. They don't think of themselves as managers who just give tasks to people and wait them to complete it. They just go and get things done and they understand that most important things they will likely have to do themselves, and they understand that there needs to be relentless focus on execution, and if something is 99% done, it's closer to 0% rather than 100%.

Lenny Rachitsky (00:56:29):
Whoa, say more there. Is the kind of insight there is just things seem like they're 99% done, but they're actually very far from being done?

Dmitry Zlokazov (00:56:38):
Sometimes the product is built, but then product owners are the ones who also make sure that, for example, customer care team or sales and marketing team are using it to a full extent because without it, it could be just another useless feature, and no one knows about it.

Lenny Rachitsky (00:56:57):
That is super cool. I like that mentality. Let me ask you something completely different. What's kind of the story of you landing at Revolut? I know you had to move your family. It was a whole adventure.

Dmitry Zlokazov (00:57:08):
My journey into Revolut actually coincided with me moving to the UK, so it was a completely new environment for myself. It's a huge stress load for the brain as well. And it's not only about using the other side of the lane on the road in the UK, but also it's a lot of things, for example, in the industry, some concepts that I've never heard about, and actually I've never worked at FinTech before, so I also changed the industry. So it was a complete turnaround for me and for my career, but I was very determined and excited about it because everyone who I've been talking to, they were saying Revolut is like it's top talent is at Revolut, all best product people are at Revolut, and I really wanted to be part of this great team.

(00:58:11):
Eventually it actually appeared to be advantageous for me because I also had this fresh view on things and even in the Revolut app, which is actually way, way better than other banks products. But even there I found some things that for me, because of this lack of context, they were not intuitive and I worked hard with the team to change that.

Lenny Rachitsky (00:58:43):
Okay, great. I'm going to take us to recurring segment of the podcast. I'm going to take us to Fail Corner. So in Fail Corner, the idea here is people come on this podcast, they share all these stories of success, everything's always going great, but in reality, things don't often go great, and there's a lot of things that don't go right. Is there a story you could share where things went wrong in your career, where you failed with a product you were building or a moment in your career where things were looking really bad?

Dmitry Zlokazov (00:59:11):
I think the most spectacular failures is probably were on the earliest stage of my career, which I studied back at university and maybe in my second year of university I started building some things, different startups, and one of them was actually a product that makes me proud even now because it was like what, 15 years ago? So 2010, meaning still no one really had even iPhones back then and me and my friends, we started building a website that allows people to buy tickets to the cinema so that they can skip the line so they don't need to come in advance to select best seats and they can just buy a ticket online and go to the seats directly. Something that today seems as a commodity. Back then no one had it.

(01:00:15):
People were using pieces of paper and we built an end-to-end system because not only we needed to build a website, but we also needed to build hardware to scan those tickets, for example. And to have these tickets in digital format, we needed to hack SMS standard because again, people didn't have smartphones. They had these Nokias and we were sending images, QR codes inside an SMS, which is like a hack of the standards in a way. And then we were scanning those things with our own devices and we built our own devices with scanners, and we actually created these beautiful devices made from stainless steel, which looked really nice inside the cinema halls.

(01:01:12):
And I remember how I was excited about it with my friends. We were like, "What an amazing thing." It's like, look, we are bringing future here, but we actually spent all our investment on this hardware and we were expecting that everyone will just rush into using our system. But it was a very low share of customers who started buying tickets online because people were not ready for it, which was growing quite slowly. And eventually we had to close it because we simply ran out of money because we spent all of it on this hardware without any proven business model. So something that currently looks like an obvious mistake back then, we were just enjoying building a product that we would love to use ourselves, which I think is the right principle, but it also was a very painful lesson. You need to stay lean, you need to validate things before you scale them. You need to think way more about the run rate of your business. So there were a lot of painful lessons for me. Since then, I also try to avoid working with hardware.

Lenny Rachitsky (01:02:27):
I was just going to say that's a common challenge for startups trying to get right into hardware, although I wouldn't be surprised now if Revolut launches something another product, and this is a new product line of Revolut now that you've had that experience.

Dmitry Zlokazov (01:02:42):
We launched a POS terminals required.

Lenny Rachitsky (01:02:48):
All right, there we go. Dmitry, before we get to our very exciting lightning round, is there anything else that we haven't touched on that you think might be really helpful for listeners to hear? Maybe a last wisdom nugget that you haven't already shared, or even just something to kind of double down on that you've already shared?

Dmitry Zlokazov (01:03:04):
No, I think that it was an amazing chat and thanks, Lenny. We covered a lot of different topics. I would just maybe summarize that if you're excited to build certain things, never hesitate to do it. The best way to do it is probably your own startup, and it also what will give you the steepest possible learning curve, but then if you want to join a company, try to choose the one that has the highest entrepreneurial spirit and that will allow you to work as closer to a mode of a founder as you possibly can.

Lenny Rachitsky (01:03:44):
That's a recurring theme in these conversations I'm having with companies that produce the PMs that have the steepest career trajectory. And so that advice is exactly what I'm taking away from this too, assuming you want your career to accelerate really quickly after you go work at this company. Okay, Dmitry, with that, we've reached our very exciting lightning round. Are you ready?

Dmitry Zlokazov (01:04:06):
Yes. Let's go.

Lenny Rachitsky (01:04:08):
Here we go. Okay. First question, what are two or three books that you've recommended most to other people?

Dmitry Zlokazov (01:04:15):
The Hard Thing About Hard Things by Ben Horowitz. Actually read it quite some time ago, but I found myself recommending it to other product managers most often. It's actually illustrative that to be a great product manager, someone needs to strive to being a great CEO. And besides this book emphasizes the importance of building systematic solutions and scalable solutions, which is critical for scaling a company. Also being honest on how important it is to grind stuff. And then second book is, I read it more recently, Build by Tony Fadell. I was really inspired by this one, especially given how I appreciate how it's not easy to build hardware and what Tony was describing there is just super exciting and inspiring. And also I think that there are different archetypes of product managers. There are people who tend to disrupt things more. Personally I think about myself as a builder, so Tony's principles that he highlighted in the book that they resonate with me a lot.

Lenny Rachitsky (01:05:44):
I'm trying to get Tony on the podcast. If anyone listening knows Tony Fadell and can nudge him, "Hey, say yes to Lenny," that'd be great. I've been in touch with his team, but he's not doing podcasts right now, but I'm trying to get him on. Okay, moving on. Do you have a favorite recent movie or TV show that you've really enjoyed?

Dmitry Zlokazov (01:05:58):
I think the last movie I watched was Oppenheimer and I really liked it. I always love watching biopics. I think they give kind of a perspective and let you think about things in perspective.

Lenny Rachitsky (01:06:17):
Is there a favorite product you recently discovered that you really love?

Dmitry Zlokazov (01:06:20):
Manus is a great thing.

Lenny Rachitsky (01:06:23):
The AI agent?

Dmitry Zlokazov (01:06:24):
Yeah. Yeah. It's just like I was super impressed how... I was mesmerized. It's so autonomous and smooth, and I just spent a few hours vibe coding and I created this JavaScript app that sends me a rare English word every day to learn and remember, and it worked, and I was just amazed.

Lenny Rachitsky (01:06:54):
What's a word you learned?

Dmitry Zlokazov (01:06:56):
Ineffable. It was the yesterday's word.

Lenny Rachitsky (01:06:59):
I love that. It's still going. That's great. Do you have a favorite life motto that you often come back to, you find useful in work or in life?

Dmitry Zlokazov (01:07:07):
I love this phrase. I think Eisenhower said it, "Plans are worthless, but planning is everything." It's like we often say how important it is to be flexible and agile and adjust to change in circumstances, but it doesn't allow us to actually not have a plan at all. It's important for us to remember that we always need to think many steps ahead and while being flexible, we also need to think things thoroughly.

Lenny Rachitsky (01:07:43):
Final question. For folks that are maybe checking out Revolut for the first time that want to play with it or already users. What's the most underrated feature? What's something that you think people should check out maybe they're not aware of, or even just like a UX, I don't know, animation, something fun that people may not know about?

Dmitry Zlokazov (01:07:58):
The thing that is not yet widely used, but I really loved it, is what we call a wealth protection. So if you go to settings, you can enable a limit for any transfers outside of Revolut. If you want to do a transfer above this limit, you'll have to do a selfie check, which is our proprietary technology. We do a video selfie here. It allows us to make sure that it's you, no one else is doing the transfer, and it's actually almost as smooth as face ID and the way the team built it is really great. I'm really proud of those guys.

Lenny Rachitsky (01:08:38):
Dmitry, you guys are doing something very special. I really appreciate you spending so much time with me chatting through all the things you guys have figured out. I think this is going to help a lot of different companies level up the way they think about product and for people to join Revolut that want to experience this and accelerate their career. So thank you for being here. Two final questions. Where can folks find you if they want to reach out and how can listeners be useful to you?

Dmitry Zlokazov (01:08:59):
I think the best way is to find me on LinkedIn and yeah, I would be happy to receive a note from anyone on how we can improve the product and any feedback on the product. And also if you know someone who can be a great fit to Revolut after you've listened to what I've told, then yeah, I would be grateful for that as well.

Lenny Rachitsky (01:09:26):
Awesome. You're about to get a flood of applications. Get prepared. Dmitry, thank you.

Dmitry Zlokazov (01:09:32):
Yeah, Lenny, thanks a lot. It was amazing time. Thank you very much.

Lenny Rachitsky (01:09:35):
Same. Bye everyone.

(01:09:38):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

