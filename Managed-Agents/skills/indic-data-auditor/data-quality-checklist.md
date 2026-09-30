
# Data Quality & Acceptance Checklist

## 1. Machine Translation (MT) — Appendix A1

- [ ] No word-by-word literal translation; must preserve natural target syntax and idiomatic usage.
- [ ] Named entities and proper nouns are accurately transliterated (not semantically translated).
- [ ] Punctuation, numbers, currency symbols, and numerical formats match the source intent.
- [ ] Dialectal consistency maintained across the document.

## 2. ASR Audio & Transcription — Appendices A2 & A3

- [ ] Audio format: Uncompressed WAV, minimum 16 kHz sampling rate, 16-bit mono.
- [ ] Noise floor: Clean background, no overlapping speakers, clipping, or heavy reverb.
- [ ] Transcription is strictly verbatim: Include colloquialisms, discourse markers, and false starts.
- [ ] Standard script orthography used (no Latin transliteration in native script fields).
- [ ] Numbers are written out as spoken words (e.g., "एक सौ" instead of "100" if spoken that way).

## 3. Text-to-Speech (TTS) Studio Audio — Appendix A4

- [ ] Recorded by professional voice artists in an acoustically treated studio (< -45 dB noise floor).
- [ ] High resolution: 48 kHz / 24-bit WAV PCM.
- [ ] Consistent pitch, speed, and volume across long-form recording sessions.
- [ ] Zero mouth clicks, breath pops, or clipping.

## 4. Optical Character Recognition (OCR) — Appendix A5

- [ ] Document OCR: Minimum 300 DPI, flatbed or deskewed scan, high contrast, no bleed-through.
- [ ] Scene OCR: Bounding box annotations tight around text, polygon tags for curved text.
- [ ] Complex conjuncts and diacritics (matras) fully legible and unambiguous.
