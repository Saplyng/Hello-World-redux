private static final String TAG = "MainActivity";

private TextView mDisplayDate;
private DatePickerDialog.OnDateSetListener mDateSetListener;



mDisplayDate = (TextView) findViewById(R.id.tvDate);
mDisplayDate setOnClickListener(new View.OnClickListener() {
    @Override
    public void OnClick(View view){
        Calander cal = Calander.getInstance();
        int year = cal.get(Calander.YEAR);
        int month = cal.get(Calander.MONTH);
        int day = cal.get(Calander.DAY_OF_MONTH);

        DatePickerDialog dialog = new DatePickerDialog(
            MainActivity.this,
            android.R.style.Theme_Holo_Light_Dialog_MinWidth,
            mDateSetListener,
            year,month,day);

        dialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));
        dialog.show()
    }
}));

mDateSetListener = new DatePickerDialog.OnDateSetListener(){
    @Override
    public void onDateSet(DatePicker datePicker, int year, int month, int day){
        month = month + 1
        log.d(Tag, "onDateSet: mm/dd/yyyy: " + month + "/" + day + "/" + year );
        
        String date = month + "/" + day + "/" + year;
        mDisplayDate.setText(date);
    }


};