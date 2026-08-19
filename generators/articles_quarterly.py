#!/usr/bin/env python3
"""
Quarterly estimated tax cluster.

WHY THIS CLUSTER
Same profile the retirement cluster had. The Search Console export for the three
months to 2026-08-16 shows eight distinct quarterly-tax queries picking up
impressions, all landing on ONE page -- /articles/quarterly-estimated-taxes,
which sits at position 74.2 with 132 impressions and zero clicks. That page has
the most impressions on the entire site and converts none of them, because one
page cannot answer eight different questions.

Topics, each taken from a query that actually appeared in that report:

    self employed quarterly taxes ..................... 19 impressions
    self employed quarterly tax updates ............... 11
    self employed estimated tax ....................... 10
    quarterly self employment tax ..................... 4
    self-employed quarterly taxes ..................... 3
    self employed quarterly tax ....................... 3
    self employed estimated tax payments .............. 2
    1099 quarterly taxes .............................. 2

NO DATES, NO DOLLAR FIGURES BEYOND WHAT IS IN STATUTE
Due dates shift when they fall on a weekend or holiday, and most thresholds are
indexed. The one figure used here -- the $1,000 threshold for individuals -- is
stated on the IRS estimated taxes page and is quoted as such, with a link. The
safe harbour percentages (90% of the current year, 100% of the prior year) are
likewise quoted from that page.

WHAT IS DELIBERATELY NOT ASSERTED
The IRS page references "special rules for farmers, fishermen, and certain
higher income taxpayers" without stating the higher percentage. These articles
therefore say a higher percentage applies above an income threshold and link to
Publication 505 for it, rather than printing a number this build did not verify.

LICENCE BOUNDARY
Chaudhry Ahmad is not a CPA. These explain how the estimated tax system works
and how the penalty is avoided. None of them compute anyone's liability or tell
a reader what to pay.

SOURCE
IRS "Estimated Taxes" (irs.gov/businesses/small-businesses-self-employed/
estimated-taxes), verified 2026-08-19: individuals must pay if they expect to
owe $1,000 or more; the penalty is generally avoided by owing under $1,000 after
withholding and credits, or paying at least 90% of the current year's tax, or
100% of the prior year's tax, whichever is smaller. An annualised income
installment method exists for uneven income, computed on Form 2210.
"""

IRS_EST = "https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes"
IRS_505 = "https://www.irs.gov/publications/p505"
IRS_2210 = "https://www.irs.gov/forms-pubs/about-form-2210"
IRS_1040ES = "https://www.irs.gov/forms-pubs/about-form-1040-es"
IRS_PAY = "https://www.irs.gov/payments"
IRS_SE = "https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes"


def _a(url, text):
    return f'<a href="{url}" rel="noopener" target="_blank">{text}</a>'


