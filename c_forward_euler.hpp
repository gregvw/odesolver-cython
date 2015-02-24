typedef double (*Callback)(void *feval, const double &y, const double &t);

void forward_euler(Callback callback, void *feval, double *y, double *t, int nt){
   
    for(int i=0;i<nt-1;++i) {
        y[i+1] = y[i] + (t[i+1]-t[i])*callback(feval,y[i],t[i]);
    }
}
