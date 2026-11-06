# YouTube quiz app (working name)

Raised 2026-11-06. Learn from YouTube videos by answering questions generated from them, so the
content is retained instead of just watched.

## His framing (11-06)

- Tried it before by pasting links into GPT with a prompt; "kind of did it." Stopped, likely
  because there was no dedicated place for it to live.
- **Questions tailored to the viewer's level**: a video may be over their head; what are *they*
  expected to learn from it?
- For him first, but he'd like to share it.
- **"Just build it" mode** (his call): UI-heavy, no time for UI. Claude writes it.
- Wants: link to YouTube (Watch Later, history, likes), and an AI key so the AI lives in the app.

## Claude's flags (11-06)

- Retention comes mostly from spaced re-asking (1 day, 3 days, a week), not one quiz right after.
- **YouTube API can't read watch history or Watch Later** (both closed to the API since 2016).
  Liked videos and the user's own playlists can be read with OAuth. Workaround: a "Study"
  playlist the app watches, or paste/share a link.
- **Transcripts are the risky part.** The captions API only serves videos you own; unofficial
  endpoints break and block cloud IPs. Alternative to test: Gemini API takes public YouTube URLs
  directly. GPT "kind of" working may have been it guessing from the title and description.
- Sharing + AI key: bring-your-own-key keeps it free for him. Public Google sign-in with YouTube
  scopes needs Google verification past 100 test users.
- Similar tools exist (e.g. NotebookLM quizzes from YouTube links); fine for personal use.

## Open

- Does "must stay free" apply here like SpellIt?
- iPhone or Android (share-to-app works differently)?
- How to set the viewer's level: ask up front, a quick pre-check, or adapt from answers?
- First step proposed: prove transcript/video access on 3 of his real videos before any UI.

## Market scan (11-06, search snippets only, not verified on the live listings)

Crowded. He raised "extension instead of an app."

- **Chrome extensions:** YouTube Quiz Generator (pauses at intervals, bring-your-own key), LearnTube
  AI (pauses at topic breaks, Chrome on-device AI or Gemini), YouTube ReCapQuiz (Quiz button in
  the player), Ulearn (quiz when the video ends, spaced-repetition dashboard), Quizify, Yoututor,
  QuizFirst (quiz *before* watching).
- **Phone/web apps:** Flica, FlashCardify, Knotic, NoteTube (SM-2), QuizRise, anki-decks.com.
- **NotebookLM:** takes YouTube links; quizzes and flashcards, easy/medium/hard.
- **Gap seen so far:** difficulty settings exist, but nothing found that tailors to what *this*
  viewer already knows. That's his idea's angle, if any.
- **Extension upside:** runs on youtube.com in his own browser, so it can read captions from the
  page, which avoids the transcript problem. Downside: desktop only; no phone or TV.
- Proposed: use two existing ones for a week (one extension with spaced repetition, plus
  NotebookLM) and write down what's missing. That list is the spec.

## The real problem: mood and failing (11-06)

His words: being in the mood to learn from a video is the hard part. Days later he expects not to
know the answers, and then thinks "screw it, let me enjoy my video." He remembers *where* he saw
something, not what it said.

- Claude: failing to recall, then seeing the answer, is what makes it stick, so being wrong is
  the method working. It still *feels* like failing, and that feeling is the design problem.
- Most videos are just for fun. Opt in per video ("learn this one"), don't quiz everything.
- Knowing where to look is fine for trivia. It isn't for things he wants to think with.
- Idea floated: explain it back by voice instead of a quiz. Asked for his approach first.
- Example video: Veritasium on reaching absolute zero.

## His flow (11-06)

1. See a video, add it to Watch Later as usual.
2. While watching, if it's worth learning, add it to a **Study playlist**. Choosing changes how
   he pays attention, but the video stays enjoyable: no questions right after.
3. Later, when he's in the mood: the app asks "what did you learn about this video?" A
   conversation, not a quiz.
4. Topics he missed are noted. Later he's reminded about **only those topics**.
5. Constraint: don't spend more time than needed on the video.

Claude's read:
- His answer to "what makes being wrong OK" is built in: no score, just topics to revisit.
- Starting with "what did you learn?" is free recall, the strongest kind. The AI then asks about
  what he left out.
- A missed topic gets a 2-sentence explanation on the spot, plus a timestamp link. No rewatching.
- Reminders need push notifications, so this points to a phone app (an installed iPhone web app
  can push), not an extension. That puts transcripts back on a server; test Gemini with YouTube URLs.
- Risk: days between watching and talking may leave too little to recall. Watch for it.
