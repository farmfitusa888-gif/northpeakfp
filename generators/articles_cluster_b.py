#!/usr/bin/env python3
"""Service cluster, second month: the 2026-09 cluster month.

WHY THESE, AND WHY NOT THE OTHERS
The engine run of 2026-09-10 (MARKETING/reports/seo/northpeakfp-2026-09-10.json)
lists 32 buyer intents across the four services with no page against them. Only
17 of those are questions this site does not already answer. The other 15 are
not written, on purpose:

  Four "examples and what they got right" pages, one per service. An examples
  page has to describe finished client work. This site publishes none: no case
  studies, no client names, no outcome figures, and on a your-money-or-your-life
  tenant an invented engagement is the worst thing that could go on the page.
  They stay unwritten until there is real client material that a client has
  agreed to publish.

  Ten intents the topical map reads as gaps because the existing page's title
  says "accountant" where the map looks for "accounting services", or "CFO"
  where it looks for "cfo advisory". The substance is already on the site and
  writing a second page for it would be duplicate content against our own:

      accounting services  cost      -> articles/accountant-cost-small-business
                           mistakes  -> articles/bookkeeping-mistakes-that-cost-money
                           questions -> articles/questions-to-ask-an-accountant
                           diy       -> articles/diy-bookkeeping-or-hire
      controller services  cost      -> articles/controller-cost-fractional-vs-full-time
                           time      -> articles/how-long-month-end-close-takes
      cfo advisory         cost      -> articles/fractional-cfo-cost
                           best      -> articles/how-to-choose-a-fractional-cfo
                           diy       -> articles/do-you-need-a-cfo-yet
                           questions -> articles/how-to-choose-a-fractional-cfo

  One, "Bookkeeping in Wilmette", is answered by the bookkeeping pillar this
  month adds (build_pillars.py), which is what a "near" intent is for.

So: bookkeeping gets a pillar and four articles, accounting services four,
controller services five, cfo advisory four.

WHAT THE COPY MAY SAY
The same rule as articles_cluster.py, and it is not a style preference here.
This is a your-money-or-your-life tenant, so every factual claim has to be
traceable to a source a reader can check. The only sources these pages use are
the site's own published pages: the three packages and what each contains, the
free 30-minute first call, the reply within one business day, the fixed figure
in writing before work begins, the individually quoted scope, catch-up scoped
separately, the major software platforms, Wilmette and remote work nationwide,
and the founder as the About page describes him.

Nothing outside that was available to check while these were written, so
nothing outside it is claimed. No tax rule, deadline, threshold or dollar
figure appears on any of these pages. Where a page would have needed one, it
sends the reader to the site's existing tax articles, which carry their own
citations. No fees, no projected results, no performance figures, no product
recommendations, no statistics and no client counts. Chaudhry Ahmad is not a
CPA and nothing here says or implies otherwise.

FORM
Every article carries a 35 to 70 word lede that answers the title, h2s phrased
as the questions buyers type, a visible FAQ that the shell also emits as
FAQPage, and reviewedBy on its Article node, which build_articles_shell.py adds
from the one REVIEWER block. Section bodies are lists of paragraphs.
"""

CONTACT = "../contact.html"
SERVICES = "../services.html"
ACC = "../accounting-services.html"
CTR = "../controller-services.html"
CFO = "../cfo-advisory.html"
BK = "../bookkeeping.html"


def _a(href, text):
    return f'<a href="{href}">{text}</a>'


