import requests
import json


test_text = """Mr. Mendoza was a man whose presence alone was enough to send chills down the spines of his students. His bald head gleamed under the fluorescent lights of the classroom, a reflection that seemed to mirror the cold, unforgiving nature of his teaching methods. Every step he took echoed with authority, his polished shoes clicking against the tile floor like a metronome of doom. His gaze, sharp and piercing, seemed to penetrate straight into the souls of those unfortunate enough to cross him.

Rumors circulated through the hallways that Mr. Mendoza hadn’t always been this way. Some said he had once been a passionate, inspiring teacher who genuinely cared about his students. But something had changed. Whether it was years of dealing with ungrateful teenagers, the stress of the school system, or perhaps some deeper, unspoken darkness, no one knew for sure. What was certain, however, was that the Mr. Mendoza who now stood before his classes was a far cry from the teacher he once was.

He ruled his classroom with an iron fist, his approach to discipline bordering on sadistic. Detention wasn’t just a punishment with Mr. Mendoza — it was an ordeal. A minute late? Detention. Forget your homework? Detention. Blink too loudly? You guessed it — detention. And his detentions weren’t the kind where you quietly sat and reflected on your mistakes. No, Mr. Mendoza made sure that every minute was filled with relentless, grueling tasks that pushed students to their limits. He had an uncanny ability to make even the most mundane assignments feel like torture. 

“I want a five-page essay on the history of punctuation,” he would bark with a cruel smirk. “Due by the end of detention. Double-spaced. Times New Roman. No excuses.”

The stories of his wrath were legendary. There was the time he made a student rewrite an entire 20-page paper because they had used a comma splice. Another time, a student who dared to chew gum in class was forced to scrape gum from the underside of every desk in the school. He had a special kind of joy in finding the smallest infractions and blowing them up into catastrophes. He was a master of psychological warfare, knowing exactly how to make students squirm with anxiety and dread.

And then there was his voice — a deep, gravelly tone that carried the weight of judgment and disappointment. He didn’t need to shout to command attention; a single, low-spoken command was enough to silence an entire room. When he called a student’s name, it was as if time froze. Everyone knew that being singled out by Mr. Mendoza meant nothing good was about to happen.

Even his tests were a testament to his cruelty. Tricky questions designed to trip up even the most prepared students. Multiple-choice answers that all seemed correct but were, in reality, carefully designed traps. Essays where the prompt was vague enough to make you second-guess everything you had ever learned.

But perhaps the most terrifying thing about Mr. Mendoza was his ability to get inside your head. He had a way of making students doubt themselves, to question their abilities and worth. “Is that really your best work?” he would ask, his expression neutral but his tone dripping with disdain. And just like that, confidence would wither away, replaced by self-doubt and fear.

Yet, despite all this, there was a strange, twisted respect for Mr. Mendoza. He was, after all, undeniably brilliant. His knowledge was vast, his understanding of his subject matter unparalleled. He could dissect a Shakespearean sonnet with surgical precision, analyze historical events with unnerving insight, and explain complex mathematical concepts in a way that made you question how you had ever found them difficult. 

But that brilliance came at a cost. It was as though Mr. Mendoza believed that to truly educate, one had to break down the student first — to strip away any semblance of confidence or comfort and rebuild them in his own harsh image. His philosophy was one of survival, where only the strongest, most resilient students would emerge from his class unscathed.

And so, year after year, students would enter his classroom with a mix of dread and curiosity. They had heard the stories, the whispered warnings passed down like ancient lore. They knew what awaited them, but they also knew that surviving Mr. Mendoza’s class meant emerging stronger, smarter, and perhaps a little more scarred. 

For Mr. Mendoza, education wasn’t about nurturing — it was about hardening. And while his methods were cruel, there was no denying that those who endured them came out the other side forever changed."""


base_url = "http://127.0.0.1:5000" 
path = "/new"
url = base_url + path

data = { "text": test_text, "doc_id": "892", "user_id": "steve", "notebook_id": "123" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)