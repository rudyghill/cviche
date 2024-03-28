.fam T
.nr PS 10p
.nr VS 15p
.ds CH
.
.
.de heading
.   nf
.   ps 14
.   B "\\$1"
\h'0n'\v'-1.2n'\
\l'\\n(.lu\(ul'\
\m[default]
.   ps 10
.   sp -.2
.   fi
..

.ce 2
.ps 18
.B "John Doe"
.ps 10
johndoe@example.com

.heading "Experience"
.TS
tab(;) nospaces;
rW15 lx.
{{experience}}
.TE

.heading "Education"
.TS
tab(;) nospaces;
rW15 lx.
{{education}}
.TE

.heading "Skills"
{{skills}}