ARTICLES_B = [

# ===================================================================
# BOOKKEEPING
# ===================================================================
{
 "slug": "how-bookkeeping-works-month-by-month",
 "cat": "Bookkeeping",
 "pillar": "bookkeeping",
 "intent": "how",
 "title": "How Bookkeeping Works, Month by Month",
 "desc": "What a bookkeeping service actually does between the first of the month and the report landing in your inbox, and what it needs from you to do it.",
 "keywords": "how bookkeeping works, monthly bookkeeping process, bookkeeping service Wilmette, small business bookkeeping",
 "read": "6 min read",
 "lede": "Bookkeeping runs on a monthly rhythm rather than a year-end scramble. Transactions are categorised as they land, every account is matched against its statement, the odd items come back to you as questions, and a report arrives on a date you agreed at the start. Here is what happens in each of those steps.",
 "sections": [
   ("What happens before the first month?",
    ["Setup is its own piece of work and it happens once. We look at the accounts the business actually uses, connect them to the software, and agree a chart of accounts that matches how you talk about the business rather than how a default template does. If your categories have drifted over the years, this is where that gets sorted out.",
     "Two things get settled here that decide everything afterwards. What counts as which category, written down so it does not depend on who is doing the work that month. And what the reporting date is, so you know when reports arrive rather than wondering.",
     "If the books are behind, catch-up is scoped separately from the ongoing work. That is deliberate: you should be able to see the one-time cost on its own rather than have it buried in a monthly fee."]),
   ("What happens during the month?",
    ["Transactions come in from the connected accounts and get categorised. Most of them are routine and the software proposes the right answer, which is exactly why somebody has to look: a bank feed will happily file an owner draw as an expense and a loan deposit as revenue, and it will do so consistently for months.",
     "Receipts and documents get attached to the transactions they belong to while everyone can still remember what they were. The items nobody can place go on a list. That list is the single most useful thing in the whole process, because it is the difference between a guess and a question."]),
   ("What happens at the end of the month?",
    ["Every account is reconciled against its statement, which means the balance in the books and the balance at the bank agree, line by line, and the difference is explained rather than plugged. Credit cards and loan accounts get the same treatment as the operating account.",
     "Then the questions come to you. Usually a short list: what was this payment for, is this deposit a customer or a transfer, did this invoice get paid. Answering it takes a few minutes and it is the part that keeps the reports honest.",
     "Once the questions are answered, the reports are produced and sent. That is the point in the month when you can look at the numbers and act on them, which is the whole reason for the schedule."]),
   ("What do you get, and what does it not include?",
    ["At the " + _a(BK, "bookkeeping level") + " you get categorised transactions, reconciled accounts, monthly financial reports and basic profit and loss reporting. The " + _a(ACC, "accounting services") + " level adds individual and business tax preparation on top of that.",
     "What bookkeeping does not include is the structured close, financial statement preparation, budget against actual reporting and KPI tracking. Those are controller work, and our " + _a("bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller or CFO guide") + " explains the difference in plain terms. You move up a level when the business does, not before."]),
   ("What does the process need from you?",
    ["Less than most owners expect, and it is the same three things every month. Keep business spending on business accounts. Send the documents for anything that is not obvious from the bank line. Answer the monthly question list.",
     "That is genuinely it. If you want to know whether your own books are in a state where this can start, say so on the free 30-minute call and we will look. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288, and every message gets a reply within one business day."]),
 ],
 "faq": [
   ("How often do you need something from me?", "Once a month, as a short list of questions about transactions nobody can place from the bank line alone. It usually takes a few minutes to answer."),
   ("What if I am behind by a year?", "That is common. Catch-up work is scoped on its own so the one-time cost is clear, and the monthly rhythm starts once the books are current."),
   ("Do I have to change accounting software?", "Usually not. We work with the major platforms and will say plainly if your current setup is holding you back before recommending any change."),
   ("When do the reports arrive?", "On a date agreed at the start of the engagement. A reporting date you can plan around matters more than a fast one you cannot."),
 ],
},

{
 "slug": "how-to-choose-a-bookkeeping-service",
 "cat": "Bookkeeping",
 "pillar": "bookkeeping",
 "intent": "best",
 "title": "How to Choose a Bookkeeping Service",
 "desc": "What separates a bookkeeping service worth paying from one that just files your transactions somewhere, and the checks to make before you sign anything.",
 "keywords": "how to choose a bookkeeping service, best bookkeeping service, bookkeeping company Wilmette, choosing a bookkeeper",
 "read": "6 min read",
 "lede": "Choose a bookkeeping service on how the work runs rather than on the monthly price. Who does the categorising, what happens when a transaction is unclear, when reports arrive, what is excluded, and whether anyone reviews the file before it becomes your tax return. Those five answers separate the field quickly.",
 "sections": [
   ("Who actually does the work?",
    ["Ask who will see your transactions each month and whether you can reach that person. In some arrangements the person who sells the service and the person who does it never speak, which is fine until something is unusual and nobody knows the business well enough to notice.",
     "At NorthPeak the founder, Chaudhry Ahmad, is the person you deal with, and he brings controller-level experience to the work. That matters for a reason that is not obvious: bookkeeping done with the reporting in mind produces a file that a lender, a preparer or a future controller can use. Bookkeeping done as data entry produces a file that has to be redone."]),
   ("What happens when a transaction is unclear?",
    ["This is the question that tells you the most. Every month has transactions that cannot be identified from the bank line alone. There are only three things a service can do with them: guess, park them somewhere and forget, or ask you.",
     "Asking is the only correct answer, and the shape of the asking matters. A short monthly list you can answer in a few minutes works. A message every time something comes up does not, and neither does a silence that turns into a suspense account nobody clears."]),
   ("What do you get each month, and when?",
    ["Ask for the deliverables by name and the date they arrive. At the bookkeeping level that is categorised transactions, reconciled accounts, monthly financial reports and basic profit and loss reporting, on a schedule agreed at the start.",
     "Then ask the harder version: what is not included. Tax preparation, a structured monthly close, financial statement preparation, budget against actual reporting and KPI tracking are all real work and none of them is bookkeeping. On this site they sit at the " + _a(ACC, "accounting services") + " and " + _a(CTR, "controller services") + " levels, and knowing which level you are buying is how you avoid an invoice conversation later."]),
   ("How is the price set?",
    ["Scope, not hours. The work follows transaction volume, the number of accounts and entities, whether payroll or sales tax is involved, and how much cleanup is waiting. A service that quotes before looking at any of that is either padding for the unknown or about to be surprised.",
     "Hourly billing is the arrangement where the invoice is a surprise every month and the incentive runs the wrong way. Every NorthPeak engagement is quoted individually as a fixed figure in writing after the free 30-minute call, and that figure does not move unless the scope does. Our guide to " + _a("accountant-cost-small-business.html", "what an accountant costs a small business") + " sets out what drives the number."]),
   ("What are the warning signs?",
    ["A service that will not say what is excluded. A quote with no reporting date. Books that are described as fine before anyone has opened them. An answer to the unclear-transaction question that is any version of we handle it. And a firm that never says you do not need us yet.",
     "That last one is a real test. Some owners should keep doing their own books for another year, and a service that cannot say so is selling rather than advising. " + _a(CONTACT, "Book a free consultation") + " or call (847) 644-2288, and if the honest answer for your business is not yet, that is the answer you will get."]),
 ],
 "faq": [
   ("Is a local bookkeeper better than a remote one?", "Not automatically. The work itself is remote either way: connected bank feeds, shared software and scheduled video reviews. NorthPeak is based in Wilmette, Illinois, and works with clients nationwide."),
   ("Should I choose on price?", "Only between quotes that cover the same scope. Two bookkeeping quotes are often two different jobs, and the cheaper one is usually missing tax preparation, the reconciliation of a second account, or the cleanup."),
   ("How do I know my books are being done properly?", "Ask to see a reconciliation report and the month's question list. Accounts that agree with their statements and a list of items somebody asked about are the two signs that a human looked."),
   ("Can I switch bookkeeping services mid-year?", "Yes, and it is common. Ask what you take with you: the file, the chart of accounts, the reconciliations and the documents should all be yours."),
 ],
},

{
 "slug": "questions-to-ask-a-bookkeeper",
 "cat": "Bookkeeping",
 "pillar": "bookkeeping",
 "intent": "questions",
 "title": "Questions to Ask a Bookkeeping Service Before You Hire",
 "desc": "The questions that make a bookkeeping engagement work: who does it, how unclear items are handled, what arrives each month, and what is excluded.",
 "keywords": "questions to ask a bookkeeper, hiring a bookkeeper, bookkeeping interview questions, bookkeeping services Wilmette",
 "read": "5 min read",
 "lede": "The useful questions for a bookkeeper are about the routine, not the resume. Who does the work each month, what happens to a transaction nobody can identify, when the reports land, what is outside the scope, and what happens if the books turn out to be further behind than either of us thought.",
 "sections": [
   ("Who will be doing my books, and can I reach them?",
    ["Ask for a name, and ask whether that person is the one you speak to when something is odd. A bookkeeping file has judgement in it, and judgement needs somebody who knows what the business does.",
     "Then ask what happens when that person is away. A service with an answer has thought about continuity. A service without one has not, and you will find out in the month it matters."]),
   ("What happens to a transaction you cannot identify?",
    ["The right answer is that it goes on a list and comes to you. Ask how often that list arrives and how long it usually is.",
     "Listen for the alternative answers, because they are common. Categorising it as miscellaneous, leaving it in a suspense account, or deciding based on the vendor name are all ways of producing a tidy-looking file that is quietly wrong. Our guide to " + _a("bookkeeping-mistakes-that-cost-money.html", "bookkeeping mistakes that cost money") + " goes through what that costs at tax time."]),
   ("What arrives each month, and on what date?",
    ["Ask for the list and the date together. Categorised transactions, reconciled accounts, monthly financial reports and basic profit and loss reporting is the bookkeeping deliverable, and a date you can plan around is worth more than a promise of speed.",
     "Ask what a reconciliation means in their answer. It should mean every account matched against its statement with any difference explained, not a balance that has been made to agree."]),
   ("What is not included?",
    ["This is the question that decides whether the first invoice surprises you. Tax preparation, a structured monthly close, financial statement preparation, budget against actual reporting, KPI tracking and payroll are all separate work.",
     "On this site, tax preparation sits with " + _a(ACC, "accounting services") + " and the close and the reporting structure sit with " + _a(CTR, "controller services") + ". Ask where each one sits in the arrangement you are being offered."]),
   ("How is the fee set, and what would change it?",
    ["Ask for a fixed figure in writing before any work begins, and ask what would move it. Volume, entities, payroll, sales tax in more than one state and the state of the books when you arrive are the honest answers.",
     "Then ask the catch-up question. If the books are further behind than expected, is that scoped separately or does it appear on a monthly invoice. Separately is the answer that keeps the one-time cost visible.",
     _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288 and ask us every question on this page."]),
   ("Will you tell me if I do not need you?",
    ["Ask it directly. An owner with a dedicated business account, software connected to the bank and a monthly reconciliation habit can carry a small, simple business a long way on their own, and our " + _a("diy-bookkeeping-or-hire.html", "do it yourself or hire guide") + " sets out where that stops paying.",
     "A service that has never once told a caller to keep doing it themselves is not in the advice business. The first call here sometimes ends that way."]),
 ],
 "faq": [
   ("How much do these questions matter for a very small business?", "More, not less. A small business has fewer transactions to hide a bad habit in, and the cost of unwinding a year of wrong categories is the same whatever the size."),
   ("Should I ask for references?", "You can, and the more useful version is asking to see a sample monthly report pack with the numbers changed. It shows you what you will actually receive."),
   ("What if I do not understand the answers?", "Say so. A bookkeeper who cannot explain the monthly routine in plain words to the owner of the business is going to be just as unclear in month seven."),
   ("Is the first conversation free?", "Yes. It is a 30-minute call about your business and your books, with no obligation, and every message gets a reply within one business day."),
 ],
},

{
 "slug": "bookkeeping-alternatives",
 "cat": "Bookkeeping",
 "pillar": "bookkeeping",
 "intent": "alternatives",
 "title": "Bookkeeping Alternatives, and When Each One Wins",
 "desc": "Software on its own, a part-time person, a bookkeeping service or a full accounting firm. What each covers, what it leaves to you, and when each one wins.",
 "keywords": "bookkeeping alternatives, bookkeeping software vs bookkeeper, part time bookkeeper, outsourced bookkeeping",
 "read": "6 min read",
 "lede": "There are four honest ways to get bookkeeping done, and the cheapest one is right for more businesses than any bookkeeper will admit. Software with your own discipline, a part-time person, an outsourced service, or a firm that carries the tax work too. Which wins depends on volume, complexity and what your own hours are worth.",
 "sections": [
   ("When does software plus your own discipline win?",
    ["When the business is small and simple and the habits are good. A dedicated business account and card, software connected to the bank so most transactions categorise themselves, receipts photographed at the point of purchase, and a reconciliation against the statement once a month.",
     "That routine will carry a solo operator or a small service business a long way, and our " + _a("bookkeeping-basics.html", "bookkeeping basics guide") + " is the whole of it. The work is not hard. It is relentless, and it has to happen every month whether you feel like it or not.",
     "It stops winning at the point where your hours on the books are worth more in the business, or where the first employee, a second entity, inventory or sales tax in more than one state arrives."]),
   ("When does a part-time person win?",
    ["When the volume is real but the work is routine and you want somebody whose only job is your books. It can be the least expensive way to buy hours, and for a business with a steady, unchanging pattern it works.",
     "The trade is what happens around the edges. One person is one person's judgement, one person's availability and one person's continuity. Ask what happens when they are away, and ask who reviews the file before it becomes a tax return."]),
   ("When does an outsourced bookkeeping service win?",
    ["When you want the monthly routine to happen without managing it, and you want the file to be usable by whoever needs it next. That is what the " + _a(BK, "bookkeeping level") + " on this site is: categorised transactions, reconciled accounts, monthly financial reports and basic profit and loss reporting, on an agreed date, quoted as a fixed figure in writing.",
     "It also wins when the books are behind. Catch-up and clean-up work is common and is scoped separately from the ongoing service, so the one-time effort has its own number rather than hiding inside a monthly fee."]),
   ("When does a firm that also does the tax work win?",
    ["When you would rather not hand a year of records to a stranger in March. " + _a(ACC, "Accounting services") + " here is bookkeeping plus individual and business tax preparation, which means the return is a transfer from clean books rather than a reconstruction.",
     "It also wins when tax planning matters rather than just filing, and our guide on " + _a("tax-planning-vs-tax-prep.html", "tax planning versus tax preparation") + " explains why those are different jobs. A preparer who has not seen the books until April can only report what happened."]),
   ("Is there an option above all of these?",
    ["Yes, and it is worth knowing about even if you do not need it yet. When the questions stop being about whether last month is right and start being about structure, the next level is " + _a(CTR, "controller services") + ": a structured monthly close, financial statement preparation, budget against actual reporting and KPI tracking.",
     "That is a different job from bookkeeping, and our " + _a("bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller or CFO guide") + " sets out where each one starts and stops. You move up a level when the complexity does."]),
   ("How do you choose between them?",
    ["Count last month's hours on the books and what you would have done with them instead. List anything that changed this year: staff, states, entities, revenue. If either list makes you wince, the answer is further down this page than where you are now.",
     "If it does not, keep doing what you are doing for another year. " + _a(CONTACT, "Book the free 30-minute call") + " or phone (847) 644-2288 and we will say plainly which of these fits, including if the answer is none of them yet."]),
 ],
 "faq": [
   ("Can software really replace a bookkeeper?", "It replaces the typing, not the checking. Software categorises and a person confirms, clears the suspense account, and asks about the transactions that do not make sense. Which of those you need depends on how much judgement your month contains."),
   ("Is outsourced bookkeeping more expensive than hiring someone?", "It depends on the volume and on what you count. An outsourced service is quoted for a scope; an employee carries payroll, taxes, software and cover when they are away. The comparison only works when both sides are complete."),
   ("Can I start with software and move later?", "Yes, and most businesses do. Keep the accounts separate and the records clean from day one and the move costs very little. Mixed personal and business spending is what makes it expensive."),
   ("What if I am somewhere between two of these?", "Say so on the call. Plenty of arrangements are split: you keep the daily habits and hand over the monthly close, the reconciliations and the reporting."),
 ],
},
# ===================================================================
# ACCOUNTING SERVICES
# ===================================================================
{
 "slug": "how-accounting-services-work",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "how",
 "title": "How Accounting Services Work, Month by Month",
 "desc": "What an accounting engagement actually looks like from the first call to the first report, through the monthly rhythm, and into the return at year end.",
 "keywords": "how accounting services work, monthly accounting process, working with an accountant, accounting services Wilmette",
 "read": "6 min read",
 "lede": "Accounting services run on a monthly cycle with a year-end at the end of it. Transactions are categorised and accounts reconciled every month, reports arrive on an agreed date, and the tax return at the end is a transfer from clean books rather than a reconstruction. Here is each stage and what it needs from you.",
 "sections": [
   ("What happens before anything starts?",
    ["A free 30-minute call. It is a conversation about the business and the books rather than a pitch, and it ends with a plain answer about what would help most, including the answer that you do not need us yet.",
     "If it goes further, you get a written scope and a fixed figure before any work begins. That scope names what is included, what is excluded and when reports arrive. Every message gets a reply within one business day, which matters more in the first fortnight than at any other point."]),
   ("What does onboarding involve?",
    ["Connecting the accounts the business actually uses, agreeing a chart of accounts that matches how you describe the business, and settling the reporting date. If the categories have drifted, they get sorted here rather than carried forward.",
     "If the books are behind, catch-up is scoped as its own piece of work with its own number. That is the point of separating it: you can see the one-time effort against the recurring service instead of finding it folded into a monthly fee. Our article on " + _a("how-long-month-end-close-takes.html", "how long a close takes") + " covers what catching up looks like in practice."]),
   ("What does the monthly rhythm look like?",
    ["Transactions are categorised as they arrive and documents are attached while everyone still remembers what they were. At the end of the month every account is reconciled against its statement, and anything that cannot be identified from the bank line comes back to you as a short list of questions.",
     "Then the reports go out on the agreed date: monthly financial reports and basic profit and loss reporting. That is the moment the numbers are useful, and it is why the date matters more than the speed.",
     "This is the " + _a(BK, "bookkeeping") + " engine underneath the service. What accounting services add on top of it is the tax work."]),
   ("What happens at year end?",
    ["Individual and business tax preparation, from books that have been reconciled every month rather than assembled in March. That is the whole argument for the monthly rhythm: the return becomes a transfer rather than a reconstruction, and the questions that come up are about decisions rather than about what a transaction was.",
     "It is also where planning and preparation separate. Preparation reports what happened. Planning happens during the year, while there is still something to decide, and our guide on " + _a("tax-planning-vs-tax-prep.html", "tax planning versus tax preparation") + " sets out the difference."]),
   ("What happens when the business outgrows this?",
    ["The signs are consistent. Decisions start waiting on numbers you do not have. A lender or a partner asks for statements rather than a return. You know revenue but not which services actually make money. At that point the next level is " + _a(CTR, "controller services") + ": a structured monthly close, financial statement preparation, budget against actual reporting and KPI tracking.",
     "Moving up is a conversation rather than a new firm, and each level includes everything below it. " + _a(CONTACT, "Book a free consultation") + " or call (847) 644-2288 and we will say which level fits."]),
 ],
 "faq": [
   ("How long before the first report arrives?", "It depends on how current the books are when we start. Clean, current books settle into the monthly rhythm quickly; a year of catch-up is scoped and completed first."),
   ("Do I need to be in Wilmette?", "No. The practice is based in Wilmette, Illinois, and works with clients remotely nationwide through scheduled video reviews."),
   ("Is tax preparation really included?", "Yes. Individual and business tax preparation is part of the Starter package and carries through every level above it."),
   ("What if my business changes mid-year?", "Tell us when it happens rather than at year end. A new entity, a first employee or sales in a second state each change the work, and the scope is adjusted rather than silently absorbed."),
 ],
},

{
 "slug": "how-to-choose-an-accounting-firm",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "best",
 "title": "How to Choose an Accounting Firm and Which Services You Need",
 "desc": "How to compare a solo practitioner, a regional firm and an online service, what titles do and do not tell you, and the checks that matter before you sign.",
 "keywords": "how to choose an accounting firm, best accounting firm for small business, choosing an accountant, accounting firm Wilmette",
 "read": "6 min read",
 "lede": "Choose an accounting firm by what you will actually receive and who will produce it, not by the size of the firm. The choice is usually between a solo practitioner, a regional firm and an online service, and each one is a genuinely different arrangement with different things going for it.",
 "sections": [
   ("Which services do you actually need?",
    ["Start here, because it changes the shortlist. Bookkeeping and monthly reports is one job. Adding individual and business tax preparation is another. A structured monthly close, financial statement preparation and budget against actual reporting is a third, and it is controller work rather than accounting work.",
     "Write down which of those you need this year. A firm that is excellent at one of them and thin on another is a fine choice if you only need the first, and an expensive mistake if you need all three. The " + _a(SERVICES, "three levels on this site") + " are laid out that way on purpose."]),
   ("What do the three kinds of firm each do well?",
    ["A solo practitioner gives you one person who knows the business, which is the best possible arrangement until that person is unavailable. Ask about continuity and about who reviews the work.",
     "A larger firm gives you cover and depth, and the trade is that the person who sells the engagement may not be the person who does it. Ask who will actually see your transactions each month.",
     "An online service gives you a price and a platform. It works well for a simple, high-volume, unchanging business, and it works badly the first time something is unusual, because there is nobody whose job it is to notice."]),
   ("What do titles tell you, and what do they not?",
    ["Less than people assume, in both directions. A title tells you somebody met a standard at a point in time. It does not tell you whether they will reconcile your accounts every month, answer within a business day, or say when you do not need them.",
     "So ask about the work rather than the letters. What is the monthly routine, who performs it, what arrives and when, and what happens when a transaction cannot be identified. To be plain about our own position, the About page describes Chaudhry Ahmad as founder and principal with controller-level experience, and that is exactly what it means. It claims no credential beyond it, here or anywhere else on this site."]),
   ("How should the fee be set?",
    ["As a fixed figure in writing for a defined scope, after somebody has looked at your books. Fees follow transaction volume, entity count, payroll, sales tax and how much cleanup is waiting, so a number quoted before any of that is either padded or optimistic.",
     "Hourly billing is the arrangement where the invoice is a surprise every month. Our guide to " + _a("accountant-cost-small-business.html", "what an accountant costs a small business") + " goes through what drives the number and what a written quote should contain."]),
   ("What should the first conversation feel like?",
    ["Like a conversation. Ours is a free 30-minute call about the business and the books, with no obligation, and it sometimes ends with the advice to keep doing your own books for another year.",
     "The firms worth shortlisting are the ones that ask more questions than they answer in that call, and the ones that will put the scope and the exclusions in writing without being pushed. Our list of " + _a("questions-to-ask-an-accountant.html", "questions to ask an accountant") + " is the version to take into the meeting. " + _a(CONTACT, "Book a call") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Does the firm need to be local?", "Only if you want to meet in person. The work runs on connected bank feeds, shared software and scheduled video reviews, and NorthPeak works with clients nationwide from Wilmette, Illinois."),
   ("How many firms should I talk to?", "Two or three, with the same written description of what you need in front of each of them. Comparing quotes for three different scopes tells you nothing."),
   ("What should I have ready?", "Nothing formal. The last bank statement, whatever your accounting software shows, and a sense of what is not working. If the books are behind, say so; it changes nothing about the call."),
   ("Can I move firms mid-year?", "Yes, and it is common. Ask what you take with you: the file, the chart of accounts, the reconciliations and the supporting documents should all be yours."),
 ],
},

{
 "slug": "how-long-accounting-services-take",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "time",
 "title": "How Long Do Accounting Services Take to Set Up?",
 "desc": "The honest timeline for an accounting engagement: the first call, onboarding, catch-up if the books are behind, and when the monthly reports start arriving.",
 "keywords": "how long accounting services take, accounting onboarding timeline, bookkeeping catch up time, accounting services Wilmette",
 "read": "5 min read",
 "lede": "The first call takes thirty minutes and the written scope follows it. What happens after that depends almost entirely on one thing: how current your books are on the day we start. Current books settle into the monthly rhythm quickly. Books that are a year behind get caught up first, as their own piece of work.",
 "sections": [
   ("How long do the first steps take?",
    ["The free consultation is a 30-minute call, and every message that comes in gets a reply within one business day, so the gap between asking and talking is usually short.",
     "After the call you get a written scope and a fixed figure before any work begins. That is a deliberate pause rather than a delay: you should be able to read what is included and what is excluded, and ask about it, before anything is committed."]),
   ("What decides how long onboarding takes?",
    ["Access and agreement. Connecting the accounts the business uses, agreeing a chart of accounts that matches how you describe the business, and settling the reporting date are the three things that have to happen before the first month can run properly.",
     "Access is the usual hold-up, and it is the part you control. Bank and card connections, the accounting file, payroll if there is any. The faster those arrive, the faster the first month closes."]),
   ("How long does catch-up take if the books are behind?",
    ["Longer than the ongoing work, which is exactly why it is scoped separately. The length follows the volume of transactions, the number of accounts, how much documentation survives and how far the categories have drifted.",
     "Nobody can give you that number before looking, and a firm that offers one has not looked. What you should get is a scope for the catch-up with its own figure, so you can see the one-time cost against the monthly one. Our article on " + _a("how-long-month-end-close-takes.html", "how long a month-end close takes") + " covers the same question for a single month."]),
   ("When do the monthly reports start?",
    ["Once the books are current, on the reporting date agreed at the start. The date is the point: a predictable date you can plan a month around is more useful than an unpredictable fast one.",
     "The monthly rhythm itself is short from your side. Transactions are categorised and accounts reconciled by us; what comes to you is a brief list of questions about items that cannot be identified from a bank line, and answering it usually takes a few minutes. Our article on " + _a("how-bookkeeping-works-month-by-month.html", "how bookkeeping works month by month") + " walks through the whole cycle."]),
   ("What about the tax return?",
    ["It follows the books rather than the calendar panic. Individual and business tax preparation is part of the service, and when the accounts have been reconciled every month the return is a transfer from clean records rather than a reconstruction from a shoebox.",
     "That is the part of the timeline people notice most, because it is the difference between a week of hunting for documents in March and a conversation about decisions. " + _a(CONTACT, "Book the free 30-minute call") + " or phone (847) 644-2288 and we will tell you what your own situation would take."]),
 ],
 "faq": [
   ("Can you start mid-year?", "Yes. Most engagements do. The months already gone are either caught up or left with the prior preparer, and that is one of the things the first call decides."),
   ("How quickly will I hear back if I get in touch?", "Every inquiry gets a reply within one business day. If it is urgent, calling (847) 644-2288 is faster than a form."),
   ("Does catch-up have to finish before the monthly service starts?", "Usually the current month starts running while the older months are worked through, so you are not waiting on history to see this month's numbers."),
   ("What slows an engagement down most?", "Waiting on access. Bank connections, the software file and payroll details are the three things that hold up a first month more often than the bookkeeping itself does."),
 ],
},

{
 "slug": "accounting-services-alternatives",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "alternatives",
 "title": "Accounting Services Alternatives, and When Each Wins",
 "desc": "Doing it yourself, a bookkeeper plus a seasonal preparer, a full accounting service, or an in-house hire. What each one covers and when each one wins.",
 "keywords": "accounting services alternatives, alternatives to hiring an accountant, in house vs outsourced accounting, do i need an accountant",
 "read": "6 min read",
 "lede": "Hiring an accounting firm is one of four ways to get this work done, and it is not always the right one. Doing it yourself, a bookkeeper plus a preparer at year end, a full service that carries both, or somebody in-house each fit a different stage. What decides it is complexity, not revenue.",
 "sections": [
   ("When does doing it yourself still win?",
    ["When the business is simple and the habits are good. A dedicated business account, software connected to the bank, receipts captured as you go, and a monthly reconciliation will carry a small operation a long way, and our " + _a("bookkeeping-basics.html", "bookkeeping basics guide") + " is the whole routine.",
     "It stops winning on two signals. Time, when the hours on the books are worth more spent selling or delivering. And complexity, when a first employee, a second entity, inventory or sales tax in more than one state arrives, because each of those adds rules that are easy to get wrong and expensive to unwind. Our " + _a("diy-bookkeeping-or-hire.html", "do it yourself or hire guide") + " draws the line in detail."]),
   ("When does a bookkeeper plus a seasonal preparer win?",
    ["When the monthly work is routine and the tax situation is straightforward. It is a common and perfectly reasonable arrangement, and for many owners it is the cheapest thing that actually works.",
     "The seam is where it costs. The preparer sees the books once, in the spring, and can only report what happened. Nobody is planning during the year, and nobody with the tax picture in mind is looking at how the books are being kept. That gap is the argument for the next option, and our guide on " + _a("tax-planning-vs-tax-prep.html", "planning versus preparation") + " explains why it matters."]),
   ("When does a full accounting service win?",
    [_a(ACC, "Accounting services") + " here means bookkeeping, reconciliations, monthly reports and individual and business tax preparation from one place. It wins when you want the return to be a transfer from clean books rather than a reconstruction, and when you would rather have one conversation than manage two suppliers.",
     "It also wins when the books are behind, because catch-up and clean-up is scoped separately with its own figure and then the monthly rhythm starts. And it wins when you want somebody to say plainly which level you need, including that you do not need the next one yet."]),
   ("When does hiring in-house win?",
    ["When the volume is large enough that a person is busy every day, and when having somebody in the building matters for how the business runs. A full-time hire buys availability and context that an outside firm cannot match.",
     "The comparison only works when both sides are complete. An in-house salary carries payroll costs, software, recruitment, holiday cover and the risk that one person is the only one who knows how anything is filed. An outside engagement is a fixed figure for a defined scope. Neither is automatically cheaper, and the honest answer depends on the volume."]),
   ("What about the level above all of these?",
    ["If the question you are asking is not whether last month is right but what next year looks like, this is the wrong page. That is " + _a(CTR, "controller services") + " for structure and " + _a(CFO, "CFO advisory") + " for the forward view, and our " + _a("bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller or CFO guide") + " sets out where each starts.",
     "Whichever of these fits, the way to find out is the same. " + _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288, and if the honest answer is that you should carry on as you are, that is the answer you will get."]),
 ],
 "faq": [
   ("Is an accounting firm always more expensive than a bookkeeper?", "For the same work, usually, because the work is not the same: tax preparation is included. Compare the two arrangements complete rather than line by line."),
   ("Can I keep my bookkeeper and add tax help?", "Yes, and plenty of businesses do. Say so at the start so the scope is written that way rather than overlapping with what you already pay for."),
   ("How do I know which of these I am ready for?", "Count the hours you spent on the books last month and list what changed in the business this year. Those two answers move most people to the right row on this page."),
   ("Does moving between these options lose anything?", "Not if the records are clean. The file, the chart of accounts, the reconciliations and the documents should always be yours to take."),
 ],
},
# ===================================================================
# CONTROLLER SERVICES
# ===================================================================
{
 "slug": "how-to-choose-a-controller",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "best",
 "title": "How to Choose a Controller and What the Services Include",
 "desc": "What controller services should deliver, how to tell a real close from a report pack, and what separates a controller from a bookkeeper with a title.",
 "keywords": "how to choose a controller, fractional controller, controller services for small business, choosing a controller",
 "read": "6 min read",
 "lede": "Choose a controller on the deliverables and the calendar rather than on the word. A controller owns a structured monthly close, produces statements somebody outside the business could rely on, compares budget against actual and tracks the measures you chose together. If those four are not named in writing, you are buying a title.",
 "sections": [
   ("What should controller services actually deliver?",
    ["Four things, and they are worth naming one at a time. Controller-level oversight, which means somebody is responsible for the file rather than working in it. A structured monthly close, which means the month ends on a date and the accounts are reconciled and reviewed by then. Financial statement preparation. And budget against actual reporting with KPI tracking, plus a monthly review call.",
     "That list is the " + _a(CTR, "controller services") + " level on this site, and it is the checklist to hold any other offer against. Our article on " + _a("how-controller-services-work.html", "how controller services work") + " walks through the month itself."]),
   ("How do you tell a close from a report pack?",
    ["A report pack is a set of documents produced from whatever the file contained on the day. A close is a process that finishes: cut-off applied, accruals recorded, every account reconciled, the review done and the month locked so the numbers do not move afterwards.",
     "So ask two questions. On what date does the month close, and what happens if a transaction turns up afterwards. A controller has an answer to both. If the answer to the second one is that the numbers just change, you do not have a close, and anything built on those statements is being built on sand."]),
   ("Who is doing the work, and what are they responsible for?",
    ["Ask whether the controller performs the bookkeeping or reviews it, and who does whichever they do not. Both arrangements work; not knowing which one you have does not.",
     "Then ask what they are on the hook for. A controller who owns the close owns the deadline, the reconciliations and the accuracy of the statements. At NorthPeak the founder, Chaudhry Ahmad, brings controller-level experience and is the person you deal with, which is what the About page says and the whole of what it claims."]),
   ("Fractional or full-time?",
    ["Fractional first, almost always. A full-time controller is a salary plus payroll costs, software, recruitment and cover, and the work in a growing business rarely fills the week until quite late. Fractional buys the same deliverables for the hours the business actually needs.",
     "The point at which the answer flips is when somebody needs to be in the building every day, or when the volume genuinely fills a role. Our article on " + _a("controller-cost-fractional-vs-full-time.html", "controller cost, fractional versus full time") + " compares the two properly."]),
   ("What should the engagement look like on paper?",
    ["A named list of deliverables, a close date, a reporting date, the frequency of the review call, and what is excluded. Then a fixed figure in writing, agreed after the free 30-minute call, that does not move unless the scope does.",
     "And one more thing that is easy to skip: what happens in the first month, when the close usually has to be built rather than run. A controller who has thought about the first month has done this before. " + _a(CONTACT, "Book a consultation") + " or call (847) 644-2288."]),
 ],
 "faq": [
   ("Do I need a controller if I already have a bookkeeper?", "Possibly. A bookkeeper records and reconciles; a controller owns the close and the statements and reviews the work. Our bookkeeper, controller or CFO guide sets out where one ends and the other starts."),
   ("Can the same firm do both?", "Yes, and here each level includes everything below it, so controller services sit on top of the bookkeeping rather than beside it."),
   ("How often should we meet?", "A monthly review call is part of the controller level. If nobody is reading the statements with you, the reporting is decoration."),
   ("What size business needs a controller?", "Size matters less than structure. The Growth package is built for businesses in the range of about five hundred thousand to five million in revenue, but the real signal is a close that never closes."),
 ],
},

{
 "slug": "controller-services-mistakes",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "mistakes",
 "title": "Controller Services Mistakes That Cost Money",
 "desc": "The mistakes that make controller-level work expensive and useless: a close that never closes, a budget nobody reads, borrowed KPIs, and reports nobody reviews.",
 "keywords": "controller services mistakes, month end close problems, budget vs actual reporting, controller for small business",
 "read": "6 min read",
 "lede": "The expensive mistakes at controller level are not errors in the numbers. They are processes that produce numbers nobody uses: a close with no date, a budget nobody compares against, measures copied from somebody else's business, and a monthly pack that lands in an inbox and stops there.",
 "sections": [
   ("What does a close with no date cost?",
    ["Everything downstream. If the month never formally ends, the statements keep changing, the comparison to last month compares two different things, and nobody can say whether a decision made in week three was based on the truth.",
     "A structured close has a date, a sequence and a finish. Cut-off applied, accruals recorded, accounts reconciled, the review done, the month locked. Our article on " + _a("how-long-month-end-close-takes.html", "how long a month-end close takes") + " sets out what that timeline realistically looks like, and the fix is almost always a date rather than more effort."]),
   ("Why does a budget nobody compares against cost money?",
    ["Because it takes the effort of building a budget and returns none of it. A budget only does work in the comparison: this is what we said, this is what happened, this is the difference and here is why. Budget against actual reporting is the deliverable, not the budget itself.",
     "The failure is usually quiet. The budget is built in January, the year happens, and nobody looks until the following January. By then the difference is history rather than a decision."]),
   ("What goes wrong with borrowed KPIs?",
    ["A business tracks the measures an article recommended for a different industry, produces them faithfully every month, and learns nothing. Measures have to be chosen for the business and for a decision somebody is actually going to make.",
     "The test is simple: for each number on the pack, name the decision it would change. If nobody can, it is a number rather than a measure, and the effort of producing it is a cost with no return."]),
   ("What happens when nobody reviews the reports?",
    ["The reporting becomes decoration. This is the most common failure of all, and it is the reason a monthly review call is part of controller services rather than an optional extra. Statements read with somebody who can explain the movement are worth several times the same statements arriving alone.",
     "It is also where errors get caught. The person who knows what the business did in a month is the owner, and the month where an unusual number is not questioned is the month a mistake survives into the return."]),
   ("What is the mistake of buying the wrong level?",
    ["Two versions, in opposite directions. Buying controller work when the bookkeeping is not reliable means building a close on a file that is not right, which produces confident wrong statements. Fix the foundation first.",
     "And buying " + _a(CFO, "CFO advisory") + " when what is missing is the close. Forecasting from statements you cannot trust is the most expensive way to be wrong, and the honest advice is usually to fix the reporting first. Our " + _a("bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller or CFO guide") + " is the map. " + _a(CONTACT, "Book a free consultation") + " or call (847) 644-2288 and we will say which level fits."]),
 ],
 "faq": [
   ("How do I know if our close is really closing?", "Ask what date the month closes and what happens to a transaction that arrives after it. Two clear answers mean a close. Anything vaguer means a report pack."),
   ("Is a monthly review call really necessary?", "It is the difference between reporting that changes decisions and reporting that fills a folder. It is included at the controller level here for that reason."),
   ("What if our KPIs were set by a previous adviser?", "Keep the ones that would change a decision and retire the rest. A shorter pack that gets read beats a longer one that does not."),
   ("Can these problems be fixed without changing firms?", "Often, yes. A date for the close, a comparison nobody skips and a call to read the results together fix most of this page without anyone new being hired."),
 ],
},

{
 "slug": "questions-to-ask-a-fractional-controller",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "questions",
 "title": "Questions to Ask Before You Buy Controller Services",
 "desc": "The questions that decide whether controller services are real: the close date, who reviews, what the statements are fit for, and what is excluded.",
 "keywords": "questions to ask a fractional controller, hiring a controller, controller services questions, month end close",
 "read": "5 min read",
 "lede": "Controller services are easy to describe and hard to compare, because two firms can use the same words for very different work. These are the questions that make the difference visible: the close date, who performs and who reviews, what the statements are fit for, and what happens in the first month.",
 "sections": [
   ("On what date does the month close?",
    ["Ask for a date, not a range. The answer tells you whether there is a process or an intention, and it is the single most useful question on this page.",
     "Then ask the follow-up: what happens if something arrives after that date. It should go into the following month with an explanation, not quietly reopen a month you have already acted on."]),
   ("Who performs the bookkeeping, and who reviews it?",
    ["Both jobs have to exist. If the same person records the transactions and signs off the close, ask what the review actually consists of, because a review of your own work is a proofread.",
     "Ask who you speak to when something looks wrong. A controller engagement should have one person who is responsible for the file and reachable about it."]),
   ("What are the statements fit for?",
    ["This sounds abstract and it is not. Ask directly: could these statements go to a lender, an investor or a buyer as they are. The answer shapes what the close has to include, and a firm that says yes should be able to say why.",
     "Ask what the pack contains too. Financial statement preparation, budget against actual reporting and KPI tracking is what the " + _a(CTR, "controller level") + " on this site includes, and the list is worth reading against any other offer."]),
   ("How does the review call work?",
    ["Ask how often, who is on it, and what is expected of you. A monthly review call is part of the controller level here, and it exists because reporting nobody reads changes nothing.",
     "Ask what happens between calls when a number looks wrong. Waiting three weeks to ask a question about last month is how a small error becomes a year-end problem."]),
   ("What is excluded, and what happens in month one?",
    ["Exclusions first: tax preparation, payroll, forecasting and modelling, and anything at " + _a(CFO, "CFO advisory") + " level are each separate work. Ask which of them are in the number you have been quoted.",
     "Then the first month, which is the one nobody asks about. Usually the close has to be built rather than run: reconciliations brought current, a chart of accounts agreed, a reporting calendar set. Ask what that involves and whether it is priced separately. Our article on " + _a("how-controller-services-work.html", "how controller services work") + " describes what happens before the first close.",
     _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288 and ask us every question on this page."]),
 ],
 "faq": [
   ("How is a fractional controller priced?", "As a fixed figure for a defined scope, quoted individually after the discovery call and confirmed in writing before work begins. Hourly billing makes the invoice a monthly surprise."),
   ("Do I need to be near Wilmette?", "No. The work runs remotely with scheduled video reviews. Local clients can meet in person when that is useful."),
   ("What if our bookkeeping is not reliable yet?", "Then that gets fixed first. A close built on an unreliable file produces confident wrong statements, and any honest answer says so before taking the engagement."),
   ("Can we start with a review rather than an engagement?", "Ask. The free 30-minute call is where that gets decided, and sometimes the answer is that the close you have is fine and something else is the problem."),
 ],
},

{
 "slug": "diy-controller-work-or-hire",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "diy",
 "title": "Controller Services: Do It Yourself or Hire It Out",
 "desc": "Which parts of controller-level work an owner or an existing bookkeeper can genuinely do, which parts need somebody else, and how to tell which side you are on.",
 "keywords": "do i need a controller, controller work yourself, bookkeeper doing controller work, fractional controller",
 "read": "6 min read",
 "lede": "Some controller work is genuinely available to an owner with good habits: setting a close date, insisting on a budget comparison, choosing the measures that matter. What is hard to do yourself is the review, because reviewing your own file is proofreading your own writing, and the errors that survive are the ones you cannot see.",
 "sections": [
   ("What can an owner do without hiring anyone?",
    ["More than most owners try. Set a date for the month to close and hold it. Ask for a comparison of budget against actual every month, even a rough one. Choose three or four measures you would actually act on and drop the rest. Read the statements with somebody once a month rather than filing them.",
     "None of that requires a title, and all of it is free. If a business does those four things consistently for a year, the reporting improves out of recognition without a single new engagement."]),
   ("What can an existing bookkeeper take on?",
    ["Often the mechanics of a structured close: cut-off, accruals, reconciling every account rather than the main one, and producing the pack on a date. A capable bookkeeper who is given the calendar and the checklist can run most of that.",
     "What does not transfer is the review. Somebody has to look at the finished month with fresh eyes and ask why a number moved, and that cannot be the person who produced it. That is the structural reason controller work exists as a separate role rather than as extra hours for the same person."]),
   ("Where does doing it yourself stop paying?",
    ["Three places. When the statements need to satisfy somebody outside the business, because a lender, an investor or a buyer reads them differently from an owner. When the volume or the entity count means the close takes longer than the month can absorb. And when a decision is waiting on numbers you do not fully trust.",
     "That last one is the expensive version. Making a hiring, leasing or financing decision on statements nobody has reviewed costs more than the review would have, and the cost does not show up until later."]),
   ("What does the middle option look like?",
    ["The arrangement most growing businesses land on. The bookkeeping stays where it is, the owner keeps the daily context, and controller-level oversight sits on top: the close is structured, the statements are prepared, budget against actual is compared and there is a monthly review call.",
     "That is exactly what the " + _a(CTR, "controller services") + " level is, and each level includes everything below it, so nothing has to be moved for it to sit on top. Our article on " + _a("how-controller-services-work.html", "how controller services work") + " describes the month."]),
   ("How do you tell which side you are on?",
    ["Answer four questions honestly. Does the month close on a date. Are all the accounts reconciled, not just the main one. Is there a budget somebody compares against. Does anyone read the statements with you.",
     "Four yeses and you are running controller work already, whoever is doing it. Two or fewer and the gap is the thing costing money, not the fee. " + _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288 and we will tell you which of those four you are missing."]),
 ],
 "faq": [
   ("Can my bookkeeper just become our controller?", "Sometimes, with the calendar, the checklist and somebody else doing the review. The review is the part that cannot be self-performed."),
   ("Is software an alternative to a controller?", "It helps with the mechanics and not with the judgement. Software will produce a pack on a schedule; it will not ask why margin fell in a month when revenue rose."),
   ("What if we only need this for part of the year?", "Say so on the call. Some engagements are shaped around a financing round or a sale process, with the ongoing arrangement decided afterwards."),
   ("Does this replace our accountant?", "No. Tax preparation is separate work and sits at the accounting services level here, which controller services include rather than replace."),
 ],
},

{
 "slug": "controller-services-alternatives",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "alternatives",
 "title": "Controller Services Alternatives, and When Each Wins",
 "desc": "A bookkeeper plus an accountant, a fractional controller, a full-time hire, or better software. What each option really covers and when each one wins.",
 "keywords": "controller services alternatives, fractional vs full time controller, alternatives to hiring a controller, outsourced controller",
 "read": "6 min read",
 "lede": "There are four ways to get controller-level work into a business, and the differences are about ownership rather than tools. A bookkeeper plus an accountant, a fractional controller, a full-time hire, or software with somebody senior reviewing it. What decides between them is who owns the close.",
 "sections": [
   ("When does a bookkeeper plus an accountant win?",
    ["When the business is straightforward and nobody outside it is reading the numbers. The bookkeeper keeps the accounts and the accountant prepares the return, and for a great many businesses that is genuinely enough.",
     "The gap is in the middle, and it is a real one. Neither role owns the monthly close, prepares statements to be relied on, or compares budget against actual. That is fine right up until somebody asks for statements or a decision needs a number you can trust."]),
   ("When does a fractional controller win?",
    ["When the gap in the middle starts to cost something, which is usually earlier than owners expect. A fractional arrangement buys the deliverables without buying a full-time role: controller-level oversight, a structured monthly close, financial statement preparation, budget against actual reporting, KPI tracking and a monthly review call.",
     "It also wins because it scales with the business rather than in steps. You move up when the complexity does, and each level includes everything below it. Our comparison of " + _a("controller-cost-fractional-vs-full-time.html", "fractional and full-time controller cost") + " sets out both sides."]),
   ("When does a full-time hire win?",
    ["When the work genuinely fills a role and somebody needs to be in the building. A full-time controller brings availability, context and the ability to be interrupted, and none of those is small.",
     "The comparison has to be complete to be honest. A salary carries payroll costs, software, recruitment, holiday cover and key-person risk, and the role has to be managed by somebody who knows what good looks like. That last one is the part most businesses discover late."]),
   ("Is better software an alternative?",
    ["Partly, and it is worth saying plainly rather than dismissing it. Modern platforms handle consolidation, reporting and the mechanics of a close far better than they used to, and they will produce a pack on a schedule without anyone remembering to.",
     "What they will not do is own the close, apply judgement to an unusual month, or ask why margin fell when revenue rose. Software makes controller work faster. It does not make it unnecessary, and a business that has bought a platform instead of a process usually has better-looking reports and the same problem."]),
   ("What about going straight to CFO advisory?",
    ["It is the most common expensive mistake in this area. Forecasting and modelling built on statements nobody closed produces confident answers to the wrong question, and our " + _a("do-you-need-a-cfo-yet.html", "do you need a CFO yet") + " guide is blunt about it: if the books are not reconciled monthly and the statements are not trusted, the foundation comes first.",
     "The order is bookkeeping, then controller, then " + _a(CFO, "CFO advisory") + ", and each level includes the ones below it. Skipping a step does not save money; it moves the cost somewhere less visible."]),
   ("How do you decide?",
    ["Ask who owns the close today. If the answer is nobody, that is the gap, and everything on this page is a different way of filling it.",
     "Then ask what the statements have to be fit for this year, and whether the volume fills a role. Those three answers pick the row. " + _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288 and we will tell you which one fits, including if the answer is that you do not need this yet."]),
 ],
 "faq": [
   ("Is fractional always cheaper than full-time?", "Not always, and the honest comparison includes payroll costs, software, cover and management time on the employment side. It is usually cheaper until the work fills a week."),
   ("Can we use a fractional controller alongside an in-house bookkeeper?", "Yes, and it is one of the most common arrangements. The bookkeeper records, the controller owns the close and the review."),
   ("Will changing software fix our close?", "It will change the mechanics. If the problem is that no date is set and nobody reviews the month, new software produces the same problem faster."),
   ("How do we know when to move up a level?", "When the questions being asked are about next year rather than last month. Until then, controller-level structure is usually the thing that is missing."),
 ],
},
# ===================================================================
# CFO ADVISORY
# ===================================================================
{
 "slug": "how-cfo-advisory-works",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "how",
 "title": "How CFO Advisory Works, Month by Month",
 "desc": "What a fractional CFO engagement actually looks like week to week: the foundation check, the first forecast, the strategy calls, and what changes over a year.",
 "keywords": "how cfo advisory works, fractional cfo process, cfo engagement, cash flow forecasting",
 "read": "6 min read",
 "lede": "CFO advisory is a standing conversation about the future, held on a schedule and grounded in statements you can trust. It starts with a check on the foundation, builds a forecast and a budget, and then runs on a weekly or every-other-week strategy call. Here is what happens at each stage.",
 "sections": [
   ("What happens before the advisory starts?",
    ["A foundation check, and it is not a formality. Forecasting and modelling are built on the statements underneath them, so the first question is whether the close is structured, the accounts are reconciled monthly and the statements are reliable.",
     "If they are, the engagement starts with a forecast. If they are not, the close and the statements get built first, and the advisory begins once they can be relied on. That is why the CFO package includes everything in Growth and Starter: advisory is only as good as the numbers underneath it, and our " + _a("do-you-need-a-cfo-yet.html", "do you need a CFO yet") + " guide is direct about what to fix first."]),
   ("What gets built in the first weeks?",
    ["A cash flow forecast and a budget, both shaped around the decisions the business is actually facing rather than around a template. The forecast answers questions about timing: what the bank balance does if a large customer pays late, what a hire does to the next two quarters, when the seasonal dip arrives.",
     "The budget is the other half. It is only useful in the comparison, so it is built to be compared against actuals every month rather than filed. That comparison is controller-level reporting, which is why the two levels sit together."]),
   ("What happens on the strategy calls?",
    ["They run weekly or every other week, agreed at the start. Each one is a working session rather than a report reading: the forecast is updated with what actually happened, the decisions in front of the business get modelled, and the numbers get argued with.",
     "Profitability and margin analysis lives here too. Knowing revenue is common; knowing which customers, services or lines actually make money is the work, and it is usually where the surprises are."]),
   ("What arrives in writing?",
    ["Executive-level financial reporting: the statements from the close, the forecast as updated, budget against actual, the margin view and whatever the current decision needs. The point of the format is that somebody outside the business could follow it.",
     "What does not arrive is a promise. Nobody honest tells you what your margin, your valuation or your growth will do, and an adviser who does is selling. What advisory buys is better information and somebody whose job is to disagree with you when the numbers do."]),
   ("How does the engagement change over a year?",
    ["The early months are heavier because the forecast and the budget are being built and the reporting is being shaped. After that it settles into a rhythm, and the work shifts from construction to decisions: a financing conversation, a pricing change, a location, a hire.",
     "The scope is a fixed monthly figure agreed in writing after the free 30-minute call, and it moves only if the scope does. If the honest answer at any point is that " + _a(CTR, "controller services") + " would serve you better than " + _a(CFO, "CFO advisory") + ", we will say so. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("How often are the calls?", "Weekly or every other week, agreed at the start of the engagement, with the cadence set by what the business is deciding rather than by a package."),
   ("Does the CFO package include the bookkeeping and the close?", "Yes. It includes everything in the Growth and Starter packages, because advisory built on statements you cannot trust is worse than no advisory."),
   ("Who is on the calls?", "The founder, Chaudhry Ahmad, is the person on every strategy call. Who joins from your side is up to you and usually depends on the decision."),
   ("Can the engagement be shaped around one decision?", "Say so on the call. Some are built around a financing round or an acquisition, with the ongoing arrangement decided afterwards."),
 ],
},

{
 "slug": "cfo-advisory-mistakes",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "mistakes",
 "title": "CFO Advisory Mistakes That Cost Money",
 "desc": "The mistakes that make a fractional CFO engagement expensive: unreliable statements, a forecast nobody updates, hiring a title, expecting promises.",
 "keywords": "cfo advisory mistakes, fractional cfo problems, forecasting mistakes, when not to hire a cfo",
 "read": "6 min read",
 "lede": "A CFO engagement fails in predictable ways, and none of them is about the adviser being wrong. It is starting before the statements are reliable, building a forecast nobody updates, hiring a title instead of a scope, and expecting somebody to promise an outcome. All four are avoidable before the engagement starts.",
 "sections": [
   ("Why is starting on unreliable statements the worst one?",
    ["Because it produces confident answers to the wrong question. A forecast is a model of the business built on the numbers the business reports, and if those numbers are not reconciled and closed, the model is precise about something that is not true.",
     "The tell is easy to check. Do the accounts get reconciled every month, does the month close on a date, do you trust last month's statements. Two no answers and the first project is " + _a(CTR, "controller services") + ", not advisory. That is not a sales position, it is the order the work has to happen in."]),
   ("What happens to a forecast nobody updates?",
    ["It becomes a document instead of a tool. A forecast is only useful when it is compared with what actually happened and adjusted, because the value is in the difference rather than in the projection.",
     "The failure looks like diligence. The model is built, it is detailed, it sits in a folder, and six months later nobody trusts it enough to act on it. Updating it on a schedule, on the strategy call, is what makes it worth the effort of building."]),
   ("What is wrong with hiring a title?",
    ["A title is not a scope. Two engagements described with the same three letters can differ completely in what actually arrives, and the difference only shows up in month three.",
     "So buy the deliverables. Cash flow forecasting and planning, strategic budgeting and modelling, profitability and margin analysis, executive-level financial reporting and a standing strategy call is the " + _a(CFO, "CFO advisory") + " level here, and it is the list to hold any offer against. Our guide to " + _a("how-to-choose-a-fractional-cfo.html", "choosing a fractional CFO") + " has the questions."]),
   ("Why is expecting a promise a mistake?",
    ["Because the promise is the warning sign. Nobody honest tells you what your margin, your valuation, your growth or your funding round will do, and anyone who does is describing a sales process rather than a financial one.",
     "What good advisory buys is different and less exciting: better information, a decision modelled before it is made, a margin problem seen before it shows in the bank, and somebody in the room whose job is to disagree with you when the numbers do."]),
   ("What are the quieter mistakes?",
    ["Bringing the adviser in only when something is already going wrong, which turns advisory into firefighting. Keeping the engagement away from the people who run the business, so decisions get modelled without the context that would have changed them. And treating the monthly reporting as something the adviser reads rather than something you read together.",
     "The fix for all three is the same: a standing cadence rather than a call when there is a crisis. " + _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288, and if the honest answer is that you are not ready for this level, that is what you will hear."]),
 ],
 "faq": [
   ("How do I know if our statements are good enough to start?", "Ask whether the accounts are reconciled monthly, whether the month closes on a date, and whether you would send the statements to a lender. Three yeses and the foundation is there."),
   ("Is it a mistake to hire a CFO too early?", "It is an expensive one, because you pay advisory rates for work that is really controller work. The honest first call sometimes ends that way."),
   ("Should the forecast be detailed or simple?", "Simple enough to update every month. A model nobody maintains is worth less than a rough one that stays current."),
   ("What if the adviser and I disagree?", "That is part of what the engagement is for. The problem is not disagreement; it is agreement that was never tested against the numbers."),
 ],
},

{
 "slug": "how-long-cfo-advisory-takes",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "time",
 "title": "How Long Does CFO Advisory Take to Get Running?",
 "desc": "The realistic timeline for a fractional CFO engagement: the foundation check, the first forecast and budget, the call cadence, and when the reporting settles.",
 "keywords": "how long does cfo advisory take, fractional cfo onboarding, cfo engagement timeline, cash flow forecast setup",
 "read": "5 min read",
 "lede": "Getting CFO advisory running takes as long as the foundation underneath it needs. With a structured close and reliable statements already in place, the forecast and the budget come first and the cadence starts quickly. Without them, the close gets built first, and that is the honest answer rather than a delay.",
 "sections": [
   ("What happens in the first conversation?",
    ["A free 30-minute call, and a reply to any message within one business day. The call is where the foundation question gets asked: is the month closing on a date, are the accounts reconciled, are the statements trusted.",
     "If they are, the engagement can start on the forecast. If they are not, the first work is " + _a(CTR, "controller services") + " and the advisory follows. That order is not negotiable, and it is the shortest path rather than the longest one."]),
   ("How long does the foundation take if it is not there?",
    ["It depends on how far behind the books are and how much structure exists. Catch-up work is scoped separately with its own figure, and building a close means agreeing a date, a sequence and a set of reconciliations rather than doing more work faster.",
     "Nobody can put a number on that before looking, and a firm that offers one has not looked. Our article on " + _a("how-long-month-end-close-takes.html", "how long a month-end close takes") + " covers what a single month looks like once the structure exists."]),
   ("How long before there is a forecast?",
    ["The first cash flow forecast and budget are the opening work of the engagement, and they take the time it takes to understand the business rather than to fill in a template. The questions are about timing, seasonality, payment behaviour and the decisions in front of you.",
     "What matters more than the build is the update. A forecast is a tool that gets compared with what happened and adjusted on the strategy call, so the first version is a starting point rather than a deliverable to be signed off and filed."]),
   ("How long until the reporting settles?",
    ["A few cycles. The early months are heavier because the reporting is being shaped: which measures belong on the pack, what the margin view should show, what a decision-ready report looks like for this business.",
     "After that it settles into a rhythm, and the work moves from construction to decisions. That shift is the point at which the engagement starts feeling like advisory rather than setup."]),
   ("What sets the cadence from then on?",
    ["Weekly or every other week strategy calls, agreed at the start, with the frequency following what the business is deciding rather than a package rule. A financing conversation or an acquisition pulls the cadence tighter; a steady quarter does not need it.",
     "The scope and the fixed monthly figure are agreed in writing before anything begins, and they move only if the scope does. " + _a(CONTACT, "Book a free consultation") + " or call (847) 644-2288 and we will tell you what your own situation would need first."]),
 ],
 "faq": [
   ("Can advisory start before the close is fixed?", "It can be discussed, but the forecasting should not start on statements nobody trusts. Starting in the wrong order costs more than waiting does."),
   ("How quickly will I get a reply?", "Every message gets a reply within one business day. If it is urgent, calling (847) 644-2288 is faster."),
   ("Is there a minimum engagement length?", "Scope is agreed individually. The useful question is how long the work in front of the business is, and that is what the first call is for."),
   ("What slows an engagement down?", "Access and clarity. Waiting on the accounting file, or starting without agreeing what decisions the engagement is meant to support, holds things up more than the modelling does."),
 ],
},

{
 "slug": "cfo-advisory-alternatives",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "alternatives",
 "title": "CFO Advisory Alternatives, and When Each One Wins",
 "desc": "Controller services, a one-off project adviser, an advisory board, a full-time CFO, or your own forecast. What each covers and when each one wins.",
 "keywords": "cfo advisory alternatives, fractional cfo vs full time, alternatives to hiring a cfo, do i need a cfo",
 "read": "6 min read",
 "lede": "Fractional CFO advisory is one of five ways to get forward-looking financial judgement into a business, and for many owners it is not the first one to try. Controller structure, a one-off project adviser, an advisory board, a full-time hire, or a forecast you keep yourself each fit a different situation.",
 "sections": [
   ("When does controller structure win instead?",
    ["Whenever the real problem is that last month is unclear. If the close has no date, the accounts are not all reconciled, or you would not send the statements to a lender, the missing thing is structure rather than strategy.",
     "That is " + _a(CTR, "controller services") + ", and it is the most common right answer for a business that thinks it needs a CFO. Fixing it also makes any later advisory cheaper and better, because the forecast is built on numbers that hold. Our " + _a("bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller or CFO guide") + " is the map."]),
   ("When does a one-off project adviser win?",
    ["When there is a single decision and no ongoing need. A financing round, an acquisition, a major lease or a pricing overhaul can each justify bringing somebody in for the decision and stopping afterwards.",
     "The limit is that a project adviser leaves with the context. Nothing is built that keeps working, and the next decision starts from scratch. That is a fine trade when the decisions are years apart and a poor one when they are monthly."]),
   ("When does an advisory board win?",
    ["When what is missing is judgement about the market rather than judgement about the numbers. A board or a group of experienced advisers brings pattern recognition, introductions and challenge, and it costs very little compared with an engagement.",
     "What it will not do is build a forecast, own the reporting or model a decision in a spreadsheet before the meeting. Boards read what somebody prepared. Somebody still has to prepare it, and that is the gap this page is about."]),
   ("When does a full-time CFO win?",
    ["When the business is large enough that the role is full and somebody needs to be in the building, on the leadership team, every day. At that point fractional stops being an efficiency and starts being a constraint.",
     "The honest comparison includes everything on both sides: an executive salary with payroll costs, recruitment, equity in some cases and the risk of a bad hire, against a fixed monthly figure for a defined scope. Our guide to " + _a("fractional-cfo-cost.html", "what a fractional CFO costs") + " sets out how the two compare."]),
   ("When is your own forecast enough?",
    ["More often than owners think, at least for a while. A simple ninety-day cash forecast is something every owner should keep, and our " + _a("cash-flow-management.html", "cash flow management guide") + " shows how to build one. A budget you actually compare against is within reach with good statements.",
     "What is hard to do yourself is the judgement: modelling a decision properly, seeing a margin problem before it reaches the bank, and having somebody whose job is to disagree with you. That is what advisory is, and it is not a spreadsheet."]),
   ("How do you choose between them?",
    ["Ask what the question is. If it is about last month, buy structure. If it is one decision, buy a project. If it is about the market, find advisers. If it is about the next twelve months and it is a standing question, that is " + _a(CFO, "CFO advisory") + ".",
     "And if the answer is that you are not there yet, that is a real answer. " + _a(CONTACT, "Book a free 30-minute call") + " or phone (847) 644-2288, and you will hear it plainly, including a shorter list of what to fix first."]),
 ],
 "faq": [
   ("Is a fractional CFO only for large companies?", "No. It exists for businesses that need executive financial judgement without a full-time executive salary, which is most businesses in the low millions of revenue."),
   ("Can we combine some of these?", "Yes, and many do. An advisory board for market judgement and a fractional CFO for the numbers is a common and sensible pairing."),
   ("What if we already have a controller?", "Then the foundation is likely in place and the question is whether the forward-looking work is being done by anyone. That is exactly what the first call is for."),
   ("Does starting with the cheapest option waste money?", "Not if the records stay clean. Structure built at the controller level is the same structure advisory would need later, so nothing is redone."),
 ],
},

]
