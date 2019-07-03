#mugi
aa=input().split()
kk=int(aa[1])
ax=list(map(int,input().split()))
ax.sort(reverse=True)
print(ax[kk-1])
