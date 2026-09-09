#!/usr/bin/env python3
"""
Service cluster: the articles that sit under the three pillar pages.

WHY THIS CLUSTER
The engine run of 2026-09-08 (MARKETING/reports/seo/northpeakfp-2026-09-08.md)
read the site's 63 pages and found that three of the four services had no
pillar page and that 41 of 44 buyer questions had no page at all. Nobody on the
site answered "how much does accounting cost" for an owner in Wilmette. The
2026-09 cluster month adds the three pillars (build_pillars.py) and these
articles, each of which links its pillar and the contact page.

WHICH INTENTS
firm.content.trade_cluster.plan() ranks buyer intents in the order a cluster
earns its keep: cost, near, best, how, mistakes, questions, time, diy, vs,
alternatives, examples. The "near" intent is carried by the pillars themselves
(each opens with the town) and the "examples" intent needs client material that
does not exist yet, so neither appears here. From the rest, these are the ones
an owner in Wilmette actually types:

    accounting services   cost, diy, mistakes, questions
    controller services   cost, vs, how, time
    cfo advisory          cost, best, diy

Bookkeeping folds into the accounting cluster: on this site it is the first
line of the Starter package, not a separate service.

WHAT THE COPY MAY SAY
Facts come only from the site's own pages: the three packages and what each
contains, the free 30-minute first call, the reply within one business day,
the fixed figure in writing before work begins, the individually quoted scope,
the practice's base in Wilmette and its remote work nationwide. No dollar fees
are printed anywhere on the site, so none are printed here; prices are
described in kind. No statistics, no client counts, no outcomes promised.
Chaudhry Ahmad is not a CPA and nothing here says or implies otherwise.

Every article carries a 35 to 70 word lede that answers the title, h2s phrased
as the questions buyers type, and a visible FAQ that the shell also emits as
FAQPage markup. Each section body is a list of paragraphs.
"""

CONTACT = "../contact.html"
ACC = "../accounting-services.html"
CTR = "../controller-services.html"
CFO = "../cfo-advisory.html"


def _a(href, text):
    return f'<a href="{href}">{text}</a>'


