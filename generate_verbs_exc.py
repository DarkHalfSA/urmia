# coding: utf8
from __future__ import unicode_literals


verb_roots = """

سیشدی#سیچ
یئدی#یئ
قینجیت#قینج
قاچماق#قاچ
اوزان#اوز
""".strip().split()


# Below code is a modified version of HAZM package's verb conjugator,
# with soem extra verbs (Anything in hazm and not in here? compare needed!)
VERBS_EXC = {}
with_nots = lambda items: items + ["ماق" + item for item in items]
simple_ends = ["دوم", "دوم", "دو", "دوک", "دوز", "دولر"]
narrative_ends = ["ه‌ام", "ه‌ای", "ه", "ه‌ایم", "ه‌اید", "ه‌اند"]
present_ends = ["م", "ی", "د", "یم", "ید", "ند"]

# special case of '#هست':
VERBS_EXC.update({conj: "هست" for conj in ["هست" + end for end in simple_ends]})
VERBS_EXC.update({conj: "هست" for conj in ["نیست" + end for end in simple_ends]})

for verb_root in verb_roots:
    conjugations = []
    if "#" not in verb_root:
        continue
    past, present = verb_root.split("#")

    if past:
        past_simples = [past + end for end in simple_ends]
        past_imperfects = ["می‌" + item for item in past_simples]
        past_narratives = [past + end for end in narrative_ends]
        conjugations = with_nots(past_simples + past_imperfects + past_narratives)
    if present:
        imperatives = ["ب" + present, "ن" + present]
        if present.endswith("ا") or present in ("آ", "گو"):
            present = present + "ی"
        present_simples = [present + end for end in present_ends]
        present_imperfects = ["می‌" + present + end for end in present_ends]
        present_subjunctives = ["ب" + present + end for end in present_ends]
        conjugations += (
            with_nots(present_simples + present_imperfects)
            + present_subjunctives
            + imperatives
        )

    if past.startswith("آ"):
        conjugations = set(
            map(
                lambda item: item.replace("بآ", "بیا").replace("نآ", "نیا"),
                conjugations,
            )
        )

    VERBS_EXC.update({conj: (past,) if past else present for conj in conjugations})
