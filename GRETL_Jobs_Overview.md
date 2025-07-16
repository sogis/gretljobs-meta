# GRETL Jobs Übersicht

**Automatisch generiert am:** 16.07.2025 08:23
**Anzahl Jobs:** 77

## Inhaltsverzeichnis

- [Zeitgesteuerte Jobs (Cron)](#zeitgesteuerte-jobs-cron)
- [Upstream-gesteuerte Jobs](#upstream-gesteuerte-jobs)
- [Schema-Übersicht](#schema-übersicht)

---

## Zeitgesteuerte Jobs (Cron)

**Anzahl:** 63

| Job | Status | Schedule | Quell-Tabellen | Ziel-Tabellen |
|-----|--------|----------|----------------|---------------|
| ada_archaeologie_pub | Aktiv | So ~1-3h | AS, ada_archaeologie_v1.fachapplikation_regierungsratsbeschluss, ada_archaeologie_v1.geo_ablage_gemeinde (+12 weitere) | ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet, ada_archaeologie_v1.fachapplikation_fundstelle, ada_archaeologie_v1.geo_flaeche (+3 weitere) |
| afu_altlasten_import_pub | Aktiv | ~1-3h |  |  |
| afu_asiatische_hornisse_pub | Aktiv | ~1-3h | afu_asiatische_hornisse_v1.asia_hornisse_ash |  |
| afu_erdwaermesonden_private_quellen_pub | Aktiv | ~1-3h | afu_erdwaermesonden_private_quellen_v1.private_quelle |  |
| afu_erdwaermesonden_pub | Aktiv | ~1-3h | afu_erdwaermesonden_v2.erdwaermesonden_bohrung, afu_erdwaermesonden_v2.erdwaermesonden_anlage |  |
| afu_ewsabfrage_2d | Aktiv | So 04:00 | afu_altlasten_pub_v2.belasteter_standort, afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzareal, afu_ewsabfrage_2d_v1.tiefenbeschraenkung (+16 weitere) |  |
| afu_grundlagendaten_ews_import | Aktiv | ~1-3h | bohrung. |  |
| afu_igel | Aktiv | So ~3-4h | afu_igel.igel_standort, LATERAL, afu_igel.igel_stall |  |
| afu_naturereigniskataster_mgdm_import | Aktiv | ~1-3h | afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_r, afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_w, afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_l (+12 weitere) |  |
| afu_neophyten_pub | Aktiv | ~6:xx | neophyten |  |
| afu_onlinerisk_transfer | Aktiv | ~18-19h | afu_online_risk.verordnungsrelevanz, gebaeude, untersuchungseinheit (+10 weitere) | with |
| afu_stehende_gewaesser_abgleich | Aktiv | So ~1-3h | afu_stehende_gewaesser_v1.stehendes_gewaesser, agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze, agi_dm01avso24.bodenbedeckung_boflaeche | afu_stehende_gewaesser_v1.stehendes_gewaesser |
| afu_wasserbewirtschaftung_pub | Aktiv | So ~1-3h | afu_wasserversorg_obj_v1.quellwasserbehaelter__dokument, afu_wasserversorg_obj_v1.pumpwerk, afu_wasserversorg_obj_v1.sammelbrunnstube (+26 weitere) | afu_wasserbewirtschaftung_pub_v2.wassrbwrtschftung_quelle |
| agem_finanz_und_lastenausgleich | Aktiv | ~1-3h | agem_fila.strassen_strassenachse, agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze |  |
| agi_adressen_pub | Aktiv | ~1-3h | agi_dm01avso24.gebaeudeadressen_gebaeudeeingang, agi_dm01avso24.gebaeudeadressen_hausnummerpos, agi_dm01avso24.gebaeudeadressen_strassenstueck (+5 weitere) |  |
| agi_av_dm01_mopublic_pub | Aktiv | 21:00 | agi_dm01avso24.fixpunktekatgrie3_hfp3nachfuehrung, agi_dm01avso24.nomenklatur_ortsname, agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchamt (+81 weitere) | mopublic_grundstueck, mopublic_gemeindegrenze, mopublic_hoheitsgrenzpunkt (+21 weitere) |
| agi_av_export_ai | Aktiv | ~1-3h |  |  |
| agi_av_gb_abgleich_pub | Aktiv | ~1-3h | agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging, agi_dm01avso24.liegenschaften_liegenschaft, agi_dm01avso24.liegenschaften_projgrundstueck (+12 weitere) | agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging, agi_av_gb_abgleich_import.differenzen_staging |
| agi_av_gwr_abgleich_pub | Aktiv | ~1-3h | agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen, agi_av_gwr_abgleich_import_v1.av_gwr_differnzen_av_gwr_differenzen | agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen |
| agi_av_kaso_abgleich_pub | Aktiv | ~3:xx | agi_dm01avso24.liegenschaften_liegenschaft, agi_dm01avso24.liegenschaften_projgrundstueck, agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging (+14 weitere) | agi_av_kaso_abgleich_v1.differenzen_staging, agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging |
| agi_av_meldewesen | Aktiv | ~3-4h | agi_av_meldewesen_import_v1.meldungen_meldung, agi_dm01avso24.liegenschaften_liegenschaft, agi_dm01avso24.liegenschaften_bergwerk (+5 weitere) | agi_av_meldewesen_work_v1.meldungen_meldung |
| agi_av_mocheckso | Aktiv | ~1-3h | agi_av_mocheckso.mocheckso_errors_mocheckso_error |  |
| agi_ch_gemeinden | Aktiv | 1. ~1-3h | agi_swissboundaries3d_v2.tlm_grenzen_tlm_kantonsgebiet, agi_swissboundaries3d_v1.tlm_grenzen_tlm_kantonsgebiet, agi_swissboundaries3d_v2.surface3d (+11 weitere) |  |
| agi_dmav_fixpunkte2_import | Aktiv | ~1-3h |  |  |
| agi_dmav_fixpunktelv_import | Aktiv | ~1-3h |  |  |
| agi_dmav_hoheitsgrenzen_lv_import | Aktiv | ~1-3h |  |  |
| agi_dmav_hoheitsgrenzpunkte_lv_import | Aktiv | ~1-3h |  |  |
| agi_dmav_plz_ortschaft_import | Aktiv | ~1-3h |  |  |
| agi_gb2av_controlling | Aktiv | ~1-3h | agi_gb2av.vollzugsgegnstnde_vollzugsgegenstand, agi_dm01avso24.liegenschaften_projgrundstueck, agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta (+10 weitere) | SET, agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta, agi_gb2av_controlling.controlling_av2gb_mutationen |
| agi_generate_matomo_reports | Aktiv | 1. ~4:xx |  |  |
| agi_gwr_pub | Aktiv | ~3-4h | agi_gwr_v1.gwr_gebaeude, agi_gwr_v1.gwr_codes, agi_gwr_v1.gwr_wohnung (+3 weitere) |  |
| agi_hoheitsgrenzen_pub | Aktiv | ~1-3h | agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksname_a3, agi_hoheitsgrenzen_v1.hoheitsgrenzen_kantonsname_pos, agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk (+17 weitere) | agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze, agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze_generalisiert, agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze (+3 weitere) |
| agi_kartenkatalog_pub | Aktiv | ~1-3h | simi.simidata_postgres_table, simi.simitheme_theme_publication, simi.simiproduct_properties_in_list (+10 weitere) |  |
| agi_stac | Aktiv | ~5-6h |  |  |
| agi_swisstopo_gebaeudeadressen | Aktiv | 2. ~1-3h | agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_address, agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_stn, agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_zip |  |
| alw_landwirtschaft_tierhaltung_import_bodenbedeckung | Aktiv | Fr ~3-4h |  |  |
| alw_landwirtschaft_tierhaltung_import_massnahmen | Aktiv | 1. ~3-4h |  |  |
| alw_landwirtschaft_tierhaltung_pub | Aktiv | ~2-4h | alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_standorte, alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_summe_tiere_flaechen, alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_kultur_flaechen (+7 weitere) |  |
| alw_strukturverbesserungen_pub | Aktiv | Sa ~1-3h | alw_strukturverbesserungen.elektrizitaet_linien, alw_strukturverbesserungen.oekologie_punkte, alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet_projekt (+49 weitere) |  |
| alw_tiergesundheit_pflanzengesundheit_massnahmen_pub | Aktiv | ~1-3h | alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_pflanzengesundheit_schadorganismen, alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_bienensperrgebiet, alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_tiergesundheit_massnahmengebiet |  |
| amb_zivilschutz_adressen_export | Aktiv | 1. ~1-3h | agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis, agi_mopublic_pub.mopublic_bodenbedeckung, agi_mopublic_pub.mopublic_gebaeudeadresse (+7 weitere) | amb_zivilschutz_adressen_staging_pub.adressen_zivilschutz |
| arp_arbeitszonenbewirtschaftung_inventar_pub | Aktiv | ~1-3h | arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_flaeche, arp_arbeitszonenbewirtschaftung_v1.regionen_region, arp_arbeitszonenbewirtschaftung_staging_v1.inventar_flaeche_v (+5 weitere) | arp_arbeitszonenbewirtschaftung_staging_v1.arbtsznnng_nvntar_arbeitszonenbewirtschaftung_inventar, arp_arbeitszonenbewirtschaftung_v1.bewertung_bewertung |
| arp_auswertung_nutzungsplanung_pub | Aktiv | ~1-3h | agi_mopublic_pub.mopublic_bodenbedeckung, arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_und_lsgrenzen, arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_gines (+9 weitere) |  |
| arp_bauzonengrenzen_pub | Aktiv | ~1-3h | arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze, arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung | arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze |
| arp_fledermaus | Aktiv | ~1-3h | arp_fledermaus_v1.fledermausfundrte_fledermausfundort |  |
| arp_mjpnatur_gelan_export | Aktiv | ~1-3h | arp_mjpnl_v2.mjpnl_beurteilung_hostet, arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen, arp_mjpnl_v2.mjpnl_vereinbarung | arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen |
| arp_mjpnatur_pub | Aktiv | ~1-3h | arp_mjpnl_v2.mjpnl_beurteilung_obl, arp_mjpnl_v2.mjpnl_beurteilung_wiese, arp_mjpnl_v2.mjpnl_beurteilung_hostet (+9 weitere) |  |
| arp_mjpnl_v2_auszahlung | Aktiv | 15. ~1-3h |  |  |
| arp_mjpnl_v2_gelan_update | Aktiv | ~1-3h |  |  |
| arp_mjpnl_v2_zahlungslauf | Aktiv | ~1-3h | agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeinde, agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk | abrechnung_per_leistung, der |
| arp_nutzungsplanung_planregister_export | Aktiv | ~1-3h |  |  |
| arp_nutzungsvereinbarung_pub | Aktiv | ~1-3h | agi_dm01avso24.liegenschaften_liegenschaft, arp_nutzungsvereinbarung.nutzungsvrnbrngen_projekte, agi_dm01avso24.gemeindegrenzen_gemeinde (+4 weitere) |  |
| arp_richtplan_grundnutzung_pub | Aktiv | 1. ~1-3h | arp_richtplan_pub_v2.richtplankarte_grundnutzung, arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung | arp_richtplan_pub_v2.richtplankarte_grundnutzung |
| avt_bodenfaktor_pub | Aktiv | So ~2-5h | avt_bodenfaktor.t_ili2db_dataset, avt_bodenfaktor.t_ili2db_basket, avt_bodenfaktor.bodenfaktor (+1 weitere) | avt_bodenfaktor.bodenfaktor |
| awjf_efj | Aktiv | ~4-5h | LATERAL, awjf_efj_v1.efj_abgaenge |  |
| awjf_forstreviere_pub | Aktiv | ~1-3h | awjf_forstreviere.forstreviere_forstrevier, awjf_forstreviere.forstreviere_forstreviergeometrie, awjf_forstreviere.forstreviere_forstkreis |  |
| awjf_programm_biodiversitaet_wald_pub | Aktiv | ~1-3h | string_agg, agi_dm01avso24.nomenklatur_flurname, awjf_forstreviere.forstreviere_forstreviergeometrie (+13 weitere) |  |
| awjf_rodung_rodungsersatz_mgdm | Aktiv | 1. ~1-3h | awjf_rodung_rodungsersatz_mgdm_v1.objekt, awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_, awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_ (+8 weitere) | awjf_rodung_rodungsersatz_mgdm_v1.objekt, awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_, awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_ (+2 weitere) |
| awjf_schutzwald_pub | Aktiv | ~1-3h | awjf_schutzwald_v1.schutzwald_info, awjf_schutzwald_pub_v1.behandelte_flaeche_status, awjf_schutzwald_pub_v1.nais_code (+8 weitere) | awjf_schutzwald_pub_v1.behandelte_flaeche, awjf_schutzwald_pub_v1.schutzwald, awjf_schutzwald_pub_v1.dokument (+1 weitere) |
| awjf_waldpflege_kontrolle | Aktiv | ~1-3h | awjf_gesuchsteller.gesuchsteller_gesuchsteller, awjf_waldpflege_erfassung.waldpflege_waldpflege |  |
| awjf_waldportal | Aktiv | ~1-3h |  |  |
| awjf_wegsanierungen_pub | Aktiv | ~1-3h | awjf_wegsanierungen_v1.wegsanierungen_wegsanierung |  |
| dsbjd_ebauso_rahmenmodell_pub | Aktiv | ~3-4h | agi_mopublic_pub.mopublic_bodenbedeckung, agi_mopublic_pub.mopublic_gebaeudeadresse, alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche (+25 weitere) | dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_punkt, dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_linie, dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_punkt (+5 weitere) |

---

## Upstream-gesteuerte Jobs

**Anzahl:** 14

| Job | Status | Upstream | Quell-Tabellen | Ziel-Tabellen |
|-----|--------|----------|----------------|---------------|
| ada_denkmalschutz_pub | Aktiv | oerebv2_einzelschutz_denkmal | ada_denkmalschutz_v1.fachapplikation_denkmal, ada_denkmalschutz_v1.oereb_doclink_v, ada_denkmalschutz_v1.gis_geometrie |  |
| afu_bodendaten_nabodat_abfrage_pub | Aktiv | afu_bodenprofilstandorte_nabodat_pub | afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf, afu_bodendaten_nabodat_v1.punktdaten_projektstandort, afu_bodendaten_nabodat_v1.codelistnnlysdten_analyseparameter (+65 weitere) | afu_bodendaten_nabodat_abfrage_pub_v1.horizont, afu_bodendaten_nabodat_abfrage_pub_v1.bodenprofil |
| afu_geotope_pub | Aktiv | oereb_einzelschutz_geotop | afu_geotope.geotope_fundstelle_grabung_dokument, afu_geotope.geotope_erratiker_fachbereich, afu_geotope.geotope_fundstelle_grabung (+27 weitere) |  |
| afu_stehende_gewaesser_pub | Aktiv | afu_stehende_gewaesser_abgleich | afu_stehende_gewaesser_v1.stehendes_gewaesser, agi_dm01avso24.bodenbedeckung_boflaeche |  |
| agi_gebaeudeinformationen_pub | Aktiv | agi_av_dm01_mopublic_pub | agi_mopublic_pub.mopublic_bodenbedeckung, agi_mopublic_pub.mopublic_gebaeudeadresse, agi_mopublic_pub.mopublic_objektname_pos (+2 weitere) |  |
| agi_grundbuchplan_pub | Aktiv | agi_av_dm01_mopublic_pub | agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis, agi_dm01avso24.liegenschaften_liegenschaft, agi_grundbuchplan_pub.grundbuchplan_liegenschaft (+10 weitere) | agi_grundbuchplan_pub.grundbuchplan_grundstueckpos |
| arp_richtplan_abbaustellen_pub | Aktiv | afu_abbaustellen_pub | afu_abbaustellen_pub_v2.abbaustelle, arp_richtplan_pub_v2.detailkarten_flaeche | arp_richtplan_pub_v2.detailkarten_flaeche |
| arp_richtplan_fruchtfolgeflaechen_pub | Aktiv | alw_fruchtfolgeflaechen_pub | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche, alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche |
| arp_richtplan_gewaesserschutz_pub | Aktiv | afu_gewaesserschutz_zonen_areale_pub | afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzareal, arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche, afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche |
| arp_richtplan_naturreservate_pub | Aktiv | arp_naturreservate_pub | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche, arp_naturreservate_pub.naturreservate_reservat | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche |
| arp_richtplan_oeffentlicher_verkehr_pub | Aktiv | avt_oeffentlicher_verkehr_pub | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie, avt_oeffentlicher_verkehr_pub.oeffntlchr_vrkehr_netz | arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie |
| arp_sein_strukturdaten_pub | Aktiv | arp_auswertung_nutzungsplanung_pub |  |  |
| awjf_efj_geodaten_upload | Aktiv | awjf_jagdreviere_jagdbanngebiete_pub, awjf_gewaesser_fischerei_pub | awjf_jagdreviere_jagdbanngebiete_v1.jagdreviere_jagdreviere, awjf_efj_geodaten_upload_v1.gebiete_gebiet, agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze (+1 weitere) | awjf_efj_geodaten_upload_v1.transfermetadaten_datenbestand, awjf_efj_geodaten_upload_v1.gebiete_gebiet |
| awjf_statische_waldgrenzen_export_ai | Aktiv | awjf_statische_waldgrenze_pub | awjf_statische_waldgrenze.geobasisdaten_typ, awjf_statische_waldgrenze_mgdm_v1.multilingualuri, awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument (+9 weitere) | awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument, awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ, awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_waldgrenze_linie (+2 weitere) |

---

## Schema-Übersicht

**Anzahl Schemas:** 99

| Schema | Beschreibung | Anzahl Jobs | Anzahl Tabellen |
|--------|--------------|-------------|-----------------|
| ada_archaeologie_pub_v1 | Amt für Denkmalpflege und Archäologie | 2 | 5 |
| ada_archaeologie_v1 | Amt für Denkmalpflege und Archäologie | 1 | 5 |
| ada_denkmalschutz_pub_v1 | Amt für Denkmalpflege und Archäologie | 1 | 2 |
| ada_denkmalschutz_v1 | Amt für Denkmalpflege und Archäologie | 1 | 3 |
| afu_abbaustellen_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_altlasten_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_asiatische_hornisse_v1 | Amt für Umwelt | 1 | 1 |
| afu_bodendaten_nabodat_abfrage_pub_v1 | Amt für Umwelt | 1 | 2 |
| afu_bodendaten_nabodat_pub | Amt für Umwelt | 1 | 1 |
| afu_bodendaten_nabodat_v1 | Amt für Umwelt | 1 | 65 |
| afu_erdwaermesonden_private_quellen_v1 | Amt für Umwelt | 1 | 1 |
| afu_erdwaermesonden_v2 | Amt für Umwelt | 1 | 2 |
| afu_ewsabfrage_2d_staging_v1 | Amt für Umwelt | 1 | 5 |
| afu_ewsabfrage_2d_v1 | Amt für Umwelt | 1 | 3 |
| afu_geotope | Amt für Umwelt | 1 | 25 |
| afu_gewaesser_oekomorphologie_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_gewaesser_v1 | Amt für Umwelt | 1 | 1 |
| afu_gewaesserschutz_pub_v3 | Amt für Umwelt | 2 | 2 |
| afu_grundlagendaten_ews_v1 | Amt für Umwelt | 1 | 4 |
| afu_grundwassergeometrie_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_grundwasserschutz_obj_v1 | Amt für Umwelt | 1 | 13 |
| afu_igel | Amt für Umwelt | 1 | 2 |
| afu_naturereigniskataster_mgdm_v1 | Amt für Umwelt | 1 | 15 |
| afu_naturgefahren_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_naturgefahrenhinweiskarte_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_online_risk | Amt für Umwelt | 1 | 10 |
| afu_stehende_gewaesser_v1 | Amt für Umwelt | 2 | 1 |
| afu_wasserbewirtschaftung_pub_v2 | Amt für Umwelt | 1 | 2 |
| afu_wasserversorg_obj_v1 | Amt für Umwelt | 1 | 15 |
| agem_fila | agem_fila | 1 | 1 |
| agi_av_gb_abgleich_import | Amt für Geoinformation | 1 | 3 |
| agi_av_gb_admin_einteilung_pub | Amt für Geoinformation | 3 | 2 |
| agi_av_gb_administrative_einteilungen_v2 | Amt für Geoinformation | 4 | 4 |
| agi_av_gwr_abgleich_import_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_gwr_abgleich_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_kaso_abgleich_v1 | Amt für Geoinformation | 1 | 3 |
| agi_av_meldewesen_import_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_meldewesen_work_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_mocheckso | Amt für Geoinformation | 1 | 1 |
| agi_dm01avso24 | Amt für Geoinformation | 13 | 81 |
| agi_gb2av | Amt für Geoinformation | 1 | 3 |
| agi_gb2av_controlling | Amt für Geoinformation | 1 | 2 |
| agi_grundbuchplan_pub | Amt für Geoinformation | 1 | 2 |
| agi_gwr_pub_v1 | Amt für Geoinformation | 1 | 1 |
| agi_gwr_v1 | Amt für Geoinformation | 1 | 3 |
| agi_hoheitsgrenzen_pub | Amt für Geoinformation | 9 | 12 |
| agi_hoheitsgrenzen_v1 | Amt für Geoinformation | 2 | 6 |
| agi_mopublic_pub | Amt für Geoinformation | 7 | 7 |
| agi_plz_ortschaften | Amt für Geoinformation | 2 | 3 |
| agi_swissboundaries3d_pub | Amt für Geoinformation | 2 | 4 |
| agi_swissboundaries3d_v1 | Amt für Geoinformation | 1 | 4 |
| agi_swissboundaries3d_v2 | Amt für Geoinformation | 1 | 6 |
| agi_swisstopo_gebaeudeadressen_pub_v1 | Amt für Geoinformation | 1 | 1 |
| agi_swisstopo_gebaeudeadressen_v1 | Amt für Geoinformation | 1 | 3 |
| alw_fruchtfolgeflaechen_pub_v1 | Amt für Landwirtschaft | 2 | 1 |
| alw_landwirtschaft_tierhaltung_v1 | Amt für Landwirtschaft | 1 | 10 |
| alw_strukturverbesserungen | Amt für Landwirtschaft | 1 | 51 |
| alw_tiergesundheit_pflanzengesundheit_massnahmen_v1 | Amt für Landwirtschaft | 1 | 3 |
| amb_zivilschutz_adressen_staging_pub | amb_zivilschutz_adressen_staging_pub | 1 | 1 |
| arp_arbeitszonenbewirtschaftung_pub_v1 | Amt für Raumplanung | 1 | 1 |
| arp_arbeitszonenbewirtschaftung_staging_v1 | Amt für Raumplanung | 1 | 3 |
| arp_arbeitszonenbewirtschaftung_v1 | Amt für Raumplanung | 1 | 2 |
| arp_auswertung_nutzungsplanung_pub_v1 | Amt für Raumplanung | 2 | 6 |
| arp_bauzonengrenzen_pub | Amt für Raumplanung | 2 | 1 |
| arp_fledermaus_v1 | Amt für Raumplanung | 1 | 1 |
| arp_mehrjahresprogramm | Amt für Raumplanung | 1 | 1 |
| arp_mjpnl_gelan_v1 | Amt für Raumplanung | 1 | 1 |
| arp_mjpnl_v2 | Amt für Raumplanung | 2 | 12 |
| arp_naturreservate | Amt für Raumplanung | 1 | 1 |
| arp_naturreservate_pub | Amt für Raumplanung | 1 | 1 |
| arp_nutzungsplanung_pub_v1 | Amt für Raumplanung | 4 | 7 |
| arp_nutzungsvereinbarung | Amt für Raumplanung | 1 | 2 |
| arp_richtplan_pub_v2 | Amt für Raumplanung | 6 | 4 |
| arp_richtplan_v2 | Amt für Raumplanung | 1 | 1 |
| avt_bodenfaktor | Amt für Verkehr und Tiefbau | 1 | 3 |
| avt_oeffentlicher_verkehr_pub | Amt für Verkehr und Tiefbau | 1 | 1 |
| awjf | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_efj_geodaten_upload_v1 | Amt für Wald, Jagd und Fischerei | 1 | 2 |
| awjf_efj_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_forstreviere | Amt für Wald, Jagd und Fischerei | 2 | 3 |
| awjf_gesuchsteller | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_jagdreviere_jagdbanngebiete_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_programm_biodiversitaet_wald_v1 | Amt für Wald, Jagd und Fischerei | 1 | 6 |
| awjf_rodung_rodungsersatz_mgdm_v1 | Amt für Wald, Jagd und Fischerei | 1 | 6 |
| awjf_rodung_rodungsersatz_v1 | Amt für Wald, Jagd und Fischerei | 1 | 5 |
| awjf_schutzwald_pub_v1 | Amt für Wald, Jagd und Fischerei | 1 | 11 |
| awjf_schutzwald_v1 | Amt für Wald, Jagd und Fischerei | 1 | 4 |
| awjf_statische_waldgrenze | Amt für Wald, Jagd und Fischerei | 1 | 3 |
| awjf_statische_waldgrenze_mgdm_v1 | Amt für Wald, Jagd und Fischerei | 1 | 9 |
| awjf_waldpflege_erfassung | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_waldstandorte_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_wegsanierungen_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| bohrung | bohrung | 1 | 1 |
| capi_p | capi_p | 1 | 1 |
| dsbjd_ebauso_rahmenmodell_pub_v1 | dsbjd_ebauso_rahmenmodell_pub_v1 | 1 | 5 |
| dsbjd_ebauso_rahmenmodell_stage_v1 | dsbjd_ebauso_rahmenmodell_stage_v1 | 1 | 3 |
| live | live | 1 | 3 |
| public | public | 1 | 1 |
| simi | simi | 1 | 13 |

---

## Detailierte Job-Informationen

### ada_archaeologie_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/ada_archaeologie_pub`
**Schedule:** H H(1-3) * * 7 (So ~1-3h)

**Quell-Tabellen:**
- AS
- ada_archaeologie_v1.fachapplikation_regierungsratsbeschluss
- ada_archaeologie_v1.geo_ablage_gemeinde
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- ada_archaeologie_v1.fachapplikation_fundstelle
- ada_archaeologie_v1.geo_schutzbereich_innenstadt
- ada_archaeologie_v1.geo_flaeche
- rep_view_rrb
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.public_qualitaet_lokalisierung_typ
- j
- ada_archaeologie_pub_v1.restricted_punktfundstelle
- ada_archaeologie_pub_v1.restricted_flaechenfundstelle
- arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze
- public.rep_view_fundstellen

**Ziel-Tabellen:**
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- ada_archaeologie_v1.fachapplikation_fundstelle
- ada_archaeologie_v1.geo_flaeche
- ada_archaeologie_pub_v1.restricted_flaechenfundstelle
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.restricted_punktfundstelle

---

### afu_altlasten_import_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_altlasten_import_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### afu_asiatische_hornisse_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_asiatische_hornisse_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- afu_asiatische_hornisse_v1.asia_hornisse_ash

---

### afu_erdwaermesonden_private_quellen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_erdwaermesonden_private_quellen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- afu_erdwaermesonden_private_quellen_v1.private_quelle

---

### afu_erdwaermesonden_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_erdwaermesonden_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- afu_erdwaermesonden_v2.erdwaermesonden_bohrung
- afu_erdwaermesonden_v2.erdwaermesonden_anlage

---

### afu_ewsabfrage_2d

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_ewsabfrage_2d`
**Schedule:** 0 4 * * 0 (So 04:00)

**Quell-Tabellen:**
- afu_altlasten_pub_v2.belasteter_standort
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzareal
- afu_ewsabfrage_2d_v1.tiefenbeschraenkung
- afu_ewsabfrage_2d_staging_v1.abklaerung
- afu_grundlagendaten_ews_v1.vorkommnis
- afu_ewsabfrage_2d_staging_v1.hinweis
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone
- afu_grundlagendaten_ews_v1.standort
- afu_grundwassergeometrie_pub_v1.grundwasserstrom_begrenzung_hgw
- afu_ewsabfrage_2d_v1.abfrageperimeter
- agi_mopublic_pub.mopublic_grundstueck
- afu_grundlagendaten_ews_v1.bohrung
- afu_naturgefahrenhinweiskarte_pub_v1.rutschung_tief
- afu_ewsabfrage_2d_staging_v1.grundstueck
- afu_grundlagendaten_ews_v1.bohrprofil
- afu_ewsabfrage_2d_staging_v1.tiefenbeschraenkung
- afu_gewaesser_oekomorphologie_pub_v1.oekomorphologie
- afu_ewsabfrage_2d_v1.abklaerung
- afu_ewsabfrage_2d_staging_v1.abfrageperimeter

---

### afu_grundlagendaten_ews_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_grundlagendaten_ews_import`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- bohrung.

---

### afu_igel

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_igel`
**Schedule:** H H(3-4) * * 0 (So ~3-4h)

**Quell-Tabellen:**
- afu_igel.igel_standort
- LATERAL
- afu_igel.igel_stall

---

### afu_naturereigniskataster_mgdm_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_naturereigniskataster_mgdm_import`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_r
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_w
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_l
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_basisinformation
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_l
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_sammelereignis
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_w_um
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_ea
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_r
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_s
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_schaden
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_a
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_a
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_ea_e
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_s

---

### afu_neophyten_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_neophyten_pub`
**Schedule:** H 6 * * * (~6:xx)

**Quell-Tabellen:**
- neophyten

---

### afu_onlinerisk_transfer

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_onlinerisk_transfer`
**Schedule:** H H(18-19) * * 1-5 (~18-19h)

**Quell-Tabellen:**
- afu_online_risk.verordnungsrelevanz
- gebaeude
- untersuchungseinheit
- afu_online_risk.stoff
- afu_online_risk.stammdaten
- afu_online_risk.bereich
- afu_online_risk.untersuchungseinheit
- afu_online_risk.gebaeude
- afu_online_risk.verordnung
- afu_online_risk.konstruktion
- afu_online_risk.betrieb
- afu_online_risk.bereichstoff
- bereich

**Ziel-Tabellen:**
- with

---

### afu_stehende_gewaesser_abgleich

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_stehende_gewaesser_abgleich`
**Schedule:** H H(1-3) * * 7 (So ~1-3h)

**Quell-Tabellen:**
- afu_stehende_gewaesser_v1.stehendes_gewaesser
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_dm01avso24.bodenbedeckung_boflaeche

**Ziel-Tabellen:**
- afu_stehende_gewaesser_v1.stehendes_gewaesser

---

### afu_wasserbewirtschaftung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_wasserbewirtschaftung_pub`
**Schedule:** H H(1-3) * * 7 (So ~1-3h)

**Quell-Tabellen:**
- afu_wasserversorg_obj_v1.quellwasserbehaelter__dokument
- afu_wasserversorg_obj_v1.pumpwerk
- afu_wasserversorg_obj_v1.sammelbrunnstube
- afu_grundwasserschutz_obj_v1.baggerschlitz
- afu_grundwasserschutz_obj_v1.bohrung
- afu_grundwasserschutz_obj_v1.sodbrunnen
- afu_grundwasserschutz_obj_v1.einbaute
- afu_wasserbewirtschaftung_pub_v2.wassrbwschftung_quelle_zustand
- afu_wasserversorg_obj_v1.quelle_gefasst__dokument
- afu_wasserversorg_obj_v1.filterbrunnen__dokument
- afu_wasserversorg_obj_v1.sammelbrunnstube__dokument
- afu_wasserversorg_obj_v1.reservoir__dokument
- afu_grundwasserschutz_obj_v1.piezometer__dokument
- afu_wasserversorg_obj_v1.reservoir
- afu_grundwasserschutz_obj_v1.piezometer_gerammt
- afu_wasserversorg_obj_v1.dokument
- afu_wasserversorg_obj_v1.kontrollschacht__dokument
- afu_wasserversorg_obj_v1.filterbrunnen
- afu_grundwasserschutz_obj_v1.dokument
- afu_grundwasserschutz_obj_v1.baggerschlitz__dokument
- afu_wasserversorg_obj_v1.quellwasserbehaelter
- afu_grundwasserschutz_obj_v1.grundwasserwaermepumpe__dokument
- afu_grundwasserschutz_obj_v1.sodbrunnen__dokument
- afu_grundwasserschutz_obj_v1.grundwasserwaermepumpe
- afu_wasserversorg_obj_v1.quelle_gefasst
- afu_wasserversorg_obj_v1.kontrollschacht
- afu_grundwasserschutz_obj_v1.einbaute__dokument
- afu_grundwasserschutz_obj_v1.bohrung__dokument
- afu_wasserversorg_obj_v1.pumpwerk__dokument

**Ziel-Tabellen:**
- afu_wasserbewirtschaftung_pub_v2.wassrbwrtschftung_quelle

---

### agem_finanz_und_lastenausgleich

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agem_finanz_und_lastenausgleich`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agem_fila.strassen_strassenachse
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze

---

### agi_adressen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_adressen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.gebaeudeadressen_gebaeudeeingang
- agi_dm01avso24.gebaeudeadressen_hausnummerpos
- agi_dm01avso24.gebaeudeadressen_strassenstueck
- agi_dm01avso24.gebaeudeadressen_benanntesgebiet
- agi_dm01avso24.t_ili2db_import
- agi_dm01avso24.gebaeudeadressen_lokalisation
- agi_dm01avso24.gebaeudeadressen_lokalisationsname
- agi_dm01avso24.t_ili2db_basket

---

### agi_av_dm01_mopublic_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_dm01_mopublic_pub`
**Schedule:** 00 21 * * * (21:00)

**Quell-Tabellen:**
- agi_dm01avso24.fixpunktekatgrie3_hfp3nachfuehrung
- agi_dm01avso24.nomenklatur_ortsname
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchamt
- agi_dm01avso24.gemeindegrenzen_gemnachfuehrung
- agi_dm01avso24.bodenbedeckung_objektname
- agi_dm01avso24.nomenklatur_flurname
- mopublic_gemeindegrenze
- agi_dm01avso24.fixpunktekatgrie2_lfp2
- agi_dm01avso24.bodenbedeckung_projgebaeudenummer
- agi_dm01avso24.einzelobjekte_eonachfuehrung
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_grenzpunktsymbol
- agi_dm01avso24.bodenbedeckung_projobjektnamepos
- agi_dm01avso24.gebaeudeadressen_gebaeudeeingang
- agi_dm01avso24.einzelobjekte_objektnamepos
- agi_dm01avso24.gebaeudeadressen_gebnachfuehrung
- agi_dm01avso24.nomenklatur_flurnamepos
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_dm01avso24.fixpunktekatgrie1_lfp1
- agi_dm01avso24.fixpunktekatgrie1_hfp1pos
- agi_dm01avso24.gemeindegrenzen_gemeinde
- t_ili2db_basket
- agi_dm01avso24.rohrleitungen_rlnachfuehrung
- agi_dm01avso24.einzelobjekte_linienelement
- agi_dm01avso24.einzelobjekte_punktelement
- agi_dm01avso24.einzelobjekte_einzelobjekt
- agi_dm01avso24.fixpunktekatgrie1_lfp1nachfuehrung
- agi_dm01avso24.fixpunktekatgrie2_hfp2
- agi_dm01avso24.nomenklatur_gelaendenamepos
- agi_dm01avso24.fixpunktekatgrie3_lfp3nachfuehrung
- agi_dm01avso24.t_ili2db_import
- agi_dm01avso24.t_ili2db_basket
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_dm01avso24.bodenbedeckung_bbnachfuehrung
- agi_dm01avso24.liegenschaften_grundstueckpos
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_dm01avso24.fixpunktekatgrie1_hfp1nachfuehrung
- agi_dm01avso24.rohrleitungen_linienelement
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_dm01avso24.rohrleitungen_leitungsobjekt
- agi_dm01avso24.liegenschaften_projgrundstueckpos
- agi_dm01avso24.nomenklatur_ortsnamepos
- agi_plz_ortschaften.plzortschaft_ortschaftsname
- agi_dm01avso24.gebaeudeadressen_hausnummerpos
- agi_dm01avso24.fixpunktekatgrie1_hfp1
- agi_dm01avso24.fixpunktekatgrie3_hfp3pos
- agi_dm01avso24.fixpunktekatgrie2_lfp2nachfuehrung
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunktsymbol
- agi_dm01avso24.bodenbedeckung_gebaeudenummer
- agi_dm01avso24.nomenklatur_nknachfuehrung
- agi_dm01avso24.einzelobjekte_objektnummer
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.bodenbedeckung_projboflaeche
- agi_dm01avso24.fixpunktekatgrie2_hfp2pos
- agi_dm01avso24.fixpunktekatgrie3_hfp3
- agi_dm01avso24.liegenschaften_grenzpunktpos
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.gebaeudeadressen_strassenstueck
- agi_plz_ortschaften.plzortschaft_ortschaft
- agi_plz_ortschaften.plzortschaft_plz6
- agi_dm01avso24.fixpunktekatgrie2_hfp2nachfuehrung
- agi_dm01avso24.fixpunktekatgrie3_lfp3pos
- agi_dm01avso24.gebaeudeadressen_lokalisation
- agi_dm01avso24.gebaeudeadressen_lokalisationsname
- t_ili2db_dataset
- agi_dm01avso24.einzelobjekte_flaechenelement
- agi_dm01avso24.gebaeudeadressen_gebaeudename
- agi_dm01avso24.nomenklatur_gelaendename
- agi_dm01avso24.nummerierngsbrche_nbgeometrie
- agi_dm01avso24.gemeindegrenzen_projgemeindegrenze
- agi_dm01avso24.einzelobjekte_objektname
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_dm01avso24.liegenschaften_grenzpunkt
- agi_dm01avso24.fixpunktekatgrie3_lfp3
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunktpos
- agi_dm01avso24.nummerierngsbrche_nummerierungsbereich
- agi_dm01avso24.fixpunktekatgrie2_lfp2pos
- agi_dm01avso24.fixpunktekatgrie1_lfp1pos
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunkt
- agi_dm01avso24.gebaeudeadressen_lokalisationsnamepos
- agi_dm01avso24.bodenbedeckung_objektnamepos
- agi_dm01avso24.bodenbedeckung_projobjektname
- agi_dm01avso24.bodenbedeckung_boflaeche

**Ziel-Tabellen:**
- mopublic_grundstueck
- mopublic_gemeindegrenze
- mopublic_hoheitsgrenzpunkt
- t_ili2db_dataset
- mopublic_objektname_pos
- mopublic_gemeindegrenze_proj
- mopublic_gebaeudeadresse
- mopublic_bodenbedeckung
- mopublic_einzelobjekt_linie
- mopublic_fixpunkt
- mopublic_grenzpunkt
- mopublic_ortsname
- mopublic_rohrleitung
- mopublic_grundstueck_linie
- mopublic_strassenname_pos
- mopublic_einzelobjekt_punkt
- mopublic_grundstueck_proj
- mopublic_einzelobjekt_flaeche
- t_ili2db_basket
- mopublic_gelaendename
- mopublic_strassenachse
- mopublic_bodenbedeckung_proj
- mopublic_flurname
- mopublic_grundstueck_proj_linie

---

### agi_av_export_ai

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_export_ai`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_av_gb_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_gb_abgleich_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_av_gb_abgleich_import.gb_daten
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_av_gb_abgleich_import.differenzen_staging
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.t_ili2db_import
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.liegenschaften_grundstuecksart
- agi_dm01avso24.t_ili2db_basket
- capi_p.V_AIO_GrundstueckeMitFlaeche

**Ziel-Tabellen:**
- agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging
- agi_av_gb_abgleich_import.differenzen_staging

---

### agi_av_gwr_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_gwr_abgleich_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen
- agi_av_gwr_abgleich_import_v1.av_gwr_differnzen_av_gwr_differenzen

**Ziel-Tabellen:**
- agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen

---

### agi_av_kaso_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_kaso_abgleich_pub`
**Schedule:** H 3 * * * (~3:xx)

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging
- sogis_av_kaso_abgleich
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_av_kaso_abgleich_v1.differenzen_staging
- agi_av_kaso_abgleich_v1.kaso_daten
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.t_ili2db_import
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.liegenschaften_grundstuecksart
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_dm01avso24.t_ili2db_basket

**Ziel-Tabellen:**
- agi_av_kaso_abgleich_v1.differenzen_staging
- agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging

---

### agi_av_meldewesen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_meldewesen`
**Schedule:** H H(3-4) * * * (~3-4h)

**Quell-Tabellen:**
- agi_av_meldewesen_import_v1.meldungen_meldung
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_bergwerk
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_av_meldewesen_work_v1.meldungen_meldung
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze

**Ziel-Tabellen:**
- agi_av_meldewesen_work_v1.meldungen_meldung

---

### agi_av_mocheckso

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_mocheckso`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_av_mocheckso.mocheckso_errors_mocheckso_error

---

### agi_ch_gemeinden

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_ch_gemeinden`
**Schedule:** H H(1-3) 1 2 * (1. ~1-3h)

**Quell-Tabellen:**
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_kantonsgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_kantonsgebiet
- agi_swissboundaries3d_v2.surface3d
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_bezirksgebiet
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_hoheitsgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_hoheitsgebiet
- agi_swissboundaries3d_pub.swissboundaries3d_hoheitsgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_landesgebiet
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_landesgebiet
- agi_swissboundaries3d_pub.swissboundaries3d_kanton
- agi_swissboundaries3d_pub.swissboundaries3d_land
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_bezirksgebiet
- agi_swissboundaries3d_pub.swissboundaries3d_bezirk
- agi_swissboundaries3d_v2.multisurface3d

---

### agi_dmav_fixpunkte2_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_fixpunkte2_import`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_dmav_fixpunktelv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_fixpunktelv_import`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_dmav_hoheitsgrenzen_lv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_hoheitsgrenzen_lv_import`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_dmav_hoheitsgrenzpunkte_lv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_hoheitsgrenzpunkte_lv_import`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_dmav_plz_ortschaft_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_plz_ortschaft_import`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### agi_gb2av_controlling

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_gb2av_controlling`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_gb2av.vollzugsgegnstnde_vollzugsgegenstand
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta
- agi_av_gb_administrative_einteilungen_v2.nachfuehrngskrise_gemeinde
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_dm01avso24.liegenschaften_projbergwerk
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- mit
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_av_gb_administrative_einteilungen_v2.nachfuehrngskrise_standort
- agi_gb2av_controlling.controlling_av2gb_mutationen
- agi_gb2av.mutationsnummer
- agi_gb2av.mutationstabelle_avmutation

**Ziel-Tabellen:**
- SET
- agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta
- agi_gb2av_controlling.controlling_av2gb_mutationen

---

### agi_generate_matomo_reports

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_generate_matomo_reports`
**Schedule:** H 4 1 * * (1. ~4:xx)

---

### agi_gwr_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_gwr_pub`
**Schedule:** H H(3-4) * * * (~3-4h)

**Quell-Tabellen:**
- agi_gwr_v1.gwr_gebaeude
- agi_gwr_v1.gwr_codes
- agi_gwr_v1.gwr_wohnung
- dwelling
- building
- codes

---

### agi_hoheitsgrenzen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_hoheitsgrenzen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksname_a3
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_kantonsname_pos
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindename_a3
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsname_a4
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindename_a4
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeinde
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeindename_pos
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze_generalisiert
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirksname_pos
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsname_a3
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksname_a4
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_kanton

**Ziel-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze_generalisiert

---

### agi_kartenkatalog_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_kartenkatalog_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- simi.simidata_postgres_table
- simi.simitheme_theme_publication
- simi.simiproduct_properties_in_list
- simi.simiiam_role
- simi.simiproduct_data_product_pub_scope
- simi.simiproduct_data_product
- simi.simidata_data_set_view
- simi.simiproduct_single_actor
- simi.simidata_table_view
- simi.simitheme_org_unit
- simi.simitheme_theme
- simi.simiproduct_layer_group
- simi.simiiam_permission

---

### agi_stac

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_stac`
**Schedule:** H H(5-6) * * * (~5-6h)

---

### agi_swisstopo_gebaeudeadressen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_swisstopo_gebaeudeadressen`
**Schedule:** H H(1-3) 2 * * (2. ~1-3h)

**Quell-Tabellen:**
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_address
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_stn
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_zip

---

### alw_landwirtschaft_tierhaltung_import_bodenbedeckung

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_import_bodenbedeckung`
**Schedule:** H H(3-4) * * 5 (Fr ~3-4h)

---

### alw_landwirtschaft_tierhaltung_import_massnahmen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_import_massnahmen`
**Schedule:** H H(3-4) 1 * * (1. ~3-4h)

---

### alw_landwirtschaft_tierhaltung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_pub`
**Schedule:** H H(2-4) * * * (~2-4h)

**Quell-Tabellen:**
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_standorte
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_summe_tiere_flaechen
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_kultur_flaechen
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_betrieb
- alw_landwirtschaft_tierhaltung_v1.bff_qualitaet_bff_qualitaet
- alw_landwirtschaft_tierhaltung_v1.t_ili2db_dataset
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_bewirtschaftungseinheit
- alw_landwirtschaft_tierhaltung_v1.t_ili2db_basket
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_kultur_punktelemente
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_gelan_person

---

### alw_strukturverbesserungen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_strukturverbesserungen_pub`
**Schedule:** H H(1-3) * * 6 (Sa ~1-3h)

**Quell-Tabellen:**
- alw_strukturverbesserungen.elektrizitaet_linien
- alw_strukturverbesserungen.oekologie_punkte
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet_projekt
- alw_strukturverbesserungen.astatus
- alw_strukturverbesserungen.wege
- alw_strukturverbesserungen.raeumlichelmnte_wege_bruecke_lehnenviadukt_material
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_trockenmauer
- alw_strukturverbesserungen.bewaesserung_linien
- alw_strukturverbesserungen.stand_gutrrglrung_stand_gueterregulierung
- alw_strukturverbesserungen.raeumlicheelemnte_wegebau_linie
- alw_strukturverbesserungen.stand
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_linie
- alw_strukturverbesserungen.beizugsgebiete
- alw_strukturverbesserungen.oekologie_linien
- alw_strukturverbesserungen.raeumlicheelemnte_bew_flaechen_bewaesserung
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_pumpwerk
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft_dokument
- alw_strukturverbesserungen.entw_bodenstruktur_linien
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft_element
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_linie
- alw_strukturverbesserungen.oekologische_flaechen
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_flaeche
- alw_strukturverbesserungen.raeumlicheelemnte_wiederherstellung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_wasserversorgung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_flaeche
- alw_strukturverbesserungen.bewaesserung_flaechen
- alw_strukturverbesserungen.genossenschaften
- alw_strukturverbesserungen.projekt
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft
- alw_strukturverbesserungen.wiederherstellung_punkte
- alw_strukturverbesserungen.raeumlicheelemnte_gemeinde_flurreglement_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_projekt
- alw_strukturverbesserungen.bewaesserung_punkte
- alw_strukturverbesserungen.raeumlicheelemnte_ev_punkt
- alw_strukturverbesserungen.wasserversorgung_punkte
- alw_strukturverbesserungen.raeumlicheelemnte_ev_linie
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet
- alw_strukturverbesserungen.raeumlicheelemnte_raeumliches_element_dokument
- alw_strukturverbesserungen.bautyp
- alw_strukturverbesserungen.oekologie_trockenmauern
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_punkt
- alw_strukturverbesserungen.elektrizitaet_punkte
- alw_strukturverbesserungen.raeumlicheelemnte_wege_bruecke_lehnenviadukt
- alw_strukturverbesserungen.entw_bodenstruktur_flaechen
- alw_strukturverbesserungen.raeumlicheelemnte_gemeinde_flurreglement
- alw_strukturverbesserungen.raeumlicheelemnte_wv_leitung_wasserversorgung
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_linie
- alw_strukturverbesserungen.raeumlicheelemnte_werkeigentum
- alw_strukturverbesserungen.funktionstyp

---

### alw_tiergesundheit_pflanzengesundheit_massnahmen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_tiergesundheit_pflanzengesundheit_massnahmen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_pflanzengesundheit_schadorganismen
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_bienensperrgebiet
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_tiergesundheit_massnahmengebiet

---

### amb_zivilschutz_adressen_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/amb_zivilschutz_adressen_export`
**Schedule:** H H(1-3) 1 * * (1. ~1-3h)

**Quell-Tabellen:**
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_gebaeudeadresse
- agi_mopublic_pub.mopublic_objektname_pos
- amb_zivilschutz_adressen_staging_pub.adressen_zivilschutz
- agi_mopublic_pub.mopublic_grundstueck
- agi_mopublic_pub.mopublic_gemeindegrenze
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_mopublic_pub.mopublic_einzelobjekt_flaeche
- agi_swisstopo_gebaeudeadressen_pub_v1.gebaeudeadressen_adresse

**Ziel-Tabellen:**
- amb_zivilschutz_adressen_staging_pub.adressen_zivilschutz

---

### arp_arbeitszonenbewirtschaftung_inventar_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_arbeitszonenbewirtschaftung_inventar_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_arbeitszonenbewirtschaftung_v1.regionen_region
- arp_arbeitszonenbewirtschaftung_staging_v1.inventar_flaeche_v
- arp_arbeitszonenbewirtschaftung_pub_v1.region_region
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_arbeitszonenbewirtschaftung_staging_v1.arbtszng_nvntar_arbeitszonenbewirtschaftung_inventar_bebtand
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- agi_mopublic_pub.mopublic_grundstueck

**Ziel-Tabellen:**
- arp_arbeitszonenbewirtschaftung_staging_v1.arbtsznnng_nvntar_arbeitszonenbewirtschaftung_inventar
- arp_arbeitszonenbewirtschaftung_v1.bewertung_bewertung

---

### arp_auswertung_nutzungsplanung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_auswertung_nutzungsplanung_pub`
**Schedule:** H H(1-3) 31 1,3,4,7,8,10,12 *\nH H(1-3) 30 4,6,9,11 *\nH H(1-3) 28,29 2 * (~1-3h)

**Quell-Tabellen:**
- agi_mopublic_pub.mopublic_bodenbedeckung
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_und_lsgrenzen
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_gines
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_ohne_lsgrenzen
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_pro_gemeinde
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- agi_mopublic_pub.mopublic_grundstueck
- original
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_mopublic_pub.mopublic_einzelobjekt_flaeche
- arp_auswertung_nutzungsplanung_pub_v1.auswrtngtzngsznen_grundnutzungszone_aggregiert_pro_gemeinde

---

### arp_bauzonengrenzen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_bauzonengrenzen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung

**Ziel-Tabellen:**
- arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze

---

### arp_fledermaus

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_fledermaus`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- arp_fledermaus_v1.fledermausfundrte_fledermausfundort

---

### arp_mjpnatur_gelan_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnatur_gelan_export`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- arp_mjpnl_v2.mjpnl_beurteilung_hostet
- arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen
- arp_mjpnl_v2.mjpnl_vereinbarung

**Ziel-Tabellen:**
- arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen

---

### arp_mjpnatur_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnatur_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- arp_mjpnl_v2.mjpnl_beurteilung_obl
- arp_mjpnl_v2.mjpnl_beurteilung_wiese
- arp_mjpnl_v2.mjpnl_beurteilung_hostet
- arp_mjpnl_v2.mjpnl_beurteilung_wbl_weide
- arp_mjpnl_v2.mjpnl_beurteilung_alr_saum
- arp_mjpnl_v2.mjpnl_beurteilung_wbl_wiese
- arp_mjpnl_v2.mjpnl_beurteilung_alr_buntbrache
- arp_mjpnl_v2.mjpnl_beurteilung_hecke
- arp_mjpnl_v2.mjpnl_beurteilung_weide_soeg
- arp_mjpnl_v2.mjpnl_vereinbarung
- arp_mjpnl_v2.mjpnl_beurteilung_weide_ln
- arp_mjpnl_v2.betrbsdttrktrdten_gelan_person

---

### arp_mjpnl_v2_auszahlung

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnl_v2_auszahlung`
**Schedule:** H H(1-3) 15 1 * (15. ~1-3h)

---

### arp_mjpnl_v2_gelan_update

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnl_v2_gelan_update`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### arp_mjpnl_v2_zahlungslauf

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnl_v2_zahlungslauf`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeinde
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk

**Ziel-Tabellen:**
- abrechnung_per_leistung
- der

---

### arp_nutzungsplanung_planregister_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_nutzungsplanung_planregister_export`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### arp_nutzungsvereinbarung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_nutzungsvereinbarung_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_liegenschaft
- arp_nutzungsvereinbarung.nutzungsvrnbrngen_projekte
- agi_dm01avso24.gemeindegrenzen_gemeinde
- arp_mehrjahresprogramm.mehrjahresprgramm_person
- arp_nutzungsvereinbarung.nutzungsvrnbrngen_nutzungsvereinbarungen
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.nomenklatur_flurname

---

### arp_richtplan_grundnutzung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_richtplan_grundnutzung_pub`
**Schedule:** H H(1-3) 1 * * (1. ~1-3h)

**Quell-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_grundnutzung
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_grundnutzung

---

### avt_bodenfaktor_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/avt_bodenfaktor_pub`
**Schedule:** H H(2-5) * * 0 (So ~2-5h)

**Quell-Tabellen:**
- avt_bodenfaktor.t_ili2db_dataset
- avt_bodenfaktor.t_ili2db_basket
- avt_bodenfaktor.bodenfaktor
- agi_dm01avso24.bodenbedeckung_boflaeche

**Ziel-Tabellen:**
- avt_bodenfaktor.bodenfaktor

---

### awjf_efj

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_efj`
**Schedule:** H H(4-5) * * * (~4-5h)

**Quell-Tabellen:**
- LATERAL
- awjf_efj_v1.efj_abgaenge

---

### awjf_forstreviere_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_forstreviere_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_forstreviere.forstreviere_forstkreis

---

### awjf_programm_biodiversitaet_wald_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_programm_biodiversitaet_wald_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- string_agg
- agi_dm01avso24.nomenklatur_flurname
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_zielgruppe
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_baumartenvielfalt
- agi_swissboundaries3d_pub.swissboundaries3d_hoheitsgebiet
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_waldbiodiversitaetsflaeche
- awjf_forstreviere.forstreviere_forstrevier
- awjf.wap_bst
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_foto
- awjf_forstreviere.forstreviere_forstkreis
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotop_zielgruppe
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotopbaum
- awjf_waldstandorte_v1.waldstandort

---

### awjf_rodung_rodungsersatz_mgdm

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_rodung_rodungsersatz_mgdm`
**Schedule:** H H(1-3) 1 3 * (1. ~1-3h)

**Quell-Tabellen:**
- awjf_rodung_rodungsersatz_mgdm_v1.objekt
- awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_
- awjf_rodung_rodungsersatz_v1.dokument
- awjf_rodung_rodungsersatz_v1.rodung_dokument
- awjf_rodung_rodungsersatz_v1.rodungsdaten
- awjf_rodung_rodungsersatz_mgdm_v1.rodungsbewilligung
- awjf_rodung_rodungsersatz_v1.ausgleichsabgabe
- awjf_rodung_rodungsersatz_mgdm_v1.uri_
- awjf_rodung_rodungsersatz_v1.flaeche
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzmassnahmennl_

**Ziel-Tabellen:**
- awjf_rodung_rodungsersatz_mgdm_v1.objekt
- awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_
- awjf_rodung_rodungsersatz_mgdm_v1.rodungsbewilligung
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzmassnahmennl_

---

### awjf_schutzwald_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_schutzwald_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- awjf_schutzwald_v1.schutzwald_info
- awjf_schutzwald_pub_v1.behandelte_flaeche_status
- awjf_schutzwald_pub_v1.nais_code
- awjf_schutzwald_pub_v1.schutzwald_hauptgefahrenpotential
- awjf_schutzwald_pub_v1.schutzwald_objektkategorie
- awjf_schutzwald_v1.behandelte_flaeche
- awjf_schutzwald_v1.dokument
- awjf_schutzwald_pub_v1.schutzwald_intensitaet_geschaetzt
- awjf_schutzwald_pub_v1.schutzwald_info_zieltyp
- awjf_schutzwald_v1.schutzwald
- awjf_schutzwald_pub_v1.behandelte_flaeche_massnahme

**Ziel-Tabellen:**
- awjf_schutzwald_pub_v1.behandelte_flaeche
- awjf_schutzwald_pub_v1.schutzwald
- awjf_schutzwald_pub_v1.dokument
- awjf_schutzwald_pub_v1.schutzwald_info

---

### awjf_waldpflege_kontrolle

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_waldpflege_kontrolle`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- awjf_gesuchsteller.gesuchsteller_gesuchsteller
- awjf_waldpflege_erfassung.waldpflege_waldpflege

---

### awjf_waldportal

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_waldportal`
**Schedule:** H H(1-3) * * * (~1-3h)

---

### awjf_wegsanierungen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_wegsanierungen_pub`
**Schedule:** H H(1-3) * * * (~1-3h)

**Quell-Tabellen:**
- awjf_wegsanierungen_v1.wegsanierungen_wegsanierung

---

### dsbjd_ebauso_rahmenmodell_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/dsbjd_ebauso_rahmenmodell_pub`
**Schedule:** H H(3-4) * * * (~3-4h)

**Quell-Tabellen:**
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_gebaeudeadresse
- alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_linie
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_grundstueck
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_punkt
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- agi_mopublic_pub.mopublic_grundstueck
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- live.oerbkrmfr_v2_0transferstruktur_eigentumsbeschraenkung
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_punkt
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- ada_denkmalschutz_pub_v1.denkmal_punkt
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_gebaeudeeingang
- afu_naturgefahren_pub_v2.synoptisches_gefahrengebiet
- ada_denkmalschutz_pub_v1.denkmal_polygon
- live.oerbkrmfr_v2_0transferstruktur_legendeeintrag
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_polygon
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_linie
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_polygon
- live.oerbkrmfr_v2_0transferstruktur_geometrie
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_punkt
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet

**Ziel-Tabellen:**
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_punkt
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_punkt
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_gebaeudeeingang
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_polygon
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_grundstueck
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_polygon

---

### ada_denkmalschutz_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/ada_denkmalschutz_pub`
**Upstream:** oerebv2_einzelschutz_denkmal

**Quell-Tabellen:**
- ada_denkmalschutz_v1.fachapplikation_denkmal
- ada_denkmalschutz_v1.oereb_doclink_v
- ada_denkmalschutz_v1.gis_geometrie

---

### afu_bodendaten_nabodat_abfrage_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/afu_bodendaten_nabodat_abfrage_pub`
**Upstream:** afu_bodenprofilstandorte_nabodat_pub

**Quell-Tabellen:**
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf
- afu_bodendaten_nabodat_v1.punktdaten_projektstandort
- afu_bodendaten_nabodat_v1.codelistnnlysdten_analyseparameter
- afu_bodendaten_nabodat_v1.punktdaten_standortbeurteilung
- afu_bodendaten_nabodat_pub.bodenproflstndrte_bodenprofilstandort
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft_ref
- afu_bodendaten_nabodat_v1.punktdaten_bodenskelettfeldbereich
- afu_bodendaten_nabodat_v1.codelistnprfldten_feinerdekoernung
- afu_bodendaten_nabodat_v1.codlstnpktstndort_exposition
- afu_bodendaten_nabodat_v1.punktdaten_messung
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodentyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_erhebungsart
- afu_bodendaten_nabodat_v1.punktdaten_projekt
- afu_bodendaten_nabodat_v1.punktdaten_profildokument
- afu_bodendaten_nabodat_v1.punktdaten_dokument
- afu_bodendaten_nabodat_v1.codlstnpktstndort_klimaeignungszone
- afu_bodendaten_nabodat_v1.punktdaten_untertyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_kleinrelief
- afu_bodendaten_nabodat_v1.punktdaten_standorteigenschaften
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_krumenzustand
- afu_bodendaten_nabodat_v1.codelistnprfldten_skelettgehalt
- afu_bodendaten_nabodat_v1.codlstnpktstndort_vegetation
- afu_bodendaten_nabodat_v1.punktdaten_wald
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodenwasserhaushaltsgruppe
- afu_bodendaten_nabodat_v1.punktdaten_ausgangsmaterial
- afu_bodendaten_nabodat_v1.codlstnpktstndort_eiszeit
- afu_bodendaten_nabodat_v1.punktdaten_horizontbezeichnung
- mit
- afu_bodendaten_nabodat_abfrage_pub_v1.bodenprofil
- afu_bodendaten_nabodat_v1.codelistnprfldten_intensitaet
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung_ref
- afu_bodendaten_nabodat_v1.codelistnprfldten_eignungsklasse
- afu_bodendaten_nabodat_v1.punktdaten_bodenfarbe
- afu_bodendaten_nabodat_v1.erhebung_probe_profil_v
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung
- afu_bodendaten_nabodat_v1.codelistnprfldten_kalkreaktionhcl
- afu_bodendaten_nabodat_v1.punktdaten_profilbeurteilung
- afu_bodendaten_nabodat_v1.codlstnpktstndort_risikoduengerfluess
- afu_bodendaten_nabodat_v1.codelistnprfldten_helligkeit
- afu_bodendaten_nabodat_v1.codelistnprfldten_nutzungseignung
- afu_bodendaten_nabodat_v1.punktdaten_horizont
- afu_bodendaten_nabodat_v1.punktdaten_probe
- afu_bodendaten_nabodat_v1.codelistnprfldten_pflanzennutzbaregruendigkeit
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest
- afu_bodendaten_nabodat_v1.codelistnprfldten_klassifikationssystem
- afu_bodendaten_nabodat_v1.codlstnpktstndort_produktionsfaehigkstufewald
- afu_bodendaten_nabodat_v1.punktdaten_gefuege
- afu_bodendaten_nabodat_v1.codlstnpktstndort_humusform
- afu_bodendaten_nabodat_v1.codlstnpktstndort_dokumenttyp
- afu_bodendaten_nabodat_v1.codelistnprfldten_wasserspeichervermoegen
- afu_bodendaten_nabodat_v1.punktdaten_koernungsbereich
- afu_bodendaten_nabodat_v1.punktdaten_profil
- afu_bodendaten_nabodat_v1.punktdaten_standort
- afu_bodendaten_nabodat_v1.punktdaten_bichqualitaet
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_ausgangsmaterial
- afu_bodendaten_nabodat_v1.codelistnprfldten_fruchtbarkeitsstufe
- afu_bodendaten_nabodat_v1.codelistnprfldten_form
- afu_bodendaten_nabodat_v1.punktdaten_erhebung
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft
- afu_bodendaten_nabodat_v1.codlstnpktstndort_gelaendeform
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtonzahl
- afu_bodendaten_nabodat_v1.codlstnpktstndort_einsatzduengerfest
- afu_bodendaten_nabodat_v1.codelistnprfldten_groesse
- afu_bodendaten_nabodat_v1.codelistnprfldten_untertyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_landschaftselement
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtontext

**Ziel-Tabellen:**
- afu_bodendaten_nabodat_abfrage_pub_v1.horizont
- afu_bodendaten_nabodat_abfrage_pub_v1.bodenprofil

---

### afu_geotope_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/afu_geotope_pub`
**Upstream:** oereb_einzelschutz_geotop

**Quell-Tabellen:**
- afu_geotope.geotope_fundstelle_grabung_dokument
- afu_geotope.geotope_erratiker_fachbereich
- afu_geotope.geotope_fundstelle_grabung
- afu_geotope.lithostratigrphie_geologische_stufe
- afu_geotope.geotope_aufschluss_fachbereich
- afu_geotope.geotope_hoehle_dokument
- arp_naturreservate.reservate_teilgebiet
- afu_geotope.geotope_quelle_dokument
- afu_geotope.geotope_landform_fachbereich
- afu_geotope.geotope_aufschluss_dokument
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- afu_geotope.geotope_fachbereich
- afu_geotope.geotope_quelle_fachbereich
- afu_geotope.geotope_fundstelle_grabung_fachbereich
- afu_geotope.geotope_quelle
- afu_geotope.geotope_zustaendige_stelle
- afu_geotope.lithostratigrphie_geologisches_system
- afu_geotope.geotope_hoehle_fachbereich
- arp_richtplan_v2.richtplankarte_ueberlagernde_flaeche
- afu_geotope.lithostratigrphie_geologische_serie
- afu_geotope.geotope_landform_dokument
- afu_geotope.geotope_landschaftsform
- afu_geotope.geotope_dokument
- afu_geotope.geotope_hoehle
- agi_plz_ortschaften.plzortschaft_ortschaftsname
- afu_geotope.geotope_erratiker
- afu_geotope.geotope_aufschluss
- agi_plz_ortschaften.plzortschaft_ortschaft
- afu_geotope.geotope_erratiker_dokument
- afu_geotope.lithostratigrphie_geologische_schicht

---

### afu_stehende_gewaesser_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/afu_stehende_gewaesser_pub`
**Upstream:** afu_stehende_gewaesser_abgleich

**Quell-Tabellen:**
- afu_stehende_gewaesser_v1.stehendes_gewaesser
- agi_dm01avso24.bodenbedeckung_boflaeche

---

### agi_gebaeudeinformationen_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/agi_gebaeudeinformationen_pub`
**Upstream:** agi_av_dm01_mopublic_pub

**Quell-Tabellen:**
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_gebaeudeadresse
- agi_mopublic_pub.mopublic_objektname_pos
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_gwr_pub_v1.gwr_gebaeude

---

### agi_grundbuchplan_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/agi_grundbuchplan_pub`
**Upstream:** agi_av_dm01_mopublic_pub

**Quell-Tabellen:**
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_grundbuchplan_pub.grundbuchplan_liegenschaft
- agi_av_gb_admin_einteilung_pub.nachfuehrngskrise_gemeinde
- agi_grundbuchplan_pub.grundbuchplan_grundstueckpos
- agi_dm01avso24.liegenschaften_grenzpunkt
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_dm01avso24.bodenbedeckung_boflaechesymbol
- agi_mopublic_pub.mopublic_gemeindegrenze
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.bodenbedeckung_boflaeche
- agi_dm01avso24.liegenschaften_grundstueckpos

**Ziel-Tabellen:**
- agi_grundbuchplan_pub.grundbuchplan_grundstueckpos

---

### arp_richtplan_abbaustellen_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_abbaustellen_pub`
**Upstream:** afu_abbaustellen_pub

**Quell-Tabellen:**
- afu_abbaustellen_pub_v2.abbaustelle
- arp_richtplan_pub_v2.detailkarten_flaeche

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.detailkarten_flaeche

---

### arp_richtplan_fruchtfolgeflaechen_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_fruchtfolgeflaechen_pub`
**Upstream:** alw_fruchtfolgeflaechen_pub

**Quell-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

---

### arp_richtplan_gewaesserschutz_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_gewaesserschutz_pub`
**Upstream:** afu_gewaesserschutz_zonen_areale_pub

**Quell-Tabellen:**
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzareal
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

---

### arp_richtplan_naturreservate_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_naturreservate_pub`
**Upstream:** arp_naturreservate_pub

**Quell-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- arp_naturreservate_pub.naturreservate_reservat

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

---

### arp_richtplan_oeffentlicher_verkehr_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_oeffentlicher_verkehr_pub`
**Upstream:** avt_oeffentlicher_verkehr_pub

**Quell-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie
- avt_oeffentlicher_verkehr_pub.oeffntlchr_vrkehr_netz

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie

---

### arp_sein_strukturdaten_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_sein_strukturdaten_pub`
**Upstream:** arp_auswertung_nutzungsplanung_pub

---

### awjf_efj_geodaten_upload

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/awjf_efj_geodaten_upload`
**Upstream:** awjf_jagdreviere_jagdbanngebiete_pub, awjf_gewaesser_fischerei_pub

**Quell-Tabellen:**
- awjf_jagdreviere_jagdbanngebiete_v1.jagdreviere_jagdreviere
- awjf_efj_geodaten_upload_v1.gebiete_gebiet
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- afu_gewaesser_v1.fischrevierabschnitt_v

**Ziel-Tabellen:**
- awjf_efj_geodaten_upload_v1.transfermetadaten_datenbestand
- awjf_efj_geodaten_upload_v1.gebiete_gebiet

---

### awjf_statische_waldgrenzen_export_ai

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/awjf_statische_waldgrenzen_export_ai`
**Upstream:** awjf_statische_waldgrenze_pub

**Quell-Tabellen:**
- awjf_statische_waldgrenze.geobasisdaten_typ
- awjf_statische_waldgrenze_mgdm_v1.multilingualuri
- awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument
- awjf_statische_waldgrenze_mgdm_v1.t_ili2db_basket
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_geometrie_dokument
- awjf_statische_waldgrenze_mgdm_v1.localiseduri
- awjf_statische_waldgrenze.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.rechtsstatus
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ_dokument
- awjf_statische_waldgrenze.dokumente_dokument

**Ziel-Tabellen:**
- awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.localiseduri
- awjf_statische_waldgrenze_mgdm_v1.multilingualuri

---
