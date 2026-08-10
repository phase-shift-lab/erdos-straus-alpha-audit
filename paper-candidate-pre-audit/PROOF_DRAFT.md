# Proof draft — exact compatibility criterion

Let (P,\alpha,d,b',c'\in\mathbb N), set (g=\alpha d), (b=gb'), (c=gc'), and (\delta=\alpha d^2). Assume

\[
4bc-b-c=P\delta. \tag{1}
\]

Define

\[
\alpha_{\mathrm{lat}}=\gcd(g,b'+c'),
\qquad d_{\mathrm{lat}}=g/\alpha_{\mathrm{lat}}. \tag{2}
\]

Put (s=b'+c') and (h=\gcd(\alpha,P)). Substitution into (1), followed by division by (\alpha d), gives

\[
4\alpha d b'c'-s=Pd. \tag{3}
\]

Modulo (g=\alpha d), this says (s\equiv-Pd\pmod{\alpha d}). Hence

\[
\alpha_{\mathrm{lat}}
=\gcd(\alpha d,s)
=\gcd(\alpha d,Pd)
=d\gcd(\alpha,P)=dh. \tag{4}
\]

Therefore

\[
d_{\mathrm{lat}}=\frac{\alpha d}{dh}=\frac{\alpha}{h}. \tag{5}
\]

It follows that

\[
\alpha_{\mathrm{lat}}d_{\mathrm{lat}}^2
=dh\left(\frac{\alpha}{h}\right)^2
=\frac{d\alpha^2}{h}. \tag{6}
\]

Comparing (6) with (\delta=\alpha d^2), and cancelling the positive factor (\alpha d), gives

\[
\delta=\alpha_{\mathrm{lat}}d_{\mathrm{lat}}^2
\quad\Longleftrightarrow\quad
d=\frac{\alpha}{\gcd(\alpha,P)}. \tag{7}
\]

This proves the criterion. No primality assumption was used until the prime specialization.

## Exact diagonal period

For

\[
L=\{(u,v)\in\mathbb Z^2:u b'+v c'\equiv0\pmod g\},
\]

a diagonal vector ((t,t)) belongs to (L) exactly when (g\mid t(b'+c')). Thus the least positive diagonal step is

\[
t_{\mathrm{diag}}=\frac{g}{\gcd(g,b'+c')}
=\frac{\alpha}{\gcd(\alpha,P)}. \tag{8}
\]

This is a lattice invariant and is not generally the square-root factor (d).

## Prime specialization

If (P) is prime and (\alpha) is square-free, then \(\gcd(\alpha,P)\) is (1) or (P). Therefore (7) becomes (d=\alpha) when (P\nmid\alpha), and (d=\alpha/P) when (P\mid\alpha).

## Two infinite structural families

### Compatible family

For (t\ge0), let

\[
\alpha=2,\quad d=2,\quad b'=1,\quad c'=8t+5,\quad P=60t+37.
\]

Then (g=4,\delta=8,b=4,c=32t+20,A=16t+10), and

\[
4bc-b-c=480t+296=8(60t+37)=P\delta.
\]

The lattice values are (\alpha_{\mathrm{lat}}=\gcd(4,8t+6)=2) and (d_{\mathrm{lat}}=2), so the bridge holds. The source gcd filters also hold. Since \(\gcd(37,60)=1\), Dirichlet's theorem gives infinitely many prime values in this progression.

### Incompatible source-filter family

For (u\ge0), let

\[
\alpha=3,\quad d=1,\quad b'=1,\quad c'=12u+10,\quad P=132u+109.
\]

Then (g=3,\delta=3,b=3,c=36u+30,A=36u+30), and

\[
4bc-b-c=396u+327=3(132u+109)=P\delta.
\]

The source gcd filters hold because \(\gcd(1,3)=1\) and \(\gcd(12u+10,3)=1\). But (\alpha_{\mathrm{lat}}=\gcd(3,12u+11)=1), (d_{\mathrm{lat}}=3), and (\alpha_{\mathrm{lat}}d_{\mathrm{lat}}^2=9\ne3). Since \(\gcd(109,132)=1\), Dirichlet's theorem gives infinitely many prime values in this progression.

These families establish structural separation; they are not standalone claims of novelty.
