from django.db import models


class Meter(models.Model):
    number = models.fields.CharField(verbose_name="Count number", max_length=50, blank=False, null=False)
    verify_date = models.fields.DateField(verbose_name="Verify date")
    two_tariff = models.fields.BooleanField(verbose_name="Two-tariff", null=False, default=False)
    units = models.fields.CharField(verbose_name="Units", max_length=20, blank=False, null=False)


class Metric(models.Model):
    title = models.fields.CharField(verbose_name="Title", max_length=50, blank=False, null=False)
    account_number = models.fields.CharField(verbose_name="Account number", max_length=50, blank=False, null=False)
    meter = models.ForeignKey(Meter, verbose_name="Meter", on_delete=models.CASCADE, null=False, default=None)


class Measuring(models.Model):
    value_t1 = models.fields.DecimalField(verbose_name="Day", max_digits=7, decimal_places=3)
    value_t2 = models.fields.DecimalField(verbose_name="Night", max_digits=7, decimal_places=3)
    meter = models.ForeignKey(Meter, verbose_name="Meter", on_delete=models.CASCADE, null=False, default=None)


class Provider(models.Model):
    title = models.fields.CharField(verbose_name="Title", max_length=50, blank=False, null=False)
