<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:mns="https://my.webiste/someNamespace">
<xsl:output method='html' encoding='UTF-8' indent='yes'/>

<xsl:template match="Poems">
    <html>
        <head>
            <title>存着的古诗</title>
			<link rel="stylesheet" href="poems.css" type="text/css" />
        </head>
        <body>
            <h2>存着的古诗</h2>
            <div id="container">
                <xsl:for-each select="Poem">

                <div class="poem-wrapper">

                    <div class="poem-title">
                        <h3>
                            <xsl:value-of select="Title"/>
                        </h3>
                    </div>
					
					<div class="poem-author">
						<p>
                            <xsl:value-of select="Author/Dynasty"/> · <xsl:value-of select="Author/Name"/>
                        </p>
					</div>
					
					<div class="poem-verses">
						<xsl:for-each select="Verses/Verse">
							<xsl:value-of select="."/>
							<xsl:value-of select="@end"/>
							<xsl:if test="@end='。'">
								<br />
							</xsl:if>
						</xsl:for-each>
					</div>

                </div>

                </xsl:for-each>
            </div>
        </body>
    </html>
</xsl:template>



</xsl:stylesheet>