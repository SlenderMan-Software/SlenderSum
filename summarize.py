from dotenv import load_dotenv
import re
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
import json

def clean_json_output(raw_response):
    # Strip markdown code fences (e.g., ```json ... ```)
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_response.strip(), flags=re.DOTALL)
    return cleaned.strip()


test_text = """
Mr. Mendoza was a man whose presence alone was enough to send chills down the spines of his students. His bald head gleamed under the fluorescent lights of the classroom, a reflection that seemed to mirror the cold, unforgiving nature of his teaching methods. Every step he took echoed with authority, his polished shoes clicking against the tile floor like a metronome of doom. His gaze, sharp and piercing, seemed to penetrate straight into the souls of those unfortunate enough to cross him.

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

For Mr. Mendoza, education wasn’t about nurturing — it was about hardening. And while his methods were cruel, there was no denying that those who endured them came out the other side forever changed.

"""

summaries = ["The Central Intelligence Agency (CIA) is a civilian foreign intelligence service of the U.S. government responsible for collecting and analyzing intelligence, conducting covert operations, and advancing national security.  Headquartered in Langley, Virginia, it's a key part of the U.S. Intelligence Community, reporting to the Director of National Intelligence.  The CIA's functions include human intelligence (HUMINT) coordination, support for foreign intelligence services, and paramilitary operations.  Its history includes involvement in numerous controversial events, such as coups in Iran, Guatemala, and Chile, and operations like MKUltra and CHAOS.  The agency has faced scrutiny for its use of torture, assassination, and other controversial tactics.", 
'The M134 Minigun is a 7.62 mm six-barrel rotary machine gun with a high rate of fire (2,000-6,000 rounds per minute). It uses a Gatling-style rotating barrel assembly and an external power source, typically an electric motor.  The term "minigun" is often used more broadly to describe similar externally powered rotary guns.', 
"Free France, led by Charles de Gaulle, was a government-in-exile established in London in 1940 after the Fall of France.  It opposed the Vichy French government and fought alongside the Allies against Axis forces, gaining support in several French colonies.  De Gaulle's Appeal of 18 June called for French resistance against Nazi Germany.", 
]

def summarize(source):
   #If you want to use the Gemini 2.0 model, uncomment the line below and comment out the one below it. Beware, it is slow albiet more cost effective.
   # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    prompt = [
        ("system", 
         """
         You are an AI summarizer. Your task is to analyze a block of text and return a structured JSON object.
You are a JSON-only summarizer.

Strictly return ONLY a JSON object in this format and nothing else:

{
  "summary": "Your summary here.",
  "key_topics": ["Topic A", "Topic B", "etc."],
  "title": "Your title here"
}

Rules:
- Do not include any introductory or explanatory text.
- DO NOT use markdown or any other formatting!!!!! 
- Ensure the JSON is syntactically valid (can be parsed by json.loads in Python).
- Each topic in 'key_topics' should be a short phrase or keyword.
- DO NOT explain anything.
- DO NOT include markdown, commentary, or bullet points outside the JSON.
- DO NOT write 'Here is the summary:' or anything before/after the JSON.
- DO NOT use triple backticks or markdown code blocks.
-GIVE RAW, UNFORMATTED JSON ONLY.

         
         """
         ),
        ("human", source)
    ]
    response = llm.invoke(prompt)
    try:
        raw = response.content
        cleaned = clean_json_output(raw)
        parsed = json.loads(cleaned)
        summary = parsed.get("summary")
        key_topics = parsed.get("key_topics", [])
        title = parsed.get("title")
        #return parsed["summary"], parsed["key_topics"], parsed["title"]
        return summary, key_topics, title
    except json.JSONDecodeError:
        print("❌ JSON decode error. Raw output was:")
        print(response.content)
        return None, [], None




def metasum(sources):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    prompt = [
        ("system", 
         """
         You are an AI summarizer. Your task is to analyze a block of text and return a structured JSON object.
You are a JSON-only summarizer.

Strictly return ONLY a JSON object in this format and nothing else:

{
  "summary": "Your summary here.",
}

Rules:
- Do not include any introductory or explanatory text.
- DO NOT use markdown or any other formatting!!!!! 
- Ensure the JSON is syntactically valid (can be parsed by json.loads in Python).
- DO NOT explain anything.
- DO NOT include markdown, commentary, or bullet points outside the JSON.
- DO NOT write 'Here is the summary:' or anything before/after the JSON.
- DO NOT use triple backticks or markdown code blocks.
-GIVE RAW, UNFORMATTED JSON ONLY.

         
         """
         ),
        ("human", sources)
    ]
    response = llm.invoke(prompt)
    try:
        raw = response.content
        cleaned = clean_json_output(raw)
        parsed = json.loads(cleaned)
        summary = parsed.get("summary")
        #return parsed["summary"], parsed["key_topics"], parsed["title"]
        return { "summary": summary }
    except json.JSONDecodeError:
        print("❌ JSON decode error. Raw output was:")
        print(response.content)
        return None


#For testing purposes:
#print(metasum(summaries)) 
metasum(summaries)