ARTICLES = [

# ===================================================================
# ACCOUNTING SERVICES
# ===================================================================
{
 "slug": "accountant-cost-small-business",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "cost",
 "title": "How Much Does an Accountant Cost for a Small Business?",
 "desc": "What drives the fee for small business accounting, why most firms will not print a price list, and what a fixed quote should include in writing.",
 "keywords": "how much does an accountant cost, small business accountant fees, bookkeeping cost, accounting fees Wilmette",
 "read": "6 min read",
 "lede": "There is no single price for a small business accountant, because the fee follows the work: how many transactions move through the books each month, how many accounts and entities there are, whether payroll or sales tax is involved, and how much cleanup is waiting. At NorthPeak every engagement is quoted individually, as a fixed figure in writing, before any work begins.",
 "sections": [
   ("What actually drives the fee?",
    ["Volume comes first. A business that runs forty transactions a month is a different job from one that runs four hundred, even if the two owners describe their needs in the same words. Every transaction has to be categorised, matched to a bank line, and reviewed.",
     "After volume comes structure. Two bank accounts and a credit card are quick to reconcile. Add a second entity, a payroll run, sales tax in more than one state, or inventory, and the monthly work grows with each one.",
     "Then there is the state of the books when we arrive. Clean, current books cost less to maintain than a year of uncategorised downloads. That is why catch-up work is scoped on its own, so the one-time effort never hides inside the ongoing fee."]),
   ("Why do accountants not publish a price list?",
    ["Because the scope is the price. A menu with a number next to bookkeeping tells you nothing until someone has looked at your bank feeds, your payroll, and your filing history. A number printed before that is either padded to cover the unknown or too low to survive contact with your books.",
     "The alternative to a menu is not hourly billing. Hourly is the arrangement where the invoice is a surprise every month and the incentive runs the wrong way. We quote a fixed figure after the discovery call, in writing, and that figure does not move unless the scope does."]),
   ("Does the fee change as the business grows?",
    ["Yes, and it should. The " + _a(ACC, "Starter package") + " covers bookkeeping, reconciliations, monthly reports, and tax preparation for the business and its owner. That is the right fit for a solo operator or a small service business with clean, low-volume books.",
     "Growth adds controller-level oversight: a structured monthly close, financial statement preparation, budget against actual, KPI tracking, and a monthly review call. The CFO package adds forecasting, modelling, margin analysis, and a standing strategy call. You move up a level when the complexity does, not before."]),
   ("What should a written quote include?",
    ["A list of what is in scope, written plainly enough that you could check it against an invoice. A list of what is out of scope, which matters more. When your reports will arrive each month. Who you will actually talk to. And, if your books are behind, a separate line for the catch-up so you know the one-time cost apart from the recurring one.",
     "If a quote is missing any of these, ask. A firm that cannot say what is excluded has not finished thinking about your job."]),
   ("How do you know the fee is worth paying?",
    ["Count the hours you spend on the books yourself, then decide what those hours are worth in the business. Add the cost of the errors you are not catching and the tax decisions nobody is planning. When that total passes the fee, the answer is clear. Our guide on " + _a("when-to-hire-accountant.html", "when to hire an accountant") + " walks through the signs in more detail.",
     "The free 30-minute call exists for exactly this question. Tell us what the books look like and we will say plainly which level fits, including if the honest answer is that you do not need us yet. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Do you charge by the hour?", "No. Every engagement is quoted individually after the discovery call and confirmed as a fixed figure in writing before any work begins."),
   ("Is the first conversation free?", "Yes. It is a 30-minute call about your business and your books, with no obligation."),
   ("What if my books are a year behind?", "Catch-up and clean-up work is common. It is scoped separately from the ongoing service so the one-time cost is clear on its own."),
   ("Do I need to be near Wilmette?", "No. The practice is based in Wilmette, Illinois, and works with clients remotely nationwide through scheduled video reviews."),
 ],
},

{
 "slug": "diy-bookkeeping-or-hire",
 "cat": "Bookkeeping",
 "pillar": "accounting-services",
 "intent": "diy",
 "title": "Do Your Own Bookkeeping or Hire Someone?",
 "desc": "An honest line between the bookkeeping an owner can do well alone and the point where doing it yourself starts costing more than an accountant would.",
 "keywords": "do my own bookkeeping, diy bookkeeping vs accountant, when to outsource bookkeeping, small business bookkeeping help",
 "read": "6 min read",
 "lede": "Plenty of owners should do their own bookkeeping, at least at first. A dedicated business account, software connected to the bank, and a monthly reconciliation will carry a small, simple business a long way. The line moves the moment the books stop being simple, or the moment your hours on them cost more than the help would.",
 "sections": [
   ("What can you do well on your own?",
    ["Quite a lot, if the business is small and the habits are good. Open a business bank account and card on day one and never mix personal spending into them. Connect accounting software to the bank so most transactions categorise themselves. Photograph receipts when you buy. Reconcile against the bank statement once a month.",
     "That routine is the whole of our " + _a("bookkeeping-basics.html", "bookkeeping basics guide") + ", and an owner who follows it will hand a preparer clean records in April. The work is not hard. It is just relentless, and it has to happen every month whether you feel like it or not."]),
   ("When does doing it yourself start to cost money?",
    ["The first sign is time. If the books are taking hours that would otherwise go to selling, delivering, or hiring, the maths has already tipped. Your hour in the business is worth more than an accountant's hour on the books.",
     "The second sign is complexity. A first employee brings payroll deposits and filings on a schedule with real penalties. Sales in more than one state bring sales tax. A second entity, inventory, or an S-Corp election each add rules that are easy to get wrong and expensive to unwind. The third sign is the decision you are about to make, such as a loan, an equipment purchase, or a change of structure, where a short professional read before you act costs less than fixing it after."]),
   ("What does a bookkeeper do that software does not?",
    ["Software categorises. A person checks. The bank feed will happily file an owner draw as an expense and a loan deposit as revenue, and it will do so consistently for months. Someone has to look at what the software decided, clear the suspense account, record accruals and depreciation, and confirm payroll posted correctly.",
     "That review is what turns a list of transactions into statements you can rely on. It is also the part owners skip when the month gets busy, which is exactly when errors compound."]),
   ("Is there a middle option?",
    ["Yes, and it is the one most small businesses end up with. You keep the daily habits: the separate account, the receipts, the software. The accountant takes the monthly close, the reconciliations, and the reporting, and prepares the return at year end. Our " + _a(ACC, "accounting services") + " start at exactly that level.",
     "The split works because each side does the part it is good at. You know what every transaction was for. We know what the books need to look like for the return and for a lender."]),
   ("How do you decide?",
    ["Write down the hours you spent on the books last month and what you would have done with them instead. List anything that changed this year: staff, states, entities, revenue. If either list makes you wince, it is time for a conversation. We will tell you plainly whether you need help yet, and the first 30 minutes are free. " + _a(CONTACT, "Book a consultation") + " or call (847) 644-2288."]),
 ],
 "faq": [
   ("Do I have to stop doing my own books to work with you?", "No. Many owners keep the daily habits and hand over the monthly close, the reconciliations, and the reporting."),
   ("Do I need to switch accounting software?", "Usually not. We work with the major platforms and will say plainly if your current setup is holding you back before recommending any change."),
   ("What if I have never reconciled?", "Then the first job is a scoped clean-up, priced on its own, and the ongoing service starts once the books are current."),
 ],
},

{
 "slug": "bookkeeping-mistakes-that-cost-money",
 "cat": "Bookkeeping",
 "pillar": "accounting-services",
 "intent": "mistakes",
 "title": "Bookkeeping Mistakes That Cost Small Businesses Money",
 "desc": "The bookkeeping habits that quietly cost owners money: mixed accounts, unreconciled months, miscategorised spending, and a close that never happens.",
 "keywords": "bookkeeping mistakes, common bookkeeping errors small business, miscategorized expenses, unreconciled accounts",
 "read": "6 min read",
 "lede": "The bookkeeping mistakes that cost money are rarely dramatic. They are small habits repeated for months: personal spending on the business card, a bank account nobody reconciles, expenses filed under the wrong heading, receipts that were never kept. Each one is cheap to fix in the month it happens and expensive to reconstruct in April.",
 "sections": [
   ("Why does mixing personal and business money cost so much?",
    ["Because every mixed transaction has to be untangled later by someone who was not there when it happened. A grocery run on the business card, a client lunch on the personal one, a transfer between the two with no note. Each takes minutes to sort in the month and far longer a year on, when nobody remembers.",
     "The fix is the first line of our " + _a("bookkeeping-basics.html", "bookkeeping basics") + ": a dedicated business account and card from day one, with nothing personal running through them. It is the single habit that makes every other part of the books easier."]),
   ("What happens when accounts are not reconciled?",
    ["Errors stay invisible. A duplicated deposit inflates revenue. A bank fee never recorded understates expenses. A payment that bounced is still showing as received. None of this surfaces until someone matches the books to the statement line by line, and if that never happens, the statements you are reading describe a business that does not quite exist.",
     "Monthly reconciliation is the check that catches these while they are still small. It is also the first thing a lender or a preparer will ask whether you have done."]),
   ("How do wrong categories cost you at tax time?",
    ["Deductions live or die by organisation. When spending is filed inconsistently, some of it lands in categories the return cannot use, some is missed entirely, and some is claimed in a way that would not survive a question. Meals and travel are the usual example: the amount is right but the record of who, what, and why is missing.",
     "Consistent categories, applied the same way every month, mean the return is a transfer rather than a reconstruction. Our guide to " + _a("business-expense-categories.html", "business expense categories") + " sets out the ones that cover most small businesses."]),
   ("What does skipping the month-end close cost?",
    ["Visibility. Without a close, there is no reliable profit and loss for last month, no balance sheet you would show anyone, and no way to compare what happened against what you planned. Decisions get made on the bank balance instead, which is not the same thing as profit.",
     "A close does not have to be elaborate. Reconcile every account, clear uncategorised transactions, record accruals and depreciation, confirm payroll, review receivables and payables, and produce the three statements. Done monthly, it turns tax season from an event into a formality."]),
   ("When is it time to hand the books over?",
    ["When any of the above has been true for more than a couple of months, or when the business has grown past the point where an evening a week keeps up. Our " + _a(ACC, "accounting services") + " start with a scoped clean-up if the books need one, and then a monthly routine that keeps them clean. The first call is free, 30 minutes, with no obligation. " + _a(CONTACT, "Book it here") + " or call (847) 644-2288."]),
 ],
 "faq": [
   ("Can you fix books that have been wrong for a year?", "Yes. Catch-up and clean-up work is common. It is scoped separately from ongoing service so the one-time effort has its own clear cost."),
   ("Which mistake matters most?", "Mixing personal and business money. It makes every other error harder to find and every month more expensive to close."),
   ("How often should the books be reconciled?", "Monthly, against every bank and credit card statement. That is the interval at which errors are still cheap to correct."),
 ],
},

{
 "slug": "questions-to-ask-an-accountant",
 "cat": "Working With an Accountant",
 "pillar": "accounting-services",
 "intent": "questions",
 "title": "Questions to Ask an Accountant Before You Hire One",
 "desc": "Seven questions to put to any accounting firm before you sign, with the answer that should come back and the answer that means keep looking.",
 "keywords": "questions to ask an accountant, how to interview an accountant, choosing an accounting firm, hiring a bookkeeper questions",
 "read": "6 min read",
 "lede": "The right questions for an accountant are the ones about how the work will actually run: who does the books, how the fee is set, when reports arrive, what happens when something is behind, and what is left out of scope. Ask them on the first call. The answers tell you more than any credentials page will.",
 "sections": [
   ("Who will actually do my books?",
    ["Ask whether the person you are talking to is the person who will see your transactions each month, or whether the work is passed down and reviewed later. Neither answer is wrong on its own. What you want is a clear one, and a named person you can reach when a question comes up.",
     "At NorthPeak the founder is the one you deal with directly. That is easy to state because the practice is built that way."]),
   ("How is the fee set, and will it change?",
    ["The answer you want is a fixed figure, in writing, after someone has looked at your books. The answer to be wary of is an hourly rate with no estimate, or a package price quoted before anyone has asked how many transactions you run. Ask what would cause the fee to change and how much notice you would get. Our guide on " + _a("accountant-cost-small-business.html", "what an accountant costs") + " explains what drives the number."]),
   ("When will I get my reports, and what will they say?",
    ["A monthly close should land on a predictable schedule, and the reports should be the three statements plus whatever you agreed to track. Ask to see a sample. If the firm cannot describe what you will receive and when, you will spend the year chasing it."]),
   ("What if my books are behind?",
    ["Every owner asks this apologetically, and there is no need. Catch-up work is common. The question is whether the firm will scope it separately, so you know the one-time cost apart from the ongoing fee, or fold it into the first few months where it is hard to see."]),
   ("What is not included?",
    ["This is the question most people forget, and the one that decides whether the first invoice surprises you. Payroll, sales tax filings, 1099s, tax planning during the year, and calls outside the scheduled review may each be in or out. A firm that has thought about your job can list its exclusions without hesitating."]),
   ("Will you tell me if I do not need you yet?",
    ["A good firm will. Some businesses are too small or too simple for a monthly engagement, and the honest answer is a checklist and a call back in a year. Our free 30-minute consultation ends that way sometimes. " + _a(CONTACT, "Book one") + " or call (847) 644-2288, and bring these questions with you."]),
   ("Which questions matter most for tax?",
    ["Ask whether planning happens during the year or only at filing. A preparer records what already happened. A planner changes the number before it is set. The difference is the subject of our guide to " + _a("tax-planning-vs-tax-prep.html", "tax planning versus tax preparation") + ", and it is the biggest gap between accounting firms that look alike on paper. Our " + _a(ACC, "accounting services") + " include tax preparation for the business and its owner at every level."]),
 ],
 "faq": [
   ("Should I ask about credentials?", "Ask what the firm has done for businesses like yours and who will handle your work. Chaudhry Ahmad brings controller-level experience, and the practice describes its work plainly rather than leaning on titles."),
   ("How long should the first conversation take?", "Ours is 30 minutes and free. That is enough to describe the business, the state of the books, and where the gaps are."),
   ("Is it rude to ask what is excluded?", "No. It is the most useful question on the list, and a firm that has scoped your work properly will welcome it."),
 ],
},

# ===================================================================
# CONTROLLER SERVICES
# ===================================================================
{
 "slug": "controller-cost-fractional-vs-full-time",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "cost",
 "title": "How Much Does a Controller Cost? Fractional vs. Full Time",
 "desc": "What a controller costs a growing business, why a fractional arrangement is usually the first step, and what the fee should buy you every month.",
 "keywords": "how much does a controller cost, fractional controller cost, outsourced controller fees, controller services pricing",
 "read": "6 min read",
 "lede": "A controller costs whatever it takes to get a structured monthly close, reliable statements, and budget-against-actual reporting every month. For most businesses in the range where the question first comes up, that is a fractional engagement quoted as a fixed monthly figure, not a full-time salary. The fee is set by the scope, and the scope is set by your books.",
 "sections": [
   ("What does a controller actually do for the money?",
    ["A bookkeeper records what happened. A controller makes sure it is right, on time, and understood. That means owning the month-end close, reviewing every reconciliation, preparing financial statements you would show a lender, comparing actuals to the budget, and tracking the handful of numbers that describe the business.",
     "It also means process. Who approves what, how bills move from receipt to payment, and where the controls sit that stop errors and leakage. Our " + _a(CTR, "controller services") + " page sets out what is included month to month."]),
   ("Why is fractional usually the first step?",
    ["Because the work in a growing business is real but not yet full-time. A business between roughly half a million and five million in revenue needs a proper close and someone accountable for it, but not forty hours a week of it. A fractional controller gives you the oversight without the salary, the benefits, and the recruiting.",
     "Full-time makes sense later, when the volume and the number of people in finance justify a seat in the office every day. Many businesses run fractional for years and never reach that point."]),
   ("What sets the fee?",
    ["Transaction volume and the number of accounts, as with bookkeeping. Then the things that are specific to a controller engagement: how many entities need consolidating, whether there is inventory or job costing, how many reports and KPIs you want, and how often you want to meet. A monthly review call is part of the Growth package. Weekly calls belong to the CFO level.",
     "The state of the books when we start matters too. A controller cannot close a month on top of a year of unreconciled accounts, so any catch-up is scoped and priced on its own first."]),
   ("How is the fee presented?",
    ["As a fixed figure in writing, after a free 30-minute call and a look at your current setup. We do not publish a rate card because the scope is the price, and we do not bill hourly because that puts the surprise on your invoice instead of in our planning. " + _a("bookkeeper-vs-controller-vs-cfo.html", "Bookkeeper, controller, or CFO") + " explains where the levels divide if you are not sure which one you are pricing."]),
   ("Is it worth it?",
    ["Ask what a late or wrong set of statements has cost you already: a decision made on the bank balance, a lender conversation that stalled, a tax surprise that a mid-year look would have caught. Then ask what your own hours on the close are worth. If those add up to more than a fractional fee, the answer is yes. If they do not, we will say so on the call. " + _a(CONTACT, "Book a consultation") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Do you publish a controller rate?", "No. Every engagement is quoted individually after the discovery call and confirmed as a fixed figure in writing before work starts."),
   ("What size of business needs a controller?", "The Growth package, which carries controller-level oversight, is built for businesses scaling operations in the range of about half a million to five million in revenue."),
   ("Can a controller engagement include bookkeeping?", "Yes. Growth includes everything in Starter: bookkeeping, reconciliations, monthly reports, and tax preparation, with the controller work on top."),
 ],
},

{
 "slug": "bookkeeper-vs-controller-vs-cfo",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "vs",
 "title": "Bookkeeper vs. Controller vs. CFO: Who Does What",
 "desc": "The three levels of financial help explained by what each one actually does, so you can match the level to the size and complexity of your business.",
 "keywords": "bookkeeper vs controller, controller vs CFO, difference between bookkeeper and controller, fractional CFO vs controller",
 "read": "6 min read",
 "lede": "A bookkeeper records transactions and keeps the accounts reconciled. A controller owns the monthly close, makes sure the statements are right, and compares results to the plan. A CFO uses those statements to look forward: forecasting cash, modelling decisions, and advising on strategy. Most growing businesses need each in turn, and the levels stack rather than replace one another.",
 "sections": [
   ("What does a bookkeeper do?",
    ["The daily and weekly work. Categorising transactions, reconciling bank and credit card accounts, recording bills and invoices, and producing a basic profit and loss each month. Good bookkeeping is the foundation everything else stands on, which is why it is the first line of our Starter package and stays in every level above it.",
     "What a bookkeeper does not do is judge. If the categories are consistent and the accounts reconcile, the job is done, even if the numbers are telling you something you need to hear."]),
   ("What does a controller add?",
    ["Accountability for the numbers being right. A controller runs a structured close on a schedule, reviews the reconciliations rather than just performing them, prepares financial statements to a standard a lender would accept, and reports budget against actual with the variances explained. They also design the internal controls: who approves spending, how payroll is checked, where the safeguards sit.",
     "This is the level at which an owner stops managing from the bank balance and starts managing from statements. It arrives with the Growth package, and our " + _a(CTR, "controller services") + " page describes it in full."]),
   ("What does a CFO do that a controller does not?",
    ["A controller looks at last month. A CFO looks at the next twelve. Cash flow forecasting, budgeting and modelling, margin analysis by product or customer, and the financial side of decisions that are expensive to reverse: a hire, a lease, a loan, a second location. A CFO also sits in the strategy conversation on a standing basis, weekly or every other week.",
     "A fractional CFO gives a business in the low millions of revenue that kind of leadership without a full-time executive salary. Our " + _a(CFO, "CFO advisory") + " page explains what the engagement looks like."]),
   ("Which one do you need?",
    ["If the books are not reconciled monthly, you need a bookkeeper first and nothing else will work until that is fixed. If the books are clean but the statements arrive late, are not trusted, or are never compared to a plan, you need a controller. If the statements are good and the questions you are asking are about the future, you need CFO advisory.",
     "Businesses rarely skip a level. A CFO forecasting from unreliable statements is guessing with better vocabulary."]),
   ("Can one firm cover all three?",
    ["Yes, and it is simpler when one does, because the levels are built on each other. NorthPeak's three packages are those three levels: Starter is bookkeeping and reporting with tax preparation, Growth adds the controller, and CFO adds the advisory. You move up when the complexity does. A free 30-minute call is the quickest way to find out where you sit. " + _a(CONTACT, "Book one here") + " or call (847) 644-2288."]),
 ],
 "faq": [
   ("Is a controller the same as an accountant?", "Not quite. Accountant is the broad term. A controller is the accountant who owns the close, the statements, and the controls inside a business."),
   ("Do I need a controller before a CFO?", "Almost always. CFO advice is only as good as the statements it is built on, and a controller is what makes those statements reliable."),
   ("Can I start with bookkeeping and move up later?", "Yes. That is how the packages are designed. Each level includes everything below it."),
 ],
},

{
 "slug": "how-controller-services-work",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "how",
 "title": "How Controller Services Work, Month by Month",
 "desc": "What an outsourced controller engagement looks like in practice: the setup, the monthly close, the reports, the review call, and how the rhythm settles in.",
 "keywords": "how controller services work, outsourced controller process, monthly close process, controller engagement",
 "read": "6 min read",
 "lede": "Controller services run on a monthly rhythm. The month closes on a set schedule, every account is reconciled and reviewed, the three financial statements and a budget-against-actual report are prepared, and you sit down with us on a review call to go through what changed and why. Before that rhythm starts, there is a setup phase that gets the books to a standard the close can stand on.",
 "sections": [
   ("What happens before the first close?",
    ["Discovery. We look at the current books, the chart of accounts, the software, the payroll setup, and how bills and invoices move through the business. Then we agree the scope in writing: what is in, what is out, what the fee is, and when reports will arrive.",
     "If the books are behind or unreliable, a clean-up comes next, scoped on its own. A controller close cannot be built on unreconciled accounts, so this step is never skipped, only sized."]),
   ("How does the monthly close run?",
    ["On the same working days every month. Bank and credit card accounts are reconciled. Uncategorised transactions are cleared. Accruals, prepaids, and depreciation are recorded. Payroll is checked against what actually posted. Receivables are aged and overdue invoices flagged. Payables and upcoming obligations are reviewed.",
     "Then the statements are produced: profit and loss, balance sheet, and cash flow. A PDF snapshot of all three is saved so there is a record of what the month looked like when it closed. Our free " + _a("../resources.html", "month-end close checklist") + " is this list, and you are welcome to run it yourself."]),
   ("What do the reports show?",
    ["The three statements, and then the comparison that gives them meaning: what happened against what you budgeted, with the variances explained rather than just listed. On top of that sit the few KPIs that actually describe your business. Which ones depends on the business, and choosing them is part of the setup.",
     "If you are new to reading statements, our guide to " + _a("financial-statements-explained.html", "the three financial statements") + " is the place to start."]),
   ("What is the review call for?",
    ["Understanding, not presentation. Once a month we walk through the reports together, answer the questions the numbers raise, and note anything that needs a decision. A margin that slipped, a customer paying slower, a cost line that grew faster than revenue. The call is where the statements turn into management.",
     "Between calls, the controller is reachable. The point of a named person is that questions get answered when they come up."]),
   ("How does the rhythm change over time?",
    ["It settles. The first few closes are slower while the chart of accounts is tidied and the reports are tuned. After that, the close lands on schedule, the reports arrive the same way every month, and the review call gets shorter because there are fewer surprises. That is the goal. When the questions start to be about the year ahead rather than the month behind, it is time to talk about " + _a(CFO, "CFO advisory") + ".",
     "This is what our " + _a(CTR, "controller services") + " are built around. The first conversation is a free 30-minute call. " + _a(CONTACT, "Book it") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Do I have to change accounting software?", "Usually not. We work with the major platforms and will say plainly if your current setup is holding you back before recommending any change."),
   ("How soon after month end do reports arrive?", "On a schedule agreed in writing at the start of the engagement. The point of a controller close is that the date is predictable."),
   ("Is the review call in person or remote?", "Either. The practice is based in Wilmette, Illinois. Local clients can meet in person; everyone else meets by scheduled video call."),
 ],
},

{
 "slug": "how-long-month-end-close-takes",
 "cat": "Controller Services",
 "pillar": "controller-services",
 "intent": "time",
 "title": "How Long Does a Month-End Close Take?",
 "desc": "How long a monthly close takes for a small business, what stretches it, what a controller does to shorten it, and how long it takes to get behind books current.",
 "keywords": "how long does month end close take, monthly close timeline, catch up bookkeeping how long, close process small business",
 "read": "5 min read",
 "lede": "A month-end close for a small business with clean books takes a few working days from the last bank statement to finished statements. What stretches it is not the volume of transactions but what is missing: unreconciled accounts, receipts nobody kept, payroll that did not post, and questions only the owner can answer. Getting behind books current is a separate job with its own timeline.",
 "sections": [
   ("What decides how long a close takes?",
    ["Three things. How current the books were when the month ended, how many accounts and entities have to be reconciled, and how quickly open questions get answered. A business with two bank accounts, software connected to both, and an owner who replies the same day can close fast. Add inventory, several entities, or a week of silence on a question, and the same close takes twice as long.",
     "The close also depends on outside dates. Bank and card statements arrive when they arrive, and payroll reports follow the payroll run. A close cannot finish before its inputs do."]),
   ("What makes a close drag on?",
    ["Uncategorised transactions that pile up until month end. A suspense account that has become a parking lot. Missing receipts for expenses that need a record. Owner draws and transfers with no note. Each of these is a question, and each question is a delay.",
     "The fix is upstream. When transactions are categorised during the month and receipts are captured at purchase, the close becomes a review rather than an investigation. That is the difference a controller's process makes, and it is described on our " + _a(CTR, "controller services") + " page."]),
   ("How long does catching up take?",
    ["It depends on how far behind the books are and what state the records are in. A few unreconciled months with statements on hand is a short job. A year of mixed personal and business spending with no receipts is a long one. What we do is scope it first, as a one-time project with its own price, so you know both the timeline and the cost before it starts.",
     "The ongoing monthly service begins once the books are current. Trying to run both at once is how catch-up work quietly never finishes."]),
   ("Can the close be made faster?",
    ["Yes, mostly by making it boring. A fixed schedule, the same checklist every month, receipts captured on the day, and a standing time for the owner's questions. Once that is in place, the close lands on the same working day each month and the review call happens on the same day too. Our " + _a("how-controller-services-work.html", "month-by-month guide") + " walks through what that rhythm looks like once it settles."]),
   ("What if you are not sure how far behind you are?",
    ["That is a normal place to start. Bring the last bank statement and whatever the software shows, and in a free 30-minute call we will tell you how big the gap is and what closing it would take. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Is a faster close always better?", "A predictable close is what matters. The aim is statements you can rely on, delivered on the same schedule every month."),
   ("Do you close every month or just at year end?", "Every month. A year-end-only close means eleven months of decisions made without reliable numbers."),
   ("How long does the review call take?", "Long enough to go through the statements and the variances. It gets shorter as the surprises get fewer."),
 ],
},

# ===================================================================
# CFO ADVISORY
# ===================================================================
{
 "slug": "fractional-cfo-cost",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "cost",
 "title": "How Much Does a Fractional CFO Cost?",
 "desc": "What a fractional CFO costs a growing business, what sets the monthly fee, how it compares with a full-time hire, and what the engagement should include.",
 "keywords": "how much does a fractional CFO cost, fractional CFO fees, outsourced CFO cost, CFO advisory pricing",
 "read": "6 min read",
 "lede": "A fractional CFO is priced as a fixed monthly fee for a defined scope: cash flow forecasting, budgeting and modelling, margin analysis, executive reporting, and a standing strategy call. The fee is set by the size and complexity of the business and how often you meet, and it is a fraction of a full-time executive salary because the role is part-time by design.",
 "sections": [
   ("What are you paying for?",
    ["Forward-looking financial leadership. A rolling cash flow forecast so the next quarter is planned rather than survived. A budget and the models behind decisions that are expensive to reverse. Margin analysis by product, service, or customer. Reporting written for an owner or a board rather than a bookkeeper. And a strategy call every week or every other week, where those numbers meet the decisions.",
     "The CFO package also includes everything in Growth and Starter: the controller close, the statements, the bookkeeping, and tax preparation. Advisory on top of unreliable books is not advisory, so the levels stack. Our " + _a(CFO, "CFO advisory") + " page sets out the full scope."]),
   ("What sets the fee?",
    ["The size of the business, first. Forecasting for a company with one revenue line and ten staff is a different job from one with three divisions and a hundred. Then the number of entities, the complexity of the model you need, the frequency of the strategy calls, and whether there is a specific project in front of you, such as a financing round, an acquisition, or a new location.",
     "The state of the underlying books matters too. If the controller work is not yet in place, that is built first, and the fee reflects the whole."]),
   ("How does it compare with a full-time CFO?",
    ["A full-time CFO is a senior executive salary plus benefits, plus the months it takes to recruit one. For a business in the low millions of revenue that is rarely justified, because the work that needs a CFO's judgment does not fill a week. A fractional engagement buys the judgment for the hours it is needed.",
     "Full-time becomes the right answer when the finance function itself needs managing every day: a team, a treasury, investors on the phone. Until then, fractional is usually the honest fit."]),
   ("How is the fee agreed?",
    ["After a free 30-minute call and a look at the business, we quote a fixed figure in writing. There is no rate card and no hourly billing. The number covers the scope we have agreed, and it changes only if the scope does. " + _a("do-you-need-a-cfo-yet.html", "Do you need a CFO yet") + " is worth reading first if you are not sure the level fits."]),
   ("Is it worth it?",
    ["Put a value on the decision you are about to make without a forecast. A hire made a quarter early, a lease signed on a hunch, a loan sized by guesswork. If a fractional CFO would change that decision, the fee is small next to it. If your questions are still about last month rather than next year, you need a controller first, and we will say so. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288."]),
 ],
 "faq": [
   ("Do you charge hourly for CFO work?", "No. The engagement is quoted individually and confirmed as a fixed monthly figure in writing before it starts."),
   ("What size of business is the CFO package for?", "Established businesses that need strategic financial leadership, in the range of about two million to one hundred million in revenue."),
   ("Can I get CFO advice without the bookkeeping?", "The CFO package includes the controller and bookkeeping levels, because advice built on unreliable statements is not worth paying for."),
 ],
},

{
 "slug": "how-to-choose-a-fractional-cfo",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "best",
 "title": "How to Choose a Fractional CFO for a Growing Business",
 "desc": "What to look for in a fractional CFO: the questions to ask, the answers that matter, and the signs that a firm is selling reports rather than judgment.",
 "keywords": "how to choose a fractional CFO, best fractional CFO, hiring an outsourced CFO, fractional CFO questions",
 "read": "6 min read",
 "lede": "Choose a fractional CFO by how they will work with you, not by the title. Ask who you will actually meet with, how often, what the forecast will look like, how the fee is set, and whether the controller work underneath is included or assumed. The right answer to each is specific and written down. A vague one means the engagement will be vague too.",
 "sections": [
   ("What should a fractional CFO actually deliver?",
    ["A rolling cash flow forecast, a budget with the model behind it, margin analysis, executive-level reporting, and a standing strategy call. Ask to see what each of those looks like for a business like yours. If the answer is a dashboard with no conversation attached, you are being sold reports, and reports you already have from your controller.",
     "Our " + _a(CFO, "CFO advisory") + " page lists what the engagement includes at NorthPeak, so you can compare line by line."]),
   ("Who will you be talking to?",
    ["The person on the sales call and the person on the monthly strategy call are not always the same. Ask. A fractional CFO is a relationship with one person who knows your numbers and your plans, and it does not work as a rotating team. At NorthPeak the founder is the one you meet, every time."]),
   ("Is the controller work included?",
    ["Advisory on top of unreliable statements is guesswork with better vocabulary. Ask whether the engagement includes the monthly close, the reconciliations, and the statement preparation, or whether it assumes somebody else is doing them well. If it assumes, ask who checks. Our CFO package includes everything in the Growth and Starter levels for exactly this reason."]),
   ("How is the fee set?",
    ["You want a fixed monthly figure, in writing, for a scope you can read. Be wary of hourly rates with no ceiling and of packages quoted before anyone has looked at the business. Our guide to " + _a("fractional-cfo-cost.html", "what a fractional CFO costs") + " explains what should drive the number."]),
   ("What does a good first conversation sound like?",
    ["Questions about your business rather than a pitch about theirs. What are you deciding this year? Where does cash get tight? What do you not trust in your current reports? A CFO who asks those on the first call is already doing the job. One who opens with a slide deck is not.",
     "It should also be honest about fit. Some businesses that ask about a CFO need a controller first, and a good firm says so. Our free 30-minute consultation ends that way when it should. " + _a(CONTACT, "Book one") + " or call (847) 644-2288."]),
   ("What are the warning signs?",
    ["Promised outcomes. Nobody honest promises what your margin or your valuation will do. A refusal to put the scope in writing. No named person. A forecast that is a spreadsheet you are expected to maintain yourself. And any reluctance to explain what is excluded, which is where the surprises live."]),
 ],
 "faq": [
   ("Does a fractional CFO need to be local?", "No. The work is forecasting, modelling, and a standing call, all of which run remotely. NorthPeak is based in Wilmette, Illinois, and meets local clients in person when that is useful."),
   ("How often should we meet?", "Weekly or every other week for a CFO engagement. Monthly is a controller rhythm, and it is not enough for decisions that move quickly."),
   ("Should I choose on price?", "Choose on scope and on who you will work with. Then make sure the price for that scope is fixed and in writing."),
 ],
},

{
 "slug": "do-you-need-a-cfo-yet",
 "cat": "CFO Advisory",
 "pillar": "cfo-advisory",
 "intent": "diy",
 "title": "Do You Need a CFO Yet? Signs a Business Is Ready",
 "desc": "The signs that a growing business has outgrown bookkeeping and controller work and needs CFO-level advice, and the signs that it is not there yet.",
 "keywords": "do I need a CFO, when to hire a fractional CFO, signs you need a CFO, CFO for small business",
 "read": "6 min read",
 "lede": "You need a CFO when the questions you are asking are about the future and nobody in the business can answer them with numbers: whether you can afford the hire, how long the cash lasts if a big customer pays late, what a second location does to margin. You do not need one yet if the questions are still about whether last month's statements are right.",
 "sections": [
   ("What are the signs you are ready?",
    ["Decisions are waiting on numbers you do not have. You are considering a loan, a lease, a significant hire, or a new line of business, and the answer to whether it works is a feeling rather than a forecast. Cash gets tight at points in the year and you find out when it happens rather than a quarter before. You know revenue but not which customers or services actually make money.",
     "Another sign is the audience. A lender, an investor, or a partner is asking for projections and a plan, and what you have is last year's return."]),
   ("What are the signs you are not there yet?",
    ["The books are not reconciled monthly. Statements arrive late or you do not trust them. There is no budget to compare against. If any of these is true, a CFO would be forecasting from numbers that are not reliable, and the honest advice is to fix the foundation first. That is controller work, and our " + _a(CTR, "controller services") + " page describes it.",
     "Size matters less than people assume, but it matters. The CFO package is built for established businesses in the range of about two million to one hundred million in revenue. Below that, the Growth package usually answers the questions being asked."]),
   ("Can you do the CFO work yourself?",
    ["Some of it, for a while. A simple cash forecast for the next ninety days is something every owner should keep, and our " + _a("cash-flow-management.html", "cash flow management guide") + " shows how. A budget you actually compare against is within reach with good statements.",
     "What is hard to do yourself is the judgment. Modelling a decision properly, seeing the margin problem before it shows in the bank, and having someone in the room whose job is to disagree with you when the numbers do. That is what you are buying with advisory, and it is not a spreadsheet."]),
   ("What does the first engagement look like?",
    ["It starts with the foundation check. If the controller work is in place, the CFO engagement begins with a forecast and a budget and settles into a weekly or every-other-week strategy call. If it is not, the close and the statements get built first, and the advisory starts once they are reliable. Everything is scoped in writing with a fixed monthly figure. Our " + _a(CFO, "CFO advisory") + " page sets out what is included."]),
   ("How do you find out where you stand?",
    ["Ask. A free 30-minute call is enough to tell whether you need advisory, a controller, or nothing yet, and we will say which. " + _a(CONTACT, "Book the call") + " or phone (847) 644-2288. If the answer is not yet, you will leave with a shorter list of what to fix first."]),
 ],
 "faq": [
   ("Is a fractional CFO only for large companies?", "No. It exists for businesses that need executive financial judgment without a full-time executive salary, which is most businesses in the low millions of revenue."),
   ("What if I need a CFO for one decision?", "Say so on the call. Some engagements are shaped around a financing round or an acquisition, with the ongoing advisory decided afterwards."),
   ("Will you tell me if I do not need one?", "Yes. The first call ends that way sometimes, with a note of what to put in place first."),
 ],
},

]

# Pillar slug -> the label used in the cluster bar and the Article "about" markup.
PILLAR_LABELS = {
    "accounting-services": "Accounting Services",
    "controller-services": "Controller Services",
    "cfo-advisory": "CFO Advisory",
}
