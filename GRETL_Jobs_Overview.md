# GRETL Jobs Übersicht

**Automatisch generiert am:** 22.12.2025 04:40
**Anzahl Jobs:** 211

## Inhaltsverzeichnis

- [Zeitgesteuerte Jobs (Cron)](#zeitgesteuerte-jobs-cron)
- [Upstream-gesteuerte Jobs](#upstream-gesteuerte-jobs)
- [Manuelle Jobs](#manuelle-jobs)
- [Schema-Übersicht](#schema-übersicht)

---

## Zeitgesteuerte Jobs (Cron)

**Anzahl:** 68

| Job | Status | Cron Schedule | Beschreibung |
|-----|--------|---------------|--------------|
| agi_av_kaso_abgleich_pub | Aktiv | `H 3 * * *` | ~3:xx |
| afu_ewsabfrage_2d | Aktiv | `0 4 * * 0` | So 04:00 |
| afu_asiatische_hornisse_import | Aktiv | `15 4 * * *` | 04:15 |
| afu_asiatische_hornisse_pub | Aktiv | `30 4 * * *` | 04:30 |
| arp_sein_konfiguration | Aktiv | `H 4 31 1,3,4,7,8,10,12 *\nH 4 30 4,6,9,11 *\nH 4 28,29 2 *` | ~4:xx |
| arp_sein_strukturdaten_export | Aktiv | `H 4 31 1,3,4,7,8,10,12 *\nH 4 30 4,6,9,11 *\nH 4 28,29 2 *` | ~4:xx |
| agi_generate_matomo_reports | Aktiv | `H 4 1 * *` | 1. ~4:xx |
| afu_neophyten_pub | Aktiv | `H 6 * * *` | ~6:xx |
| agi_av_dm01_mopublic_pub | Aktiv | `00 21 * * *` | 21:00 |
| arp_auswertung_nutzungsplanung_pub | Aktiv | `H H(1-3) 31 1,3,4,7,8,10,12 *\nH H(1-3) 30 4,6,9,11 *\nH H(1-3) 28,29 2 *` | ~1-3h |
| afu_igel | Aktiv | `H H(3-4) * * 0` | So ~3-4h |
| avt_bodenfaktor_pub | Aktiv | `H H(2-5) * * 0` | So ~2-5h |
| afu_onlinerisk_transfer | Aktiv | `H H(18-19) * * 1-5` | ~18-19h |
| alw_landwirtschaft_tierhaltung_import_bodenbedeckung | Aktiv | `H H(3-4) * * 5` | Fr ~3-4h |
| alw_strukturverbesserungen_pub | Aktiv | `H H(1-3) * * 6` | Sa ~1-3h |
| agi_ch_gemeinden | Aktiv | `H H(1-3) 1 2 *` | 1. ~1-3h |
| alw_landwirtschaft_tierhaltung_import_massnahmen | Aktiv | `H H(3-4) 1 * *` | 1. ~3-4h |
| amb_zivilschutz_adressen_export | Aktiv | `H H(1-3) 1 * *` | 1. ~1-3h |
| arp_richtplan_grundnutzung_pub | Aktiv | `H H(1-3) 1 * *` | 1. ~1-3h |
| awjf_rodung_rodungsersatz_mgdm | Aktiv | `H H(1-3) 1 3 *` | 1. ~1-3h |
| agi_swisstopo_gebaeudeadressen | Aktiv | `H H(1-3) 2 * *` | 2. ~1-3h |
| arp_mjpnl_v2_auszahlung | Aktiv | `H H(1-3) 15 1 *` | 15. ~1-3h |
| ada_archaeologie_pub | Aktiv | `H H(1-3) * * 7` | So ~1-3h |
| afu_altlasten_import_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| afu_erdwaermesonden_private_quellen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| afu_erdwaermesonden_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| afu_grundlagendaten_ews_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| afu_naturereigniskataster_mgdm_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| afu_stehende_gewaesser_abgleich | Aktiv | `H H(1-3) * * 7` | So ~1-3h |
| afu_wasserbewirtschaftung_pub | Aktiv | `H H(1-3) * * 7` | So ~1-3h |
| agem_finanz_und_lastenausgleich | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_adressen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_av_export_ai | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_av_gb_abgleich_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_av_gwr_abgleich_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_av_meldewesen | Aktiv | `H H(3-4) * * *` | ~3-4h |
| agi_av_mocheckso | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_dmav_fixpunkte2_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_dmav_fixpunktelv_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_dmav_hoheitsgrenzen_lv_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_dmav_hoheitsgrenzpunkte_lv_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_dmav_plz_ortschaft_import | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_gb2av_controlling | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_gwr_pub | Aktiv | `H H(3-4) * * *` | ~3-4h |
| agi_hoheitsgrenzen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_kartenkatalog | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_kartenkatalog_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| agi_stac | Aktiv | `H H(5-6) * * *` | ~5-6h |
| alw_landwirtschaft_tierhaltung_pub | Aktiv | `H H(2-4) * * *` | ~2-4h |
| alw_tiergesundheit_pflanzengesundheit_massnahmen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_agglomerationsprogramme_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_arbeitszonenbewirtschaftung_inventar_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_bauzonengrenzen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_fledermaus | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_mjpnatur_gelan_export | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_mjpnatur_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_mjpnl_v2_zahlungslauf | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_nutzungsplanung_planregister_export | Aktiv | `H H(1-3) * * *` | ~1-3h |
| arp_nutzungsvereinbarung_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| awjf_efj | Aktiv | `H H(4-5) * * *` | ~4-5h |
| awjf_forstreviere_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| awjf_programm_biodiversitaet_wald_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| awjf_schutzwald_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| awjf_waldpflege_kontrolle | Aktiv | `H H(1-3) * * *` | ~1-3h |
| awjf_wegsanierungen_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| dsbjd_ausgleichsabgabe_pub | Aktiv | `H H(1-3) * * *` | ~1-3h |
| dsbjd_ebauso_rahmenmodell_pub | Aktiv | `H H(3-4) * * *` | ~3-4h |
| sgv_schadenkarte | Aktiv | `H H(6-7) * * *` | ~6-7h |

---

## Upstream-gesteuerte Jobs

**Anzahl:** 13

| Job | Status | Upstream Job |
|-----|--------|--------------|
| ada_denkmalschutz_pub | Aktiv | oerebv2_einzelschutz_denkmal |
| afu_bodendaten_nabodat_abfrage_pub | Aktiv | afu_bodenprofilstandorte_nabodat_pub |
| afu_geotope_pub | Aktiv | oereb_einzelschutz_geotop |
| afu_stehende_gewaesser_pub | Aktiv | afu_stehende_gewaesser_abgleich |
| agi_gebaeudeinformationen_pub | Aktiv | agi_av_dm01_mopublic_pub |
| agi_grundbuchplan_pub | Aktiv | agi_av_dm01_mopublic_pub |
| arp_richtplan_abbaustellen_pub | Aktiv | afu_abbaustellen_pub |
| arp_richtplan_fruchtfolgeflaechen_pub | Aktiv | alw_fruchtfolgeflaechen_pub |
| arp_richtplan_gewaesserschutz_pub | Aktiv | afu_gewaesserschutz_zonen_areale_pub |
| arp_richtplan_naturreservate_pub | Aktiv | arp_naturreservate_pub |
| arp_richtplan_oeffentlicher_verkehr_pub | Aktiv | avt_oeffentlicher_verkehr_pub |
| awjf_efj_geodaten_upload | Aktiv | awjf_jagdreviere_jagdbanngebiete_pub, awjf_gewaesser_fischerei_pub |
| awjf_statische_waldgrenzen_export_ai | Aktiv | awjf_statische_waldgrenze_pub |

---

## Manuelle Jobs

**Anzahl:** 130

| Job | Status |
|-----|--------|
| afu_abbaustellen_pub | Aktiv |
| afu_ara_einzugsgebiete_pub | Aktiv |
| afu_baugrundklassen_pub | Aktiv |
| afu_bodendaten_schadstoffuntersuchung_pub | Aktiv |
| afu_bodenprofilstandorte_nabodat_pub | Aktiv |
| afu_bodenverdichtung_pub | Aktiv |
| afu_bootsanbindeplaetze_mfk | Aktiv |
| afu_bootsanbindeplaetze_pub | Aktiv |
| afu_bootsanbindeplaetze_sap | Aktiv |
| afu_ekat_2005_pub | Aktiv |
| afu_ekat_2010_pub | Aktiv |
| afu_ekat_2015_pub | Aktiv |
| afu_ewsabfrage_3d | Aktiv |
| afu_geologie_pub | Aktiv |
| afu_gewaesser_gewaessereigenschaften_pub | Aktiv |
| afu_gewaesser_oekomorphologie_pub | Aktiv |
| afu_gewaesser_revitalisierung_pub | Aktiv |
| afu_gewaesserschutz_bereiche_pub | Aktiv |
| afu_gewaesserschutz_zonen_areale_pub | Aktiv |
| afu_grundwassergeometrie_pub | Aktiv |
| afu_hydro_messstationen_pub | Aktiv |
| afu_hydrologische_einzugsgebiete_pub | Aktiv |
| afu_immissionskarten_luft_pub | Aktiv |
| afu_isboden_csv_import | Aktiv |
| afu_isboden_pub | Aktiv |
| afu_karst_pub | Aktiv |
| afu_klimaanalyse_pub | Aktiv |
| afu_klimaanalyse_windpfeile_pub | Aktiv |
| afu_nabodat_import | Aktiv |
| afu_naturgefahren_freigeben | Aktiv |
| afu_naturgefahren_import | Aktiv |
| afu_naturgefahren_pilot_import | Aktiv |
| afu_naturgefahren_produkte | Aktiv |
| afu_naturgefahren_pub | Aktiv |
| afu_naturgefahrenhinweiskarte_pub | Aktiv |
| afu_oekomorphologie_csvimport | Aktiv |
| afu_qrcat_berechnungen | Aktiv |
| afu_quellen_ungefasst_csvimport | Aktiv |
| afu_quellen_ungefasst_pub | Aktiv |
| afu_schadendienst_pub | Aktiv |
| afu_schadstoffbelastete_boeden_pub | Aktiv |
| afu_schutzbauten_export | Aktiv |
| afu_schutzbauten_import | Aktiv |
| afu_schutzbauten_pub | Aktiv |
| afu_stoerfallverordnung_pub | Aktiv |
| agi_check_ili_export | Aktiv |
| agi_dmav_dauerndebodenverschiebungen_export | Aktiv |
| agi_dmav_fixpunkte3_import | Aktiv |
| agi_dmav_rohrleitungen_export | Aktiv |
| agi_dmav_toleranzstufen_export | Aktiv |
| agi_inventar_hoheitsgrenzen_pub | Aktiv |
| agi_layer_rollout | Aktiv |
| agi_lk_netzgebiete_pub | Aktiv |
| agi_plz_ortschaften_pub_manueller_import | Aktiv |
| agi_schema_dump | Aktiv |
| agi_suchindex_pub | Aktiv |
| alw_drainagen_bemerkungen_pub | Aktiv |
| alw_drainagen_import | Aktiv |
| alw_drainagen_pub | Aktiv |
| alw_fruchtfolgeflaechen | Aktiv |
| alw_fruchtfolgeflaechen_export_ai | Aktiv |
| alw_fruchtfolgeflaechen_pub | Aktiv |
| alw_futterbaulinien_pub | Aktiv |
| alw_gewaesserraum_pub | Aktiv |
| alw_strukturverbesserungen_suissemelio | Aktiv |
| alw_zonengrenzen_import | Aktiv |
| arp_mjpnl_auszahlung | Aktiv |
| arp_mjpnl_gelan_update | Aktiv |
| arp_mjpnl_initialisierung | Aktiv |
| arp_mjpnl_migration | Aktiv |
| arp_mjpnl_v2_gelan_update | Aktiv |
| arp_mjpnl_v2_initialisierung | Aktiv |
| arp_mjpnl_v2_migration | Aktiv |
| arp_mjpnl_zahlungslauf | Aktiv |
| arp_naturreservate_pub | Aktiv |
| arp_naturschutzobjekte_pub | Aktiv |
| arp_nutzungsplanung_delete_dataset | Aktiv |
| arp_nutzungsplanung_digizone_pub | Aktiv |
| arp_nutzungsplanung_import | Aktiv |
| arp_nutzungsplanung_import_ersterfassung | Aktiv |
| arp_nutzungsplanung_kanton_pub | Aktiv |
| arp_nutzungsplanung_planregister_pub_alles | Aktiv |
| arp_nutzungsplanung_pub | Aktiv |
| arp_richtplan_inventar_historische_verkehrswege_pub | Aktiv |
| arp_richtplan_richtplan_pub | Aktiv |
| arp_sein_konfiguration_local | Aktiv |
| arp_statent_import | Aktiv |
| arp_statpop_import | Aktiv |
| arp_statpopent_hektarraster | Aktiv |
| arp_waldreservate_pub | Aktiv |
| arp_wanderwege_import_xtf | Aktiv |
| arp_wanderwege_pub | Aktiv |
| arp_wildruhezonen_export_ai | Aktiv |
| avt_ausnahmetransportrouten_export_ai | Aktiv |
| avt_groblaermkataster_pub | Aktiv |
| avt_gvm_import | Aktiv |
| avt_kantonsstrassen_pub | Aktiv |
| avt_kunstbauten_pub | Aktiv |
| avt_mehrjahresplanung_pub | Aktiv |
| avt_oeffentlicher_verkehr_pub | Aktiv |
| avt_oev_gueteklassen_import | Aktiv |
| avt_oevkov | Aktiv |
| avt_strassenlaerm | Aktiv |
| avt_strassenzustand_pub | Aktiv |
| avt_verkehrszaehlstellen_pub | Aktiv |
| awjf_biotopbaeume_import | Aktiv |
| awjf_gesuchsteller | Aktiv |
| awjf_gewaesser_fischerei_pub | Aktiv |
| awjf_jagdreviere_jagdbanngebiete_pub | Aktiv |
| awjf_rodung_rodungsersatz_pub | Aktiv |
| awjf_samenerntekataster_pub | Aktiv |
| awjf_seltene_baeume_pub | Aktiv |
| awjf_silvaprotect_pub | Aktiv |
| awjf_statische_waldgrenze_pub | Aktiv |
| awjf_wald_pub | Aktiv |
| awjf_waldpflege_kontrolle_pub | Aktiv |
| awjf_waldplan_bestandeskarte_import_shp | Aktiv |
| awjf_waldplan_bestandeskarte_pub | Aktiv |
| awjf_waldplan_bestandeskarte_staging | Aktiv |
| awjf_waldplan_pub | Aktiv |
| awjf_waldplan_pub_erstimport | Aktiv |
| awjf_waldportal | Aktiv |
| awjf_waldwanderwege_pub | Aktiv |
| awjf_wildtiersensible_gebiete_pub | Aktiv |
| hba_gebaeude_pub | Aktiv |
| hba_gebaeude_pub_v2 | Aktiv |
| hba_grundstuecke_pub | Aktiv |
| hba_grundstuecke_pub_v2 | Aktiv |
| ksta_landwert_pub | Aktiv |
| sk_plakatstandorte | Aktiv |

---

## Schema-Übersicht

**Anzahl Schemas:** 234

| Schema | Beschreibung | Anzahl Jobs | Anzahl Tabellen |
|--------|--------------|-------------|-----------------|
| EXCLUDED | EXCLUDED | 1 | 12 |
| ada_archaeologie_pub_v1 | Amt für Denkmalpflege und Archäologie | 2 | 5 |
| ada_archaeologie_v1 | Amt für Denkmalpflege und Archäologie | 1 | 5 |
| ada_denkmalschutz_pub_v1 | Amt für Denkmalpflege und Archäologie | 1 | 2 |
| ada_denkmalschutz_v1 | Amt für Denkmalpflege und Archäologie | 1 | 3 |
| afu_abbaustellen_fff_v1 | Amt für Umwelt | 1 | 1 |
| afu_abbaustellen_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_abbaustellen_v1 | Amt für Umwelt | 1 | 2 |
| afu_altlasten_pub | Amt für Umwelt | 1 | 1 |
| afu_altlasten_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_altlasten_restricted_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_ara_einzugsgebiete | Amt für Umwelt | 1 | 1 |
| afu_asiatische_hornisse_v2 | Amt für Umwelt | 1 | 2 |
| afu_baugrundklassen_v1 | Amt für Umwelt | 1 | 1 |
| afu_bodendaten_nabodat_abfrage_pub_v1 | Amt für Umwelt | 1 | 2 |
| afu_bodendaten_nabodat_pub | Amt für Umwelt | 1 | 1 |
| afu_bodendaten_nabodat_v1 | Amt für Umwelt | 3 | 77 |
| afu_bodenverdichtung_v1 | Amt für Umwelt | 1 | 2 |
| afu_bootsanbindeplaetze | Amt für Umwelt | 1 | 2 |
| afu_bootsanbindeplaetze_mfk | Amt für Umwelt | 1 | 2 |
| afu_bootsanbindeplaetze_v1 | Amt für Umwelt | 1 | 8 |
| afu_erdwaermesonden_private_quellen_v1 | Amt für Umwelt | 1 | 1 |
| afu_erdwaermesonden_v2 | Amt für Umwelt | 1 | 2 |
| afu_ewsabfrage_2d_staging_v1 | Amt für Umwelt | 1 | 5 |
| afu_ewsabfrage_2d_v1 | Amt für Umwelt | 1 | 3 |
| afu_ewsabfrage_3d_staging_v1 | Amt für Umwelt | 1 | 2 |
| afu_gefahrenkartierung | Amt für Umwelt | 1 | 13 |
| afu_geologie_v1 | Amt für Umwelt | 1 | 27 |
| afu_geotope | Amt für Umwelt | 1 | 25 |
| afu_gewaesser_gewaessereigenschaften_pub_v1 | Amt für Umwelt | 1 | 5 |
| afu_gewaesser_oekomorphologie_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_gewaesser_revitalisierung_v1 | Amt für Umwelt | 1 | 2 |
| afu_gewaesser_v1 | Amt für Umwelt | 4 | 5 |
| afu_gewaesserschutz_bereiche_v1 | Amt für Umwelt | 1 | 1 |
| afu_gewaesserschutz_pub | Amt für Umwelt | 1 | 1 |
| afu_gewaesserschutz_pub_v3 | Amt für Umwelt | 3 | 2 |
| afu_gewaesserschutz_staging_v3 | Amt für Umwelt | 1 | 10 |
| afu_gewaesserschutz_zonen_areale_v1 | Amt für Umwelt | 2 | 6 |
| afu_grundlagendaten_ews_v1 | Amt für Umwelt | 1 | 4 |
| afu_grundwassergeometrie_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_grundwassergeometrie_v1 | Amt für Umwelt | 1 | 12 |
| afu_grundwasserschutz_obj_v1 | Amt für Umwelt | 1 | 13 |
| afu_hydro_messstationen_pub_v1 | Amt für Umwelt | 1 | 2 |
| afu_hydro_messstationen_v1 | Amt für Umwelt | 1 | 1 |
| afu_hydrologische_einzugsgebiete_v2 | Amt für Umwelt | 1 | 3 |
| afu_igel | Amt für Umwelt | 1 | 2 |
| afu_immissionskarten_luft_v1 | Amt für Umwelt | 1 | 1 |
| afu_isboden | Amt für Umwelt | 2 | 16 |
| afu_isboden_csv_import_v1 | Amt für Umwelt | 1 | 1 |
| afu_isboden_fff_pub | Amt für Umwelt | 1 | 1 |
| afu_isboden_pub | Amt für Umwelt | 1 | 1 |
| afu_karst_v1 | Amt für Umwelt | 1 | 6 |
| afu_klimaanalyse_v1 | Amt für Umwelt | 1 | 12 |
| afu_klimaanalyse_windpfeile_v1 | Amt für Umwelt | 1 | 12 |
| afu_naturereigniskataster_mgdm_v1 | Amt für Umwelt | 1 | 15 |
| afu_naturgefahren_beurteilungsgebiet_v1 | Amt für Umwelt | 1 | 10 |
| afu_naturgefahren_beurteilungsgebiet_v2 | Amt für Umwelt | 1 | 7 |
| afu_naturgefahren_mgdm_v1 | Amt für Umwelt | 1 | 3 |
| afu_naturgefahren_pub_v2 | Amt für Umwelt | 1 | 1 |
| afu_naturgefahren_staging_v1 | Amt für Umwelt | 1 | 24 |
| afu_naturgefahren_staging_v2 | Amt für Umwelt | 2 | 33 |
| afu_naturgefahren_v1 | Amt für Umwelt | 1 | 22 |
| afu_naturgefahren_v2 | Amt für Umwelt | 1 | 2 |
| afu_naturgefahrenhinweiskarte_pub_v1 | Amt für Umwelt | 1 | 1 |
| afu_naturgefahrenhinweiskarte_v1 | Amt für Umwelt | 1 | 9 |
| afu_online_risk | Amt für Umwelt | 1 | 10 |
| afu_quellen_ungefasst_staging_v1 | Amt für Umwelt | 1 | 1 |
| afu_schadendienst_v1 | Amt für Umwelt | 1 | 2 |
| afu_schadstoffbelastete_boeden | Amt für Umwelt | 1 | 63 |
| afu_schadstoffbelastete_boeden_pub | Amt für Umwelt | 1 | 8 |
| afu_schutzbauten_v1 | Amt für Umwelt | 1 | 40 |
| afu_stehende_gewaesser_v1 | Amt für Umwelt | 2 | 1 |
| afu_stoerfallverordnung_v1 | Amt für Umwelt | 1 | 8 |
| afu_wasserbewirtschaftung_pub_v2 | Amt für Umwelt | 1 | 2 |
| afu_wasserversorg_obj_v1 | Amt für Umwelt | 1 | 15 |
| agem_fila | agem_fila | 1 | 1 |
| agi_av_gb_abgleich_import | Amt für Geoinformation | 1 | 3 |
| agi_av_gb_admin_einteilung_pub | Amt für Geoinformation | 4 | 2 |
| agi_av_gb_administrative_einteilungen_v2 | Amt für Geoinformation | 4 | 4 |
| agi_av_gwr_abgleich_import_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_gwr_abgleich_pub_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_gwr_abgleich_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_kaso_abgleich_v1 | Amt für Geoinformation | 1 | 3 |
| agi_av_meldewesen_import_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_meldewesen_work_v1 | Amt für Geoinformation | 1 | 1 |
| agi_av_mocheckso | Amt für Geoinformation | 1 | 1 |
| agi_dm01avso24 | Amt für Geoinformation | 22 | 81 |
| agi_gb2av | Amt für Geoinformation | 1 | 3 |
| agi_gb2av_controlling | Amt für Geoinformation | 1 | 2 |
| agi_gebaeudeinformationen_pub_v1 | Amt für Geoinformation | 2 | 1 |
| agi_grundbuchplan_pub | Amt für Geoinformation | 1 | 2 |
| agi_gwr_pub_v1 | Amt für Geoinformation | 3 | 2 |
| agi_gwr_v1 | Amt für Geoinformation | 1 | 3 |
| agi_hoheitsgrenzen_pub | Amt für Geoinformation | 37 | 12 |
| agi_hoheitsgrenzen_v1 | Amt für Geoinformation | 2 | 6 |
| agi_inventar_hoheitsgrenzen | Amt für Geoinformation | 1 | 3 |
| agi_kartenkatalog_v2 | Amt für Geoinformation | 1 | 2 |
| agi_lk_netzgebiete_v1 | Amt für Geoinformation | 1 | 4 |
| agi_mopublic_pub | Amt für Geoinformation | 12 | 7 |
| agi_plz_ortschaften | Amt für Geoinformation | 3 | 3 |
| agi_plz_ortschaften_pub | Amt für Geoinformation | 1 | 2 |
| agi_swissboundaries3d_pub | Amt für Geoinformation | 3 | 4 |
| agi_swissboundaries3d_v1 | Amt für Geoinformation | 1 | 4 |
| agi_swissboundaries3d_v2 | Amt für Geoinformation | 1 | 6 |
| agi_swisstopo_gebaeudeadressen_pub_v1 | Amt für Geoinformation | 1 | 1 |
| agi_swisstopo_gebaeudeadressen_v1 | Amt für Geoinformation | 1 | 3 |
| alw_drainagen_bemerkungen_v1 | Amt für Landwirtschaft | 1 | 1 |
| alw_drainagen_v1 | Amt für Landwirtschaft | 1 | 3 |
| alw_fff_uebersteuerung | Amt für Landwirtschaft | 1 | 1 |
| alw_fruchtfolgeflaechen | Amt für Landwirtschaft | 1 | 27 |
| alw_fruchtfolgeflaechen_mgdm_v1 | Amt für Landwirtschaft | 1 | 2 |
| alw_fruchtfolgeflaechen_pub_v1 | Amt für Landwirtschaft | 3 | 1 |
| alw_fruchtfolgeflaechen_v1 | Amt für Landwirtschaft | 2 | 2 |
| alw_futterbaulinien_v1 | Amt für Landwirtschaft | 1 | 1 |
| alw_gewaesserraum | Amt für Landwirtschaft | 1 | 1 |
| alw_gewaesserraum_v1 | Amt für Landwirtschaft | 2 | 1 |
| alw_landwirtschaft_tierhaltung_v1 | Amt für Landwirtschaft | 1 | 10 |
| alw_strukturverbesserungen | Amt für Landwirtschaft | 2 | 51 |
| alw_tiergesundheit_pflanzengesundheit_massnahmen_v1 | Amt für Landwirtschaft | 1 | 3 |
| alw_uebersteuerung_fff_v2 | Amt für Landwirtschaft | 1 | 1 |
| alw_zonengrenzen | Amt für Landwirtschaft | 2 | 6 |
| amb_zivilschutz_adressen_staging_pub | amb_zivilschutz_adressen_staging_pub | 1 | 1 |
| arp_agglomerationsprogramme | Amt für Raumplanung | 1 | 13 |
| arp_arbeitszonenbewirtschaftung_pub_v2 | Amt für Raumplanung | 1 | 1 |
| arp_arbeitszonenbewirtschaftung_staging_v2 | Amt für Raumplanung | 1 | 3 |
| arp_arbeitszonenbewirtschaftung_v2 | Amt für Raumplanung | 1 | 2 |
| arp_auswertung_nutzungsplanung_pub_v1 | Amt für Raumplanung | 3 | 6 |
| arp_bauzonengrenzen_pub | Amt für Raumplanung | 2 | 1 |
| arp_fledermaus_v1 | Amt für Raumplanung | 1 | 1 |
| arp_inventar_historische_verkehrswege_v1 | Amt für Raumplanung | 1 | 2 |
| arp_laermempfindlichkeitsstufen_mgdm_v1 | Amt für Raumplanung | 1 | 9 |
| arp_mehrjahresprogramm | Amt für Raumplanung | 2 | 1 |
| arp_mjpnatur_pub | Amt für Raumplanung | 1 | 1 |
| arp_mjpnl_gelan_v1 | Amt für Raumplanung | 1 | 1 |
| arp_mjpnl_v1 | Amt für Raumplanung | 1 | 15 |
| arp_mjpnl_v2 | Amt für Raumplanung | 2 | 12 |
| arp_naturreservate | Amt für Raumplanung | 3 | 10 |
| arp_naturreservate_pub | Amt für Raumplanung | 2 | 1 |
| arp_naturreservate_staging_v1 | Amt für Raumplanung | 1 | 5 |
| arp_naturschutzobjekte_pub_v1 | Amt für Raumplanung | 1 | 1 |
| arp_naturschutzobjekte_v1 | Amt für Raumplanung | 1 | 6 |
| arp_npl_pub | Amt für Raumplanung | 1 | 1 |
| arp_nutzungsplanung_export_v1 | Amt für Raumplanung | 2 | 24 |
| arp_nutzungsplanung_import_v1 | Amt für Raumplanung | 2 | 25 |
| arp_nutzungsplanung_kanton_v1 | Amt für Raumplanung | 3 | 28 |
| arp_nutzungsplanung_mgdm_v1 | Amt für Raumplanung | 2 | 20 |
| arp_nutzungsplanung_planregister_pub_v1 | Amt für Raumplanung | 6 | 1 |
| arp_nutzungsplanung_pub_v1 | Amt für Raumplanung | 8 | 7 |
| arp_nutzungsplanung_transfer_pub_v1 | Amt für Raumplanung | 3 | 10 |
| arp_nutzungsplanung_transfer_v1 | Amt für Raumplanung | 2 | 28 |
| arp_nutzungsplanung_v1 | Amt für Raumplanung | 2 | 32 |
| arp_nutzungsvereinbarung | Amt für Raumplanung | 1 | 2 |
| arp_planungszonen_mgdm_v1 | Amt für Raumplanung | 1 | 8 |
| arp_richtplan_pub_v2 | Amt für Raumplanung | 8 | 10 |
| arp_richtplan_v2 | Amt für Raumplanung | 2 | 16 |
| arp_sein_konfiguration_grundlagen_v2 | Amt für Raumplanung | 3 | 2 |
| arp_statpop_statent_staging_v1 | Amt für Raumplanung | 2 | 3 |
| arp_statpop_statent_v1 | Amt für Raumplanung | 2 | 3 |
| arp_waldabstandslinien_mgdm_v1 | Amt für Raumplanung | 1 | 9 |
| arp_waldreservate_mgdm_v1 | Amt für Raumplanung | 1 | 3 |
| arp_waldreservate_pub_v1 | Amt für Raumplanung | 1 | 3 |
| arp_waldreservate_v1 | Amt für Raumplanung | 1 | 4 |
| arp_wanderwege_pub_v1 | Amt für Raumplanung | 1 | 1 |
| arp_wanderwege_v1 | Amt für Raumplanung | 2 | 23 |
| auen | auen | 1 | 1 |
| avt_bodenfaktor | Amt für Verkehr und Tiefbau | 1 | 3 |
| avt_gesamtverkehrsmodell_2019_pub_v1 | Amt für Verkehr und Tiefbau | 1 | 4 |
| avt_kantonsstrassen_pub_v1 | Amt für Verkehr und Tiefbau | 1 | 2 |
| avt_kantonsstrassen_staging_v1 | Amt für Verkehr und Tiefbau | 1 | 3 |
| avt_kunstbauten_staging_v1 | Amt für Verkehr und Tiefbau | 1 | 1 |
| avt_mehrjahresplanung_v2 | Amt für Verkehr und Tiefbau | 1 | 4 |
| avt_oeffentlicher_verkehr | Amt für Verkehr und Tiefbau | 1 | 2 |
| avt_oeffentlicher_verkehr_pub | Amt für Verkehr und Tiefbau | 1 | 1 |
| avt_strassenlaerm_v1 | Amt für Verkehr und Tiefbau | 1 | 5 |
| avt_strassenzustand_staging_v1 | Amt für Verkehr und Tiefbau | 1 | 1 |
| avt_verkehrszaehlstellen | Amt für Verkehr und Tiefbau | 1 | 2 |
| awa_stromversorgungssicherheit_mgdm_v1 | awa_stromversorgungssicherheit_mgdm_v1 | 1 | 4 |
| awjf | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_efj_geodaten_upload_v1 | Amt für Wald, Jagd und Fischerei | 1 | 2 |
| awjf_efj_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_forstreviere | Amt für Wald, Jagd und Fischerei | 5 | 3 |
| awjf_gesuchsteller | Amt für Wald, Jagd und Fischerei | 2 | 1 |
| awjf_jagdreviere_jagdbanngebiete_v1 | Amt für Wald, Jagd und Fischerei | 2 | 4 |
| awjf_programm_biodiversitaet_wald_v1 | Amt für Wald, Jagd und Fischerei | 2 | 7 |
| awjf_rodung_rodungsersatz_mgdm_v1 | Amt für Wald, Jagd und Fischerei | 1 | 6 |
| awjf_rodung_rodungsersatz_v1 | Amt für Wald, Jagd und Fischerei | 2 | 13 |
| awjf_samenerntekataster_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_schutzwald_pub_v1 | Amt für Wald, Jagd und Fischerei | 1 | 11 |
| awjf_schutzwald_v1 | Amt für Wald, Jagd und Fischerei | 3 | 4 |
| awjf_seltene_baeume | Amt für Wald, Jagd und Fischerei | 1 | 4 |
| awjf_silvaprotect_v1 | Amt für Wald, Jagd und Fischerei | 1 | 5 |
| awjf_statische_waldgrenze | Amt für Wald, Jagd und Fischerei | 5 | 4 |
| awjf_statische_waldgrenze_mgdm_v1 | Amt für Wald, Jagd und Fischerei | 1 | 9 |
| awjf_statische_waldgrenze_staging_v1 | Amt für Wald, Jagd und Fischerei | 1 | 8 |
| awjf_wald_oberhoehenbonitaet_v1 | Amt für Wald, Jagd und Fischerei | 1 | 2 |
| awjf_waldpflege_erfassung | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_waldpflege_kontrolle | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_waldplan_bestandeskarte_staging_v1 | Amt für Wald, Jagd und Fischerei | 2 | 1 |
| awjf_waldplan_bestandeskarte_v1 | Amt für Wald, Jagd und Fischerei | 4 | 1 |
| awjf_waldplan_pub_v2 | Amt für Wald, Jagd und Fischerei | 2 | 7 |
| awjf_waldplan_v2 | Amt für Wald, Jagd und Fischerei | 2 | 19 |
| awjf_waldstandorte_v1 | Amt für Wald, Jagd und Fischerei | 2 | 1 |
| awjf_waldwanderwege | Amt für Wald, Jagd und Fischerei | 1 | 2 |
| awjf_wegsanierungen_v1 | Amt für Wald, Jagd und Fischerei | 1 | 1 |
| awjf_wildtiersensible_gebiete_v1 | Amt für Wald, Jagd und Fischerei | 1 | 2 |
| bohrung | bohrung | 1 | 1 |
| capi_p | capi_p | 1 | 1 |
| dsbjd_ausgleichsabgabe_v1 | dsbjd_ausgleichsabgabe_v1 | 1 | 1 |
| dsbjd_ebauso_rahmenmodell_pub_v1 | dsbjd_ebauso_rahmenmodell_pub_v1 | 1 | 5 |
| dsbjd_ebauso_rahmenmodell_stage_v1 | dsbjd_ebauso_rahmenmodell_stage_v1 | 1 | 3 |
| editdb | editdb | 4 | 9 |
| export | export | 1 | 46 |
| flachmoore | flachmoore | 1 | 1 |
| hba_gebaeude_v2 | hba_gebaeude_v2 | 1 | 1 |
| hba_grundstuecke_v2 | hba_grundstuecke_v2 | 1 | 1 |
| hochmoore | hochmoore | 1 | 1 |
| import | import | 1 | 9 |
| importschema_xtf | importschema_xtf | 2 | 10 |
| klimaeignung | klimaeignung | 1 | 2 |
| ksta_landwerte | ksta_landwerte | 1 | 1 |
| l | l | 1 | 2 |
| live | live | 1 | 3 |
| main | main | 2 | 3 |
| mjpnatur | mjpnatur | 1 | 11 |
| pubdb | pubdb | 3 | 21 |
| public | public | 2 | 2 |
| sein | sein | 2 | 8 |
| sgv_schadenkarte_pub_v1 | sgv_schadenkarte_pub_v1 | 1 | 1 |
| sgv_schadenkarte_v1 | sgv_schadenkarte_v1 | 1 | 1 |
| simi | simi | 4 | 44 |
| sk_plakatstandorte_staging_v1 | sk_plakatstandorte_staging_v1 | 1 | 1 |
| sk_plakatstandorte_v1 | sk_plakatstandorte_v1 | 1 | 1 |
| themeDB | themeDB | 1 | 1 |
| trockenwiesenweiden | trockenwiesenweiden | 1 | 1 |

---

## Detailierte Job-Informationen

### ada_archaeologie_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/ada_archaeologie_pub`
**Schedule:** `H H(1-3) * * 7` (So ~1-3h)

**Quell-Tabellen:**
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.public_qualitaet_lokalisierung_typ
- ada_archaeologie_pub_v1.restricted_flaechenfundstelle
- ada_archaeologie_pub_v1.restricted_punktfundstelle
- ada_archaeologie_v1.fachapplikation_fundstelle
- ada_archaeologie_v1.fachapplikation_regierungsratsbeschluss
- ada_archaeologie_v1.geo_ablage_gemeinde
- ada_archaeologie_v1.geo_flaeche
- ada_archaeologie_v1.geo_schutzbereich_innenstadt
- arp_bauzonengrenzen_pub.bauzonengrenzen_bauzonengrenze
- j
- public.rep_view_fundstellen
- rep_view_rrb

**Ziel-Tabellen:**
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.restricted_flaechenfundstelle
- ada_archaeologie_pub_v1.restricted_punktfundstelle
- ada_archaeologie_v1.fachapplikation_fundstelle
- ada_archaeologie_v1.geo_flaeche

---

### afu_altlasten_import_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_altlasten_import_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### afu_asiatische_hornisse_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_asiatische_hornisse_import`
**Schedule:** `15 4 * * *` (04:15)

**Quell-Tabellen:**
- EXCLUDED.geometrie
- EXCLUDED.import_bemerkung
- EXCLUDED.import_datum_sichtung
- EXCLUDED.import_foto_url
- EXCLUDED.import_kanton
- EXCLUDED.import_lat
- EXCLUDED.import_lon
- EXCLUDED.import_occurrence_id
- EXCLUDED.import_ort
- EXCLUDED.import_unique_nest_id
- EXCLUDED.import_x_koordinate
- EXCLUDED.import_y_koordinate
- ST_Read
- afu_individuals
- editdb.afu_asiatische_hornisse_v2.asia_hornisse_sichtung
- infofauna_individuals
- infofauna_nests

**Ziel-Tabellen:**
- SET
- afu_individuals
- anstatt
- auf
- infofauna_individuals
- infofauna_nests
- nur

---

### afu_asiatische_hornisse_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_asiatische_hornisse_pub`
**Schedule:** `30 4 * * *` (04:30)

**Quell-Tabellen:**
- afu_asiatische_hornisse_v2.asia_hornisse_nest
- afu_asiatische_hornisse_v2.asia_hornisse_sichtung

---

### afu_erdwaermesonden_private_quellen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_erdwaermesonden_private_quellen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- afu_erdwaermesonden_private_quellen_v1.private_quelle

---

### afu_erdwaermesonden_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_erdwaermesonden_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- afu_erdwaermesonden_v2.erdwaermesonden_anlage
- afu_erdwaermesonden_v2.erdwaermesonden_bohrung

---

### afu_ewsabfrage_2d

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_ewsabfrage_2d`
**Schedule:** `0 4 * * 0` (So 04:00)

**Quell-Tabellen:**
- afu_altlasten_pub_v2.belasteter_standort
- afu_ewsabfrage_2d_staging_v1.abfrageperimeter
- afu_ewsabfrage_2d_staging_v1.abklaerung
- afu_ewsabfrage_2d_staging_v1.grundstueck
- afu_ewsabfrage_2d_staging_v1.hinweis
- afu_ewsabfrage_2d_staging_v1.tiefenbeschraenkung
- afu_ewsabfrage_2d_v1.abfrageperimeter
- afu_ewsabfrage_2d_v1.abklaerung
- afu_ewsabfrage_2d_v1.tiefenbeschraenkung
- afu_gewaesser_oekomorphologie_pub_v1.oekomorphologie
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzareal
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone
- afu_grundlagendaten_ews_v1.bohrprofil
- afu_grundlagendaten_ews_v1.bohrung
- afu_grundlagendaten_ews_v1.standort
- afu_grundlagendaten_ews_v1.vorkommnis
- afu_grundwassergeometrie_pub_v1.grundwasserstrom_begrenzung_hgw
- afu_naturgefahrenhinweiskarte_pub_v1.rutschung_tief
- agi_mopublic_pub.mopublic_grundstueck

---

### afu_grundlagendaten_ews_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_grundlagendaten_ews_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- bohrung.

---

### afu_igel

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_igel`
**Schedule:** `H H(3-4) * * 0` (So ~3-4h)

**Quell-Tabellen:**
- LATERAL
- afu_igel.igel_stall
- afu_igel.igel_standort

---

### afu_naturereigniskataster_mgdm_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_naturereigniskataster_mgdm_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_basisinformation
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_a
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_ea_e
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_l
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_r
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_s
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_detailinformation_w_um
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_a
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_ea
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_l
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_r
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_s
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_prozessraum_w
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_sammelereignis
- afu_naturereigniskataster_mgdm_v1.storme_mgdm_schaden

---

### afu_neophyten_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_neophyten_pub`
**Schedule:** `H 6 * * *` (~6:xx)

**Quell-Tabellen:**
- neophyten

---

### afu_onlinerisk_transfer

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_onlinerisk_transfer`
**Schedule:** `H H(18-19) * * 1-5` (~18-19h)

**Quell-Tabellen:**
- afu_online_risk.bereich
- afu_online_risk.bereichstoff
- afu_online_risk.betrieb
- afu_online_risk.gebaeude
- afu_online_risk.konstruktion
- afu_online_risk.stammdaten
- afu_online_risk.stoff
- afu_online_risk.untersuchungseinheit
- afu_online_risk.verordnung
- afu_online_risk.verordnungsrelevanz
- bereich
- gebaeude
- untersuchungseinheit

---

### afu_stehende_gewaesser_abgleich

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_stehende_gewaesser_abgleich`
**Schedule:** `H H(1-3) * * 7` (So ~1-3h)

**Quell-Tabellen:**
- afu_stehende_gewaesser_v1.stehendes_gewaesser
- agi_dm01avso24.bodenbedeckung_boflaeche
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze

**Ziel-Tabellen:**
- afu_stehende_gewaesser_v1.stehendes_gewaesser

---

### afu_wasserbewirtschaftung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/afu_wasserbewirtschaftung_pub`
**Schedule:** `H H(1-3) * * 7` (So ~1-3h)

**Quell-Tabellen:**
- afu_grundwasserschutz_obj_v1.baggerschlitz
- afu_grundwasserschutz_obj_v1.baggerschlitz__dokument
- afu_grundwasserschutz_obj_v1.bohrung
- afu_grundwasserschutz_obj_v1.bohrung__dokument
- afu_grundwasserschutz_obj_v1.dokument
- afu_grundwasserschutz_obj_v1.einbaute
- afu_grundwasserschutz_obj_v1.einbaute__dokument
- afu_grundwasserschutz_obj_v1.grundwasserwaermepumpe
- afu_grundwasserschutz_obj_v1.grundwasserwaermepumpe__dokument
- afu_grundwasserschutz_obj_v1.piezometer__dokument
- afu_grundwasserschutz_obj_v1.piezometer_gerammt
- afu_grundwasserschutz_obj_v1.sodbrunnen
- afu_grundwasserschutz_obj_v1.sodbrunnen__dokument
- afu_wasserbewirtschaftung_pub_v2.wassrbwschftung_quelle_zustand
- afu_wasserversorg_obj_v1.dokument
- afu_wasserversorg_obj_v1.filterbrunnen
- afu_wasserversorg_obj_v1.filterbrunnen__dokument
- afu_wasserversorg_obj_v1.kontrollschacht
- afu_wasserversorg_obj_v1.kontrollschacht__dokument
- afu_wasserversorg_obj_v1.pumpwerk
- afu_wasserversorg_obj_v1.pumpwerk__dokument
- afu_wasserversorg_obj_v1.quelle_gefasst
- afu_wasserversorg_obj_v1.quelle_gefasst__dokument
- afu_wasserversorg_obj_v1.quellwasserbehaelter
- afu_wasserversorg_obj_v1.quellwasserbehaelter__dokument
- afu_wasserversorg_obj_v1.reservoir
- afu_wasserversorg_obj_v1.reservoir__dokument
- afu_wasserversorg_obj_v1.sammelbrunnstube
- afu_wasserversorg_obj_v1.sammelbrunnstube__dokument

**Ziel-Tabellen:**
- afu_wasserbewirtschaftung_pub_v2.wassrbwrtschftung_quelle

---

### agem_finanz_und_lastenausgleich

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agem_finanz_und_lastenausgleich`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agem_fila.strassen_strassenachse
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze

---

### agi_adressen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_adressen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.gebaeudeadressen_benanntesgebiet
- agi_dm01avso24.gebaeudeadressen_gebaeudeeingang
- agi_dm01avso24.gebaeudeadressen_hausnummerpos
- agi_dm01avso24.gebaeudeadressen_lokalisation
- agi_dm01avso24.gebaeudeadressen_lokalisationsname
- agi_dm01avso24.gebaeudeadressen_strassenstueck
- agi_dm01avso24.t_ili2db_basket
- agi_dm01avso24.t_ili2db_import

---

### agi_av_dm01_mopublic_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_dm01_mopublic_pub`
**Schedule:** `00 21 * * *` (21:00)

**Quell-Tabellen:**
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchamt
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.bodenbedeckung_bbnachfuehrung
- agi_dm01avso24.bodenbedeckung_boflaeche
- agi_dm01avso24.bodenbedeckung_gebaeudenummer
- agi_dm01avso24.bodenbedeckung_objektname
- agi_dm01avso24.bodenbedeckung_objektnamepos
- agi_dm01avso24.bodenbedeckung_projboflaeche
- agi_dm01avso24.bodenbedeckung_projgebaeudenummer
- agi_dm01avso24.bodenbedeckung_projobjektname
- agi_dm01avso24.bodenbedeckung_projobjektnamepos
- agi_dm01avso24.einzelobjekte_einzelobjekt
- agi_dm01avso24.einzelobjekte_eonachfuehrung
- agi_dm01avso24.einzelobjekte_flaechenelement
- agi_dm01avso24.einzelobjekte_linienelement
- agi_dm01avso24.einzelobjekte_objektname
- agi_dm01avso24.einzelobjekte_objektnamepos
- agi_dm01avso24.einzelobjekte_objektnummer
- agi_dm01avso24.einzelobjekte_punktelement
- agi_dm01avso24.fixpunktekatgrie1_hfp1
- agi_dm01avso24.fixpunktekatgrie1_hfp1nachfuehrung
- agi_dm01avso24.fixpunktekatgrie1_hfp1pos
- agi_dm01avso24.fixpunktekatgrie1_lfp1
- agi_dm01avso24.fixpunktekatgrie1_lfp1nachfuehrung
- agi_dm01avso24.fixpunktekatgrie1_lfp1pos
- agi_dm01avso24.fixpunktekatgrie2_hfp2
- agi_dm01avso24.fixpunktekatgrie2_hfp2nachfuehrung
- agi_dm01avso24.fixpunktekatgrie2_hfp2pos
- agi_dm01avso24.fixpunktekatgrie2_lfp2
- agi_dm01avso24.fixpunktekatgrie2_lfp2nachfuehrung
- agi_dm01avso24.fixpunktekatgrie2_lfp2pos
- agi_dm01avso24.fixpunktekatgrie3_hfp3
- agi_dm01avso24.fixpunktekatgrie3_hfp3nachfuehrung
- agi_dm01avso24.fixpunktekatgrie3_hfp3pos
- agi_dm01avso24.fixpunktekatgrie3_lfp3
- agi_dm01avso24.fixpunktekatgrie3_lfp3nachfuehrung
- agi_dm01avso24.fixpunktekatgrie3_lfp3pos
- agi_dm01avso24.gebaeudeadressen_gebaeudeeingang
- agi_dm01avso24.gebaeudeadressen_gebaeudename
- agi_dm01avso24.gebaeudeadressen_gebnachfuehrung
- agi_dm01avso24.gebaeudeadressen_hausnummerpos
- agi_dm01avso24.gebaeudeadressen_lokalisation
- agi_dm01avso24.gebaeudeadressen_lokalisationsname
- agi_dm01avso24.gebaeudeadressen_lokalisationsnamepos
- agi_dm01avso24.gebaeudeadressen_strassenstueck
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_dm01avso24.gemeindegrenzen_gemnachfuehrung
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunkt
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunktpos
- agi_dm01avso24.gemeindegrenzen_hoheitsgrenzpunktsymbol
- agi_dm01avso24.gemeindegrenzen_projgemeindegrenze
- agi_dm01avso24.liegenschaften_grenzpunkt
- agi_dm01avso24.liegenschaften_grenzpunktpos
- agi_dm01avso24.liegenschaften_grenzpunktsymbol
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_grundstueckpos
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_dm01avso24.liegenschaften_projgrundstueckpos
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_dm01avso24.nomenklatur_flurname
- agi_dm01avso24.nomenklatur_flurnamepos
- agi_dm01avso24.nomenklatur_gelaendename
- agi_dm01avso24.nomenklatur_gelaendenamepos
- agi_dm01avso24.nomenklatur_nknachfuehrung
- agi_dm01avso24.nomenklatur_ortsname
- agi_dm01avso24.nomenklatur_ortsnamepos
- agi_dm01avso24.nummerierngsbrche_nbgeometrie
- agi_dm01avso24.nummerierngsbrche_nummerierungsbereich
- agi_dm01avso24.rohrleitungen_leitungsobjekt
- agi_dm01avso24.rohrleitungen_linienelement
- agi_dm01avso24.rohrleitungen_rlnachfuehrung
- agi_dm01avso24.t_ili2db_basket
- agi_dm01avso24.t_ili2db_import
- agi_plz_ortschaften.plzortschaft_ortschaft
- agi_plz_ortschaften.plzortschaft_ortschaftsname
- agi_plz_ortschaften.plzortschaft_plz6
- mopublic_gemeindegrenze
- t_ili2db_basket
- t_ili2db_dataset

**Ziel-Tabellen:**
- mopublic_bodenbedeckung
- mopublic_bodenbedeckung_proj
- mopublic_einzelobjekt_flaeche
- mopublic_einzelobjekt_linie
- mopublic_einzelobjekt_punkt
- mopublic_fixpunkt
- mopublic_flurname
- mopublic_gebaeudeadresse
- mopublic_gelaendename
- mopublic_gemeindegrenze
- mopublic_gemeindegrenze_proj
- mopublic_grenzpunkt
- mopublic_grundstueck
- mopublic_grundstueck_linie
- mopublic_grundstueck_proj
- mopublic_grundstueck_proj_linie
- mopublic_hoheitsgrenzpunkt
- mopublic_objektname_pos
- mopublic_ortsname
- mopublic_rohrleitung
- mopublic_strassenachse
- mopublic_strassenname_pos
- t_ili2db_basket
- t_ili2db_dataset

---

### agi_av_export_ai

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_export_ai`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_av_gb_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_gb_abgleich_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_av_gb_abgleich_import.differenzen_staging
- agi_av_gb_abgleich_import.gb_daten
- agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_grundstuecksart
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_dm01avso24.t_ili2db_basket
- agi_dm01avso24.t_ili2db_import
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- capi_p.V_AIO_GrundstueckeMitFlaeche

**Ziel-Tabellen:**
- agi_av_gb_abgleich_import.differenzen_staging
- agi_av_gb_abgleich_import.uebersicht_des_vergleichs_staging

---

### agi_av_gwr_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_gwr_abgleich_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_av_gwr_abgleich_import_v1.av_gwr_differnzen_av_gwr_differenzen
- agi_av_gwr_abgleich_pub_v1.av_gwr_differnzen_av_gwr_differenzen
- agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen
- agi_gebaeudeinformationen_pub_v1.gebaeude_gebaeude

**Ziel-Tabellen:**
- agi_av_gwr_abgleich_pub_v1.av_gwr_differnzen_av_gwr_differenzen
- agi_av_gwr_abgleich_v1.av_gwr_differnzen_av_gwr_differenzen

---

### agi_av_kaso_abgleich_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_kaso_abgleich_pub`
**Schedule:** `H 3 * * *` (~3:xx)

**Quell-Tabellen:**
- agi_av_gb_administrative_einteilungen_v2.grundbuchkreise_grundbuchkreis
- agi_av_kaso_abgleich_v1.differenzen_staging
- agi_av_kaso_abgleich_v1.kaso_daten
- agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_grundstuecksart
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_dm01avso24.liegenschaften_selbstrecht
- agi_dm01avso24.t_ili2db_basket
- agi_dm01avso24.t_ili2db_import
- sogis_av_kaso_abgleich

**Ziel-Tabellen:**
- agi_av_kaso_abgleich_v1.differenzen_staging
- agi_av_kaso_abgleich_v1.uebersicht_des_vergleichs_staging

---

### agi_av_meldewesen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_meldewesen`
**Schedule:** `H H(3-4) * * *` (~3-4h)

**Quell-Tabellen:**
- agi_av_meldewesen_import_v1.meldungen_meldung
- agi_av_meldewesen_work_v1.meldungen_meldung
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_dm01avso24.liegenschaften_bergwerk
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_selbstrecht

**Ziel-Tabellen:**
- agi_av_meldewesen_work_v1.meldungen_meldung

---

### agi_av_mocheckso

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_av_mocheckso`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_av_mocheckso.mocheckso_errors_mocheckso_error

---

### agi_ch_gemeinden

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_ch_gemeinden`
**Schedule:** `H H(1-3) 1 2 *` (1. ~1-3h)

**Quell-Tabellen:**
- agi_swissboundaries3d_pub.swissboundaries3d_bezirk
- agi_swissboundaries3d_pub.swissboundaries3d_hoheitsgebiet
- agi_swissboundaries3d_pub.swissboundaries3d_kanton
- agi_swissboundaries3d_pub.swissboundaries3d_land
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_bezirksgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_hoheitsgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_kantonsgebiet
- agi_swissboundaries3d_v1.tlm_grenzen_tlm_landesgebiet
- agi_swissboundaries3d_v2.multisurface3d
- agi_swissboundaries3d_v2.surface3d
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_bezirksgebiet
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_hoheitsgebiet
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_kantonsgebiet
- agi_swissboundaries3d_v2.tlm_grenzen_tlm_landesgebiet

---

### agi_dmav_fixpunkte2_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_fixpunkte2_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_dmav_fixpunktelv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_fixpunktelv_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_dmav_hoheitsgrenzen_lv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_hoheitsgrenzen_lv_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_dmav_hoheitsgrenzpunkte_lv_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_hoheitsgrenzpunkte_lv_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_dmav_plz_ortschaft_import

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_dmav_plz_ortschaft_import`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### agi_gb2av_controlling

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_gb2av_controlling`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_av_gb_administrative_einteilungen_v2.nachfuehrngskrise_gemeinde
- agi_av_gb_administrative_einteilungen_v2.nachfuehrngskrise_standort
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projbergwerk
- agi_dm01avso24.liegenschaften_projgrundstueck
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_dm01avso24.liegenschaften_projselbstrecht
- agi_gb2av.mutationsnummer
- agi_gb2av.mutationstabelle_avmutation
- agi_gb2av.vollzugsgegnstnde_vollzugsgegenstand
- agi_gb2av_controlling.controlling_av2gb_mutationen
- agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta
- mit

**Ziel-Tabellen:**
- SET
- agi_gb2av_controlling.controlling_av2gb_mutationen
- agi_gb2av_controlling.controlling_gb2av_vollzugsmeldung_delta

---

### agi_generate_matomo_reports

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_generate_matomo_reports`
**Schedule:** `H 4 1 * *` (1. ~4:xx)

---

### agi_gwr_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_gwr_pub`
**Schedule:** `H H(3-4) * * *` (~3-4h)

**Quell-Tabellen:**
- agi_gwr_v1.gwr_codes
- agi_gwr_v1.gwr_gebaeude
- agi_gwr_v1.gwr_wohnung
- building
- codes
- dwelling

---

### agi_hoheitsgrenzen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_hoheitsgrenzen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.gemeindegrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksname_a3
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksname_a4
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindename_a3
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindename_a4
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsname_a3
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsname_a4
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirksname_pos
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeinde
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeindename_pos
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_kanton
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_kantonsname_pos

**Ziel-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze_generalisiert
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze_generalisiert

---

### agi_kartenkatalog

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_kartenkatalog`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_kartenkatalog_v2.kartenkatalog_ebene
- agi_kartenkatalog_v2.kartenkatalog_thema
- simi.simidata_data_set_view
- simi.simidata_postgres_table
- simi.simidata_table_view
- simi.simiiam_permission
- simi.simiiam_role
- simi.simiproduct_data_product
- simi.simiproduct_data_product_pub_scope
- simi.simiproduct_layer_group
- simi.simiproduct_properties_in_list
- simi.simiproduct_single_actor
- simi.simitheme_org_unit
- simi.simitheme_theme
- simi.simitheme_theme_publication

---

### agi_kartenkatalog_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_kartenkatalog_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- simi.simidata_data_set_view
- simi.simidata_postgres_table
- simi.simidata_table_view
- simi.simiiam_permission
- simi.simiiam_role
- simi.simiproduct_data_product
- simi.simiproduct_data_product_pub_scope
- simi.simiproduct_layer_group
- simi.simiproduct_properties_in_list
- simi.simiproduct_single_actor
- simi.simitheme_org_unit
- simi.simitheme_theme
- simi.simitheme_theme_publication

---

### agi_stac

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_stac`
**Schedule:** `H H(5-6) * * *` (~5-6h)

---

### agi_swisstopo_gebaeudeadressen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/agi_swisstopo_gebaeudeadressen`
**Schedule:** `H H(1-3) 2 * *` (2. ~1-3h)

**Quell-Tabellen:**
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_address
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_stn
- agi_swisstopo_gebaeudeadressen_v1.officlndxfddrsses_zip

---

### alw_landwirtschaft_tierhaltung_import_bodenbedeckung

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_import_bodenbedeckung`
**Schedule:** `H H(3-4) * * 5` (Fr ~3-4h)

---

### alw_landwirtschaft_tierhaltung_import_massnahmen

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_import_massnahmen`
**Schedule:** `H H(3-4) 1 * *` (1. ~3-4h)

---

### alw_landwirtschaft_tierhaltung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_landwirtschaft_tierhaltung_pub`
**Schedule:** `H H(2-4) * * *` (~2-4h)

**Quell-Tabellen:**
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_betrieb
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_bewirtschaftungseinheit
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_gelan_person
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_kultur_flaechen
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_kultur_punktelemente
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_standorte
- alw_landwirtschaft_tierhaltung_v1.betrbsdttrktrdten_summe_tiere_flaechen
- alw_landwirtschaft_tierhaltung_v1.bff_qualitaet_bff_qualitaet
- alw_landwirtschaft_tierhaltung_v1.t_ili2db_basket
- alw_landwirtschaft_tierhaltung_v1.t_ili2db_dataset

---

### alw_strukturverbesserungen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_strukturverbesserungen_pub`
**Schedule:** `H H(1-3) * * 6` (Sa ~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- alw_strukturverbesserungen.astatus
- alw_strukturverbesserungen.bautyp
- alw_strukturverbesserungen.beizugsgebiete
- alw_strukturverbesserungen.bewaesserung_flaechen
- alw_strukturverbesserungen.bewaesserung_linien
- alw_strukturverbesserungen.bewaesserung_punkte
- alw_strukturverbesserungen.elektrizitaet_linien
- alw_strukturverbesserungen.elektrizitaet_punkte
- alw_strukturverbesserungen.entw_bodenstruktur_flaechen
- alw_strukturverbesserungen.entw_bodenstruktur_linien
- alw_strukturverbesserungen.funktionstyp
- alw_strukturverbesserungen.genossenschaften
- alw_strukturverbesserungen.oekologie_linien
- alw_strukturverbesserungen.oekologie_punkte
- alw_strukturverbesserungen.oekologie_trockenmauern
- alw_strukturverbesserungen.oekologische_flaechen
- alw_strukturverbesserungen.projekt
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet_projekt
- alw_strukturverbesserungen.raeumlicheelemnte_bew_flaechen_bewaesserung
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_linie
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_flaeche
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_linie
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_pumpwerk
- alw_strukturverbesserungen.raeumlicheelemnte_ev_linie
- alw_strukturverbesserungen.raeumlicheelemnte_ev_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_gemeinde_flurreglement
- alw_strukturverbesserungen.raeumlicheelemnte_gemeinde_flurreglement_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_genossenschaft_element
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_flaeche
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_linie
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_trockenmauer
- alw_strukturverbesserungen.raeumlicheelemnte_projekt
- alw_strukturverbesserungen.raeumlicheelemnte_raeumliches_element_dokument
- alw_strukturverbesserungen.raeumlicheelemnte_wasserversorgung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_wege_bruecke_lehnenviadukt
- alw_strukturverbesserungen.raeumlicheelemnte_wegebau_linie
- alw_strukturverbesserungen.raeumlicheelemnte_werkeigentum
- alw_strukturverbesserungen.raeumlicheelemnte_wiederherstellung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_wv_leitung_wasserversorgung
- alw_strukturverbesserungen.raeumlichelmnte_wege_bruecke_lehnenviadukt_material
- alw_strukturverbesserungen.stand
- alw_strukturverbesserungen.stand_gutrrglrung_stand_gueterregulierung
- alw_strukturverbesserungen.wasserversorgung_punkte
- alw_strukturverbesserungen.wege
- alw_strukturverbesserungen.wiederherstellung_punkte

---

### alw_tiergesundheit_pflanzengesundheit_massnahmen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/alw_tiergesundheit_pflanzengesundheit_massnahmen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_bienensperrgebiet
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_pflanzengesundheit_schadorganismen
- alw_tiergesundheit_pflanzengesundheit_massnahmen_v1.massnhmnngsndheit_tiergesundheit_massnahmengebiet

---

### amb_zivilschutz_adressen_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/amb_zivilschutz_adressen_export`
**Schedule:** `H H(1-3) 1 * *` (1. ~1-3h)

**Quell-Tabellen:**
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_mopublic_pub.mopublic_einzelobjekt_flaeche
- agi_mopublic_pub.mopublic_gebaeudeadresse
- agi_mopublic_pub.mopublic_gemeindegrenze
- agi_mopublic_pub.mopublic_grundstueck
- agi_mopublic_pub.mopublic_objektname_pos
- agi_swisstopo_gebaeudeadressen_pub_v1.gebaeudeadressen_adresse
- amb_zivilschutz_adressen_staging_pub.adressen_zivilschutz

**Ziel-Tabellen:**
- amb_zivilschutz_adressen_staging_pub.adressen_zivilschutz

---

### arp_agglomerationsprogramme_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_agglomerationsprogramme_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_swissboundaries3d_pub.swissboundaries3d_hoheitsgebiet
- arp_agglomerationsprogramme.agglomrtnsprgrmme_agglo_line
- arp_agglomerationsprogramme.agglomrtnsprgrmme_agglo_point
- arp_agglomerationsprogramme.agglomrtnsprgrmme_agglo_surface
- arp_agglomerationsprogramme.agglomrtnsprgrmme_agglomerationsprogramm
- arp_agglomerationsprogramme.agglomrtnsprgrmme_federfuehrung
- arp_agglomerationsprogramme.agglomrtnsprgrmme_federfuehrung_massnahme
- arp_agglomerationsprogramme.agglomrtnsprgrmme_gemeinde
- arp_agglomerationsprogramme.agglomrtnsprgrmme_gemeinde_massnahme
- arp_agglomerationsprogramme.agglomrtnsprgrmme_massnahme
- arp_agglomerationsprogramme.agglomrtnsprgrmme_paket
- arp_agglomerationsprogramme.agglomrtnsprgrmme_prioritaet
- arp_agglomerationsprogramme.agglomrtnsprgrmme_projektphase
- arp_agglomerationsprogramme.agglomrtnsprgrmme_umsetzungsstand

---

### arp_arbeitszonenbewirtschaftung_inventar_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_arbeitszonenbewirtschaftung_inventar_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_mopublic_pub.mopublic_grundstueck
- arp_arbeitszonenbewirtschaftung_pub_v2.region_region
- arp_arbeitszonenbewirtschaftung_staging_v2.arbtszng_nvntar_arbeitszonenbewirtschaftung_inventar_bebtand
- arp_arbeitszonenbewirtschaftung_staging_v2.inventar_flaeche_v
- arp_arbeitszonenbewirtschaftung_v2.regionen_region
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_und_lsgrenzen
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- mit

**Ziel-Tabellen:**
- arp_arbeitszonenbewirtschaftung_staging_v2.arbtsznnng_nvntar_arbeitszonenbewirtschaftung_inventar
- arp_arbeitszonenbewirtschaftung_v2.bewertung_bewertung

---

### arp_auswertung_nutzungsplanung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_auswertung_nutzungsplanung_pub`
**Schedule:** `H H(1-3) 31 1,3,4,7,8,10,12 *\nH H(1-3) 30 4,6,9,11 *\nH H(1-3) 28,29 2 *` (~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_mopublic_pub.mopublic_einzelobjekt_flaeche
- agi_mopublic_pub.mopublic_grundstueck
- arp_auswertung_nutzungsplanung_pub_v1.auswrtngtzngsznen_grundnutzungszone_aggregiert_pro_gemeinde
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_ohne_lsgrenzen
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_mit_zonen_und_lsgrenzen
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_bebauungsstand_pro_gemeinde
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_gines
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- original

---

### arp_bauzonengrenzen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_bauzonengrenzen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

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
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- arp_fledermaus_v1.fledermausfundrte_fledermausfundort

---

### arp_mjpnatur_gelan_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnatur_gelan_export`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen
- arp_mjpnl_v2.mjpnl_beurteilung_hostet
- arp_mjpnl_v2.mjpnl_vereinbarung

**Ziel-Tabellen:**
- arp_mjpnl_gelan_v1.mehrjahresprgramm_vereinbarungensflaechen

---

### arp_mjpnatur_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnatur_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- arp_mjpnl_v2.betrbsdttrktrdten_gelan_person
- arp_mjpnl_v2.mjpnl_beurteilung_alr_buntbrache
- arp_mjpnl_v2.mjpnl_beurteilung_alr_saum
- arp_mjpnl_v2.mjpnl_beurteilung_hecke
- arp_mjpnl_v2.mjpnl_beurteilung_hostet
- arp_mjpnl_v2.mjpnl_beurteilung_obl
- arp_mjpnl_v2.mjpnl_beurteilung_wbl_weide
- arp_mjpnl_v2.mjpnl_beurteilung_wbl_wiese
- arp_mjpnl_v2.mjpnl_beurteilung_weide_ln
- arp_mjpnl_v2.mjpnl_beurteilung_weide_soeg
- arp_mjpnl_v2.mjpnl_beurteilung_wiese
- arp_mjpnl_v2.mjpnl_vereinbarung

---

### arp_mjpnl_v2_auszahlung

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnl_v2_auszahlung`
**Schedule:** `H H(1-3) 15 1 *` (15. ~1-3h)

---

### arp_mjpnl_v2_zahlungslauf

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_mjpnl_v2_zahlungslauf`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_bezirk
- agi_hoheitsgrenzen_v1.hoheitsgrenzen_gemeinde

**Ziel-Tabellen:**
- abrechnung_per_leistung
- der

---

### arp_nutzungsplanung_planregister_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_nutzungsplanung_planregister_export`
**Schedule:** `H H(1-3) * * *` (~1-3h)

---

### arp_nutzungsvereinbarung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_nutzungsvereinbarung_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.nomenklatur_flurname
- arp_mehrjahresprogramm.mehrjahresprgramm_person
- arp_nutzungsvereinbarung.nutzungsvrnbrngen_nutzungsvereinbarungen
- arp_nutzungsvereinbarung.nutzungsvrnbrngen_projekte

---

### arp_richtplan_grundnutzung_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_richtplan_grundnutzung_pub`
**Schedule:** `H H(1-3) 1 * *` (1. ~1-3h)

**Quell-Tabellen:**
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_richtplan_pub_v2.richtplankarte_grundnutzung

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_grundnutzung

---

### arp_sein_konfiguration

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_sein_konfiguration`
**Schedule:** `H 4 31 1,3,4,7,8,10,12 *\nH 4 30 4,6,9,11 *\nH 4 28,29 2 *` (~4:xx)

**Quell-Tabellen:**
- ST_Read
- Shapefile
- arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gemeinde
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gemeinde_objektinfo
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gruppe
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_objektinfo
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_thema
- importschema_xtf.geometrie
- importschema_xtf.geometrie_linie
- importschema_xtf.geometrie_perimeter
- importschema_xtf.geometrie_punkt
- importschema_xtf.geometriekollektion
- importschema_xtf.hinweis
- importschema_xtf.hinweisortsbildteil
- importschema_xtf.ivs_linienobjekte_lv95
- importschema_xtf.ivs_objekte
- importschema_xtf.ivs_slanamen
- main.
- main.sein_sammeltabelle
- main.sein_sammeltabelle_filtered
- pubdb.ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- pubdb.ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- pubdb.afu_altlasten_pub_v2.belasteter_standort
- pubdb.afu_stoerfallverordnung_pub_v1.betrieb
- pubdb.afu_stoerfallverordnung_pub_v1.betrieb_kb
- pubdb.afu_stoerfallverordnung_pub_v1.durchgangsstrasse
- pubdb.afu_stoerfallverordnung_pub_v1.durchgangsstrasse_kb
- pubdb.afu_stoerfallverordnung_pub_v1.erdgasroehrenspeicher
- pubdb.afu_stoerfallverordnung_pub_v1.erdgasroehrenspeicher_kb
- pubdb.afu_stoerfallverordnung_pub_v1.nationalstrasse
- pubdb.afu_stoerfallverordnung_pub_v1.nationalstrasse_kb
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_flaeche
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_linie
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_punkt
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_uebersicht_gemeinde
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernder_punkt
- pubdb.awjf_wildtierkorridore_pub_v1.wildtierkorridor
- read_parquet
- sein.arp_sein_konfiguration_grundlagen_v2.gemeinde_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115auswertung_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gruppe
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_thema
- sein.main.sein_sammeltabelle
- sein.main.sein_sammeltabelle_filtered
- sein_sammeltabelle
- sein_sammeltabelle_filtered

**Ziel-Tabellen:**
- Sammeltabelle
- for
- main.sein_sammeltabelle_filtered
- sein.arp_sein_konfiguration_grundlagen_v2.gemeinde_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115auswertung_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gruppe
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_thema
- sein.main.sein_sammeltabelle
- sein.main.sein_sammeltabelle_filtered
- sein_sammeltabelle
- sein_sammeltabelle_filtered

---

### arp_sein_strukturdaten_export

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/arp_sein_strukturdaten_export`
**Schedule:** `H 4 31 1,3,4,7,8,10,12 *\nH 4 30 4,6,9,11 *\nH 4 28,29 2 *` (~4:xx)

**Quell-Tabellen:**
- Parzelle
- agi_gwr_pub_v1.gwr_gebaeude
- agi_gwr_pub_v1.gwr_wohnung
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_grundstueck
- arp_auswertung_nutzungsplanung_pub_v1.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_sein_konfiguration_grundlagen_v2.grundlagen_gemeinde
- arp_statpop_statent_v1.statent
- arp_statpop_statent_v1.statpop
- export.gebaeude
- export.gebklasse10_mapping
- export.gemeinde_bodenbedeckung
- export.gemeinde_bodenbedeckungen_json
- export.gemeinde_gebaeude_statistik
- export.gemeinde_geoms
- export.gemeinde_grundnutzungen_json
- export.gemeinde_gwr_json
- export.gemeinde_statent_statistik
- export.gemeinde_statpop_json
- export.gemeinde_wohnungen_statistik
- export.parzellen_bodenbedeckung
- export.parzellen_bodenbedeckungen_json
- export.parzellen_gebaeude_statistik
- export.parzellen_geoms
- export.parzellen_grundnutzungen_json
- export.parzellen_gwr_json
- export.parzellen_statent_statistik
- export.parzellen_statpop_json
- export.parzellen_wohnungen_statistik
- export.statent
- export.statpop
- export.strukturdaten_gemeinde
- export.strukturdaten_parzelle
- export.strukturdaten_zonenschild
- export.strukturdaten_zonentyp
- export.wohnung
- export.zonenschild_bodenbedeckung
- export.zonenschild_bodenbedeckungen_json
- export.zonenschild_gebaeude_statistik
- export.zonenschild_geoms
- export.zonenschild_grundnutzungen_json
- export.zonenschild_gwr_json
- export.zonenschild_statent_statistik
- export.zonenschild_statpop_json
- export.zonenschild_wohnungen_statistik
- export.zonentyp_bodenbedeckung
- export.zonentyp_bodenbedeckungen_json
- export.zonentyp_dump
- export.zonentyp_gebaeude_statistik
- export.zonentyp_geoms
- export.zonentyp_grundnutzungen_json
- export.zonentyp_gwr_json
- export.zonentyp_statent_statistik
- export.zonentyp_statpop_json
- export.zonentyp_wohnungen_statistik
- import.bauzonenstatistik_liegenschaft_nach_bebauungsstand
- import.grundlagen_gemeinde
- import.gwr_gebaeude
- import.gwr_wohnung
- import.hoheitsgrenzen_gemeindegrenze
- import.mopublic_bodenbedeckung
- import.nutzungsplanung_grundnutzung
- import.statpop_statent_statent
- import.statpop_statent_statpop
- verwendet

**Ziel-Tabellen:**
- export.gebaeude
- export.gebklasse10_mapping
- export.gemeinde_bodenbedeckung
- export.gemeinde_bodenbedeckungen_json
- export.gemeinde_gebaeude_statistik
- export.gemeinde_geoms
- export.gemeinde_grundnutzungen_json
- export.gemeinde_gwr_json
- export.gemeinde_statent_statistik
- export.gemeinde_statpop_json
- export.gemeinde_wohnungen_statistik
- export.parzellen_bodenbedeckung
- export.parzellen_bodenbedeckungen_json
- export.parzellen_gebaeude_statistik
- export.parzellen_geoms
- export.parzellen_grundnutzungen_json
- export.parzellen_gwr_json
- export.parzellen_statent_statistik
- export.parzellen_statpop_json
- export.parzellen_wohnungen_statistik
- export.statent
- export.statpop
- export.strukturdaten_gemeinde
- export.strukturdaten_parzelle
- export.strukturdaten_zonenschild
- export.strukturdaten_zonentyp
- export.wohnung
- export.zonenschild_bodenbedeckung
- export.zonenschild_bodenbedeckungen_json
- export.zonenschild_gebaeude_statistik
- export.zonenschild_geoms
- export.zonenschild_grundnutzungen_json
- export.zonenschild_gwr_json
- export.zonenschild_statent_statistik
- export.zonenschild_statpop_json
- export.zonenschild_wohnungen_statistik
- export.zonentyp_bodenbedeckung
- export.zonentyp_bodenbedeckungen_json
- export.zonentyp_dump
- export.zonentyp_gebaeude_statistik
- export.zonentyp_geoms
- export.zonentyp_grundnutzungen_json
- export.zonentyp_gwr_json
- export.zonentyp_statent_statistik
- export.zonentyp_statpop_json
- export.zonentyp_wohnungen_statistik

---

### avt_bodenfaktor_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/avt_bodenfaktor_pub`
**Schedule:** `H H(2-5) * * 0` (So ~2-5h)

**Quell-Tabellen:**
- agi_dm01avso24.bodenbedeckung_boflaeche
- avt_bodenfaktor.bodenfaktor
- avt_bodenfaktor.t_ili2db_basket
- avt_bodenfaktor.t_ili2db_dataset

**Ziel-Tabellen:**
- avt_bodenfaktor.bodenfaktor

---

### awjf_efj

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_efj`
**Schedule:** `H H(4-5) * * *` (~4-5h)

**Quell-Tabellen:**
- LATERAL
- awjf_efj_v1.efj_abgaenge

---

### awjf_forstreviere_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_forstreviere_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- awjf_forstreviere.forstreviere_forstkreis
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie

---

### awjf_programm_biodiversitaet_wald_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_programm_biodiversitaet_wald_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.nomenklatur_flurname
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_swissboundaries3d_pub.swissboundaries3d_hoheitsgebiet
- awjf.wap_bst
- awjf_forstreviere.forstreviere_forstkreis
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_baumartenvielfalt
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotop_zielgruppe
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotopbaum
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_foto
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_waldbiodiversitaetsflaeche
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_zielgruppe
- awjf_waldstandorte_v1.waldstandort
- string_agg

---

### awjf_rodung_rodungsersatz_mgdm

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_rodung_rodungsersatz_mgdm`
**Schedule:** `H H(1-3) 1 3 *` (1. ~1-3h)

**Quell-Tabellen:**
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzmassnahmennl_
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_
- awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_
- awjf_rodung_rodungsersatz_mgdm_v1.objekt
- awjf_rodung_rodungsersatz_mgdm_v1.rodungsbewilligung
- awjf_rodung_rodungsersatz_mgdm_v1.uri_
- awjf_rodung_rodungsersatz_v1.ausgleichsabgabe
- awjf_rodung_rodungsersatz_v1.dokument
- awjf_rodung_rodungsersatz_v1.flaeche
- awjf_rodung_rodungsersatz_v1.rodung_dokument
- awjf_rodung_rodungsersatz_v1.rodungsdaten

**Ziel-Tabellen:**
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzmassnahmennl_
- awjf_rodung_rodungsersatz_mgdm_v1.ersatzverzicht_
- awjf_rodung_rodungsersatz_mgdm_v1.massnahmenltyp_
- awjf_rodung_rodungsersatz_mgdm_v1.objekt
- awjf_rodung_rodungsersatz_mgdm_v1.rodungsbewilligung

---

### awjf_schutzwald_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_schutzwald_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- awjf_schutzwald_pub_v1.behandelte_flaeche_massnahme
- awjf_schutzwald_pub_v1.behandelte_flaeche_status
- awjf_schutzwald_pub_v1.nais_code
- awjf_schutzwald_pub_v1.schutzwald_hauptgefahrenpotential
- awjf_schutzwald_pub_v1.schutzwald_info_zieltyp
- awjf_schutzwald_pub_v1.schutzwald_intensitaet_geschaetzt
- awjf_schutzwald_pub_v1.schutzwald_objektkategorie
- awjf_schutzwald_v1.behandelte_flaeche
- awjf_schutzwald_v1.dokument
- awjf_schutzwald_v1.schutzwald
- awjf_schutzwald_v1.schutzwald_info

**Ziel-Tabellen:**
- awjf_schutzwald_pub_v1.behandelte_flaeche
- awjf_schutzwald_pub_v1.dokument
- awjf_schutzwald_pub_v1.schutzwald
- awjf_schutzwald_pub_v1.schutzwald_info

---

### awjf_waldpflege_kontrolle

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_waldpflege_kontrolle`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- awjf_gesuchsteller.gesuchsteller_gesuchsteller
- awjf_waldpflege_erfassung.waldpflege_waldpflege

---

### awjf_wegsanierungen_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/awjf_wegsanierungen_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- awjf_wegsanierungen_v1.wegsanierungen_wegsanierung

---

### dsbjd_ausgleichsabgabe_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/dsbjd_ausgleichsabgabe_pub`
**Schedule:** `H H(1-3) * * *` (~1-3h)

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- dsbjd_ausgleichsabgabe_v1.ausgleichsabgaben_ausgleichsabgabe

---

### dsbjd_ebauso_rahmenmodell_pub

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/dsbjd_ebauso_rahmenmodell_pub`
**Schedule:** `H H(3-4) * * *` (~3-4h)

**Quell-Tabellen:**
- ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- ada_denkmalschutz_pub_v1.denkmal_polygon
- ada_denkmalschutz_pub_v1.denkmal_punkt
- afu_naturgefahren_pub_v2.synoptisches_gefahrengebiet
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_gebaeudeadresse
- agi_mopublic_pub.mopublic_grundstueck
- alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_pub_v1.nutzungsplanung_ueberlagernd_punkt
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_polygon
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_punkt
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_gebaeudeeingang
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_grundstueck
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_polygon
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_punkt
- live.oerbkrmfr_v2_0transferstruktur_eigentumsbeschraenkung
- live.oerbkrmfr_v2_0transferstruktur_geometrie
- live.oerbkrmfr_v2_0transferstruktur_legendeeintrag

**Ziel-Tabellen:**
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_polygon
- dsbjd_ebauso_rahmenmodell_pub_v1.fachthemen_fachthema_punkt
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_gebaeudeeingang
- dsbjd_ebauso_rahmenmodell_pub_v1.lokalisation_grundstueck
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_linie
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_polygon
- dsbjd_ebauso_rahmenmodell_stage_v1.fachthemen_fachthema_punkt

---

### sgv_schadenkarte

**Status:** Aktiv
**Trigger:** cron
**Pfad:** `../gretljobs/sgv_schadenkarte`
**Schedule:** `H H(6-7) * * *` (~6-7h)

**Quell-Tabellen:**
- LATERAL
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_gebaeudeinformationen_pub_v1.gebaeude_gebaeude
- agi_gwr_pub_v1.gwr_gebaeude
- agi_mopublic_pub.mopublic_grundstueck
- sgv_schadenkarte_v1.schadenfall

**Ziel-Tabellen:**
- sgv_schadenkarte_pub_v1.schadenfall
- wo

---

### ada_denkmalschutz_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/ada_denkmalschutz_pub`
**Upstream:** oerebv2_einzelschutz_denkmal

**Quell-Tabellen:**
- ada_denkmalschutz_v1.fachapplikation_denkmal
- ada_denkmalschutz_v1.gis_geometrie
- ada_denkmalschutz_v1.oereb_doclink_v

---

### afu_bodendaten_nabodat_abfrage_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/afu_bodendaten_nabodat_abfrage_pub`
**Upstream:** afu_bodenprofilstandorte_nabodat_pub

**Quell-Tabellen:**
- afu_bodendaten_nabodat_abfrage_pub_v1.bodenprofil
- afu_bodendaten_nabodat_pub.bodenproflstndrte_bodenprofilstandort
- afu_bodendaten_nabodat_v1.codelistnnlysdten_analyseparameter
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodentyp
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodenwasserhaushaltsgruppe
- afu_bodendaten_nabodat_v1.codelistnprfldten_eignungsklasse
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtontext
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtonzahl
- afu_bodendaten_nabodat_v1.codelistnprfldten_feinerdekoernung
- afu_bodendaten_nabodat_v1.codelistnprfldten_form
- afu_bodendaten_nabodat_v1.codelistnprfldten_fruchtbarkeitsstufe
- afu_bodendaten_nabodat_v1.codelistnprfldten_groesse
- afu_bodendaten_nabodat_v1.codelistnprfldten_helligkeit
- afu_bodendaten_nabodat_v1.codelistnprfldten_intensitaet
- afu_bodendaten_nabodat_v1.codelistnprfldten_kalkreaktionhcl
- afu_bodendaten_nabodat_v1.codelistnprfldten_klassifikationssystem
- afu_bodendaten_nabodat_v1.codelistnprfldten_nutzungseignung
- afu_bodendaten_nabodat_v1.codelistnprfldten_pflanzennutzbaregruendigkeit
- afu_bodendaten_nabodat_v1.codelistnprfldten_skelettgehalt
- afu_bodendaten_nabodat_v1.codelistnprfldten_untertyp
- afu_bodendaten_nabodat_v1.codelistnprfldten_wasserspeichervermoegen
- afu_bodendaten_nabodat_v1.codlstnpktstndort_ausgangsmaterial
- afu_bodendaten_nabodat_v1.codlstnpktstndort_dokumenttyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_einsatzduengerfest
- afu_bodendaten_nabodat_v1.codlstnpktstndort_eiszeit
- afu_bodendaten_nabodat_v1.codlstnpktstndort_erhebungsart
- afu_bodendaten_nabodat_v1.codlstnpktstndort_exposition
- afu_bodendaten_nabodat_v1.codlstnpktstndort_gelaendeform
- afu_bodendaten_nabodat_v1.codlstnpktstndort_humusform
- afu_bodendaten_nabodat_v1.codlstnpktstndort_kleinrelief
- afu_bodendaten_nabodat_v1.codlstnpktstndort_klimaeignungszone
- afu_bodendaten_nabodat_v1.codlstnpktstndort_krumenzustand
- afu_bodendaten_nabodat_v1.codlstnpktstndort_landschaftselement
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_produktionsfaehigkstufewald
- afu_bodendaten_nabodat_v1.codlstnpktstndort_risikoduengerfluess
- afu_bodendaten_nabodat_v1.codlstnpktstndort_vegetation
- afu_bodendaten_nabodat_v1.erhebung_probe_profil_v
- afu_bodendaten_nabodat_v1.punktdaten_ausgangsmaterial
- afu_bodendaten_nabodat_v1.punktdaten_bichqualitaet
- afu_bodendaten_nabodat_v1.punktdaten_bodenfarbe
- afu_bodendaten_nabodat_v1.punktdaten_bodenskelettfeldbereich
- afu_bodendaten_nabodat_v1.punktdaten_dokument
- afu_bodendaten_nabodat_v1.punktdaten_erhebung
- afu_bodendaten_nabodat_v1.punktdaten_gefuege
- afu_bodendaten_nabodat_v1.punktdaten_horizont
- afu_bodendaten_nabodat_v1.punktdaten_horizontbezeichnung
- afu_bodendaten_nabodat_v1.punktdaten_koernungsbereich
- afu_bodendaten_nabodat_v1.punktdaten_messung
- afu_bodendaten_nabodat_v1.punktdaten_probe
- afu_bodendaten_nabodat_v1.punktdaten_profil
- afu_bodendaten_nabodat_v1.punktdaten_profilbeurteilung
- afu_bodendaten_nabodat_v1.punktdaten_profildokument
- afu_bodendaten_nabodat_v1.punktdaten_projekt
- afu_bodendaten_nabodat_v1.punktdaten_projektstandort
- afu_bodendaten_nabodat_v1.punktdaten_standort
- afu_bodendaten_nabodat_v1.punktdaten_standortbeurteilung
- afu_bodendaten_nabodat_v1.punktdaten_standorteigenschaften
- afu_bodendaten_nabodat_v1.punktdaten_untertyp
- afu_bodendaten_nabodat_v1.punktdaten_wald
- mit

**Ziel-Tabellen:**
- afu_bodendaten_nabodat_abfrage_pub_v1.bodenprofil
- afu_bodendaten_nabodat_abfrage_pub_v1.horizont

---

### afu_geotope_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/afu_geotope_pub`
**Upstream:** oereb_einzelschutz_geotop

**Quell-Tabellen:**
- afu_geotope.geotope_aufschluss
- afu_geotope.geotope_aufschluss_dokument
- afu_geotope.geotope_aufschluss_fachbereich
- afu_geotope.geotope_dokument
- afu_geotope.geotope_erratiker
- afu_geotope.geotope_erratiker_dokument
- afu_geotope.geotope_erratiker_fachbereich
- afu_geotope.geotope_fachbereich
- afu_geotope.geotope_fundstelle_grabung
- afu_geotope.geotope_fundstelle_grabung_dokument
- afu_geotope.geotope_fundstelle_grabung_fachbereich
- afu_geotope.geotope_hoehle
- afu_geotope.geotope_hoehle_dokument
- afu_geotope.geotope_hoehle_fachbereich
- afu_geotope.geotope_landform_dokument
- afu_geotope.geotope_landform_fachbereich
- afu_geotope.geotope_landschaftsform
- afu_geotope.geotope_quelle
- afu_geotope.geotope_quelle_dokument
- afu_geotope.geotope_quelle_fachbereich
- afu_geotope.geotope_zustaendige_stelle
- afu_geotope.lithostratigrphie_geologische_schicht
- afu_geotope.lithostratigrphie_geologische_serie
- afu_geotope.lithostratigrphie_geologische_stufe
- afu_geotope.lithostratigrphie_geologisches_system
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_plz_ortschaften.plzortschaft_ortschaft
- agi_plz_ortschaften.plzortschaft_ortschaftsname
- arp_naturreservate.reservate_teilgebiet
- arp_richtplan_v2.richtplankarte_ueberlagernde_flaeche

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
- agi_gwr_pub_v1.gwr_gebaeude
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_bodenbedeckung_proj
- agi_mopublic_pub.mopublic_gebaeudeadresse
- agi_mopublic_pub.mopublic_objektname_pos

---

### agi_grundbuchplan_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/agi_grundbuchplan_pub`
**Upstream:** agi_av_dm01_mopublic_pub

**Quell-Tabellen:**
- agi_av_gb_admin_einteilung_pub.grundbuchkreise_grundbuchkreis
- agi_av_gb_admin_einteilung_pub.nachfuehrngskrise_gemeinde
- agi_dm01avso24.bodenbedeckung_boflaeche
- agi_dm01avso24.bodenbedeckung_boflaechesymbol
- agi_dm01avso24.liegenschaften_grenzpunkt
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_grundstueckpos
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_lsnachfuehrung
- agi_dm01avso24.liegenschaften_projliegenschaft
- agi_grundbuchplan_pub.grundbuchplan_grundstueckpos
- agi_grundbuchplan_pub.grundbuchplan_liegenschaft
- agi_mopublic_pub.mopublic_gemeindegrenze

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
- alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

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
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

**Ziel-Tabellen:**
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

---

### arp_richtplan_naturreservate_pub

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/arp_richtplan_naturreservate_pub`
**Upstream:** arp_naturreservate_pub

**Quell-Tabellen:**
- arp_naturreservate_pub.naturreservate_reservat
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche

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

### awjf_efj_geodaten_upload

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/awjf_efj_geodaten_upload`
**Upstream:** awjf_jagdreviere_jagdbanngebiete_pub, awjf_gewaesser_fischerei_pub

**Quell-Tabellen:**
- afu_gewaesser_v1.fischrevierabschnitt_v
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- awjf_efj_geodaten_upload_v1.gebiete_gebiet
- awjf_jagdreviere_jagdbanngebiete_v1.jagdreviere_jagdreviere

**Ziel-Tabellen:**
- awjf_efj_geodaten_upload_v1.gebiete_gebiet
- awjf_efj_geodaten_upload_v1.transfermetadaten_datenbestand

---

### awjf_statische_waldgrenzen_export_ai

**Status:** Aktiv
**Trigger:** upstream
**Pfad:** `../gretljobs/awjf_statische_waldgrenzen_export_ai`
**Upstream:** awjf_statische_waldgrenze_pub

**Quell-Tabellen:**
- awjf_statische_waldgrenze.dokumente_dokument
- awjf_statische_waldgrenze.geobasisdaten_typ
- awjf_statische_waldgrenze.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_geometrie_dokument
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ_dokument
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.localiseduri
- awjf_statische_waldgrenze_mgdm_v1.multilingualuri
- awjf_statische_waldgrenze_mgdm_v1.rechtsstatus
- awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument
- awjf_statische_waldgrenze_mgdm_v1.t_ili2db_basket

**Ziel-Tabellen:**
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_typ
- awjf_statische_waldgrenze_mgdm_v1.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_mgdm_v1.localiseduri
- awjf_statische_waldgrenze_mgdm_v1.multilingualuri
- awjf_statische_waldgrenze_mgdm_v1.rechtsvorschrften_dokument

---

### afu_abbaustellen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_abbaustellen_pub`

**Quell-Tabellen:**
- abbaustelle
- afu_abbaustellen_v1.abbaustelle
- afu_abbaustellen_v1.geometrie

---

### afu_ara_einzugsgebiete_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_ara_einzugsgebiete_pub`

**Quell-Tabellen:**
- afu_ara_einzugsgebiete.einzugsgebiete_ara_einzugsgebiet

---

### afu_baugrundklassen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_baugrundklassen_pub`

**Quell-Tabellen:**
- afu_baugrundklassen_v1.baugrundklasse

---

### afu_bodendaten_schadstoffuntersuchung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bodendaten_schadstoffuntersuchung_pub`

**Quell-Tabellen:**
- afu_bodendaten_nabodat_v1.codelistnnlysdten_analysematerial
- afu_bodendaten_nabodat_v1.codelistnnlysdten_analyseparameter
- afu_bodendaten_nabodat_v1.codelistnnlysdten_belastung
- afu_bodendaten_nabodat_v1.codelistnnlysdten_beprobungsart
- afu_bodendaten_nabodat_v1.codelistnnlysdten_geraet
- afu_bodendaten_nabodat_v1.codelistnnlysdten_methodeaufbereitung
- afu_bodendaten_nabodat_v1.codelistnnlysdten_methodeaufschluss
- afu_bodendaten_nabodat_v1.codelistnnlysdten_methodemessung
- afu_bodendaten_nabodat_v1.codelistnnlysdten_probentyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_erhebungsart
- afu_bodendaten_nabodat_v1.codlstnpktstndort_status
- afu_bodendaten_nabodat_v1.codlstnpktstndort_zugangsstufe
- afu_bodendaten_nabodat_v1.erhebung_probe_profil_v
- afu_bodendaten_nabodat_v1.punktdaten_erhebung
- afu_bodendaten_nabodat_v1.punktdaten_messung
- afu_bodendaten_nabodat_v1.punktdaten_probe
- afu_bodendaten_nabodat_v1.punktdaten_probedbf
- afu_bodendaten_nabodat_v1.punktdaten_projekt
- afu_bodendaten_nabodat_v1.punktdaten_projektstandort
- afu_bodendaten_nabodat_v1.punktdaten_standort

---

### afu_bodenprofilstandorte_nabodat_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bodenprofilstandorte_nabodat_pub`

**Quell-Tabellen:**
- afu_bodendaten_nabodat_v1.codelistnnlysdten_analyseparameter
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodentyp
- afu_bodendaten_nabodat_v1.codelistnprfldten_bodenwasserhaushaltsgruppe
- afu_bodendaten_nabodat_v1.codelistnprfldten_eignungsklasse
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtontext
- afu_bodendaten_nabodat_v1.codelistnprfldten_farbtonzahl
- afu_bodendaten_nabodat_v1.codelistnprfldten_feinerdekoernung
- afu_bodendaten_nabodat_v1.codelistnprfldten_form
- afu_bodendaten_nabodat_v1.codelistnprfldten_fruchtbarkeitsstufe
- afu_bodendaten_nabodat_v1.codelistnprfldten_groesse
- afu_bodendaten_nabodat_v1.codelistnprfldten_helligkeit
- afu_bodendaten_nabodat_v1.codelistnprfldten_intensitaet
- afu_bodendaten_nabodat_v1.codelistnprfldten_kalkreaktionhcl
- afu_bodendaten_nabodat_v1.codelistnprfldten_klassifikationssystem
- afu_bodendaten_nabodat_v1.codelistnprfldten_nutzungseignung
- afu_bodendaten_nabodat_v1.codelistnprfldten_pflanzennutzbaregruendigkeit
- afu_bodendaten_nabodat_v1.codelistnprfldten_skelettgehalt
- afu_bodendaten_nabodat_v1.codelistnprfldten_untertyp
- afu_bodendaten_nabodat_v1.codelistnprfldten_wasserspeichervermoegen
- afu_bodendaten_nabodat_v1.codelistnprfldten_zustandorgsubst
- afu_bodendaten_nabodat_v1.codlstnpktstndort_ausgangsmaterial
- afu_bodendaten_nabodat_v1.codlstnpktstndort_dokumenttyp
- afu_bodendaten_nabodat_v1.codlstnpktstndort_einsatzduengerfest
- afu_bodendaten_nabodat_v1.codlstnpktstndort_eiszeit
- afu_bodendaten_nabodat_v1.codlstnpktstndort_erhebungsart
- afu_bodendaten_nabodat_v1.codlstnpktstndort_exposition
- afu_bodendaten_nabodat_v1.codlstnpktstndort_gelaendeform
- afu_bodendaten_nabodat_v1.codlstnpktstndort_humusform
- afu_bodendaten_nabodat_v1.codlstnpktstndort_kleinrelief
- afu_bodendaten_nabodat_v1.codlstnpktstndort_klimaeignungszone
- afu_bodendaten_nabodat_v1.codlstnpktstndort_krumenzustand
- afu_bodendaten_nabodat_v1.codlstnpktstndort_landschaftselement
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft
- afu_bodendaten_nabodat_v1.codlstnpktstndort_limitierendeeigenschaft_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationempf_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest
- afu_bodendaten_nabodat_v1.codlstnpktstndort_meliorationfest_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung
- afu_bodendaten_nabodat_v1.codlstnpktstndort_nutzungsbeschraenkung_ref
- afu_bodendaten_nabodat_v1.codlstnpktstndort_produktionsfaehigkstufewald
- afu_bodendaten_nabodat_v1.codlstnpktstndort_risikoduengerfluess
- afu_bodendaten_nabodat_v1.codlstnpktstndort_vegetation
- afu_bodendaten_nabodat_v1.erhebung_probe_profil_v
- afu_bodendaten_nabodat_v1.punktdaten_ausgangsmaterial
- afu_bodendaten_nabodat_v1.punktdaten_bichqualitaet
- afu_bodendaten_nabodat_v1.punktdaten_bodenfarbe
- afu_bodendaten_nabodat_v1.punktdaten_bodenskelettfeldbereich
- afu_bodendaten_nabodat_v1.punktdaten_dokument
- afu_bodendaten_nabodat_v1.punktdaten_erhebung
- afu_bodendaten_nabodat_v1.punktdaten_gefuege
- afu_bodendaten_nabodat_v1.punktdaten_horizont
- afu_bodendaten_nabodat_v1.punktdaten_horizontbezeichnung
- afu_bodendaten_nabodat_v1.punktdaten_koernungsbereich
- afu_bodendaten_nabodat_v1.punktdaten_messung
- afu_bodendaten_nabodat_v1.punktdaten_probe
- afu_bodendaten_nabodat_v1.punktdaten_profil
- afu_bodendaten_nabodat_v1.punktdaten_profilbeurteilung
- afu_bodendaten_nabodat_v1.punktdaten_profildokument
- afu_bodendaten_nabodat_v1.punktdaten_projekt
- afu_bodendaten_nabodat_v1.punktdaten_projektstandort
- afu_bodendaten_nabodat_v1.punktdaten_standort
- afu_bodendaten_nabodat_v1.punktdaten_standortbeurteilung
- afu_bodendaten_nabodat_v1.punktdaten_standorteigenschaften
- afu_bodendaten_nabodat_v1.punktdaten_untertyp
- afu_bodendaten_nabodat_v1.punktdaten_wald

---

### afu_bodenverdichtung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bodenverdichtung_pub`

**Quell-Tabellen:**
- afu_bodenverdichtung_v1.bodenverdichtung_bodenverdichtung_typ
- afu_bodenverdichtung_v1.bodenverdichtung_hinweiskarte

---

### afu_bootsanbindeplaetze_mfk

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bootsanbindeplaetze_mfk`

**Quell-Tabellen:**
- ST_READ
- afu_bootsanbindeplaetze_mfk.main.abgleich_mfk
- afu_bootsanbindeplaetze_mfk.main.data_mfk
- editdb.afu_bootsanbindeplaetze_v1.bootsanbindeplatz
- editdb.afu_bootsanbindeplaetze_v1.bootsdaten
- editdb.afu_bootsanbindeplaetze_v1.kontaktdaten

**Ziel-Tabellen:**
- abgleich_mfk
- afu_bootsanbindeplaetze_mfk.main.abgleich_mfk
- data_mfk
- for

---

### afu_bootsanbindeplaetze_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bootsanbindeplaetze_pub`

**Quell-Tabellen:**
- afu_bootsanbindeplaetze_v1.bootsanbindeplatz
- afu_bootsanbindeplaetze_v1.bootsdaten
- afu_bootsanbindeplaetze_v1.bootskategorie
- afu_bootsanbindeplaetze_v1.dokument
- afu_bootsanbindeplaetze_v1.eigentum
- afu_bootsanbindeplaetze_v1.hauptstandort
- afu_bootsanbindeplaetze_v1.kontaktdaten
- afu_bootsanbindeplaetze_v1.standort

---

### afu_bootsanbindeplaetze_sap

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_bootsanbindeplaetze_sap`

**Quell-Tabellen:**
- CURRENT_DATE
- afu_bootsanbindeplaetze.main.kontokorrent_structure
- afu_bootsanbindeplaetze.main.sap_structure
- pubdb.afu_bootsanbindeplaetze_pub_v1.bootsanbindeplatz

**Ziel-Tabellen:**
- afu_bootsanbindeplaetze.main.kontokorrent_structure
- afu_bootsanbindeplaetze.main.sap_structure
- for
- kontokorrent_structure
- sap_structure

---

### afu_ekat_2005_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_ekat_2005_pub`

---

### afu_ekat_2010_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_ekat_2010_pub`

---

### afu_ekat_2015_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_ekat_2015_pub`

---

### afu_ewsabfrage_3d

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_ewsabfrage_3d`

**Quell-Tabellen:**
- afu_ewsabfrage_3d_staging_v1.hinweis
- afu_ewsabfrage_3d_staging_v1.tiefenbeschraenkung

---

### afu_geologie_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_geologie_pub`

**Quell-Tabellen:**
- afu_geologie_v1.ausbildung_festgestein
- afu_geologie_v1.ausbildung_lockergestein
- afu_geologie_v1.geologie_abrisskanten
- afu_geologie_v1.geologie_abrisskanten_typ
- afu_geologie_v1.geologie_geologische_schicht_grundwasser_art
- afu_geologie_v1.geologie_geologische_schicht_sackung_festgestein
- afu_geologie_v1.geologie_geologische_schicht_verkittungsgrad_lockergestein
- afu_geologie_v1.geologie_grundschicht
- afu_geologie_v1.geologie_holozaen
- afu_geologie_v1.geologie_karstformen
- afu_geologie_v1.geologie_karstformen_typ
- afu_geologie_v1.geologie_pleistozaen
- afu_geologie_v1.geologie_schichtfallen
- afu_geologie_v1.geologie_schichtfallen_typ
- afu_geologie_v1.geologie_tektonische_strukturen
- afu_geologie_v1.geologie_tektonische_strukturen_typ
- afu_geologie_v1.geologische_formation
- afu_geologie_v1.geologische_schichtgliederung
- afu_geologie_v1.geologische_serie
- afu_geologie_v1.geologisches_system
- afu_geologie_v1.grundwasserfuehrung_maechtigkeit
- afu_geologie_v1.grundwassertyp
- afu_geologie_v1.kohaesion
- afu_geologie_v1.lithologie
- afu_geologie_v1.material
- afu_geologie_v1.reibungswinkel
- afu_geologie_v1.wasserdurchlaessigkeit

---

### afu_gewaesser_gewaessereigenschaften_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_gewaesser_gewaessereigenschaften_pub`

**Quell-Tabellen:**
- afu_gewaesser_gewaessereigenschaften_pub_v1.abschnittstyp
- afu_gewaesser_gewaessereigenschaften_pub_v1.digitalisierungsdetail
- afu_gewaesser_gewaessereigenschaften_pub_v1.eigentumsart
- afu_gewaesser_gewaessereigenschaften_pub_v1.gewaessereigenschaften_groesse
- afu_gewaesser_v1.gewaessereigenschaft_v

**Ziel-Tabellen:**
- afu_gewaesser_gewaessereigenschaften_pub_v1.gewaessereigenschaften

---

### afu_gewaesser_oekomorphologie_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_gewaesser_oekomorphologie_pub`

**Quell-Tabellen:**
- afu_gewaesser_v1.absturz_v
- afu_gewaesser_v1.bauwerk_v
- afu_gewaesser_v1.oekomorph_v

---

### afu_gewaesser_revitalisierung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_gewaesser_revitalisierung_pub`

**Quell-Tabellen:**
- afu_gewaesser_revitalisierung_v1.gewaesser_revitalisierung_nutzen
- afu_gewaesser_revitalisierung_v1.gewaesser_revitalisierung_priorisierung

---

### afu_gewaesserschutz_bereiche_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_gewaesserschutz_bereiche_pub`

**Quell-Tabellen:**
- afu_gewaesserschutz_bereiche_v1.gsbereiche_gsbereich

---

### afu_gewaesserschutz_zonen_areale_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_gewaesserschutz_zonen_areale_pub`

**Quell-Tabellen:**
- afu_gewaesserschutz_staging_v3.gewaesserschutz_bereich_typ
- afu_gewaesserschutz_staging_v3.gewaesserschutz_dokument
- afu_gewaesserschutz_staging_v3.gewaesserschutz_gewaesserschutzbereich
- afu_gewaesserschutz_staging_v3.gewaesserschutz_rechtsstatusart
- afu_gewaesserschutz_staging_v3.gewaesserschutz_schutzareal
- afu_gewaesserschutz_staging_v3.gewaesserschutz_schutzzone
- afu_gewaesserschutz_staging_v3.gewaesserschutz_zoneundareal_typ
- afu_gewaesserschutz_staging_v3.gewaesserschutz_zustroembereich
- afu_gewaesserschutz_staging_v3.t_ili2db_basket
- afu_gewaesserschutz_staging_v3.t_ili2db_dataset
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_dokument
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_gwsareal
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_gwszone
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_rechtsvorschriftgwsareal
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_rechtsvorschriftgwszone
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_status
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument

---

### afu_grundwassergeometrie_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_grundwassergeometrie_pub`

**Quell-Tabellen:**
- afu_grundwassergeometrie_v1.grundwasser_maechtigkeit
- afu_grundwassergeometrie_v1.grundwasser_maechtigkeit_m
- afu_grundwassergeometrie_v1.grundwasser_mittelstand
- afu_grundwassergeometrie_v1.grundwasser_tiefstand
- afu_grundwassergeometrie_v1.grundwasser_wasseramt
- afu_grundwassergeometrie_v1.grundwasserspiegel_mittel_tief
- afu_grundwassergeometrie_v1.grundwasserstauer
- afu_grundwassergeometrie_v1.grundwasserstrom_begrenzung_hgw
- afu_grundwassergeometrie_v1.isohypse_hoechster_grundwasserstand
- afu_grundwassergeometrie_v1.isohypse_kurventyp
- afu_grundwassergeometrie_v1.isohypse_mittlerer_grundwasserstand
- afu_grundwassergeometrie_v1.isohypse_tiefer_grundwasserstand

---

### afu_hydro_messstationen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_hydro_messstationen_pub`

**Quell-Tabellen:**
- afu_hydro_messstationen_pub_v1.messstationen_typ
- afu_hydro_messstationen_v1.messstationen
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze_generalisiert

**Ziel-Tabellen:**
- afu_hydro_messstationen_pub_v1.messstationen

---

### afu_hydrologische_einzugsgebiete_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_hydrologische_einzugsgebiete_pub`

**Quell-Tabellen:**
- afu_hydrologische_einzugsgebiete_v2.einzugsgebiet_gross
- afu_hydrologische_einzugsgebiete_v2.einzugsgebiet_klein
- afu_hydrologische_einzugsgebiete_v2.einzugsgebiet_mittel

---

### afu_immissionskarten_luft_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_immissionskarten_luft_pub`

**Quell-Tabellen:**
- afu_immissionskarten_luft_v1.luftbelastung_2010_2020

---

### afu_isboden_csv_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_isboden_csv_import`

**Quell-Tabellen:**
- afu_isboden.begelfor_t
- afu_isboden.bodeneinheit_auspraegung_t
- afu_isboden.bodeneinheit_t
- afu_isboden.bodentyp_t
- afu_isboden.gefuegeform_t
- afu_isboden.gefueggr_t
- afu_isboden.humusform_wa_t
- afu_isboden.kalkgehalt_t
- afu_isboden.kartiererin_v
- afu_isboden.koernkl_t
- afu_isboden.skelett_t
- afu_isboden.untertyp_t
- afu_isboden.wasserhhgr_t
- afu_isboden.zw_bodeneinheit_untertyp
- afu_isboden_csv_import_v1.csv_import_csv_import_t

**Ziel-Tabellen:**
- afu_isboden.bodeneinheit_auspraegung_t
- afu_isboden.bodeneinheit_t
- afu_isboden.zw_bodeneinheit_untertyp
- afu_isboden_csv_import_v1.csv_import_csv_import_t
- l
- to

---

### afu_isboden_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_isboden_pub`

**Quell-Tabellen:**
- afu_erosion_gbf20_p
- afu_erosion_gbf20_p_code
- afu_isboden.begelfor_t
- afu_isboden.bodeneinheit_auspraegung_t
- afu_isboden.bodeneinheit_onlinedata_t
- afu_isboden.bodeneinheit_t
- afu_isboden.bodentyp_t
- afu_isboden.gefuegeform_t
- afu_isboden.gefueggr_t
- afu_isboden.hinweiskarte_bodenverdichtung_qgis_server_client_t
- afu_isboden.humusform_wa_t
- afu_isboden.kalkgehalt_t
- afu_isboden.koernkl_t
- afu_isboden.skelett_t
- afu_isboden.untertyp_t
- afu_isboden.wasserhhgr_t
- afu_isboden.zw_bodeneinheit_untertyp

---

### afu_karst_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_karst_pub`

**Quell-Tabellen:**
- afu_karst_v1.karst_allogene_gebiete
- afu_karst_v1.karst_felsueberdeckung
- afu_karst_v1.karst_maechtigkeit
- afu_karst_v1.karst_subartesische_zone
- afu_karst_v1.karst_verkarstung
- afu_karst_v1.karst_verkarstung_verkarstungsgrad

---

### afu_klimaanalyse_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_klimaanalyse_pub`

**Quell-Tabellen:**
- afu_klimaanalyse_v1.arbeitszone_ohne_wohnen
- afu_klimaanalyse_v1.ausgangsgroessen_bewertung
- afu_klimaanalyse_v1.ausgangsgroessen_bewertung_kaltluftprozess
- afu_klimaanalyse_v1.entwicklungsflaechen
- afu_klimaanalyse_v1.entwicklungsflaechen_agglopr
- afu_klimaanalyse_v1.entwicklungsflaechen_typ
- afu_klimaanalyse_v1.kaltluftbereich_ist
- afu_klimaanalyse_v1.kaltluftbereich_zukunft
- afu_klimaanalyse_v1.kaltluftentstehung_ist
- afu_klimaanalyse_v1.kaltluftentstehung_zukunft
- afu_klimaanalyse_v1.kaltluftprozess_ist
- afu_klimaanalyse_v1.kaltluftprozess_zukunft

---

### afu_klimaanalyse_windpfeile_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_klimaanalyse_windpfeile_pub`

**Quell-Tabellen:**
- afu_klimaanalyse_windpfeile_v1.windpfeil_100m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_100m_zukunft
- afu_klimaanalyse_windpfeile_v1.windpfeil_10m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_10m_zukunft
- afu_klimaanalyse_windpfeile_v1.windpfeil_200m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_200m_zukunft
- afu_klimaanalyse_windpfeile_v1.windpfeil_300m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_300m_zukunft
- afu_klimaanalyse_windpfeile_v1.windpfeil_500m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_500m_zukunft
- afu_klimaanalyse_windpfeile_v1.windpfeil_50m_ist
- afu_klimaanalyse_windpfeile_v1.windpfeil_50m_zukunft

---

### afu_nabodat_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_nabodat_import`

---

### afu_naturgefahren_freigeben

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahren_freigeben`

**Quell-Tabellen:**
- afu_naturgefahren_v2.t_ili2db_dataset

**Ziel-Tabellen:**
- afu_naturgefahren_v2.t_ili2db_basket

---

### afu_naturgefahren_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahren_import`

---

### afu_naturgefahren_pilot_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahren_pilot_import`

---

### afu_naturgefahren_produkte

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahren_produkte`

**Quell-Tabellen:**
- LATERAL
- afu_gefahrenkartierung.gefahrenkartirung_erhebungsgebiet
- afu_gefahrenkartierung.gefahrenkartirung_gk_absenkung_einsturz
- afu_gefahrenkartierung.gefahrenkartirung_gk_hangmure
- afu_gefahrenkartierung.gefahrenkartirung_gk_rutsch_kont_sackung
- afu_gefahrenkartierung.gefahrenkartirung_gk_rutsch_spontan
- afu_gefahrenkartierung.gefahrenkartirung_gk_sturz
- afu_gefahrenkartierung.gefahrenkartirung_gk_synoptisch_generiert
- afu_gefahrenkartierung.gefahrenkartirung_gk_wasser
- afu_gefahrenkartierung.gefahrenkartirung_ik_synoptisch_mgdm
- afu_gefahrenkartierung.gefahrenkartirung_perimeter_gefahrenkartierung
- afu_gefahrenkartierung.gefahrenkartirung_prozessquelle_wasser
- afu_gefahrenkartierung.gefahrenkartirung_punktsignatur
- afu_gefahrenkartierung.gefahrenkartirung_ueberflutungskarte
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_absenkung
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_einsturz
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_fels_berg_sturz
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_hangmure
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_permanente_rutschung
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_spontane_rutschung
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_stein_block_schlag
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_uebermurung
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_ueberschwemmung
- afu_naturgefahren_beurteilungsgebiet_v1.erhebungsgebiet_ufererosion
- afu_naturgefahren_staging_v1.abklaerungsperimeter
- afu_naturgefahren_staging_v1.dokumente_pro_gemeinde
- afu_naturgefahren_staging_v1.erhebungsgebiet
- afu_naturgefahren_staging_v1.fliessrichtung
- afu_naturgefahren_staging_v1.fliesstiefen
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_sturz
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_wasser
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_absenkung_einsturz
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_fels_bergsturz
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_hangmure
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_murgang
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_permanente_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_spontane_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_stein_blockschlag
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_ueberflutung
- afu_naturgefahren_staging_v1.kennwert_uebermurung_geschwindigkeit
- afu_naturgefahren_staging_v1.kennwert_uebermurung_hoehe
- afu_naturgefahren_staging_v1.kennwert_ueberschwemmung_geschwindigkeit
- afu_naturgefahren_staging_v1.synoptische_intensitaet
- afu_naturgefahren_staging_v1.synoptisches_gefahrengebiet
- afu_naturgefahren_staging_v1.t_ili2db_basket
- afu_naturgefahren_staging_v1.ufererosion
- afu_naturgefahren_staging_v2.dokumente_pro_gemeinde
- afu_naturgefahren_staging_v2.erhebungsgebiet
- afu_naturgefahren_staging_v2.fliessrichtung
- afu_naturgefahren_staging_v2.fliesstiefen
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_sturz
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_wasser
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_absenkung_einsturz
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_fels_bergsturz
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_hangmure
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_murgang
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_permanente_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_spontane_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_stein_blockschlag
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_ueberflutung
- afu_naturgefahren_staging_v2.kennwert_uebermurung_geschwindigkeit
- afu_naturgefahren_staging_v2.kennwert_uebermurung_hoehe
- afu_naturgefahren_staging_v2.kennwert_ueberschwemmung_geschwindigkeit
- afu_naturgefahren_staging_v2.synoptische_intensitaet
- afu_naturgefahren_staging_v2.synoptisches_gefahrengebiet
- afu_naturgefahren_staging_v2.ufererosion
- afu_naturgefahren_v1.abklaerungsperimeter
- afu_naturgefahren_v1.auftrag
- afu_naturgefahren_v1.befundabsenkung
- afu_naturgefahren_v1.befundbergfelssturz
- afu_naturgefahren_v1.befundeinsturz
- afu_naturgefahren_v1.befundhangmure
- afu_naturgefahren_v1.befundpermanenterutschung
- afu_naturgefahren_v1.befundspontanerutschung
- afu_naturgefahren_v1.befundsteinblockschlag
- afu_naturgefahren_v1.befunduebermurung
- afu_naturgefahren_v1.befundueberschwemmungdynamisch
- afu_naturgefahren_v1.befundueberschwemmungstatisch
- afu_naturgefahren_v1.befundufererosion
- afu_naturgefahren_v1.bericht
- afu_naturgefahren_v1.pq_jaehrlichkeit_bergfelssturz
- afu_naturgefahren_v1.pq_jaehrlichkeit_hangmure
- afu_naturgefahren_v1.pq_jaehrlichkeit_spontanerutschung
- afu_naturgefahren_v1.pq_jaehrlichkeit_steinblockschlag
- afu_naturgefahren_v1.prozessquelle
- afu_naturgefahren_v1.t_ili2db_basket
- afu_naturgefahren_v1.t_ili2db_dataset
- afu_naturgefahren_v1.teilauftrag
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- auf
- gk_poly
- node_parent_root_map
- poly_cleanup
- public.poly_cleanup
- splited

**Ziel-Tabellen:**
- afu_naturgefahren_staging_v1.abklaerungsperimeter
- afu_naturgefahren_staging_v1.dokumente_pro_gemeinde
- afu_naturgefahren_staging_v1.erhebungsgebiet
- afu_naturgefahren_staging_v1.fliessrichtung
- afu_naturgefahren_staging_v1.fliesstiefen
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_sturz
- afu_naturgefahren_staging_v1.gefahrengebiet_hauptprozess_wasser
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_absenkung_einsturz
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_fels_bergsturz
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_hangmure
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_murgang
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_permanente_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_spontane_rutschung
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_stein_blockschlag
- afu_naturgefahren_staging_v1.gefahrengebiet_teilprozess_ueberflutung
- afu_naturgefahren_staging_v1.kennwert_uebermurung_geschwindigkeit
- afu_naturgefahren_staging_v1.kennwert_uebermurung_hoehe
- afu_naturgefahren_staging_v1.kennwert_ueberschwemmung_geschwindigkeit
- afu_naturgefahren_staging_v1.synoptische_intensitaet
- afu_naturgefahren_staging_v1.synoptisches_gefahrengebiet
- afu_naturgefahren_staging_v1.t_ili2db_basket
- afu_naturgefahren_staging_v1.t_ili2db_dataset
- afu_naturgefahren_staging_v1.ufererosion
- der
- f
- gk_poly
- poly_cleanup
- public.poly_cleanup
- splited

---

### afu_naturgefahren_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahren_pub`

**Quell-Tabellen:**
- LATERAL
- UNNEST
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_fels_berg_sturz
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_hangmure
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_permanente_rutschung
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_spontane_rutschung
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_stein_block_schlag
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_uebermurung
- afu_naturgefahren_beurteilungsgebiet_v2.erhebungsgebiet_ueberschwemmung
- afu_naturgefahren_mgdm_v1.hazard_mapping_assessment_area
- afu_naturgefahren_mgdm_v1.hazard_mapping_hazard_area
- afu_naturgefahren_mgdm_v1.hazard_mapping_synoptic_intensity
- afu_naturgefahren_staging_v2.abklaerungsperimeter
- afu_naturgefahren_staging_v2.beurteilung_einfach_typ
- afu_naturgefahren_staging_v2.beurteilung_komplex_typ
- afu_naturgefahren_staging_v2.dokumente_pro_gemeinde
- afu_naturgefahren_staging_v2.erhebungsgebiet
- afu_naturgefahren_staging_v2.fliessrichtung
- afu_naturgefahren_staging_v2.fliesstiefen
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_sturz
- afu_naturgefahren_staging_v2.gefahrengebiet_hauptprozess_wasser
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_absenkung_einsturz
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_fels_bergsturz
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_hangmure
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_murgang
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_permanente_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_spontane_rutschung
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_stein_blockschlag
- afu_naturgefahren_staging_v2.gefahrengebiet_teilprozess_ueberflutung
- afu_naturgefahren_staging_v2.gefahrenstufe_typ
- afu_naturgefahren_staging_v2.hauptprozess
- afu_naturgefahren_staging_v2.intensitaet_typ
- afu_naturgefahren_staging_v2.kennwert_uebermurung_geschwindigkeit
- afu_naturgefahren_staging_v2.kennwert_uebermurung_hoehe
- afu_naturgefahren_staging_v2.kennwert_ueberschwemmung_geschwindigkeit
- afu_naturgefahren_staging_v2.m_geschwindigkeit_typ
- afu_naturgefahren_staging_v2.m_hoehe_typ
- afu_naturgefahren_staging_v2.synoptische_intensitaet
- afu_naturgefahren_staging_v2.synoptisches_gefahrengebiet
- afu_naturgefahren_staging_v2.teilprozess_quellen
- afu_naturgefahren_staging_v2.teilprozess_synoptisch
- afu_naturgefahren_staging_v2.ue_fliessgeschwindigkeit_typ
- afu_naturgefahren_staging_v2.ueberflutungshoehe_wasser
- afu_naturgefahren_staging_v2.ufererosion

**Ziel-Tabellen:**
- afu_naturgefahren_mgdm_v1.hazard_mapping_assessment_area
- afu_naturgefahren_mgdm_v1.hazard_mapping_hazard_area
- afu_naturgefahren_mgdm_v1.hazard_mapping_synoptic_intensity

---

### afu_naturgefahrenhinweiskarte_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_naturgefahrenhinweiskarte_pub`

**Quell-Tabellen:**
- afu_naturgefahrenhinweiskarte_v1.blockschlag
- afu_naturgefahrenhinweiskarte_v1.murgang
- afu_naturgefahrenhinweiskarte_v1.rutschung_bekannt
- afu_naturgefahrenhinweiskarte_v1.rutschung_lockergestein
- afu_naturgefahrenhinweiskarte_v1.rutschung_tief
- afu_naturgefahrenhinweiskarte_v1.steinschlag
- afu_naturgefahrenhinweiskarte_v1.talboeden_geringe_neigung
- afu_naturgefahrenhinweiskarte_v1.ueberflutung
- afu_naturgefahrenhinweiskarte_v1.uebersarung

---

### afu_oekomorphologie_csvimport

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_oekomorphologie_csvimport`

**Quell-Tabellen:**
- absturzcsv
- bauwerkcsv
- gewaesserbasisgeometrie
- nicht
- oekomorphcsv

**Ziel-Tabellen:**
- absturz
- bauwerk
- oekomorph
- oekomorphcsv

---

### afu_qrcat_berechnungen

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_qrcat_berechnungen`

**Quell-Tabellen:**
- arp_statpop_statent_v1.hektarraster_statpopstatent
- und

---

### afu_quellen_ungefasst_csvimport

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_quellen_ungefasst_csvimport`

**Quell-Tabellen:**
- afu_quellen_ungefasst_staging_v1.csv_import
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze

**Ziel-Tabellen:**
- afu_quellen_ungefasst_staging_v1.csv_import

---

### afu_quellen_ungefasst_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_quellen_ungefasst_pub`

**Quell-Tabellen:**
- bewertung

**Ziel-Tabellen:**
- quelle_ungefasst

---

### afu_schadendienst_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_schadendienst_pub`

**Quell-Tabellen:**
- afu_schadendienst_v1.nichtschadenfall
- afu_schadendienst_v1.schadenfall

---

### afu_schadstoffbelastete_boeden_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_schadstoffbelastete_boeden_pub`

**Quell-Tabellen:**
- afu_schadstoffbelastete_boeden.schadstoffbelasteter_boden_begruendung_aus_vsb_entlassen
- afu_schadstoffbelastete_boeden.schadstoffbelasteter_boden_status
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_anbaugebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_bodenbelastungsgebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_anbaugebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_bodenbelastungsflaeche
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_eisenbahn
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_flugplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_gartenbau
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_geogene_bodenbelastung
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_militaerischer_schiessplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_schiessanlage
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_siedlungsgebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_stahlbruecke
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_stahlkonstruktion
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_stahlmast
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_dokument_strasse
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_eisenbahn
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_flugplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_gartenbau
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_gebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_geogene_bodenbelastung
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_lage
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_leitung
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_militaerischer_schiessplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_anbaugebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_bodenbelastungsflaeche
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_eisenbahn
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_flugplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_gartenbau
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_geogene_bodenbelastung
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_militaerischer_schiessplatz
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_schiessanlage
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_siedlungsgebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_stahlbruecke
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_stahlkonstruktion
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_stahlmast
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schadstoff_strasse
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schiessanlage
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schiessanlage_schiessanlagentyp
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_schiessanlagentyp
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_siedlungsgebiet
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_stahlbruecke
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_stahlkonstruktion
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_stahlkonstruktionstyp
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_stahlmast
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_strasse
- afu_schadstoffbelastete_boeden.schdstfflstt_bden_transportunternehmen
- afu_schadstoffbelastete_boeden.schdstfstt_bden_bodenbelastungsgebiet_belastungsstufe
- afu_schadstoffbelastete_boeden.schdstfstt_bden_bodenbelastungsgebiet_verursacher
- afu_schadstoffbelastete_boeden.schdstfstt_bden_eisenbahn_flaechentyp
- afu_schadstoffbelastete_boeden.schdstfstt_bden_eisenbahn_verdachtsstreifenbreite
- afu_schadstoffbelastete_boeden.schdstfstt_bden_eisenbahn_verkehrsfrequenz
- afu_schadstoffbelastete_boeden.schdstfstt_bden_militaerischer_schiessplatz_betriebsstatus
- afu_schadstoffbelastete_boeden.schdstfstt_bden_schiessanlage_sanierungsstatus
- afu_schadstoffbelastete_boeden.schdstfstt_bden_schiessanlage_trennkriterium
- afu_schadstoffbelastete_boeden.schdstfstt_bden_stahlbruecke_brueckentyp
- afu_schadstoffbelastete_boeden.schdstfstt_bden_stahlmast_radius
- afu_schadstoffbelastete_boeden.schdstfstt_bden_strasse_strassentyp
- afu_schadstoffbelastete_boeden.schdstfstt_bden_strasse_verdachtsstreifenbreite
- afu_schadstoffbelastete_boeden.schdstfstt_bden_strasse_verkehrsfrequenz
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.nomenklatur_flurname
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze

---

### afu_schutzbauten_export

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_schutzbauten_export`

---

### afu_schutzbauten_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_schutzbauten_import`

---

### afu_schutzbauten_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_schutzbauten_pub`

**Quell-Tabellen:**
- afu_schutzbauten_v1.baumaterial_typ
- afu_schutzbauten_v1.beurteilung_typ
- afu_schutzbauten_v1.dokument
- afu_schutzbauten_v1.koerperschaft_typ
- afu_schutzbauten_v1.rutschung_abdeckung_ingmassnahme
- afu_schutzbauten_v1.rutschung_andere_werksart_flaeche
- afu_schutzbauten_v1.rutschung_andere_werksart_linie
- afu_schutzbauten_v1.rutschung_andere_werksart_punkt
- afu_schutzbauten_v1.rutschung_auffangnetz
- afu_schutzbauten_v1.rutschung_damm
- afu_schutzbauten_v1.rutschung_hangstuetzwerk_entwaesserung_palisade
- afu_schutzbauten_v1.schutzbaute_dokument
- afu_schutzbauten_v1.sturz_abdeckung_verankerung
- afu_schutzbauten_v1.sturz_andere_werksart_flaeche
- afu_schutzbauten_v1.sturz_andere_werksart_linie
- afu_schutzbauten_v1.sturz_andere_werksart_punkt
- afu_schutzbauten_v1.sturz_galerie
- afu_schutzbauten_v1.sturz_schutznetz_palisade_damm_schutzzaun_mauer
- afu_schutzbauten_v1.sturz_unterfangung
- afu_schutzbauten_v1.t_ili2db_basket
- afu_schutzbauten_v1.t_ili2db_dataset
- afu_schutzbauten_v1.wasser_andere_werksart_flaeche
- afu_schutzbauten_v1.wasser_andere_werksart_linie
- afu_schutzbauten_v1.wasser_andere_werksart_punkt
- afu_schutzbauten_v1.wasser_bruecke_steg
- afu_schutzbauten_v1.wasser_buhne
- afu_schutzbauten_v1.wasser_damm
- afu_schutzbauten_v1.wasser_eindolung
- afu_schutzbauten_v1.wasser_entlastungsbauwerk
- afu_schutzbauten_v1.wasser_entlastungsstollen_kanal
- afu_schutzbauten_v1.wasser_furt
- afu_schutzbauten_v1.wasser_geschiebeablagerungsplatz
- afu_schutzbauten_v1.wasser_hochwasser_geschiebe_rueckhaltebauwerk
- afu_schutzbauten_v1.wasser_mauer
- afu_schutzbauten_v1.wasser_murbrecher_murbremse
- afu_schutzbauten_v1.wasser_rampe_sohlensicherung
- afu_schutzbauten_v1.wasser_schwemmholz_eis_rueckhaltebauwerk
- afu_schutzbauten_v1.wasser_sperre_schwelle
- afu_schutzbauten_v1.wasser_uferdeckwerk_ufermauer
- afu_schutzbauten_v1.wirksamkeit_typ

---

### afu_stoerfallverordnung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/afu_stoerfallverordnung_pub`

**Quell-Tabellen:**
- afu_stoerfallverordnung_v1.betrieb
- afu_stoerfallverordnung_v1.betriebsareal
- afu_stoerfallverordnung_v1.durchgangsstrasse
- afu_stoerfallverordnung_v1.durchgangsstrasse_achsentyp
- afu_stoerfallverordnung_v1.durchgangsstrasse_darstellung
- afu_stoerfallverordnung_v1.erdgasroehrenspeicher
- afu_stoerfallverordnung_v1.konsultationsbereich
- afu_stoerfallverordnung_v1.nationalstrasse

---

### agi_check_ili_export

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_check_ili_export`

---

### agi_dmav_dauerndebodenverschiebungen_export

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_dmav_dauerndebodenverschiebungen_export`

---

### agi_dmav_fixpunkte3_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_dmav_fixpunkte3_import`

---

### agi_dmav_rohrleitungen_export

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_dmav_rohrleitungen_export`

---

### agi_dmav_toleranzstufen_export

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_dmav_toleranzstufen_export`

---

### agi_inventar_hoheitsgrenzen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_inventar_hoheitsgrenzen_pub`

**Quell-Tabellen:**
- agi_inventar_hoheitsgrenzen.invntr_hhtsgrnzen_gemeinde
- agi_inventar_hoheitsgrenzen.invntr_hhtsgrnzen_gemeinde_hoheitsgrenzstein
- agi_inventar_hoheitsgrenzen.invntr_hhtsgrnzen_kantonsgrenzstein

---

### agi_layer_rollout

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_layer_rollout`

**Quell-Tabellen:**
- simi.simi.simitheme_theme
- simi.simi.simitheme_theme_publication
- simi.simidata_data_set_view
- simi.simidata_db_schema
- simi.simidata_postgres_db
- simi.simidata_postgres_table
- simi.simidata_raster_ds
- simi.simidata_raster_view
- simi.simidata_styleasset
- simi.simidata_table_field
- simi.simidata_table_view
- simi.simidata_view_field
- simi.simiextended_dependency
- simi.simiextended_relation
- simi.simiiam_group
- simi.simiiam_group_user_link
- simi.simiiam_identity
- simi.simiiam_permission
- simi.simiiam_role
- simi.simiiam_role_group_link
- simi.simiiam_role_user_link
- simi.simiiam_user
- simi.simiproduct_data_product
- simi.simiproduct_data_product_pub_scope
- simi.simiproduct_external_wms_layers
- simi.simiproduct_external_wms_service
- simi.simiproduct_facade_layer
- simi.simiproduct_layer_group
- simi.simiproduct_map
- simi.simiproduct_product_list
- simi.simiproduct_properties_in_facade
- simi.simiproduct_properties_in_list
- simi.simiproduct_single_actor
- simi.simitheme_agency
- simi.simitheme_file_type
- simi.simitheme_org_unit
- simi.simitheme_published_sub_area
- simi.simitheme_published_sub_area_helper
- simi.simitheme_sub_area
- simi.simitheme_sub_org
- simi.simitheme_theme
- simi.simitheme_theme_publication
- simi.simitheme_theme_publication_custom_file_type_link

**Ziel-Tabellen:**
- simi.simitheme_published_sub_area
- simi.simitheme_published_sub_area_helper

---

### agi_lk_netzgebiete_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_lk_netzgebiete_pub`

**Quell-Tabellen:**
- agi_lk_netzgebiete_v1.amedium
- agi_lk_netzgebiete_v1.netzgebiet
- agi_lk_netzgebiete_v1.organisation
- agi_lk_netzgebiete_v1.perimeter
- awa_stromversorgungssicherheit_mgdm_v1.organisation
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level3
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level5
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level7

**Ziel-Tabellen:**
- awa_stromversorgungssicherheit_mgdm_v1.organisation
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level3
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level5
- awa_stromversorgungssicherheit_mgdm_v1.ruledarea_level7

---

### agi_plz_ortschaften_pub_manueller_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_plz_ortschaften_pub_manueller_import`

**Quell-Tabellen:**
- agi_plz_ortschaften.plzortschaft_ortschaft
- agi_plz_ortschaften.plzortschaft_ortschaftsname
- agi_plz_ortschaften.plzortschaft_plz6
- agi_plz_ortschaften_pub.plzortschaften_ortschaft
- agi_plz_ortschaften_pub.plzortschaften_postleitzahl

**Ziel-Tabellen:**
- agi_plz_ortschaften_pub.plzortschaften_ortschaft
- agi_plz_ortschaften_pub.plzortschaften_postleitzahl

---

### agi_schema_dump

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_schema_dump`

---

### agi_suchindex_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/agi_suchindex_pub`

**Quell-Tabellen:**
- id
- simi.solr_layer_base_v

---

### alw_drainagen_bemerkungen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_drainagen_bemerkungen_pub`

**Quell-Tabellen:**
- alw_drainagen_bemerkungen_v1.bemerkungen_bemerkungen

---

### alw_drainagen_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_drainagen_import`

---

### alw_drainagen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_drainagen_pub`

**Quell-Tabellen:**
- alw_drainagen_v1.administration_organisation
- alw_drainagen_v1.vsadssmini_knoten
- alw_drainagen_v1.vsadssmini_leitung

---

### alw_fruchtfolgeflaechen

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_fruchtfolgeflaechen`

**Quell-Tabellen:**
- afu_abbaustellen_fff_v1.uebersteuerung
- afu_altlasten_pub.belasteter_standort
- afu_altlasten_restricted_pub_v1.belasteter_standort
- afu_gewaesserschutz_pub.gewaesserschutz_schutzzone
- afu_gewaesserschutz_pub_v3.gewaesserschutz_schutzzone
- afu_isboden_fff_pub.bodeneinheit
- afu_isboden_pub.bodeneinheit
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_bodenbelastungsgebiet
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_flugplatz
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_gaertnerei
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_rebbau
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_schrebergarten
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_stahlbruecke
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_stahlkonstruktion
- afu_schadstoffbelastete_boeden_pub.schdstfflstt_bden_stahlmast
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- agi_mopublic_pub.mopublic_bodenbedeckung
- agi_mopublic_pub.mopublic_gemeindegrenze
- alw_fff_uebersteuerung.uebersteuerung
- alw_fruchtfolgeflaechen.fff_komplett
- alw_fruchtfolgeflaechen.fff_maske_bodenbedeckung
- alw_fruchtfolgeflaechen.fff_maske_fertig
- alw_fruchtfolgeflaechen.fff_maske_ohne_altlasten
- alw_fruchtfolgeflaechen.fff_maske_ohne_auen_flachmoore_hochmoore_vogelreservate
- alw_fruchtfolgeflaechen.fff_maske_ohne_bauzonen
- alw_fruchtfolgeflaechen.fff_maske_ohne_klimaeignung
- alw_fruchtfolgeflaechen.fff_maske_ohne_naturreservate
- alw_fruchtfolgeflaechen.fff_maske_ohne_schadstoffbelastete_boeden
- alw_fruchtfolgeflaechen.fff_maske_ohne_trockenwiesen
- alw_fruchtfolgeflaechen.fff_maske_where_bodenkartierung
- alw_fruchtfolgeflaechen.fff_maske_where_not_bodenkartierung
- alw_fruchtfolgeflaechen.fff_mit_bodenkartierung_100
- alw_fruchtfolgeflaechen.fff_mit_bodenkartierung_50
- alw_fruchtfolgeflaechen.fff_mit_gewaesserraum
- alw_fruchtfolgeflaechen.fff_mit_uebersteuerung
- alw_fruchtfolgeflaechen.fff_ohne_bodenkartierung
- alw_fruchtfolgeflaechen.fff_zusammengesetzt
- alw_fruchtfolgeflaechen.fruchtfolgeflaeche_clean
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_buffer_mm
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_exteriorring
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_union
- alw_fruchtfolgeflaechen.inventarflaechen_fruchtfolgeflaeche
- alw_fruchtfolgeflaechen.polys
- alw_fruchtfolgeflaechen.polys_attr
- alw_fruchtfolgeflaechen.polys_join
- alw_fruchtfolgeflaechen.polys_point
- alw_fruchtfolgeflaechen_pub_v1.fruchtfolgeflaeche
- alw_gewaesserraum.gewaesserraum
- alw_gewaesserraum_v1.gewaesserraum
- alw_uebersteuerung_fff_v2.uebersteuerung
- arp_mjpnatur_pub.flaechen
- arp_naturreservate_pub.naturreservate_reservat
- arp_naturschutzobjekte_pub_v1.flachmoor
- arp_npl_pub.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- auen.auen_standorte
- flachmoore.flachmoore_standorte
- hochmoore.hochmoore_standorte
- klimaeignung.kategorien_eignung
- klimaeignung.klimaeignung_klima_area
- trockenwiesenweiden.trockenwiesenwden_standorte

**Ziel-Tabellen:**
- afu_isboden_pub.bodeneinheit
- alw_fruchtfolgeflaechen.fff_komplett
- alw_fruchtfolgeflaechen.fff_maske_bodenbedeckung
- alw_fruchtfolgeflaechen.fff_maske_fertig
- alw_fruchtfolgeflaechen.fff_maske_ohne_schadstoffbelastete_boeden
- alw_fruchtfolgeflaechen.fff_maske_where_bodenkartierung
- alw_fruchtfolgeflaechen.fff_maske_where_not_bodenkartierung
- alw_fruchtfolgeflaechen.fff_mit_bodenkartierung_100
- alw_fruchtfolgeflaechen.fff_mit_bodenkartierung_50
- alw_fruchtfolgeflaechen.fff_mit_gewaesserraum
- alw_fruchtfolgeflaechen.fff_mit_uebersteuerung
- alw_fruchtfolgeflaechen.fff_ohne_bodenkartierung
- alw_fruchtfolgeflaechen.fff_zusammengesetzt
- alw_fruchtfolgeflaechen.fruchtfolgeflaeche_clean
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_buffer_mm
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_exteriorring
- alw_fruchtfolgeflaechen.fruchtfolgeflaechen_union
- alw_fruchtfolgeflaechen.polys
- alw_fruchtfolgeflaechen.polys_attr
- alw_fruchtfolgeflaechen.polys_join
- alw_fruchtfolgeflaechen.polys_point

---

### alw_fruchtfolgeflaechen_export_ai

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_fruchtfolgeflaechen_export_ai`

**Quell-Tabellen:**
- alw_fruchtfolgeflaechen_mgdm_v1.fruchtfolgeflaeche
- alw_fruchtfolgeflaechen_mgdm_v1.qualitaet_kantonal
- alw_fruchtfolgeflaechen_v1.fruchtfolgeflaeche

---

### alw_fruchtfolgeflaechen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_fruchtfolgeflaechen_pub`

**Quell-Tabellen:**
- alw_fruchtfolgeflaechen_v1.fruchtfolgeflaeche
- alw_fruchtfolgeflaechen_v1.statistik

---

### alw_futterbaulinien_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_futterbaulinien_pub`

**Quell-Tabellen:**
- alw_futterbaulinien_v1.futterbaulinien_geometrie

---

### alw_gewaesserraum_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_gewaesserraum_pub`

**Quell-Tabellen:**
- alw_gewaesserraum_v1.gewaesserraum

---

### alw_strukturverbesserungen_suissemelio

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_strukturverbesserungen_suissemelio`

**Quell-Tabellen:**
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet
- alw_strukturverbesserungen.raeumlicheelemnte_beizugsgebiet_projekt
- alw_strukturverbesserungen.raeumlicheelemnte_bew_flaechen_bewaesserung
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_linie
- alw_strukturverbesserungen.raeumlicheelemnte_bewaesserung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_flaeche
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_linie
- alw_strukturverbesserungen.raeumlicheelemnte_entw_bodenstruktur_pumpwerk
- alw_strukturverbesserungen.raeumlicheelemnte_ev_linie
- alw_strukturverbesserungen.raeumlicheelemnte_ev_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_flaeche
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_linie
- alw_strukturverbesserungen.raeumlicheelemnte_oekologie_trockenmauer
- alw_strukturverbesserungen.raeumlicheelemnte_projekt
- alw_strukturverbesserungen.raeumlicheelemnte_wasserversorgung_punkt
- alw_strukturverbesserungen.raeumlicheelemnte_wege_bruecke_lehnenviadukt
- alw_strukturverbesserungen.raeumlicheelemnte_wegebau_linie
- alw_strukturverbesserungen.raeumlicheelemnte_wv_leitung_wasserversorgung

---

### alw_zonengrenzen_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/alw_zonengrenzen_import`

**Quell-Tabellen:**
- alw_zonengrenzen.languagecode_iso639_1
- alw_zonengrenzen.localisedtext
- alw_zonengrenzen.lz_kataloge_lz_katalog_typ
- alw_zonengrenzen.lz_kataloge_lz_katalog_typref
- alw_zonengrenzen.multilingualtext
- alw_zonengrenzen.zonengrenzen_lz_flaeche

---

### arp_mjpnl_auszahlung

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_auszahlung`

---

### arp_mjpnl_gelan_update

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_gelan_update`

---

### arp_mjpnl_initialisierung

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_initialisierung`

---

### arp_mjpnl_migration

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_migration`

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.nomenklatur_flurname
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- alw_zonengrenzen.lz_kataloge_lz_katalog_typ
- alw_zonengrenzen.zonengrenzen_lz_flaeche
- l.datum_auszahlung
- l.gueltigbis
- mjpnatur.code
- mjpnatur.flaechen
- mjpnatur.flaechen_geom_t
- mjpnatur.flaechenart
- mjpnatur.leistung
- mjpnatur.leistungsart
- mjpnatur.personen
- mjpnatur.rrbeschluss
- mjpnatur.status
- mjpnatur.vbart
- mjpnatur.vereinbarung

**Ziel-Tabellen:**
- abrechnung_per_leistung
- basierend

---

### arp_mjpnl_v2_gelan_update

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_v2_gelan_update`

---

### arp_mjpnl_v2_initialisierung

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_v2_initialisierung`

---

### arp_mjpnl_v2_migration

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_v2_migration`

---

### arp_mjpnl_zahlungslauf

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_mjpnl_zahlungslauf`

**Quell-Tabellen:**
- arp_mjpnl_v1.betrbsdttrktrdten_gelan_person
- arp_mjpnl_v1.mjpnl_berater
- arp_mjpnl_v1.mjpnl_beurteilung_alr_buntbrache
- arp_mjpnl_v1.mjpnl_beurteilung_alr_saum
- arp_mjpnl_v1.mjpnl_beurteilung_hecke
- arp_mjpnl_v1.mjpnl_beurteilung_hostet
- arp_mjpnl_v1.mjpnl_beurteilung_obl
- arp_mjpnl_v1.mjpnl_beurteilung_wbl_weide
- arp_mjpnl_v1.mjpnl_beurteilung_wbl_wiese
- arp_mjpnl_v1.mjpnl_beurteilung_weide_ln
- arp_mjpnl_v1.mjpnl_beurteilung_weide_soeg
- arp_mjpnl_v1.mjpnl_beurteilung_wiese
- arp_mjpnl_v1.mjpnl_vereinbarung
- arp_mjpnl_v1.t_ili2db_basket
- arp_mjpnl_v1.umweltziele_uzl_subregion

**Ziel-Tabellen:**
- abrechnung_per_leistung
- arp_mjpnl_v1.mjpnl_beurteilung_alr_buntbrache
- arp_mjpnl_v1.mjpnl_beurteilung_alr_saum
- arp_mjpnl_v1.mjpnl_beurteilung_hecke
- arp_mjpnl_v1.mjpnl_beurteilung_hostet
- arp_mjpnl_v1.mjpnl_beurteilung_obl
- arp_mjpnl_v1.mjpnl_beurteilung_wbl_weide
- arp_mjpnl_v1.mjpnl_beurteilung_wbl_wiese
- arp_mjpnl_v1.mjpnl_beurteilung_weide_ln
- arp_mjpnl_v1.mjpnl_beurteilung_weide_soeg
- arp_mjpnl_v1.mjpnl_beurteilung_wiese
- arp_mjpnl_v1.mjpnl_vereinbarung
- der

---

### arp_naturreservate_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_naturreservate_pub`

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_mehrjahresprogramm.mehrjahresprgramm_person
- arp_naturreservate.reservate_dokument
- arp_naturreservate.reservate_erhebung
- arp_naturreservate.reservate_pflanze
- arp_naturreservate.reservate_pflanze_erhebung
- arp_naturreservate.reservate_reservat
- arp_naturreservate.reservate_reservat_dokument
- arp_naturreservate.reservate_reservat_zustaendiger
- arp_naturreservate.reservate_teilgebiet
- arp_naturreservate.reservate_teilgebiet_erhebung
- arp_naturreservate.reservate_zustaendiger
- arp_naturreservate_staging_v1.naturreservate_pflanzenliste
- arp_naturreservate_staging_v1.naturreservate_reservat
- arp_naturreservate_staging_v1.naturreservate_teilgebiet
- arp_naturreservate_staging_v1.t_ili2db_basket
- arp_naturreservate_staging_v1.t_ili2db_dataset
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument

---

### arp_naturschutzobjekte_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_naturschutzobjekte_pub`

**Quell-Tabellen:**
- arp_naturschutzobjekte_v1.amphibienstandort
- arp_naturschutzobjekte_v1.blaue_flaechen_grenchen
- arp_naturschutzobjekte_v1.flachmoor
- arp_naturschutzobjekte_v1.flechte
- arp_naturschutzobjekte_v1.karch_objekt
- arp_naturschutzobjekte_v1.moos

---

### arp_nutzungsplanung_delete_dataset

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_delete_dataset`

---

### arp_nutzungsplanung_digizone_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_digizone_pub`

---

### arp_nutzungsplanung_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_import`

**Quell-Tabellen:**
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_import_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_import_v1.rechtsvorschrften_hinweisweiteredokumente
- arp_nutzungsplanung_import_v1.t_ili2db_basket
- arp_nutzungsplanung_import_v1.t_ili2db_dataset
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument_entscheid_sbv
- arp_nutzungsplanung_transfer_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_v1.t_ili2db_dataset
- x

**Ziel-Tabellen:**
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_transfer_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_v1.t_ili2db_dataset

---

### arp_nutzungsplanung_import_ersterfassung

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_import_ersterfassung`

**Quell-Tabellen:**
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_import_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_import_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_import_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_import_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_import_v1.rechtsvorschrften_hinweisweiteredokumente
- arp_nutzungsplanung_import_v1.t_ili2db_basket
- arp_nutzungsplanung_import_v1.t_ili2db_dataset
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument_entscheid_sbv
- arp_nutzungsplanung_transfer_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_v1.t_ili2db_dataset
- x

**Ziel-Tabellen:**
- Geometrie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_transfer_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_v1.t_ili2db_dataset

---

### arp_nutzungsplanung_kanton_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_kanton_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_export_v1.t_ili2db_basket
- arp_nutzungsplanung_export_v1.t_ili2db_dataset
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_ep_typ_kanton_erschliessung_linienobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_kanton_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_np_typ_kanton_grundnutzung
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_flaeche
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_linie
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_punkt
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_kanton_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_kanton_v1.rechtsvorschrften_dokument_entscheid_sbv
- arp_nutzungsplanung_kanton_v1.t_ili2db_basket
- arp_nutzungsplanung_kanton_v1.t_ili2db_dataset
- arp_nutzungsplanung_mgdm_v1.catalogue_ch_catalogue_ch
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_geometrie_dokument
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_grundnutzung_zonenflaeche
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_linienbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_objektbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_dokument
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_kt
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_ueberlagernde_festlegung
- arp_nutzungsplanung_mgdm_v1.localisedblob
- arp_nutzungsplanung_mgdm_v1.localisedtext
- arp_nutzungsplanung_mgdm_v1.localiseduri
- arp_nutzungsplanung_mgdm_v1.multilingualblob
- arp_nutzungsplanung_mgdm_v1.multilingualtext
- arp_nutzungsplanung_mgdm_v1.multilingualuri
- arp_nutzungsplanung_mgdm_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_mgdm_v1.t_ili2db_basket
- arp_nutzungsplanung_mgdm_v1.t_ili2db_dataset
- arp_nutzungsplanung_mgdm_v1.transfermetadaten_amt
- arp_nutzungsplanung_mgdm_v1.transfermetadaten_datenbestand
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset

**Ziel-Tabellen:**
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_export_v1.t_ili2db_basket
- arp_nutzungsplanung_export_v1.t_ili2db_dataset
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_linienbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_objektbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_kt
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_ueberlagernde_festlegung
- arp_nutzungsplanung_mgdm_v1.localiseduri
- arp_nutzungsplanung_mgdm_v1.multilingualuri
- arp_nutzungsplanung_mgdm_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset

---

### arp_nutzungsplanung_planregister_pub_alles

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_planregister_pub_alles`

**Quell-Tabellen:**
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_dokument
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_rechtsvorschriftgwsareal
- afu_gewaesserschutz_zonen_areale_v1.gwszonen_rechtsvorschriftgwszone
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_naturreservate.reservate_dokument
- arp_naturreservate.reservate_reservat
- arp_naturreservate.reservate_reservat_dokument
- arp_nutzungsplanung_kanton_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_kanton_v1.rechtsvorschrften_dokument_entscheid_sbv
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument
- arp_nutzungsplanung_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_v1.rechtsvorschrften_dokument_entscheid_sbv
- awjf_statische_waldgrenze.dokumente_dokument
- awjf_statische_waldgrenze.geobasisdaten_typ
- awjf_statische_waldgrenze.geobasisdaten_typ_dokument

---

### arp_nutzungsplanung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_nutzungsplanung_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_laermempfindlichkeit_zonenflaeche
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_typ
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_typ_dokument
- arp_laermempfindlichkeitsstufen_mgdm_v1.localiseduri
- arp_laermempfindlichkeitsstufen_mgdm_v1.multilingualuri
- arp_laermempfindlichkeitsstufen_mgdm_v1.rechtsstatus
- arp_laermempfindlichkeitsstufen_mgdm_v1.rechtsvorschrften_dokument
- arp_laermempfindlichkeitsstufen_mgdm_v1.t_ili2db_basket
- arp_laermempfindlichkeitsstufen_mgdm_v1.t_ili2db_dataset
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_export_v1.t_ili2db_basket
- arp_nutzungsplanung_export_v1.t_ili2db_dataset
- arp_nutzungsplanung_kanton_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_linie
- arp_nutzungsplanung_mgdm_v1.catalogue_ch_catalogue_ch
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_geometrie_dokument
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_grundnutzung_zonenflaeche
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_linienbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_objektbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_dokument
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_kt
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_ueberlagernde_festlegung
- arp_nutzungsplanung_mgdm_v1.localisedblob
- arp_nutzungsplanung_mgdm_v1.localisedtext
- arp_nutzungsplanung_mgdm_v1.localiseduri
- arp_nutzungsplanung_mgdm_v1.multilingualblob
- arp_nutzungsplanung_mgdm_v1.multilingualtext
- arp_nutzungsplanung_mgdm_v1.multilingualuri
- arp_nutzungsplanung_mgdm_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_mgdm_v1.t_ili2db_basket
- arp_nutzungsplanung_mgdm_v1.t_ili2db_dataset
- arp_nutzungsplanung_mgdm_v1.transfermetadaten_amt
- arp_nutzungsplanung_mgdm_v1.transfermetadaten_datenbestand
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset
- arp_nutzungsplanung_v1.erschlssngsplnung_ep_typ_kanton_erschliessung_linienobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_v1.laermmpfhktsstfen_empfindlichkeitsstufe
- arp_nutzungsplanung_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe
- arp_nutzungsplanung_v1.laermmpfhktsstfen_typ_empfindlichkeitsstufe_dokument
- arp_nutzungsplanung_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_v1.nutzungsplanung_np_typ_kanton_grundnutzung
- arp_nutzungsplanung_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_flaeche
- arp_nutzungsplanung_v1.nutzungsplanung_np_typ_kanton_ueberlagernd_punkt
- arp_nutzungsplanung_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_v1.rechtsvorschrften_dokument_entscheid_sbv
- arp_nutzungsplanung_v1.t_ili2db_basket
- arp_nutzungsplanung_v1.t_ili2db_dataset
- arp_planungszonen_mgdm_v1.geobasisdaten_planungszone
- arp_planungszonen_mgdm_v1.geobasisdaten_typ_planungszone
- arp_planungszonen_mgdm_v1.localiseduri
- arp_planungszonen_mgdm_v1.multilingualuri
- arp_planungszonen_mgdm_v1.rechtsstatus
- arp_planungszonen_mgdm_v1.rechtsvorschrften_dokument
- arp_planungszonen_mgdm_v1.t_ili2db_basket
- arp_planungszonen_mgdm_v1.t_ili2db_dataset
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_typ
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_typ_dokument
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_waldabstand_linie
- arp_waldabstandslinien_mgdm_v1.localiseduri
- arp_waldabstandslinien_mgdm_v1.multilingualuri
- arp_waldabstandslinien_mgdm_v1.rechtsstatus
- arp_waldabstandslinien_mgdm_v1.rechtsvorschrften_dokument
- arp_waldabstandslinien_mgdm_v1.t_ili2db_basket
- arp_waldabstandslinien_mgdm_v1.t_ili2db_dataset

**Ziel-Tabellen:**
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_laermempfindlichkeit_zonenflaeche
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_typ
- arp_laermempfindlichkeitsstufen_mgdm_v1.geobasisdaten_typ_dokument
- arp_laermempfindlichkeitsstufen_mgdm_v1.localiseduri
- arp_laermempfindlichkeitsstufen_mgdm_v1.multilingualuri
- arp_laermempfindlichkeitsstufen_mgdm_v1.rechtsvorschrften_dokument
- arp_laermempfindlichkeitsstufen_mgdm_v1.t_ili2db_dataset
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_flaechenobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_linienobjekt_dokument
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt
- arp_nutzungsplanung_export_v1.erschlssngsplnung_typ_erschliessung_punktobjekt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_grundnutzung_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_flaeche_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_linie_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.nutzungsplanung_typ_ueberlagernd_punkt_dokument
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_export_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_export_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_export_v1.t_ili2db_basket
- arp_nutzungsplanung_export_v1.t_ili2db_dataset
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_grundnutzung_zonenflaeche
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_linienbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_objektbezogene_festlegung
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_dokument
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_typ_kt
- arp_nutzungsplanung_mgdm_v1.geobasisdaten_ueberlagernde_festlegung
- arp_nutzungsplanung_mgdm_v1.localiseduri
- arp_nutzungsplanung_mgdm_v1.multilingualuri
- arp_nutzungsplanung_mgdm_v1.rechtsvorschrften_dokument
- arp_nutzungsplanung_mgdm_v1.t_ili2db_dataset
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_empfindlichkeitsstufe
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_flaechenobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_linienobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_erschliessung_punktobjekt
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_grundnutzung
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_flaeche
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_linie
- arp_nutzungsplanung_transfer_pub_v1.nutzungsplanung_ueberlagernd_punkt
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_basket
- arp_nutzungsplanung_transfer_pub_v1.t_ili2db_dataset
- arp_planungszonen_mgdm_v1.geobasisdaten_planungszone
- arp_planungszonen_mgdm_v1.geobasisdaten_typ_planungszone
- arp_planungszonen_mgdm_v1.localiseduri
- arp_planungszonen_mgdm_v1.multilingualuri
- arp_planungszonen_mgdm_v1.rechtsvorschrften_dokument
- arp_planungszonen_mgdm_v1.t_ili2db_dataset
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_typ
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_typ_dokument
- arp_waldabstandslinien_mgdm_v1.geobasisdaten_waldabstand_linie
- arp_waldabstandslinien_mgdm_v1.localiseduri
- arp_waldabstandslinien_mgdm_v1.multilingualuri
- arp_waldabstandslinien_mgdm_v1.rechtsvorschrften_dokument
- arp_waldabstandslinien_mgdm_v1.t_ili2db_dataset

---

### arp_richtplan_inventar_historische_verkehrswege_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_richtplan_inventar_historische_verkehrswege_pub`

**Quell-Tabellen:**
- arp_inventar_historische_verkehrswege_v1.ivs_inventarkarte_ivs_linienobjekte_lv95
- arp_inventar_historische_verkehrswege_v1.ivs_inventarkarte_ivs_signatur_linie
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie

---

### arp_richtplan_richtplan_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_richtplan_richtplan_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_richtplan_pub_v2.detailkarten_flaeche
- arp_richtplan_pub_v2.detailkarten_linie
- arp_richtplan_pub_v2.detailkarten_punkt
- arp_richtplan_pub_v2.raumkonzept_flaeche
- arp_richtplan_pub_v2.raumkonzept_linie
- arp_richtplan_pub_v2.raumkonzept_punkt
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie
- arp_richtplan_pub_v2.richtplankarte_ueberlagernder_punkt
- arp_richtplan_v2.detailkarten_anpassung
- arp_richtplan_v2.detailkarten_flaeche
- arp_richtplan_v2.detailkarten_linie
- arp_richtplan_v2.detailkarten_punkt
- arp_richtplan_v2.raumkonzept_anpassung
- arp_richtplan_v2.raumkonzept_flaeche
- arp_richtplan_v2.raumkonzept_linie
- arp_richtplan_v2.raumkonzept_punkt
- arp_richtplan_v2.richtplankarte_anpassung
- arp_richtplan_v2.richtplankarte_dokument
- arp_richtplan_v2.richtplankarte_ueberlagernde_flaeche
- arp_richtplan_v2.richtplankarte_ueberlagernde_flaeche_dokument
- arp_richtplan_v2.richtplankarte_ueberlagernde_linie
- arp_richtplan_v2.richtplankarte_ueberlagernde_linie_dokument
- arp_richtplan_v2.richtplankarte_ueberlagernder_punkt
- arp_richtplan_v2.richtplankarte_ueberlagernder_punkt_dokument

---

### arp_sein_konfiguration_local

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_sein_konfiguration_local`

**Quell-Tabellen:**
- ST_Read
- Shapefile
- arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- duckdb_settings
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gemeinde
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gemeinde_objektinfo
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_gruppe
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_objektinfo
- editdb.arp_sein_konfiguration_grundlagen_v2.grundlagen_thema
- importschema_xtf.geometrie
- importschema_xtf.geometrie_linie
- importschema_xtf.geometrie_perimeter
- importschema_xtf.geometrie_punkt
- importschema_xtf.geometriekollektion
- importschema_xtf.hinweis
- importschema_xtf.hinweisortsbildteil
- importschema_xtf.ivs_linienobjekte_lv95
- importschema_xtf.ivs_objekte
- importschema_xtf.ivs_slanamen
- main.
- main.sein_sammeltabelle
- main.sein_sammeltabelle_filtered
- pubdb.ada_archaeologie_pub_v1.public_flaechenfundstelle_siedlungsgebiet
- pubdb.ada_archaeologie_pub_v1.public_punktfundstelle_siedlungsgebiet
- pubdb.afu_altlasten_pub_v2.belasteter_standort
- pubdb.afu_stoerfallverordnung_pub_v1.betrieb
- pubdb.afu_stoerfallverordnung_pub_v1.betrieb_kb
- pubdb.afu_stoerfallverordnung_pub_v1.durchgangsstrasse
- pubdb.afu_stoerfallverordnung_pub_v1.durchgangsstrasse_kb
- pubdb.afu_stoerfallverordnung_pub_v1.erdgasroehrenspeicher
- pubdb.afu_stoerfallverordnung_pub_v1.erdgasroehrenspeicher_kb
- pubdb.afu_stoerfallverordnung_pub_v1.nationalstrasse
- pubdb.afu_stoerfallverordnung_pub_v1.nationalstrasse_kb
- pubdb.agi_hoheitsgrenzen_pub.hoheitsgrenzen_bezirksgrenze
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_flaeche
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_linie
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_massnahme_punkt
- pubdb.arp_agglomerationsprogramme_pub.agglomrtnsprgrmme_uebersicht_gemeinde
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernde_flaeche
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernde_linie
- pubdb.arp_richtplan_pub_v2.richtplankarte_ueberlagernder_punkt
- pubdb.awjf_wildtierkorridore_pub_v1.wildtierkorridor
- read_parquet
- sein.arp_sein_konfiguration_grundlagen_v2.gemeinde_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115auswertung_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gruppe
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_thema
- sein.main.sein_sammeltabelle
- sein.main.sein_sammeltabelle_filtered
- sein_sammeltabelle
- sein_sammeltabelle_filtered
- themeDB.main.sein_sammeltabelle

**Ziel-Tabellen:**
- Sammeltabelle
- for
- main.sein_sammeltabelle_filtered
- sein.arp_sein_konfiguration_grundlagen_v2.gemeinde_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115auswertung_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gemeinde
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_gruppe
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_objektinfo
- sein.arp_sein_konfiguration_grundlagen_v2.so_rp_s0250115grundlagen_thema
- sein.main.sein_sammeltabelle
- sein.main.sein_sammeltabelle_filtered
- sein_sammeltabelle
- sein_sammeltabelle_filtered

---

### arp_statent_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_statent_import`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_statpop_statent_staging_v1.nutzungszonen
- arp_statpop_statent_staging_v1.statent

---

### arp_statpop_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_statpop_import`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_nutzungsplanung_pub_v1.nutzungsplanung_grundnutzung
- arp_statpop_statent_staging_v1.nutzungszonen
- arp_statpop_statent_staging_v1.statpop

---

### arp_statpopent_hektarraster

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_statpopent_hektarraster`

**Quell-Tabellen:**
- employees_total

---

### arp_waldreservate_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_waldreservate_pub`

**Quell-Tabellen:**
- arp_waldreservate_mgdm_v1.mcpfe_class_catalogue
- arp_waldreservate_mgdm_v1.waldreservat
- arp_waldreservate_mgdm_v1.waldreservat_teilobjekt
- arp_waldreservate_pub_v1.rechtsstatus
- arp_waldreservate_pub_v1.waldreservat_mcpfe_code
- arp_waldreservate_v1.dokumente_dokument
- arp_waldreservate_v1.geobasisdaten_waldreservat
- arp_waldreservate_v1.geobasisdaten_waldreservat_dokument
- arp_waldreservate_v1.geobasisdaten_waldreservat_teilobjekt

**Ziel-Tabellen:**
- arp_waldreservate_mgdm_v1.waldreservat
- arp_waldreservate_mgdm_v1.waldreservat_teilobjekt
- arp_waldreservate_pub_v1.waldreservat

---

### arp_wanderwege_import_xtf

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_wanderwege_import_xtf`

**Quell-Tabellen:**
- arp_wanderwege_v1.hpm_base_base_geometry
- arp_wanderwege_v1.hpm_base_metadata
- arp_wanderwege_v1.hpm_base_route
- arp_wanderwege_v1.hpm_base_route_signalisation
- arp_wanderwege_v1.hpm_base_way_route
- arp_wanderwege_v1.hpm_catalogues_direction_of_signalisation
- arp_wanderwege_v1.hpm_catalogues_hiking_segment_type
- arp_wanderwege_v1.hpm_catalogues_hpm_catalog_item
- arp_wanderwege_v1.hpm_catalogues_hpm_route_type
- arp_wanderwege_v1.hpm_catalogues_hpm_type
- arp_wanderwege_v1.hpm_catalogues_location_category
- arp_wanderwege_v1.hpm_catalogues_mtb_segment_type
- arp_wanderwege_v1.hpm_catalogues_obliging_authorities
- arp_wanderwege_v1.hpm_catalogues_obliging_land_owner
- arp_wanderwege_v1.hpm_catalogues_public_transport_section
- arp_wanderwege_v1.hpm_catalogues_quality_of_way
- arp_wanderwege_v1.hpm_catalogues_route_category
- arp_wanderwege_v1.hpm_catalogues_route_type
- arp_wanderwege_v1.hpm_catalogues_state
- arp_wanderwege_v1.hpm_catalogues_surface
- arp_wanderwege_v1.hpm_walk_lv95_hiking_way
- arp_wanderwege_v1.hpm_walk_lv95_signalisation
- arp_wanderwege_v1.hpm_walk_lv95_way

---

### arp_wanderwege_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_wanderwege_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_kantonsgrenze
- arp_wanderwege_v1.hpm_base_metadata
- arp_wanderwege_v1.hpm_base_route
- arp_wanderwege_v1.hpm_base_route_signalisation
- arp_wanderwege_v1.hpm_base_way_route
- arp_wanderwege_v1.hpm_catalogues_direction_of_signalisation
- arp_wanderwege_v1.hpm_catalogues_hiking_segment_type
- arp_wanderwege_v1.hpm_catalogues_location_category
- arp_wanderwege_v1.hpm_catalogues_surface
- arp_wanderwege_v1.hpm_walk_lv95_hiking_way
- arp_wanderwege_v1.hpm_walk_lv95_signalisation

**Ziel-Tabellen:**
- arp_wanderwege_pub_v1.wanderwege_signalisation

---

### arp_wildruhezonen_export_ai

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/arp_wildruhezonen_export_ai`

---

### avt_ausnahmetransportrouten_export_ai

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_ausnahmetransportrouten_export_ai`

---

### avt_groblaermkataster_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_groblaermkataster_pub`

---

### avt_gvm_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_gvm_import`

**Quell-Tabellen:**
- avt_gesamtverkehrsmodell_2019_pub_v1.klasse_dtv

**Ziel-Tabellen:**
- avt_gesamtverkehrsmodell_2019_pub_v1.miv_verkehrsdichte_2019
- avt_gesamtverkehrsmodell_2019_pub_v1.miv_verkehrsdichte_prognose_2030
- avt_gesamtverkehrsmodell_2019_pub_v1.miv_verkehrsdichte_prognose_2040

---

### avt_kantonsstrassen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_kantonsstrassen_pub`

**Quell-Tabellen:**
- avt_kantonsstrassen_staging_v1.achse
- avt_kantonsstrassen_staging_v1.bezugspunkt
- avt_kantonsstrassen_staging_v1.signalisierte_geschwindigkeit

---

### avt_kunstbauten_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_kunstbauten_pub`

**Quell-Tabellen:**
- avt_kunstbauten_staging_v1.kunstbaute

---

### avt_mehrjahresplanung_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_mehrjahresplanung_pub`

**Quell-Tabellen:**
- avt_kantonsstrassen_pub_v1.achse
- avt_kantonsstrassen_pub_v1.bezugspunkt
- avt_mehrjahresplanung_v2.kantonsstrassen_achse
- avt_mehrjahresplanung_v2.kantonsstrassen_bezugspunkt
- avt_mehrjahresplanung_v2.projekte_projekt
- avt_mehrjahresplanung_v2.projekte_projektgeometrie

**Ziel-Tabellen:**
- avt_mehrjahresplanung_v2.projekte_projekt
- avt_mehrjahresplanung_v2.projekte_projektgeometrie

---

### avt_oeffentlicher_verkehr_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_oeffentlicher_verkehr_pub`

**Quell-Tabellen:**
- avt_oeffentlicher_verkehr.oeffntlchr_vrkehr_haltestelle
- avt_oeffentlicher_verkehr.oeffntlchr_vrkehr_netz

---

### avt_oev_gueteklassen_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_oev_gueteklassen_import`

---

### avt_oevkov

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_oevkov`

**Quell-Tabellen:**
- avt_oevkov_

**Ziel-Tabellen:**
- avt_oevkov_

---

### avt_strassenlaerm

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_strassenlaerm`

**Quell-Tabellen:**
- avt_strassenlaerm_v1.codelisten_exposure_limit_value_catalogue
- avt_strassenlaerm_v1.codelisten_operation_status_catalogue
- avt_strassenlaerm_v1.codelisten_pointofdetermination_catalogue
- avt_strassenlaerm_v1.immission_strasse_dispersion_calculation
- avt_strassenlaerm_v1.immission_strasse_pointofdetermination

---

### avt_strassenzustand_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_strassenzustand_pub`

**Quell-Tabellen:**
- avt_strassenzustand_staging_v1.strassenzustand

**Ziel-Tabellen:**
- avt_strassenzustand_staging_v1.strassenzustand

---

### avt_verkehrszaehlstellen_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/avt_verkehrszaehlstellen_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- avt_verkehrszaehlstellen.verkehrszhlstllen_dokument
- avt_verkehrszaehlstellen.verkehrszhlstllen_verkehrszaehlstelle

---

### awjf_biotopbaeume_import

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_biotopbaeume_import`

**Quell-Tabellen:**
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotopbaum_import

**Ziel-Tabellen:**
- awjf_programm_biodiversitaet_wald_v1.biodiversitt_wald_biotopbaum

---

### awjf_gesuchsteller

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_gesuchsteller`

**Quell-Tabellen:**
- awjf_gesuchsteller.gesuchsteller_gesuchsteller

---

### awjf_gewaesser_fischerei_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_gewaesser_fischerei_pub`

**Quell-Tabellen:**
- afu_gewaesser_v1.fischrevierabschnitt_v

---

### awjf_jagdreviere_jagdbanngebiete_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_jagdreviere_jagdbanngebiete_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_jagdreviere_jagdbanngebiete_v1.jagdbanngebiete_jagdbanngebiete
- awjf_jagdreviere_jagdbanngebiete_v1.jagdbanngebiete_jagdbanngebiete_art
- awjf_jagdreviere_jagdbanngebiete_v1.jagdreviere_hegering
- awjf_jagdreviere_jagdbanngebiete_v1.jagdreviere_jagdreviere

---

### awjf_rodung_rodungsersatz_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_rodung_rodungsersatz_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_forstreviere.forstreviere_forstkreis
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_rodung_rodungsersatz_v1.ausgleichsabgabe
- awjf_rodung_rodungsersatz_v1.dokument
- awjf_rodung_rodungsersatz_v1.flaeche
- awjf_rodung_rodungsersatz_v1.flaeche_ersatzmassnahmennl
- awjf_rodung_rodungsersatz_v1.flaeche_massnahmennl_typ
- awjf_rodung_rodungsersatz_v1.geometrie_objekttyp
- awjf_rodung_rodungsersatz_v1.punkt
- awjf_rodung_rodungsersatz_v1.rodung_dokument
- awjf_rodung_rodungsersatz_v1.rodungsdaten
- awjf_rodung_rodungsersatz_v1.rodungsdaten_art_bewilligungsverfahren
- awjf_rodung_rodungsersatz_v1.rodungsdaten_ersatzverzicht
- awjf_rodung_rodungsersatz_v1.rodungsdaten_rodungszweck
- awjf_rodung_rodungsersatz_v1.verfahrensstatus

---

### awjf_samenerntekataster_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_samenerntekataster_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_forstreviere.forstreviere_forstkreis
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_samenerntekataster_v1.flaeche

---

### awjf_seltene_baeume_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_seltene_baeume_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_forstreviere.forstreviere_forstkreis
- awjf_forstreviere.forstreviere_forstrevier
- awjf_forstreviere.forstreviere_forstreviergeometrie
- awjf_seltene_baeume.seltene_baumarten_baumtyp
- awjf_seltene_baeume.seltene_baumarten_beziehung_pflanzung_baumtyp
- awjf_seltene_baeume.seltene_baumarten_freistellung
- awjf_seltene_baeume.seltene_baumarten_pflanzung

---

### awjf_silvaprotect_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_silvaprotect_pub`

**Quell-Tabellen:**
- awjf_silvaprotect_v1.silvaprotect_andere_kt
- awjf_silvaprotect_v1.silvaprotect_gerinne
- awjf_silvaprotect_v1.silvaprotect_lawine
- awjf_silvaprotect_v1.silvaprotect_rutschung
- awjf_silvaprotect_v1.silvaprotect_steinschlag

---

### awjf_statische_waldgrenze_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_statische_waldgrenze_pub`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- arp_nutzungsplanung_planregister_pub_v1.planregister_dokument
- awjf_statische_waldgrenze.dokumente_dokument
- awjf_statische_waldgrenze.geobasisdaten_typ
- awjf_statische_waldgrenze.geobasisdaten_typ_dokument
- awjf_statische_waldgrenze.geobasisdaten_waldgrenze_linie
- awjf_statische_waldgrenze_staging_v1.t_ili2db_basket
- awjf_statische_waldgrenze_staging_v1.t_ili2db_dataset
- awjf_statische_waldgrenze_staging_v1.waldgrenze_art_waldgrenze
- awjf_statische_waldgrenze_staging_v1.waldgrenze_dokument
- awjf_statische_waldgrenze_staging_v1.waldgrenze_planungsart
- awjf_statische_waldgrenze_staging_v1.waldgrenze_rechtsstatus
- awjf_statische_waldgrenze_staging_v1.waldgrenze_verbindlichkeit
- awjf_statische_waldgrenze_staging_v1.waldgrenze_waldgrenze

---

### awjf_wald_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_wald_pub`

**Quell-Tabellen:**
- awjf_wald_oberhoehenbonitaet_v1.oberhoehenbonitaet
- awjf_wald_oberhoehenbonitaet_v1.oberhoehenbonitaet_oberhoehenbonitaets_code
- awjf_waldstandorte_v1.waldstandort

---

### awjf_waldpflege_kontrolle_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldpflege_kontrolle_pub`

**Quell-Tabellen:**
- awjf_waldpflege_kontrolle.waldpflege_waldpflege

---

### awjf_waldplan_bestandeskarte_import_shp

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldplan_bestandeskarte_import_shp`

---

### awjf_waldplan_bestandeskarte_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldplan_bestandeskarte_pub`

**Quell-Tabellen:**
- agi_dm01avso24.bodenbedeckung_boflaeche
- awjf_waldplan_bestandeskarte_staging_v1.waldplan_bestandeskarte
- awjf_waldplan_bestandeskarte_v1.waldplan_bestandeskarte

---

### awjf_waldplan_bestandeskarte_staging

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldplan_bestandeskarte_staging`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- awjf_waldplan_bestandeskarte_staging_v1.waldplan_bestandeskarte
- awjf_waldplan_bestandeskarte_v1.waldplan_bestandeskarte

---

### awjf_waldplan_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldplan_pub`

**Quell-Tabellen:**
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_mopublic_pub.mopublic_grundstueck
- awjf_schutzwald_v1.schutzwald
- awjf_statische_waldgrenze.geobasisdaten_waldgrenze_linie
- awjf_waldplan_bestandeskarte_v1.waldplan_bestandeskarte
- awjf_waldplan_pub_v2.t_ili2db_basket
- awjf_waldplan_pub_v2.t_ili2db_dataset
- awjf_waldplan_pub_v2.waldplan_schutzwald
- awjf_waldplan_pub_v2.waldplan_waldfunktion
- awjf_waldplan_pub_v2.waldplan_waldnutzung
- awjf_waldplan_pub_v2.waldplan_waldplan_grundstueck
- awjf_waldplan_pub_v2.waldplan_walduebersicht
- awjf_waldplan_v2.art_hauptgefahrenpotential
- awjf_waldplan_v2.biodiversitaetstyp
- awjf_waldplan_v2.forstkreise
- awjf_waldplan_v2.intensitaetsstufe
- awjf_waldplan_v2.objekte_schutzwald
- awjf_waldplan_v2.t_ili2db_basket
- awjf_waldplan_v2.t_ili2db_dataset
- awjf_waldplan_v2.waldeigentuemer
- awjf_waldplan_v2.waldfunktionskategorie
- awjf_waldplan_v2.waldnutzungskategorie
- awjf_waldplan_v2.waldplan_schutzwald
- awjf_waldplan_v2.waldplan_waldeigentum
- awjf_waldplan_v2.waldplan_waldfunktion
- awjf_waldplan_v2.waldplan_waldnutzung
- awjf_waldplan_v2.waldplan_waldplantyp
- awjf_waldplan_v2.waldplancatalgues_forstrevier
- awjf_waldplan_v2.waldplankatalog_forstbetrieb
- awjf_waldplan_v2.waldplankatalog_forstrevier
- awjf_waldplan_v2.wirtschaftszonen
- biodiversitaet_objekt_flaechen_berechnet
- grundstuecke
- grundstuecke_berechnung
- hiebsatzrelevante_waldflaechen_grundstueck
- hiebsatzrelevante_waldflaechen_grundstueck_json
- position
- produktive_waldflaechen
- produktive_waldflaechen_grundstueck
- waldflaeche_grundstueck
- waldflaechen_berechnet
- waldfunktion
- waldfunktion_flaechen_berechnet
- waldnutzung
- waldnutzung_flaechen_berechnet
- walduebersicht_cleaned_geometry
- walduebersicht_union_geometry
- wytweideflaechen_berechnet

**Ziel-Tabellen:**
- Fl
- awjf_waldplan_pub_v2.t_ili2db_basket
- awjf_waldplan_pub_v2.t_ili2db_dataset
- awjf_waldplan_pub_v2.waldplan_schutzwald
- awjf_waldplan_pub_v2.waldplan_waldfunktion
- awjf_waldplan_pub_v2.waldplan_waldnutzung
- awjf_waldplan_pub_v2.waldplan_waldplan_grundstueck
- awjf_waldplan_pub_v2.waldplan_walduebersicht
- awjf_waldplan_v2.t_ili2db_basket
- awjf_waldplan_v2.t_ili2db_dataset
- awjf_waldplan_v2.waldplan_schutzwald
- awjf_waldplan_v2.waldplan_waldeigentum
- awjf_waldplan_v2.waldplan_waldfunktion
- awjf_waldplan_v2.waldplan_waldnutzung
- awjf_waldplan_v2.waldplankatalog_forstbetrieb
- awjf_waldplan_v2.waldplankatalog_forstrevier
- biodiversitaet_objekt_flaechen_berechnet
- grundstuecke
- grundstuecke_berechnung
- hiebsatzrelevante_waldflaechen_grundstueck
- produktive_waldflaechen
- produktive_waldflaechen_grundstueck
- waldflaeche_grundstueck
- waldflaechen_berechnet
- waldfunktion
- waldfunktion_flaechen_berechnet
- waldnutzung
- waldnutzung_flaechen_berechnet
- walduebersicht_cleaned_geometry
- walduebersicht_union_geometry
- wytweideflaechen_berechnet

---

### awjf_waldplan_pub_erstimport

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldplan_pub_erstimport`

**Quell-Tabellen:**
- agi_dm01avso24.gemeindegrenzen_gemeinde
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- agi_mopublic_pub.mopublic_grundstueck
- awjf_schutzwald_v1.schutzwald
- awjf_statische_waldgrenze.geobasisdaten_waldgrenze_linie
- awjf_waldplan_bestandeskarte_v1.waldplan_bestandeskarte
- awjf_waldplan_pub_v2.t_ili2db_basket
- awjf_waldplan_pub_v2.t_ili2db_dataset
- awjf_waldplan_pub_v2.waldplan_schutzwald
- awjf_waldplan_pub_v2.waldplan_waldfunktion
- awjf_waldplan_pub_v2.waldplan_waldnutzung
- awjf_waldplan_pub_v2.waldplan_waldplan_grundstueck
- awjf_waldplan_pub_v2.waldplan_walduebersicht
- awjf_waldplan_v2.art_hauptgefahrenpotential
- awjf_waldplan_v2.biodiversitaetstyp
- awjf_waldplan_v2.forstkreise
- awjf_waldplan_v2.intensitaetsstufe
- awjf_waldplan_v2.objekte_schutzwald
- awjf_waldplan_v2.t_ili2db_basket
- awjf_waldplan_v2.t_ili2db_dataset
- awjf_waldplan_v2.waldeigentuemer
- awjf_waldplan_v2.waldfunktionskategorie
- awjf_waldplan_v2.waldnutzungskategorie
- awjf_waldplan_v2.waldplan_schutzwald
- awjf_waldplan_v2.waldplan_waldeigentum
- awjf_waldplan_v2.waldplan_waldfunktion
- awjf_waldplan_v2.waldplan_waldnutzung
- awjf_waldplan_v2.waldplankatalog_forstbetrieb
- awjf_waldplan_v2.waldplankatalog_forstrevier
- awjf_waldplan_v2.wirtschaftszonen
- biodiversitaet_objekt_flaechen_berechnet
- grundstuecke
- grundstuecke_berechnung
- hiebsatzrelevante_waldflaechen_grundstueck
- jsonb_array_elements
- position
- produktive_waldflaechen
- produktive_waldflaechen_grundstueck
- waldflaeche_grundstueck
- waldflaechen_berechnet
- waldfunktion
- waldfunktion_flaechen_berechnet
- waldnutzung
- waldnutzung_flaechen_berechnet
- walduebersicht_cleaned_geometry
- walduebersicht_union_geometry
- wytweideflaechen_berechnet

**Ziel-Tabellen:**
- Fl
- awjf_waldplan_pub_v2.t_ili2db_basket
- awjf_waldplan_pub_v2.t_ili2db_dataset
- awjf_waldplan_pub_v2.waldplan_schutzwald
- awjf_waldplan_pub_v2.waldplan_waldfunktion
- awjf_waldplan_pub_v2.waldplan_waldnutzung
- awjf_waldplan_pub_v2.waldplan_waldplan_grundstueck
- awjf_waldplan_pub_v2.waldplan_walduebersicht
- awjf_waldplan_v2.t_ili2db_basket
- awjf_waldplan_v2.t_ili2db_dataset
- awjf_waldplan_v2.waldplan_schutzwald
- awjf_waldplan_v2.waldplan_waldeigentum
- awjf_waldplan_v2.waldplan_waldfunktion
- awjf_waldplan_v2.waldplan_waldnutzung
- awjf_waldplan_v2.waldplankatalog_forstbetrieb
- awjf_waldplan_v2.waldplankatalog_forstrevier
- biodiversitaet_objekt_flaechen_berechnet
- calculated_values
- differences
- grundstuecke
- grundstuecke_berechnung
- hiebsatzrelevante_waldflaechen_grundstueck
- produktive_waldflaechen
- produktive_waldflaechen_grundstueck
- waldflaeche_grundstueck
- waldflaechen_berechnet
- waldfunktion
- waldfunktion_flaechen_berechnet
- waldnutzung
- waldnutzung_flaechen_berechnet
- walduebersicht_cleaned_geometry
- walduebersicht_union_geometry
- wytweideflaechen_berechnet

---

### awjf_waldportal

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldportal`

---

### awjf_waldwanderwege_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_waldwanderwege_pub`

**Quell-Tabellen:**
- awjf_waldwanderwege.waldwanderwege_posten
- awjf_waldwanderwege.waldwanderwege_wanderwege

---

### awjf_wildtiersensible_gebiete_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/awjf_wildtiersensible_gebiete_pub`

**Quell-Tabellen:**
- awjf_wildtiersensible_gebiete_v1.wildtrsnsbl_gbete_fokus_typ
- awjf_wildtiersensible_gebiete_v1.wildtrsnsbl_gbete_gebiet

---

### hba_gebaeude_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/hba_gebaeude_pub`

**Quell-Tabellen:**
- agi_dm01avso24.bodenbedeckung_boflaeche
- agi_dm01avso24.bodenbedeckung_gebaeudenummer
- agi_dm01avso24.einzelobjekte_einzelobjekt
- agi_dm01avso24.einzelobjekte_flaechenelement
- agi_dm01avso24.einzelobjekte_objektnummer
- hba_gebaeude_v2.gebaeude_gebaeude

---

### hba_gebaeude_pub_v2

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/hba_gebaeude_pub_v2`

---

### hba_grundstuecke_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/hba_grundstuecke_pub`

**Quell-Tabellen:**
- agi_dm01avso24.liegenschaften_grundstueck
- agi_dm01avso24.liegenschaften_liegenschaft
- agi_dm01avso24.liegenschaften_selbstrecht
- hba_grundstuecke_v2.grundstuecke_grundstueck

---

### hba_grundstuecke_pub_v2

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/hba_grundstuecke_pub_v2`

---

### ksta_landwert_pub

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/ksta_landwert_pub`

**Quell-Tabellen:**
- ksta_landwerte.landwerte_landwert

---

### sk_plakatstandorte

**Status:** Aktiv
**Trigger:** manual
**Pfad:** `../gretljobs/sk_plakatstandorte`

**Quell-Tabellen:**
- agi_hoheitsgrenzen_pub.hoheitsgrenzen_gemeindegrenze
- sk_plakatstandorte_staging_v1.standorte
- sk_plakatstandorte_v1.standorte

**Ziel-Tabellen:**
- sk_plakatstandorte_staging_v1.standorte

---
