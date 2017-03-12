                                <?php 
                                    include 'header.php';                                       // Template-Kopf und Navigation
                                ?>
                                <!----------------------------------------------------------------------------------------Was eben hier hin kommt ...-->
                                <?php 
                                    // wenn nichts anderes ausgewählt wurde, ist Stündlich ausgewählt
                                    if (isset ($_GET['diagram_mode'])) {
                                        $diagram_mode = $_GET['diagram_mode'];
                                    }else{
                                        $diagram_mode = 'hourly';
                                    }

                                ?>
                                <h2 class="art-postheader"><?php echo _('Diagramme'); ?></h2>
                                <div class="hg_container" style="margin-bottom: 20px; margin-top: 20px;">
                                    <table style="width: 100%;">
                                        <tr>
                                            <td><img src="images/hourly_30x30.png" alt=""></td>
                                            <td><img src="images/daily_30x30.png" alt=""></td>
                                            <td><img src="images/weekly_30x30.png" alt=""></td>
                                            <td><img src="images/monthly_30x30.png" alt=""></td>
                                        </tr>
                                        <tr>
                                            <td><a href="diagrams.php?diagram_mode=hourly" class="art-button"><?php echo _('Stunde'); ?></a></td>
                                            <td><a href="diagrams.php?diagram_mode=daily" class="art-button"><?php echo _('Tag'); ?></a></td>
                                            <td><a href="diagrams.php?diagram_mode=weekly" class="art-button"><?php echo _('Woche'); ?></a></td>
                                            <td><a href="diagrams.php?diagram_mode=monthly" class="art-button"><?php echo _('Monat'); ?></a></td>
                                        </tr>
                                    </table>
                                </div>

                                    <div style="">
                                    <h2><?php echo _('Temperaturverlauf'); ?> </h2>
                                    <img src="/pic/pi-ager_sensortemp-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Luftfeuchtigkeitsverlauf'); ?></h2>
                                    <img src="/pic/pi-ager_sensorhum-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Kuehlung'); ?></h2>
                                    <img src="/pic/pi-ager_cool-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Heizung'); ?></h2>
                                    <img src="/pic/pi-ager_heat-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Befeuchtung'); ?></h2>
                                    <img src="/pic/pi-ager_lbf-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Luftumwaelzung'); ?></h2>
                                    <img src="/pic/pi-ager_uml-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    <h2><?php echo _('Luftaustausch'); ?></h2>
                                    <img src="/pic/pi-ager_lat-<?php echo $diagram_mode; ?>.png" alt="<?php echo $diagram_mode; ?>" />
                                    </div>
                                <!----------------------------------------------------------------------------------------Ende! ...-->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <?php 
            include 'footer.php';
        ?>