ARTICLES = [

# ---------------------------------------------------------------------------
{
 "slug": "how-to-calculate-estimated-taxes",
 "cat": "Tax Planning",
 "title": "How to Work Out What You Owe in Quarterly Taxes",
 "desc": "The estimated tax calculation, in the order you actually do it — income, self-employment tax, deductions, credits — and the shortcut most people should use instead.",
 "keywords": "self employed quarterly taxes, how to calculate estimated taxes, quarterly self employment tax",
 "read": "7 min read",
 "lede": "Almost everyone I talk to about this is doing one of two things: guessing, or setting aside a flat percentage someone told them once. Both work until the year they don't. Here is what the calculation actually consists of, and why I usually recommend the shortcut over the arithmetic.",
 "sections": [
   ("Start with whether you owe anything at all",
    "You are generally expected to make estimated payments if you expect to owe "
    "<strong>$1,000 or more</strong> when the return is filed, after withholding and "
    "credits. " + _a(IRS_EST, "That threshold is on the IRS estimated taxes page") + ". If "
    "you have a W-2 job alongside the business and enough is being withheld there, you may "
    "clear the bar without making a single quarterly payment."),

   ("Two taxes, not one",
    "This is the part that catches people in their first profitable year. Self-employment "
    "income is hit by income tax <em>and</em> by self-employment tax, which covers the "
    "Social Security and Medicare contributions an employer would otherwise split with you. "
    + _a(IRS_SE, "The IRS explains the mechanism") + ". Someone who budgeted only for income "
    "tax is short by a wide margin, and finds out in April."),

   ("The order the calculation actually runs in",
    "Estimate net self-employment income for the year. Add other income. Compute "
    "self-employment tax on the business portion, and take the deductible half of it as an "
    "adjustment. Apply your deductions and arrive at taxable income. Compute income tax. Add "
    "the self-employment tax back. Subtract credits and anything already withheld. What is "
    "left is the year's liability, and the quarterly payment is a portion of it. "
    + _a(IRS_1040ES, "Form 1040-ES") + " carries the worksheet."),

   ("Why I usually recommend the shortcut instead",
    "That whole calculation depends on forecasting a year you have not lived yet. The "
    "alternative is to base payments on last year's actual tax, which is a known number "
    "rather than a guess &mdash; and which, done correctly, protects you from the "
    "underpayment penalty regardless of how this year turns out. That is the safe harbour, "
    "and it is the single most useful thing in this system for anyone with uneven income."),

   ("Set the money aside where you cannot spend it",
    "The mechanical failure I see most often is not a bad calculation. It is a correct "
    "calculation followed by the money being gone in month two. A separate account that "
    "receives a fixed percentage of every deposit, moved the day the deposit lands, solves "
    "more estimated-tax problems than any spreadsheet."),

   ("Where the books come in",
    "Every figure above starts with net self-employment income, and that number is only as "
    "good as your bookkeeping. If the books are three months behind, the estimate is fiction "
    "&mdash; and the correction arrives with a penalty attached. This is the least glamorous "
    "argument for current books and the most expensive one to ignore."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "estimated-tax-safe-harbor",
 "cat": "Tax Planning",
 "title": "The Safe Harbor Rule for Estimated Taxes",
 "desc": "How to avoid the underpayment penalty without forecasting your year accurately — pay a set percentage of last year's tax and the penalty generally cannot reach you.",
 "keywords": "estimated tax safe harbor, avoid underpayment penalty, self employed estimated tax",
 "read": "6 min read",
 "lede": "This is the most useful rule in the estimated tax system and the one fewest self-employed people know exists. It lets you stop trying to predict a year you have not finished living.",
 "sections": [
   ("The rule itself",
    "You generally avoid the underpayment penalty if any one of these is true: you owe less "
    "than $1,000 after withholding and credits; you pay at least <strong>90% of the current "
    "year's tax</strong>; or you pay at least <strong>100% of the prior year's tax</strong>, "
    "whichever of the two is smaller. "
    + _a(IRS_EST, "The IRS states all three") + " on its estimated taxes page."),

   ("Why the prior-year option is the valuable one",
    "The 90% test requires knowing what this year's tax will be, which for most "
    "self-employed people is exactly the thing they cannot know in April. The prior-year "
    "test uses a number that is already on a filed return. It is fixed, it is verifiable, "
    "and it does not care whether this year turns out to be your best or your worst."),

   ("What that means in practice",
    "Take last year's total tax. Divide it by four. Pay that on schedule. If this year "
    "explodes, you will owe the difference at filing &mdash; but generally without a penalty, "
    "because you met the harbour. If this year collapses, you have overpaid and it comes back "
    "as a refund. The trade you are making is cash-flow timing in exchange for certainty, and "
    "for most people that is the right trade."),

   ("The exception worth knowing about",
    "There are special rules for farmers and fishermen, and for higher-income taxpayers a "
    "<em>higher</em> percentage of the prior year's tax applies instead of 100%. The IRS "
    "notes the exception on the estimated taxes page and carries the detail in "
    + _a(IRS_505, "Publication 505") + ". If your income is well above average, confirm which "
    "percentage applies to you before assuming 100% is enough &mdash; that assumption is the "
    "expensive version of this mistake."),

   ("Withholding counts, and it is treated generously",
    "If you also have W-2 income, tax withheld from those wages counts toward the harbour. "
    "It is also generally treated as paid evenly across the year regardless of when it was "
    "actually withheld &mdash; which is why increasing withholding late in the year can "
    "repair an underpayment in a way that a late estimated payment cannot. That asymmetry is "
    "genuinely useful in a year that went sideways."),

   ("What the safe harbour does not do",
    "It prevents the penalty. It does not reduce the tax. If you earn far more this year than "
    "last, you will still owe the balance at filing, and it can be a large number arriving all "
    "at once. Meeting the harbour and setting aside for the true liability are two different "
    "jobs, and doing only the first is how people end up with a penalty-free bill they cannot "
    "pay."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "1099-quarterly-taxes",
 "cat": "Tax Planning",
 "title": "1099 Quarterly Taxes: What Contractors Actually Owe",
 "desc": "Nobody withholds tax from a 1099 payment. What that means for what you owe, when, and the number most first-year contractors get wrong.",
 "keywords": "1099 quarterly taxes, contractor estimated taxes, 1099 self employment tax",
 "read": "6 min read",
 "lede": "The difference between a W-2 and a 1099 is not really the form. It is that with a W-2, someone else was quietly handling your tax all year. With a 1099, that job transferred to you and nobody mentioned it.",
 "sections": [
   ("Nothing was withheld, and that is the whole story",
    "A 1099 payment arrives gross. No federal income tax, no Social Security, no Medicare. "
    "The full amount hits your account and it all looks like yours. It is not &mdash; some "
    "portion of it belongs to a tax bill that has not arrived yet."),

   ("You now pay both halves",
    "As an employee, your employer paid half of your Social Security and Medicare and you "
    "paid the other half through payroll. As a contractor you pay both halves, through "
    "self-employment tax, on top of income tax. "
    + _a(IRS_SE, "The IRS sets out how it is computed") + ". This is the single biggest "
    "reason a first-year contractor's bill is larger than they expected."),

   ("There is an offset, and it is not the one people think",
    "You get to deduct the employer-equivalent half of your self-employment tax as an "
    "adjustment to income. That softens the blow. It does not eliminate it, and it is not a "
    "credit &mdash; it reduces taxable income, not the tax itself. People routinely "
    "overestimate what this is worth."),

   ("Business expenses are the real lever",
    "Self-employment tax is computed on <em>net</em> earnings, not gross receipts. Legitimate "
    "business expenses reduce the base for both income tax and self-employment tax, which "
    "makes each properly documented deduction worth more to a contractor than to an employee. "
    "This is why sloppy records cost contractors more than anyone else &mdash; and why "
    "reconstructing them in April never recovers everything."),

   ("Whether you owe quarterly at all",
    "The trigger is expecting to owe $1,000 or more when the return is filed, after "
    "withholding and credits. If contracting is a side income and your day job withholds "
    "enough, you may not need to pay quarterly at all. If contracting is the whole income, "
    "you almost certainly do. " + _a(IRS_EST, "The IRS threshold is here") + "."),

   ("If you also have a W-2 job",
    "You have a lever most full-time contractors do not: increasing withholding at the job "
    "instead of making estimated payments. Withheld tax is generally treated as paid evenly "
    "across the year, which makes it a more forgiving instrument than a late quarterly "
    "payment. For people with both kinds of income, this is often the simplest fix."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "missed-quarterly-tax-payment",
 "cat": "Tax Planning",
 "title": "You Missed a Quarterly Tax Payment. Now What?",
 "desc": "The underpayment penalty is interest, not a fine, and it keeps accruing. What to do the week you notice, and the two routes to reducing it.",
 "keywords": "missed quarterly tax payment, underpayment penalty, late estimated tax payment",
 "read": "5 min read",
 "lede": "This is not a crisis and it is not nothing. The penalty behaves like interest on the amount you were short, for the time you were short — which means the useful response is speed, not worry.",
 "sections": [
   ("What the penalty actually is",
    "It is not a flat fine. It is computed on how much you underpaid and for how long, which "
    "is why a payment made three weeks late costs far less than the same shortfall carried to "
    "April. The practical consequence: pay as soon as you notice, even if you cannot pay the "
    "full amount. Partial and immediate beats complete and later."),

   ("Do not skip the next one to compensate",
    "The instinct is to treat the year as already lost. It is not &mdash; the calculation runs "
    "period by period. Missing the next payment as well compounds a manageable problem into a "
    "worse one. Pay what you can now, and pay the next one on schedule."),

   ("Route one: the safe harbour may already cover you",
    "Before assuming you owe a penalty, check whether you have already paid at least 100% of "
    "last year's tax through a combination of estimated payments and withholding &mdash; or "
    "90% of this year's. " + _a(IRS_EST, "Either generally avoids the penalty") + ". People "
    "who front-loaded payments or have W-2 withholding alongside a business are sometimes "
    "covered without realising it."),

   ("Route two: annualise, if your income is lumpy",
    "The default calculation assumes you earned evenly across the year. If you did not "
    "&mdash; a seasonal business, one large project in the autumn, a slow start &mdash; you "
    "can annualise your income and compute unequal required payments, which often reduces or "
    "eliminates the penalty. This is done on "
    + _a(IRS_2210, "Form 2210") + ", and it is the most commonly missed remedy in this whole "
    "area."),

   ("The W-2 lever, one more time",
    "If you or a spouse have wage income, increasing withholding for the rest of the year is "
    "generally treated as if it had been paid evenly all year. That is a genuine repair "
    "mechanism for an underpayment already incurred, and there is no equivalent for estimated "
    "payments. If it is available to you, it is usually the first thing to try."),

   ("Then fix the cause",
    "Almost every missed payment I see traces back to the same thing: the money was never "
    "separated, so by the due date it had been spent on something legitimate. A dedicated "
    "account and a fixed transfer on every deposit prevents the next four."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "how-to-pay-estimated-taxes",
 "cat": "Tax Planning",
 "title": "How to Actually Pay Your Estimated Taxes",
 "desc": "The mechanics — which payment channels exist, what to keep as proof, and the state half that people forget until it is late.",
 "keywords": "how to pay estimated taxes, self employed estimated tax payments, pay quarterly taxes",
 "read": "5 min read",
 "lede": "Working out the number is the hard part. Paying it is not — but people still get tripped up, almost always on the same three things: applying a payment to the wrong year, keeping no proof, and forgetting the state entirely.",
 "sections": [
   ("The channels",
    "The IRS offers several ways to pay, including direct transfer from a bank account, card "
    "payments, and the Electronic Federal Tax Payment System. "
    + _a(IRS_PAY, "The IRS payments page") + " lists what is currently available. Whichever "
    "you use, the requirement is the same: the payment must be applied to the correct tax "
    "year and the correct payment period."),

   ("The mistake that causes the most cleanup",
    "Applying a payment to the wrong year. It is a dropdown, it takes one second to get wrong, "
    "and the result is a payment sitting against a year that did not need it while the year "
    "that did shows a shortfall. Untangling that is slow. Check the year before you confirm, "
    "every time."),

   ("Keep the confirmation",
    "Save the confirmation number and the date for every payment, somewhere that is not your "
    "inbox. At filing you will need the total paid and the dates, and reconstructing that from "
    "bank statements in April is exactly the kind of hour nobody has. A single running note "
    "with four lines a year is enough."),

   ("Do not forget the state",
    "Federal estimated payments are only half of it. Illinois has its own estimated payment "
    "system with its own thresholds and its own channel, and paying the IRS does nothing for "
    "it. This is the most common oversight I see, because the federal side gets all the "
    "attention and the state bill arrives quietly."),

   ("A note on timing",
    "The four payment periods are not evenly spaced calendar quarters, which surprises people "
    "who set reminders three months apart and end up late. Due dates also shift when they land "
    "on a weekend or holiday. Take the dates from "
    + _a(IRS_1040ES, "the current Form 1040-ES") + " each year rather than from memory or from "
    "an article &mdash; including this one."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "uneven-income-estimated-taxes",
 "cat": "Tax Planning",
 "title": "Estimated Taxes When Your Income Is Uneven",
 "desc": "The default rules assume you earn steadily across the year. If you do not, the annualized income method can cut or remove a penalty you would otherwise owe.",
 "keywords": "uneven income estimated taxes, annualized income installment method, seasonal business quarterly taxes",
 "read": "6 min read",
 "lede": "Four equal payments assume four equal quarters. Plenty of businesses do not work that way — a seasonal trade, a practice that bills in one lump, a year where the big project closed in November. There is a method for exactly this, and it is badly under-used.",
 "sections": [
   ("Why equal payments punish uneven income",
    "The default treats your annual income as if it arrived evenly. If you earned almost "
    "nothing in the first half and a great deal in the fourth quarter, that assumption says "
    "you should have been making large payments in April on income you had not yet earned. "
    "The result is a penalty for a period in which you genuinely had nothing to pay from."),

   ("The remedy",
    "The annualised income installment method computes what you should have paid in each "
    "period based on what you had actually earned by that point. Instead of four equal "
    "required payments, you get four unequal ones that follow your real income curve. "
    + _a(IRS_EST, "The IRS points to it") + " for anyone whose income is received unevenly, "
    "and it is calculated on " + _a(IRS_2210, "Form 2210") + "."),

   ("Who it helps most",
    "Seasonal businesses. Anyone paid on completion of long projects. Consultants with a "
    "small number of large invoices. People who started self-employment partway through the "
    "year. And anyone whose year contained one unusual event &mdash; a property sale, a "
    "settlement, a single outsized contract &mdash; that landed late."),

   ("What it costs you",
    "Record-keeping. To annualise, you need income and deductions by period, not just an "
    "annual total. If your books are current this is a report. If they are not, it is an "
    "archaeology project, and the method stops being worth the effort. This is the clearest "
    "case I know of where good bookkeeping converts directly into money."),

   ("The alternative that needs no forms",
    "If your prior year's tax was modest, the safe harbour may be simpler and cheaper than "
    "annualising. Paying based on last year's known figure sidesteps the whole question of "
    "when this year's income arrived. Annualising is the better tool when last year's tax was "
    "high and this year's income is both lower and lumpy &mdash; which is a narrower situation "
    "than people assume. Work out which applies before doing the extra work."),
 ],
},

# ---------------------------------------------------------------------------
{
 "slug": "first-year-self-employed-taxes",
 "cat": "Tax Planning",
 "title": "Your First Year Self-Employed: When Quarterly Taxes Start",
 "desc": "What changes the moment you have self-employment income, when the first payment is actually due, and the safe harbor quirk that makes year one easier than year two.",
 "keywords": "first year self employed taxes, when to start paying quarterly taxes, new business estimated tax",
 "read": "6 min read",
 "lede": "Year one has a quirk almost nobody takes advantage of: the safe harbour is measured against last year's tax, and last year you may have had very little. That can make your first year the cheapest one to get through — and your second the one that surprises you.",
 "sections": [
   ("What changes immediately",
    "The moment you have self-employment income, two things are true that were not before. "
    "Nobody is withholding tax on your behalf, and you now owe self-employment tax as well as "
    "income tax. Neither waits for you to feel established or to hit a revenue milestone."),

   ("When the first payment is actually due",
    "Not immediately, and not on a fixed anniversary of starting. Payments are due for the "
    "period in which the income was earned, which means someone who starts in August has a "
    "different first due date from someone who started in February. Take the periods from "
    + _a(IRS_1040ES, "the current Form 1040-ES") + " rather than assuming even quarters."),

   ("The year-one advantage",
    "The safe harbour lets you avoid the penalty by paying 100% of your <em>prior</em> year's "
    "tax. If your prior year was a W-2 job with full withholding, or a low-income year, that "
    "figure may be small or already satisfied. "
    + _a(IRS_EST, "The IRS rule is here") + ". It does not reduce what you eventually owe "
    "&mdash; it removes the penalty while you find your footing."),

   ("Which is exactly why year two bites",
    "Your first profitable year becomes the prior year for the safe harbour calculation in "
    "year two. The bar jumps, often sharply, and it does so at the same time as the balance "
    "for year one falls due. Two obligations landing together is the single most common cash "
    "crunch I see in new businesses, and it is entirely predictable a year in advance."),

   ("Set the habit before you need it",
    "Open a separate account now. Move a fixed percentage of every payment into it the day it "
    "arrives. Do it while the amounts are small and the habit is cheap to form, because the "
    "year you need it most is the year the numbers are large enough to be tempting."),

   ("The one thing worth doing early",
    "Get the bookkeeping running from the first transaction rather than reconstructing it "
    "later. Every calculation in this cluster &mdash; the estimate, the safe harbour, the "
    "annualisation &mdash; starts from net self-employment income. Year one is the cheapest "
    "time to set that up properly and the most expensive to skip."),
 ],
},

]
