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
